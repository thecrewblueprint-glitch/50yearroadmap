#!/usr/bin/env python3
"""
Validate roadmap.json against the current branch/journey model.

Checks (see AGENTS.md §3-4):
- Valid JSON; required top-level keys present.
- Branches: required fields; status_percentage 0-100; valid lifecycle;
  unique branch ids; unique work-item ids across all branches; valid work-item
  priority/status enums.
- Phases: valid status; branch_ids resolve; every branch is in exactly one phase.
- Journey: you_are_here resolves; milestone ids unique; area_branch_id resolves;
  every step_id resolves to a real work item; valid milestone state enum.
- this_week_focus ids resolve to real work items.
- ecosystem_flow present and non-empty.
- Public-safety: no email/phone/SSN/card/API-key/real-street-address/HTML in any
  string (error); owner personal names surfaced as a warning.

Exit code 0 = pass (warnings allowed), 1 = validation errors (or bad JSON).

Usage:  python3 scripts/validate-roadmap.py [path-to-roadmap.json]
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ROADMAP = ROOT / "roadmap.json"
SAFETY_SCHEMA = ROOT / "data" / "schema" / "roadmap-public-safety.json"

PRIORITIES = {"CRITICAL", "HIGH", "MEDIUM", "LOW"}
WORK_STATUS = {"not_started", "in_progress", "blocked", "completed"}
MILESTONE_STATE = {"current", "upcoming", "done"}
PHASE_STATUS = {"active", "future"}
LIFECYCLE = {"active", "future"}

REQUIRED_TOP = ["branches", "journey", "phases", "this_week_focus",
                "ecosystem_flow", "north_star", "end_goal"]

# Stricter than the schema's naive address regex (avoids matching "way" inside
# "Pathway", "always", etc.). Mirrors the watcher's detector.
STRICT_STREET_ADDRESS = re.compile(
    r"\b\d{1,6}\s+(?:[A-Z][A-Za-z]*\.?\s+){1,4}"
    r"(?:St|Street|Ave|Avenue|Rd|Road|Blvd|Boulevard|Dr|Drive|Ct|Court|"
    r"Ln|Lane|Pkwy|Parkway|Pl|Place|Ter|Terrace|Cir|Circle)\b"
)
OWNER_NAMES = re.compile(r"\b(Aaron|Bowman)\b", re.IGNORECASE)
_SKIP_PATTERNS = {"street_address", "person_name_with_context", "description"}


class Validator:
    def __init__(self):
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.pii_patterns: dict[str, re.Pattern] = {}

    def err(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    # ---- safety patterns ----
    def load_pii_patterns(self) -> None:
        try:
            schema = json.loads(SAFETY_SCHEMA.read_text(encoding="utf-8"))
        except Exception:
            self.warn("Could not load safety schema; PII checks limited to "
                      "address/name heuristics.")
            return
        for name, pattern in schema.get("forbidden_patterns", {}).items():
            if name in _SKIP_PATTERNS:
                continue
            try:
                self.pii_patterns[name] = re.compile(pattern, re.IGNORECASE)
            except re.error:
                pass

    # ---- helpers ----
    @staticmethod
    def walk_strings(node, path="$"):
        if isinstance(node, str):
            yield path, node
        elif isinstance(node, dict):
            for k, v in node.items():
                yield from Validator.walk_strings(v, f"{path}.{k}")
        elif isinstance(node, list):
            for i, v in enumerate(node):
                yield from Validator.walk_strings(v, f"{path}[{i}]")

    # ---- structural checks ----
    def check(self, data: dict) -> None:
        for key in REQUIRED_TOP:
            if key not in data:
                self.err(f"missing required top-level key: '{key}'")

        branches = data.get("branches") or []
        if not isinstance(branches, list) or not branches:
            self.err("'branches' must be a non-empty array")
            branches = branches if isinstance(branches, list) else []

        branch_ids: set[str] = set()
        work_ids: dict[str, str] = {}   # work id -> branch id (for dupe detection)
        for i, b in enumerate(branches):
            where = f"branches[{i}]"
            bid = b.get("id")
            if not bid:
                self.err(f"{where}: missing 'id'")
            else:
                if bid in branch_ids:
                    self.err(f"{where}: duplicate branch id '{bid}'")
                branch_ids.add(bid)
                where = f"branch '{bid}'"

            for field in ("name", "role", "ultimate_goal", "current_state"):
                if not b.get(field):
                    self.warn(f"{where}: missing '{field}'")

            pct = b.get("status_percentage")
            if not isinstance(pct, (int, float)) or not (0 <= pct <= 100):
                self.err(f"{where}: status_percentage must be a number 0-100 (got {pct!r})")

            if b.get("lifecycle") not in LIFECYCLE:
                self.err(f"{where}: lifecycle must be one of {sorted(LIFECYCLE)} (got {b.get('lifecycle')!r})")

            if not isinstance(b.get("blockers", []), list):
                self.err(f"{where}: 'blockers' must be an array")

            for j, w in enumerate(b.get("work_items", []) or []):
                wwhere = f"{where} work_items[{j}]"
                wid = w.get("id")
                if not wid:
                    self.err(f"{wwhere}: missing 'id'")
                elif wid in work_ids:
                    self.err(f"{wwhere}: duplicate work-item id '{wid}' "
                             f"(also in branch '{work_ids[wid]}')")
                else:
                    work_ids[wid] = bid
                if not w.get("task"):
                    self.err(f"{wwhere}: missing 'task'")
                if w.get("priority") not in PRIORITIES:
                    self.err(f"{wwhere}: priority must be one of {sorted(PRIORITIES)} (got {w.get('priority')!r})")
                if w.get("status") not in WORK_STATUS:
                    self.err(f"{wwhere}: status must be one of {sorted(WORK_STATUS)} (got {w.get('status')!r})")

        # ---- phases ----
        phases = data.get("phases") or []
        phase_membership: dict[str, int] = {}
        for i, p in enumerate(phases):
            where = f"phases[{i}]"
            if p.get("status") not in PHASE_STATUS:
                self.err(f"{where}: status must be one of {sorted(PHASE_STATUS)} (got {p.get('status')!r})")
            for bid in p.get("branch_ids", []) or []:
                if bid not in branch_ids:
                    self.err(f"{where}: branch_ids references unknown branch '{bid}'")
                phase_membership[bid] = phase_membership.get(bid, 0) + 1
        for bid in branch_ids:
            count = phase_membership.get(bid, 0)
            if count == 0:
                self.err(f"branch '{bid}' is not listed in any phase")
            elif count > 1:
                self.err(f"branch '{bid}' appears in {count} phases (must be exactly one)")

        # ---- journey ----
        journey = data.get("journey") or {}
        milestones = journey.get("milestones", []) or []
        milestone_ids: set[str] = set()
        for i, m in enumerate(milestones):
            where = f"journey.milestones[{i}]"
            mid = m.get("id")
            if not mid:
                self.err(f"{where}: missing 'id'")
            elif mid in milestone_ids:
                self.err(f"{where}: duplicate milestone id '{mid}'")
            else:
                milestone_ids.add(mid)
                where = f"milestone '{mid}'"
            if not m.get("title"):
                self.err(f"{where}: missing 'title'")
            if m.get("state") not in MILESTONE_STATE:
                self.err(f"{where}: state must be one of {sorted(MILESTONE_STATE)} (got {m.get('state')!r})")
            ab = m.get("area_branch_id")
            if ab and ab not in branch_ids:
                self.err(f"{where}: area_branch_id references unknown branch '{ab}'")
            for sid in m.get("step_ids", []) or []:
                if sid not in work_ids:
                    self.err(f"{where}: step_ids references unknown work item '{sid}'")

        yah = journey.get("you_are_here")
        if yah and yah not in milestone_ids:
            self.err(f"journey.you_are_here '{yah}' does not match any milestone")
        elif not yah:
            self.warn("journey.you_are_here is not set")

        # ---- this_week_focus ----
        twf = data.get("this_week_focus") or {}
        for key in ("priority_1", "priority_2", "priority_3"):
            for tok in str(twf.get(key, "")).split(","):
                tok = tok.strip()
                if tok and tok not in work_ids:
                    self.err(f"this_week_focus.{key} references unknown work item '{tok}'")

        # ---- ecosystem_flow ----
        flow = (data.get("ecosystem_flow") or {}).get("flow")
        if not isinstance(flow, list) or not flow:
            self.warn("ecosystem_flow.flow is empty or missing")

        # ---- advisory: work items not on the journey path ----
        on_path = {sid for m in milestones for sid in (m.get("step_ids") or [])}
        orphan = [w for w in work_ids if w not in on_path]
        if orphan:
            self.warn(f"{len(orphan)} work item(s) not referenced by any milestone: "
                      + ", ".join(sorted(orphan)))

        # ---- public-safety scan over every string ----
        for path, text in self.walk_strings(data):
            for name, rx in self.pii_patterns.items():
                if rx.search(text):
                    self.err(f"public-safety: {path} matches forbidden pattern '{name}'")
            if STRICT_STREET_ADDRESS.search(text):
                self.err(f"public-safety: {path} looks like a street address")
            if OWNER_NAMES.search(text):
                self.warn(f"public-safety: {path} contains an owner personal name "
                          f"(ok if intentional)")
            if "<" in text or ">" in text:
                self.err(f"public-safety: {path} contains angle brackets / HTML")


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_ROADMAP
    v = Validator()
    v.load_pii_patterns()

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"✗ FAIL: {path} not found")
        return 1
    except json.JSONDecodeError as e:
        print(f"✗ FAIL: {path} is not valid JSON — {e}")
        return 1

    v.check(data)

    for w in v.warnings:
        print(f"  ⚠ {w}")
    for e in v.errors:
        print(f"  ✗ {e}")

    if v.errors:
        print(f"\n✗ FAIL — {len(v.errors)} error(s), {len(v.warnings)} warning(s) in {path.name}")
        return 1
    print(f"\n✓ PASS — {path.name} is valid ({len(v.warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
