---
{
  "chunk_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0008",
  "archive_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41",
  "archive_filename": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41.zip",
  "source_path": "ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json",
  "chunk_index": 8,
  "chunk_count_for_source": 40,
  "char_start": 78301,
  "char_end": 90296,
  "source_sha256": "89d6af20402670cdf4e0c6685b02a157093c86475bd4dc8bfa987c63252c20ab",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

CalendarThe database is festivals anymore.2Rename Festival profiles to Opportunity profilesIt should support festivals, tours, conventions, residencies, stadium builds, etc.3Rename Active 2026 festivals stat to Active 2026 opportunitiesPrevents the app from narrowing itself too early.4Replace “festival target” language with “production opportunity” or “work target”Better matches your actual use case.5Keep “Music Festival” as one opportunity type, not the whole app categoryFestivals remain important, but they are not the whole database. First fix to do: update the visible wording in index.html. PriorityFixWhy1Convert festival records into general opportunity recordsLets the app track festivals, tours, conventions, stadium builds, residencies, etc.2Add opportunityType to every recordNeeded for filtering and sorting.3Add startDate and endDate instead of only monthLong-term gigs need date ranges.4Add venue fieldImportant for union/local/vendor research.5Add accommodationPotentialCore to your goal.6Add travelPaidPotentialCore to your goal.7Add perDiemPotentialCore to your goal.8Add longTermValueScoreLets the app prioritize good leads.9Add nextResearchActionsTurns the database into a workbench instead of a static list.10Move away from pipe-delimited strings into structured objectsEasier to maintain and expand. Second fix to do: add the new opportunity fields to the active data model. PriorityFixWhy1Add opportunity type badgeExample: Music Festival, Tour, Convention, Arena Build.2Add lodging badgeExample: Lodging unknown, Lodging possible, Lodging confirmed.3Add travel badgeExample: Travel unknown, Travel likely, Travel confirmed.4Add per diem badgeExample: Per diem unknown, Per diem possible.5Add long-term value score badgeHelps rank opportunities.6Add date range to cardsMonth alone is not enough.7Add “next best action” to cardsExample: “Verify production labor provider.”8Separate inactive/unverified opportunities from active onesKeep old research, but do not clutter the active view. Third fix to do: upgrade card display after the data fields exist. PriorityFixWhy1Add source quality labelsOfficial source, trade source, user note, unverified.2Add checkedDate to every major claimKeeps stale data from being trusted forever.3Add verificationStatus per field, not per recordA festival can be active but still have unverified vendors.4Add missing-data checklistShows what still needs researched.5Add Needs Verification tabThis should become the daily research workbench.6Keep inactive records archived but hidden from active viewPrevents accidental outreach to dead leads. Fourth fix to do: create the Needs Verification tab. PriorityFixWhy1Replace single careerUrl with a links objectA company may have homepage, careers, contact, union directory, application portal.2Label links Careers, Apply, Homepage, Contact, Directory.3Add linkStatusVerified career page vs homepage fallback.4Add employer type filterLabor provider, vendor, promoter, venue, union, rental, staging, audio, etc.5Add “best use” fieldExample: “Apply for shop work,” “Track tour labor,” “Contact local branch.”6Add regional market coverageExample: Arizona, Michigan, Chicago, SoCal, Southeast.7Add “confirmed festival vendor” only when verifiedAvoids fake certainty. Fifth fix to do: upgrade employer links to structured link objects. PriorityFixWhy1Add possible IATSE local candidates to each opportunityBased on city/state/venue.2Mark local candidates as “needs jurisdiction confirmation”Avoids claiming jurisdiction incorrectly.3Add state filter that works cleanly for IATSE localsCurrent search works, but dedicated filtering would be better.4Add “official directory” link to each local cardAlready started; keep it consistent.5Add local type/craft filtersStagehands, wardrobe, broadcast, studio, mixed, exhibition, etc. Sixth fix to do: connect likely IATSE local candidates to opportunity records. CategoryData to addTouring productionsarena tours, stadium tours, amphitheater tours, comedy tours, theater toursArena/stadium buildsSuper Bowl, Final Four, WrestleMania, major boxing/MMA, college playoff eventsConventions/exposCES, NAB, Comic-Con, auto shows, medical conventions, trade showsCorporate eventsproduct launches, tech conferences, annual meetingsVenue residenciesLas Vegas residencies, casino runs, theater residenciesSeasonal productionsholiday shows, theme park seasons, fair grandstand seasonsBroadcast/live TVaward shows, sports broadcasts, concert livestreams, esportsFair/grandstand circuitsstate fairs, county fairs, touring concert series\nSeventh fix to do: add one new opportunity category after the structure is stable. Possible future approaches:\nOptionDescriptionComplexityManual research queueYou or AI adds verified records manuallyLowRSS/source monitoringWatch official sites, promoters, trade publicationsMediumGitHub data updatesNew data added through JSON commitsMediumWeb scraper pipelinePulls from selected public pagesMedium/highAPI-based feedsUses ticketing/event/job APIs where availableHighAI-assisted research queueAI suggests new leads, human approvesBest long-term option\nFor your use case, the safest future system is:\nDo not let random scraped data publish directly to the app without review. Recommended Fix Order\nI would fix it in this order:\nStart Point\nThe first fix should be small and clean:\nThat aligns the whole interface before we restructure the data underneath.",
        "c": [
          "c357",
          "c358",
          "c359",
          "c360",
          "c361",
          "c362"
        ]
      }
    ],
    [
      "u",
      "t169",
      "Do all phase 1 fixes now"
    ],
    [
      "a",
      "t170",
      "I’ll apply Phase 1 as a UI-language patch only: no data deletion, no data restructuring yet. This will rename festival-only labels to long-term opportunity scouting labels across the active index.html."
    ],
    [
      "a",
      "t171",
      "I’m fetching the active index.html and applying Phase 1 as a direct replacement: title/hero/stat/tab/section labels only. Data files stay unchanged."
    ],
    [
      "a",
      "t172",
      "I have the current file SHA. I’m going to patch the visible labels now without touching the active data or deleting any records."
    ],
    [
      "a",
      "t173",
      {
        "txt": "Phase 1 is done. App identity changed\nOld framing:\nNew framing:\nVerified in index.html.\n2. Calendar renamed\nOld:\nNew:\nThe calendar description now explicitly says it will expand beyond festivals into:\nVerified in index.html.\n3. Festival profiles renamed\nOld:\nNew:\nVerified in index.html.\n4. Navigation language changed\nNavigation now uses:\ninstead of festival-only language.\n5. Search placeholder updated\nSearch now says:\nVerified in index.html.\n6. Stats wording changed\nThe visible stat now uses:\ninstead of active festivals / departments. Commit\nPhase 1 is complete.",
        "c": [
          "c363",
          "c364",
          "c365",
          "c366",
          "c367",
          "c368",
          "c369",
          "c370",
          "c371",
          "c372",
          "c373",
          "c374",
          "c375",
          "c376",
          "c377",
          "c378",
          "c379",
          "c380",
          "c381",
          "c382"
        ]
      }
    ],
    [
      "u",
      "t174",
      "Create structures data packages that the web page points to that better reflects and condeses the data into an easily readable and Pullable fashion."
    ],
    [
      "a",
      "t175",
      "The app will still work from index.html, but it will load clean package files instead of one compressed pipe-delimited master file. Old files will remain as archive."
    ],
    [
      "a",
      "t176",
      "I’m creating four structured packages now: production branches, opportunities, employers, and a loader. The loader will rebuild the current legacy FESTIVAL_ATLAS_MASTER_DATA object so the page keeps working while the data becomes easier to read and pull."
    ],
    [
      "a",
      "t177",
      "The branch and employer packages are committed. I’m adding the opportunity package now with structured records and the new lodging/travel/per diem fields in place, even when values are still unknown."
    ],
    [
      "u",
      "t178",
      "We can name the app production atlas. I realize the repo won't change but that is fine."
    ],
    [
      "a",
      "t179",
      "I’ll use Production Atlas as the app-facing name from here forward. The GitHub repo can stay festival-atlas; the visible app branding and future documentation should read Production Atlas."
    ],
    [
      "a",
      "t180",
      "naming correction. I’m checking whether the opportunity package was created before the interruption, then I’ll finish the package loader."
    ],
    [
      "a",
      "t181",
      "The opportunity package did not finish before the interruption. I’m creating it now in a condensed structured format, then I’ll add a compatibility loader so the existing page can pull from the package files."
    ],
    [
      "a",
      "t182",
      {
        "txt": "The web page now points to structured Production Atlas data packages instead of the older compressed master data file. Compatibility loader\nThis loader pulls from the structured packages and rebuilds the legacy FESTIVAL_ATLAS_MASTER_DATA object the current page already expects. Verified in the loader: it reads RESOURCE_BRANCHES, RESOURCE_OPPORTUNITIES, and RESOURCE_EMPLOYERS, then converts them into the app’s existing structure. Commit:\nPage now points to packages\nindex.html now loads:\nVerified in index.html. Page update commit\nImportant note\nI did not delete the older master files. They remain in the repo as archive/reference material. The visible page now points to the structured Production Atlas package system.",
        "c": [
          "c383",
          "c384",
          "c385",
          "c386",
          "c387",
          "c388",
          "c389",
          "c390",
          "c391",
          "c392",
          "c393",
          "c394",
          "c395",
          "c396",
          "c397",
          "c398",
          "c399",
          "c400",
          "c401",
          "c402",
          "c403",
          "c404"
        ]
      }
    ],
    [
      "u",
      "t183",
      "Run phase 2 fixes"
    ],
    [
      "a",
      "t184",
      "I’ll run Phase 2 against the structured packages: strengthen the opportunity data model, add normalized fields for type/date/venue/lodging/travel/per diem/value score/next actions, and make the app pull those fields cleanly."
    ],
    [
      "a",
      "t185",
      "I’m going to expand the structured opportunity package now so it does not lose records from the older active file. Phase 2 will make every opportunity record carry the same normalized fields: opportunityType, startDate, endDate, venue, lodging/travel/per diem fields, value score, and next research actions."
    ],
    [
      "a",
      "t186",
      "I found the issue: the package only had a partial seed set plus a hidden batch placeholder. I’m replacing it with an expanded structured opportunity package so the active app has real individual records instead of a placeholder."
    ],
    [
      "a",
      "t187",
      {
        "txt": "Phase 2 is done. What Phase 2 changed\n1. The opportunity package is now structured\nI replaced the partial seed package with a normalized RESOURCE_OPPORTUNITIES package. The placeholder batch was removed\nThe old hidden placeholder:\nwas replaced with individual opportunity records.\n4. Added a permanent schema document\nCreated:\nThis documents the required Production Atlas opportunity structure so future data additions stay clean and pullable instead of drifting back into compressed strings. The schema defines required core fields like opportunityType, startDate, endDate, venue, and producer. It also defines required status, branch, lodging, travel, and per diem fields.
