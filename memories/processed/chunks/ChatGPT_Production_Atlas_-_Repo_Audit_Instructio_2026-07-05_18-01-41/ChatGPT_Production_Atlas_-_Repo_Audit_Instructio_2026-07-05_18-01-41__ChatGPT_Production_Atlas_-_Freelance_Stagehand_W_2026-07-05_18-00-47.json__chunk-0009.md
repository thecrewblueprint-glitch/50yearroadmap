---
{
  "chunk_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0009",
  "archive_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41",
  "archive_filename": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41.zip",
  "source_path": "ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json",
  "chunk_index": 9,
  "chunk_count_for_source": 40,
  "char_start": 89696,
  "char_end": 101691,
  "source_sha256": "89d6af20402670cdf4e0c6685b02a157093c86475bd4dc8bfa987c63252c20ab",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

ed\nI replaced the partial seed package with a normalized RESOURCE_OPPORTUNITIES package. The placeholder batch was removed\nThe old hidden placeholder:\nwas replaced with individual opportunity records.\n4. Added a permanent schema document\nCreated:\nThis documents the required Production Atlas opportunity structure so future data additions stay clean and pullable instead of drifting back into compressed strings. The schema defines required core fields like opportunityType, startDate, endDate, venue, and producer. It also defines required status, branch, lodging, travel, and per diem fields. Commits\nCurrent state\nProduction Atlas now has a proper structured opportunity data layer. The next phase is UI/card work: displaying lodging, travel, per diem, opportunity type, and value score more in the calendar and opportunity profile cards.",
        "c": [
          "c405",
          "c406",
          "c407",
          "c408",
          "c409",
          "c410",
          "c411",
          "c412"
        ]
      }
    ],
    [
      "u",
      "t188",
      "Some of the information for my line of work is not easily accessible to the public. What can we do about that?"
    ],
    [
      "a",
      "t189",
      {
        "txt": "Yes. A lot of production labor information is relationship-based, word-of-mouth, buried in vendor networks, or only visible after you have worked a call. That does not kill the app. Main rule\nProduction Atlas should not pretend unknown information is public or verified. What we can do\n1. Separate public data from private data\nBecause the repo/site may be public, we should not put sensitive working intel into the public GitHub Pages app. Add confidence levels\nEach claim should have a confidence label. Example:\nThis is better than leaving fields blank.\n4. Track “how to find the answer”\nWhen public information does not exist, the app should tell us the next research method. Example methods:\nSo instead of saying “unknown,” the database says:\n5. It lets us use field knowledge safely.\n6. Add a “Needs Human Verification” queue\nSome things AI and public search will not solve. The app should have a tab like:\nExamples:\nThis turns the app into a real scouting workflow, not a public-data scraper.\n7. Use “private notes” carefully\nPrivate notes should be written like this:\nAvoid storing:\nThe app should help you remember patterns, not expose people. Best structure going forward\nFor each opportunity, add this block:\nAnd this:\nIn the public version, we only show:\nPrivate notes stay hidden.",
        "c": [
          "c413",
          "c414",
          "c415",
          "c416",
          "c417",
          "c418",
          "c419",
          "c420",
          "c421",
          "c422",
          "c423",
          "c424",
          "c425",
          "c426",
          "c427",
          "c428",
          "c429",
          "c430",
          "c431",
          "c432",
          "c433",
          "c434",
          "c435",
          "c436",
          "c437",
          "c438",
          "c439",
          "c440",
          "c441",
          "c442",
          "c443",
          "c444",
          "c445",
          "c446"
        ]
      }
    ],
    [
      "u",
      "t190",
      "Go ahead and make these changes"
    ],
    [
      "a",
      "t191",
      "I’ll add the intelligence classification layer now: source type, visibility, confidence, research status, field-intel placeholders, human verification flags, and public/private safety separation. Then I’ll surface the safe parts in the app without exposing private notes."
    ],
    [
      "a",
      "t192",
      "I’ll patch three files: the opportunity package defaults, the loader pass-through fields, and the schema documentation. Then I’ll verify the fields landed."
    ],
    [
      "a",
      "t193",
      "I’m applying this as a loader-level upgrade so we do not have to rewrite every opportunity record manually. The loader will add safe defaults to every record and pass the classification fields through to the app."
    ],
    [
      "a",
      "t194",
      {
        "txt": "Private-data separation\nCreated:\nThis schema documents the rule that Production Atlas must separate public evidence from field intelligence, and the public app must not publish sensitive/private details. New schema fields\nThe schema defines:\nVerified in the schema. It also defines the research-status block:\nVerified in the schema. Intelligence buckets added\nThe schema now defines these buckets:\nVerified in the schema. Commits\nThe app can now safely handle public information and private/field intelligence without mixing them.",
        "c": [
          "c447",
          "c448",
          "c449",
          "c450",
          "c451",
          "c452",
          "c453",
          "c454",
          "c455",
          "c456",
          "c457",
          "c458",
          "c459",
          "c460",
          "c461",
          "c462",
          "c463",
          "c464"
        ]
      }
    ],
    [
      "u",
      "t195",
      "Do a code audit. Make sure everything so far is working how it was intended to. Fix bugs. Remove or rewrite code that only patches other code, so that is it clean and functional without extra bulk code"
    ],
    [
      "a",
      "t196",
      "I’ll audit the current research-version code path, then patch only what should remain part of the long-term Production Atlas structure. I’ll remove compatibility/patch logic where it is no longer needed and keep the repo archive files intact."
    ],
    [
      "a",
      "t197",
      "I’m refactoring the app now so it reads directly from the structured Production Atlas packages. This removes the legacy compatibility loader from the active page and cleans the remaining festival-named functions/IDs from the UI code path."
    ],
    [
      "a",
      "t198",
      "I found the main cleanup target: index.html still depends on the compatibility loader. I’m replacing it with a direct Production Atlas implementation and then deleting the loader file from the active branch."
    ],
    [
      "a",
      "t199",
      {
        "txt": "Code audit and cleanup are complete. Removed the compatibility loader from the active app\nindex.html no longer loads:\nIt now reads directly from the structured packages:\nVerified in the active page.\n2. Deleted obsolete patch file\nRemoved:\nCommit:\n3. Cleaned active app internals\nThe page now uses cleaner active concepts:\ninstead of relying on the old festival master-data object. Verified in index.html.\n4. Preserved safety logic\nThe active opportunity array now filters out records marked:\nVerified in index.html.\n5. Preserved intelligence classification\nThe page now applies public-safe classification directly inside the active code path:\nVerified in index.html.\n6. Improved displayed opportunity cards\nOpportunity cards now show:\nVerified in index.html.\n7. Cleaned modal profile behavior\nOpportunity profiles now show:\nVerified in index.html. Audit record added\nCreated:\nCommit:\nMain cleanup commit\nCurrent status\nThe active app is now cleaner:\nRemaining next build items:",
        "c": [
          "c465",
          "c466",
          "c467",
          "c468",
          "c469",
          "c470",
          "c471",
          "c472",
          "c473",
          "c474",
          "c475",
          "c476",
          "c477",
          "c478",
          "c479",
          "c480",
          "c481",
          "c482",
          "c483",
          "c484",
          "c485",
          "c486",
          "c487",
          "c488",
          "c489",
          "c490",
          "c491",
          "c492",
          "c493",
          "c494"
        ]
      }
    ],
    [
      "u",
      "t200",
      "Remove the empty homepage fallback tag inside the employer matrix"
    ],
    [
      "a",
      "t201",
      "I’ll remove the fallback-status chip from the employer matrix/cards where it is visual clutter, while keeping valid homepage/career links clickable."
    ],
    [
      "a",
      "t202",
      "I’m checking the employer rendering path now and will remove the status chip that displays homepage_fallback, while preserving the actual link."
    ],
    [
      "a",
      "t203",
      "I’m verifying the employer card and matrix code now to confirm the fallback status chip is gone."
    ],
    [
      "a",
      "t204",
      {
        "txt": "Removed\nThe employer display no longer renders the extra status chip:\nWhat changed\nEmployer cards\nBefore, each employer card showed:\nNow it only shows the useful link:\nVerified in index.html. Commit",
        "c": [
          "c495",
          "c496",
          "c497",
          "c498",
          "c499",
          "c500",
          "c501",
          "c502"
        ]
      }
    ],
    [
      "u",
      "t205",
      "Remove visual clutter from all parts of the site. If the links or information in a section doesn't help with the end goal of finding gigs to fill time slots in the scheduling of my work year it isn't needed to be put into the visual space of the public facing app"
    ],
    [
      "a",
      "t206",
      "I’ll simplify the public-facing app around the actual decision: “Can this help fill a work-year time slot?” I’ll remove public UI sections that are more like internal research structure, keep the data packages intact, and leave only the views that help you scout opportunities, employer routes, and local-union paths."
    ],
    [
      "a",
      "t207",
      "I’ll strip the public UI down to work-year scouting essentials: calendar, opportunity profiles, employer routes, and local-union lookup. I’ll keep the data and internal research structure in the packages, but remove public visual sections that do not directly help identify gigs or fill schedule gaps."
    ],
    [
      "a",
      "t208",
      "I’m verifying the simplified public-facing UI now."
    ],
    [
      "a",
      "t209",
      {
        "txt": "Public visual clutter removed\nThe public-facing app now only has four views:\nRemoved from the public visual space:\nVerified in index.html. Visual purpose narrowed\nThe public UI now centers on:\nOpportunity cards now show only decision-useful information. Commit",
        "c": [
          "c503",
          "c504",
          "c505",
          "c506",
          "c507",
          "c508",
          "c509",
          "c510",
          "c511",
          "c512"
        ]
      }
    ],
    [
      "u",
      "t210",
      "Revert that last update"
    ],
    [
      "a",
      "t211",
      "I’ll revert only the last public-UI simplification update and restore the version immediately before it. The homepage fallback tag removal will remain, because that was the commit before the last one."
    ],
    [
      "a",
      "t212",
      "I’ll restore index.html from the commit immediately before the last simplification change: 253f46a2d99d3cce67675239a2431a86be6e4515."
    ],
    [
      "a",
      "t213",
      "I’m verifying that the full tab set and matrix/analytics sections are restored."
    ],
    [
      "a",
      "t214",
      {
        "txt": "Restored\nThe app is back to the version immediately before the simplification pass, including:\nVerified in index.html. Preserved\nThe previous fix that removed the empty homepage_fallback status chip remains intact.",
        "c": [
          "c513",
          "c514",
          "c515",
          "c516"
        ]
      }
    ],
    [
      "u",
      "t215",
      "What is the best way to raise the value scores for these opportunities?"
    ],
    [
      "a",
      "t216",
      {
        "txt": "The best way to raise value scores is not to manually inflate them. Production Atlas should treat the score as a work-year usefulness score, not an event popularity score. Suggested score impact:\n2. Paid travel / mileage / flights\nExamples:\nSuggested score impact:\n3. Per diem\nExamples:\nSuggested score impact:\n4.
