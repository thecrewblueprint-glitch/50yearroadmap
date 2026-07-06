---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__collaboration-log__2026-06-27-045-chatgpt-map__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/collaboration-log/2026-06-27-045-chatgpt-map-static-fallback.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 1880,
  "source_sha256": "2a3c038c97432126f5a2abb16d6b57981133ea72ce18a08cc7f633e15741f1da",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Collaboration Log Entry — Map Static Fallback

Status: incomplete
Created: 2026-06-27
Review after: 2026-07-11
Assistant: ChatGPT
Branch: research-version
Commit: 9458987

## Files changed

```text
assets/map-static-fallback.js
map.html
```

## What changed

Aaron reported that the map page does not work.

The existing map page depends on the external Leaflet library. If Leaflet fails to load, is blocked, or does not initialize correctly on mobile, the page can fail or show a library-unavailable message.

This update adds a local static fallback map renderer.

## Behavior

If Leaflet works:

```text
The existing Leaflet map remains available.
```

If Leaflet does not work:

```text
The page renders a built-in clickable static map panel.
```

The fallback uses existing public data:

```text
window.scopedOpportunities
window.RESOURCE_OPP_COORDS
window.branches
openOpportunity(id)
```

## Fallback features

```text
Clickable map markers
Approximate regional placement from stored coordinates
Mapped festival cards
Multi-market / unmapped festival cards
Filter support for search, department, state, and month
Festival modals still open from markers/cards
No backend
No new external dependency
```

## Public safety

The fallback explicitly labels marker placement as approximate and only uses existing public opportunity data. It does not expose private contacts, pay rates, lodging, or private notes.

## Cache/version update

`map.html` now loads:

```html
<script src="assets/map-static-fallback.js?v=mapfix1"></script>
```

## Validation status

Validation not run; connector session cannot run local repo validation.

Required next command:

```bash
npm run validate:all
```

## Next action

Validate, wait for GitHub Pages deploy, hard refresh the map page, and test on mobile. If Leaflet still fails, the static fallback should render instead of a broken map.
