# Roadmap Watcher — Guide

The watcher turns curated evidence into **proposed** roadmap updates for you to
review. It never edits `roadmap.json` — you promote what you approve by hand.

This is the current **branch/journey-model** watcher. The older pillar-model
watcher it replaces is retired.

## What it does

`scripts/roadmap-watcher.py`:

1. Loads the **current branches** from `roadmap.json` (so it always targets the
   live model — no hardcoded list).
2. Reads the curated digests in `data/raw-reports/*-digest.md`.
3. Extracts candidate **work items** (from "Projects/Decisions" sections) and
   **blockers** (from "Blockers" sections).
4. Maps each candidate to the best-matching branch (branch-name tokens weigh
   heavily, plus keyword overlap).
5. **Public-safe filter:** anything matching a forbidden pattern from
   `data/schema/roadmap-public-safety.json` (email, phone, SSN, card, API key,
   real street address, HTML) is flagged, not proposed.
6. **De-dupes** against what each branch already tracks, so proposals are
   genuinely new (existing ones are marked `already_in_roadmap: true`).
7. Writes proposals to `data/roadmap/watcher-proposals.json`.

## How to run

```bash
python3 scripts/roadmap-watcher.py
```

Deterministic and safe to re-run — it rebuilds the proposals file. Requires
only the Python standard library.

## The output

`data/roadmap/watcher-proposals.json`:

- `summary` — counts (claims, new suggestions, already-tracked, unmapped, flagged).
- `proposals_by_branch` — for each branch, `work_item_candidates` and
  `blocker_candidates`, each with a `suggestion`, `detail`, `evidence` (which
  digest it came from), `confidence`, and `already_in_roadmap`.
- `unmapped_claims` — candidates with no confident branch match (triage by hand).
- `flagged_unsafe` — candidates withheld for public-safety review.

## Two ways progress reaches the roadmap

The watcher is **not** a reality-sync. It only reads the curated digests in
`data/raw-reports/` — it cannot see your Google Drive, your website, or your work
outside those files. So there are two paths, and both end at the same safe
**promote** step:

- **Path A — evidence-based (watcher).** The watcher proposes candidates from the
  digests. You approve the good ones.
- **Path B — real-world progress (the watcher can't see).** Things like "I filed
  my taxes," "the site is updated," "these docs now exist." You (or an AI helper)
  describe them directly.

Both paths are applied with the **promote helper**, which writes into
`roadmap.json` for you — assigning IDs, enforcing the enums, and validating (with
rollback) so the roadmap can never end up broken or unsafe.

## The promote helper

`scripts/promote-proposals.py` reads a small file you control —
`data/roadmap/promotions.json` — and applies it to `roadmap.json`. It supports
three kinds of change:

```json
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
```

Run it:

```bash
python3 scripts/promote-proposals.py --dry-run   # preview; writes nothing
python3 scripts/promote-proposals.py             # apply
```

Guarantees:

- **All-or-nothing.** If any entry is invalid it refuses and changes nothing.
- **Auto-IDs.** New work items get the next id for the branch (`dh-13`, `cb-5`, …).
- **Enum-checked.** `status` ∈ {not_started, in_progress, blocked, completed,
  moved_later}; `priority` ∈ {CRITICAL, HIGH, MEDIUM, LOW}.
- **Validated with rollback.** It runs `validate-roadmap.py`; if that fails
  (including the public-safety/PII scan), `roadmap.json` is restored untouched.
- **No double-apply.** On success it resets `promotions.json` to the empty template.

## The full workflow (human in the loop)

**Path A — from the watcher:**
1. `python3 scripts/roadmap-watcher.py` — regenerate proposals.
2. `python3 scripts/prioritize-proposals.py` — rank them into
   `data/roadmap/proposal-backlog.md`.
3. Read the backlog. For each item you approve, add an entry to
   `promotions.json` (`add_work_items` / `add_blockers`) — in your own clean words.

**Path B — real-world progress:**
1. Just describe it in `promotions.json` — most often a `set_status` (mark an
   existing item `completed`/`in_progress`) or a new work item/blocker.

**Then, for both:**
4. `python3 scripts/promote-proposals.py --dry-run` to preview, then run it for real.
5. If you added a **new work item**, the validator may warn it isn't referenced by
   any journey milestone. That's a nudge, not an error — wire it into a milestone's
   `step_ids` (or a 30/60/90 window) by hand if it belongs on the timeline.
6. Review `git diff roadmap.json`, log the change in `CHANGELOG.md`, and commit.
   The live dashboard/timeline pick it up on the next load.

The watcher proposes; the promote helper applies safely; you always decide what
gets in.
