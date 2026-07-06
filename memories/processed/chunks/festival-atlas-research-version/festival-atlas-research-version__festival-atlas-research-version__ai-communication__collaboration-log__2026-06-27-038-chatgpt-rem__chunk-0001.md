---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__collaboration-log__2026-06-27-038-chatgpt-rem__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/collaboration-log/2026-06-27-038-chatgpt-remove-home-stats-bubbles.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 1365,
  "source_sha256": "ce80d55e828a091e06ea6126aeb8cf68d4f45da2c01857914ca0e31a245083e6",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Collaboration Log Entry — Remove Home Stats Bubbles

Status: incomplete
Created: 2026-06-27
Review after: 2026-07-11
Assistant: ChatGPT
Branch: research-version
Commit: 22e2a23290de973d37d58506183b97dc3cfa995e and 60683c9fec1289413789911128abd51e77ce6b81

## Files changed

```text
assets/home-upcoming.js
assets/atlas.css
```

## What changed

Aaron requested removal of the bubbles at the bottom of the home page that display site stats.

## Implementation

`assets/home-upcoming.js` no longer carries the existing `.stats` block forward when it replaces the home dashboard with the sorted upcoming festival grid.

`assets/atlas.css` also adds a defensive home-only rule:

```css
body[data-page="home"] .home-dash .stats {
  display: none !important;
}
```

This keeps stats available on other pages while hiding the home page stats bubbles.

## Scope preserved

```text
No route changes
No link changes
No data changes
No JavaScript overlay rewrites beyond the existing home-upcoming renderer
No effect on stats outside the home page
```

## Validation status

Validation not run; connector session cannot run local repo validation.

Required next command:

```bash
npm run validate:all
```

## Next action

Validate and hard refresh the home page. Confirm the stats bubbles are gone and the Upcoming Festivals section still renders and opens festival modals.
