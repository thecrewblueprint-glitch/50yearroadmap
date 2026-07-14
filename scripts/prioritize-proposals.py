#!/usr/bin/env python3
"""
Prioritize watcher proposals into a "work-on-first" backlog.

Reads (never modifies) data/roadmap/watcher-proposals.json and roadmap.json,
ranks the NEW candidates (already_in_roadmap == false), and writes a
human-readable report to data/roadmap/proposal-backlog.md.

Ranking is driven by the owner's own plan so it reflects real priority:

1. Operating window — which 30/60/90 window the candidate's branch belongs to
   (derived from thirty_sixty_ninety.focus_step_ids). Earlier window = higher.
   Branches not in any window fall back to phase order (Phase 1 before Phase 2).
2. Blockers before work items within a window (blockers gate progress).
3. Confidence (high before medium) as a tiebreaker, then title A-Z.

This DELETES NOTHING. It is a read-only view over the proposals; re-run it any
time the proposals change.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

_STOP = {"the", "a", "an", "and", "or", "of", "to", "for", "in", "on", "with",
         "is", "are", "be", "as", "that", "this", "system", "systems", "llc",
         "deadhang", "new", "need", "needs", "still"}


def toks(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z][a-z0-9'/-]+", (text or "").lower())
            if len(w) > 2 and w not in _STOP}


def containment(a: set[str], b: set[str]) -> float:
    """Share of a's tokens present in b."""
    return len(a & b) / len(a) if a else 0.0

ROOT = Path(__file__).resolve().parents[1]
ROADMAP = ROOT / "roadmap.json"
PROPOSALS = ROOT / "data" / "roadmap" / "watcher-proposals.json"
OUTPUT = ROOT / "data" / "roadmap" / "proposal-backlog.md"

TOP_N = 12  # size of the "Work on these first" shortlist


