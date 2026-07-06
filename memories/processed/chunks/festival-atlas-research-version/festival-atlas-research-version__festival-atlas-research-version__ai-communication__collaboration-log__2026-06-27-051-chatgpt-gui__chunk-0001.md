---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__collaboration-log__2026-06-27-051-chatgpt-gui__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/collaboration-log/2026-06-27-051-chatgpt-guide-current-status-update.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 2160,
  "source_sha256": "5eeb4b431308cf0f85aa8189a42ac0cbe713c39316eec1b45ca66841862c1287",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Collaboration Log Entry — Guide Page Current Status Update

Status: incomplete
Created: 2026-06-27
Review after: 2026-07-11
Assistant: ChatGPT
Branch: research-version
Commit: 3450f90

## Files updated

```text
guide.html
assets/guide-page.js
```

## What changed

Aaron requested that the Guide page be reviewed and updated so it reflects the current status of the public web app.

The Guide page now describes the current public app structure and workflow:

```text
Opportunities
Calendar
Map
Departments
Employers
Sources
Footer white pages
Footer legal/information pages
Schedule and IATSE pages as additional available pages
```

## Public workflow now described

The guide now explains:

```text
Start with Opportunities
Use promoter, state, and date filters
Use Calendar month/week views
Read blue approximate work-window bars vs gold festival show-date bars
Use the static U.S. map for regional planning
Use Departments for trade-first research
Use Employers for general public company routes
Use Sources for centralized source links
Use public white pages and legal pages in the footer
```

## Public-safety language updated

The guide now clarifies:

```text
General employer routes are not confirmed event-specific contracts
Confirmed event-specific routes require a public tie to that event
Approximate work windows are planning estimates, not exact call dates
Private contacts, phone numbers, personal emails, pay rates, lodging details, referrals, rumors, and internal notes do not belong in the public UI
Raw source links belong on Sources, not popups
```

## Navigation cleanup

The guide shell no longer includes Guide as a top-nav item. Top nav is aligned with the current primary app navigation:

```text
Home
Opportunities
Calendar
Map
Departments
Employers
Sources
```

## Cache update

```text
assets/guide-page.js?v=guide3
```

## Validation status

Validation not run; connector session cannot run local repo validation.

Required next command:

```bash
npm run validate:all
```

## Next action

Validate, wait for GitHub Pages deploy, hard refresh guide.html, and confirm the guide reads as public documentation for the current app.
