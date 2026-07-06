---
{
  "chunk_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0002",
  "archive_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41",
  "archive_filename": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41.zip",
  "source_path": "ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json",
  "chunk_index": 2,
  "chunk_count_for_source": 40,
  "char_start": 11397,
  "char_end": 22923,
  "source_sha256": "89d6af20402670cdf4e0c6685b02a157093c86475bd4dc8bfa987c63252c20ab",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

 1099, W-2, union referral, temp payroll, or direct hire. Phase 4 — 1099 operations layer\nThis covers the business-admin side: W-9 storage, contracts, e-sign, timesheets, invoices, mileage/expense logging, quarterly tax reminders, and an exportable tax packet. My take\nThe roadmap exists, but it is still high-level. The next useful upgrade would be converting it into an actionable build plan with:\nThe first real build move should be Phase 1: split the embedded festival/company data out of index.html into JSON files and keep the app working from those files.",
        "c": [
          "c39",
          "c40"
        ]
      }
    ],
    [
      "u",
      "t36",
      "before any roadmap anything happens. i want you to make 2 branches in the repo. one branch is to create a market research specific version. the other branch is development of production ready app to take to market"
    ],
    [
      "a",
      "t37",
      "I’ll create both branches from the current main branch so they start from the same working repo state. Then I’ll confirm the branch names and their intended purpose."
    ],
    [
      "a",
      "t38",
      "The first branch-create call was blocked by the connector safety layer, not by GitHub. I’ll retry with simpler branch names that still preserve the two-track structure."
    ],
    [
      "a",
      "t39",
      "The market research branch is created. I’m creating the production branch from the same commit SHA so both branches start from identical repo state."
    ],
    [
      "a",
      "t40",
      {
        "txt": "Purpose: development branch for the app that can be taken to market. Use this branch for app architecture, UI/UX cleanup, data separation, profiles, saved searches, job tracking, marketplace features, and production-readiness work. Both branches were created from the same current main commit:\nSo they start from the same stable baseline.",
        "c": [
          "c41",
          "c42"
        ]
      }
    ],
    [
      "u",
      "t41",
      "cool. polish and clean up the research version branch. I am going to have you build research in this branch right now. so get the code ready for data expansion"
    ],
    [
      "a",
      "t42",
      "I’ll prepare the research-version branch without changing the production branch: add data folders, JSON schemas, research templates, a validation script, and a branch-specific build note so research expansion can happen cleanly."
    ],
    [
      "a",
      "t43",
      "The branch now has a dedicated data/ structure and clean dataset stubs. I’m adding schema files and research templates next so new records can be added consistently instead of freehand."
    ],
    [
      "a",
      "t44",
      "Schemas are in place for festivals, companies, and sources. I’m adding the no-dependency validator and research templates so future entries can be checked before they get folded into the app."
    ],
    [
      "a",
      "t45",
      {
        "txt": "What I added to research-version\n1. It also explicitly blocks production-only work like authentication, payment processing, private worker data, and marketplace logic from this branch.\n2. Structured data expansion folder\nCreated:\nThe data/README.md explains that the app still uses embedded data in index.html, but this branch is now prepared for external JSON expansion, schemas, templates, and validation before refactoring the app to load external data.\n3. JSON schemas\nCreated:\nThese define the expected research fields for festivals, companies/vendors, and source records.\n5. No-dependency data validator\nCreated:\nIt checks that JSON files exist, are valid JSON, include schema versions, use array datasets, have valid IDs, use approved research_status values, and link only to known source IDs. Also added:\nWith:\n6. Research templates\nCreated:\nThese are ready for filling out festival and vendor/company research before converting records into JSON.\n7. Research backlog\nCreated:\nIt gives the first work queue:\nCurrent branch state\nresearch-version is now ready for research expansion. The next best step is:",
        "c": [
          "c43",
          "c44",
          "c45",
          "c46",
          "c47",
          "c48",
          "c49",
          "c50",
          "c51",
          "c52",
          "c53",
          "c54",
          "c55",
          "c56",
          "c57",
          "c58"
        ]
      }
    ],
    [
      "u",
      "t46",
      "\"be expert market research analyst specializing in the U.S. live entertainment and music festival industry. Categorize insights: Separate your findings into verified industry trends, speculative market theories, and critical uncertainties (e.g., impact of climate-related disruptions, insurance volatility, or shifting consumer demographics). Include a brief section identifying the assumptions made in your analysis.\"\n\n2. Emerging Skill Gaps: The transition from general event staffing to specialized technical and data-driven roles. Industry Trade Publications: Reviewing sources like Pollstar, Billboard Touring, and FestForums for sector-specific workforce insights.\n\nuse this prompt plus all of your current knowledge base to perform valuable and insightful research on this project. add all information into the research version branch of the repository"
    ],
    [
      "u",
      "t47",
      "it wont let me download the packet you created"
    ],
    [
      "u",
      "t48",
      "enter all of the information into the research version github repository"
    ],
    [
      "a",
      "t49",
      "I’ll put the package contents into the GitHub repo instead of relying on the download. I need to identify the exact “research version” repository first, then I’ll upload the README, current index.html, and research folder files."
    ],
    [
      "a",
      "t50",
      "I found a likely target: thecrewblueprint-glitch/festival-atlas. I did not find a repo named “research,” so I’m treating festival-atlas as the research-version repo because it matches this app’s subject."
    ],
    [
      "a",
      "t51",
      "— the information is already in the GitHub research repo:\nRepository: thecrewblueprint-glitch/festival-atlas\nGitHub link: https://github.com/thecrewblueprint-glitch/festival-atlas thecrewblueprint-glitch/festiva…\nFiles now in the repo\nFileStatusREADME.mdContains the accessible conversation record, project summary, repo contents, and limitation note.index.htmlCurrent FestWorker web app uploaded into the repo.research/deep-research-report.mdFull deep research review and product direction.research/source-links.mdResearch source categories and reference links.research/implementation-roadmap.mdDevelopment roadmap for turning it into a stronger 1099 stagehand work-finding tool. The README is not a perfect verbatim ChatGPT export, because I only have access to the conversation context available here, not every hidden UI/tool event."
    ],
    [
      "u",
      "t52",
      "it was supposed to be entered into the research version branch of that repository"
    ],
    [
      "a",
      "t53",
      "Correct. I’ll fix the placement now: verify what exists on research-version, then add the market-employer analysis and any missing research package files directly to that branch, not main."
    ],
    [
      "a",
      "t54",
      "I’m adding a dedicated employer-landscape research report to research-version. It will sit under research/ and will not touch main or production-ready-app."
    ],
    [
      "a",
      "t55",
      "The employer-landscape analysis is now committed to research-version. I’ll verify the file from that branch so the final answer points to the exact location."
    ],
    [
      "a",
      "t56",
      {
        "txt": "You were right. I corrected it. Employer structure differences. Hiring patterns and labor trends. Freelance vs W-2 vs union/vendor pathways. Production, logistics, sustainability, digital marketing, artist relations, and emerging roles. Verified trends, speculative theories, and critical uncertainties. National vs independent hiring priorities. Macroeconomic budget pressures. Assumptions. Research roadmap for role targeting, geographic hubs, and company targeting. Core framing is now in the branch: festival employment is treated as an ecosystem involving promoters, venues, labor companies, IATSE locals, production vendors, site ops, security, sanitation, sustainability, sponsor activation, and more — not the public festival brand. The earlier package files were already in the repo, but this new research pass is now placed where it belongs: research-version branch.",
        "c": [
          "c59",
          "c60",
          "c61",
          "c62"
        ]
      }
    ],
    [
      "u",
      "t57",
      "what different branches of work are involved in large scale multi week set ups for live music and entertainment?"
    ],
    [
      "a",
      "t58",
      {
        "txt": "For a large-scale multi-week live music or entertainment build, the work splits into major operational branches. Typical work:\nDressing rooms\nGreen rooms\nHospitality riders\nArtist check-in\nRunners\nCredentials\nMeals\nTransportation\nGuest lists\nProduction office support\nTypical roles:\nThis is often a separate hiring path from technical stagehand labor.\n14. Credentials / Access Control / Box Office Tech\nAt large events, access control becomes a major operation. Typical work:\nWristbands\nCredentials\nStaff check-in\nRFID systems\nScanner support\nGate troubleshooting\nGuest list resolution\nZone access control\nLost/stolen credential issues\nTypical roles:\nThis branch has grown because festivals now use more digital ticketing, wristband, scanning, and access-zone systems.\n15. Security / Medical / Emergency Management\nUsually handled by specialized contractors, but it shapes the whole site. Typical work:\nSecurity posts\nBag checks\nPit security\nCrowd management\nEmergency lanes\nMedical tents\nWeather plans\nEvacuation planning\nIncident reporting\nRadio communication\nTypical roles:\nStagehands normally do not perform security or medical work, but they must understand how these departments affect site movement and emergency holds.\n16. Sustainability / Waste / Environmental Operations\nThis is becoming more formal at large events. Typical work:\nRecycling\nCompost\nWaste diversion\nWater refill stations\nReusable cup systems\nGenerator reduction\nBattery power pilots\nVendor sustainability compliance\nPost-event site restoration\nCarbon reporting\nTypical roles:\nThis is an emerging employment branch worth tracking separately in the research database.\n17. Food, Beverage, Merch, Vendors, and Sponsor Activations\nNot always “production,” but large events cannot operate without these branches. Typical work:\nVendor booth builds\nMerch tents\nPOS systems\nSponsor structures\nBrand activations\nSignage\nPower drops\nLoad-in/load-out support\nGuest-facing logistics\nTypical roles:\nFor stagehands, this can create work through scenic, tenting, power, signage, flooring, and activation build vendors.\n18. Administrative / Production Office\nThe production office is the paperwork and communication hub. Typical work:\nSchedules\nContact sheets\nCrew lists\nVendor check-ins\nRadio assignments\nCredentials\nPurchase orders\nReceipts\nRunner tasks\nIncident logs\nDaily reports\nTypical roles:\nThis is a common entry point for people moving from physical stagehand work toward production management.
