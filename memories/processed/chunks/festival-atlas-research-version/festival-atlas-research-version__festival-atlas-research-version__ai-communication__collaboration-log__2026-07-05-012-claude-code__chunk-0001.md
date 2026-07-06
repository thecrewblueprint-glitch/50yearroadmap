---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__collaboration-log__2026-07-05-012-claude-code__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/collaboration-log/2026-07-05-012-claude-code-analytics-queue-and-map-coords.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 2287,
  "source_sha256": "32854f26ce21136df1b6ab0f0e5d6dd30142aba99d42aba68b0ad0ba8f310f42",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

Status: complete
Created: 2026-07-05
Review after: 2026-07-19
Assistant: Claude Code
Branch: research-version
Commit: this commit (+ preceding analytics-queue commits)
Access mode: Local clone / terminal + headless Chromium render checks

# Analytics research queue port + map coordinate fill

## 1. Analytics research queue (ported)

Reinstated the action-first research queue on analytics.html (owner-requested).
- Added assets/research-queue-page.js (self-contained: injects its own
  vtier/queue-list styles, so no atlas.css version bump).
- Included it on analytics.html and refreshed the header copy.
- Made it robust to research-version's async #app re-render (core re-renders
  after branch research loads) via a MutationObserver that re-injects the queue
  when core wipes it; render is idempotent so it cannot loop.
- It was on the validator's retired-runtime list; core renders no queue (the
  feature had been dropped, not folded in), so reinstating the standalone helper
  duplicates nothing. Removed assets/research-queue-page.js from
  tools/validate-static-app.js retiredRuntimeReferences.
- Verified headless: 1 queue section, 5 buckets, 28 items, no console errors.

## 2. Map coordinates (filled)

data/packages/opportunity-coords.js grew from 119 to 258 entries. Added
venue/city-level coordinates for 139 festivals that had none (the 95 imported
this session plus pre-existing festivals that were never geocoded). All 139 are
within valid US lat/long ranges; coordinates are venue-precise where the venue
is well known and city/town-centroid otherwise (appropriate for the map's
travel-clustering purpose).

Left without coordinates (cannot be pinned, intentional): breakaway-2026 and
country-thunder-us-2026 (multi-market tour overviews, already null),
great-beyond-2026 and desert-hearts-2026 (no city in the record),
blue-ridge-rock-2026 ("Virginia market", no specific venue). 249 of 254
opportunities now carry coordinates.

## Validation status

`npm run validate:all` passes 3/3. analytics.html and map.html render headless
with no console errors.

## Next action

Refine any city-centroid coordinates to venue-precise as time allows. Fill the 5
remaining records once their exact locations are confirmed (or leave the
multi-market overviews null by design).
