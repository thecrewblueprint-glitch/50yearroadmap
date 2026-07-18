# Stage 5 Scope — Personal Operations / Roadmap System Canonical Documentation

**Status:** BUILT (2026-07-18). Reconstructed from the repository itself (the
system documents the system we work in): `roadmap.json`, `app.js`/`index.html`,
`AGENTS.md`, `DATA_SAFETY_POLICY.md`, the `scripts/` pipeline, and the
`governance/` folder. Roadmap personal-operations branch synced to reality
(dashboard live, 90-day windows exist, layered views exist).
**Goal:** everything about the command center — the operating system for the
whole initiative — is reconstructable from repository documentation alone.

## Definition of done

A person or AI who has never seen this repo can read one folder and understand —
and rebuild — the command center: what it is, the roadmap data model, the
dashboard, the AI pipeline (memories → watcher → prioritizer → validator),
governance and collaboration rules, the public-safety model, and where it's
headed (database migration, templates).

## Where it lives

```
companies/
  personal-operations/
    README.md
    00_overview.md            # what the command center is; the core question it answers
    01_data_model.md          # roadmap.json branch/journey model (single source of truth)
    02_dashboard.md           # the live views: Timeline, Dashboard, 30/60/90, branch hubs, The Vision
    03_ai_pipeline.md         # process-memories → watcher → prioritizer → validator (human-in-the-loop)
    04_governance.md          # AGENTS, CHANGELOG, governance/, collaboration rules, the Stage model
    05_growth_model.md        # anti-sprawl gates, templates, database migration, self-assessment
```

Public-safety (`DATA_SAFETY_POLICY.md`, the schema, the validator PII scan) is
covered under `04_governance` rather than a standalone doc, since it is a
governance control.

## Guardrails (public-safe — repo is public)

- No raw memory exports, no PII, no financials. This folder documents the
  **system**, and the system's own rules already forbid publishing raw evidence.
- Describe the pipeline and model; don't paste sensitive proposal/backlog content.

## Source material

- `roadmap.json`, `index.html`, `app.js`, `styles.css`, `ninety.css`,
  `branch.html`, `present.html` — the live dashboard.
- `scripts/` — process-memories, roadmap-watcher, prioritize-proposals,
  validate-roadmap.
- `AGENTS.md`, `CHANGELOG.md`, `DATA_SAFETY_POLICY.md`, `WATCHER_GUIDE.md`,
  `governance/` — rules, log, safety, the Stage model.
- `INTERACTIVE_DASHBOARD_SPEC.md` — the (unbuilt) future interactive-dashboard
  direction; referenced by the growth model.

## Build sequence

1. Scaffold `companies/personal-operations/` + README + 5 docs. ✅
2. Draft from the repo itself. ✅
3. Sync roadmap personal-operations branch (po-1/po-3/po-4 completed; state
   rewritten; status 35→65). ✅
4. Update CHANGELOG + CURRENT_STATE. ✅

## Owner-input gaps (low urgency)

- `po-5` downloadable documentation templates — not built; confirm the desired
  set (investor pitch, market research, project plan) when ready.
- Database migration (OD-5) timing — deferred until JSON editing is the
  bottleneck.
