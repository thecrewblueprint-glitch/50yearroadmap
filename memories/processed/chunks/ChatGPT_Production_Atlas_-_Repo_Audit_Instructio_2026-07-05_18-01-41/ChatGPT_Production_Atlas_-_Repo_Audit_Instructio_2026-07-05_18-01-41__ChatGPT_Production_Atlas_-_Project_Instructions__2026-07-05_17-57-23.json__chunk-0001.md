---
{
  "chunk_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Project_Instructions__2026-07-05_17-57-23.json__chunk-0001",
  "archive_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41",
  "archive_filename": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41.zip",
  "source_path": "ChatGPT_Production_Atlas_-_Project_Instructions__2026-07-05_17-57-23.json",
  "chunk_index": 1,
  "chunk_count_for_source": 3,
  "char_start": 0,
  "char_end": 11939,
  "source_sha256": "73b29cfad59ef10e48ddc5c875381740c1af32a67aa4ba6631e4e155ab58f52c",
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
      "Process your new added project instructions"
    ],
    [
      "a",
      "t2",
      "I’ll treat the Production Atlas / Festival Atlas repo instructions as the active project operating rules. For future Production Atlas / work research app tasks, I will:\nWork from thecrewblueprint-glitch/festival-atlas\nUse research-version as the default branch\nRead the specified repo docs first before acting\nKeep scope limited to the current static GitHub Pages research app unless you explicitly expand it\nAvoid backend/login/database/private workflow/scraping architecture by default\nFollow public-safety rules for contacts, sources, pay rates, lodging, and sensitive notes\nKeep source links centralized on sources.html\nUse the branch research manifest as authoritative\nRun validation for code/data changes when relevant\nLeave repo-visible handoff notes in ai-communication/ after meaningful updates\nWhen you ask me to continue the app, audit Claude’s work, patch files, validate, or pick up the roadmap, I’ll start from the repo context instead of asking you to restate it."
    ],
    [
      "u",
      "t3",
      "Connect to repo"
    ],
    [
      "a",
      "t4",
      "I’ll connect to thecrewblueprint-glitch/festival-atlas on research-version, read the required project docs first, then report the repo state and next actionable step."
    ],
    [
      "a",
      "t5",
      "I’ve confirmed the repo startup rules from research-version: repo docs are the source of truth, research-version overrides main, and updates need validation plus an ai-communication/ handoff when meaningful. Next I’m reading the collaboration protocol, roadmap, current-state handoff, and core app files."
    ],
    [
      "a",
      "t6",
      "The roadmap confirms the current task class is catch-up/inspection, not a code or data change. Stage 1 is still the entry point: baseline validation, page/nav normalization, manifest authority, and public-safe rendering."
    ],
    [
      "a",
      "t7",
      {
        "txt": "Repo state confirmed\nRepository: thecrewblueprint-glitch/festival-atlas\nActive branch: research-version\nDefault branch: main, but not current working state unless you say otherwise. Live Pages URL: https://thecrewblueprint-glitch.github.io/festival-atlas/\nApp type: static GitHub Pages research dashboard; no backend, login, database, private contact storage, payment, or scraping automation. Required project rules loaded\nI read the required startup docs and core files:\nai-communication/PROJECT_CHAT_GROUP_INSTRUCTIONS.md\nai-communication/AI_COLLABORATION_PROTOCOL.md\nai-communication/PRODUCT_ROADMAP.md\nai-communication/2026-06-22-chatgpt-to-claude-current-state.md\nREADME.md\npackage.json\ndata/packages/branch-research-manifest.js\nassets/atlas-core-v2.js\ntools/validate-static-app.js\ntools/validate-branch-research-packages.js\nCurrent app structure\nActive pages are listed as:\nREADME now includes map.html and schedule.html. Current roadmap position\nThe active roadmap is still focused on making the static work research app function well. Execution order starts with:\nRun validation and fix failures. Important finding\nThere is a likely Stage 1 cleanup issue:\nREADME and roadmap list 12 active pages, including map.html and schedule.html.\nindex.html navigation also includes Map and Schedule. But tools/validate-static-app.js currently validates only 10 required pages and does not include map.html or schedule.html. First patch should likely update the static validator to include map.html and schedule.html. Data/loading model confirmed\nBranch research package loading is manifest-driven through data/packages/branch-research-manifest.js. The manifest currently lists branch research batches from staging, rigging, lighting, audio, video/LED, power, site ops, logistics, scenic, stage management, production office, and backline.\natlas-core-v2.js still has a hardcoded fallback list, but it loads branch-research-manifest.js and replaces the fallback when window.BRANCH_RESEARCH_MANIFEST exists. Validation status\nValidation not run; this was a repo catch-up/inspection only through GitHub file access. Next best action: patch tools/validate-static-app.js so it validates map.html and schedule.html, then run or trigger npm run validate:all, then leave a handoff in ai-communication/.",
        "c": [
          "c1",
          "c2"
        ]
      }
    ],
    [
      "u",
      "t8",
      "Claude has completed the 4 stage roadmap and is now executing a data clean up"
    ],
    [
      "a",
      "t9",
      "I’ll treat Claude’s completed roadmap work as repo state, not memory. I’ll refresh from research-version, inspect the latest ai-communication/ handoffs if present, then verify what the current cleanup phase is before recommending or touching anything."
    ],
    [
      "a",
      "t10",
      "I’m not finding the new Claude stage handoffs through code search yet. I’m going to check recent commits and known ai-communication naming patterns next; if Claude committed the files, they should show up there even if search indexing is stale."
    ],
    [
      "a",
      "t11",
      "Primary risk during cleanup: accidentally publishing unsafe/private details, breaking manifest/report pairing, or weakening source-confidence language. Data cleanup rules I’ll apply\nFor any cleanup work, I’ll check against:\ndata/packages/opportunities-2026.js\ndata/packages/us-employers.js\ndata/packages/production-branches.js\ndata/iatse-us-local-directory.js\ndata/packages/branch-research-batch-*.js\ndata/packages/branch-research-manifest.js\nmatching research/*.md reports\nsources.html source rendering behavior\nvalidators in tools/\nCleanup priorities\nThe cleanup phase should focus on:\nPublic-safety audit\nNo private contacts, emails, phone numbers, pay rates, lodging details, rumors, private notes, or referrals. Each target has required fields. Confidence/status wording does not overstate vendor certainty. Source integrity\nRaw links stay centralized on sources.html. Cards/modals should point to source status, not dump source URLs. Validation\nFor data changes: npm run validate:branch-research\nFor app/data cleanup affecting pages: npm run validate:all\nNote\nI attempted to locate fresh Claude stage/data-cleanup handoffs through the GitHub connector, but search did not surface them yet."
    ],
    [
      "u",
      "t12",
      "Get up to date on the project and tell me what should be done next"
    ],
    [
      "a",
      "t13",
      "I’ll refresh from research-version, check the repo-visible handoffs and current files, then give you a practical “next work” recommendation based on validation risk and cleanup priority."
    ],
    [
      "a",
      "t14",
      "The specific dated Claude handoffs are not present under the expected filenames on research-version; GitHub returned 404 for stage 1–4 handoff paths. I’ll continue from the actual current files and treat missing handoffs as a documentation gap."
    ],
    [
      "a",
      "t15",
      "Current files still show the earlier app state: 12 active pages in README, but the static validator checks only 10. That gap should be fixed before relying on validation during cleanup."
    ],
    [
      "a",
      "t16",
      {
        "txt": "Confirmed\nThe repo still defines Production Atlas as a static GitHub Pages research dashboard for live-event production opportunities, employer/vendor routes, IATSE/local routes, and department-specific production branches.\nresearch-version is still the active working branch; main remains the default branch but not the working source of truth. README lists 12 active pages:\nindex.html\ncalendar.html\nopportunities.html\nbranches.html\nemployers.html\niatse.html\nmatrix.html\nanalytics.html\nsources.html\nguide.html\nmap.html\nschedule.html\nBranch research loading is still manifest-based through data/packages/branch-research-manifest.js. Important problem I found\nThe repo does not currently show the Claude stage 1–4 handoff files under the expected filenames:\nGitHub returned 404 for those paths. That means either:\nClaude did the work but did not commit the stage handoffs,\nthe files use different names,\nClaude worked on a different branch/local checkout, or\nGitHub search/indexing is stale, but the exact paths still are not present. Second issue: validator drift\nREADME says there are 12 active pages, including map.html and schedule.html. But tools/validate-static-app.js currently validates only these 10 pages:\nIt does not validate map.html or schedule.html. That should be fixed before trusting validation during cleanup. What should be done next\n1. Patch validation first\nUpdate tools/validate-static-app.js so requiredPages includes:\nThis is the next safest repo change because it protects all future cleanup work.\n2. Next cleanup should begin only after validate:all checks all active pages. Then run/trigger validation\nAfter the validator patch:\nIf data cleanup changes touch branch packages:\nThe available scripts are defined in package.json.\n4. Employer data cleanup\nus-employers.js contains public employer/vendor records and links. Opportunity source cleanup\nSome records have active2026SourceUrl; others do not. Branch research wording cleanup\nEnsure confirmedVendors, likelyResponsible, and publicLeads do not overstate vendor certainty. Backlog weak records\nCreate a cleanup backlog in ai-communication/ listing:\nmissing dates\nmissing active source links\nuncertain producer/promoter\nvague venue\nweak confidence language\nemployer links needing review\nMy recommendation\nDo this next:\nPatch tools/validate-static-app.js to include map.html and schedule.html, create a data-cleanup catch-up handoff, then run npm run validate:all.",
        "c": [
          "c3",
          "c4",
          "c5",
          "c6",
          "c7",
          "c8",
          "c9",
          "c10",
          "c11",
          "c12"
        ]
      }
    ],
    [
      "u",
      "t17",
      "Claude was In the middle of gathering source urls for things when he ran into limit usage problems"
    ],
    [
      "a",
      "t18",
      {
        "txt": "That changes the immediate next step. Current situation\nClaude was not doing general data cleanup yet. That means the next work should not jump into broad cleanup first. What should be done next\n1. Patch validator drift first\nStill important: tools/validate-static-app.js should include:\nRight now README says those are active pages, but the validator does not check them. That should be patched before trusting npm run validate:all.\n3. Resume source URL gathering in small batches\nThe source pass should continue in chunks, not all at once. Track unresolved records\nCreate a backlog file:\nSuggested sections:\n5. Then validate\nAfter each source batch:\nIf only opportunity source URLs changed, validate:all is enough after the validator patch. Based on the visible file sample, likely first targets include:\nThose should be verified before lower-value speculative records because they affect the usefulness of the dashboard most.",
        "c": [
          "c13",
          "c14",
          "c15",
          "c16",
          "c17",
          "c18",
          "c19",
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
      "I’ll search across likely Claude/head branches for the missing ai-communication files first, then patch the validator/page drift on research-version.
