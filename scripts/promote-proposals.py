#!/usr/bin/env python3
"""
Promote helper — safely apply approved roadmap updates.

The watcher only PROPOSES (writes data/roadmap/watcher-proposals.json); it never
edits roadmap.json. This helper is the human-in-the-loop "apply" step: you record
the updates you approve in data/roadmap/promotions.json, then run this script and
it writes them into roadmap.json — assigning IDs, enforcing the enums, and
validating the result (rolling back if anything is wrong).

It handles BOTH update paths:
  1. Evidence-based items you approved from the watcher backlog.
  2. Real-world progress the watcher can't see (Drive, website, "I filed taxes")
     — you describe it the same way.

promotions.json supports three kinds of change:

  {
    "set_status": { "dh-6": "completed", "dh-2": "in_progress" },

    "add_work_items": [
      { "branch_id": "deadhang-labor",
        "task": "Register for AZ TPT before merch sales",
        "why": "Selling tangible goods triggers AZ transaction privilege tax",
        "priority": "MEDIUM",
        "status": "not_started" }
    ],

    "add_blockers": [
      { "branch_id": "production-atlas", "text": "Scenic dataset still incomplete" }
    ]
  }

Rules:
- status must be one of: not_started, in_progress, blocked, completed, moved_later
- priority must be one of: CRITICAL, HIGH, MEDIUM, LOW
- new work-item IDs are assigned automatically (dh-13, cb-5, ...)
- nothing is applied unless EVERY entry is valid AND the validator passes
- on success, promotions.json is reset to an empty template so nothing is
  applied twice. Review `git diff roadmap.json`, then commit.

Usage:
  python3 scripts/promote-proposals.py            # apply
  python3 scripts/promote-proposals.py --dry-run  # preview only, write nothing
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROADMAP = ROOT / "roadmap.json"
PROMOTIONS = ROOT / "data" / "roadmap" / "promotions.json"
VALIDATOR = ROOT / "scripts" / "validate-roadmap.py"

WORK_STATUS = {"not_started", "in_progress", "blocked", "completed", "moved_later"}
PRIORITIES = {"CRITICAL", "HIGH", "MEDIUM", "LOW"}

EMPTY_TEMPLATE = {
    "_README": (
        "Record approved roadmap updates here, then run "
        "`python3 scripts/promote-proposals.py`. On success this file is reset. "
        "See WATCHER_GUIDE.md for the full workflow."
    ),
    "set_status": {},
    "add_work_items": [],
    "add_blockers": [],
}


def fail(msg: str) -> "NoReturn":  # type: ignore[name-defined]
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as e:
        fail(f"{path.relative_to(ROOT)} is not valid JSON: {e}")


def write_roadmap(data) -> None:
    ROADMAP.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                       encoding="utf-8")


def branch_map(roadmap) -> dict:
    return {b["id"]: b for b in roadmap.get("branches", [])}


def id_prefix(branch) -> str:
    """Derive the id prefix (e.g. 'dh') from a branch's existing work items."""
    for w in branch.get("work_items", []) or []:
        wid = w.get("id", "")
        if "-" in wid:
            return wid.rsplit("-", 1)[0]
    # Fallback: initials of the branch id (deadhang-labor -> dl)
    return "".join(part[0] for part in branch["id"].split("-") if part)


def next_id(branch) -> str:
    prefix = id_prefix(branch)
    nums = []
    for w in branch.get("work_items", []) or []:
        wid = w.get("id", "")
        if wid.startswith(prefix + "-"):
            tail = wid[len(prefix) + 1:]
            if tail.isdigit():
                nums.append(int(tail))
    return f"{prefix}-{(max(nums) + 1) if nums else 1}"


def all_work_item_ids(roadmap) -> dict:
    ids = {}
    for b in roadmap.get("branches", []):
        for w in b.get("work_items", []) or []:
            ids[w["id"]] = b["id"]
    return ids


