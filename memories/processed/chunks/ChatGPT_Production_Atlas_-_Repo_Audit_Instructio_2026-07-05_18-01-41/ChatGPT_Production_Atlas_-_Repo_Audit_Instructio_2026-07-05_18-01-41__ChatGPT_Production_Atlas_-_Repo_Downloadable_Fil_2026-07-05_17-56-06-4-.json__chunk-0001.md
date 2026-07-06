---
{
  "chunk_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Repo_Downloadable_Fil_2026-07-05_17-56-06-4-.json__chunk-0001",
  "archive_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41",
  "archive_filename": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41.zip",
  "source_path": "ChatGPT_Production_Atlas_-_Repo_Downloadable_Fil_2026-07-05_17-56-06 (4).json",
  "chunk_index": 1,
  "chunk_count_for_source": 4,
  "char_start": 0,
  "char_end": 11926,
  "source_sha256": "e5be644cabf4cbf2a98271b7dbccb22c5a7bc6e0b499720d5f7cbaaeb5007daa",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

{
  "v": 2,
  "p": "chatgpt",
  "m": [
    [
      "a",
      "t1",
      "I’ll create a clean standalone handoff document for an outside researcher who has no project context. I’ll pull the current repo-visible research guide first, then generate a downloadable file."
    ],
    [
      "a",
      "t2",
      "I’ll pull the latest repo-visible research guide and package it as a standalone outside-researcher handoff. I’ll generate a polished .docx and verify the rendered pages before giving you the download."
    ],
    [
      "a",
      "t3",
      "The repo search index is not finding the new file by keyword, so I’m fetching the exact path from the last update. Then I’ll build the standalone handoff from that content plus the mapped execution plan."
    ],
    [
      "a",
      "t4",
      {
        "txt": "Created a standalone outside-researcher handoff file. It includes:\nDownload it here:",
        "c": [
          "c1",
          "c2"
        ]
      }
    ],
    [
      "u",
      "t5",
      {
        "txt": "Production_Atlas_External_Research_Handoff.docxDocumentHere is the revised handoff document with all critical, moderate, and minor flaws addressed. ---\n\nProduction Atlas External Research Handoff\n\nResearch guide for outside sources with no prior app context\n\nVersion: 2.0\n\nCurrent as of: 2026-06-23\n\n---\n\n1. The research should answer three practical questions:\n\n- Can a traveling technician get there and afford to work the event? - Who is the public hiring route? - Is there a union or non-union route? The packet must include:\n\n- A short producer-level summary when researching a producer group. - One event-level structured block per event using the output template in Section 10. - Public source URLs for every confirmed or partial claim. - Clear status values: confirmed, partial, possible, unlikely, unknown, or not_applicable. - A short unknowns list showing what still needs human verification. - A lastVerified timestamp for every event block. Absolute Public-Safety Rules\n\nDo not research, record, publish, or infer any of the following:\n\n- Private contact names, personal phone numbers, or personal email addresses. - Pay rates, hourly rates, day rates, weekly rates, salary ranges, or compensation amounts. - Hotel names, hotel addresses, crew lodging booking details, rooming lists, or private accommodation instructions. - Private field notes, NDA-covered information, client-sensitive information, crew gossip, or forum rumors as confirmed facts. - Anything behind a login, paywall, private Facebook group, private Discord, private crew board, or non-public document. - Raw scraped text. Summarize and attribute instead of dumping copied source text. Public-safe sources include: official festival/producer/venue websites, verified social media accounts, press releases, industry publications (TPi, IQ, Mondodr, Pollstar), public LinkedIn case studies, and IATSE.org local directory listings. If a section cannot be confirmed publicly, write exactly:\n\n> Unknown publicly. Travel / per diem / mileage confirmed / possible / unknown / unlikely / not_applicable Do not guess. possible for remote, multi-week, or known touring-vendor patterns only when evidence supports the pattern. Event status confirmed / postponed / cancelled / tbd Use confirmed only when dates and producer are publicly announced for 2026.\n\n4.1 \"Possible\" Decision Rubric\n\nBefore assigning possible to any field, at least one of the following must be true:\n\n1. Required Research Sections for Each Event\n\nA. Crew Accommodation\n\nQuestion: Is lodging, camping, or crew housing typically provided or arranged for production crew? - This is not attendee hotel-block research. - Look for official crew/vendor pages, producer job postings, vendor job postings, production profiles, and public producer/venue statements. - Treat Reddit or forum discussions as leads only, not confirmed facts. Travel Compensation\n\nQuestion: Does the production company or vendor route pay for travel, mileage, flights, rental cars, housing, or per diem for out-of-market crew? - Search producer and vendor job postings for travel, per diem, mileage reimbursement, housing provided, or fly-out language. - Company-level evidence is useful, but do not overstate it as event-specific unless the source supports the specific event. - Do not record dollar amounts or pay rates. Labor and Staffing Route\n\nQuestion: How does a production technician get hired for this event? - Research IATSE/local jurisdiction route, non-union labor/staffing route, and direct vendor application route. - Do not name a specific IATSE local number unless confirmed from IATSE.org or a direct current public source. - Use this wording when uncertain: verify applicable IATSE/local jurisdiction for <city or site> (research local number before outreach)\n\nD. Vendor Stack\n\nQuestion: What audio, lighting, video/LED, staging, rigging, site-operations, and power companies publicly work this event? - Priority departments: staging/structural, audio, lighting, video/LED, rigging, site ops, power, and fencing. - Use public production profiles, official vendor case studies, official festival partner pages, public LinkedIn credits, and public industry features. - Do not claim a vendor works a specific event unless the source supports that event or supports the producer route. Hand to Claude Code or the database maintainer only after each event block is complete and public-safe. Search Query Bank\n\nResearch area Suggested searches\nCrew accommodation <festival name> crew camping production <festival name> production crew lodging <festival name> vendor camping crew <producer name> production jobs lodging provided <festival name> site crew housing\nTravel and per diem <producer name> production jobs per diem <producer name> travel crew lodging production <vendor name> festival crew travel per diem <festival name> production manager crew logistics\nLabor and staffing route <festival name> production crew jobs 2026 <festival name> stagehand jobs <festival name> labor provider <venue name> IATSE <city name> IATSE jurisdiction <producer name> careers event production\nVendor stack <festival name> TPi Magazine production <festival name> Mondo dr production <festival name> IQ Magazine production vendors <festival name> audio lighting video staging vendor <festival name> production credits vendors <vendor name> <festival name> case study\n\nAdvanced operators for 2026-specific results:\n- \"<festival name>\" \"2026\" \"production crew\" after:2025-09-01\n- site:linkedin.com \"<festival name>\" \"production\"\n- site:glassdoor.com \"<producer name>\" \"festival\" \"per diem\"\n- site:iatse.org \"<city name>\" local\n\n---\n\n10. Required Output Template\n\nReturn one block per event. Do not include private contacts, pay rates, lodging addresses, or rumor-only claims. Paste into data/packages/opportunities-2026.js and run npm run validate:all before pushing. - Industry publications like TPi, IQ, Mondodr, Pollstar, SoundGirls, and vendor case studies are especially useful for vendor-stack research. - If using Reddit or forums, use them only to generate search leads. Do not cite them as confirmed production facts unless the requester explicitly permits that level of evidence. - Separate producer-level patterns from event-specific confirmed facts. Use the evidenceLevel field to flag the distinction. - If a source supports only a producer-level pattern, label it producer-pattern in evidenceLevel. Never imply one event uses a vendor because another event by the same producer does. Update data/packages/opportunities-2026.js with these fields: <paste output block>. - possible values are labeled and meet the rubric in Section 4.1. - Unknown sections say: Unknown publicly. - No private contacts, phone numbers, personal emails, pay rates, hotel names, rooming details, rumors, or NDA-sensitive material are included. - IATSE/local wording is cautious unless a current direct public source confirms exact jurisdiction details. - Vendor names are tied to public source evidence and separated by department. - evidenceLevel is set for every source. - lastVerified is today's date. - eventDates and eventStatus are filled if publicly available. - The final answer includes one data-ready block per event and a source list. Do not use private crew boards or DMs.\n3. What to ask: \"What is the public application process for production crew for [event name] 2026?\" or \"Does [producer/vendor] provide crew lodging or travel support for out-of-market technicians?\"\n4. Do not ask about: Pay rates, specific hotel names, rooming lists, or private contact details.\n5. Re-submission: Verified data should be returned as a new research packet with lastVerified updated and sources labeled event-specific. ---\n\nSummary of Changes from Version 1.0\n\nChange Section Rationale\nAdded eventStatus 4, 10 Track cancelled/postponed/TBD events\nAdded eventDates (load-in, show, strike) 10 Essential for travel cost decisions\nAdded lastVerified 10 Freshness tracking\nAdded not_applicable status 4 Handle structurally irrelevant fields\nAdded \"Possible\" rubric 4.1 Reduce researcher inconsistency\nAdded evidenceLevel 5, 10 Separate producer patterns from event facts\nSplit site_ops_power into site_ops and power 5D More actionable vendor detail\nAdded other vendor department 5D Catch-all for non-standard vendors\nAdded advanced search operators 9 2026-specific results\nAdded unknownsList 10 Track gaps for human verification\nAdded Human Verification Protocol 13 Close process loop on unknown fields\nDocumented scoring methodology 8 Transparency for researchers\nAdded positive public-safe source definition 3 Clarify what is acceptable\n\n---\n\nReady to research an event or producer batch whenever you name one.",
        "c": [
          "c3",
          "c4",
          "c5",
          "c6",
          "c7"
        ]
      }
    ],
    [
      "a",
      "t6",
      {
        "txt": "Truncation check\nThe pasted text does not look truncated. It has a complete beginning, numbered sections, summary-of-changes table, and closes with:\nSo the paste appears complete. File mismatch\nThe uploaded DOCX appears to be the older handoff, not the revised v2.0 you pasted. The file version still says only “Current as of 2026-06-23,” not “Version 2.0,” and its Expected Deliverable only lists status values as confirmed, partial, possible, unlikely, or unknown—it does not include the newer not_applicable, eventStatus, eventDates, or lastVerified structure from your paste. The uploaded file’s output template also still uses the older shape with lodgingStatus, travelStatus, laborRouteStatus, vendorStackStatus, and site_ops_power; it does not include the revised eventStatus, eventDates, lastVerified, unknownsList, split site_ops / power, or evidenceLevel. So: your pasted v2.0 is newer than the uploaded file. The new evidenceLevel field is especially useful because it forces the researcher to say whether a source is:\nThat distinction matters. Remaining problems to fix before using it\n1. “Unchanged from original” cannot stay\nSections 7 and 8 say:\nThat breaks the document for an outside researcher with no prior context. Since this is supposed to be a standalone handoff, every section must be fully included. Do not reference an “original” document. Fix: paste the full Recommended Batch Order and Priority Event List directly into v2.0.\n2. “Paste into opportunities-2026.js” is too risky\nThis line is dangerous:\nAn outside researcher should not be told to paste directly into the app data file. Better wording:\nThis matters because the output block is not guaranteed to match the current app schema yet.\n3. eventDates may create false precision\nThis field:\nis valuable, but load-in and strike dates are often not public. It does not solve the hidden-data problem by itself.
