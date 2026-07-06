---
{
  "chunk_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Project_Instructions__2026-07-05_17-57-23.json__chunk-0002",
  "archive_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41",
  "archive_filename": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41.zip",
  "source_path": "ChatGPT_Production_Atlas_-_Project_Instructions__2026-07-05_17-57-23.json",
  "chunk_index": 2,
  "chunk_count_for_source": 3,
  "char_start": 11339,
  "char_end": 23331,
  "source_sha256": "73b29cfad59ef10e48ddc5c875381740c1af32a67aa4ba6631e4e155ab58f52c",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

",
          "c20",
          "c21",
          "c22",
          "c23",
          "c24",
          "c25",
          "c26",
          "c27",
          "c28",
          "c29",
          "c30",
          "c31",
          "c32"
        ]
      }
    ],
    [
      "u",
      "t19",
      "Search the other repository branches for the files Claude was supposed to make. Fix the validator drift and pages issue."
    ],
    [
      "a",
      "t20",
      "I’ll search across likely Claude/head branches for the missing ai-communication files first, then patch the validator/page drift on research-version. After the edit I’ll leave a handoff documenting what I found and what still needs validation."
    ],
    [
      "a",
      "t21",
      "PR #1 is now closed and unmerged. Its head branch is claude/research-version-edits-z0gqw6, so I’ll inspect that branch for the missing handoff files before changing research-version."
    ],
    [
      "a",
      "t22",
      "The page files themselves exist and load the expected shared runtime/helper files. The drift is specifically in the validator’s requiredPages list, not missing page files."
    ],
    [
      "u",
      "t23",
      "Continue"
    ],
    [
      "a",
      "t24",
      "Continuing. I need to verify whether the validator patch landed or whether the interrupted update failed, then I’ll complete the patch and add the handoff cleanly."
    ],
    [
      "a",
      "t25",
      "Validator drift is patched on research-version in commit 45c57f6: map.html and schedule.html are now in requiredPages. Next I’m adding the handoff note with the branch-search result and validation caveat."
    ],
    [
      "a",
      "t26",
      "The handoff is committed on research-version in 994fe06. I’m doing a quick verification fetch now so the final answer can cite the actual updated files."
    ],
    [
      "a",
      "t27",
      {
        "txt": "Branch search result\nI checked the known Claude PR branch:\nPR #1 is now:\nThe expected Claude handoff/source-cleanup files were not found on either research-version or claude/research-version-edits-z0gqw6:\nThe current handoff records that as a repo-visible gap. Validator drift fixed\nPatched:\nThe validator now includes:\nin requiredPages. Commit:\nHandoff added\nCreated:\nCommit:\nThe handoff documents:\nbranch/PR findings\nmissing expected Claude handoff files\nvalidator fix\nsource URL cleanup status\nnext required validation\nwhat not to do next\nValidation status\nValidation not run from here because this was a GitHub connector edit, not a local Node execution environment. Next command to run locally or in Claude Code:\nThen resume the source URL pass in small batches against:",
        "c": [
          "c33",
          "c34",
          "c35",
          "c36",
          "c37",
          "c38",
          "c39",
          "c40",
          "c41",
          "c42",
          "c43",
          "c44"
        ]
      }
    ]
  ],
  "t": {
    "t1": "2026-07-05T21:57:23.204Z",
    "t2": "2026-07-05T21:57:23.205Z",
    "t3": "2026-07-05T21:57:23.205Z",
    "t4": "2026-07-05T21:57:23.205Z",
    "t5": "2026-07-05T21:57:23.205Z",
    "t6": "2026-07-05T21:57:23.205Z",
    "t7": "2026-07-05T21:57:23.205Z",
    "t8": "2026-07-05T21:57:23.207Z",
    "t9": "2026-07-05T21:57:23.207Z",
    "t10": "2026-07-05T21:57:23.207Z",
    "t11": "2026-07-05T21:57:23.207Z",
    "t12": "2026-07-05T21:57:23.208Z",
    "t13": "2026-07-05T21:57:23.208Z",
    "t14": "2026-07-05T21:57:23.209Z",
    "t15": "2026-07-05T21:57:23.209Z",
    "t16": "2026-07-05T21:57:23.209Z",
    "t17": "2026-07-05T21:57:23.213Z",
    "t18": "2026-07-05T21:57:23.213Z",
    "t19": "2026-07-05T21:57:23.217Z",
    "t20": "2026-07-05T21:57:23.217Z",
    "t21": "2026-07-05T21:57:23.217Z",
    "t22": "2026-07-05T21:57:23.217Z",
    "t23": "2026-07-05T21:57:23.217Z",
    "t24": "2026-07-05T21:57:23.217Z",
    "t25": "2026-07-05T21:57:23.217Z",
    "t26": "2026-07-05T21:57:23.217Z",
    "t27": "2026-07-05T21:57:23.217Z"
  },
  "c": {
    "c1": [
      "index.html",
      "calendar.html\nopportunities.html\nbranches.html\nemployers.html\niatse.html\nmatrix.html\nanalytics.html\nsources.html\nguide.html\nmap.html\nschedule.html"
    ],
    "c2": [
      "index.html",
      "calendar.html\nopportunities.html\nbranches.html\nemployers.html\niatse.html\nmatrix.html\nanalytics.html\nsources.html\nguide.html\nmap.html\nschedule.html"
    ],
    "c3": [
      "text",
      "ai-communication/2026-06-22-claude-stage-1-update.md\nai-communication/2026-06-22-claude-stage-2-update.md\nai-communication/2026-06-22-claude-stage-3-update.md\nai-communication/2026-06-22-claude-stage-4-update.md"
    ],
    "c4": [
      "text",
      "ai-communication/2026-06-22-claude-stage-1-update.md\nai-communication/2026-06-22-claude-stage-2-update.md\nai-communication/2026-06-22-claude-stage-3-update.md\nai-communication/2026-06-22-claude-stage-4-update.md"
    ],
    "c5": [
      "text",
      "const requiredPages = [\n  'index.html',\n  'calendar.html',\n  'opportunities.html',\n  'branches.html',\n  'employers.html',\n  'iatse.html',\n  'matrix.html',\n  'analytics.html',\n  'sources.html',\n  'guide.html'\n];"
    ],
    "c6": [
      "text",
      "const requiredPages = [\n  'index.html',\n  'calendar.html',\n  'opportunities.html',\n  'branches.html',\n  'employers.html',\n  'iatse.html',\n  'matrix.html',\n  'analytics.html',\n  'sources.html',\n  'guide.html'\n];"
    ],
    "c7": [
      "text",
      "ai-communication/2026-06-22-chatgpt-data-cleanup-catchup.md"
    ],
    "c8": [
      "text",
      "ai-communication/2026-06-22-chatgpt-data-cleanup-catchup.md"
    ],
    "c9": [
      "text",
      "npm run validate:all"
    ],
    "c10": [
      "text",
      "npm run validate:all"
    ],
    "c11": [
      "text",
      "npm run validate:branch-research\nnpm run validate:static-app\nnpm run validate:all"
    ],
    "c12": [
      "text",
      "npm run validate:branch-research\nnpm run validate:static-app\nnpm run validate:all"
    ],
    "c13": [
      "text",
      "ai-communication/2026-06-22-source-url-cleanup-status.md"
    ],
    "c14": [
      "text",
      "ai-communication/2026-06-22-source-url-cleanup-status.md"
    ],
    "c15": [
      "text",
      "Current phase: source URL gathering / source verification\nClaude stopped due to usage limits\nKnown completed records: unknown unless Claude documented them elsewhere\nNext assistant should inspect current data files before editing\nDo not duplicate source work blindly\nDo not add private/unofficial contact data\nKeep source links centralized through existing source mechanisms"
    ],
    "c16": [
      "text",
      "Current phase: source URL gathering / source verification\nClaude stopped due to usage limits\nKnown completed records: unknown unless Claude documented them elsewhere\nNext assistant should inspect current data files before editing\nDo not duplicate source work blindly\nDo not add private/unofficial contact data\nKeep source links centralized through existing source mechanisms"
    ],
    "c17": [
      "text",
      "5–10 opportunities at a time"
    ],
    "c18": [
      "text",
      "5–10 opportunities at a time"
    ],
    "c19": [
      "active2026sourceurl",
      "producer.name\nproducer.status\nactive2026Status\nstartDate\nendDate\nvenue\nnextResearchActions\nsourceQuality"
    ],
    "c20": [
      "active2026sourceurl",
      "producer.name\nproducer.status\nactive2026Status\nstartDate\nendDate\nvenue\nnextResearchActions\nsourceQuality"
    ],
    "c21": [
      "text",
      "official festival site\nofficial ticket page\nofficial venue/event page\nofficial promoter page\nmajor public announcement\nWikipedia only as fallback/secondary context"
    ],
    "c22": [
      "text",
      "official festival site\nofficial ticket page\nofficial venue/event page\nofficial promoter page\nmajor public announcement\nWikipedia only as fallback/secondary context"
    ],
    "c23": [
      "text",
      "ai-communication/2026-06-22-source-url-backlog.md"
    ],
    "c24": [
      "text",
      "ai-communication/2026-06-22-source-url-backlog.md"
    ],
    "c25": [
      "text",
      "## Needs Official 2026 Source\n- opportunity id\n- current name\n- missing field\n- attempted source terms\n- next search suggestion\n\n## Has Source But Needs Better Source\n- opportunity id\n- current source\n- issue\n\n## Needs Date Verification\n- opportunity id\n- current date/month\n- issue\n\n## Needs Venue Verification\n- opportunity id\n- current venue\n- issue"
    ],
    "c26": [
      "text",
      "## Needs Official 2026 Source\n- opportunity id\n- current name\n- missing field\n- attempted source terms\n- next search suggestion\n\n## Has Source But Needs Better Source\n- opportunity id\n- current source\n- issue\n\n## Needs Date Verification\n- opportunity id\n- current date/month\n- issue\n\n## Needs Venue Verification\n- opportunity id\n- current venue\n- issue"
    ],
    "c27": [
      "text",
      "npm run validate:all"
    ],
    "c28": [
      "text",
      "npm run validate:all"
    ],
    "c29": [
      "text",
      "1. Patch static validator to include map.html and schedule.html.\n2. Add source URL cleanup status handoff.\n3. Add source URL backlog file.\n4. Pick the first 5–10 opportunity records missing source URLs.\n5. Gather official/public URLs only.\n6. Update opportunities-2026.js.\n7. Run npm run validate:all.\n8. Add a short handoff with completed IDs and remaining IDs."
    ],
    "c30": [
      "text",
      "1. Patch static validator to include map.html and schedule.html.\n2. Add source URL cleanup status handoff.\n3. Add source URL backlog file.\n4. Pick the first 5–10 opportunity records missing source URLs.\n5. Gather official/public URLs only.\n6. Update opportunities-2026.js.\n7. Run npm run validate:all.\n8. Add a short handoff with completed IDs and remaining IDs."
    ],
    "c31": [
      "stagecoach-2026",
      "bourbon-and-beyond-2026\ninkcarceration-2026\nportola-2026\nedc-orlando-2026\nrailbird-2026"
    ],
    "c32": [
      "stagecoach-2026",
      "bourbon-and-beyond-2026\ninkcarceration-2026\nportola-2026\nedc-orlando-2026\nrailbird-2026"
    ],
    "c33": [
      "text",
      "State: closed\nMerged: false\nBase: main\nHead: claude/research-version-edits-z0gqw6"
    ],
    "c34": [
      "text",
      "State: closed\nMerged: false\nBase: main\nHead: claude/research-version-edits-z0gqw6"
    ],
    "c35": [
      "text",
      "ai-communication/2026-06-22-claude-stage-1-update.md\nai-communication/2026-06-22-claude-stage-2-update.md\nai-communication/2026-06-22-claude-stage-3-update.md\nai-communication/2026-06-22-claude-stage-4-update.md\nai-communication/2026-06-22-source-url-cleanup-status.md\nai-communication/2026-06-22-source-url-backlog.md"
    ],
    "c36": [
      "text",
      "ai-communication/2026-06-22-claude-stage-1-update.md\nai-communication/2026-06-22-claude-stage-2-update.md\nai-communication/2026-06-22-claude-stage-3-update.md\nai-communication/2026-06-22-claude-stage-4-update.md\nai-communication/2026-06-22-source-url-cleanup-status.md\nai-communication/2026-06-22-source-url-backlog.md"
    ],
    "c37": [
      "text",
      "45c57f66172856d292a7ae4f54eb81ca16810ef2"
    ],
    "c38": [
      "text",
      "45c57f66172856d292a7ae4f54eb81ca16810ef2"
    ],
    "c39": [
      "text",
      "ai-communication/2026-06-22-chatgpt-validator-and-source-catchup.md"
    ],
    "c40": [
      "text",
      "ai-communication/2026-06-22-chatgpt-validator-and-source-catchup.md"
    ],
    "c41": [
      "text",
      "994fe061684807d35e3900c5b0b16baf1a898301"
    ],
    "c42": [
      "text",
      "994fe061684807d35e3900c5b0b16baf1a898301"
    ],
    "c43": [
      "text",
      "npm run validate:all"
    ],
    "c44": [
      "text",
      "npm run validate:all"
    ]
  },
  "tokenStats": {
    "rawChatTokens": 3816,
    "compressedTokens": 2995,