def main() -> int:
    dry_run = "--dry-run" in sys.argv

    roadmap = load_json(ROADMAP)
    if not roadmap or "branches" not in roadmap:
        fail("roadmap.json missing or has no branches.")

    promo = load_json(PROMOTIONS)
    if promo is None:
        # First run: create the template and stop.
        if not dry_run:
            PROMOTIONS.parent.mkdir(parents=True, exist_ok=True)
            PROMOTIONS.write_text(json.dumps(EMPTY_TEMPLATE, indent=2) + "\n",
                                  encoding="utf-8")
            print(f"Created {PROMOTIONS.relative_to(ROOT)} — fill it in, then re-run.")
        else:
            print("No promotions.json yet (dry-run made no changes).")
        return 0

    set_status = promo.get("set_status") or {}
    add_items = promo.get("add_work_items") or []
    add_blockers = promo.get("add_blockers") or []

    if not set_status and not add_items and not add_blockers:
        print("Nothing to promote (promotions.json is empty). Add entries and re-run.")
        return 0

    branches = branch_map(roadmap)
    existing_ids = all_work_item_ids(roadmap)
    actions: list[str] = []
    errors: list[str] = []

    # --- validate everything up front; apply nothing until all checks pass ---

    # 1. status changes
    for wid, status in set_status.items():
        if wid not in existing_ids:
            errors.append(f"set_status: unknown work-item id '{wid}'")
        if status not in WORK_STATUS:
            errors.append(f"set_status['{wid}']: status must be one of "
                          f"{sorted(WORK_STATUS)} (got {status!r})")

    # 2. new work items
    planned_items = []  # (branch, item_dict)
    for i, it in enumerate(add_items):
        w = f"add_work_items[{i}]"
        bid = it.get("branch_id")
        if bid not in branches:
            errors.append(f"{w}: unknown branch_id {bid!r}")
            continue
        task = (it.get("task") or "").strip()
        why = (it.get("why") or "").strip()
        priority = it.get("priority", "MEDIUM")
        status = it.get("status", "not_started")
        if not task:
            errors.append(f"{w}: 'task' is required")
        if priority not in PRIORITIES:
            errors.append(f"{w}: priority must be one of {sorted(PRIORITIES)} "
                          f"(got {priority!r})")
        if status not in WORK_STATUS:
            errors.append(f"{w}: status must be one of {sorted(WORK_STATUS)} "
                          f"(got {status!r})")
        if not errors:
            planned_items.append((branches[bid],
                                  {"task": task, "why": why,
                                   "priority": priority, "status": status}))

    # 3. new blockers
    planned_blockers = []
    for i, bl in enumerate(add_blockers):
        w = f"add_blockers[{i}]"
        bid = bl.get("branch_id")
        text = (bl.get("text") or "").strip()
        if bid not in branches:
            errors.append(f"{w}: unknown branch_id {bid!r}")
        if not text:
            errors.append(f"{w}: 'text' is required")
        if bid in branches and text:
            planned_blockers.append((branches[bid], text))

    if errors:
        print("Refusing to promote — fix these first:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    # --- apply (in memory) ---
    for wid, status in set_status.items():
        for b in roadmap["branches"]:
            for wk in b.get("work_items", []) or []:
                if wk["id"] == wid:
                    old = wk.get("status")
                    wk["status"] = status
                    actions.append(f"status: {wid} {old} -> {status}")

    for branch, item in planned_items:
        new_id = next_id(branch)  # recomputed per insert so sequential adds don't collide
        item = {"id": new_id, **item}
        branch.setdefault("work_items", []).append(item)
        actions.append(f"work_item: + {new_id} ({branch['id']}) — {item['task']}")

    for branch, text in planned_blockers:
        branch.setdefault("blockers", []).append(text)
        actions.append(f"blocker: + ({branch['id']}) — {text}")

    print("Planned changes:")
    for a in actions:
        print(f"  - {a}")

    if dry_run:
        print("\n--dry-run: no files written.")
        return 0

    # --- write, then validate; roll back on failure ---
    original = ROADMAP.read_text(encoding="utf-8")
    write_roadmap(roadmap)

    result = subprocess.run([sys.executable, str(VALIDATOR)],
                            capture_output=True, text=True)
    if result.returncode != 0:
        ROADMAP.write_text(original, encoding="utf-8")  # rollback
        print("\nValidator FAILED — roadmap.json rolled back, nothing changed.",
              file=sys.stderr)
        print(result.stdout + result.stderr, file=sys.stderr)
        return 1

    # success: reset promotions file so nothing is applied twice
    PROMOTIONS.write_text(json.dumps(EMPTY_TEMPLATE, indent=2) + "\n",
                          encoding="utf-8")

    print(f"\n✓ Applied {len(actions)} change(s). Validator PASS.")
    print("  promotions.json reset. Review `git diff roadmap.json`, then commit.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
