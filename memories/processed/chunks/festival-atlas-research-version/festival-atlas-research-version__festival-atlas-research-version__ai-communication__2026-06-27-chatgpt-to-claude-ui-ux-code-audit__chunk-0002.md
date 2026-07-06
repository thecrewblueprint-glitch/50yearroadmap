---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__2026-06-27-chatgpt-to-claude-ui-ux-code-audit__chunk-0002",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/2026-06-27-chatgpt-to-claude-ui-ux-code-audit-handoff.md",
  "chunk_index": 2,
  "chunk_count_for_source": 2,
  "char_start": 11391,
  "char_end": 16170,
  "source_sha256": "797f806c5af46f7f63f894fa531c6672f27fffd4dc101547952d2264e5a5dc6b",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

ies remain on map page.
```

### 7. Public copy terminology cleanup

Current desired public terminology:

```text
Departments, not branches, when user-facing.
Employer routes, not guaranteed employers.
Confirmed event-specific routes only where publicly tied.
General employer routes stay on Employers page.
Unknown publicly. Human verification needed. for uncertain info when needed.
```

Audit across:

```text
assets/atlas-core-v2.js
assets/home-upcoming.js
assets/home-cleanup.js
assets/festival-modal-public-safe.js
assets/calendar-interactive.js
assets/map-page-static.js
assets/site-footer.js
all *.html public pages
```

Look for public-facing remnants:

```text
Branch / branches where Department / departments is intended
Research queue
Future live feed
Validation
Roadmap
Internal
Supplemental not part of primary navigation
Use this for job mapping
Notes to Aaron/Claude/ChatGPT
```

Some internal code comments are okay. Visible public page text should be polished.

### 8. White pages and legal pages

Added public documentation and legal baseline pages.

Audit:

```text
Confirm all pages use same visual shell.
Confirm all pages include global footer.
Confirm legal pages do not overclaim attorney-reviewed compliance.
Confirm privacy/cookie statements align with current static app behavior.
Confirm Contact / Data Requests page does not ask users to submit private/sensitive information publicly.
```

Important:

These legal pages are baseline public pages, not attorney-reviewed legal advice. Do not claim complete legal compliance unless reviewed by counsel.

## Known technical concerns from recent work

Several changes are layered as JS enhancement scripts rather than clean core integration:

```text
assets/home-upcoming.js
assets/home-cleanup.js
assets/festival-modal-public-safe.js
assets/map-page-static.js
assets/opportunities-promoter-filter.js
assets/site-footer.js
```

This was done for rapid public-page iteration. It may now be time to audit whether some behavior should be consolidated into:

```text
assets/atlas-core-v2.js
assets/atlas.css
individual page HTML
```

Do not perform a large rewrite unless necessary. Prefer small verified fixes.

## Files to inspect closely

Core app/UI:

```text
assets/atlas-core-v2.js
assets/atlas.css
```

Recent UI scripts:

```text
assets/calendar-interactive.js
assets/map-page-static.js
assets/home-upcoming.js
assets/home-cleanup.js
assets/home-guide-page.js
assets/festival-modal-public-safe.js
assets/opportunities-promoter-filter.js
assets/site-footer.js
```

Public pages:

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
about.html
data-methodology.html
employer-route-methodology.html
date-work-window-disclaimer.html
privacy-policy.html
terms-and-conditions.html
limitation-of-liability.html
cookie-notice.html
accessibility.html
affiliate-disclosure.html
contact-data-requests.html
```

Data files relevant to UI filters/map/calendar:

```text
data/packages/opportunities-2026.js
data/packages/opportunity-coords.js
data/packages/production-branches.js
data/packages/us-employers.js
data/iatse-us-local-directory.js
data/packages/research-queue-route-updates.js
data/packages/opportunity-taxonomy.js
```

## Required validation

After any code/data changes, run:

```bash
npm run validate:all
```

If narrowing the validation during diagnosis:

```bash
npm run validate:static-app
npm run validate:branch-research
```

Do not claim completion unless validation was run, or clearly document why it could not be run.

## Requested Claude output

Please produce an audit report in `ai-communication/` with:

```text
1. Files inspected
2. Issues found
3. User-visible bugs confirmed
4. Public-safety/copy issues found
5. UI/UX regressions found
6. Accessibility/mobile issues found
7. Recommended minimal fixes
8. Any fixes applied
9. Validation command/result
10. Remaining risks
```

If fixes are applied, create a handoff log in:

```text
ai-communication/collaboration-log/YYYY-MM-DD-claude-ui-ux-audit-update.md
```

## Priority order for Claude

1. Fix/cleanly integrate the Opportunities promoter/state/date filters.
2. Confirm public navigation and footer consistency.
3. Confirm modal public-safety behavior.
4. Confirm calendar and map UI work on mobile.
5. Remove visible internal/draft language from public pages.
6. Validate all static app checks.

## Current user-facing problem to reproduce first

Open:

```text
opportunities.html
```

Expected visible filter bar:

```text
All promoters | All states | All dates | Reset
```

Current reported by Aaron:

```text
State dropdown is missing.
```

Start by reproducing and fixing that issue before broader cleanup.
