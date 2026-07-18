# 01 — Data Model

**Status:** Documented.

## Single source of truth

`roadmap.json` (repository root) is the **single source of truth** for every
dashboard view. It uses the **branch/journey model**. Nothing else holds roadmap
state — the dashboard reads this file directly, and a validator gates it (doc 03).

## Top-level shape

- **`north_star` / `end_goal`** — the destination (the Homestead) and how it's
  reached.
- **`phase` / `phase_description` / `phases[]`** — the current phase and the
  phased plan (Phase 1: Labor → Training → Jobs; Phase 2: the Homestead).
- **`this_week_focus`** — the priority work-item IDs for the week.
- **`thirty_sixty_ninety`** — the 30/60/90-day operating windows, each with focus
  step IDs, outcomes, and a guardrail.
- **`branches[]`** — each branch's goal, role, `status_percentage`, current state,
  blockers, and `work_items` (see below).
- **`journey`** — the linear "you are here → Homestead" milestone path.
- **`ecosystem_flow`** — how the branches connect end to end.

## Branches and work items

Each branch has an `id`, `name`, `role`, `status_percentage`, `ultimate_goal`,
`current_state`, `critical_blocker`, `blockers[]`, and `work_items[]`. Each work
item has an `id` (e.g. `dh-1`, `cb-2`, `pa-3`), `task`, `why`, `priority`, and a
`status`.

### Work-item status enum

- `not_started`
- `in_progress`
- `blocked`
- `completed`
- `moved_later` — deliberately deferred, **preserved not deleted** (principle 5).

## Referential integrity

IDs are referenced in several places — `this_week_focus`, the 30/60/90 windows'
`focus_step_ids`, the journey milestones' `step_ids`, and the phases' `branch_ids`.
The validator (doc 03) checks that every referenced ID resolves, that statuses are
in-enum, and that there are no duplicates — so the model can't silently drift.

## Why JSON (for now)

JSON keeps the source of truth diff-able, reviewable in git, and directly
readable by the static dashboard with no backend. Moving to a database is a
tracked future decision (OD-5, doc 05) — deferred until hand-editing JSON becomes
the bottleneck.
