#!/usr/bin/env python3
"""
Validate Roadmap Watcher output.

This catches the failure modes found during the July 2026 memory/digest pass:
- empty project proposals despite active digest projects
- blockers mapped only to pillar-7
- Production Atlas active work failing to become the frontier
- missing completed or moved-later proposal buckets
- stale or malformed watcher-proposals.json

Run from repo root:
    python3 scripts/validate-watcher-output.py
"""

import json
import sys
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
PROPOSALS_PATH = ROOT / "data" / "roadmap" / "watcher-proposals.json"
DIGEST_DIR = ROOT / "data" / "raw-reports"

VALID_PILLARS = {f"pillar-{i}" for i in range(1, 9)}
REQUIRED_TOP_LEVEL = {"generated_at", "frontier", "proposals"}
REQUIRED_BUCKETS = {"projects", "tasks", "completed", "moved_later", "blockers", "conflicts"}


def load_json(path: Path) -> Dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def fail(errors: List[str], message: str) -> None:
    errors.append(f"FAIL: {message}")


def warn(warnings: List[str], message: str) -> None:
    warnings.append(f"WARN: {message}")


def count_digest_files() -> int:
    if not DIGEST_DIR.exists():
        return 0
    return len(list(DIGEST_DIR.glob("*-digest.md")))


def validate() -> int:
    errors: List[str] = []
    warnings: List[str] = []

    if not PROPOSALS_PATH.exists():
        fail(errors, f"missing {PROPOSALS_PATH.relative_to(ROOT)}")
        return report(errors, warnings)

    try:
        data = load_json(PROPOSALS_PATH)
    except Exception as exc:
        fail(errors, f"could not parse watcher-proposals.json: {exc}")
        return report(errors, warnings)

    missing_top = REQUIRED_TOP_LEVEL - set(data.keys())
    if missing_top:
        fail(errors, f"watcher-proposals.json missing top-level keys: {sorted(missing_top)}")

    proposals = data.get("proposals")
    if not isinstance(proposals, dict):
        fail(errors, "proposals must be an object")
        return report(errors, warnings)

    missing_buckets = REQUIRED_BUCKETS - set(proposals.keys())
    if missing_buckets:
        fail(errors, f"proposals missing buckets: {sorted(missing_buckets)}")

    for bucket in REQUIRED_BUCKETS:
        if bucket in proposals and not isinstance(proposals[bucket], list):
            fail(errors, f"proposals.{bucket} must be a list")

    digest_count = count_digest_files()
    projects = proposals.get("projects", [])
    completed = proposals.get("completed", [])
    moved_later = proposals.get("moved_later", [])
    blockers = proposals.get("blockers", [])

    if digest_count > 0 and not projects:
        fail(errors, "digest files exist but active project proposals are empty")

    if digest_count > 0 and not blockers:
        fail(errors, "digest files exist but blocker proposals are empty")

    if not completed:
        warn(warnings, "completed proposal bucket is empty; verify this is intended")

    if not moved_later:
        warn(warnings, "moved_later proposal bucket is empty; verify this is intended")

    for bucket_name, records in proposals.items():
        if not isinstance(records, list):
            continue
        for index, record in enumerate(records):
            if not isinstance(record, dict):
                fail(errors, f"{bucket_name}[{index}] is not an object")
                continue
            pillar = record.get("pillar_id")
            if pillar is not None and pillar not in VALID_PILLARS:
                fail(errors, f"{bucket_name}[{index}] has invalid pillar_id: {pillar}")
            title = record.get("title")
            if bucket_name not in {"tasks", "conflicts"} and not title:
                fail(errors, f"{bucket_name}[{index}] missing title")

    blocker_pillars = {record.get("pillar_id") for record in blockers if isinstance(record, dict)}
    if blockers and blocker_pillars == {"pillar-7"}:
        fail(errors, "all blockers are mapped to pillar-7; digest pillar mapping likely failed")

    project_pillars = {record.get("pillar_id") for record in projects if isinstance(record, dict)}
    if "pillar-3" not in project_pillars:
        fail(errors, "Production Atlas active projects are missing from project proposals")

    frontier = data.get("frontier")
    if not isinstance(frontier, dict):
        fail(errors, "frontier must be an object")
    else:
        frontier_pillar = frontier.get("pillar_id")
        if frontier_pillar not in VALID_PILLARS:
            fail(errors, f"frontier has invalid pillar_id: {frontier_pillar}")
        if frontier_pillar != "pillar-3":
            warn(
                warnings,
                "frontier is not Production Atlas; this can be valid later, but verify it is intentional after the July 2026 Atlas-heavy digest pass",
            )
        if frontier.get("active_work", 0) <= 0:
            fail(errors, "frontier active_work must be greater than zero")

    return report(errors, warnings)


def report(errors: List[str], warnings: List[str]) -> int:
    print("ROADMAP WATCHER OUTPUT VALIDATION")
    print("=" * 42)

    if errors:
        for item in errors:
            print(item)
    else:
        print("PASS: no blocking validation errors")

    if warnings:
        print()
        for item in warnings:
            print(item)

    print()
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(validate())
