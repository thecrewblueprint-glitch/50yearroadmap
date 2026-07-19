# Operations Command Center

A repo-backed, AI-assisted roadmap, memory, evidence, and project-state system.

## Dashboard

View the GitHub Pages dashboard here:

https://thecrewblueprint-glitch.github.io/50yearroadmap/

## Purpose

Organize businesses, apps, goals, daily reports, completed work, future plans, long-term vision, and deep roadmap context into one auditable command center.

The system is designed to answer one practical question:

> What is the next thing I should probably focus on without losing the rest of the vision?

## Core Principles

1. **Chaos goes in. Auditable roadmap structure comes out.**
2. **Flexible detours without destroying linear progression.**
3. **Raw memory remains evidence, not public output.**
4. **Deep context influences direction, but is not published raw.**
5. **Moved-later items are preserved, not deleted.**

## Structure

- Root (`index.html`, `app.js`, `styles.css`, `roadmap.json`): the live GitHub Pages dashboard. Pages serves from the repository root.
- `/companies`: Canonical, rebuildable documentation for each company/branch (the permanent knowledge base — see below).
- `/memories`: Raw imported archives and exports; preserved as source evidence.
- `/memories/processed`: Generated chunks, indexes, and navigation files from raw memory archives.
- `/data/raw-reports`: Curated operational digests.
- `/data/roadmap`: Approved roadmap state, decision indexes, watcher proposals, the ranked backlog, and the connections/leads log.
- `/data/roadmap-deep-context`: Mission, values, identity, and long-range intent context (indexed by `data/roadmap/deep-context-decision-sources.json`).
- `/data/schema`: Public-safety data-validation rules.
- `/governance`: Current state, decision log, open decisions, known risks, lessons learned, and AI/human handoffs.
- `/scripts`: Memory processing, the watcher, the prioritizer, the promote helper, and the validator.

## Data Pipeline

Automated/tooled steps are marked ✅; manual steps are marked ⏳.

```text
RAW MEMORY ARCHIVES
  ↓  ✅ scripts/process-memories.py (+ GitHub Action)
/memories/processed chunks + indexes
  ↓  ⏳ manual curation
curated digests in /data/raw-reports
  ↓  ✅ scripts/roadmap-watcher.py  (proposals only — never edits roadmap.json)
data/roadmap/watcher-proposals.json
  ↓  ✅ scripts/prioritize-proposals.py  (ranked "work on first" backlog)
data/roadmap/proposal-backlog.md
  ↓  ⏳ owner records approvals in data/roadmap/promotions.json
  ↓  ✅ scripts/promote-proposals.py  (applies + auto-IDs + validates, rollback on fail)
roadmap.json  (branch model)
  ↓  ✅ scripts/validate-roadmap.py  (gate: refs, enums, PII)
  ↓  commit to main → dashboard
```

Memory processing is automated; the watcher, prioritizer, promote helper, and
validator are built and run on demand. Promotion into `roadmap.json` is
deliberately human-in-the-loop — the watcher only proposes, and the promote
helper only applies changes **you approved** in `promotions.json`. Two update
paths feed it: evidence the watcher found, and real-world progress it can't see
(described directly). See `WATCHER_GUIDE.md`.

Deep-context files follow a parallel route:

```text
/data/roadmap-deep-context
  ↓
/data/roadmap/deep-context-decision-sources.json
  ↓
watcher decision context for priority, sequencing, frontier, and project boundaries
```

## Current Live Snapshot

The live dashboard reads:

```text
roadmap.json
```

It uses the **branch model** and includes:

- `north_star` / `end_goal` — the destination (the Homestead) and how to reach it
- `phase` / `phase_description` / `phases[]` — the current phase and the phased plan
- `this_week_focus` — the priority work items for the week
- `thirty_sixty_ninety` — the 30/60/90-day operating windows
- `branches[]` — each branch's goal, current state, % complete, blockers, and work items (status: `not_started` / `in_progress` / `blocked` / `completed` / `moved_later`)
- `journey` — the linear "you are here → Homestead" milestone path
- `ecosystem_flow` — how the branches connect end to end

## Canonical Company Documentation

`/companies/<company>/` holds the permanent, rebuildable record of each
company/branch — enough that someone who has never seen the business could
understand and rebuild it from the repo alone. Everything is public-safe (no PII,
financials, or private data). Status as of 2026-07-18:

| Company | Folder | Docs | State |
| --- | --- | --- | --- |
| Deadhang Labor LLC | `companies/deadhang-labor/` | 15 | ✅ Documented |
| The Crew Blueprint | `companies/crew-blueprint/` | 9 | ✅ Documented |
| Production Atlas | `companies/production-atlas/` | 9 | ✅ Documented |
| Contractor Tools | `companies/contractor-tools/` | 6 | ✅ Documented |
| Personal Operations / Roadmap System | `companies/personal-operations/` | 6 | ✅ Documented |

Each folder opens with a `README.md` index. The documentation is built stage by
stage under `governance/STAGE_*_SCOPE.md`; the reasoning and current snapshot live
in `governance/`.

## Governance & Agent Rules

- `AGENTS.md` — strict rules for how AI agents interact with this repo (commit to `main`, validate, log).
- `CHANGELOG.md` — the running work/decision log.
- `/governance/` — current state, decisions, open decisions, known risks, lessons, and handoffs.