def load(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def window_for_branches(roadmap: dict) -> dict[str, dict]:
    """Map each branch id -> its earliest 30/60/90 window (order, label)."""
    branches = roadmap.get("branches", [])
    item_branch = {}
    for b in branches:
        for w in b.get("work_items", []):
            item_branch[w["id"]] = b["id"]

    mapping: dict[str, dict] = {}
    windows = (roadmap.get("thirty_sixty_ninety") or {}).get("windows", [])
    for order, win in enumerate(windows):
        for sid in win.get("focus_step_ids", []):
            bid = item_branch.get(sid)
            if bid and bid not in mapping:
                mapping[bid] = {"order": order, "label": win.get("label", f"Window {order+1}")}
    return mapping


def branch_tier(bid: str, roadmap: dict, win_map: dict) -> tuple[int, str]:
    """Return (sort_rank, human_label) for a branch's priority tier."""
    if bid in win_map:
        return win_map[bid]["order"], win_map[bid]["label"]
    branch = next((b for b in roadmap.get("branches", []) if b["id"] == bid), {})
    # Not in a 30/60/90 window: order after the windows, by phase.
    base = 100
    if branch.get("lifecycle") == "future" or branch.get("phase") == 2:
        return base + 10, "Later (Phase 2)"
    return base, "Phase 1 (unscheduled)"


def main() -> int:
    roadmap = load(ROADMAP)
    proposals = load(PROPOSALS)
    win_map = window_for_branches(roadmap)
    branch_name = {b["id"]: b.get("name", b["id"]) for b in roadmap.get("branches", [])}

    # The branch you're currently on (the "you are here" milestone's area) leads
    # its window tier — that's where the owner is actually working right now.
    journey = roadmap.get("journey", {})
    here_ms = next((m for m in journey.get("milestones", [])
                    if m.get("id") == journey.get("you_are_here")), {})
    current_branch = here_ms.get("area_branch_id")

    # Existing roadmap items (per branch) as token sets, so we can hide
    # candidates that are effectively already covered even if the watcher's
    # title-only dedup missed them (e.g. a reworded promotion).
    existing_tokens: dict[str, list[set[str]]] = {}
    for b in roadmap.get("branches", []):
        sets = [toks(w.get("task", "")) for w in b.get("work_items", [])]
        sets += [toks(x) for x in b.get("blockers", [])]
        if b.get("critical_blocker"):
            sets.append(toks(b["critical_blocker"]))
        existing_tokens[b["id"]] = [s for s in sets if s]

    rows = []
    covered_count = 0
    for bid, bucket in proposals.get("proposals_by_branch", {}).items():
        tier_rank, tier_label = branch_tier(bid, roadmap, win_map)
        for kind, key in (("blocker", "blocker_candidates"),
                          ("work item", "work_item_candidates")):
            for e in bucket.get(key, []):
                if e.get("already_in_roadmap"):
                    continue
                # Hide candidates whose meaning is already in the roadmap.
                ctoks = toks(e.get("suggestion", ""))
                if ctoks and any(containment(ctoks, ex) >= 0.6
                                 for ex in existing_tokens.get(bid, [])):
                    covered_count += 1
                    continue
                rows.append({
                    "branch_id": bid,
                    "branch": branch_name.get(bid, bid),
                    "kind": kind,
                    "tier_rank": tier_rank,
                    "tier": tier_label,
                    "branch_priority": 0 if bid == current_branch else 1,
                    "is_blocker": kind == "blocker",
                    "confidence": e.get("confidence", "medium"),
                    "suggestion": e.get("suggestion", ""),
                    "detail": e.get("detail", ""),
                    "evidence": e.get("evidence", "").split("/")[-1],
                })

    conf_rank = {"high": 0, "medium": 1, "low": 2}
    rows.sort(key=lambda r: (
        r["tier_rank"],                       # 30 -> 60 -> 90 -> later
        r["branch_priority"],                 # the branch you're on leads its tier
        r["branch"],                          # then group by branch
        0 if r["is_blocker"] else 1,          # blockers (gates) before work items
        conf_rank.get(r["confidence"], 3),    # higher confidence first
        r["suggestion"].lower(),
    ))
    for i, r in enumerate(rows, 1):
        r["rank"] = i

    # ---- write the report ----
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    lines = [
        "# Proposal Backlog — Work-On-First Order",
        "",
        f"_Generated {now} by `scripts/prioritize-proposals.py`. "
        "Read-only view over the watcher proposals — nothing is deleted._",
        "",
        "Ranked by your own 30/60/90 windows (earliest first), blockers before "
        "work items, then confidence. Promote deliberately; this is a queue, not "
        "a to-do dump.",
        "",
        f"**{len(rows)} open candidates** shown"
        + (f" ({covered_count} more look already-covered and were hidden)."
           if covered_count else ".")
        + " Full evidence — including every proposal, nothing deleted — lives in "
        "`data/roadmap/watcher-proposals.json`.",
        "",
        "## ⭐ Work on these first",
        "",
    ]
    for r in rows[:TOP_N]:
        tag = "🚧 blocker" if r["is_blocker"] else "work"
        lines.append(f"{r['rank']}. **{r['suggestion']}**  \n"
                     f"   _{r['branch']} · {r['tier']} · {tag} · {r['confidence']} confidence_")
    lines.append("")

    # Grouped full backlog by tier
    lines.append("## Full backlog by window")
    current_tier = None
    for r in rows:
        if r["tier"] != current_tier:
            current_tier = r["tier"]
            lines.append("")
            lines.append(f"### {current_tier}")
            lines.append("")
        tag = "🚧" if r["is_blocker"] else "•"
        lines.append(f"- {tag} **{r['suggestion']}** — {r['branch']} "
                     f"({r['confidence']}) · _{r['evidence']}_")
    lines.append("")

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # ---- console summary ----
    print(f"Backlog ranked -> {OUTPUT.relative_to(ROOT)}")
    print(f"  {len(rows)} open candidates. Top {min(TOP_N, len(rows))}:")
    for r in rows[:TOP_N]:
        flag = "BLOCKER" if r["is_blocker"] else "work   "
        print(f"  {r['rank']:>2}. [{flag}] {r['tier']:<16} {r['suggestion'][:56]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
