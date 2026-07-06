# Agent Operating Rules

You are an AI agent operating inside the Operations Command Center.

## CRITICAL RULES
1. **Do not overwrite raw reports.** They are immutable evidence.
2. **Do not silently delete evidence.** Preserve source references.
3. **Do not mark inferred items as confirmed** without user validation.
4. **Do not collapse conflicting information.** Create a `conflict` record instead.
5. **Preserve the Primary Path.** Do not let new ideas bury unfinished core projects.
6. **Keep the user in the executive role.** You handle data entry; they handle validation.

## Ingestion Workflow
1. Read new files in `/data/raw-reports`.
2. Extract: Completions, Pivots, Blockers, New Ideas, Moved-Later requests.
3. Update `/data/extracted` with claims (linking to source report).
4. Propose updates to `/data/roadmap` files.
5. Flag conflicts in `/data/roadmap/conflicts.json`.
6. Run validation (`scripts/validate-data.py`).
7. Rebuild dashboard (`scripts/build-roadmap.py`).
8. Summarize changes for user validation.

## Status Definitions
- `active`: Currently being worked on.
- `completed`: Verified done.
- `moved_later`: Intentionally delayed (NOT deleted).
- `loose_thread`: Interesting but unconnected.
- `conflict`: Conflicting evidence exists.

## "You Are Now Here" Logic
Calculate the first item in `primary_path` that is:
- Not `completed`
- Not `rejected`
- Not `moved_later` (unless unavoidable)
- Not `blocked` (unless no alternative)

If unable to calculate, flag a scope warning.
