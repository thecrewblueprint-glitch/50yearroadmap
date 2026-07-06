---
{
  "chunk_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Repo_Downloadable_Fil_2026-07-05_17-56-06-5-.json__chunk-0001",
  "archive_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41",
  "archive_filename": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41.zip",
  "source_path": "ChatGPT_Production_Atlas_-_Repo_Downloadable_Fil_2026-07-05_17-56-06 (5).json",
  "chunk_index": 1,
  "chunk_count_for_source": 2,
  "char_start": 0,
  "char_end": 11975,
  "source_sha256": "388bc23e58e1584014b930ae487ff15eb8b996293116235a5ff1c13e9af9f48f",
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
      {
        "txt": "Claude update stages\nStagePurposeShip when completeStage 1 — Stabilize the AppValidation, page inventory, navigation, manifest/report consistency, public-safe renderingApp validates and current pages are syncedStage 2 — Daily Work Research UsabilityHome/Guide improvements, Research Queue / Next Action view, value tiers, sorting, filtersAaron can quickly see what to research or pursue nextStage 3 — Clearer Opportunity DataStandardized cards, modals, branch cards, confidence language, cleanup listRecords are easier to compare and verifyStage 4 — Useful Planning ViewsCalendar, Map, Schedule, Analytics, Sources improvementsAaron can plan timing/geography/priority from the app\nPractical instruction for Claude\nClaude should not ship all 4 at once. Best cadence:\nSo Claude should create 4 separate update handoffs, one after each stage:\nFor now, Claude should ship only Stage 1 first.",
        "c": [
          "c1",
          "c2",
          "c3",
          "c4"
        ]
      }
    ],
    [
      "u",
      "t2",
      "Create instructions for the project chat group so that I don't have to constantly tell you each new chat to connect to the repository or what is going on you know a new chat connects and reads the repository information and you'll be up to date"
    ],
    [
      "a",
      "t3",
      "I’ll add a standing “project chat group instructions” file in ai-communication/ that tells every new assistant/chat exactly how to connect, what branch to read, what files to inspect first, and how to get current without you re-explaining context."
    ],
    [
      "u",
      "t4",
      "Print the instructions here so I can add them in chat gpt functions"
    ],
    [
      "a",
      "t5",
      {
        "txt": "Production Atlas / Festival Atlas — Project Chat InstructionsWhen Aaron opens a new chat about Production Atlas, Festival Atlas, the work research app, or the thecrewblueprint-glitch/festival-atlas repository, do not ask him to restate the project context first.Immediately connect to the repository context and catch up from repo-visible documentation.Repositorymain is not the current working state unless Aaron explicitly says to use main.If using GitHub tools, fetch from:If using a local terminal, run:First Files to ReadRead these first, in order:Then inspect task-specific files only as needed.Do not deep-read or cache the full research/ archive unless Aaron asks for research restructuring, source verification, report conversion, or archive cleanup.Current Project SummaryProduction Atlas / Festival Atlas is Aaron’s static work research app for scouting live-event production opportunities.The app should help answer:The current goal is to make the static work research app function well, not to build a backend or future platform.Current App BoundaryThe app is currently:Do not introduce backend/auth/private workflow/payment/scraping architecture unless Aaron explicitly opens that topic.Active RoadmapThe active roadmap is:It is intentionally limited to making the current work research app function.Roadmap stages:Do not expand the roadmap into backend architecture, private user systems, LMS integration, or general business planning unless Aaron asks.Collaboration ProtocolThe active collaboration protocol is:Core rules:Every meaningful AI update should leave a repo-visible handoff in:Public Safety RulesDo not publish or render:Public app may show:For uncertain information, use:Source Link RuleSource links belong on:Do not put raw source links inside:Sources should remain centralized for auditability and public-safety control.Manifest RuleBranch research packages are loaded through:When adding or editing branch research packages:Validation CommandsUse these commands when relevant:For documentation-only changes, validation may be skipped, but say:For code/data changes, do not claim completion unless validation was run or the inability to run it is documented.How a New Chat Should StartA new assistant session should do this:If Claude or Another Assistant Cannot See a FileMost likely cause:Tell them to run:Then check:Current Claude Work DirectionClaude has been directed to commence early roadmap steps.Claude should work in stages, not ship everything at once:After each stage, Claude should create:Each stage handoff should include:What New Chats Should Not DoDo not:Standard Opening Response for New ChatsWhen Aaron says something like:A good assistant response is:Then perform the repo catch-up.Final RuleAaron should not have to rebuild context manually.Every assistant must treat the repo documentation as the starting context and keep it updated enough that the next assistant can continue without requiring Aaron to repeat the project history. I also added this to the repo at:\nCommit:",
        "c": [
          "c5",
          "c6",
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
          "c32",
          "c33",
          "c34",
          "c35"
        ]
      }
    ]
  ],
  "t": {
    "t1": "2026-07-05T21:57:55.890Z",
    "t2": "2026-07-05T21:57:55.892Z",
    "t3": "2026-07-05T21:57:55.892Z",
    "t4": "2026-07-05T21:57:55.892Z",
    "t5": "2026-07-05T21:57:55.893Z"
  },
  "c": {
    "c1": [
      "text",
      "One stage = one contained update package + one handoff."
    ],
    "c2": [
      "text",
      "One stage = one contained update package + one handoff."
    ],
    "c3": [
      "text",
      "ai-communication/YYYY-MM-DD-claude-stage-1-update.md\nai-communication/YYYY-MM-DD-claude-stage-2-update.md\nai-communication/YYYY-MM-DD-claude-stage-3-update.md\nai-communication/YYYY-MM-DD-claude-stage-4-update.md"
    ],
    "c4": [
      "text",
      "ai-communication/YYYY-MM-DD-claude-stage-1-update.md\nai-communication/YYYY-MM-DD-claude-stage-2-update.md\nai-communication/YYYY-MM-DD-claude-stage-3-update.md\nai-communication/YYYY-MM-DD-claude-stage-4-update.md"
    ],
    "c5": [
      "text",
      "Repository: thecrewblueprint-glitch/festival-atlas\nPrimary working branch: research-version"
    ],
    "c6": [
      "text",
      "repo: thecrewblueprint-glitch/festival-atlas\nref: research-version"
    ],
    "c7": [
      "text",
      "git fetch origin\ngit checkout research-version\ngit pull origin research-version"
    ],
    "c8": [
      "text",
      "1. ai-communication/PROJECT_CHAT_GROUP_INSTRUCTIONS.md\n2. ai-communication/AI_COLLABORATION_PROTOCOL.md\n3. ai-communication/PRODUCT_ROADMAP.md\n4. ai-communication/2026-06-22-chatgpt-to-claude-current-state.md\n5. README.md\n6. package.json\n7. data/packages/branch-research-manifest.js\n8. assets/atlas-core-v2.js\n9. tools/validate-static-app.js\n10. tools/validate-branch-research-packages.js"
    ],
    "c9": [
      "text",
      "Where is the work?\nWhen is it happening?\nWhich production departments does it touch?\nWho are the public employer/vendor/labor-route leads?\nWhat action should Aaron take next?"
    ],
    "c10": [
      "text",
      "Static GitHub Pages app\nPublic-safe research dashboard\nNo backend\nNo login\nNo database\nNo private contact storage\nNo payment processing\nNo scraping/network automation"
    ],
    "c11": [
      "text",
      "Stage 1 — Stabilize the app\nStage 2 — Make the dashboard useful for daily work research\nStage 3 — Make opportunity data clearer and more sortable\nStage 4 — Make planning views useful"
    ],
    "c12": [
      "text",
      "ai-communication/AI_COLLABORATION_PROTOCOL.md"
    ],
    "c13": [
      "text",
      "Repo-visible files beat chat memory.\nresearch-version beats main unless Aaron says otherwise.\nManifest beats fallback arrays.\nValidation beats assumption.\nPublic safety beats convenience.\nSmall verified updates beat large undocumented changes."
    ],
    "c14": [
      "text",
      "private contacts\nphone numbers\npersonal emails\npay rates\nhotel/lodging details\ncrew rumors\nprivate field notes\nNDA information\nclient-sensitive information\nprivate referrals"
    ],
    "c15": [
      "text",
      "official/public source links\ngeneral confidence labels\npublic route notes\npublic-safe employer/vendor leads\nnext action notes\nhuman verification language"
    ],
    "c16": [
      "text",
      "Unknown publicly. Human verification needed."
    ],
    "c17": [
      "text",
      "opportunity popups\nbranch popups\nmap popups\nschedule cards"
    ],
    "c18": [
      "text",
      "data/packages/branch-research-manifest.js"
    ],
    "c19": [
      "text",
      "1. Add/update the package in data/packages/.\n2. Add/update the matching report in research/.\n3. Update branch-research-manifest.js if a package is added or removed.\n4. Ensure each branch package has exactly one window.OPPORTUNITY_BRANCH_RESEARCH_BATCH_* export.\n5. Run validation."
    ],
    "c20": [
      "text",
      "npm run validate:branch-research\nnpm run validate:static-app\nnpm run validate:all"
    ],
    "c21": [
      "text",
      "Validation not run; documentation-only change."
    ],
    "c22": [
      "text",
      "1. Identify Aaron’s requested task.\n2. Use the GitHub repo and research-version branch as current context.\n3. Read the project chat instructions, collaboration protocol, product roadmap, latest current-state handoff, README, and relevant files.\n4. Confirm whether the task is docs, code, data, research, validation, or planning.\n5. Work from current repo files, not stale chat memory.\n6. If making changes, commit them to research-version unless Aaron gives a different branch instruction.\n7. Leave a handoff in ai-communication/ after meaningful changes."
    ],
    "c23": [
      "text",
      "They are looking at main, a stale local checkout, or a PR/head branch instead of research-version."
    ],
    "c24": [
      "text",
      "git fetch origin\ngit checkout research-version\ngit pull origin research-version\nls ai-communication"
    ],
    "c25": [
      "text",
      "cat ai-communication/PROJECT_CHAT_GROUP_INSTRUCTIONS.md\ncat ai-communication/PRODUCT_ROADMAP.md\ncat ai-communication/AI_COLLABORATION_PROTOCOL.md"
    ],
    "c26": [
      "text",
      "Stage 1 — Stabilize the app first.\nStage 2 — Improve daily work research usability.\nStage 3 — Clarify opportunity data.\nStage 4 — Improve planning views."
    ],
    "c27": [
      "text",
      "ai-communication/YYYY-MM-DD-claude-stage-N-update.md"
    ],
    "c28": [
      "text",
      "files changed\nvalidation command/result\nwhat was fixed\nwhat still needs work\nnext recommended roadmap step"
    ],
    "c29": [
      "text",
      "Ask Aaron to re-explain the project before checking the repo.\nAssume main is current.\nDeep-load the full research archive by default.\nReintroduce Firecrawl or scraping automation.\nAdd backend/login/database/private workflow scope to this app roadmap.\nPublish private/sensitive data.\nMove source links into popups.\nMake large undocumented changes.\nSkip handoff notes after meaningful repo updates."
    ],
    "c30": [
      "text",
      "connect to the Production Atlas repo\npick up the work research app\ncontinue the Festival Atlas roadmap\nClaude made updates, catch up"
    ],
    "c31": [
      "text",
      "I’ll connect to the Production Atlas repository on research-version, read the project chat instructions, collaboration protocol, roadmap, current-state handoff, README, and the task-specific files. I’ll avoid the heavy research archive unless this task requires it, then I’ll report the current state and next step."
    ],
    "c32": [
      "text",
