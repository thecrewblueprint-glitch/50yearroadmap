# Changelog

The shared work log for this repository. Every agent (and the owner) records
what changed here so the next collaborator can pick up with full context.
See `AGENTS.md` for the rules. Newest entries first.

**How to add an entry:** at the top of the "Entries" section, add a dated
block. Say *what* changed, *why*, and note any *follow-ups* or *open threads*.
Keep it short but specific. One block per working session is fine.

---

## Open threads

Things known-incomplete or awaiting a decision. Clear them when resolved.

- **Watcher remains manual.** The current branch/journey watcher exists and writes
  proposals only to `data/roadmap/watcher-proposals.json`; it is not wired into
  CI and never edits `roadmap.json` automatically.
- **Proposal review backlog.** The latest watcher output contains candidate work
  items/blockers for human review. Approved items still need to be promoted by
  hand into `roadmap.json`.

---

## Entries

### 2026-07-22 — BUILT: "Dock Sweep" — first playable scene (build ladder rung 2)
- Built the first **embodied playable scene** the owner envisioned: a single-file
  canvas game where the learner **drags to look around a load-in dock wider than
  the screen** and reacts to what happens while they're looking elsewhere — a
  forklift crossing, a case rolling loose, a load swinging overhead, the lead
  calling out. Off-screen events raise **edge arrows**; each hazard must be pointed
  at before its timed ring runs out. An **AWARENESS meter** and score drive a
  debrief with ratings ("SENT HOME EARLY" → "CREW CHIEF NOTICED YOU"). Gear
  (road case, barricade, truss, shackle) is **tappable to learn** what it is and
  how a green hand treats it. Teaches the two things the owner named: **listening**
  (lead calls) and **keeping your head on a swivel** (moving hazards). Fully
  self-contained — no backend, no external requests; works on a phone.
- This is **rung 2** of the build ladder in `05_platform.md` (cards → **playable
  2D scenes** → first-person 3D → full sim/VR).
- **Smoke-tested in Chromium via Playwright:** syntax clean, zero page/console
  errors, 0px horizontal overflow, start → play → end → replay all transition,
  camera pans the full 2400px world, hazard alerts score and feed AWARENESS,
  debrief renders a real score/rating/takeaway, gear inspection popup works.
- Delivered to the owner privately — the scene stays out of the public repo per
  the doc-09 guardrail; the repo records that it exists. Awaiting the owner's
  vision-check on whether the *feel* lands before the other lessons become scenes.
- `cb-5` note updated to reflect the first scene prototype exists.

### 2026-07-22 — Captured the embodied-game vision + build ladder (Crew Blueprint)
- Owner's full delivery vision: an **actual playable game with characters and
  scenes** — learners look around a jobsite, see the items being taught, and
  *experience* why listening and head-on-a-swivel matter. Market-validated
  (Interplay/Transfr win on simulation).
- Recorded in `companies/crew-blueprint/05_platform.md` with an honest 4-rung
  build ladder: cards (done) → **playable 2D scenes (next)** → first-person 3D →
  full sim/VR. Each rung gated on the previous proving the feel.
### 2026-07-22 — cb-5 v2: full UI/UX audit on the gamified module prototype
- Owner flagged UI/UX issues + scrolling errors. Audited and fixed: **scroll position
  now resets to top on every screen/step change** (the main bug — you landed
  mid-page after each transition); after grading a list, the view scrolls back to
  the marked answers; replaced the `confirm()` reset (silently blocked in sandboxed
  viewers) with a two-tap inline confirm; correct-answer reveal on the sorting game
  now shows green (was amber = confusable with "your pick"); review-run messaging
  fixed (a failed replay no longer says "no XP banked" when the earlier pass
  stands, and banked XP now shows the true delta); mobile polish (no double-tap
  zoom, no text-selection on taps, horizontal-overflow guard, safe-area padding,
  fade-in transitions); multi-select check button disabled until a pick, with a
  live selected-count.
- Re-verified end-to-end in Chromium: scroll reset confirmed (859px → 0), 0px
  horizontal overflow, L1 + L2 played through (310 XP), green reveal on wrong
  sort, two-tap reset works, zero page errors. Delivered v2 privately.
### 2026-07-22 — BUILT: first gamified module prototype (cb-5)
- Built the first playable Crew Blueprint prototype: **Module 1 "Your First Work
  Call" as a single-file gamified skill tree** — 5 lesson nodes (learn → do →
  check → result) using the owner's real lesson content, one interaction per node
  (task multi-select, call-type sorting, scenario judgment), knowledge checks,
  **80% pass gates**, XP/streak/rank (Green Hand → Crew-Ready), localStorage
  progress, industrial dark theme, fully self-contained (no backend, no external
  requests). Footer carries the no-certification / employer-authorization
  disclaimer.
- **Smoke-tested end-to-end in Chromium via Playwright:** tree renders (5 nodes,
  4 locked), lesson 1 played to 100%, +170 XP banked, node 2 unlocked, progress
  persisted, zero page errors.
- Delivered to the owner privately — the full lesson content stays out of the
  public repo per the doc-09 guardrail; the repo records that it exists.
- `cb-5` → in_progress (remaining: owner vision-check → iterate → deploy).
### 2026-07-22 — Recorded the owner's vision & source (deep context)
- Added `data/roadmap-deep-context/2026-07-22-owner-vision-and-source-deep-context.md`
  — the owner's own words on where the vision comes from and the mandate for the
  system: **record the daily insights faithfully, and go beyond storage — turn the
  words into real things people can benefit from.** Companion to the operating-truth
  doc. Verbatim, public-safe.
### 2026-07-22 — Draft the Homes for Hands 'Live & Travel Free' guide (hs-1)
- Wrote `data/roadmap/homes-for-hands-guide.md` — the caravan-facing resource guide
  (the tangible form of the care seed): finding free/cheap places to sleep (The Dyrt,
  public-land dispersed camping, finder apps), host networks (Harvest Hosts,
  Escapees), community (Xscapers, Workamper), work-for-stay, and **where to turn for
  real help** (Roadie Clinic, Backline, HOWA, 211, 988) + the Homes for Hands
  mutual-aid ethos and honest limits. Public-safe; living/verify-before-use.
