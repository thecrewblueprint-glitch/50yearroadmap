---
{
  "chunk_id": "kimi-batch-2026-07-05__md_handoff_bundle__raw_sources__Pasted_markdown3.md__chunk-0002",
  "archive_id": "kimi-batch-2026-07-05",
  "archive_filename": "kimi-batch-2026-07-05.zip",
  "source_path": "md_handoff_bundle/raw_sources/Pasted_markdown3.md",
  "chunk_index": 2,
  "chunk_count_for_source": 3,
  "char_start": 11330,
  "char_end": 23288,
  "source_sha256": "a4c0f3eb41d3a31b64d0ae178aa8a196f3b0d4124a0fd1d66da14c5080270feb",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

esses.
    
-   Pay rates, hourly rates, day rates, weekly rates, salary ranges, or compensation amounts.
    
-   Hotel names, hotel addresses, crew lodging booking details, rooming lists, or private accommodation instructions.
    
-   Private field notes, NDA-covered information, client-sensitive information, crew gossip, or forum rumors as confirmed facts.
    
-   Anything behind a login, paywall, private Facebook group, private Discord, private crew board, or non-public document.
    
-   Raw scraped text. Summarize and attribute instead of dumping copied source text.
    

**Public-safe sources include:** official festival/producer/venue websites, verified social media accounts, press releases, industry publications (TPi, IQ, Mondo\*dr, Pollstar), public LinkedIn case studies, and IATSE.org local directory listings.

If a section cannot be confirmed publicly, write exactly:

> Unknown publicly. Human verification needed.

* * *

## 4\. Status Values and How to Use Them

| Field group | Allowed values | Use rules |
| --- | --- | --- |
| Lodging / crew accommodation | confirmed / possible / unknown / unlikely / not_applicable | confirmed only with direct public source. possible requires minimum evidence (see Section 4.1). unknown when nothing public is available. not_applicable when the event structure makes the question irrelevant (e.g., single-day urban event with no overnight crew). |
| Travel / per diem / mileage | confirmed / possible / unknown / unlikely / not_applicable | Do not guess. possible for remote, multi-week, or known touring-vendor patterns only when evidence supports the pattern. |
| Labor route | confirmed / possible / unknown | confirmed requires public route evidence. possible can be producer/venue pattern. unknown means no public route found. |
| Vendor stack | confirmed / partial / unknown | confirmed means department vendors are publicly identified. partial means some departments or producer-level vendors are identified. unknown means no public vendor stack found. |
| Event status | confirmed / postponed / cancelled / tbd | Use confirmed only when dates and producer are publicly announced for 2026. |

### 4.1 "Possible" Decision Rubric

Before assigning `possible` to any field, at least one of the following must be true:

1.  **Producer pattern:** The same producer has confirmed the same pattern at 2+ other events in the past 24 months.
    
2.  **Venue pattern:** The same venue has confirmed the same pattern in prior years with the same event type.
    
3.  **Vendor pattern:** A vendor in the event's ecosystem has public statements (career page, case study, job posting) describing their standard terms for similar events.
    
4.  **Industry standard:** A widely documented industry practice applies (e.g., major multi-day camping festivals typically provide production camping).
    

If none apply, default to `unknown`.

* * *

## 5\. Required Research Sections for Each Event

### A. Crew Accommodation

**Question:** Is lodging, camping, or crew housing typically provided or arranged for production crew?

-   This is not attendee hotel-block research. Focus on production crew during load-in, show days, and strike.
    
-   Look for official crew/vendor pages, producer job postings, vendor job postings, production profiles, and public producer/venue statements.
    
-   Treat Reddit or forum discussions as leads only, not confirmed facts.
    

```
lodgingStatus: 'confirmed|possible|unknown|unlikely|not_applicable',
lodgingNotes: '<public-safe summary>',
lodgingSources: [
  { label: '<source label>', url: '<source URL>', evidenceLevel: 'event-specific|producer-pattern|industry-standard' }
]
```

### B. Travel Compensation

**Question:** Does the production company or vendor route pay for travel, mileage, flights, rental cars, housing, or per diem for out-of-market crew?

-   Search producer and vendor job postings for travel, per diem, mileage reimbursement, housing provided, or fly-out language.
    
-   Company-level evidence is useful, but do not overstate it as event-specific unless the source supports the specific event.
    
-   Do not record dollar amounts or pay rates.
    

```
travelStatus: 'confirmed|possible|unknown|unlikely|not_applicable',
travelNotes: '<public-safe summary>',
travelSources: [
  { label: '<source label>', url: '<source URL>', evidenceLevel: 'event-specific|producer-pattern|industry-standard' }
]
```

### C. Labor and Staffing Route

**Question:** How does a production technician actually get hired for this event?

-   Research IATSE/local jurisdiction route, non-union labor/staffing route, and direct vendor application route.
    
-   Do not name a specific IATSE local number unless confirmed from IATSE.org or a direct current public source.
    
-   Use this wording when uncertain: `verify applicable IATSE/local jurisdiction for <city or site> (research local number before outreach)`
    

```
laborRouteStatus: 'confirmed|possible|unknown',
laborRouteNotes: '<public-safe summary>',
iatseJurisdictionNote: 'verify applicable IATSE/local jurisdiction for <city or site> (research local number before outreach)',
nonUnionRouteNotes: '<public-safe non-union route notes or unknown publicly>',
laborSources: [
  { label: '<source label>', url: '<source URL>', evidenceLevel: 'event-specific|producer-pattern|industry-standard' }
]
```

### D. Vendor Stack

**Question:** What audio, lighting, video/LED, staging, rigging, site-operations, and power companies publicly work this event?

-   Priority departments: staging/structural, audio, lighting, video/LED, rigging, site ops, power, and fencing.
    
-   Use public production profiles, official vendor case studies, official festival partner pages, public LinkedIn credits, and public industry features.
    
-   Do not claim a vendor works a specific event unless the source supports that event or clearly supports the producer route.
    

```
vendorStackStatus: 'confirmed|partial|unknown',
vendorStackNotes: '<public-safe summary>',
vendors: [
  { department: 'audio', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' },
  { department: 'lighting', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' },
  { department: 'video_led', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' },
  { department: 'staging', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' },
  { department: 'rigging', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' },
  { department: 'site_ops', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' },
  { department: 'power', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' },
  { department: 'other', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' }
],
vendorSources: [
  { label: '<source label>', url: '<source URL>', evidenceLevel: 'event-specific|producer-pattern|industry-standard' }
]
```

* * *

## 6\. Research Execution Map

Research should be done by producer batch first, then by individual event. This is more efficient than researching isolated events because producer, vendor, and staffing patterns often repeat.

1.  **Producer-level search:** identify public producer patterns, vendor ecosystems, career pages, and labor route clues.
    
2.  **Event-specific search:** confirm what applies to the individual event and avoid unsupported transfer of facts.
    
3.  **Labor route search:** verify city, venue, IATSE/local jurisdiction wording, and public staffing/application paths.
    
4.  **Vendor stack search:** confirm department vendors through production profiles, official vendor pages, or public credits.
    
5.  **Convert to the output block.**
    
6.  **Hand to Claude Code or the database maintainer only after each event block is complete and public-safe.**
    

* * *

## 7\. Recommended Batch Order

*(Unchanged from original — see original Section 7)*

* * *

## 8\. Priority Event List

*(Unchanged from original — see original Section 8)*

**Scoring methodology:** Events are scored based on estimated production scale (stage count, attendance, load-in duration), 1099 contractor accessibility (public hiring routes, non-union pathways), and travel cost reasonableness (proximity to major markets, lodging availability). Score is a composite 0–100. Tier 1 = 60+, Tier 2 = 50–59, Tier 3 = 40–49, Tier 4 = 30–39.

* * *

## 9\. Search Query Bank

| Research area | Suggested searches |
| --- | --- |
| Crew accommodation | <festival name> crew camping production<festival name> production crew lodging<festival name> vendor camping crew<producer name> production jobs lodging provided<festival name> site crew housing |
| Travel and per diem | <producer name> production jobs per diem<producer name> travel crew lodging production<vendor name> festival crew travel per diem<festival name> production manager crew logistics |
| Labor and staffing route | <festival name> production crew jobs 2026<festival name> stagehand jobs<festival name> labor provider<venue name> IATSE<city name> IATSE jurisdiction<producer name> careers event production |
| Vendor stack | <festival name> TPi Magazine production<festival name> Mondo dr production<festival name> IQ Magazine production vendors<festival name> audio lighting video staging vendor<festival name> production credits vendors<vendor name> <festival name> case study |

**Advanced operators for 2026-specific results:**

-   `"<festival name>" "2026" "production crew" after:2025-09-01`
    
-   `site:linkedin.com "<festival name>" "production"`
    
-   `site:glassdoor.com "<producer name>" "festival" "per diem"`
    
-   `site:iatse.org "<city name>" local`
    

* * *

## 10\. Required Output Template

Return one block per event. Keep source URLs inside source arrays. Do not include private contacts, pay rates, lodging addresses, or rumor-only claims.

**Copy this exactly.** Paste into `data/packages/opportunities-2026.js` and run `npm run validate:all` before pushing.

```
{
  id: '<event-id>',
  eventStatus: 'confirmed|postponed|cancelled|tbd',
  eventDates: { loadInStart: 'YYYY-MM-DD', showDates: 'YYYY-MM-DD to YYYY-MM-DD', strikeEnd: 'YYYY-MM-DD', totalDaysOnSite: <number> },
  lastVerified: 'YYYY-MM-DD',
  lodgingStatus: 'confirmed|possible|unknown|unlikely|not_applicable',
  lodgingNotes: '<public-safe summary>',
  lodgingSources: [
    { label: '<source label>', url: '<source URL>', evidenceLevel: 'event-specific|producer-pattern|industry-standard' }
  ],
  travelStatus: 'confirmed|possible|unknown|unlikely|not_applicable',
  travelNotes: '<public-safe summary>',
  travelSources: [
    { label: '<source label>', url: '<source URL>', evidenceLevel: 'event-specific|producer-pattern|industry-standard' }
  ],
  laborRouteStatus: 'confirmed|possible|unknown',
  laborRouteNotes: '<public-safe summary>',
  iatseJurisdictionNote: 'verify applicable IATSE/local jurisdiction for <city or site> (research local number before outreach)',
  nonUnionRouteNotes: '<public-safe non-union route notes or unknown publicly>',
  laborSources: [
    { label: '<source label>', url: '<source URL>', evidenceLevel: 'event-specific|producer-pattern|industry-standard' }
  ],
  vendorStackStatus: 'confirmed|partial|unknown',
  vendorStackNotes: '<public-safe summary>',
  vendors: [
    { department: 'audio', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' },
