# July 2026 Month-to-Date Work Report (Public-Safe Digest)

> Provenance: sanitized digest of an owner-supplied July 1–16 month-to-date work
> report. Per DATA_SAFETY_POLICY.md, the following were **redacted** from the
> committed version: income amounts and per-client pay breakdowns, bank/financial
> details, personal/third-party names and emails, reservation/receipt numbers and
> lodging specifics, and secret names. The full unredacted report is kept
> privately by the owner, not in this repo. Work activity and decisions are
> preserved.

## Executive summary

In the first half of July 2026, work combined active paid production labor
(Michigan and Wisconsin) with substantial Deadhang Labor LLC administration:
tax systems, financial recordkeeping, job-search materials, website/portfolio,
repositories, and a new print-on-demand merchandise operation.

Confirmed paid production labor: **60 hours** total.

| Work period | Confirmed hours | Role breakdown |
| --- | ---: | --- |
| Michigan festival run (Jul 1–2) | 20 | Production labor |
| Wisconsin run (Jul 11–14) | 40 | 33 hand hours; 7 climber/rigger hours |
| **Total** | **60** | 53 general production; 7 climber/rigger |

In parallel: established a permanent tax knowledge base repository, developed
six tax-planning manuals, consolidated 2026 work-income tracking, converted
future Upstage Companies work from W-2 to 1099 invoicing, rebuilt resumes and
outreach materials, advanced Festival/Production Atlas and The Crew Blueprint
content infrastructure, advanced the Deadhang roadmap/command center and
portfolio, and began a print-on-demand clothing line with a planned
GitHub/Printify automation pipeline.

## Workstreams

### 1. Tax knowledge base
Turned tax research into a permanent GitHub-hosted operating knowledge base in a
dedicated invoicing repository (`knowledge-base/` root). Set up an initial file
set (business overview, expense categories, recordkeeping, future topics,
disclaimer) and a broad long-term folder architecture (accounting, bookkeeping,
audit, compliance, deductions, depreciation, equipment, finance, insurance, IRS,
legal, LLC, mileage, payroll, procedures, receipts, retirement, Schedule C,
S-corp planning, state tax, templates, travel, general taxes). Produced six
repository-ready manuals: estimated quarterly tax planning, self-employment tax,
QBI, S-corp election decision framework, annual tax strategy framework, and tax
elections & strategic decisions. Backlog: Pub 535 summary, Schedule C overview,
Pub 463 summary, expense-substantiation guide, depreciation fundamentals.

### 2. Financial reconstruction and tax prep
Assessed whether prior-year business expenses can be reconstructed despite
incomplete contemporaneous tracking; organized financial records for tax-preparer
use. Consolidated 2026 work-income tracking across multiple staffing companies
(both W-2 and 1099). *(Specific amounts and per-client figures redacted.)* Next
step: publish the master work/contracts/payments tracker as a native Google Sheet
in the Business folder.

### 3. Upstage Companies 1099 / invoicing transition
Submitted updated W-9 and direct-deposit info to switch future Upstage work from
W-2 to 1099. Upstage confirmed and stated future projects must be invoiced.
Preserved the invoicing rules: required fields (name, event name, event date,
hours, hourly rate, total), a dedicated invoice destination address, and a
required email subject format. Continued broader invoice logic, including
checking Guardian Production Services rules.

### 4. Travel, lodging, and expense tracking
Reconciled travel and lodging records for the Michigan run and layover
(hotel folios, an Amtrak trip, a storage payment, and a bank-activity review for
layover expenses). *(Amounts, reservation/receipt numbers, and lodging specifics
redacted.)* Travel-planning covered routes between Chicago, Twin Lakes,
Milwaukee, and the Wisconsin job location.

### 5. Resume / application / job-search
Substantially rebuilt professional materials for live-event production work:
IATSE Local 26 outreach (certifications removed as requested); a Kalamazoo-area
search surfacing a Stage Technician role (Chenery Auditorium) and a Technical
Director role (Farmers Alley Theatre); multiple business-forward resumes; a
Mountain Productions-targeted package; formatting/consistency audits; employer
name corrections; reframed sections (`Venue Experience`, `Festival Experience`);
separation of direct employers from shared-jobsite experience; cleaned reference
list *(names redacted)*; and a 500-character LinkedIn services description.
Emphasis: national-travel readiness, load-ins/outs, staging, lighting, A/V
support, set changes, equipment safety, and supervised rigging support without
overstating employment relationships.