- `hs-1` → in_progress; linked from `connections.md`. Validator: PASS.
### 2026-07-22 — Homestead: retire the build, keep a light care seed (major reshape)
- Owner realization/decision: the abundant US van-life resource ecosystem already
  solves the caravan's travel & lodging (free/cheap, at scale), so the physical
  Homestead **build is retired** and **land acquisition is off the table** — no land,
  no build, no business, no framework. Recorded in `governance/DECISION_LOG.md`.
- **Reshaped the roadmap's endgame:** retired the `land-acquisition` branch (removed
  branch + journey milestone + Phase-2 ref); reframed the `homestead` branch as the
  **Homes for Hands care seed** (a 'live & travel free' resource guide + a mutual-aid/
  ally ethos; hs-1..hs-4 rewritten, all low/light). Rewrote north_star, end_goal,
  Phase 2 ('Homes for Hands - the care seed'), and the final journey milestone
  ('Care for the caravan'). 6 branches now; validator PASS (0 warnings).
- Updated `partnerships/research/04` (strategic implications → don't build it),
  `governance/CURRENT_STATE.md`, and the `connections.md` Homestead section.
- The care seed preserves the part existing resources don't cover — crew who need
  help — closest to the owner's 'for others, out of love' purpose.
### 2026-07-22 — Reframe RV/camping services as resources; add The Dyrt; name "the caravan"
- Owner distinction: Escapees / Harvest Hosts (and similar) aren't partnership
  targets — they're **resources the caravan uses** for lodging/logistics, or
  **models** to study. Added a `resource` status to `connections.md` and
  recategorized Escapees, Harvest Hosts, Workamper accordingly.
- Added **The Dyrt** (owner-provided) — US camping app / free-campsite finder — as
  a lodging resource for the caravan (connections.md + `partnerships/research/04`).
- Captured **"the caravan"** = the owner's term for the mobile community of
  traveling live-event workers the Homestead forms and serves. Split the Homestead
  research leads into partners/allies vs. resources/models. Validator: PASS.
### 2026-07-21 — Add Escapees + Harvest Hosts to Homestead research/leads
- Owner request. Added **Harvest Hosts** (+ Boondockers Welcome) to
  `partnerships/research/04` and `connections.md` — the **distributed host-network**
  model (membership + reciprocity, ~9,700 host locations, no land ownership): the
  complement to Escapees' **own-the-land** co-op model. Framed the two together
  (own a small base + network wider hosts) and noted both as possible partners.
- Elevated **Escapees/Xscapers** from model-only to a possible partnership lead.
  All deferred (build-first). Validator: PASS.
### 2026-07-21 — Reviewed & mapped the Crew Blueprint content (it exists)
- Owner: the ground-work content is already built (scattered across accounts/computer,
  "no idea which account has what"). Reviewed via the Drive connector.
- **Found it, and it's on-target.** All Crew Blueprint content the connector sees is
  in the owner's personal Google account, in a hub folder "Course Data Packages"
  (organized by discipline). **Course 1 'Your First Work Call' Module 1 is COMPLETE**
  — 5 entry-level, US-context ground/field-hand lessons in structured JSON
  (`module-01-lessons.json`), QA-reviewed. Lighting/video/rigging/hazard folders
  started; WordPress backups separate.
- Added `companies/crew-blueprint/09_content_inventory.md` — a public-safe map of
  what exists, where, and how ready it is to gamify (no lesson bodies). README +1.
- Reconciled roadmap: `cb-4` now notes Module 1 complete; `cb-5` reframed as a
  **packaging** task (wrap the existing JSON in the gamified shell), not authoring.
- PII: abstracted the account (owner's personal Google account) — no email in repo.
  Validator: PASS.
### 2026-07-21 — Crew Blueprint repositioned: US-standard, ground-up, first-mover
- Owner correction: **do not lead with rigging.** Build to **US industry standards**
  and teach **ground-up** — start with field-hand/ground fundamentals (the owner's
  real expertise); specialized disciplines and rigging come far later. Aim: the
  **first US-standard gamified training** for the trade (Tech Crew HQ proved the
  format but is Australia-only).
- Recorded in `governance/DECISION_LOG.md`. Updated roadmap crew-blueprint
  (ultimate_goal, current_state, `cb-4`, `cb-5` — MVP is now a ground-work
  fundamental, not rigging), docs `00/01/03`, and corrected
  `partnerships/research/01` (the earlier "lead with rigging" call). Validator: PASS.
### 2026-07-21 — Recorded the owner's operating truth (deep context)
- Added `data/roadmap-deep-context/2026-07-21-owner-operating-truth-deep-context.md`
  — the owner's own words on how they work ("ideas → words → creation … for myself
  and for others out of love"), recorded verbatim at their word that it's "just
  facts of my being." The why beneath every branch. Public-safe; no private detail.
### 2026-07-21 — Capture all partnership leads as future considerations (build-first)
- Owner decision: **build more himself before approaching partners.** Recorded in
  `governance/DECISION_LOG.md`; noted at the top of the `partnerships/` playbook.
- Broadened `data/roadmap/connections.md` from Homestead-only into the **cross-company
  leads registry** — all research leads added, organized by company (Deadhang staffing,
  Crew Blueprint training, Production Atlas data, Homestead), with Fit + status
  (`future`/`model`/`reference`/`contacted`) and the build-first posture stated.
- Roadmap: added `dh-13` and `cb-6` (partnership-lead items, `moved_later`) via the
  promote helper and wired into milestones m5/m4; reframed `pa-4` → `moved_later`;
  updated `hs-4` note (Escapees co-op-land model; further outreach deferred).
- Nothing set to active outreach except The Roadie Clinic (already contacted).
  Validator: PASS (0 warnings); no emails in roadmap.json.
### 2026-07-21 — Partnership research: labor-staffing, industry-intelligence, nomadic-community
- Completed the sector sweep (docs 02–04 in `partnerships/research/`):
  - **Labor staffing (Deadhang):** mature national market (Rhino, Crew One, Upstage,
    Show Support, Stage Crew, ShowPros). These are competitors *and* Deadhang's best
    partners — Deadhang already works through Upstage (1099) and Crew One (portfolio).
    Validates Track 1 (become preferred subcontractor); warm starts exist.
  - **Industry intelligence (Production Atlas):** job-board/directory lane taken
    (ProductionHUB 150k+, Giggs); premium touring data owned by Pollstar (Live
    Nation). None do Atlas's worker-facing structured department/pathway/regional
    intelligence — confirms the "not a job board" positioning and the whitespace.
  - **Nomadic community (Homestead):** live-event-specific version is whitespace, but
    **Escapees RV Club / Xscapers** is a near-exact proven template (member co-op
    LAND parks incl. Benson AZ; working-nomad subgroup; 40 yrs). Study + apply.
- Captured partner leads per sector for `connections.md`. All four sectors now have a
  first-pass landscape study.

### 2026-07-21 — Partnership research: gamified-learning landscape
- Started `partnerships/research/` (sector-by-sector "who already built a version
  of this idea" landscape research). First study: gamified stagehand/rigging/
  production training for The Crew Blueprint.
- **Key finding:** the niche (pro live-music crew × real rigging × real
  gamification × US) is essentially open. Closest analog = **Tech Crew HQ** (AU;
  light gamification, no rigging, education market — a potential partner/licensor,
  not a direct competitor). Proven model = **Interplay Learning / Transfr**
  (gamified trades at scale, other trades). The traditional field (Rock Lititz /
  Academy of Live Technology, ITI, Bigger Hammer, Rugged Training, USITT, ETCP) is
  best read as content/credibility **partners**, not competitors.
- Captured partner leads for `connections.md`; validates the `cb-3` gamified
  direction and points Crew Blueprint to lead with rigging.

### 2026-07-18 — Partnership Playbook: framework laid down
- Started a cross-company **Partnership Playbook** (`partnerships/`) — the strategic
  system for using partnerships to accelerate growth across Deadhang, Crew Blueprint,
  Production Atlas, and the Homestead.
- Built the **framework first** (per owner's systematic approach): README index with
  the strategic spine (rent-the-infrastructure, find one anchor, sequence by leverage)
  + nine scoped stubs (strategy, value proposition, partner types, targeting, the
  offer, outreach, pipeline, deal structures, risks & review). Each stub defines its
  purpose and how it connects to its neighbors, so the whole coheres before filling.
- Sections will be filled **one at a time, in order**, starting with 01_strategy.
  Public-safe (strategy + templates only; partner specifics stay private); the live
  target list remains `data/roadmap/connections.md`.

### 2026-07-18 — Decision: Crew Blueprint delivery = gamified static, not an LMS
- Owner decided a **gamified, static, browser-based** delivery over an LMS —
  simpler and it sidesteps the platform instability that blocked the LMS
  (no accounts/DB/backend; progress in localStorage). Discipline/pathway map =
  skill tree; mechanics start highly simplified and grow.
- Recorded in `governance/DECISION_LOG.md`; **resolved OD-4** (moved out of
  `OPEN_DECISIONS.md`).
- Roadmap: reframed `cb-3` ("Build gamified static learning delivery…", status
  moved_later→not_started), rewrote crew-blueprint current_state + blockers, and
  **added `cb-5`** ("Ship first gamified MVP module from an existing packet") —
  added via the new promote helper (dogfood), then wired into journey milestone m4.
- Reconciled the Crew Blueprint docs to the decision: `05_platform` (full
  gamified-delivery section; LMS/heavy-infra reframed as retired/gated), plus
  `00_overview`, `01_learning_model` (skill tree), `07_content_pipeline`,
  `08_growth_model`, and the folder README. Validator: PASS (0 warnings).

### 2026-07-18 — Add promote helper + document the two-path update workflow
- Built `scripts/promote-proposals.py` — the human-in-the-loop "apply" step that
  the pipeline was missing. Reads owner-approved changes from
  `data/roadmap/promotions.json` (status updates, new work items, new blockers),
  writes them into `roadmap.json` with **auto-assigned IDs** and enum checks, runs
  the validator, and **rolls back on any failure** (including the public-safety/PII
  scan). Resets `promotions.json` on success so nothing double-applies. `--dry-run`
  previews. It is now the only script that writes `roadmap.json`.
- Added `data/roadmap/promotions.json` (empty template).
- Tested end-to-end: apply (auto-ID `dh-13`, status change, blocker) → validator
  PASS; PII case → rolled back, no leak. Reverted all test data.
- **Documented the two update paths** (evidence-based via the watcher; real-world
  progress the watcher can't see) in `WATCHER_GUIDE.md`, and synced the pipeline
  description across `AGENTS.md`, `README.md`, and
  `companies/personal-operations/03_ai_pipeline.md`.
- Clarifies the design: the watcher is not a reality-sync — it proposes from
  curated digests only; the promote helper applies what you approve.

### 2026-07-18 — Refresh dashboard + timeline currency (roadmap.json)
- Brought the live dashboard/timeline source up to date after the Deadhang document work:
  - `generated_at` 2026-07-09 → 2026-07-18.
  - Deadhang `current_state` rewritten to reflect canonical docs, the drafted IC
    agreement (attorney-review gate), Mesa business license, live tracker, and
    current-state plan/SOPs; `status_percentage` 60 → 63; `critical_blocker` refined.
  - `this_week_focus` refreshed (dh-5/dh-8 finalize docs + taxes; dh-10 attorney
    review; cb-4/pa-3/po-2) — the old dh-1/dh-2 focus was stale.
  - **30-day window** re-themed "Finalize the business foundation" (its old outcomes
    — structure reviewed, tracker live, dashboard clean — are now met); focus
    dh-5/dh-8/dh-10.
  - **60-day window** re-themed "Harden the contractor tools" and repointed off the
    completed ct-2/ct-4 to the remaining ct-1/ct-3.
- Validator: PASS (0 warnings); all focus/journey references resolve.

### 2026-07-18 — 30-day work: closed the Deadhang document gaps (P&L, SOPs, marketing)
- Filled the four gaps from the document register (doc 12):
  - **SOPs** → new repo doc `companies/deadhang-labor/14_sops.md` (public-safe):
    inquiry→booking→pre-gig→show-day→invoice→payment→tracking→recordkeeping, plus
    gated contractor-engagement and merch/TPT procedures.
  - **Profit & Loss** → `Deadhang_Labor_LLC_Profit_and_Loss_2026_TEMPLATE.xlsx`:
    monthly, formula-driven, Schedule-C-aligned. Delivered for private storage
    (fill with real figures in Drive, not the public repo).
  - **Marketing / content calendar** → `Deadhang_Labor_LLC_Marketing_Content_Calendar_TEMPLATE.xlsx`:
    dated calendar with drop-downs + an ideas/themes backlog. Delivered privately.
  - **Website privacy/terms** → already closed (exist live; see prior entry).
- The two `.xlsx` templates are deliverables kept in private storage (not committed
  to this public repo); doc 12 records that they exist. README Deadhang count 14→15.

### 2026-07-18 — Website update handoff for the Deadhang site developer
- Wrote `companies/deadhang-labor/handoffs/2026-07-18-website-portfolio-disclaimer.md`
  — a self-contained coder handoff to (1) add the trademark/role disclaimer to
  `portfolio.html` (drop-in HTML + fallback CSS), (2) re-frame captions to lead
  with the labor role (current→suggested table, owner confirms exact role), and
  (3) verify the mobile menu + HTTPS. Explicitly scopes OUT the legal pages and the
  brand. Public-safe.

### 2026-07-18 — Evaluated deadhanglaborllc.com content
- Reviewed the live site (home, about, portfolio, services, contact, and the legal
  pages) via WebFetch.
- **Legal pages already exist and are complete** — Privacy (names Formspree/Google
  Fonts, no tracking cookies, AZ/Maricopa, effective 2026-06-15), Terms &
  Disclaimer (IC status, IP, liability, AZ law), Cookie Policy. The earlier
  "website privacy/terms" gap is **closed** (doc 12 updated).
- **Updated doc 07** (digital assets): documented the legal pages, marked resolved
  items (Formspree named; no tracking cookies), and recorded the two remaining
  website items.
- **One real recommendation:** add a **trademark/role disclaimer on the portfolio
  page** (big named events/artists/tours are used with no on-page nominative-use
  disclaimer) and lead captions with the labor role rather than build/deployment
  verbs. Recorded as a brand standard (doc 08) with drop-in disclaimer text (doc 07).
- Content/voice otherwise strong and correctly signals a solo IC operator.
  Validator: PASS; scans clean.

### 2026-07-18 — Add Deadhang current-state business plan (living doc)
- Owner: keep the aspirational Vision Business Plan as-is; add a **living
  current-state plan**. Created `companies/deadhang-labor/13_current_state_business_plan.md`
  — mirrors the vision plan's structure (mission → operating model → foundation →
  financials → risk → roadmap) but grounded in today's reality (solo operator,
  direct + staffing-company work, insurance deferred, documents being finalized),
  plus a "bridge: current state → vision" staged path. Public-safe (no figures/PII),
  self-updating rule stated. README Deadhang count 13→14. Validator: PASS.

### 2026-07-18 — 30-day work: reviewed existing Deadhang business documents
- Owner asked to review the business documents already created (they live in
  private Google Drive, not the repo). Reviewed the real document set via the
  Google Drive connector.
- **Found more than the roadmap credited:** formation docs (Articles, EIN CP-575,
  Operating Agreement), a **City of Mesa business license application** (May 2026,
  fee paid), Client MSA, a thorough **Master Independent Contractor Agreement**
  template (23 sections, AZ governing law), W-9/direct-deposit/onboarding forms,
  Financial Tracking System, Master Invoice Template, a live "2026 Work, Contracts
  & Payments Master Tracker," and a comprehensive Business Plan.
- **Added `companies/deadhang-labor/12_document_register.md`** — a public-safe
  index of what exists + a finalization checklist (de-dup, consolidate account
  ownership, attorney review, fill gaps). No PII/financials.
- **Reconciled canonical docs/roadmap to reality:**
  - Doc 11: corrected the licenses note — a Mesa business license **was applied
    for** (previously said "none"). Kept TPT-not-required-for-services.
  - Doc 05: the Client MSA and the IC agreement **templates exist**; remaining
    gate is Arizona attorney review.
  - Roadmap: `dh-2` not_started→in_progress (live tracker exists); `dh-5` and
    `dh-10` why-text updated to reflect existing docs + finalization/legal-review
    gate; added a "business documents need finalization" blocker.
- Flagged the **Business Plan as aspirational** (staffing agency ahead of current
  solo reality) — use as target (doc 10), not current state.
- README Deadhang doc count 12→13. Validator: PASS; PII re-scan clean.

### 2026-07-18 — Repository audit + post-audit cleanup + Stage 5
- **Audit.** Full repository audit recorded in `governance/AUDIT_2026-07-18.md`
  (structure, roadmap integrity, docs, git history, per-project status, tech debt,
  governance). Verdict: healthy — validator passes, all roadmap refs resolve, zero
  broken links, clean single-trunk history. Gaps were currency/hygiene. Then
  executed the recommended fixes:
- **README** refreshed to surface `companies/` canonical documentation + a 5-of-5
  status table.
- **CI gate added** — `.github/workflows/validate-roadmap.yml` runs
  `validate-roadmap.py` on push/PR touching the roadmap, schema, or validator.
- **Legacy pillar debt removed** — deleted `scripts/build-roadmap.py`,
  `data/roadmap/{vision.json,pillars.json}`, and the `compiled.json` artifact;
  cleaned `.gitignore`; updated the retired-model notes in AGENTS/CHATGPT_HANDOFF/
  DATA_SAFETY_POLICY to say "removed 2026-07-18". (`deep-context-decision-sources.json`
  is NOT legacy — used by the watcher — retained.)
- **Stale docs retired** — deleted `UI_UX_ANALYSIS.md` (retired 8-pillar model)
  and `CLAUDE_FRAMEWORK_AUDIT_HANDOFF.md` (superseded). Kept
  `INTERACTIVE_DASHBOARD_SPEC.md` (unbuilt future value; now referenced from the
  personal-operations docs).
- **Stage 5 BUILT — Personal Operations / command center.** Scaffolded
  `companies/personal-operations/` + README + 5 docs (overview, data model,
  dashboard, AI pipeline, governance, growth model). Synced the roadmap
  `personal-operations` branch to reality: `po-1` (dashboard) / `po-3` (90-day) /
  `po-4` (layered views) → `completed`; `po-2` → `in_progress`; state rewritten;
  status 35→65; repointed this_week_focus + 30-day focus off the completed po-1.
  Added `STAGE_5_SCOPE.md`.
- **Watcher-output convention documented** (in `companies/personal-operations/03_ai_pipeline.md`):
  keep tracked, revert incidental regeneration.
- **governance/README + CURRENT_STATE** updated: Stage 0 marked complete, Stages
  1–5 indexed with their `companies/` folders. **All five companies now have
  canonical documentation.** Validator: PASS (0 warnings).

### 2026-07-18 — Stage 4 BUILT: Contractor Tools canonical documentation
- No fresh owner review this time — reconstructed from existing repo evidence
  (roadmap `ct-1..ct-4` + the July digests' invoice/calendar architecture
  decisions). Future/unconfirmed pieces (team coordination) marked as such.
- Scaffolded `companies/contractor-tools/` and drafted README + 6 canonical docs:
  00_overview, 01_invoice_generator, 02_payment_tracking,
  03_calendar_infrastructure, 04_architecture_principles, 05_growth_model.
  Public-safe: describes the tools, never their data (no amounts/clients/PII).
- Captured the grounded specifics: 1099 invoice generator (single-file HTML;
  text → PHP/OpenRouter parse → validated JSON → human review → deterministic
  calc → fixed PDF; payment terms Net 15/30/45/60 + Due on Receipt; AI never
  controls totals; parser/PDF must-not-drift guardrail), payment tracking (`ct-4`
  done), calendar ICS feeds (Google/Apple/Outlook) + the authorization-renewal
  service-layer design (`ct-3`), and the MVP-first/anti-overbuild principles
  (`ct-1`, `ct-2`).
- Light roadmap sync (current_state rewritten + canonical-docs pointer; statuses
  already accurate). Added `STAGE_4_SCOPE.md`, updated CURRENT_STATE. Validator: PASS.

### 2026-07-18 — Stage 3 BUILT: Production Atlas canonical documentation
- Owner supplied the Production Atlas completed-work review (go-ahead + source
  material, same flow as Stage 2).
- Scaffolded `companies/production-atlas/` and drafted README + 9 canonical docs:
  00_overview, 01_architecture, 02_repository_strategy, 03_research_methodology,
  04_application, 05_departments, 06_validation, 07_data_policy, 08_growth_model.
  Public-safe: documents the **system**, never the sensitive research payload (no
  private contacts/pay/NDA/client data/rumors — the same things the app itself
  must not expose).
- **Synced roadmap production-atlas branch to reality** — the stale old-model
  language ("34 active items and 19 blockers", frontier pillar) is gone. Reframed
  as an **industry intelligence/research platform, not a job board**; rewrote
  role/ultimate_goal/current_state/blockers; `pa-1` (public/private boundary +
  verification) → `completed`; `pa-3` refocused on Scenic + datasets and `pa-5`
  on usability (both `in_progress`). Status 20→50. Repointed this_week_focus,
  90-day focus, and journey m3 off the completed pa-1. Added `STAGE_3_SCOPE.md`.
- Updated `governance/CURRENT_STATE.md`. Validator: PASS (0 warnings).

### 2026-07-18 — Stage 2 BUILT: The Crew Blueprint canonical documentation
- Owner supplied a full completed-work review that answered both open scope
  questions (authority/safety model = job-readiness, not certification; content
  pipeline = topic → plan → NotebookLM research → Claude draft → Manus QA → DOCX
  packet → archive). Green-lit the build.
- Scaffolded `companies/crew-blueprint/` and drafted all 9 canonical docs:
  README + 00_overview, 01_learning_model, 02_authority_and_safety, 03_curriculum,
  04_standards_alignment, 05_platform, 06_brand, 07_content_pipeline,
  08_growth_model. Public-safe throughout (no certification claims; catalog/scope
  only, not full paid lessons; no PII/pricing).
- **Synced roadmap crew-blueprint branch to reality:** the key correction is that
  it is **no longer blocked by software** — platform work (`cb-3`) set to
  `moved_later` (intentionally deferred); authority model (`cb-1`) → `completed`;
  content mapping (`cb-2`) and packet production (`cb-4`) → `in_progress`.
  Rewrote current_state/critical_blocker/blockers (constraint is now content
  volume). Bumped status 25→35. Repointed this_week_focus, 90-day focus, and
  journey m4 off the completed cb-1 to the active content work.
- Updated `governance/CURRENT_STATE.md` (Crew Blueprint line + snapshot date) and
  marked `STAGE_2_SCOPE.md` BUILT. Validator: PASS (0 warnings).

### 2026-07-18 — Stage 2 scoped: The Crew Blueprint canonical documentation
- Added `governance/STAGE_2_SCOPE.md` (mirrors Stage 1 structure): proposed
  `companies/crew-blueprint/` folder + 9-doc set, per-doc source/readiness table,
  public-safe guardrails (**no certification claims**; describe course
  architecture/catalog but do **not** reproduce full paid lessons), source-material
  map, build sequence, and the handful of owner-input gaps (authority/safety model,
  content pipeline steps).

### 2026-07-17 — Stage 1: Deadhang docs completed via owner interview
- One-item-at-a-time interview filled every "To confirm" fact:
  - `01` Legal — **formed 2026** (first year); AZ single-member LLC.
  - `03` Operations — work comes in via **direct relationships + staffing
    companies**; gig log lives in **Google Sheets/Drive + ChatGPT** (formalizing via `dh-2`).
  - `06` Safety — operating baseline: **OSHA / ANSI / ESTA / ETCP first + site
    requirements** (detailed procedures still build via `dh-11`).
  - `08` Brand — exact navy/gold from the **site CSS** (source of truth); noted
    per-project CSS schemas (Deadhang, Crew Blueprint, roadmap, Production Atlas).
  - `11` Compliance — **no TPT/business license now** (service labor); **merch
    t-shirt launch (`dh-12`) triggers likely AZ TPT registration** — evaluate before selling.
- Docs 00, 01, 02, 03, 04, 07, 08, 09, 10, 11 are Documented. Remaining: `05`
  (contractor framework) and `06` (detailed procedures) complete as `dh-10`/`dh-11`
  land; optional tagline. Stage 1 substantially complete.

### 2026-07-17 — Stage 1 first pass: Deadhang canonical documentation drafted
- Scaffolded `companies/deadhang-labor/` and drafted all 12 canonical docs
  (README + 00 overview → 11 compliance/risk): legal structure, services,
  operations, financial systems, contracts, safety, digital assets, brand,
  revenue streams, growth model, compliance/risk.
- Ready docs written fully from repo context; in-progress/gap items marked
  "To confirm (owner)" rather than blocking. Sensitive detail (income, account
  numbers, tax records, brand assets) is **referenced**, not reproduced.
- PII-scanned clean (no emails, dollar amounts, SSN, or full name).
- Remaining for Stage 1 completion: owner fills the "To confirm" facts;
  safety + contractor-framework docs finish as that work lands.

### 2026-07-17 — Stage 1 scope drafted (Deadhang canonical documentation)
- Added `governance/STAGE_1_SCOPE.md`: goal + definition-of-done, proposed
  `companies/deadhang-labor/` folder, a 12-document canonical set (with per-doc
  source + readiness), public-safe guardrails, source-material map, and a build
  sequence. Awaiting owner sign-off on structure + a few ⚠️ facts before drafting.
- No roadmap/data changes; scoping only.

### 2026-07-17 — Governance docs added + stale docs refreshed (Stage 0 cont.)
- Added the genuinely-new governance docs (the ones not already covered):
  `governance/OPEN_DECISIONS.md`, `KNOWN_RISKS.md`, `LESSONS_LEARNED.md`.
- Evaluated the docs that already fill the other proposed roles and refreshed the
  stale ones (Stage 0 = remove outdated info):
  - `README.md`: it wrongly listed the watcher, `/data/schema`, and
    `/data/roadmap-deep-context` as "not yet in the repo" (all exist now); updated
    the pipeline (watcher/prioritizer/validator are built), the data-model snapshot
    (added north_star/end_goal/phases/journey/thirty_sixty_ninety + full status
    enum), and added `/governance/`.
  - `CHATGPT_HANDOFF.md`: refreshed to 2026-07-17 — added `completed`/`moved_later`
    statuses, the `thirty_sixty_ninety` field, the prioritizer script, governance,
    Deadhang AZ-LLC facts, Homestead outreach, and the GPT-paused note.
- Did NOT add duplicate docs: SESSION_SUMMARY (=CHANGELOG), AI_HANDOFF
  (=CHATGPT_HANDOFF), NEXT_ACTIONS (=roadmap this_week/30-60-90/backlog),
  EXECUTIVE_SUMMARY (=README + governance CURRENT_STATE) — the existing files serve
  those roles.

### 2026-07-17 — Stage 0: roadmap synchronization + governance framework
- Acted on the ChatGPT Stage 0 handoff (GPT paused — GitHub connector issue;
  Claude solo on the repo for now). GPT's session was read-only; nothing had
  been committed.
- **Roadmap synchronized with reality** (`roadmap.json`): made Deadhang's
  Arizona single-member LLC / Schedule C / cash-basis identity explicit
  (corrected any drift toward Wisconsin); `dh-1` business-structure audit →
  in_progress (~90%); `dh-6` client MSA → completed; added `dh-9` insurance
  (`moved_later` — deferred, not forgotten), `dh-10` independent-contractor
  framework (in_progress), `dh-11` safety documentation (in_progress), `dh-12`
  print-on-demand merch line under Deadhang (in_progress, no new LLC); refreshed
  current_state/blockers; Deadhang 45% → 60%. Validator passes.
- **Governance framework established** in `/governance/`: `README.md` (purpose +
  Stage 0–5 plan), `CURRENT_STATE.md` (snapshot), `DECISION_LOG.md` (structure,
  tax, insurance, print-on-demand, single-source-of-truth decisions), and
  `handoffs/2026-07-17-chatgpt-stage0-handoff.md` (the source handoff, stored
  verbatim). `AGENTS.md` §8 now points to it.
- Noted that Stage 0's "collaboration standards" and "AI handoff system" were
  already largely built (`AGENTS.md`, `CHANGELOG.md`, `CHATGPT_HANDOFF.md`).
- **Open:** remaining proposed governance docs (EXECUTIVE_SUMMARY, NEXT_ACTIONS,
  OPEN_DECISIONS, KNOWN_RISKS, LESSONS_LEARNED, SESSION_SUMMARY) — several
  overlap with existing files; confirm with owner before adding. Stages 1–5 not
  started (Stage 0 first, by design).

### 2026-07-16 — Add nomadic-movement lead: Van Life Campgrounds
- Owner-supplied lead for the Homestead / nomadic-movement vision.
- Added `hs-4` to the Homestead branch: "Investigate Van Life Campgrounds
  (vanlifecampgrounds.com) as a nomadic-movement connection" (HIGH, not_started),
  mapped onto milestone m8. Website + purpose only — validator passes, no email
  in roadmap.json.
- Recorded the full contact (org, website, info@ business email, purpose) in a
  new `data/roadmap/connections.md` leads log (business contacts only; no private
  individuals). Ran a reputation check on the domain: verdict unknown, but
  registered 4+ years (established, not flagged malicious).

### 2026-07-16 — Add sanitized July MTD work report to the evidence layer
- Stored a **public-safe** digest of the owner's July 1–16 month-to-date report
  as `data/raw-reports/2026-07-16-july-mtd-work-report-digest.md`.
- Redacted (per DATA_SAFETY_POLICY, repo is public): income amounts + per-client
  pay breakdowns, bank/financial details, personal/third-party names and emails,
  reservation/receipt numbers and lodging specifics, and secret names. The full
  unredacted report stays private with the owner, not in this repo.
- Preserved work activity/decisions: 60 confirmed paid labor hours, tax
  knowledge base + 6 manuals, Upstage W-2→1099 transition, Festival/Production
  Atlas fixes, Crew Blueprint course-preview workflow, new print-on-demand
  clothing line + Printify automation spec.
- Verified the file contains no dollar amounts, emails, phones, or redacted names.

### 2026-07-16 — Add 30-day work summary to the evidence layer
- Stored the owner-supplied 30-day work summary (Jun 16 – Jul 16) as
  `data/raw-reports/2026-07-16-30-day-work-summary-digest.md`. Redacted one
  email address to keep it public-safe (DATA_SAFETY_POLICY); all other content
  preserved.
- Confirms/expands real progress across Deadhang (site live, 1099 invoice tool,
  affirmation calendar), Crew Blueprint (3 publication-ready course packets:
  RIG-201 96/100, Bridle Math, Predictive Hazard), Festival Atlas (Production
  Atlas — calendar sorting), and system org (Android file organizer).
- Not yet reflected into roadmap.json — flagged for owner-directed promotion
  (esp. Crew Blueprint course content, which shows more progress than the
  branch currently records). Watcher runs cleanly with the new digest present.

### 2026-07-09 — Record real Deadhang / Contractor Tools progress (owner update)
- Owner reported: website SSL/security fixed, portfolio clean and site running;
  an invoice + finance-tracking system is in place; last 3 years of finances
  sorted; tax filings being brought current.
- Reflected in roadmap.json:
  - `dh-7` (website hardening/SSL + portfolio) → **completed**
  - `dh-5` (business documents) → **in_progress** (finances sorted)
  - New `dh-8` "Resolve tax situation and bring filings current" → **in_progress**
    (HIGH), mapped onto milestone m1
  - Removed the resolved Deadhang blocker "Invoice tracking and payment systems
    incomplete"; refreshed Deadhang current_state; status 30% → 45%
  - Contractor Tools: `ct-2` (invoice MVP) and `ct-4` (payment tracking) →
    **completed**; refreshed current_state; status 15% → 35%
- Validator passes. Re-ran the prioritizer so the backlog reflects the changes.

### 2026-07-09 — Add proposal prioritizer (ranked "work-on-first" backlog)
- Added `scripts/prioritize-proposals.py`: a **read-only** ranker over the
  watcher proposals. It deletes nothing and never edits the proposals or
  `roadmap.json`; it writes `data/roadmap/proposal-backlog.md`.
- Ranking: by the owner's own 30/60/90 windows (earliest first), the current
  "you are here" branch leads its tier, blockers before work items, then
  confidence. Verified the proposals file is byte-identical before/after (md5).
- Also hides candidates already covered in the roadmap via a token-containment
  check (catches reworded promotions the watcher's title-only dedup missed) —
  e.g. the 3 Deadhang items promoted earlier no longer resurface. 117 raw
  candidates → 108 shown (9 already-covered hidden).
- Documented in AGENTS.md §5.

### 2026-07-09 — Promote 3 Deadhang foundation items from the watcher backlog
- Triaged the watcher proposals and promoted the 3 genuinely-new, public-safe
  Deadhang items that sharpen the current 30-day "stabilize the business
  foundation" window (the rest of GPT's suggested promotions already existed):
  - `dh-5` Assemble first-year business document system (plan, formation/EIN
    records, operating agreement)
  - `dh-6` Select and standardize a client MSA / service agreement
  - `dh-7` Finish website hardening (SSL/security) and portfolio cleanup
- Mapped all three onto milestone `m1` ("Solidify Deadhang's foundation") so they
  stay on the linear path (no orphan work). Left `this_week_focus` and the
  30/60/90 windows unchanged — sequencing those is the owner's call.
- Validator passes; items render on the timeline and in the Deadhang branch.
- Backlog note: many watcher candidates remain (mostly Production Atlas /
  Personal Operations); promote further items deliberately, not in bulk.

### 2026-07-09 — Formalize 30/60/90 into roadmap.json + add moved_later (owner-approved)
- Followed GPT's framework-audit handoff to fix the two-sources-of-truth issue.
- Moved GPT's 30/60/90 plan verbatim from the `ninety.js` sidecar into
  `roadmap.json` as a formal `thirty_sixty_ninety` field. `app.js` already read
  this field, so it now renders the 30/60/90 with no sidecar — deleted
  `ninety.js` and its `<script>` include (kept `ninety.css`). One source of
  truth, one renderer.
- Extended `scripts/validate-roadmap.py`: it now checks every
  `thirty_sixty_ninety.windows[].focus_step_ids` resolves to a real work item.
  Verified: live roadmap PASSes; a planted bad focus_step_id FAILs.
- Added the `moved_later` deferred-work status: valid in the validator, with
  dashed/muted styling in the work-item list and timeline dots so deferred work
  stays visible but off the active path. (Also added `completed` styling, which
  the validator already accepted.)
- Updated AGENTS.md §3/§4 to document the new field, the `moved_later` status,
  and the focus_step_ids integrity rule.

### 2026-07-09 — Claude framework audit handoff
- Added `CLAUDE_FRAMEWORK_AUDIT_HANDOFF.md` with a handoff note for Claude and
  the framework audit/recommended sequence to review before larger updates.
- The note directs the next agent to likely follow the audit path: promote the
  30 / 60 / 90 layer into `roadmap.json`, update validation, remove the sidecar
  data once formalized, add moved-later handling, and triage watcher proposals
  through the framework before promotion.
- No roadmap data or production page logic was changed, so no roadmap validation
  run was required.

### 2026-07-09 — 30 / 60 / 90 operating dashboard
- Added a dashboard section for a 30 / 60 / 90 execution layer above the End Goal
  section in `index.html`.
- Added `ninety.css` for the three-window dashboard cards and mobile layout.
- Added `ninety.js` as a standalone first-pass renderer. It reads current
  `roadmap.json` work items by ID, then displays 30-day, 60-day, and 90-day
  operating windows tied to existing branch work items.
- Updated `app.js` with a branch/journey-compatible renderer so the same section
  can later read from `roadmap.json.thirty_sixty_ninety` if the data model is
  formally promoted.
- `roadmap.json` was intentionally not changed in this pass; no roadmap
  validation run was required.

### 2026-07-09 — Documentation cleanup for current branch/journey system
- Cleaned the stale Open Threads section so it no longer claims the watcher or
  validator are missing after both were added.
- Updated the public data-safety policy to match the current repo-root dashboard
  and branch/journey model, removing retired pillar/docs/build-roadmap language.
- Updated the watcher detail cleanup so future proposal runs strip legacy
  pillar-model labels from candidate descriptions before writing proposals.
- `roadmap.json` was not changed, so no roadmap validation run was required.

### 2026-07-09 — Handoff doc for GPT
- Added `CHATGPT_HANDOFF.md`: a current-state orientation for a GPT collaborator
  (points to AGENTS.md/CHANGELOG, the branch/journey data model, the pipeline,
  the scripts, the commit-to-main rule, and safety/evidence rules). Replaces the
  stale pillar-model handoff that only exists on the legacy branch.

### 2026-07-09 — End-to-end flow audit + watcher accuracy fixes
- Audited the full pipeline (process-memories → watcher → validator → dashboard).
  Findings: memory processing is deterministic (8 archives → 518 sources → 880
  chunks, committed output accurate); validator passes on live and catches all
  planted violations; dashboard renders; watcher never writes `roadmap.json`.
- Watcher accuracy: confident mappings are correct (it rightly routes
  invoice→Contractor Tools and market-research→Production Atlas despite
  misleading titles). Found several clearly-mappable items being left unmapped
  because the keyword index ignored branch blockers.
- Fix: `branch_keyword_index` now also draws from each branch's `blockers` and
  `critical_blocker`. Result: unmapped 9 → 2 (the 2 left are genuinely
  ambiguous), already-tracked recognition 10 → 14, no new mis-maps.
- Polished the proposal `detail` field (stripped markdown bold / empty labels).
- Known/accepted: 1 of 124 mapped items is a borderline route (a "roadmap
  milestones" note whose sentence references Homes for Hands scored Homestead
  8 vs Personal-Ops 7). Left as-is — it's what human review catches, and
  title-weighting to fix it would regress the correctly-overridden titles.

### 2026-07-09 — roadmap.json validator
- Added `scripts/validate-roadmap.py` for the current model. Enforces the
  AGENTS.md §4 integrity rules (all step/branch/phase/focus refs resolve, no
  duplicate ids, every branch in exactly one phase, valid `you_are_here`) plus
  enum/range checks (priority, status, lifecycle, phase status, milestone state,
  status_percentage 0-100) and a public-safety scan (email/phone/SSN/card/real
  street address/HTML = error; owner personal name = warning).
- Exit code 0 = pass, 1 = errors, so it can gate commits/CI. Verified: the live
  roadmap PASSes with no warnings; a copy with 11 planted violations FAILs and
  each violation is reported.
- Wired into AGENTS.md §4 and the coordination checklist as the pre-commit step.

### 2026-07-09 — New watcher (branch/journey model)
- Built `scripts/roadmap-watcher.py` for the current model, using the retired
  pillar-model watcher only as reference (the old code was not merged).
- It loads current branches from `roadmap.json`, extracts work-item/blocker
  candidates from `data/raw-reports/*-digest.md`, maps them to branches,
  applies public-safe filtering (`data/schema/roadmap-public-safety.json`),
  de-dupes against the existing roadmap, and writes **proposals only** to
  `data/roadmap/watcher-proposals.json`. It never edits `roadmap.json`.
- First run: 133 claims → 114 new suggestions, 10 already-tracked, 9 unmapped,
  0 unsafe. Verified deterministic and that `roadmap.json` is untouched.
- Fixed a false-positive in the street-address safety check (the schema regex
  matched "way" inside words like "Pathway"); the watcher now uses a stricter,
  word-boundaried, case-sensitive address detector.
- Added `WATCHER_GUIDE.md`; updated `AGENTS.md` §5 (watcher now available as a
  proposal generator, run manually).

### 2026-07-09 — Port useful content from feature branch to main
- Brought over from `claude/repository-review-yvxvn5` (owner-approved):
  `data/roadmap-deep-context/` (2 files — resolves the dangling reference in
  `deep-context-decision-sources.json`), `data/raw-reports/` (10 curated
  digests), `DATA_SAFETY_POLICY.md`, and `data/schema/roadmap-public-safety.json`.
- Did **not** port the 7 root `.zip` archives — `main` already has them under
  `memories/` (correct location) and already processed. The feature-branch
  copies at repo root were misplaced duplicates.
- Did **not** port the old `docs/` dashboard copy (superseded) or the
  old-model watcher (being rebuilt instead).

### 2026-07-09 — Collaboration system + branch audit
- Rewrote `AGENTS.md` into a multi-agent operating guide: commit-to-`main` /
  no-branching rule, the current branch/journey data model, integrity rules,
  and a start/work/finish coordination checklist.
- Added this `CHANGELOG.md` as the shared work log.
- Audited all branches. Findings: `dev` has no unique commits;
  `claude/repository-review-yvxvn5` holds 40 unmerged commits (the old-model
  watcher, curated digests, deep-context files, governance/workflow docs, raw
  memory archives, and a now-superseded `docs/` dashboard copy). Nothing merged
  yet — logged under Open threads for an owner decision.

### 2026-07-09 — Dashboard rebuild & restructure (reconstructed from git)
This session predates the changelog; summarized from commit history.
- Rebuilt the dashboard around the **branch/journey model** and moved the live
  site to the **repo root** (Pages serves from root, not `/docs`); removed the
  duplicate `docs/` copy.
- Reframed into two lenses with a switcher: **Timeline** (linear path, now →
  Homestead) and **Dashboard** (branches grouped by phase, this-week focus,
  ecosystem flow). Added the **End Goal** section and restored the **Homestead**
  and **Land Acquisition** as Phase 2.
- Added **The Vision** page (`present.html`) — a read-only vision document —
  and a per-branch hub (`branch.html`) with a sitemap menu and focused
  sub-views (work / blockers / details).
- Removed the **Skills & Certifications** branch (teaching lives in The Crew
  Blueprint). Rebranded the header to **Deadhang Labor**; dropped 50-year
  framing.
- Hardened `app.js` (guards against missing fields, keyboard access,
  accessible pagination) and defused `scripts/build-roadmap.py` so it can no
  longer overwrite the live `roadmap.json`.
