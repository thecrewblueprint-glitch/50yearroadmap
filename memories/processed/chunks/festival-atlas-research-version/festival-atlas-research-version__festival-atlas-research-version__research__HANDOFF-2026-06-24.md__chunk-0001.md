---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__research__HANDOFF-2026-06-24.md__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/research/HANDOFF-2026-06-24.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 11109,
  "source_sha256": "f31867d4a2494be76cc4d04693e611950d414560eab8e007fe56b71551a767cb",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Production Atlas — Handoff Document
**Date:** 2026-06-24
**Branch:** `research-version` (HEAD: `58fa326`)
**Repository:** `thecrewblueprint-glitch/festival-atlas`
**Deploy target:** GitHub Pages (auto-deploys on push to `research-version`)

---

## What This Project Is

Production Atlas is a **static GitHub Pages research dashboard** for live-event production workers. No backend, no auth, no database. All data lives in JS files that set `window.RESOURCE_*` globals and are loaded as plain `<script>` tags. Pages read those globals and render everything client-side.

The site helps production workers identify 2026 festival work targets, filter by trade/location, review vendor routes, and plan travel.

**Live URL:** `https://thecrewblueprint-glitch.github.io/festival-atlas/`

---

## Repository Layout

```
festival-atlas/
├── index.html                     # Home
├── guide.html                     # How-to guide
├── calendar.html                  # Month grid view
├── schedule.html                  # Gantt timeline view
├── opportunities.html             # Card list view
├── branches.html                  # Trade branch research view
├── employers.html                 # Employer directory
├── iatse.html                     # IATSE local directory
├── matrix.html                    # Matrix view
├── analytics.html                 # Research Queue (stats dashboard)
├── sources.html                   # Source URLs (only place links appear in UI)
├── map.html                       # Leaflet map view
│
├── assets/
│   ├── atlas.css                  # All styles
│   ├── atlas-core-v2.js           # Main renderer IIFE — handles all page routing
│   ├── confidence-badges.js       # Badge rendering (source quality indicators)
│   ├── approx-date-labels.js      # Approximate date label rendering
│   ├── home-guide-page.js         # Home/Guide page logic
│   ├── guide-page.js              # Guide page content
│   └── research-queue-page.js     # Analytics page logic
│
├── data/
│   ├── iatse-us-local-directory.js
│   └── packages/
│       ├── opportunities-2026.js          # MASTER DATA FILE — 61 records (54 active)
│       ├── opportunity-coords.js          # Map lat/lng — loaded only on map.html
│       ├── opportunity-taxonomy.js        # Trade taxonomy definitions
│       ├── production-branches.js         # Production branch definitions
│       ├── us-employers.js                # Employer directory data
│       ├── research-queue-route-updates.js # Route research notes
│       ├── branch-research-manifest.js    # Manifest of all batch packages
│       ├── branch-research-runtime.js     # Branch research loader runtime
│       ├── guide-for-use-runtime.js       # Guide page data
│       └── branch-research-batch-001-* through branch-research-batch-006-*
│           (56 packages total, covering 10 trades across 6 batches)
│
├── tools/
│   ├── validate-data.js            # Validates opportunities-2026.js
│   ├── validate-branch-research-packages.js
│   └── validate-static-app.js
│
└── research/
    ├── data-quality-backlog.md     # Active backlog — this file
    ├── HANDOFF-2026-06-24.md       # This document
    └── RESEARCH_PROMPT_FILL_GAPS.md
```

---

## Git Workflow

- **Active development branch:** `research-version`
- **Frozen baseline:** `main` — DO NOT push to main without explicit user instruction
- **Deploy:** GitHub Actions auto-deploys `research-version` on every push
- Always run `npm run validate:all` before committing. It must pass 3/3 clean.
- Push command: `git push -u origin research-version`

---

## Master Data File: `data/packages/opportunities-2026.js`

### Structure

Records are created by an `opp()` helper that merges a defaults object with each record's fields:

```js
function opp(o) {
  return Object.assign({
    active2026Status: 'active_target',
    visibleInActive2026View: true,
    sourceQuality: 'user_report_or_prior_research_needs_source_attachment',
    // ... other defaults
  }, o);
}
window.RESOURCE_OPPORTUNITIES = [ opp({...}), opp({...}), ... ];
```

Fields defined inside the record object `o` override defaults. So to mark a record as verified, you add `sourceQuality:'source_attached_verified'` inside its `o` object.

### Key Fields

| Field | Type | Notes |
|---|---|---|
| `id` | string | Slug, e.g. `'coachella-2026'` |
| `name` | string | Display name |
| `startDate` / `endDate` | `'YYYY-MM-DD'` or `null` | null triggers approximate Gantt bar |
| `active2026SourceUrl` | string | Official URL confirming 2026 activity |
| `sourceQuality` | enum | See below |
| `longTermValueScore` | number | 0–100, used for priority ranking |
| `active2026Status` | enum | `'active_target'`, `'inactive_2026'`, etc. |
| `visibleInActive2026View` | bool | false = hidden from card/list views |
| `nextResearchActions` | array of strings | Open research tasks |

### sourceQuality Values

- `'user_report_or_prior_research_needs_source_attachment'` — default, no confirmed source
- `'source_attached_verified'` — web-confirmed active for 2026 with official URL

**As of 2026-06-24: All 54 active records carry `source_attached_verified`.**

### Record Counts

- **Total records:** 61
- **Active (visible):** 54
- **Inactive/hidden:** 7 (including `dreamville-2026` marked inactive after 2025)

---

## `data/packages/opportunity-coords.js`

