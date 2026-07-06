---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__collaboration-log__2026-06-27-041-chatgpt-cal__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/collaboration-log/2026-06-27-041-chatgpt-calendar-two-color-date-layers.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 2160,
  "source_sha256": "4994748c59b2f1b9245713aa6993649dc7e42e0c69cc20283c557f67a833e317",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Collaboration Log Entry — Calendar Two-Color Date Layers

Status: incomplete
Created: 2026-06-27
Review after: 2026-07-11
Assistant: ChatGPT
Branch: research-version
Commit: d61b26b9b7f2ba927bac01a0371f0724de433fba and 14863e0bce7711e77acd1078cef751100c68f83c

## Files changed

```text
assets/calendar-interactive.js
calendar.html
```

## What changed

Aaron requested a clear two-color scheme for approximate working dates versus actual festival show days so the calendar visualization is useful without implying approximate work windows are real confirmed dates.

## Calendar visualization update

The calendar now renders two layers per festival:

```text
Approximate work window = muted/dashed planning bar
Festival show days = brighter solid show-date bar
```

This applies in both:

```text
Month view
Week view
```

## Legend and disclaimer

The calendar now includes a visible legend:

```text
Approx. work window
Festival show days
```

The calendar also includes a stronger disclaimer:

```text
Date disclaimer: festival dates are based on public sources. Approximate work windows are planning estimates only and are subject to change; verify current dates with official sources before making travel, outreach, or availability decisions.
```

The status strip also states:

```text
Dashed muted bars = approximate work windows · solid bright bars = festival show dates
```

## Day modal update

Clicking a day now separates:

```text
Festival show days
Approximate work-window estimates
```

## Public safety / accuracy

Approximate work windows remain explicitly labeled as estimates. The app does not claim exact load-in, strike, or crew-call dates.

## Cache/version update

`calendar.html` now loads:

```html
<script src="assets/calendar-interactive.js?v=cal3"></script>
```

## Validation status

Validation not run; connector session cannot run local repo validation.

Required next command:

```bash
npm run validate:all
```

## Next action

Validate, wait for GitHub Pages deploy, and hard refresh the calendar page. Inspect month and week views for clear visual separation between approximate work windows and actual festival show days.
