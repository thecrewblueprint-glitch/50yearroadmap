# Personal Operations / Roadmap System — Canonical Documentation

**What this is:** the permanent, rebuildable record of the **command center
itself** — the repo-backed, AI-assisted roadmap, memory, evidence, and
project-state system that runs the whole initiative. This is the operating system
the other four companies are managed *with*.

If you have never seen this repo, you can read this one folder and understand —
and rebuild — the command center: the roadmap data model, the live dashboard, the
AI pipeline, the governance and collaboration rules, the public-safety model, and
where it's headed.

## The core question it answers

> What is the next thing I should probably focus on without losing the rest of
> the vision?

## The big picture (as of 2026-07)

**Mature and operational.** The dashboard is live on GitHub Pages;
`roadmap.json` (branch model) is the single source of truth; governance and the
AI pipeline are established. Remaining work is polish — finishing anti-sprawl
scope gates, downloadable documentation templates, and the eventual database
migration (deferred).

## The documents

| Doc | Covers |
| --- | --- |
| [00_overview](00_overview.md) | What the command center is; the question it answers |
| [01_data_model](01_data_model.md) | `roadmap.json` branch/journey model — the single source of truth |
| [02_dashboard](02_dashboard.md) | The live views: Timeline, Dashboard, 30/60/90, branch hubs, The Vision |
| [03_ai_pipeline](03_ai_pipeline.md) | memories → watcher → prioritizer → validator (human-in-the-loop) |
| [04_governance](04_governance.md) | AGENTS, CHANGELOG, governance/, collaboration rules, public-safety, the Stage model |
| [05_growth_model](05_growth_model.md) | Anti-sprawl gates, templates, database migration, self-assessment |

## Guardrails (this repo is public)

This documents the **system**, whose own rules forbid publishing raw evidence,
PII, or financials. No raw memory exports or sensitive backlog content here.
