---
{
  "chunk_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Repo_Downloadable_Fil_2026-07-05_17-56-06-4-.json__chunk-0003",
  "archive_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41",
  "archive_filename": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41.zip",
  "source_path": "ChatGPT_Production_Atlas_-_Repo_Downloadable_Fil_2026-07-05_17-56-06 (4).json",
  "chunk_index": 3,
  "chunk_count_for_source": 4,
  "char_start": 20477,
  "char_end": 32476,
  "source_sha256": "e5be644cabf4cbf2a98271b7dbccb22c5a7bc6e0b499720d5f7cbaaeb5007daa",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

e: '<source URL or unknown>' },\n  { department: 'site_ops', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' },\n  { department: 'power', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' },\n  { department: 'other', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' }\n],\nvendorSources: [\n  { label: '<source label>', url: '<source URL>', evidenceLevel: 'event-specific|producer-pattern|industry-standard' }\n]"
    ],
    "c7": [
      "javascript",
      "{\n  id: '<event-id>',\n  eventStatus: 'confirmed|postponed|cancelled|tbd',\n  eventDates: { loadInStart: 'YYYY-MM-DD', showDates: 'YYYY-MM-DD to YYYY-MM-DD', strikeEnd: 'YYYY-MM-DD', totalDaysOnSite: <number> },\n  lastVerified: 'YYYY-MM-DD',\n  lodgingStatus: 'confirmed|possible|unknown|unlikely|not_applicable',\n  lodgingNotes: '<public-safe summary>',\n  lodgingSources: [\n    { label: '<source label>', url: '<source URL>', evidenceLevel: 'event-specific|producer-pattern|industry-standard' }\n  ],\n  travelStatus: 'confirmed|possible|unknown|unlikely|not_applicable',\n  travelNotes: '<public-safe summary>',\n  travelSources: [\n    { label: '<source label>', url: '<source URL>', evidenceLevel: 'event-specific|producer-pattern|industry-standard' }\n  ],\n  laborRouteStatus: 'confirmed|possible|unknown',\n  laborRouteNotes: '<public-safe summary>',\n  iatseJurisdictionNote: 'verify applicable IATSE/local jurisdiction for <city or site> (research local number before outreach)',\n  nonUnionRouteNotes: '<public-safe non-union route notes or unknown publicly>',\n  laborSources: [\n    { label: '<source label>', url: '<source URL>', evidenceLevel: 'event-specific|producer-pattern|industry-standard' }\n  ],\n  vendorStackStatus: 'confirmed|partial|unknown',\n  vendorStackNotes: '<public-safe summary>',\n  vendors: [\n    { department: 'audio', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' },\n    { department: 'lighting', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' },\n    { department: 'video_led', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' },\n    { department: 'staging', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' },\n    { department: 'rigging', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' },\n    { department: 'site_ops', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' },\n    { department: 'power', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' },\n    { department: 'other', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' }\n  ],\n  vendorSources: [\n    { label: '<source label>', url: '<source URL>', evidenceLevel: 'event-specific|producer-pattern|industry-standard' }\n  ],\n  unknownsList: [\n    '<what still needs human verification>'\n  ],\n  publicSafetyNotes: 'No private contacts, pay rates, lodging details, or rumor-only claims included.'\n}"
    ],
    "c8": [
      "text",
      "Ready to research an event or producer batch whenever you name one."
    ],
    "c9": [
      "text",
      "Ready to research an event or producer batch whenever you name one."
    ],
    "c10": [
      "eventstatus",
      "eventDates\nlastVerified\nnot_applicable\npossible-decision rubric\nevidenceLevel\nunknownsList\nhuman verification protocol\nscoring methodology"
    ],
    "c11": [
      "eventstatus",
      "eventDates\nlastVerified\nnot_applicable\npossible-decision rubric\nevidenceLevel\nunknownsList\nhuman verification protocol\nscoring methodology"
    ],
    "c12": [
      "event-specific",
      "producer-pattern\nindustry-standard"
    ],
    "c13": [
      "event-specific",
      "producer-pattern\nindustry-standard"
    ],
    "c14": [
      "text",
      "(Unchanged from original — see original Section 7)\n(Unchanged from original — see original Section 8)"
    ],
    "c15": [
      "text",
      "(Unchanged from original — see original Section 7)\n(Unchanged from original — see original Section 8)"
    ],
    "c16": [
      "text",
      "Copy this exactly. Paste into data/packages/opportunities-2026.js and run npm run validate:all before pushing."
    ],
    "c17": [
      "text",
      "Copy this exactly. Paste into data/packages/opportunities-2026.js and run npm run validate:all before pushing."
    ],
    "c18": [
      "text",
      "Return this as a data-ready research block. Do not edit the repository directly unless explicitly assigned. The database maintainer will review, sanitize, convert, and apply the update."
    ],
    "c19": [
      "text",
      "Return this as a data-ready research block. Do not edit the repository directly unless explicitly assigned. The database maintainer will review, sanitize, convert, and apply the update."
    ],
    "c20": [
      "text",
      "eventDates: {\n  loadInStart,\n  showDates,\n  strikeEnd,\n  totalDaysOnSite\n}"
    ],
    "c21": [
      "text",
      "eventDates: {\n  loadInStart,\n  showDates,\n  strikeEnd,\n  totalDaysOnSite\n}"
    ],
    "c22": [
      "text",
      "eventDates: {\n  loadInStart: 'unknown',\n  showDates: 'YYYY-MM-DD to YYYY-MM-DD',\n  strikeEnd: 'unknown',\n  totalDaysOnSite: 'unknown'\n}"
    ],
    "c23": [
      "text",
      "eventDates: {\n  loadInStart: 'unknown',\n  showDates: 'YYYY-MM-DD to YYYY-MM-DD',\n  strikeEnd: 'unknown',\n  totalDaysOnSite: 'unknown'\n}"
    ],
    "c24": [
      "text",
      "Do not infer load-in or strike dates unless publicly confirmed. If only show dates are public, leave loadInStart and strikeEnd as unknown."
    ],
    "c25": [
      "text",
      "Do not infer load-in or strike dates unless publicly confirmed. If only show dates are public, leave loadInStart and strikeEnd as unknown."
    ],
    "c26": [
      "text",
      "not_applicable when the event structure makes the question irrelevant, e.g., single-day urban event with no overnight crew"
    ],
    "c27": [
      "text",
      "not_applicable when the event structure makes the question irrelevant, e.g., single-day urban event with no overnight crew"
    ],
    "c28": [
      "text",
      "Use not_applicable only when the field truly does not apply to the event type or record type. Do not use not_applicable simply because lodging or travel seems unlikely."
    ],
    "c29": [
      "text",
      "Use not_applicable only when the field truly does not apply to the event type or record type. Do not use not_applicable simply because lodging or travel seems unlikely."
    ],
    "c30": [
      "text",
      "Industry standard: major multi-day camping festivals typically provide production camping."
    ],
    "c31": [
      "text",
      "Industry standard: major multi-day camping festivals typically provide production camping."
    ],
    "c32": [
      "text",
      "Industry-standard evidence can support a possible label only when combined with event structure, venue conditions, or producer/vendor evidence. It cannot alone confirm a claim."
    ],
    "c33": [
      "text",
      "Industry-standard evidence can support a possible label only when combined with event structure, venue conditions, or producer/vendor evidence. It cannot alone confirm a claim."
    ],
    "c34": [
      "text",
      "Contact the producer's public careers email..."
    ],
    "c35": [
      "text",
      "Contact the producer's public careers email..."
    ],
    "c36": [
      "text",
      "The outside researcher should not contact producers, venues, vendors, or unions unless explicitly instructed. Instead, list the public channel that the maintainer could use for verification."
    ],
    "c37": [
      "text",
      "The outside researcher should not contact producers, venues, vendors, or unions unless explicitly instructed. Instead, list the public channel that the maintainer could use for verification."
    ],
    "c38": [
      "dates",
      "event status\npublic producer route\npublic vendor credits\npublic IATSE/local verification language\nofficial source URLs"
    ],
    "c39": [
      "dates",
      "event status\npublic producer route\npublic vendor credits\npublic IATSE/local verification language\nofficial source URLs"
    ],
    "c40": [
      "text",
      "who actually hires\ncrew camping realities\ntravel/per diem realities\nvendor labor practices\ndispatch routes"
    ],
    "c41": [
      "text",
      "who actually hires\ncrew camping realities\ntravel/per diem realities\nvendor labor practices\ndispatch routes"
    ],
    "c42": [
      "text",
      "1. Replace “unchanged from original” placeholders with full content.\n2. Remove direct “paste into opportunities-2026.js” instruction.\n3. Allow unknown load-in/strike dates.\n4. Tighten not_applicable rules.\n5. Tighten industry-standard possible rules.\n6. Clarify outside researchers should not perform outreach unless explicitly instructed.\n7. Add a note that hidden human intelligence belongs in Airtable intake, not public research output."
    ],
    "c43": [
      "text",
      "1. Replace “unchanged from original” placeholders with full content.\n2. Remove direct “paste into opportunities-2026.js” instruction.\n3. Allow unknown load-in/strike dates.\n4. Tighten not_applicable rules.\n5. Tighten industry-standard possible rules.\n6. Clarify outside researchers should not perform outreach unless explicitly instructed.\n7. Add a note that hidden human intelligence belongs in Airtable intake, not public research output."
    ],
    "c44": [
      "text",
      "research/notebooklm-public-research/012-bonnaroo-vendor-stack-evidence-map.md"
    ],
    "c45": [
      "text",
      "research/notebooklm-public-research/012-bonnaroo-vendor-stack-evidence-map.md"
    ],
    "c46": [
      "text",
      "2be802cd3b8ad32ae0f8b17c6e1cdc435321aed1\nCapture Bonnaroo vendor stack evidence map"
    ],
    "c47": [
      "text",
      "2be802cd3b8ad32ae0f8b17c6e1cdc435321aed1\nCapture Bonnaroo vendor stack evidence map"
    ],
    "c48": [
      "text",
      "research/notebooklm-public-research/013-dwp-producer-event-pattern-evidence-map.md"
    ],
    "c49": [
      "text",
      "research/notebooklm-public-research/013-dwp-producer-event-pattern-evidence-map.md"
    ],
    "c50": [
      "text",
      "1baa664699e895e2d00cac15430d6afccfca36cf\nCapture DWP producer event pattern evidence map"
    ],
    "c51": [
      "text",
      "1baa664699e895e2d00cac15430d6afccfca36cf\nCapture DWP producer event pattern evidence map"
    ],
    "c52": [
      "text",
      "research/notebooklm-public-research/014-louder-than-life-event-evidence-map.md"
    ],
    "c53": [
      "text",
      "research/notebooklm-public-research/014-louder-than-life-event-evidence-map.md"
    ],
    "c54": [
      "text",
      "766e58035917ea2176da3df478acac63582e7df6\nCapture Louder Than Life event evidence map"
    ],
    "c55": [
      "text",
      "766e58035917ea2176da3df478acac63582e7df6\nCapture Louder Than Life event evidence map"
    ],
    "c56": [
      "text",
      "ai-communication/collaboration-log/2026-06-24-019-chatgpt-bonnaroo-dwp-ltl-evidence-maps.md"
    ],
    "c57": [
      "text",
      "ai-communication/collaboration-log/2026-06-24-019-chatgpt-bonnaroo-dwp-ltl-evidence-maps.md"
    ],
    "c58": [
      "text",
      "6bacde467ad0b7581b94873559e5a719d7e06338\nAdd Bonnaroo DWP LTL evidence map log"
    ],
    "c59": [
      "text",
      "6bacde467ad0b7581b94873559e5a719d7e06338\nAdd Bonnaroo DWP LTL evidence map log"
    ],
    "c60": [
      "text",
      "ai-communication/2026-06-24-chatgpt-to-claude-notebooklm-research-handoff.md"
    ],
    "c61": [
