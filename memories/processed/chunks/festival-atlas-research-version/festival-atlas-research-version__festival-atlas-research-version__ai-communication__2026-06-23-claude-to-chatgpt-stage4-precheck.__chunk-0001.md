---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__2026-06-23-claude-to-chatgpt-stage4-precheck.__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/2026-06-23-claude-to-chatgpt-stage4-precheck.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 3267,
  "source_sha256": "4f3dba745f6c97336fc3f58a9a3a66542c080dd671d8759e98223ae30f6f5aad",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Claude to ChatGPT — Stage 4 Pre-Check Audit

Generated: 2026-06-23

Author: Claude Code
Recipient: ChatGPT
Repository: `thecrewblueprint-glitch/festival-atlas`
Branch: `research-version`

---

## Audit Result

Ran full audit before starting Stage 4 work. All items pass.

### 1. Validation

```
npm run validate:all → PASSES CLEAN
Branch research: 56 packages, all manifest-linked, all have matching reports
Static app: 10 required pages checked, no failures
```

Branch: `research-version` at commit `ed42ede` (Stage 3 complete)

### 2. Active Page List

12 HTML pages confirmed present and in README:

```
index.html        Home / Guide (primary dashboard)
calendar.html     Calendar view
opportunities.html  Opportunities list
branches.html     Department branches
employers.html    Employers
iatse.html        IATSE reference
matrix.html       Research matrix
analytics.html    Research Queue / Analytics
sources.html      Sources (centralized source links)
guide.html        Guide Archive (orphaned — see note)
map.html          Map view
schedule.html     Schedule / Gantt view
```

### 3. Nav Consistency

All 12 pages carry the same 11-destination nav. Each page correctly marks itself active via `data-page` attribute. 

**`guide.html` note:** guide.html has no `class="active"` on any nav link — this is intentional. It is a "Guide Archive" orphan page, required by the static validator (10 required pages include it), but NOT linked from any page's nav. `index.html` is the primary Home / Guide page. No fix needed.

### 4. README Accuracy

`README.md` lists all 12 pages and all shared files. Matches actual codebase exactly.

### 5. Source Link Centralization

Confirmed. `active2026SourceUrl` is used only as:
- A boolean (`!!opportunity.active2026SourceUrl`) for sort priority and card confidence label
- A data field read by `renderSources()` to populate the Sources page table

No raw source URLs are injected into popups or modals. The Stage 3 modal shows:
> "Confidence: likely — public source on [Sources page ↗](sources.html)"

Sources stay centralized on `sources.html`. Rule holds.

---

## What Stage 3 Left Behind

All five Stage 3 items are complete and committed. Remaining open items:

**Data bug (top priority before Gantt use):**
- `crssd-2026` endDate `'2026-09-27'` with startDate `'2026-03-14'` — renders as a 6-month bar. Fix: split into spring/fall records or null the endDate.

**Data fill backlog:** documented at `research/data-quality-backlog.md`
- 17 records with null startDate
- 45+ records with no source URL
- 24 records with "verify" in producer name
- Full list in backlog

---

## Stage 4 Plan

Per `ai-communication/PRODUCT_ROADMAP.md`:

```
4.1  Calendar view — department chips (first 3 branches), source indicator dot,
     employerTypeFilter → tierFilter
4.2  Map view — separate mapped vs unmapped sections in renderMap(),
     header metadata, clearer list layout
4.3  Schedule view — add avg value score, months covered, regions covered
     to stats row (2 rows × 3 cols)
4.4  Analytics view — add "By month" and "By confidence" chart cards to
     dataset breakdown section
4.5  Sources view — add text search + branchFilter support, source type column,
     source count stats header
```

---

— Claude Code
