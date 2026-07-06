---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__research__data-quality-backlog.md__chunk-0002",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/research/data-quality-backlog.md",
  "chunk_index": 2,
  "chunk_count_for_source": 2,
  "char_start": 11332,
  "char_end": 17414,
  "source_sha256": "7de00fd34522f5e1ef48536c5505b7b6accaafac8742e7b119bde7f8631dd4f3",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

esota-2026: Jun 26–27, Allianz Field Festival Grounds, St. Paul MN
- breakaway-michigan-2026: Aug 14–15, Belknap Park, Grand Rapids MI
- breakaway-mass-2026: Aug 21–22, Palladium Outdoors, Worcester MA
- breakaway-philadelphia-2026: Sep 11–12, Subaru Park Festival Grounds, Chester PA
- breakaway-carolina-2026: Sep 25–26, zMAX Dragway, Charlotte NC
- breakaway-utah-2026: Oct 2–3, America First Field, Sandy UT
- breakaway-norcal-2026: Oct 16–17, Cal Expo Center, Sacramento CA
- breakaway-houston-2026: Nov 13–14, venue TBD (confirm when announced)

Country Thunder US 2026 — 3 per-market records:
- country-thunder-arizona-2026: Apr 9–12, Country Thunder Arizona Grounds, Florence AZ
- country-thunder-florida-2026: May 8–10, Coachman Park, Clearwater FL (new venue for 2026)
- country-thunder-wisconsin-2026: Jul 16–19, Shadow Hill Ranch, Twin Lakes WI

Remaining open: `breakaway-houston-2026` venue is TBD — update when Breakaway announces it.

---

## Category 2 — Missing Public Source URL

**All active records now have source URLs and `sourceQuality:'source_attached_verified'` as of 2026-06-24.** Category 2 is fully resolved.

Remaining action: breakaway-2026 and country-thunder-us-2026 have sources attached at the tour level; per-market records still needed when individual market dates are confirmed.

---

## Category 3 — Unclear or Wrong Dates (Data Bugs)

These records have technical date issues that produce incorrect Gantt bars or filter behavior.

```
crssd-2026   FIXED 2026-06-23: endDate corrected to '2026-03-15'. Fall edition needs a
  separate crssd-fall-2026 record when official fall dates are confirmed.

breakaway-2026   startDate: '2026-04-10', endDate: '2026-11-14'
  This IS a 14-city run spanning April–November. The wide date range is correct
  but the single record should note it is a multi-city tour, not a single event.
  Already labeled "Multiple cities / US multi-market" — acceptable, leave as is,
  but add a note that each city leg needs its own research record.

country-thunder-us-2026   startDate: '2026-04-09', endDate: '2026-07-19'
  Same: multi-market season run, not one event. Already labeled as multi-market.
  Acceptable with current labeling. When dates are confirmed per market, split records.
```

---

## Category 4 — Unclear Venue or Region

These records have placeholder or unverified venue/region data.

```
breakaway-2026           region: 'United States multi-market' — acceptable; each leg needs city
country-thunder-us-2026  region: 'United States multi-market' — same; per-market split needed
```

Note: shaky-knees (Piedmont Park) and sick-new-world (Las Vegas Festival Grounds) resolved 2026-06-23.

---

## Category 5 — Producer Name Needs Verification

**Resolved 2026-06-24 (Category 5 verification pass):**

All 23 active records with "verify" language in producer names have been updated. Sources: official festival websites, Pollstar news, and web search verification.

Key corrections:
- rocklahoma: was "AEG / partners" → Danny Wimmer Presents (acquired 2024)
- railbird: was "Live Nation / partners" → C3 Presents / Live Nation (Allison Barker, presented by C3)
- sick-new-world: was "Live Nation / partners" → C3 Presents / Live Nation (Velvet Hammer Music co-creator)
- okechobee: was "verify current status" → Soundslinger (OMF LLC) — Madison House no longer current
- hulaween: was "Suwannee / partners" → Spirit of the Suwannee / Michael Berg (repurchased from Etix)
- electric-forest: was "Insomniac / Madison House, verify current" → Insomniac / Madison House Presents ✓
- breakaway: was "Breakaway / multi-city producer, verify markets" → Breakaway Presents (independent)
- high-sierra: was "High Sierra / partners" → Dave Margulies / High Sierra Music Festival (also relocated to Grass Valley)

Remaining 31 active records retain `needs_source_link` status but have clean producer names (no "verify" language). These are major well-known producers (Goldenvoice/AEG, C3 Presents, DWP, Insomniac, etc.) — status can be updated in a future pass with formal source citations.

```
dreamville-2026   (inactive — skip)
```

---

## Category 6 — Low-Confidence Records That May Be Overstated

These records are in the active view but have a value score or presentation that may signal more certainty than the data supports. Review before using as outreach justification.

```
breakaway-2026       Score 74 — multi-city, source attached at tour level, no per-market dates.
                     High score reflects potential, not confirmed work. Treat as speculative
                     until per-market dates and venues are confirmed.

country-thunder-us-2026  Score 62 — same situation. Source attached, no per-market split.
```

Note: crssd-2026 (date bug) and summerfest-2026 (missing source) resolved as of 2026-06-23.

---

## Category 7 — Route Lead Wording (Branch Records)

The branch research data uses raw status values like `likely_venue_infrastructure_route` and `unconfirmed_route_lead`. Stage 3 code now maps these to standardized labels (`Likely route`, `Route lead`, `unverified`). However, any branch record with confidence `unverified` or `possible` that is presented as certain in outreach materials needs to be re-reviewed.

Action: When reviewing branch records in the app, any card showing "Route lead only — not a confirmed vendor" warning should be treated as a research direction, not a confirmed employer. Do not claim the company is working the event without a direct public source.

---

## How to Use This Backlog

1. Open the app Research Queue (analytics.html) to see live counts grouped by category.
2. Use `research/RESEARCH_PROMPT_FILL_GAPS.md` to generate a targeted research pass for a specific event.
3. After filling a gap (source URL, confirmed date, confirmed venue), update `data/packages/opportunities-2026.js` with the new field and re-run `npm run validate:all`.
4. Remove the item from this backlog once the gap is filled and verified.

Priority order: fix data bugs (Category 3) first, then attach sources (Category 2), then confirm dates (Category 1).