Extracted from `atlas-core-v2.js` on 2026-06-24. Sets `window.RESOURCE_OPP_COORDS` — a plain object mapping record IDs to `[lat, lng]` arrays. Two multi-market records (`breakaway-2026`, `country-thunder-us-2026`) have `null` coords.

Loaded **only on `map.html`** before `atlas-core-v2.js`. In `atlas-core-v2.js`, `OPP_COORDS` is now defined as:
```js
var OPP_COORDS = window.RESOURCE_OPP_COORDS || {};
```
The `|| {}` fallback prevents errors on non-map pages.

---

## Validation

```bash
npm run validate:all
```

Runs 3 validators in sequence:
1. `validate:data` — checks `opportunities-2026.js` structure and field types
2. `validate:branch-research` — checks all 56 branch packages
3. `validate:static-app` — checks HTML, nav, banned constructs, manifest coverage

Must pass clean (0 errors) before every commit.

---

## Security / Privacy Rules — MUST REMAIN IN EFFECT

These rules are non-negotiable. Do not violate them:

- **Do NOT publish:** private contacts, phone numbers, personal emails, pay rates, hotel/lodging details, crew rumors, private field notes, NDA information, client-sensitive information, private referrals
- **Do NOT** re-add Firecrawl or any `FIRECRAWL_API_KEY`, create new network research automation, or publish raw Firecrawl artifact text
- **Do NOT** mark social/forum/job-board results as confirmed vendors
- **Do NOT** put source links inside popups or modals — source links belong on `sources.html` only
- **Do NOT** delete older research packages without explicit user approval
- **Do NOT** merge or reopen PR #1 without explicit instruction
- **Do NOT** convert the app into a backend/auth/payment system
- **Do NOT** push to `main` directly without explicit instruction
- Airtable base is private — raw submissions must NOT be published directly

---

## Banned Constructs (Validator Will Reject)

- `.chip` or `.chips` CSS classes
- `function chip(` in any JS file
- `<script async>` or `<script defer>` on data package `<script>` tags
- Do NOT name specific IATSE local numbers in route notes — use the pattern: "verify applicable IATSE/local jurisdiction for [city]"

---

## Current Open Tasks (Backlog)

### Active backlog items (from `research/data-quality-backlog.md`)

**Category 1 — Missing confirmed dates (2 records):**
- `breakaway-2026` (score 74) — multi-city run; per-market date records needed
- `country-thunder-us-2026` (score 62) — multi-market run; per-market date records needed

**Category 3 — Date bugs:**
- `crssd-fall-2026` — fall 2026 edition confirmed to exist on crssdfest.com but specific dates unknown; add a new `crssd-fall-2026` record when fall dates are publicly confirmed

**Category 5 — Producer names need verification (~24 records):**
Many producer fields contain "verify" because the relationship is uncertain. These should be confirmed via official festival websites or press releases before being used in outreach.

**Not yet started (future sessions):**
- Accommodation/travel fill — `accommodation` and `travelCompensation` fields are currently null on all 54 active records. Top 20 by score are the priority.
- Airtable App Feedback form — must be created manually on desktop Airtable (Table `tblJmDO9heY7KYv9m`, Base `appw5bN1XEGAD7Ga9`). Show: Subject, Feedback, Feedback Type, Page or Section. Hide: Review Status, Reviewer Notes.

---

## What Was Completed in This Session (2026-06-24)

1. **Top 20 source verification pass** — added `sourceQuality:'source_attached_verified'` to top 20 records by `longTermValueScore`. Fixed 7 non-official URLs (Wikipedia, news articles, business-insider guide) → official event sites.

2. **OPP_COORDS extraction** — moved 54-entry hardcoded coordinate map from `assets/atlas-core-v2.js` into `data/packages/opportunity-coords.js`. Reduces parse overhead on all non-map pages. Loaded only on `map.html`.

3. **Full source verification pass (all 54 records)** — added `sourceQuality:'source_attached_verified'` to all remaining 34 active records. Fixed 6 additional Wikipedia URLs → official sites (ultra-miami, governors-ball, kilby-block-party, sea-hear-now, newport-folk, newport-jazz).

All three changes committed and pushed to `research-version`.

---

## Script Load Order Reference

Most pages load:
```html
<script src="data/packages/production-branches.js"></script>
<script src="data/packages/opportunities-2026.js"></script>
<script src="data/packages/us-employers.js"></script>
<script src="data/iatse-us-local-directory.js"></script>
<script src="data/packages/opportunity-taxonomy.js"></script>
<script src="data/packages/research-queue-route-updates.js"></script>
<script src="assets/atlas-core-v2.js"></script>
<script src="assets/confidence-badges.js"></script>
<script src="assets/approx-date-labels.js"></script>
```

`map.html` additionally loads `opportunity-coords.js` **before** `atlas-core-v2.js`.

Branch research pages also load `branch-research-manifest.js` and `branch-research-runtime.js`.

---

## How to Add a New Opportunity Record

1. Add a new `opp({...})` entry to the array in `data/packages/opportunities-2026.js`
2. Add the record's `[lat, lng]` to `data/packages/opportunity-coords.js`
3. If it has confirmed dates and a web-verified source URL, include `sourceQuality:'source_attached_verified'`
4. Run `npm run validate:all` — must pass 3/3
5. Commit and push to `research-version`

---

## IATSE Wording Rule

When referencing union jurisdiction in route notes or research text, always use the pattern:

> "verify applicable IATSE/local jurisdiction for [city]"

Never name a specific IATSE local number (e.g., do not write "IATSE Local 16").

---

*End of handoff. Questions: read `research/data-quality-backlog.md` for the full active task list, and `npm run validate:all` to confirm current health.*
