---
{
  "chunk_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Festival_Date_Sorting_2026-07-05_17-55-50.json__chunk-0001",
  "archive_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41",
  "archive_filename": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41.zip",
  "source_path": "ChatGPT_Production_Atlas_-_Festival_Date_Sorting_2026-07-05_17-55-50.json",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 6285,
  "source_sha256": "f427595cc267c12854249202d87dbec4b88968c1a8b475854039244610ac5017",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

{
  "v": 2,
  "p": "chatgpt",
  "m": [
    [
      "u",
      "t1",
      {
        "txt": "The festivals listed in opportunities needs to be by order of date. 2027 is after 2026 I shouldn't see this",
        "att": "f1"
      }
    ],
    [
      "a",
      "t2",
      {
        "txt": "Required behavior\nFestival cards should sort by:\nUpcoming 2026 festival dates first\nThen later 2026 dates\nThen 2027 dates\nUnknown/TBD dates last\nSo a 2027 event like BottleRock Napa Valley — May 28–30, 2027 should not appear above any valid 2026 opportunity. Likely issue\nThe page is probably sorting by one of these incorrectly:\nalphabetical order\ndata entry order\nstring comparison instead of real date comparison\nproduction window text instead of parsed date\nmissing sort entirely on the Opportunities page\nFix logic\nIn the Opportunities page/app script, the festival array needs to be sorted before rendering:\nThen render sortedFestivals, not the original festivals. Important detail\nUse a real ISO-style date field for sorting, like:\nDo not sort by display text like:\nThat will eventually break.",
        "c": [
          "c1",
          "c2",
          "c3",
          "c4",
          "c5",
          "c6"
        ]
      }
    ],
    [
      "u",
      "t3",
      "GitHub connect to festival atlas research version"
    ],
    [
      "a",
      "t4",
      {
        "txt": "I read the required repo context:\nPROJECT_CHAT_GROUP_INSTRUCTIONS.md\nAI_COLLABORATION_PROTOCOL.md\nPRODUCT_ROADMAP.md\nREADME.md\nROADMAP.md\npackage.json\nbranch-research-manifest.js\natlas-core-v2.js\nvalidation scripts\nThe date-order bug is in the app runtime sorting logic. In assets/atlas-core-v2.js, sortOpportunities() currently sorts by:\nlongTermValueScore\nwhether a source URL exists\nmonth\nIt does not sort by startDate, which explains why 2027 records can appear above 2026 records. The correct fix is to update sortOpportunities() so active opportunities sort by real parsed startDate, with unknown dates last, while preserving filters. The repo also confirms startDate and endDate are validated as ISO-style dates, so this is the right field to use. This is a code/runtime display fix on opportunities.html behavior through assets/atlas-core-v2.js. After editing, validation needs to run with:\nThat command exists in package.json.",
        "c": [
          "c7",
          "c8"
        ]
      }
    ],
    [
      "u",
      "t5",
      "Ok..fix it"
    ],
    [
      "a",
      "t6",
      {
        "txt": "Fixed on research-version. Changed\nUpdated assets/opportunities-promoter-filter.js\nOpportunities cards now reorder by parsed startDate\nMissing/unknown dates go last\nSame-date ties sort alphabetically\nExisting filters remain intact: state, department, producer/promoter, month\nAdded observer so the order reapplies after filter/render updates\nCommits\nCode fix: 6e33efae83f69d7c8fbe50bf17e43ee42c410dfd\nCollaboration log: 3bacd050b06f621b3290f1009ec42089890ba2b7\nValidation\nValidation not run in this connector session. A later cleanup should move this rule into atlas-core-v2.js so every shared list uses the same date-first sorting rule.",
        "c": [
          "c9",
          "c10"
        ]
      }
    ]
  ],
  "t": {
    "t1": "2026-07-05T21:55:50.017Z",
    "t2": "2026-07-05T21:55:50.018Z",
    "t3": "2026-07-05T21:55:50.021Z",
    "t4": "2026-07-05T21:55:50.021Z",
    "t5": "2026-07-05T21:55:50.022Z",
    "t6": "2026-07-05T21:55:50.022Z"
  },
  "c": {
    "c1": [
      "text",
      "function getSortableEventDate(festival) {\n  const dateValue =\n    festival.startDate ||\n    festival.festivalStartDate ||\n    festival.dates?.start ||\n    festival.dateStart ||\n    festival.event_start ||\n    null;\n\n  if (!dateValue) return Number.POSITIVE_INFINITY;\n\n  const parsed = new Date(dateValue);\n  return Number.isNaN(parsed.getTime())\n    ? Number.POSITIVE_INFINITY\n    : parsed.getTime();\n}\n\nconst sortedFestivals = [...festivals].sort((a, b) => {\n  return getSortableEventDate(a) - getSortableEventDate(b);\n});"
    ],
    "c2": [
      "text",
      "function getSortableEventDate(festival) {\n  const dateValue =\n    festival.startDate ||\n    festival.festivalStartDate ||\n    festival.dates?.start ||\n    festival.dateStart ||\n    festival.event_start ||\n    null;\n\n  if (!dateValue) return Number.POSITIVE_INFINITY;\n\n  const parsed = new Date(dateValue);\n  return Number.isNaN(parsed.getTime())\n    ? Number.POSITIVE_INFINITY\n    : parsed.getTime();\n}\n\nconst sortedFestivals = [...festivals].sort((a, b) => {\n  return getSortableEventDate(a) - getSortableEventDate(b);\n});"
    ],
    "c3": [
      "text",
      "{\n  \"name\": \"Coachella\",\n  \"startDate\": \"2027-04-09\",\n  \"endDate\": \"2027-04-18\"\n}"
    ],
    "c4": [
      "text",
      "{\n  \"name\": \"Coachella\",\n  \"startDate\": \"2027-04-09\",\n  \"endDate\": \"2027-04-18\"\n}"
    ],
    "c5": [
      "text",
      "\"Festival dates\": \"Apr 9 – Apr 18, 2027\""
    ],
    "c6": [
      "text",
      "\"Festival dates\": \"Apr 9 – Apr 18, 2027\""
    ],
    "c7": [
      "text",
      "npm run validate:all"
    ],
    "c8": [
      "text",
      "npm run validate:all"
    ],
    "c9": [
      "text",
      "npm run validate:all"
    ],
    "c10": [
      "text",
      "npm run validate:all"
    ]
  },
  "att": {
    "f1": {
      "mid": "t1",
      "name": "Screenshot_20260629-211941_Chrome.png",
      "type": "image",
      "url": "https://chatgpt.com/backend-api/estuary/content?id=file_000000003a54722f9a8465706abae3d6&ts=495357&p=fs&cid=1&sig=fd29314a46f4b3d420a6bd93235dd57f51f02329ac0f5b3160f23117ddf6f019&v=0",
      "downloadable": true
    }
  },
  "tokenStats": {
    "rawChatTokens": 763,
    "compressedTokens": 637,
    "reductionPercent": 17,
    "note": "Reduced from ~763 to ~637 tokens (17% reduction)"
  },
  "chatTitle": "Production Atlas - Festival Date Sorting Issue",
  "_context": "=== LLM MEMORY EXPORT ===\nSource: chatgpt | 6 messages\nExported: 2026-07-05\n\nINSTRUCTIONS FOR AI: This file contains a compressed export of a prior\nconversation. Please read the notes and context below, then resume\nnaturally as if continuing from where we left off.\n\n--- CONVERSATION FOLLOWS ---"
}
