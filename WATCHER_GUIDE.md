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

## The review workflow (human in the loop)

1. Run the watcher.
2. Open `data/roadmap/watcher-proposals.json`. Skim each branch's candidates
   where `already_in_roadmap` is `false`.
3. For anything worth keeping, add it to the matching branch's `work_items` or
   `blockers` in `roadmap.json` — in your own words, with a proper `id`.
4. Check `unmapped_claims` for anything important that needs a home.
5. Validate `roadmap.json` (see `AGENTS.md` §4) and log the change in
   `CHANGELOG.md`.

The watcher proposes; you decide. Nothing reaches the live dashboard until you
put it in `roadmap.json` yourself.
