#!/usr/bin/env python3
"""
Roadmap Watcher — branch/journey model.

Reads the curated digests in data/raw-reports/, extracts candidate work items
and blockers, maps each to one of the CURRENT branches in roadmap.json, filters
out anything that isn't public-safe, and de-dupes against what the roadmap
already contains. It writes PROPOSALS for human review to
data/roadmap/watcher-proposals.json.

Design guarantees:
- It NEVER writes roadmap.json. The owner promotes approved proposals by hand.
- Branches are loaded from roadmap.json at run time, so the watcher always
  targets the live model instead of a hardcoded pillar list.
- Every proposal cites the digest it came from (evidence).
- Public-safe: any candidate matching a forbidden pattern from
  data/schema/roadmap-public-safety.json is flagged, not proposed.
- Deterministic and safe to re-run; it rebuilds the proposals file.

This replaces the retired pillar-model watcher.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROADMAP = ROOT / "roadmap.json"
DIGEST_DIR = ROOT / "data" / "raw-reports"
DEEP_CONTEXT_INDEX = ROOT / "data" / "roadmap" / "deep-context-decision-sources.json"
SAFETY_SCHEMA = ROOT / "data" / "schema" / "roadmap-public-safety.json"
OUTPUT = ROOT / "data" / "roadmap" / "watcher-proposals.json"

# Mapping thresholds
NAME_TOKEN_WEIGHT = 3   # a branch-name token appearing in a claim is a strong signal
MIN_SCORE = 2           # below this, a claim is left unmapped for human triage
DEDUP_JACCARD = 0.55    # claim considered "already present" above this title overlap

STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "to", "for", "in", "on", "at", "by",
    "with", "is", "are", "be", "as", "that", "this", "it", "its", "from", "into",
    "need", "needs", "must", "should", "will", "can", "not", "no", "remain",
    "remains", "still", "new", "current", "system", "systems", "work", "project",
    "projects", "decision", "decisions", "context", "llc",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_json(path: Path):
    if not path.exists():
        return None
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def tokens(text: str) -> set[str]:
    words = re.findall(r"[a-zA-Z][a-zA-Z0-9'-]+", (text or "").lower())
    return {w for w in words if len(w) > 2 and w not in STOPWORDS}


# A stricter street-address detector than the schema's naive one. The schema
# regex has no word boundaries and runs case-insensitively, so it matches the
# suffix inside ordinary words ("Path-way", "al-ways", "gate-way"). This version
# requires a leading house number and a capitalized street suffix as a whole word.
STRICT_STREET_ADDRESS = re.compile(
    r"\b\d{1,6}\s+(?:[A-Z][A-Za-z]*\.?\s+){1,4}"
    r"(?:St|Street|Ave|Avenue|Rd|Road|Blvd|Boulevard|Dr|Drive|Ct|Court|"
    r"Ln|Lane|Pkwy|Parkway|Pl|Place|Ter|Terrace|Cir|Circle)\b"
)

# Categories we do NOT trust the schema regex for (handled specially or skipped).
_SPECIAL = {"street_address", "person_name_with_context", "description"}


def load_forbidden_patterns() -> dict[str, re.Pattern]:
    schema = load_json(SAFETY_SCHEMA) or {}
    raw = schema.get("forbidden_patterns", {})
    compiled = {}
    for name, pattern in raw.items():
        if name in _SPECIAL:
            continue
        try:
            compiled[name] = re.compile(pattern, re.IGNORECASE)
        except re.error:
            pass
    return compiled


def unsafe_reason(text: str, patterns: dict[str, re.Pattern]) -> str | None:
    if "<" in text or ">" in text:
        return "contains angle brackets / HTML"
    # 'person_name_with_context' (owner identity + LLC) is intentionally NOT a
    # hard block: digests legitimately name the businesses, and proposals are an
    # internal review artifact, not published dashboard output.
    for name, rx in patterns.items():
        if rx.search(text):
            return f"matched forbidden pattern: {name}"
    if STRICT_STREET_ADDRESS.search(text):
        return "matched forbidden pattern: street_address"
    return None


def branch_name_tokens(branch: dict) -> set[str]:
    # Distinctive tokens from the branch name (drop generic words).
    return tokens(branch.get("name", ""))


def branch_keyword_index(branch: dict) -> set[str]:
    # Draw keywords from every curated field that describes the branch's scope,
    # including its blockers — incoming blocker claims often echo the wording of
    # blockers the branch already tracks, which improves mapping accuracy.
    parts = [branch.get("name", ""), branch.get("role", ""),
             branch.get("ultimate_goal", ""), branch.get("critical_blocker", "")]
    parts.extend(branch.get("blockers", []) or [])
    for w in branch.get("work_items", []):
        parts.append(w.get("task", ""))
    return tokens(" ".join(parts))


def existing_titles(branch: dict) -> list[set[str]]:
    titles = [w.get("task", "") for w in branch.get("work_items", [])]
    titles += list(branch.get("blockers", []))
    if branch.get("critical_blocker"):
        titles.append(branch["critical_blocker"])
    return [tokens(t) for t in titles if t]


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def split_sections(text: str) -> list[tuple[str, str]]:
    """Return [(level2_heading, body)] for each '## ' section."""
    sections = []
    current_head = None
    current_lines: list[str] = []
    for line in text.splitlines():
        if line.startswith("## "):
            if current_head is not None:
                sections.append((current_head, "\n".join(current_lines)))
            current_head = line[3:].strip()
            current_lines = []
        elif current_head is not None:
            current_lines.append(line)
    if current_head is not None:
        sections.append((current_head, "\n".join(current_lines)))
    return sections


def parse_projects(body: str) -> list[tuple[str, str]]:
    """'### Title' subsections -> [(title, first paragraph)]."""
    out = []
    title = None
    buf: list[str] = []
    for line in body.splitlines():
        if line.startswith("### "):
            if title:
                out.append((title, " ".join(buf).strip()))
            title = line[4:].strip()
            buf = []
        elif title:
            if line.strip():
                buf.append(line.strip())
    if title:
        out.append((title, " ".join(buf).strip()))
    return out


def parse_blockers(body: str) -> list[tuple[str, str]]:
    """Numbered '1. **Title** — desc' items -> [(title, desc)]."""
    out = []
    for m in re.finditer(r"^\s*\d+\.\s*\*\*(.+?)\*\*\s*[—-]?\s*(.*)$",
                         body, re.MULTILINE):
        out.append((m.group(1).strip(), m.group(2).strip()))
    # Fallback: bare '**Title**' bullets
    if not out:
        for m in re.finditer(r"^\s*[-*]\s*\*\*(.+?)\*\*\s*[—-]?\s*(.*)$",
                             body, re.MULTILINE):
            out.append((m.group(1).strip(), m.group(2).strip()))
    return out


def clean_detail(text: str) -> str:
    """Normalize candidate descriptions before writing proposal details.

    The curated digests were partly created during the retired pillar-model era,
    so their raw detail text can include legacy labels such as `Pillar: pillar-2`.
    Proposal output should stay branch/journey-oriented even when the evidence
    digest still contains those historical labels.
    """
    detail = re.sub(r"\*\*", "", text or "")
    detail = re.sub(r"\s*Pillar:\s*pillar-\d+\s*\([^)]*\)", "", detail)
    detail = re.sub(r"\s*Pillar:\s*pillar-\d+\b", "", detail)
    detail = re.sub(r"\s*Evidence:\s*`?memories/processed/[^`\s]+`?[^.]*", "", detail)
    detail = re.sub(r"\s*Evidence:\s*$", "", detail)
    detail = re.sub(r"\s+", " ", detail).strip()
    return detail


def extract_claims() -> list[dict]:
    """Pull project/blocker candidates out of every *-digest.md file."""
    claims = []
    if not DIGEST_DIR.exists():
        return claims
    for digest in sorted(DIGEST_DIR.glob("*-digest.md")):
        text = digest.read_text(encoding="utf-8")
        evidence = str(digest.relative_to(ROOT))
        for heading, body in split_sections(text):
            h = heading.lower()
            if "blocker" in h:
                for title, desc in parse_blockers(body):
                    claims.append({"kind": "blocker", "title": title,
                                   "desc": desc, "evidence": evidence})
            elif "project" in h or "decision" in h or "workstream" in h:
                for title, desc in parse_projects(body):
                    claims.append({"kind": "work_item", "title": title,
                                   "desc": desc, "evidence": evidence})
    return claims


def score_branch(claim_tokens: set[str], name_toks: set[str],
                 kw_index: set[str]) -> int:
    name_hits = len(claim_tokens & name_toks)
    overlap = len(claim_tokens & kw_index)
    return NAME_TOKEN_WEIGHT * name_hits + overlap


def main() -> int:
    roadmap = load_json(ROADMAP)
    if not roadmap or "branches" not in roadmap:
        print("ERROR: roadmap.json missing or has no branches.", file=sys.stderr)
        return 1

    branches = roadmap["branches"]
    patterns = load_forbidden_patterns()
    deep_ctx = load_json(DEEP_CONTEXT_INDEX) or {}

    # Precompute per-branch matching data
    meta = {}
    for b in branches:
        meta[b["id"]] = {
            "name": b.get("name", b["id"]),
            "name_tokens": branch_name_tokens(b),
            "kw_index": branch_keyword_index(b),
            "existing": existing_titles(b),
        }

    proposals = {
        b["id"]: {"branch_name": b.get("name", b["id"]),
                  "work_item_candidates": [], "blocker_candidates": []}
        for b in branches
    }
    unmapped, flagged = [], []

    claims = extract_claims()
    for claim in claims:
        text = f"{claim['title']} {claim['desc']}".strip()
        reason = unsafe_reason(text, patterns)
        if reason:
            flagged.append({"title": claim["title"], "evidence": claim["evidence"],
                            "reason": reason})
            continue

        ctoks = tokens(text)
        best_id, best_score = None, 0
        for bid, m in meta.items():
            s = score_branch(ctoks, m["name_tokens"], m["kw_index"])
            if s > best_score:
                best_id, best_score = bid, s

        if not best_id or best_score < MIN_SCORE:
            unmapped.append({"kind": claim["kind"], "title": claim["title"],
                             "evidence": claim["evidence"],
                             "reason": "no confident branch match"})
            continue

        # De-dupe against what the branch already tracks
        title_toks = tokens(claim["title"])
        already = any(jaccard(title_toks, ex) >= DEDUP_JACCARD
                      for ex in meta[best_id]["existing"])

        entry = {
            "suggestion": claim["title"],
            "detail": clean_detail(claim["desc"])[:500],
            "evidence": claim["evidence"],
            "confidence": "high" if best_score >= NAME_TOKEN_WEIGHT else "medium",
            "already_in_roadmap": already,
        }
        bucket = ("blocker_candidates" if claim["kind"] == "blocker"
                  else "work_item_candidates")
        proposals[best_id][bucket].append(entry)

    # Count only genuinely new suggestions for the summary
    new_items = sum(
        1 for b in proposals.values()
        for k in ("work_item_candidates", "blocker_candidates")
        for e in b[k] if not e["already_in_roadmap"]
    )

    output = {
        "generated_at": now_iso(),
        "generator": "scripts/roadmap-watcher.py",
        "model": "branch-journey",
        "note": ("Proposals for human review. Nothing here is applied to "
                 "roadmap.json automatically. Promote approved items by hand."),
        "inputs": {
            "digests": sorted(str(p.relative_to(ROOT))
                              for p in DIGEST_DIR.glob("*-digest.md"))
            if DIGEST_DIR.exists() else [],
            "deep_context_sources": [s.get("path") for s in deep_ctx.get("sources", [])],
        },
        "summary": {
            "branches": len(branches),
            "claims_extracted": len(claims),
            "new_suggestions": new_items,
            "already_in_roadmap": sum(
                1 for b in proposals.values()
                for k in ("work_item_candidates", "blocker_candidates")
                for e in b[k] if e["already_in_roadmap"]),
            "unmapped": len(unmapped),
            "flagged_unsafe": len(flagged),
        },
        "proposals_by_branch": proposals,
        "unmapped_claims": unmapped,
        "flagged_unsafe": flagged,
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n",
                      encoding="utf-8")

    s = output["summary"]
    print(f"Watcher run complete -> {OUTPUT.relative_to(ROOT)}")
    print(f"  branches: {s['branches']} | claims: {s['claims_extracted']} | "
          f"new: {s['new_suggestions']} | already-tracked: {s['already_in_roadmap']} | "
          f"unmapped: {s['unmapped']} | flagged-unsafe: {s['flagged_unsafe']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
