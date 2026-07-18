# Handoff to GPT

You're joining an existing repository as a collaborating AI. This document
orients you fast. **Read `AGENTS.md` in full before making any change** — this
handoff is the summary; `AGENTS.md` is the law.

_Last updated: 2026-07-17. The living record of what's been done is
`CHANGELOG.md` (read its newest entries first); durable decisions are in
`governance/DECISION_LOG.md`._

---

## What this repo is

A repo-backed planning system for **Deadhang Labor** whose north star is the
**Homestead** — a community home base for traveling stagehands, powered by a
self-sustaining Labor → Training → Jobs engine.

It publishes a GitHub Pages dashboard **from the repository root**:
https://thecrewblueprint-glitch.github.io/50yearroadmap/

## The one rule that matters most

**Commit directly to `main`. Do not create branches. Do not open PRs.**
Branching is what previously stranded a whole watcher pipeline on a side branch
while the model changed underneath it. Single-trunk keeps collaborators in sync.

If you find useful work on another branch (there's a legacy branch
`claude/repository-review-yvxvn5`), **do not merge it silently** — summarize it
and ask the owner.

## Every change ends with three things

1. If you touched `roadmap.json`: run `python3 scripts/validate-roadmap.py`
   and fix any errors (it must pass).
2. Add a dated entry to `CHANGELOG.md` (what changed + why).
3. Commit and push to `main`.

---

## The live product (repo root — treat as production)

| File | Role |
|---|---|
| `index.html` | Timeline view (default) + Dashboard view, toggled in the header |
| `branch.html` | Per-branch hub — `?branch=<id>&view=overview\|work\|blockers\|details` |
| `present.html` | "The Vision" — read-only page for investors/collaborators |
| `app.js` | Dashboard logic |
| `styles.css` | Shared theme (professional blue/teal) |
| `roadmap.json` | **Single source of truth for all views** |

`roadmap.json` is hand-authored. There is no automated builder writing it. When
the plan changes, you edit `roadmap.json` directly and keep it valid.

## The data model (current — "branch / journey")

Top-level keys of `roadmap.json`:

- `north_star` — one-sentence destination.
- `end_goal` — `{ destination, what_it_is, how_to_reach_it[] }`.
- `phases` — `[{ number, name, status: active|future, goal, branch_ids[] }]`.
- `branches` (7) — each: `{ id, name, role, status_percentage, ultimate_goal,
  current_state, critical_blocker, timeline:{ phase_1_ready, description },
  blockers[], work_items[], phase, lifecycle: active|future }`.
  Work item: `{ id, task, why, priority: CRITICAL|HIGH|MEDIUM|LOW,
  status: not_started|in_progress|blocked|completed|moved_later }`
  (`moved_later` = deferred: visible but off the active path).
- `journey` — `{ you_are_here, start_label, milestones[{ id, order, title,
  area_branch_id, state: current|upcoming|done, summary, outcome, step_ids[],
  leads_to }] }`. `step_ids` reference `work_items` by id (branches stay the
  single source of truth; milestones just sequence existing work).
- `this_week_focus` — `{ priority_1, priority_2, priority_3, note }` (each
  priority is a comma-separated list of work-item ids).
- `thirty_sixty_ninety` — `{ title, summary, windows[{ id, label, status, theme,
  goal, focus_step_ids[], outcomes[], guardrail }] }` (30/60/90 operating layer;
  `focus_step_ids` reference work items). Rendered by `app.js` in the Dashboard view.
- `ecosystem_flow` — `{ flow[] }`.

> A previous **pillar model** (`vision.json`, `pillars.json`, `frontier`,
> `pillar_id`-keyed proposals) is **retired**; its files and
> `scripts/build-roadmap.py` were **removed 2026-07-18**. Do not reintroduce it
> into `roadmap.json`. (The current `watcher-proposals.json` is the branch-model
> watcher output — that one is live.)

## The pipeline

```
memories/ (raw archives)
  → scripts/process-memories.py   [automated, also a GitHub Action]
memories/processed/ (chunks + indexes)
  → curate by hand
data/raw-reports/*-digest.md
  → scripts/roadmap-watcher.py    [proposals only — never edits roadmap.json]
data/roadmap/watcher-proposals.json
  → owner/agent promotes approved items by hand
roadmap.json
  → scripts/validate-roadmap.py   [gate: must pass]
  → commit to main → dashboard
```

### Scripts
- `scripts/process-memories.py` — chunks raw archives. Deterministic, safe to
  re-run. (Only its output timestamp changes on re-run; don't commit that churn.)
- `scripts/roadmap-watcher.py` — reads the digests, maps candidate work
  items/blockers to the **current** branches, public-safe filters, de-dupes
  against the roadmap, writes proposals. **Read `WATCHER_GUIDE.md`.** It proposes;
  a human decides. Nothing reaches the dashboard until a human puts it in
  `roadmap.json`.
- `scripts/validate-roadmap.py` — validates `roadmap.json` (refs resolve, no
  dupes, enums/ranges, public-safety). Exit 0 = pass, 1 = errors.
- `scripts/prioritize-proposals.py` — ranks open proposals into
  `data/roadmap/proposal-backlog.md` ("work on first" order). Read-only; deletes
  nothing.

## Evidence & safety (do not violate)

- **Raw memory is immutable evidence** — never overwrite `/memories` or the
  curated `data/raw-reports` digests.
- **Never publish private data** to the dashboard: no emails, phone numbers,
  addresses, financial info, or owner personal identity. The safety patterns
  live in `data/schema/roadmap-public-safety.json`; the validator enforces them.
- **Consult deep context** (`data/roadmap-deep-context/`, indexed by
  `data/roadmap/deep-context-decision-sources.json`) before changing direction.
- **The owner is the executive.** You structure and maintain; the owner decides
  direction. For direction changes (the Homestead, Crew Blueprint scope, phase
  sequencing, what "you are here" points to), confirm rather than deciding alone.

## Current status (2026-07-17)

- Dashboard: fully functional (Timeline, Dashboard incl. 30/60/90, branch hubs, The Vision).
- Governance: `/governance/` established (CURRENT_STATE, DECISION_LOG,
  OPEN_DECISIONS, KNOWN_RISKS, LESSONS_LEARNED, handoffs) alongside `AGENTS.md` +
  `CHANGELOG.md`. Repo is in **Stage 0** (stabilization) — do Stage 0 before Stages 1–5.
- Watcher, validator, and prioritizer built and audited; `moved_later` and the
  `thirty_sixty_ninety` layer are live.
- Deadhang facts locked: **Arizona single-member LLC / Schedule C / cash basis**
  (see `DECISION_LOG.md`) — do not drift to other-state assumptions.
- Homestead outreach started: The Roadie Clinic contacted; connections shortlist
  in `data/roadmap/connections.md`.
- **Open threads / decisions:** `CHANGELOG.md` (top) and `governance/OPEN_DECISIONS.md`.
- **Note:** GPT is paused (GitHub connector issue) — Claude is solo on the repo
  until that's fixed.

## Start-here checklist for GPT

1. Read `AGENTS.md`, then the newest `CHANGELOG.md` entries.
2. Skim `roadmap.json` (the data) and open the live dashboard.
3. Make focused changes on `main`; validate if you touched `roadmap.json`.
4. Log every change in `CHANGELOG.md`; commit and push to `main`.
5. Anything ambiguous about direction → ask the owner, don't guess.
