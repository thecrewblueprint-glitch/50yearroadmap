---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__README.md__chunk-0002",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/README.md",
  "chunk_index": 2,
  "chunk_count_for_source": 2,
  "char_start": 11348,
  "char_end": 20850,
  "source_sha256": "b2ee17bf7416b823056642bd7c24b663803f2fdf97420c49e5165c7874010d51",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

               Map
assets/employers-department-browser.js  Employers
assets/sources-employer-links.js        Sources support
assets/guide-page.js                    Guide content
assets/research-queue-page.js           Analytics supplemental audit queue
```

Do not create patch-layer helper scripts for behavior that belongs in an existing owner file.

## Required runtime load order

Every active core HTML page must load the main data packages, then the public-safe research update packages, then any public-cycle scoping guard, then the app runtime. Current order for primary app pages:

```html
<script src="data/packages/production-branches.js?v=multi1"></script>
<script src="data/packages/opportunities-2026.js?v=multi1"></script>
<script src="data/packages/us-employers.js?v=multi1"></script>
<script src="data/iatse-us-local-directory.js?v=multi1"></script>
<script src="data/packages/opportunity-taxonomy.js?v=taxonomy2"></script>
<script src="data/packages/research-queue-route-updates.js?v=route1"></script>
<script src="data/packages/opportunity-rollover-2027.js?v=rollover2"></script>
<script src="data/packages/public-cycle-scope.js?v=cycle1"></script>
<script src="assets/atlas-core-v2.js?v=multi20"></script>
<script src="assets/approx-date-labels.js?v=approx1"></script>
```

Cache-bust query values are bumped together across all pages whenever the underlying shared asset changes, so every page requests the same current version.

`iatse.html` also loads `data/iatse-organization-info.js`. `map.html` also loads `data/packages/opportunity-coords.js` and `assets/map-page-static.js`. `calendar.html` also loads `assets/calendar-interactive.js`. `employers.html` also loads `assets/employers-department-browser.js`. `sources.html` also loads `assets/sources-employer-links.js`. `analytics.html` loads `assets/research-queue-page.js`. Public modal pages may load `assets/festival-modal-public-safe.js`. Footer/legal/white-page navigation is normalized through `assets/site-footer.js`.

Do not add `async` or `defer` to these data/runtime package scripts.

## Analytics research queue boundary

The action-first research queue currently lives only on the supplemental retained `analytics.html` page. It is public-safe audit/planning scaffolding and is not part of the primary public workflow. Public cards, modals, map popups, schedule cards, and primary page copy should still avoid research queue tasks, internal next actions, confidence/audit language, missing-data warnings, source-needed filler, value-tier badges, or confidence badges.

## Important data files

```text
data/packages/production-branches.js
data/packages/opportunities-2026.js
data/packages/us-employers.js
data/iatse-us-local-directory.js
data/iatse-organization-info.js
data/packages/opportunity-taxonomy.js
data/packages/research-queue-route-updates.js
data/packages/opportunity-rollover-2027.js
data/packages/public-cycle-scope.js
data/packages/opportunity-coords.js
data/packages/festival-research-master-list.js
data/packages/branch-research-manifest.js
data/packages/branch-research-batch-*.js
```

## Active taxonomy, route, cycle, and map packages

```text
data/packages/opportunity-taxonomy.js              source/date research updates
data/packages/research-queue-route-updates.js      public producer/operator route leads
data/packages/opportunity-rollover-2027.js         separate-year 2027 public-cycle bridge
data/packages/public-cycle-scope.js                default public-cycle visibility guard
data/packages/opportunity-coords.js                map coordinates for opportunity records
```

Route updates are public-safe route leads only. They do not confirm vendors, labor providers, private contacts, pay, lodging, travel support, per diem, call times, or referrals.

## Core vs supplemental work-finding data

Core public work-finding display should focus on:

```text
event/festival name
city, state, region
venue/site when known
event dates
approximate production/build/load-in window
approximate strike/load-out window
producer/promoter/operator when publicly known
public employer/vendor/company/labor-route leads
public apply/careers/contact/homepage routes
source availability through sources.html
```

Supplemental data may remain in the repository for deeper research, validation, and source review. Missing supplemental fields should not be blasted publicly.

Hide these from public cards, modals, map popups, schedule cards, and primary page copy:

```text
confidence labels or scores
work-year value scores
priority target labels
next human action
next research action
research queue tasks
route intelligence paragraphs
branch confidence
branch status values
internal evidence summaries
empty branch records
No event-specific branch record yet
unknown / verify / source needed filler
lodging unknown / travel unknown / per diem unknown clutter
verify before outreach repeated as public warning text
```

Accommodation, travel, lodging, per diem, and similar worker-support details are supplemental only. Add them when reliable public information exists, but do not treat missing lodging, travel, or per diem information as a blocker for finding where work is, when it happens, which public producer/employer route exists, or what official route to research next.

## Calendar-cycle and 2027 rollover rule

The chosen rollover model is separate year-specific records.

`data/packages/opportunity-rollover-2027.js` is a temporary static bridge that creates public `*-2027` records for verified 2027 public cycles and archives the corresponding active `*-2026` records out of the active public view. `data/packages/public-cycle-scope.js` additionally keeps the default public 2026 view from mixing in future-year records unless the app scope is changed.

Do not expand the older mutation model where a visible `*-2026` record becomes a 2027 opportunity. Long-term cleanup should move verified `*-2027` records into canonical opportunity data and then shrink or retire the bridge.

Do not update exact dates unless the new public dates are visible from a reliable source. If a page says a future year is coming but does not publish dates, mark the record for review rather than inventing dates.

## Festival research master-list rule

`data/packages/festival-research-master-list.js` is the current festival registry and research-intake control file. It currently contains 258 records after reconciliation. It is not automatically active opportunity data by itself: records must be individually verified and promoted or matched to app data before they should be treated as active public opportunities.

## Employer-link rule

Employer, vendor, producer, venue, and labor-route links are high priority. Prefer public links in this order:

```text
1. apply page
2. careers/jobs page
3. contact page
4. official company homepage
```

A homepage is acceptable when it is the only reliable public route or when the contact/application path is embedded on the homepage. Do not use private contacts, personal emails, phone numbers, pay information, rumors, or private referrals.

## IATSE / local jurisdiction wording rule

Do not name specific IATSE local numbers in event route research notes unless a direct current public source supports that exact jurisdiction claim and the context requires it.

Preferred event-route language:

```text
verify applicable IATSE/local jurisdiction for <city or site> (research local number before outreach)
```

The `iatse.html` page is built around how a worker actually joins IATSE: the overhire-to-membership path, the permit-vs-member distinction, other ways in, official IATSE resource links, and a searchable local directory. Each local opens a modal with actionable join steps and a link to the official directory for that local's real contact.

## Branch research loading rule

Branch research data is loaded through:

```text
data/packages/branch-research-manifest.js
```

When adding a new branch research batch:

1. Create one data package in `data/packages/`.
2. Create one matching report in `research/`.
3. Add the data package filename to `data/packages/branch-research-manifest.js`.
4. Keep the rule: one branch research data file equals one `window.*` export only.
5. Run validation when possible, or document inability to run validation if using connector-only access and Aaron says continue.

## Public-safety rules

Public data may include official/public links, employer homepages, source records, public route notes, public company names, public producer/promoter/operator names, and public apply/careers/contact routes.

Do **not** publish:

```text
private contacts
phone numbers
personal emails
pay rates
hotel/lodging details
crew rumors
private field notes
NDA information
client-sensitive information
private referrals
```

Source links belong on:

```text
sources.html
```

Do not put raw source links inside public popups.

## Validation

```bash
npm run validate:data
npm run validate:branch-research
npm run validate:static-app
npm run validate:all
```

`validate:all` currently runs all three validation layers.

GitHub Actions workflows:

```text
.github/workflows/validate-branch-research.yml
.github/workflows/deploy-research-version-pages.yml
```

When Aaron says continue from a connector-only environment, continue making requested edits, state that validation was not run from the environment, and treat human live visual review as the immediate review gate. Do not claim validation passed unless it actually ran.
