---
{
  "chunk_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Repo_Downloadable_Fil_2026-07-05_17-56-06.json__chunk-0001",
  "archive_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41",
  "archive_filename": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41.zip",
  "source_path": "ChatGPT_Production_Atlas_-_Repo_Downloadable_Fil_2026-07-05_17-56-06.json",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 10225,
  "source_sha256": "0ea64f217091c21813a0fbc8fcc61ed46a6825639f78402c337053a73bb8c11a",
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
      "I’ll do this as a repo audit-and-patch pass on research-version: inventory archive findings, compare them to app data/package files, apply safe public-data updates, then leave a collaboration log. I’ll keep changes constrained to the current static app boundary and run validation where the environment allows it."
    ],
    [
      "a",
      "t2",
      "Direct git clone is blocked in this runtime because DNS cannot resolve GitHub, so I’m using the connected GitHub API for file reads/writes and web verification for current public dates/URLs."
    ],
    [
      "a",
      "t3",
      "I found concrete archive-backed items that are safe to apply: Welcome to Rockville and Beyond Wonderland have public 2027 dates now, Stagecoach has rolled to 2027 sale/planning but no exact dates in fetched text, and prior audit recommended canonical source URL fixes. Next I’m checking employer-route data before patching."
    ],
    [
      "u",
      "t4",
      "I want and need you to update research for any festival between January 1st and now. Those festivals have rolled into the 2027 year and do not require 2026 information encoded to them."
    ],
    [
      "a",
      "t5",
      "I’m changing scope: any festival record dated January 1 through June 28, 2026 should no longer be treated as a current 2026 opportunity. I’ll update those to 2027 where public 2027 dates are available; where not available, I’ll remove them from the active view or mark them for 2027 verification instead of preserving stale 2026 scheduling data."
    ],
    [
      "a",
      "t6",
      "I’m treating records whose 2026 event window starts before or on June 28, 2026 as stale for the active planning layer unless a 2027 public record is available. Records later than today stay 2026."
    ],
    [
      "a",
      "t7",
      "I created the rollover override package. Now I’m wiring it into the public pages after existing route updates and before atlas-core-v2.js, so the runtime reads the rolled-forward dates before rendering cards, calendar, map, sources, and modals."
    ],
    [
      "a",
      "t8",
      {
        "txt": "Implemented a first pass on research-version. The rollover file currently handles verified 2027 records for:\nRecord2027 updatecoachella-2026Apr 9–18, 2027ultra-miami-2026Mar 26–28, 2027edc-las-vegas-2026May 14–23, 2027, two-weekend public cyclewelcome-to-rockville-2026May 6–9, 2027beyond-wonderland-socal-2026Mar 26–27, 2027bottlerock-napa-2026May 28–30, 2027\nI verified the key public rollover sources while patching: Welcome to Rockville’s official page shows May 6–9, 2027 at Daytona International Speedway; Beyond SoCal’s official page shows March 26–27, 2027; Ultra’s official page shows March 26–28, 2027; EDC Las Vegas’s official page shows May 14–16 and May 21–23, 2027; BottleRock public reporting says May 28–30, 2027; and Coachella public reporting says Apr 9–11 and Apr 16–18, 2027. Rockville 2027 Beyond Wonderland SoCal 2026 Ultra Music Festival EDC Las Vegas 2027 San Francisco Chronicle Pitchfork\nFiles changed\nThe repo now shows these changed files compared with the pre-work commit 4142bb481171bf385f70ea6872b609167e00e945:\nThe compare result shows research-version is now 11 commits ahead of the starting commit, with those six files changed. Important caveat\nI could not run local validation because this runtime could not use a normal local GitHub checkout. Run locally:\nOne risk to review\nI had to simplify data/packages/opportunity-taxonomy.js into a compatibility loader that pulls in the rollover package. It keeps the expected hook names and marker strings, but it should be browser-tested. Jan–June 2026 records without verified 2027 dates no longer appear as active planning targets.\nsources.html still works.",
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
      "t9",
      "Ok. Continue auditing the archive data and creating whatever new data pathways complete the data retrieval for my web app"
    ],
    [
      "a",
      "t10",
      "I’ll continue from the current research-version state. First I’ll stabilize the rollover pathway I added, then I’ll audit archive reports for concrete app-usable findings and convert the safe ones into data packages rather than leaving them stranded in markdown."
    ],
    [
      "a",
      "t11",
      "I confirmed approx-date-labels.js already loads opportunity-taxonomy.js and calls applyOpportunityTaxonomy() on page events. That means the rollover package can be treated as a shared data pathway even on pages where the HTML was not directly edited."
    ],
    [
      "a",
      "t12",
      "The backlog confirms the per-market split work is already partly encoded, but it also exposes more rollover targets I missed in the first pass: crssd-2026 and sick-new-world-2026 are January–June records and should not stay active as 2026 planning targets. I’m patching that now."
    ],
    [
      "a",
      "t13",
      {
        "txt": "Fixed missed rollover targets\nI patched data/packages/opportunity-rollover-2027.js to include two early-year records I missed in the first pass:\nThose now follow the same rule: if no verified 2027 public date/source is encoded yet, they are hidden from active planning until verified.\n2. Added employer-source retrieval to sources.html\nCreated:\nThis adds a new Employer route sources section to sources.html, pulling from:\nIt surfaces public employer links for:\nIt respects the existing filters where relevant:\nThis closes a real retrieval gap: the Sources page previously showed opportunity and branch source records, but not the employer/careers/contact routes that are central to the app’s purpose.\n3. Current changed files\nCompared to the starting commit, research-version now includes changes to:\nStill required locally\nI still could not run repo validation from this connector-only environment. Verified rollover records show their 2027 dates.",
        "c": [
          "c7",
          "c8",
          "c9",
          "c10",
          "c11",
          "c12",
          "c13",
          "c14",
          "c15",
          "c16",
          "c17",
          "c18",
          "c19",
          "c20"
        ]
      }
    ]
  ],
  "t": {
    "t1": "2026-07-05T21:56:06.783Z",
    "t2": "2026-07-05T21:56:06.783Z",
    "t3": "2026-07-05T21:56:06.784Z",
    "t4": "2026-07-05T21:56:06.784Z",
    "t5": "2026-07-05T21:56:06.784Z",
    "t6": "2026-07-05T21:56:06.784Z",
    "t7": "2026-07-05T21:56:06.784Z",
    "t8": "2026-07-05T21:56:06.784Z",
    "t9": "2026-07-05T21:56:06.790Z",
    "t10": "2026-07-05T21:56:06.790Z",
    "t11": "2026-07-05T21:56:06.790Z",
    "t12": "2026-07-05T21:56:06.791Z",
    "t13": "2026-07-05T21:56:06.791Z"
  },
  "c": {
    "c1": [
      "text",
      "data/packages/opportunity-rollover-2027.js"
    ],
    "c2": [
      "text",
      "data/packages/opportunity-rollover-2027.js"
    ],
    "c3": [
      "text",
      "ai-communication/collaboration-log/2026-06-28-002-chatgpt-2027-rollover-audit.md\ncalendar.html\ndata/packages/opportunity-rollover-2027.js\ndata/packages/opportunity-taxonomy.js\nindex.html\nopportunities.html"
    ],
    "c4": [
      "text",
      "ai-communication/collaboration-log/2026-06-28-002-chatgpt-2027-rollover-audit.md\ncalendar.html\ndata/packages/opportunity-rollover-2027.js\ndata/packages/opportunity-taxonomy.js\nindex.html\nopportunities.html"
    ],
    "c5": [
      "text",
      "npm run validate:branch-research\nnpm run validate:static-app\nnpm run validate:all"
    ],
    "c6": [
      "text",
      "npm run validate:branch-research\nnpm run validate:static-app\nnpm run validate:all"
    ],
    "c7": [
      "text",
      "Apply / careers\nCareers\nContact\nHomepage\nDirectory"
    ],
    "c8": [
      "text",
      "Apply / careers\nCareers\nContact\nHomepage\nDirectory"
    ],
    "c9": [
      "search",
      "Department\nRegion\nEmployer type"
    ],
    "c10": [
      "search",
      "Department\nRegion\nEmployer type"
    ],
    "c11": [
      "text",
      "data/packages/opportunity-rollover-2027.js\nassets/sources-employer-links.js"
    ],
    "c12": [
      "text",
      "data/packages/opportunity-rollover-2027.js\nassets/sources-employer-links.js"
    ],
    "c13": [
      "text",
      "ai-communication/collaboration-log/2026-06-28-002-chatgpt-2027-rollover-audit.md"
    ],
    "c14": [
      "text",
      "ai-communication/collaboration-log/2026-06-28-002-chatgpt-2027-rollover-audit.md"
    ],
    "c15": [
      "text",
      "ai-communication/collaboration-log/2026-06-28-002-chatgpt-2027-rollover-audit.md\nassets/sources-employer-links.js\ncalendar.html\ndata/packages/opportunity-rollover-2027.js\ndata/packages/opportunity-taxonomy.js\nindex.html\nopportunities.html\nsources.html"
    ],
    "c16": [
      "text",
      "ai-communication/collaboration-log/2026-06-28-002-chatgpt-2027-rollover-audit.md\nassets/sources-employer-links.js\ncalendar.html\ndata/packages/opportunity-rollover-2027.js\ndata/packages/opportunity-taxonomy.js\nindex.html\nopportunities.html\nsources.html"
    ],
    "c17": [
      "text",
      "npm run validate:branch-research\nnpm run validate:static-app\nnpm run validate:all"
    ],
    "c18": [
      "text",
      "npm run validate:branch-research\nnpm run validate:static-app\nnpm run validate:all"
    ],
    "c19": [
      "home",
      "Opportunities\nCalendar\nSources\nMap"
    ],
    "c20": [
      "home",
      "Opportunities\nCalendar\nSources\nMap"
    ]
  },
  "tokenStats": {
    "rawChatTokens": 1591,
    "compressedTokens": 1329,
    "reductionPercent": 16,
    "note": "Reduced from ~1,591 to ~1,329 tokens (16% reduction)"
  },
  "chatTitle": "Production Atlas - Repo Downloadable File",
  "_context": "=== LLM MEMORY EXPORT ===\nSource: chatgpt | 13 messages\nExported: 2026-07-05\n\nINSTRUCTIONS FOR AI: This file contains a compressed export of a prior\nconversation. Please read the notes and context below, then resume\nnaturally as if continuing from where we left off.\n\n--- CONVERSATION FOLLOWS ---"
}
