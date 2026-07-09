# Agent Operating Rules

You are an AI agent operating inside the Operations Command Center.

## CRITICAL RULES

1. **Do not overwrite raw reports.** They are immutable evidence.
2. **Do not silently delete evidence.** Preserve source references.
3. **Do not mark inferred items as confirmed** without user validation.
4. **Do not collapse conflicting information.** Create a `conflict` record instead.
5. **Preserve the Primary Path.** Do not let new ideas bury unfinished core projects.
6. **Keep the user in the executive role.** The agent handles data entry and structure; the user validates direction.
7. **Raw memory dumps are source evidence.** They are expected to feed future digests through `scripts/process-memories.py`, chunk indexes, and curated digest files.
8. **Do not render raw memory dumps in the public roadmap.** Public/dashboard output should use distilled, public-safe roadmap records.
9. **Consult deep context before changing direction.** Files in `data/roadmap-deep-context/` and the index at `data/roadmap/deep-context-decision-sources.json` are decision context for frontier, sequencing, priority, and project-boundary changes.

## Evidence Layers

1. `/memories` — raw imported archives and exports.
2. `/memories/processed` — generated chunks, indexes, and navigation files from raw memory archives.
3. `/data/roadmap-deep-context` — special high-meaning roadmap context that influences direction.
4. `/data/raw-reports` — curated watcher-ready operational digests.
5. `/data/roadmap` — approved state and decision indexes.
6. `/docs` — live GitHub Pages dashboard output.

## Ingestion Workflow

1. Preserve new raw archives in `/memories`.
2. Run or trigger memory processing to create `/memories/processed` chunks and indexes.
3. Review relevant chunks and create curated digest files in `/data/raw-reports`.
4. Store mission/identity/values-heavy roadmap material in `/data/roadmap-deep-context`.
5. Run the watcher to propose updates to `/data/roadmap/watcher-proposals.json`.
6. Promote approved data into `/data/roadmap/projects.json`, `/data/roadmap/tasks.json`, and `/roadmap.json`.
7. Validate and summarize changes for user review.

## Status Definitions

- `active`: Currently being worked on.
- `completed`: Verified done.
- `blocked`: Requires decision, outside input, sequencing, or prerequisite work.
- `moved_later`: Intentionally delayed; preserved, not deleted.
- `loose_thread`: Interesting but not yet connected.
- `conflict`: Conflicting evidence exists.

## "You Are Now Here" Logic

Calculate the strongest current frontier using:

- pillar priority
- active work count
- blockers
- recent evidence
- deep-context alignment
- primary path protection

Do not change the frontier without checking the deep-context decision index when the change affects Homes for Hands, The Crew Blueprint scope, Deadhang-to-Homestead relationship, Production Atlas priority, milestone sequencing, or the roadmap's life-architecture direction.
