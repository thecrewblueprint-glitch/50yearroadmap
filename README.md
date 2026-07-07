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

- `/memories`: Raw imported archives and exports; preserved as source evidence.
- `/memories/processed`: Generated chunks, indexes, and navigation files from raw memory archives.
- `/data/roadmap-deep-context`: Mission, emotional meaning, values, identity, long-range intent, and life-architecture context.
- `/data/raw-reports`: Curated watcher-ready operational digests.
- `/data/roadmap`: Approved roadmap state, proposals, and decision indexes.
- `/docs`: GitHub Pages dashboard output.
- `/scripts`: Processing, watcher, validation, and build tools.
- `/data/schema`: Data validation rules.

## Data Pipeline

```text
RAW MEMORY ARCHIVES
  ↓
/memories/processed chunks + indexes
  ↓
curated digests in /data/raw-reports
  ↓
roadmap watcher proposals
  ↓
approved /data/roadmap state
  ↓
/docs/roadmap.json dashboard snapshot
```

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
docs/roadmap.json
```

That snapshot is currently built from the watcher-processed roadmap data and includes:

- current frontier
- pillar summaries
- blocker list
- completed list
- moved-later list
- deep-context decision policy

## Agent Rules

See `AGENTS.md` for strict rules on how AI agents must interact with this repo.
