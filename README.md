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
- `/memories`: Raw imported archives and exports; preserved as source evidence.
- `/memories/processed`: Generated chunks, indexes, and navigation files from raw memory archives.
- `/data/raw-reports`: Curated operational digests.
- `/data/roadmap`: Approved roadmap state and decision indexes.
- `/scripts`: Memory processing and build tools.

Planned / referenced but not yet in the repo:

- `/data/roadmap-deep-context`: Mission, values, identity, and long-range intent context. Referenced by `AGENTS.md` and `data/roadmap/deep-context-decision-sources.json`.
- A roadmap **watcher** that turns curated digests into proposals — described in the pipeline below as a workflow; there is no watcher script yet.
- `/data/schema`: Data validation rules.

## Data Pipeline

Automated steps are marked ✅; manual/planned steps are marked ⏳.

```text
RAW MEMORY ARCHIVES
  ↓  ✅ scripts/process-memories.py (+ GitHub Action)
/memories/processed chunks + indexes
  ↓  ⏳ manual curation
curated digests in /data/raw-reports
  ↓  ⏳ watcher (planned — no script yet)
roadmap proposals
  ↓  ⏳ manual approval
approved /data/roadmap state
  ↓  ⏳ manual authoring
roadmap.json dashboard snapshot (branch model)
```

Only memory processing is automated today. Everything downstream of the
processed chunks is currently done by hand; the live `roadmap.json` is
authored directly in the branch model the dashboard reads.

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

- `ultimate_goal` — the north-star statement
- `phase` / `phase_description` — the current phase
- `this_week_focus` — the priority work items for the week
- `branches[]` — each branch's goal, current state, % complete, blockers, and work items
- `ecosystem_flow` — how the branches connect end to end

## Agent Rules

See `AGENTS.md` for strict rules on how AI agents must interact with this repo.
