# Stage 3 Scope — Production Atlas Canonical Documentation

**Status:** BUILT (2026-07-18). Owner supplied the full Production Atlas
completed-work review, which is both the go-ahead and the source material (same
flow as Stage 2). All docs drafted in `companies/production-atlas/`; roadmap
production-atlas branch synced to reality (stale old-model language replaced;
`pa-1` complete; status corrected upward).
**Goal:** everything about Production Atlas is reconstructable from repository
documentation alone.

## Definition of done

A person or AI who has never seen Production Atlas can read one folder and
understand — and rebuild — it: what it is (an industry **intelligence /
research** platform, **not** a job board), its static architecture, its
repository/branching strategy, its research methodology and package system, its
application structure, its department coverage, its validation system, its
public-data policy, and its growth direction. No outside context required, except
deliberately-private internal research (see guardrails).

## Where it lives

Same per-company pattern as Stages 1–2:

```
companies/
  production-atlas/
    README.md
    00_overview.md            # vision, purpose, "not a job board"
    01_architecture.md        # static GitHub Pages app; no backend/db/login/scraping; modernization
    02_repository_strategy.md  # festival-atlas repo, "Production Atlas" product, research-version branch
    03_research_methodology.md # structured packages, confidence/verification, public-safe vs internal
    04_application.md          # navigation pages + manifest-driven research-package loader
    05_departments.md          # department framework + coverage status (Scenic incomplete)
    06_validation.md           # validation rules + data-cleanup/modernization completed
    07_data_policy.md          # public data policy (what must never be exposed)
    08_growth_model.md         # long-term direction, remaining work, self-assessment
```

## Guardrails (public-safe — repo is public)

The **subject** of this project is a public/private data boundary, so the docs
describe the **system**, never the sensitive research payload. Keep OUT:
- Private contact information, pay rates, NDA-protected or client-sensitive
  information, internal notes, and rumors/unverified claims — the same things the
  Production Atlas public app itself must never expose (doc 07).
- The internal research corpus lives in the `festival-atlas` repo's
  research-version branch, not here — this folder documents the model, not the data.

## Source material

- Owner's "Production Atlas — Project Completion Review" (2026-07-18).
- `roadmap.json` production-atlas branch (`pa-1..pa-5`).
- `data/raw-reports/` Production Atlas / Festival Atlas digests (branch discipline,
  research-version scope).
- Referenced, not copied: `thecrewblueprint-glitch/festival-atlas` (the app +
  research corpus).

## Build sequence

1. Scaffold `companies/production-atlas/` + README + 9 docs. ✅
2. Draft all docs from the review. ✅
3. Sync roadmap production-atlas branch to reality (reframe as intelligence
   platform; `pa-1` done; correct state/blockers/status). ✅
4. Update CHANGELOG + CURRENT_STATE. ✅
