# Current State

A plain-language snapshot of where things actually stand. Update it when reality
moves. For the live, structured version see `roadmap.json` (the dashboard);
for the running history see `CHANGELOG.md`.

_Snapshot: 2026-07-18._

## Business identity (fixed)

Arizona single-member LLC · Schedule C · cash basis · owner-operated · live-event
production labor. (See `DECISION_LOG.md`.)

## Deadhang Labor LLC — business audit

**Complete:** Arizona LLC · EIN · business bank account · business website
(live + SSL) · business email · cash accounting · Schedule C · W-9 system ·
invoice system · record retention · existing client MSA · operational structure.

**In progress:** independent-contractor framework · safety documentation ·
print-on-demand merch line (additional revenue stream, under Deadhang).

**Deferred (not forgotten):** business insurance — until the appropriate
scaling stage.

**Still to build:** team-deployment capability; systematic gig tracking; tax
closeout (returns filed — amend if needed, confirm balance, pay).

`dh-1` (business structure audit) is ~90% complete.

## Projects at a glance (Phase 1 branches)

- **Deadhang Labor LLC** (~60%) — foundation largely in place; scaling + contractor/safety work ahead.
- **The Crew Blueprint** (~35%) — training resource; **foundation complete and no longer blocked by software** (vision, course architecture, multi-AI content workflow, brand, legal/authority model, website shell, plugin architecture all decided). Next-gen platform intentionally deferred; the real constraint is now content-production volume. Canonical docs in `companies/crew-blueprint/`.
- **Production Atlas** (~50%) — live-event **industry intelligence/research** platform (not a job board); static GitHub Pages app reading manifest-driven research packages (`festival-atlas` repo, `research-version` branch). Architecture, methodology, public-safe data model, and validation settled; department research ~85% (Scenic incomplete). Remaining: research-corpus depth, usability, governance. Canonical docs in `companies/production-atlas/`.
- **Contractor Tools** (~35%) — shared infrastructure layer; built: 1099 invoice generator (deterministic single-file tool) + payment tracking; calendar feeds (ICS, multi-platform) working. Remaining: reliable calendar authorization renewal (`ct-3`), backend-scope validation (`ct-1`); team coordination is future. Canonical docs in `companies/contractor-tools/`.
- **Personal Operations / Roadmap System** (~65%) — this repo/command center; mature and operational (live dashboard, branch-model source of truth, AI pipeline, governance + CI validator). Remaining: anti-sprawl scope gates (`po-2`), documentation templates (`po-5`), deferred database migration (OD-5). Canonical docs in `companies/personal-operations/`.

## Phase 2 (the destination)

- **Land Acquisition** and **The Homestead / Homes for Hands** — nomadic-movement
  home base for traveling live-event workers. Outreach started (The Roadie Clinic
  contacted; rated connection shortlist in `data/roadmap/connections.md`).

## Where governance stands

Stage 0 complete: roadmap synchronized with reality, governance folder
established, collaboration + AI-handoff standards in place (`AGENTS.md`,
`CHANGELOG.md`, `CHATGPT_HANDOFF.md`), and a CI validator wired in. Stages 1–5
(canonical documentation for all five companies) are built — see
`companies/` and `governance/STAGE_*_SCOPE.md`. A full repository audit is
recorded in `governance/AUDIT_2026-07-18.md`. Ongoing work is currency and the
remaining per-branch roadmap items.
