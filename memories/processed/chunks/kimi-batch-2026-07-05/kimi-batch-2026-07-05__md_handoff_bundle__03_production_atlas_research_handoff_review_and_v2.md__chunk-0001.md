---
{
  "chunk_id": "kimi-batch-2026-07-05__md_handoff_bundle__03_production_atlas_research_handoff_review_and_v2.md__chunk-0001",
  "archive_id": "kimi-batch-2026-07-05",
  "archive_filename": "kimi-batch-2026-07-05.zip",
  "source_path": "md_handoff_bundle/03_production_atlas_research_handoff_review_and_v2.md",
  "chunk_index": 1,
  "chunk_count_for_source": 3,
  "char_start": 0,
  "char_end": 11998,
  "source_sha256": "d9d5ccdc7e3b2f8f9b1f57090dc4b701f388b731c09dba7cf02c060d87d22b80",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Production Atlas — Research Handoff Review and Revised V2

Source file: `Pasted markdown(3).md`

---

Original URL: https://www.kimi.com/chat/19ef7afe-9032-804c-8000-09e2d8602934?chat_enter_method=history
Export Time: 7/5/2026, 5:10:32 PM

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

I understand the project context. I'm ready to research any event or producer batch you name.

Please paste the event name or producer batch you'd like me to start with. For example:

-   **Producer batch:** "Danny Wimmer Presents" (Batch 1)
    
-   **Individual event:** "Louder Than Life 2026" or "EDC Las Vegas 2026"
    
-   **Tier list:** "All Tier 1 events"
    

What should I research first?

---

**[USER]**

Find flaws in the research packet and make it better.

---

**[ASSISTANT]**

I need to see the research packet you're referring to. Could you paste it here? Once I have it, I'll review it against the handoff document requirements and flag any issues with:

-   **Public-safety violations** (private contacts, pay rates, hotel details, rumors, etc.)
    
-   **Status value misuse** (confirmed vs. possible vs. unknown)
    
-   **Missing source URLs** or weak attribution
    
-   **IATSE/local jurisdiction wording** that isn't cautious enough
    
-   **Vendor claims** that aren't tied to public evidence
    
-   **Producer-level patterns** overstated as event-specific facts
    
-   **Template compliance** (missing fields, wrong format)
    

Paste the packet and I'll give you a clean critique plus suggested fixes.

---

**[USER]**

The research handoff document

---

**[ASSISTANT]**

I understand — you'd like me to review the research handoff document itself for flaws and suggest improvements.

Here is my critique, organized by severity and section:

* * *

## Critical Flaws

### 1\. No Event-Specific Date Fields

The template (Section 10) lacks `eventDates`, `loadInDates`, or `strikeDates`. For a traveling 1099 contractor, knowing when load-in starts and when strike ends is essential for booking travel and deciding if accommodation costs are justified. Without dates, the "can I afford to work this event?" question cannot be answered.

**Fix:** Add `loadInStart`, `showDates`, `strikeEnd`, and `totalDaysOnSite` to the output template.

### 2\. "Possible" Is Over-Used and Under-Defined

Section 4 allows `possible` for lodging, travel, and labor routes when "strong venue/producer pattern supports it but no source confirms it." This is a judgment call with no criteria. Two researchers will apply it differently.

**Fix:** Add a decision rubric for `possible`:

-   At least 2 prior events by the same producer with the same pattern?
    
-   Same venue used in prior years with confirmed pattern?
    
-   Same vendor ecosystem with public statements about their standard terms?
    
-   Otherwise, default to `unknown`.
    

### 3\. No Deduplication Rule for Producer Batches

Section 6 says research by producer batch first, but Section 10's output template has no field to flag "this is a producer-level pattern, not event-specific." This risks event blocks being inflated with unconfirmed producer assumptions.

**Fix:** Add a `evidenceLevel` field to each source object: `'event-specific' | 'producer-pattern' | 'industry-standard'`.

### 4\. Vendor Stack Departments Are Too Narrow

`site_ops_power` is one field, but site ops and power are often separate vendors (e.g., one company does fencing/site logistics, another does generators/utility tie-ins). Collapsing them loses actionable detail.

**Fix:** Split into `site_ops` and `power`, or add an `other_vendors` catch-all array for departments not in the fixed list.

* * *

## Moderate Flaws

### 5\. Search Query Bank Is Under-Indexed for 2026

Section 9 suggests generic queries like `<festival name> production crew jobs 2026` but doesn't include year-specific operators, date-restricted searches, or LinkedIn/Glassdoor as explicit sources. Many festivals haven't announced 2026 details yet.

**Fix:** Add queries like:

-   `"<festival name>" "2026" "production crew" after:2025-09-01`
    
-   `site:linkedin.com "<festival name>" "production"`
    
-   `site:glassdoor.com "<producer name>" "festival" "per diem"`
    

### 6\. No "Not Applicable" Status

Some fields genuinely don't apply. For example, a single-day urban festival at a permanent venue may have no crew camping at all — not "unlikely," but structurally irrelevant. "Unlikely" implies it was considered and rejected.

**Fix:** Add `not_applicable` as an allowed status for lodging/travel fields, with a note explaining why.

### 7\. Missing "Last Verified" Timestamp

The document says "Current as of 2026-06-23" but the output template has no per-event `lastVerified` field. A contractor looking at data from January vs. June needs to know freshness.

**Fix:** Add `lastVerified: 'YYYY-MM-DD'` to every output block.

### 8\. No Escalation Path for "Human Verification Needed"

Section 12 says "Unknown publicly. Human verification needed" but never says *who* does the verification or *how* it gets back into the database. This is a process gap, not a template gap, but it will cause stale `unknown` fields to persist.

**Fix:** Add a Section 13: "Human Verification Protocol" — define who contacts the producer/vendor, what questions to ask, and how verified data is re-submitted.

* * *

## Minor / Polish Issues

### 9\. Inconsistent Score Granularity

Tier 1 is 60+, Tier 2 is 50–59, but some Tier 2 events (Austin City Limits at 58, Welcome to Rockville at 58, Hulaween at 58) score higher than Tier 3 events (Sick New World at 48, Oceans Calling at 48). The scoring methodology isn't explained, so a researcher can't verify or challenge a score.

**Fix:** Document the scoring formula in Section 8 or move it to an appendix.

### 10\. "Public-Safe" Is Defined by Negation

Section 3 lists what *not* to include but doesn't define what *is* acceptable. For example, is a public LinkedIn post by a vendor naming a festival a valid source? Is a festival's official "partners" page sufficient for vendor confirmation?

**Fix:** Add a positive definition: "Public-safe sources include: official festival/producer/venue websites, verified social media accounts, press releases, industry publications (TPi, IQ, Mondo\*dr, Pollstar), public LinkedIn case studies, and IATSE.org local directory listings."

### 11\. No Handling of Cancelled / Postponed / TBD Events

Okeechobee 2026 already has "Verify current status" in the notes. But the template has no `eventStatus` field (confirmed, postponed, cancelled, TBD).

**Fix:** Add `eventStatus: 'confirmed|postponed|cancelled|tbd'` at the top of each event block.

### 12\. Template Uses Single Quotes and Backslashes

The Section 10 template uses `\'` escaping throughout, which is JavaScript-legal but error-prone for copy-paste handoffs. A malformed paste will break `npm run validate:all`.

**Fix:** Provide a clean JSON template alongside the JS-style block, or add a "Copy this exactly" warning.

* * *

## Summary Table of Fixes

| Priority | Issue | Fix |
| --- | --- | --- |
| Critical | No date fields | Add load-in/show/strike dates |
| Critical | "Possible" undefined | Add rubric with minimum evidence |
| Critical | No producer vs. event distinction | Add evidenceLevel to sources |
| Critical | Vendor departments too narrow | Split site_ops_power |
| Moderate | Search queries outdated | Add 2026-specific operators |
| Moderate | No "not applicable" status | Add to allowed values |
| Moderate | No per-event timestamp | Add lastVerified |
| Moderate | No human verification workflow | Add Section 13 |
| Minor | Score unexplained | Document formula |
| Minor | "Public-safe" vague | Add positive definition |
| Minor | No event status field | Add eventStatus |
| Minor | Template fragile | Add JSON alternative |

* * *

Would you like me to produce a revised version of the handoff document incorporating these changes, or would you prefer I move on to researching an actual event/producer batch using the current (flawed but workable) document?

---

**[USER]**

Yes make the revised version

---

**[ASSISTANT]**

Here is the revised handoff document with all critical, moderate, and minor flaws addressed. I've incorporated the fixes directly into the relevant sections.

* * *

**Production Atlas External Research Handoff**

*Research guide for outside sources with no prior app context*

**Version:** 2.0  
**Current as of:** 2026-06-23

* * *

## 1\. Quick Brief

Production Atlas is a public-safe scouting database for a 1099 live-event production contractor. It tracks United States music festivals and large live events in 2026 and identifies which opportunities are worth pursuing for stagehand, event technician, rigging, lighting, audio, video, staging, and site-operations work.

The research should answer three practical questions:

-   Can a traveling technician get there and afford to work the event? Research crew lodging, camping, housing, travel, mileage, per diem, and related logistics.
    
-   Who is the public hiring route? Research staffing companies, labor brokers, production vendors, producers, venue routes, and public application paths.
    
-   Is there a union or non-union route? Research the applicable IATSE/local jurisdiction when publicly supported, and use verification wording when uncertain.
    

* * *

## 2\. Expected Deliverable

Return a structured research packet for each event or producer batch. The packet must include:

-   A short producer-level summary when researching a producer group.
    
-   One event-level structured block per event using the output template in Section 10.
    
-   Public source URLs for every confirmed or partial claim.
    
-   Clear status values: `confirmed`, `partial`, `possible`, `unlikely`, `unknown`, or `not_applicable`.
    
-   A short unknowns list showing what still needs human verification.
    
-   A `lastVerified` timestamp for every event block.
    

* * *

## 3\. Absolute Public-Safety Rules

Do not research, record, publish, or infer any of the following:

-   Private contact names, personal phone numbers, or personal email addresses.
    
-   Pay rates, hourly rates, day rates, weekly rates, salary ranges, or compensation amounts.
    
-   Hotel names, hotel addresses, crew lodging booking details, rooming lists, or private accommodation instructions.
    
-   Private field notes, NDA-covered information, client-sensitive information, crew gossip, or forum rumors as confirmed facts.
    
-   Anything behind a login, paywall, private Facebook group, private Discord, private crew board, or non-public document.
    
-   Raw scraped text. Summarize and attribute instead of dumping copied source text.
    

**Public-safe sources include:** official festival/producer/venue websites, verified social media accounts, press releases, industry publications (TPi, IQ, Mondo\*dr, Pollstar), public LinkedIn case studies, and IATSE.org local directory listings.

