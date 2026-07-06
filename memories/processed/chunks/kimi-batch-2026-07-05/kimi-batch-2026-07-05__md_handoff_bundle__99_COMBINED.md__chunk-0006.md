---
{
  "chunk_id": "kimi-batch-2026-07-05__md_handoff_bundle__99_COMBINED.md__chunk-0006",
  "archive_id": "kimi-batch-2026-07-05",
  "archive_filename": "kimi-batch-2026-07-05.zip",
  "source_path": "md_handoff_bundle/99_COMBINED.md",
  "chunk_index": 6,
  "chunk_count_for_source": 11,
  "char_start": 56911,
  "char_end": 68900,
  "source_sha256": "9772a55e6bd39feb19ba3cd97e82a79ceb707555954f39f31d7c675db0f025a1",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

Batch Order

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
  ],
  unknownsList: [
    '<what still needs human verification>'
  ],
  publicSafetyNotes: 'No private contacts, pay rates, lodging details, or rumor-only claims included.'
}
```

* * *

## 11\. Source Quality and Handoff Rules

-   Prefer official festival, venue, producer, vendor, union, and production-industry sources over generic blogs or forums.
    
-   Industry publications such as TPi, IQ, Mondo\*dr, Pollstar, SoundGirls, and vendor case studies are especially useful for vendor-stack research.
    
-   If using Reddit or forums, use them only to generate search leads. Do not cite them as confirmed production facts unless the requester explicitly permits that level of evidence.
    
-   Separate producer-level patterns from event-specific confirmed facts. Use the `evidenceLevel` field to flag the distinction.
    
-   If a source supports only a producer-level pattern, label it `producer-pattern` in `evidenceLevel`. Never imply one event uses a vendor just because another event by the same producer does.
    

After research, send this database handoff line with the completed event block:

> Here are research results for `<event name>` (ID: `<event-id>`). Update `data/packages/opportunities-2026.js` with these fields: `<paste output block>`. Run `npm run validate:all` before pushing.

* * *

## 12\. Final Quality Checklist for the Outside Researcher

-   \[ \] Every confirmed claim has a source URL.
    
-   \[ \] `possible` values are clearly labeled and meet the rubric in Section 4.1.
    
-   \[ \] Unknown sections say: *Unknown publicly. Human verification needed.*
    
-   \[ \] No private contacts, phone numbers, personal emails, pay rates, hotel names, rooming details, rumors, or NDA-sensitive material are included.
    
-   \[ \] IATSE/local wording is cautious unless a current direct public source confirms exact jurisdiction details.
    
-   \[ \] Vendor names are tied to public source evidence and separated by department.
    
-   \[ \] `evidenceLevel` is set for every source.
    
-   \[ \] `lastVerified` is today's date.
    
-   \[ \] `eventDates` and `eventStatus` are filled if publicly available.
    
-   \[ \] The final answer includes one data-ready block per event and a source list.
    

* * *

## 13\. Human Verification Protocol

When a field is marked `unknown` or needs human verification:

1.  **Who verifies:** The database maintainer or a designated outreach contact (not the external researcher).
    
2.  **How to verify:** Contact the producer's public careers email, the venue's public production contact, or the vendor's public business development channel. Do not use private crew boards or DMs.
    
3.  **What to ask:** "What is the public application process for production crew for \[event name\] 2026?" or "Does \[producer/vendor\] provide crew lodging or travel support for out-of-market technicians?"
    
4.  **Do not ask about:** Pay rates, specific hotel names, rooming lists, or private contact details.
    
5.  **Re-submission:** Verified data should be returned as a new research packet with `lastVerified` updated and sources labeled `event-specific`.
    

* * *

## Summary of Changes from Version 1.0

| Change | Section | Rationale |
| --- | --- | --- |
| Added eventStatus | 4, 10 | Track cancelled/postponed/TBD events |
| Added eventDates (load-in, show, strike) | 10 | Essential for travel cost decisions |
| Added lastVerified | 10 | Freshness tracking |
| Added not_applicable status | 4 | Handle structurally irrelevant fields |
| Added "Possible" rubric | 4.1 | Reduce researcher inconsistency |
| Added evidenceLevel | 5, 10 | Separate producer patterns from event facts |
| Split site_ops_power into site_ops and power | 5D | More actionable vendor detail |
| Added other vendor department | 5D | Catch-all for non-standard vendors |
| Added advanced search operators | 9 | 2026-specific results |
| Added unknownsList | 10 | Track gaps for human verification |
| Added Human Verification Protocol | 13 | Close process loop on unknown fields |
| Documented scoring methodology | 8 | Transparency for researchers |
| Added positive public-safe source definition | 3 | Clarify what is acceptable |

* * *

Ready to research an event or producer batch whenever you name one.

<!-- END 03_production_atlas_research_handoff_review_and_v2.md -->


---

<!-- BEGIN 04_production_atlas_batch1_research_and_research_plan_context.md -->

# Production Atlas — Batch 1 Research + Better Research Plan Context

Source file: `Pasted markdown(4).md`

---

Original URL: https://www.kimi.com/chat/19ef7005-7272-8355-8000-09e2ac710ab6?chat_enter_method=history
Export Time: 7/5/2026, 5:10:46 PM

**[USER]**

I am giving you a handoff document for Production Atlas / Festival Atlas research.

Your job is to use the document as the full project context and produce public-safe research results for the event or producer batch I name next.

Do not include private contacts, phone numbers, personal emails, pay rates, hotel/lodging details, rumors, login-only information, or copied scraped text.

Focus only on:
1. crew lodging / camping / accommodation signals
2. travel / per diem / mileage / housing support signals
3. labor and staffing routes
4. IATSE/local jurisdiction verification language
5. public production vendor stack

Use only public sources. If something is not publicly confirmed, say:
“Unknown publicly. Human verification needed.”

Use “possible” only when the pattern is strong but not directly confirmed.

Return results in the JavaScript-style output format from the handoff document, with source labels and URLs included.

Start with this target:
[PASTE EVENT NAME OR PRODUCER BATCH HERE]

---

**[ASSISTANT]**

I understand the handoff document and its requirements. I'm ready to research any event or producer batch you specify.

Please paste the **event name or producer batch** you want me to start with, and I'll begin public-safe research immediately.

For reference, here are the batch options from the handoff document:

-   **Batch 1**: Danny Wimmer Presents (Louder Than Life, Bourbon & Beyond, Welcome to Rockville, Sonic Temple, Aftershock, Inkcarceration)
    
-   **Batch 2**: Goldenvoice / AEG (Coachella, Stagecoach, Portola)
    
-   **Batch 3**: Insomniac / Live Nation EDM (EDC Las Vegas, EDC Orlando, HARD Summer, Beyond Wonderland SoCal, Countdown NYE, Dreamstate SoCal, Electric Forest)
    
-   **Batch 4**: C3 Presents / Live Nation (Bonnaroo, Lollapalooza Chicago, Austin City Limits, Shaky Knees, Oceans Calling, Sea.Hear.Now, Roots Picnic, Railbird)
    
-   **Batch 5**: Multi-market split records (Breakaway, Country Thunder)
    
-   **Batch 6**: Remote / lodging-sensitive festivals (Electric Forest, Bonnaroo, Hulaween, Rock Fest Wisconsin, High Sierra, FloydFest, Pickathon, Telluride Bluegrass, Hinterland)
    

Or you can name a **specific event** from the priority list (e.g., `Summerfest 2026`, `BottleRock Napa Valley 2026`, `New Orleans Jazz Fest 2026`, etc.).

What would you like me to research first?

---

**[USER]**

Batch 1

---

**[ASSISTANT]**

I'll research **Batch 1: Danny Wimmer Presents** — covering Louder Than Life, Bourbon & Beyond, Welcome to Rockville, Sonic Temple, Aftershock, and Inkcarceration. Let me start with producer-level research and then drill into each event.

