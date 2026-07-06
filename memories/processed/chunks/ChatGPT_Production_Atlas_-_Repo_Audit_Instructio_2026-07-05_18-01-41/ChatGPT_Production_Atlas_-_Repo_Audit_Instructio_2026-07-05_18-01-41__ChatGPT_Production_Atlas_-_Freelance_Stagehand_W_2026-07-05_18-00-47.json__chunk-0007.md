---
{
  "chunk_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0007",
  "archive_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41",
  "archive_filename": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41.zip",
  "source_path": "ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json",
  "chunk_index": 7,
  "chunk_count_for_source": 40,
  "char_start": 67621,
  "char_end": 78901,
  "source_sha256": "89d6af20402670cdf4e0c6685b02a157093c86475bd4dc8bfa987c63252c20ab",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

stinction in the data so we still know which links are true hiring pages versus general company pages."
    ],
    [
      "a",
      "t147",
      "I’m applying that rule now: verified hiring/career links stay as career links; every employer without a verified hiring page gets its official homepage as the fallback link, while the data status marks it as homepage_fallback rather than verified_career."
    ],
    [
      "a",
      "t148",
      "The fallback-link rule is now applied. I’m verifying the data file so I can give you the exact status."
    ],
    [
      "a",
      "t149",
      {
        "txt": "Link rule now applied\nThe employer matrix now uses this logic:\nThe data also keeps a status label so we know which is which:\nExamples now corrected\nThese now link to company homepages instead of dead/unverified career pages:\nVerified in the active data file. Commit",
        "c": [
          "c245",
          "c246",
          "c247",
          "c248",
          "c249",
          "c250",
          "c251",
          "c252",
          "c253",
          "c254"
        ]
      }
    ],
    [
      "u",
      "t150",
      "Create an iatse directory for all of the United States"
    ],
    [
      "a",
      "t151",
      {
        "txt": "New link rule\nThe employer matrix now uses:\nThe active data also marks each link as either:\nHomepage fallbacks now added\nThese employers now link to homepages instead of blank/dead/unverified careers pages:\nVerified career links kept\nThese still point to career/apply/job/local directory pages:\nVerified in the active data file. The UI already links whatever URL is present in careerUrl, so the matrix should now route to either a verified career page or a homepage fallback.",
        "c": [
          "c255",
          "c256",
          "c257",
          "c258",
          "c259",
          "c260",
          "c261",
          "c262",
          "c263",
          "c264"
        ]
      }
    ],
    [
      "u",
      "t152",
      "Create an iatse local directory for all of the United states"
    ],
    [
      "a",
      "t153",
      "I’ll add this as a separate U.S. IATSE directory data file on the research-version branch, then add a visible directory page/section into the app. I’ll use the official IATSE local-union directory as the source and mark records as source-derived rather than guessed."
    ],
    [
      "a",
      "t154",
      "I’ll add this as a separate active directory file, then wire it into the research-version app as its own tab. It will not replace the employer matrix; it will be a U.S. IATSE local lookup by state, district, jurisdiction, and craft."
    ],
    [
      "a",
      "t155",
      "I’ll create a dedicated file for the U.S. IATSE local directory and then add an app tab for it. The directory will be searchable by local number, state, city/jurisdiction, craft, and district."
    ],
    [
      "a",
      "t156",
      {
        "txt": ". Added visible app tab\nAdded a new tab/section:\nThe section is searchable by:\nVerified in index.html: the app now has a United States IATSE local directory section and loads the new directory file. Commits\nNote: this is a lookup aid, not a final jurisdiction ruling. Each card links back to the official IATSE directory for final verification before outreach.",
        "c": [
          "c265",
          "c266",
          "c267",
          "c268",
          "c269",
          "c270"
        ]
      }
    ],
    [
      "u",
      "t157",
      "Back at it. Let's begin. What do you see that needs fixed, changed, added, or removed from the web app we are currently building which is solely based as the resource scouting database for this app?"
    ],
    [
      "a",
      "t158",
      "I’ll audit the current research-version app as it exists now: active data source, IATSE directory, index behavior, and what still does not match the “resource scouting database” goal."
    ],
    [
      "a",
      "t159",
      {
        "txt": "Here is the clean audit of what needs fixed, changed, added, or removed for the current purpose: a resource scouting database for the future app, not the full job app yet. Current core problem\nThe app is drifting between three things:\nFor this phase, it should be only:\nEverything else should support that. Fix first\n1. The data model is still too compressed\nThe current active master data is still mostly pipe-delimited strings inside JavaScript. It needs to move to structured records like:\nRight now the app can display information, but it cannot properly track verification, confidence, source quality, or department-by-department staffing progress.\n2. Source URLs are incomplete\nSome 2026 active statuses came from the user-provided status report but still have no direct source URL attached. Example:\nDo not auto-claim jurisdiction yet. A homepage fallback should not look the same as a verified apply page. Recommended tabs:\nThe key addition is Needs Verification. Add verification status filters\nAdd filters for:\nThis will make the database useful as a workbench, not a display page.\n8. Add source quality ranking\nNot all sources should count the same. Add soon\n10. Festival-by-festival scouting checklist\nEach festival should have a progress checklist:\nThis should be stored in data, not shown visually.\n11. “Best lead” field\nFor each festival, add:\nThat gives you a practical next move instead of a pile of research.\n12. Contact fields\nFor each company/local:\nDo not force every record into one careerUrl. Remove or hide\n14. Hide inactive festivals from the main scouting view\nAlready partly done, but keep them separated. Main view should not show:\nunless the user selects a research filter.\n15. Priority order\nHere is the order I would build from here:\nMost important correction\nThe app should become a research operations dashboard, not a directory.",
        "c": [
          "c271",
          "c272",
          "c273",
          "c274",
          "c275",
          "c276",
          "c277",
          "c278",
          "c279",
          "c280",
          "c281",
          "c282",
          "c283",
          "c284",
          "c285",
          "c286",
          "c287",
          "c288",
          "c289",
          "c290",
          "c291",
          "c292",
          "c293",
          "c294",
          "c295",
          "c296",
          "c297",
          "c298",
          "c299",
          "c300",
          "c301",
          "c302",
          "c303",
          "c304",
          "c305",
          "c306",
          "c307",
          "c308",
          "c309",
          "c310",
          "c311",
          "c312",
          "c313",
          "c314",
          "c315",
          "c316",
          "c317",
          "c318",
          "c319",
          "c320",
          "c321",
          "c322",
          "c323",
          "c324",
          "c325",
          "c326"
        ]
      }
    ],
    [
      "u",
      "t160",
      "The calendar doesn't have to be festivals only. I need it to track any long term gig that might give accomodations that lives inside the industry I work in"
    ],
    [
      "a",
      "t161",
      "Understood. The calendar should become a long-term production opportunity calendar, not a festival calendar."
    ],
    [
      "a",
      "t162",
      "I’m going to treat that as a product-scope correction: the database should track long-term work opportunities, with festivals only one opportunity type. I’m adding a dedicated scouting model file so future records are structured around lodging/travel/accommodation potential, not festival names."
    ],
    [
      "a",
      "t163",
      {
        "txt": "That changes the scope of the database. New direction\nThe calendar should track:\nFestivals are only one category. Better database question\nThe app should now answer:\nImmediate next fix\nThe next code change should be to replace visible festival-only language with:\nThen we add an Opportunity Type filter and a Travel / Lodging Potential badge to every card.",
        "c": [
          "c327",
          "c328",
          "c329",
          "c330",
          "c331",
          "c332",
          "c333",
          "c334",
          "c335",
          "c336",
          "c337",
          "c338",
          "c339",
          "c340",
          "c341",
          "c342",
          "c343",
          "c344"
        ]
      }
    ],
    [
      "u",
      "t164",
      "Go and find the correct link paths to provide for the entire web app. Fix any broken links, make sure every link on the page links out to the proper places or at the very least to a page that holds information about the selected items."
    ],
    [
      "a",
      "t165",
      "I’ll verify the active app’s outbound links from the current research-version files, then patch the data and UI so every clickable item routes either to a verified career/apply page, official homepage, official event page, or official directory/source page."
    ],
    [
      "a",
      "t166",
      {
        "txt": "I captured that scope change in the repo. It is now scoped as a:\nThe model now says it should track any live-event / production-industry opportunity that may provide:\nThat is now documented in the repo. Festivals become one category\nFestivals stay in the system, but only as one opportunity type inside the broader database. The repo note explicitly says not to use “Festival Calendar” as the working name and to use “Long-Term Production Opportunity Calendar” instead. File added\nCommit:\nNext code correction\nThe visible app still needs the UI wording changed from festival-first to opportunity-first. The next patch should rename:\nThen add an Opportunity Type filter and lodging/travel/per diem badges.",
        "c": [
          "c345",
          "c346",
          "c347",
          "c348",
          "c349",
          "c350",
          "c351",
          "c352",
          "c353",
          "c354",
          "c355",
          "c356"
        ]
      }
    ],
    [
      "u",
      "t167",
      "Create a list of all things needed fixed. Let's fix everything little by little then add we can add more data or figure out how to create a live stream of new data if possible"
    ],
    [
      "a",
      "t168",
      {
        "txt": "Here is the working repair backlog, ordered so we can fix the foundation first, then add more data, then consider live/automated data later. Fix List — Resource Scouting Database\nPhase 1 — Clean the app’s identity and language\nThe app still reads like a festival-only database in places. PriorityFixWhy1Rename Festival staffing calendar to Long-Term Opportunity CalendarThe database is festivals anymore.2Rename Festival profiles to Opportunity profilesIt should support festivals, tours, conventions, residencies, stadium builds, etc.3Rename Active 2026 festivals stat to Active 2026 opportunitiesPrevents the app from narrowing itself too early.4Replace “festival target” language with “production opportunity” or “work target”Better matches your actual use case.5Keep “Music Festival” as one opportunity type, not the whole app categoryFestivals remain important, but they are not the whole database. First fix to do: update the visible wording in index.html.
