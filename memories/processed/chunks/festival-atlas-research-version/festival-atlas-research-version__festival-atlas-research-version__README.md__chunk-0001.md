---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__README.md__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/README.md",
  "chunk_index": 1,
  "chunk_count_for_source": 2,
  "char_start": 0,
  "char_end": 11948,
  "source_sha256": "b2ee17bf7416b823056642bd7c24b663803f2fdf97420c49e5165c7874010d51",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Production Atlas

A project of [Deadhang Labor LLC](https://deadhanglaborllc.com).

Generated: 2026-06-22  
Updated: 2026-07-05

Production Atlas is a static GitHub Pages work-mapping app for live-event production contractors. The public app is focused on factual, publicly known or publicly obtainable information that helps workers find festival opportunities, understand public dates and approximate production windows, identify public producer/promoter and employer-route leads, review source references, and plan scheduling.

The repository can contain deeper research and supplemental audit data, but the public-facing pages should stay concise, worker-useful, and public-safe.

README current when significant app behavior changes. Do not leave source-of-truth drift for another assistant to discover.

## Live GitHub Pages site

- **Custom domain:** https://atlas.thecrewblueprint.com/
- **GitHub Pages URL:** https://thecrewblueprint-glitch.github.io/festival-atlas/

Maintenance rule: keep this README current when significant app behavior, public navigation, public filter scope, runtime loading, active shared files, validation contract, data state, page roles, collaboration-log convention, public-safety policy, or source-link policy changes.

## Repository / branch

```text
Repository: thecrewblueprint-glitch/festival-atlas
Active research branch: research-version
Default branch: main
Pages source: GitHub Actions
Live preview source branch: research-version
Public site: https://atlas.thecrewblueprint.com/
```

`research-version` is the intended live working branch. `main` must not be edited, patched, merged into, or used as a live hotfix unless Aaron explicitly says to touch `main`.

## Current state snapshot

Current repo-visible app state as of 2026-07-05:

```text
Public app type: static GitHub Pages app
Public navigation: Home, Opportunities, Calendar, Map, Employers, IATSE, Contribute
Schedule: functional by direct URL only; off header navigation pending rebuild
Active opportunity package: data/packages/opportunities-2026.js
Current active opportunity count: 254 opportunity records
Festival registry/master list: 258 records in data/packages/festival-research-master-list.js
Map coordinates: 249 of 254 opportunity records currently mappable
Analytics: supplemental retained audit page with action-first research queue
Backend/auth/database/payment/scraping: none
```

The app functions are currently treated as correct. Documentation should describe current behavior instead of reintroducing removed UI or patch-layer assumptions.

## Source-of-truth rule

When repo-visible documents disagree, resolve in this order:

```text
1. Actual files on research-version
2. Aaron's latest explicit instruction
3. ai-communication/DOCUMENT_DRIFT_CONTROL_PROTOCOL.md
4. Validation scripts
5. README.md
6. ROADMAP.md
7. ai-communication/AI_COLLABORATION_PROTOCOL.md
8. ai-communication/PROJECT_CHAT_GROUP_INSTRUCTIONS.md
9. ai-communication/PRODUCT_ROADMAP.md
10. Latest topic-specific decision record
11. Latest collaboration log for the affected file/topic
12. Older handoffs and chat memory
```

## Collaboration log rule

Routine per-commit or per-small-change notes belong in:

```text
ai-communication/collaboration-log/
```

Use one new file per commit or compact commit group. Do not maintain one giant append-only active-session ledger for routine work.

Recommended filename pattern:

```text
YYYY-MM-DD-###-assistant-short-topic.md
```

Each log entry must include lifecycle metadata:

```text
Status: complete | incomplete | blocked | superseded
Created: YYYY-MM-DD
Review after: YYYY-MM-DD
Assistant: ChatGPT | Claude | Claude Code | other
Branch: research-version
Commit: <sha>            (or "Commits: <sha>, <sha>" or "Commit range: <sha>..<sha>")
```

For current work, logs should also include access mode, files changed, files deleted, documents examined for drift, documents updated, documents intentionally not updated and why, validation status, human-review status where applicable, known risks, and next action.

Two-week cleanup rule:

```text
complete or superseded logs older than 14 days may be deleted if no longer useful.
incomplete or blocked logs older than 14 days should be moved to ai-communication/collaboration-log/incomplete/.
incomplete or blocked logs must remain auditable and must not be deleted during routine cleanup.
```

Use `ai-communication/` root for major handoffs, decision records, current-state summaries, and cross-assistant instructions. Use `ai-communication/collaboration-log/` for compact per-commit/per-change notes.

## Public page strategy

The app should help answer:

```text
Where is the work?
When is it happening?
Who publicly produces, promotes, operates, or routes the work?
What is the approximate build/load-in and strike/load-out window?
Which public companies, employers, vendors, or labor routes are relevant?
Where can a worker apply, contact, or research those companies?
How does this affect calendar, travel, and scheduling decisions?
```

### Primary work-flow pages

```text
index.html        Home: quick explanation, dashboard, and clear Guide link.
guide.html        Full Guide for Use and public-safe workflow.
opportunities.html
                  Festival/event profiles with page-specific filters for text search,
                  state, department, producer/promoter, and date/month.
calendar.html     Month-by-month planning view for event timing and availability.
map.html          Location view for routing, travel clustering, and nearby opportunities.
                  Current Map filters are state and date/month; do not re-add the
                  removed department filter unless Aaron explicitly reopens it.
employers.html    Public company, employer, vendor, producer, venue, and apply/contact routes.
iatse.html        How to join IATSE: union-join guidance, official IATSE resources,
                  searchable local directory, pagination, and per-local join steps.
contribute.html   Public-safe human-submission route; all submissions require review.
feedback.html     Public app feedback route.
```

Schedule state:

```text
schedule.html     Local browser-only planning view. Temporarily off public navigation
                  (unlinked, noindex, robots-disallowed); still functional by direct URL,
                  saved schedules preserved, pending a mobile/usability rebuild.
```

### Header / footer navigation rule

Current header nav:

```text
Home
Opportunities
Calendar
Map
Employers
IATSE
Contribute
```

Schedule is temporarily off public navigation pending a rebuild; the page still works by direct URL. Guide and Sources are footer/reference links, not header nav links. The Guide also appears as a home-page callout between the nav bar and the first home card. Sources remains a central audit/source page and must stay reachable from the footer/reference flow and contextual source-page links.

### Source / audit page

```text
sources.html      Central public source list for auditability.
```

Source links still belong on `sources.html`, not inside opportunity popups, branch popups, map popups, or schedule cards.

### White pages

```text
about.html
                    What Production Atlas is and is not.
data-methodology.html
                    How public event, employer, source, map, date, and planning data works.
employer-route-methodology.html
                    Difference between general employer routes and confirmed event-specific routes.
date-work-window-disclaimer.html
                    Public event dates vs. approximate work-window planning estimates.
```

### Legal / policy pages

```text
privacy-policy.html
terms-and-conditions.html
limitation-of-liability.html
cookie-notice.html
accessibility.html
affiliate-disclosure.html
contact-data-requests.html
```

### Supplemental retained pages

These pages are retained because validation expects them and they may be useful for deeper review, but they are not part of the primary public navigation:

```text
branches.html      Supplemental department/research view. Public nav currently hides it.
matrix.html        Supplemental department/employer matrix.
analytics.html     Supplemental clustering/audit view with the intentionally restored
                   action-first research queue in assets/research-queue-page.js.
```

Do not delete supplemental retained pages unless validation scripts and public workflow are updated in the same work cycle.

## Public filter scope

Aaron has intentionally reopened the public filter decision. Do not revert the app to a date/promoter-only model.

Current page-specific filter direction:

```text
opportunities.html: text search (name, city, venue, producer), state, department, producer/promoter, date/month
calendar.html: date/month, plus any page-specific calendar controls
map.html: state and date/month; no department filter in current UI
employers.html: text search (name, type, state), department, state, employer type
sources.html: festival, department, employer
schedule.html: date/month (off public navigation; reachable by direct URL only)
iatse.html: text search for local number, city, state, state abbreviation, craft, district, and organization family
```

Opportunities and Employers paginate results 10 per page with a numbered Prev/Next jumper; changing any search or filter resets to page 1. The IATSE page is tabbed (How to join / Find a local / About IATSE) and paginates its local directory the same way.

Do not expose confidence, value-tier, accommodation, travel, per-diem, source-quality, or research-queue status as primary public filters unless Aaron explicitly reopens those items.

## Active shared files

```text
assets/atlas.css
assets/atlas-core-v2.js
assets/approx-date-labels.js
assets/festival-modal-public-safe.js
assets/calendar-interactive.js
assets/map-page-static.js
assets/employers-department-browser.js
assets/sources-employer-links.js
assets/guide-page.js
assets/research-queue-page.js        analytics.html supplemental audit queue only
assets/site-footer.js
assets/icons.js
data/iatse-us-local-directory.js
data/iatse-organization-info.js
data/packages/opportunity-taxonomy.js
data/packages/research-queue-route-updates.js
data/packages/opportunity-rollover-2027.js
data/packages/public-cycle-scope.js
data/packages/opportunity-coords.js
data/packages/festival-research-master-list.js
data/packages/branch-research-manifest.js
```

Retired public helpers must not be reintroduced:

```text
assets/confidence-badges.js
assets/opportunities-promoter-filter.js
assets/opportunities-date-sort.js
assets/iatse-page.js
```

`assets/research-queue-page.js` is no longer retired. It is intentionally restored for the supplemental `analytics.html` audit queue. It must not be moved into primary public navigation, cards, modals, map popups, schedule cards, or public filters unless Aaron explicitly changes the app scope.

## Runtime ownership

`assets/atlas-core-v2.js` owns core public rendering, opportunity date sorting, producer/promoter filter population and filtering, IATSE organization rendering, modals, Sources rendering, and the current Schedule renderer.

External page renderers remain acceptable only where they are intentionally page-owned:

```text
assets/calendar-interactive.js          Calendar
assets/map-page-static.js               Map
assets/employers-department-browser.js  Employers
assets/sources-employer-links.js        Sources support
assets/guide-page.js                    Guide content
assets/research-queue-page.js           Analytics supplemental audit queue
```

Do not create patch-layer helper scripts for behavior that belongs in an existing owner file.

## Required runtime load order

Every active core HTML page must load the main data packages, then the public-safe research update packages, then any public-cycle scoping guard, then the app runtime. Current order for primary app pages:

```html
