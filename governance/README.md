# Governance

The operating-governance layer for this repository as it grows from a roadmap
into the operational command center for Aaron's companies (Deadhang Labor LLC,
The Crew Blueprint, Production Atlas, Festival Atlas, and future products).

## What lives here

- `CURRENT_STATE.md` — a plain-language snapshot of where things actually stand.
- `DECISION_LOG.md` — durable strategic decisions (structure, tax, direction)
  with the reasoning, so they aren't re-litigated.
- `handoffs/` — dated AI/human handoff documents (context transfers).

## What already exists elsewhere (do not duplicate)

Stage 0 asked for collaboration standards, a change log, and an AI-handoff
system. Much of that is already built — treat these as part of governance:

- **`AGENTS.md`** (repo root) — the operating rules and collaboration standard:
  commit-to-`main`, the data model, integrity rules, the start/work/finish
  checklist. This *is* the collaboration standard.
- **`CHANGELOG.md`** (repo root) — the running work/decision log and open threads.
- **`CHATGPT_HANDOFF.md`** (repo root) — the standing AI-onboarding handoff.
- **`scripts/validate-roadmap.py`**, **`roadmap-watcher.py`**,
  **`prioritize-proposals.py`** — the enforcement/automation layer.

## The long-term repository evolution (from the 2026-07-17 handoff)

- **Stage 0 — Stabilization & governance** *(in progress)*: remove outdated info,
  synchronize the roadmap with reality, and establish governance + collaboration +
  AI-handoff standards. Do this before further project development.
- **Stage 1 — Deadhang Labor canonical documentation**: Deadhang fully
  reconstructable from repo docs alone.
- **Stage 2 — The Crew Blueprint documentation**: safety philosophy, course
  architecture, standards, research workflow, authority hierarchy.
- **Stage 3 — Production Atlas**: architecture, data model, verification
  pipeline, methodology — documented before implementation continues.
- **Stage 4 — Shared infrastructure**: common auth, contractors, scheduling,
  payments, shared data across projects.
- **Stage 5 — Executive command center**: operational dashboard + decision,
  risk, and progress trackers + master roadmap + AI collaboration system.

## Principle

Every decision is traceable. Every milestone has completion criteria. Every
project has canonical documentation. Any AI or human contributor can resume
without re-learning context. The repository is the single source of truth.
