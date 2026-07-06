---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__collaboration-log__2026-06-27-048-chatgpt-pub__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/collaboration-log/2026-06-27-048-chatgpt-public-white-pages-and-global-footer.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 1881,
  "source_sha256": "df8cb45fe77b2e7c21718fff4e50160fef0b63489685265da78597ea6f602bd5",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Collaboration Log Entry — Public White Pages and Global Footer

Status: incomplete
Created: 2026-06-27
Review after: 2026-07-11
Assistant: ChatGPT
Branch: research-version
Commit: 3aa4a29

## Files added

```text
assets/site-footer.js
about.html
data-methodology.html
employer-route-methodology.html
date-work-window-disclaimer.html
```

## Files updated

```text
index.html
opportunities.html
calendar.html
map.html
branches.html
employers.html
sources.html
guide.html
schedule.html
iatse.html
matrix.html
analytics.html
```

## What changed

Aaron clarified that public-facing explanatory white pages should exist, but internal notes should not appear in public page copy.

This update adds a reusable public footer and a public documentation layer.

## Global footer

Added:

```text
assets/site-footer.js
```

The footer renders:

```text
Production Atlas public description
Primary work-map links
White-page links
```

White-page footer links:

```text
About
How the Data Works
Employer Route Methodology
Date & Work Window Disclaimer
```

## Public white pages

Added:

```text
about.html
data-methodology.html
employer-route-methodology.html
date-work-window-disclaimer.html
```

These pages are written as public documentation, not internal notes.

## Public copy cleanup

Home page internal/helper notes were removed earlier, and this pass also cleaned supplemental page copy on:

```text
matrix.html
analytics.html
```

The public copy rule is now:

```text
Internal collaboration notes belong in ai-communication/.
Visible app pages must read like finished public pages.
```

## Validation status

Validation not run; connector session cannot run local repo validation.

Required next command:

```bash
npm run validate:all
```

## Next action

Validate, wait for Pages deploy, then hard refresh several pages and confirm the footer appears with the white-page links.
