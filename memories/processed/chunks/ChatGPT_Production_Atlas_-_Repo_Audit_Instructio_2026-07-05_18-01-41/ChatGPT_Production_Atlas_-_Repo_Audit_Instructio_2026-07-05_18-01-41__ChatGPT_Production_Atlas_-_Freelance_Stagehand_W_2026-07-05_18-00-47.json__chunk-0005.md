---
{
  "chunk_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0005",
  "archive_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41",
  "archive_filename": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41.zip",
  "source_path": "ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json",
  "chunk_index": 5,
  "chunk_count_for_source": 40,
  "char_start": 45017,
  "char_end": 57004,
  "source_sha256": "89d6af20402670cdf4e0c6685b02a157093c86475bd4dc8bfa987c63252c20ab",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

ages app will stop reading data/atlas-research-data.js and will use only the new master data file. Older files remain as archive, not active data sources."
    ],
    [
      "u",
      "t105",
      "dont delete any old research let it be in the file but take it out of view of the index page"
    ],
    [
      "a",
      "t106",
      "I will not delete older research files or old data files. I’m only removing the messy/archived sources from the active Pages view by pointing index.html to one clean master data file."
    ],
    [
      "a",
      "t107",
      "I checked the new master file. I’m replacing the master file contents with the full consolidated dataset now, then I’ll update index.html to read only from that master file."
    ],
    [
      "a",
      "t108",
      "The master data file is now the consolidated source. I’m updating index.html next so the visible Pages app reads only data/festival-atlas-master-data.js and no longer reads the older compiled data file."
    ],
    [
      "a",
      "t109",
      {
        "txt": "The app now reads from one active master file only:\nVerified in index.html:\nand the app now uses:\nfor the visible UI. It starts with the narrowed production labor categories: staging, rigging, lighting, audio, video/LED, power, site ops, logistics, scenic/carpentry, backline, stage management, and production office. Commits\nNo old research was deleted. It is no longer driving the visible index.html page.",
        "c": [
          "c171",
          "c172",
          "c173",
          "c174"
        ]
      }
    ],
    [
      "u",
      "t110",
      "do the deeper research needed per the notes on the cards. \"Next research: identify whether any of these companies, a local IATSE local, a nonunion labor provider, or another vendor staffs this festival.\""
    ],
    [
      "a",
      "t111",
      "I’ll start the deeper verification pass on the active master data, not the archived files. This will add structured research fields for actual/likely staffing pathways, source URLs, IATSE/local checks, and explicit “not publicly verified yet” flags where the vendor relationship cannot be confirmed from public sources."
    ],
    [
      "a",
      "t112",
      {
        "txt": "Correct. I did not delete the old research. What I changed\nI created one clean active data file:\nThat file is now the single source powering the visible GitHub Pages app. The older research files and older messy data files remain in the repo, but index.html no longer reads from them. Active app source\nindex.html now reads only:\nand uses:\nfor the visible UI. Master file status\nThe master file starts with the clean production category model:\nVerified in the master data file. Wikipedia+1\nFor actual department vendors, public confirmation is much harder. Some vendors publish portfolios, but many festival labor/vendor relationships are not public, change annually, or are only known through calls, locals, contracts, and production networks. So the app now marks those as verification work instead of guessing. Commits\nThe old research remains in the repository as archive/history. The visible app now reads from one clean master file.",
        "c": [
          "c175",
          "c176",
          "c177",
          "c178",
          "c179",
          "c180",
          "c181",
          "c182",
          "c183",
          "c184"
        ]
      }
    ],
    [
      "a",
      "t114",
      "It will show only festival-specific confirmed companies, or a clear “no confirmed public vendor yet” note. Then I’ll add the first deeper-research pass with sourced producer/promoter verification and conservative staffing-pathway records."
    ],
    [
      "a",
      "t115",
      "I’m correcting the visible behavior now: the festival modal will stop showing global employer leads under a festival’s mapped branches. It will only show festival-specific confirmed vendors if the master data has them; otherwise it will display “no confirmed public vendor yet.”"
    ],
    [
      "a",
      "t116",
      "The current index.html SHA is confirmed. I’m replacing it with a cleaner version that still reads the master file, but its festival modal will only display confirmedVendors attached to that festival record. Global employer leads stay in the Employers and Matrix tabs only."
    ],
    [
      "a",
      "t117",
      {
        "txt": "Yes — I corrected that specific issue. That was wrong for your use case. What I changed\nThe festival modal now does this:\nIf no source-backed vendor has been attached to that exact festival branch, the card now says:\nVerified in the active index.html: the page now explicitly states that global employer leads are not shown as if they staff a specific festival, and a festival branch will show “No confirmed public vendor yet” until a source confirms the exact relationship. What research was added\nI also added a verification tracking file:\nThat file sets the rule that festival branches must only display confirmed vendors, and it lays out the next research workflow:\nFirst deeper-research findings\nThe first verification pass confirms producer/promoter ecosystems where public sources support them:\nGoldenvoice / AEG is tied to Coachella and Stagecoach. Wikipedia+1\nCurrent commits\nThe app is now safer: it will not present unverified companies as festival-specific staffers.",
        "c": [
          "c185",
          "c186",
          "c187",
          "c188",
          "c189",
          "c190",
          "c191",
          "c192",
          "c193",
          "c194"
        ]
      }
    ],
    [
      "u",
      "t118",
      "i dont want or need globale employers only united states employers"
    ],
    [
      "a",
      "t119",
      "I’ll clean the active master data so the visible app shows United States employer leads only. I will not delete old archived research; I’ll only change the active master file and the visible label language in index.html."
    ],
    [
      "a",
      "t120",
      "Multinational companies will only remain if they are useful as U.S. operations / U.S. hiring leads. The active app will not present broad global employer categories."
    ],
    [
      "a",
      "t121",
      "I updated the active master data to U.S.-only employer leads. I’m also updating index.html with a new cache-busting version so Pages loads the U.S.-only master file instead of any previously cached copy."
    ],
    [
      "a",
      "t122",
      {
        "txt": "The active app is now United States employer leads only. Visible app labels\nThe visible app now says:\nand:\nVerified in index.html. Data source\nThe Pages app now loads the U.S.-only master file with a new cache-busting version:\nVerified in index.html. Commits\nOlder research and older data files remain in the repo as archive material, but the visible app now uses the U.S.-only master data source.",
        "c": [
          "c195",
          "c196",
          "c197",
          "c198",
          "c199",
          "c200",
          "c201",
          "c202"
        ]
      }
    ],
    [
      "u",
      "t123",
      "run a verification check for all festivals make sure they are active in 2026"
    ],
    [
      "a",
      "t124",
      "I’ll run this as a 2026 active-status verification pass on the research-version branch. I’ll keep inactive/uncertain festivals in the master file only if they are marked, rather than silently deleting them."
    ],
    [
      "a",
      "t125",
      "I found two clear non-active/unsafe records from the first verification pass: Boston Calling is not scheduled for 2026, and Hangout/Sand In My Boots will not run in 2026. I’m writing a full pass file now so the app can distinguish confirmed active, inactive, and still-needs-verification records without deleting historical research."
    ],
    [
      "a",
      "t126",
      {
        "txt": "Wikipedia+3Wikipedia+3Pitchfork+3\nRemove or hide from active 2026 view\nThe check found these should not be treated as active 2026 work targets:\nBoston Calling is listed with next edition in 2027, not 2026. Hangout/Sand In My Boots is reported as not returning in 2026. Electric Zoo has no next 2026 date in the source found. Wikipedia+3Wikipedia+3People.com+3\nStill needs verification before active display\nSome records remain in research, but should not be treated as confirmed active 2026 until a specific source is attached:\nNext required app/data update\nThe verification file recommends adding these fields to each festival in the master data:\nThen the app should show only:\nin the active work-target view, while keeping inactive and unverified festivals archived but out of the main page.",
        "c": [
          "c203",
          "c204",
          "c205",
          "c206",
          "c207",
          "c208",
          "c209",
          "c210",
          "c211",
          "c212",
          "c213",
          "c214"
        ]
      }
    ],
    [
      "u",
      "t127",
      "find and verify all links in the employer matrix"
    ],
    [
      "a",
      "t129",
      "I’ll verify the active employer-matrix links against the current U.S.-only master data file, then update the research branch with a link verification pass and fix any bad or overly broad URLs in the active data."
    ],
    [
      "a",
      "t130",
      "I found three buckets: verified working career/hiring links, links that could not be verified cleanly through the web tool, and employer records that have no link yet. I’m committing a link-verification report now so the matrix work has an auditable checklist instead of guessed URLs."
    ],
    [
      "a",
      "t131",
      {
        "txt": "Added verification report\nCommit:\nVerified working / relevant links\nThese links were verified as usable career, hiring, jobs, or official application/contact routes:\nEmployerVerified link statusBigger Hammer Production ServicesVerified careers pageClair Global U.S.Verified careers/jobs pageEighth Day SoundVerified careers pageNEP Live Events U.S.Verified careers pageTAIT U.S.Verified careers page; slash version redirectsAll Access Staging & ProductionsVerified careers pageAggreko U.S.Verified redirect to North America careersUnited RentalsVerified jobs pageSunbelt RentalsVerified redirect to careers siteASM Global U.S. venues / Legends GlobalVerified redirect to Legends Global careersIATSE Local UnionsVerified local union directoryAEG / GoldenvoiceVerified AEG careers page\nExamples: Bigger Hammer’s careers page lists stagehand and rigger roles, Clair Global’s careers page lists current openings, United Rentals has a searchable jobs page, and Sunbelt redirects to its careers site. Sunbelt Rentals+3Bigger Hammer+3Clair Global+3\nLinks that still need manual verification\nSome URLs may be valid, but I could not cleanly verify them through the web tool because the page was blocked, redirected unclearly, failed to open, or did not return usable career content. These should show as verify link, not as confirmed hiring links, until checked:\nRecords with no link yet\nThese should remain employer leads, but should not show clickable links until an official route is found:\nRecommended data change\nThe report recommends adding this to every employer record:\nThen the app should only make a link clickable when careerUrlStatus is verified or verified_redirect.",
        "c": [
          "c215",
          "c216",
          "c217",
          "c218",
          "c219",
          "c220",
          "c221",
          "c222",
          "c223",
          "c224"
        ]
      }
    ],
    [
      "u",
      "t132",
      "The verification file recommends adding these fields to each festival in the master data:\n\nactive2026Status: \"confirmed_active_2026 | inactive_2026 | needs_verification\",\nactive2026SourceUrl: \"https://...\",\nactive2026CheckedDate: \"2026-06-21\",\nvisibleInActive2026View: true | false"
    ],
    [
      "a",
      "t133",
