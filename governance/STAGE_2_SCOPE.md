# Stage 2 Scope — The Crew Blueprint Canonical Documentation

**Status:** BUILT (2026-07-18). Owner supplied the full completed-work review,
which answered both open questions (authority/safety model and content
pipeline). All 9 docs drafted in `companies/crew-blueprint/`; roadmap
crew-blueprint branch synced to reality (platform deferred, `cb-1` complete).
Remaining: catalog grows as new packets are produced (`cb-4`); discipline/pathway
map builds out (`cb-2`).
**Goal:** everything about The Crew Blueprint is reconstructable from repository
documentation alone — what it is, what it teaches, how the content is
organized, its authority/safety model, its brand, and its platform plan.

## Definition of done

A person or AI who has never seen The Crew Blueprint can read one folder and
understand — and rebuild — the resource: its mission, who it serves, the
discipline/pathway learning model, the course architecture and catalog, the
safety/content authority framework, the brand system, and the platform
roadmap. No outside context required, except deliberately-private or paid
material (see guardrails).

## Where it lives (proposed)

Same per-company pattern as Stage 1:

```
companies/
  crew-blueprint/
    README.md                 # index + one-paragraph "what this is"
    00_overview.md            # mission, audience, what it is / is NOT
    01_learning_model.md      # discipline/pathway mapping, visual/workflow approach
    02_authority_and_safety.md# content authority + "no certification" trust model
    03_curriculum.md          # course architecture + catalog (titles/scope, not full lessons)
    04_standards_alignment.md # OSHA / ASME / ANSI / ESTA / ETCP alignment
    05_platform.md            # LMS status, static course-preview interim, stabilization plan
    06_brand.md               # CSS schema, voice, naming
    07_content_pipeline.md    # how a lesson goes from draft → review → publish-ready
    08_growth_model.md        # content-first → foundational library → platform launch
```

## The canonical document set

| Doc | Covers | Primary source today | Status |
| --- | --- | --- | --- |
| 00_overview | Mission, audience (working stagehands), "learn what/why/how it fits"; explicit **non-goals** (not a certifying body) | roadmap crew-blueprint branch, owner statements | ✅ ready to draft |
| 01_learning_model | Visual, workflow-based approach; discipline/pathway mapping (`cb-2`) | roadmap `cb-2`, owner concept | ✅ ready to draft |
| 02_authority_and_safety | Content-authority + safety trust model (`cb-1`); how material can be safety-critical without issuing certifications | roadmap `cb-1` | ⚠️ ready; model still being defined — document intent + open questions |
| 03_curriculum | Course architecture and catalog: the 3 publication-ready packets (Rigging Hardware ID & Inspection; Bridle Math & Angle Tension; Predictive Hazard Recognition) by title/scope/level | owner-provided packets | ⚠️ describe catalog only — do NOT paste full paid lesson content |
| 04_standards_alignment | Alignment to OSHA / ASME / ANSI / ESTA / ETCP standards & concepts | packets, Deadhang doc 06 | ✅ ready to draft |
| 05_platform | LMS deferred (`cb-3`); interim static `course-preview.html` workflow in `Contentrepo`; stabilization plan | roadmap `cb-3`, owner statements | ⚠️ ready; reference the other repo, don't duplicate |
| 06_brand | The Crew Blueprint's own CSS schema (source of truth), voice, naming | live site CSS, Deadhang doc 08 | ⚠️ colors/assets referenced to their source, not hardcoded |
| 07_content_pipeline | Draft → review → publish-ready flow; scoring/QA (e.g. the 96/100 review pass) | owner workflow | ⚠️ ready; confirm the standard steps |
| 08_growth_model | Content-first pause → foundational library (`cb-4`) → platform launch | roadmap timeline, `cb-4` | ✅ ready to draft |

## Guardrails (public-safe — repo is public)

Keep OUT of these docs (belongs in private storage / the private content repo):
- **Full paid lesson content.** Describe the course architecture, titles,
  scope, and learning objectives — do **not** reproduce complete lessons,
  answer keys, or assessment banks that are (or will be) sold or gated.
- **No certification claims.** The Crew Blueprint teaches skills and context;
  it does **not** certify anyone. Every doc must reflect that. It aligns to
  OSHA/ASME/ANSI/ESTA/ETCP standards and concepts — it does not confer them.
- Income figures, pricing, PII, third-party contact details, secret keys.
- Where sensitive/paid detail is essential, **reference** its private home
  (e.g. "full lessons maintained in the private `Contentrepo`").

## Source material available

- `roadmap.json` — crew-blueprint branch (current state, `cb-1..cb-4`, blockers).
- Owner-provided course packets (3 publication-ready) — used for catalog/scope only.
- `companies/deadhang-labor/06_safety.md` — already cross-references Crew
  Blueprint teaching material; keep the two consistent (teaching vs. operating).
- Other repos (referenced, not copied): `Contentrepo` (lessons, brand assets,
  `course-preview.html`).

## Build sequence (after sign-off)

1. Scaffold `companies/crew-blueprint/` with `README.md` + the 9 stubs.
2. Draft the ✅ "ready" docs first (00, 01, 04, 08) — highest signal, least blocked.
3. Draft the ⚠️ docs, confirming open facts with the owner (authority model,
   pipeline steps, brand source).
4. Cross-link: roadmap crew-blueprint branch ↔ this folder; Deadhang doc 06 ↔
   Crew Blueprint doc 04 (shared safety standards, different purpose).
5. Mark Stage 2 complete when the definition-of-done is met; update CHANGELOG +
   DECISION_LOG.

## What I need from the owner to proceed

1. **Approve the folder + structure** (`companies/crew-blueprint/`, the 9 docs) — or adjust.
2. A few facts for the ⚠️ items (only what's comfortable in a public repo):
   - The **authority/safety model** (`cb-1`): how do you want the trust framework
     framed — "educational reference aligned to industry standards, not a
     certifying authority"? Any liability language you want stated up front?
   - The **content pipeline** (`07`): the standard steps a lesson goes through
     (draft → self-review → scored QA → publish-ready) — confirm or correct.
3. Confirm what stays **referenced** vs. lives elsewhere (full lessons + brand
   assets in `Contentrepo`; only catalog/scope in this public repo).
