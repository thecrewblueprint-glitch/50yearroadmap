---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__2026-06-23-claude-to-chatgpt-stage4-complete.__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/2026-06-23-claude-to-chatgpt-stage4-complete.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 5334,
  "source_sha256": "107452a7eb1784ef10dd5d8f42f81aebeec33c9f822eefb291d98a815b93b4e1",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Claude to ChatGPT Handoff — Stage 4 Complete

Generated: 2026-06-23

Author: Claude Code
Recipient: ChatGPT
Repository: `thecrewblueprint-glitch/festival-atlas`
Branch: `research-version`

---

## What Was Done This Session

Stage 4 of the product roadmap is complete. All five planning view improvements are implemented, validated, and pushed.

### Commit: Stage 4 (384f12c)

**4.1 — Calendar view improvements**

`renderCalendar()` in `assets/atlas-core-v2.js` now shows more context per event:

```
[value tier badge]
[event name — bold]
[city, state]
[NEW: dept chips — first 3 branch names, +N more if more]
[NEW: ● source — green dot, shown only if source URL is attached]
```

`calendar.html` filter bar: `employerTypeFilter` → `tierFilter` (consistent with opportunities.html and schedule.html). Calendar events now respond to the tier filter.

**4.2 — Map view improvements**

`renderMap()` now separates events into two labelled sections in the list below the map:

```
Mapped events (N)
  [opportunity cards for events with coordinates]

Multi-market / unmapped (N)
  [explanation: "These events span multiple cities or lack a single map coordinate."]
  [opportunity cards for events without coordinates]
```

Previously all events were mixed together in one unsectioned grid. The `<div id="mapList">` container no longer has the `grid` class hardcoded — sections build their own inner `<div class="grid">` elements. Map pin metadata line also updated: "N multi-market (no single location — see list)" → "N multi-market / unmapped".

**4.3 — Schedule view improvements**

Stats row now shows 6 items in a 2×3 grid (`repeat(3,1fr)` unchanged):

```
[events planned]  [approx event days]  [date overlaps]
[avg value score] [months covered]     [regions covered]
```

The three new stats compute from `scheduledOpps` array:
- avg value score: `Math.round(sum of scores / count)` (0 if empty)
- months covered: unique `o.month` values from scheduled events
- regions covered: unique `o.region` values from scheduled events

**4.4 — Analytics view improvements**

Dataset breakdown section now has 6 chart cards (previously 4):

```
By region          By value tier
By month           By confidence    ← NEW
Branch records     Employers by type
```

"By month" uses `MONTHS[(o.month||1)-1]` for readable labels.
"By confidence" uses `confidenceLabel(o.confidence||o.sourceType)` — the same controlled vocabulary used on cards and modals.

**4.5 — Sources view improvements**

`renderSources()` now:
- Applies text search (`filter.q`) against event name + branch name + source label
- Applies branch filter (`filter.branch`) to show only sources attached to a specific department
- Shows a 3-stat header: sources shown / opportunity sources / branch sources
- Added a Type column to the table: "Opportunity" or "Branch"
- Shows a no-match row if filters produce zero results

Table now has 5 columns: Item | Type | Section | Source label | Link

Sources page filter bar already had `#q` and `#branchFilter` — these now work.

---

## Current State

```text
Branch:     research-version
Validation: npm run validate:all — PASSES CLEAN (56 packages)
Commit:     384f12c
Pages:      12 HTML pages
Packages:   56 branch research packages, all manifest-linked
```

Files changed in Stage 4:
```text
assets/atlas-core-v2.js  — renderCalendar, renderMap, renderSchedule,
                           renderAnalytics, renderSources
calendar.html             — employerTypeFilter → tierFilter
```

---

## Known Gaps Still Open

### Critical data bug (fix before Gantt use):
- `crssd-2026` has `endDate: '2026-09-27'` with `startDate: '2026-03-14'` — renders as a 6-month Gantt bar. Fix: set endDate to the March weekend end date or null it and add a nextResearchAction note about the fall edition.

### Ongoing data fill work:
- 17 active opportunities have null startDate — Gantt shows approximate bars; Sources page shows no confirmed dates
- 45+ active opportunities have no public source URL — display as "Unverified"
- Most producer names contain "verify" — unknown operator status
- Full gap list: `research/data-quality-backlog.md`
- Research tool: `research/RESEARCH_PROMPT_FILL_GAPS.md`

---

## What Is Not Touched

- PR #1 (`claude/research-version-edits-z0gqw6` → `main`) — open, untouched, do not merge without explicit instruction
- No Firecrawl references re-added
- No source links inside popups (Sources page link only, no raw URLs injected)
- No private contact/pay/lodging data published

---

## Suggested Next Steps (Stage 5)

Per the product intent, possible priorities:

**Data cleanup (highest leverage, can run any time):**
```
- Fix crssd-2026 date bug
- Fill source URLs for high-value records: summerfest, lollapalooza, breakaway, country-thunder
- Confirm dates for 17 null-date records
- Use research/data-quality-backlog.md as the task queue
```

**Stage 5 ideas (new features):**
```
- 5.1  Export / print view — portable PDF-style summary of schedule and top targets
- 5.2  Branch research fill — add batch 007+ with more opportunities per department
- 5.3  Sources page enhancements — sort by opportunity, show last-verified date
- 5.4  Map enhancements — department color legend, click-to-filter by map region
- 5.5  Notification or reminder text for upcoming high-value events
```

---

— Claude Code
