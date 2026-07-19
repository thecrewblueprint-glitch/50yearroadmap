# 05 — Platform

**Status:** Documented. Delivery direction **decided (2026-07-18): gamified,
static, browser-based — NOT an LMS** (roadmap `cb-3`; `governance/DECISION_LOG.md`).

The key strategic fact: **The Crew Blueprint is no longer blocked by software
development.** Content, not engineering, is the priority (see doc 08).

## Delivery model — gamified static (the decision)

The learning experience is delivered as a **gamified, static, browser-based
experience**, not a traditional LMS:

- **Skill tree** — the discipline/pathway map (doc 01, `cb-2`) *is* the game
  structure: nodes to unlock across disciplines and levels.
- **Client-side progress** — learner progress (XP, streaks, completion) is stored
  in the browser (**localStorage**). **No accounts, no database, no backend.**
- **Why this over an LMS:** it is simpler *and* sidesteps the exact platform
  instability (accounts + DB + backend) that blocked the LMS. It also fits the
  Blueprint's model — rewarding *skill* with XP/badges, not issuing certification
  (consistent with doc 02).
- **Mechanics start highly simplified** — progress bar, XP, a streak, and one real
  interaction per node — and grow only once the format is proven.
- **Content source unchanged** — the canonical DOCX packets (doc 07) remain the
  single source of truth; gamified modules *wrap* that content.
- **First step (`cb-5`):** build one MVP module from an existing packet (e.g.
  Rigging Hardware ID) as a single static skill-tree node, before building the
  full tree.

Anything requiring accounts/cloud (cross-device sync, leaderboards, social) is a
*later* option, gated the same way heavier infrastructure always is here — only
when the simple version is genuinely the bottleneck.

## Website foundation (in place)

- **Domain** secured.
- **Hosting** in place (WordPress.com).
- **Theme** selected — *Extendable* — carrying the industrial visual direction
  (see doc 06).
- **Staging-first workflow** — changes are made on staging before production.
- **Industrial visual direction** applied.
- **Coming Soon strategy implemented** — public front while content is built.

## Plugin architecture (defined)

A **modular** architecture is decided (build deferred with the platform). The
modules:

- **Crew Blueprint Core** — shared foundation/services.
- **Site Shell** — presentation/navigation frame.
- **~~LMS~~ → Gamified delivery** — course delivery and progression is now the
  gamified static skill tree above, not an LMS module.
- **Resource Hub** — supporting resources and references.
- **Safety Notices** — surfacing safety callouts/disclaimers consistently.
- **Content Studio / Content Engine** — authoring and content generation.

The modular *philosophy* (separate concerns) still holds, but delivery is the
gamified static experience — the heavy LMS module is superseded.

## Retired / off the table

The gamified-static decision takes these out of the plan (not paused — replaced):

- **Legacy WordPress LMS** — retired in favor of gamified static delivery.
- **JSON import system**, **plugin debugging** — tied to the LMS build; no longer
  the path.

## Heavy infrastructure — only if the simple version hits real limits

Explicitly **not** needed for the gamified static approach; revisit only if
cross-device sync, leaderboards, or social features prove genuinely necessary:

- **User accounts / database** — the whole point of client-side progress is to
  avoid these; add them only if learners must sync across devices.
- **Laravel backend**, **AWS infrastructure**, **RAG**, **advanced search**,
  **mobile app** — later options, gated the same way all heavy infrastructure is
  here.

## Content surface

Finished course content is delivered as **gamified static modules** generated
from the canonical DOCX packets (doc 07) and served from the existing site. The
packet remains the source of truth; the module is a gamified view of it.
