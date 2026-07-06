---
{
  "chunk_id": "kimi-batch-2026-07-05__md_handoff_bundle__03_production_atlas_research_handoff_review_and_v2.md__chunk-0003",
  "archive_id": "kimi-batch-2026-07-05",
  "archive_filename": "kimi-batch-2026-07-05.zip",
  "source_path": "md_handoff_bundle/03_production_atlas_research_handoff_review_and_v2.md",
  "chunk_index": 3,
  "chunk_count_for_source": 3,
  "char_start": 22685,
  "char_end": 28227,
  "source_sha256": "d9d5ccdc7e3b2f8f9b1f57090dc4b701f388b731c09dba7cf02c060d87d22b80",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

ed|partial|unknown',
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
