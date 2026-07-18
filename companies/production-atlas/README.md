# Production Atlas — Canonical Documentation

**What this is:** the permanent, rebuildable record of Production Atlas — a
long-term **intelligence and research platform** for the U.S. live-event
industry. It is **not a job board**; it makes industry research structured,
searchable, and actionable.

If you have never seen Production Atlas, you can read this one folder and
understand — and rebuild — it: its vision, static architecture,
repository/branching strategy, research methodology, application structure,
department coverage, validation system, public-data policy, and growth direction.

## Naming (important)

- **Product name:** Production Atlas.
- **Repository:** `thecrewblueprint-glitch/festival-atlas`.
- **Research** lives on the **`research-version`** branch; production-ready code
  is kept separate (see doc 02).

## The big picture (as of 2026-07)

The project has **moved beyond defining its architecture.** Vision, architecture,
branching, research methodology, the public-safe data model, and validation are
settled. The application is a static GitHub Pages app that reads manifest-driven
research packages. The remaining work is **completing the research corpus**
(Scenic department), **usability**, and **governance/documentation** — so the
repo becomes a durable, collaborative knowledge system rather than just a static
app.

## The documents

| Doc | Covers |
| --- | --- |
| [00_overview](00_overview.md) | Vision, audience, purpose — and why it is **not** a job board |
| [01_architecture](01_architecture.md) | Static GitHub Pages app; no backend/db/login/scraping; modernization |
| [02_repository_strategy](02_repository_strategy.md) | `festival-atlas` repo, product name, `research-version` branch, prod/research split |
| [03_research_methodology](03_research_methodology.md) | Structured packages, confidence/verification, public-safe vs internal |
| [04_application](04_application.md) | Navigation pages + manifest-driven research-package loader |
| [05_departments](05_departments.md) | Department framework + coverage status (Scenic incomplete) |
| [06_validation](06_validation.md) | Validation rules + completed data cleanup/modernization |
| [07_data_policy](07_data_policy.md) | Public data policy — what must never be exposed |
| [08_growth_model](08_growth_model.md) | Long-term direction, remaining work, self-assessment |

## Guardrails (this repo is public)

This project is *about* a public/private data boundary, so this folder documents
the **system**, never the sensitive research payload. It contains no private
contact info, pay rates, NDA/client-sensitive information, internal notes, or
unverified claims. The internal research corpus lives in the `festival-atlas`
research-version branch, not here.
