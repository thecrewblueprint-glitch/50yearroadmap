---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__collaboration-log__2026-06-27-043-chatgpt-cal__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/collaboration-log/2026-06-27-043-chatgpt-calendar-show-label-centering.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 1792,
  "source_sha256": "b26bcdc66ba4c8a7fd073d2cb33d3c984ed5064298cddfb40022ea86e6525303",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Collaboration Log Entry — Calendar Show Label Centering

Status: incomplete
Created: 2026-06-27
Review after: 2026-07-11
Assistant: ChatGPT
Branch: research-version
Commit: e80dc7ef1c5e01477ff7c8765998276550b497ed and 90617001ac7370a23ac4123161d585b9460e3101

## Files changed

```text
assets/calendar-interactive.js
calendar.html
```

## What changed

Aaron requested that festival names be centered onto the actual festival day bars rather than appearing across the whole approximate work-window bar.

## Implementation

The combined calendar bar still has:

```text
Outer muted/dashed bar = approximate work window
Inner bright solid segment = festival show days
```

The festival name now renders inside the inner bright show-date segment:

```html
<i class="cal-show-overlay">
  <span class="cal-show-name">Festival name</span>
</i>
```

The outer approximate work-window bar no longer uses the festival name as its main visible label. It keeps only a small `Approx.` label so users understand the outer bar is approximate.

## Why

This visually anchors the festival title to the actual public show dates instead of implying the whole approximate work window is the festival itself.

## Cache/version update

`calendar.html` now loads:

```html
<script src="assets/calendar-interactive.js?v=cal6"></script>
```

## Public safety / accuracy

Approximate work windows remain visually distinct from actual show days and remain labeled as estimates.

## Validation status

Validation not run; connector session cannot run local repo validation.

Required next command:

```bash
npm run validate:all
```

## Next action

Validate, wait for Pages deploy, hard refresh the calendar page, and check whether festival names are centered on the bright show-day segments in month and week views.
