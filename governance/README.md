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

## Other files here

- `KNOWN_RISKS.md`, `LESSONS_LEARNED.md`, `OPEN_DECISIONS.md` — risk, learning,
  and open-decision registers.
- `STAGE_1_SCOPE.md` … `STAGE_5_SCOPE.md` — the per-stage documentation plans
  (each marked BUILT).
- `AUDIT_2026-07-18.md` — the full repository audit.

## The long-term repository evolution (from the 2026-07-17 handoff)

Each documentation stage lands in `companies/<company>/` and is scoped in the
matching `STAGE_*_SCOPE.md`.

- **Stage 0 — Stabilization & governance** ✅ *complete*: outdated info removed,
  roadmap synchronized with reality, and governance + collaboration + AI-handoff
  standards established.
- **Stage 1 — Deadhang Labor canonical documentation** ✅ `companies/deadhang-labor/`.
- **Stage 2 — The Crew Blueprint documentation** ✅ `companies/crew-blueprint/`.
- **Stage 3 — Production Atlas** ✅ `companies/production-atlas/`.
- **Stage 4 — Contractor Tools (shared infrastructure)** ✅ `companies/contractor-tools/`.
- **Stage 5 — Personal Operations / command center** ✅ `companies/personal-operations/`.

All five companies now have canonical documentation. Ongoing work is currency
(keep docs + roadmap in sync as reality moves) and the remaining per-branch work
items in `roadmap.json`.

## Principle

Every decision is traceable. Every milestone has completion criteria. Every
project has canonical documentation. Any AI or human contributor can resume
without re-learning context. The repository is the single source of truth.