### 6. Festival Atlas / Production Atlas
Continued building/debugging the static, public-safe research platform
(opportunities, calendar, map, employers, IATSE, contribute, feedback, sources;
schedule data kept off public nav). Reaffirmed the public-safety rule: never
publish private contacts, phone numbers, emails, pay rates, lodging, crew rumors,
NDA material, or client-sensitive info; label uncertain claims "Unknown
publicly. Human verification needed." Jul 15 fixes: filter out past-dated
festivals; add/repair 2026/2027 year filters; persist filters in URL params;
restore IATSE directory rendering; improve light-mode contrast; move theme toggle
top-right; repair calendar header; update cache-busting. Also flagged improving
union-local-number searches (e.g., "local 26", "iatse 26", "26").

### 7. The Crew Blueprint content repository
Worked in the private content repository to add a static course-preview and
course-JSON browser workflow (`course-preview.html`, usage doc, README links).
Supports previewing/validating course material without prematurely returning to a
complex LMS deployment.

### 8. Deadhang roadmap and command center
Refined the roadmap/command-center implementation. Added two workflow
requirements: a "You are now here" control and a "Move to later" status for
deferred tasks that keeps the linear order. Purpose: prevent idea sprawl,
forgotten half-built projects, and loss of the business-development sequence.
Working context: this `50yearroadmap` repo (commit to `main`; validate on
`roadmap.json` changes). *(Both features are now implemented in the roadmap.)*

### 9. Portfolio and website
SSL/security remained the last open core website/cPanel item after business email
was confirmed working; prepared Country Thunder Wisconsin content for the
portfolio; maintained accurate, non-overstated portfolio captions.

### 10. Print-on-demand clothing line
Began turning Deadhang humor and branding into a print-on-demand clothing line:
evaluated LLC tax/bookkeeping impact, compared print quality/pricing and mobile
vendor connectivity, and selected shirt concepts (e.g., "Gravity Is Always
Hiring", "It's Not Heavy Unless You Lift It Wrong", "Professional Box Pusher",
"Not My Department Today", "Powered by Catering Coffee", "Living Out of a Pelican
Case"), plus a Deadhang-branded logo/tower concept.

### 11. Printify automation pipeline
Defined a production-automation project (a dedicated GitHub repo) — a Python 3.12
+ GitHub Actions pipeline so a "Make this into a shirt" command handles artwork
processing, Printify upload, product creation, pricing, and publishing without
manual API/product steps. Uses an existing GitHub secret *(name redacted)*.
Status: handoff/specification stage; production implementation not yet verified.

## Key decisions
- Jul 2 (not Jul 3) was the final Michigan workday.
- Upstage work moves to a 1099 invoicing workflow for future projects.
- The permanent tax reference system lives in the invoicing repo's knowledge base.
- Tax docs should be operational, authoritative, and repository-ready (AI/bookkeeper/CPA-usable), not one-off answers.
- Festival/Production Atlas must stay public-safe and distinguish unknown from verified.
- The roadmap must stay linear even when tasks are deferred.
- The clothing operation uses print-on-demand rather than holding inventory initially.
- Printify automation relies on the existing GitHub secret and removes routine manual steps.

## Open / unverified items
- Confirm whether any paid shifts occurred after Jul 14 (none in the recovered record).
- Recover/reconcile an expected Grand Rapids hotel receipt; classify a storage payment before treating it as a business expense.
- Complete the bank-transaction review for the layover period and attach supporting receipts.
- Publish the master work/payments tracker as a native Google Sheet.
- Confirm the final Guardian Production Services invoicing procedure.
- Verify Festival Atlas fixes live after cache-busting.
- Complete the remaining Deadhang website SSL/security work.
- Add and publish the Country Thunder Wisconsin portfolio content.
- Continue the tax-document backlog and confirm all manuals are committed.
- Implement and test the Printify automation pipeline.
- Produce final production-ready shirt artwork and confirm garment/provider choices.
