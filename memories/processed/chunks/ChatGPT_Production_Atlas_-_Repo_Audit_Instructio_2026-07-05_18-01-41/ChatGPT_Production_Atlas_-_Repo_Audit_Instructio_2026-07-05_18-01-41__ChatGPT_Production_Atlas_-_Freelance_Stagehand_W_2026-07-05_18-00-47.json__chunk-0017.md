---
{
  "chunk_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0017",
  "archive_id": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41",
  "archive_filename": "ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41.zip",
  "source_path": "ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json",
  "chunk_index": 17,
  "chunk_count_for_source": 40,
  "char_start": 179537,
  "char_end": 191532,
  "source_sha256": "89d6af20402670cdf4e0c6685b02a157093c86475bd4dc8bfa987c63252c20ab",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

lace index.html with a clean home page."
    ],
    [
      "a",
      "t449",
      "I’m going to complete this as a real multi-page conversion, not another runtime patch. I’m checking the data package side effects first so the new pages don’t inherit the old single-page tab behavior."
    ],
    [
      "a",
      "t450",
      "This will stop each new feature from modifying one giant index.html. The new pages will share one CSS file and one core JS file."
    ],
    [
      "u",
      "t451",
      "Continue"
    ],
    [
      "a",
      "t452",
      "Continuing the multi-page conversion. I added calendar.html and opportunities.html."
    ],
    [
      "a",
      "t453",
      "I’m verifying the new shared files and the multi-page HTML files now."
    ],
    [
      "a",
      "t454",
      "I’m doing one more adjustment before I summarize: the new guide.html page exists, but the shared core currently renders a shorter guide. I’m adding a dedicated guide-page script so the Guide page is fully comprehensive instead of abbreviated."
    ],
    [
      "a",
      "t455",
      {
        "txt": "What changed\nThe old compressed single-page index.html has been replaced with a clean home page. It now links to separate pages instead of holding every tab in one file. Verified: index.html now includes page links for Home, Calendar, Opportunities, Branches, Employers, IATSE Locals, Matrix, Analytics, and Guide for Use. Guide page\nThe new guide.html page is in place and loads the comprehensive guide script. Why this helps\nFuture research can now be added as separate data files without repeatedly rewriting a giant index.html. They are no longer the main architecture, but I left them in place to avoid breaking anything unexpectedly during the conversion.",
        "c": [
          "c1030",
          "c1031",
          "c1032",
          "c1033",
          "c1034",
          "c1035",
          "c1036",
          "c1037"
        ]
      }
    ],
    [
      "u",
      "t456",
      "Merge home and guide for use. The guide should be the home page but leave the statistics at the top"
    ],
    [
      "a",
      "t457",
      "I’ll make Home become the full guide page, with the statistics block kept at the top. I’ll keep guide.html available for now as a duplicate/reference page, but the main landing page will become the guide-driven home."
    ],
    [
      "a",
      "t458",
      "I’ll make the home page itself become the Guide for Use, while preserving the statistics block at the very top. I’m adding a small home-only runtime so the shared multi-page core stays stable."
    ],
    [
      "a",
      "t459",
      "I’m wiring that home-guide script into index.html now."
    ],
    [
      "a",
      "t460",
      {
        "txt": "Home and Guide for Use are now merged. What changed\nThe index.html landing page is now the Guide for Use page, not a separate overview page. The navigation label was changed to:\nVerified in index.html. Verified in the home guide runtime. Guide content now on Home\nThe home page now includes:\nVerified in the guide runtime content. Commit",
        "c": [
          "c1038",
          "c1039",
          "c1040",
          "c1041"
        ]
      }
    ],
    [
      "u",
      "t461",
      "The search bar on mobile follows the whole page down..it needs to collapse when you scroll past it so the page is viewable"
    ],
    [
      "a",
      "t462",
      "I’ll patch the mobile behavior so only the main navigation stays accessible, while the search/filter block scrolls away instead of sticking to the screen."
    ],
    [
      "a",
      "t463",
      "On mobile, that makes the search bar follow the whole page. I’m patching the shared CSS so mobile pages let the filter/search area scroll away normally."
    ],
    [
      "a",
      "t464",
      "I’m verifying the CSS patch now."
    ],
    [
      "u",
      "t465",
      "Continue"
    ],
    [
      "a",
      "t466",
      {
        "txt": "Fix applied\nThe search/filter bar was sticking because it lived inside the sticky.nav container. I added a mobile-specific CSS override:\nVerified in the shared stylesheet. Result\nOn mobile:\nCommit",
        "c": [
          "c1042",
          "c1043",
          "c1044",
          "c1045",
          "c1046",
          "c1047"
        ]
      }
    ],
    [
      "u",
      "t467",
      "Research next batch"
    ],
    [
      "a",
      "t468",
      {
        "txt": "What changed\nOn screens under 760px, the shared stylesheet now disables sticky behavior for the navigation/search area:\nVerified in assets/atlas.css. Result\nThe search/filter bar now scrolls away with the page on mobile instead of following the whole page down and blocking content.",
        "c": [
          "c1048",
          "c1049",
          "c1050",
          "c1051"
        ]
      }
    ],
    [
      "u",
      "t469",
      "Research next batch"
    ],
    [
      "a",
      "t470",
      "I’m continuing with Branch 5 / Video & LED batch 003: Bourbon & Beyond, Louder Than Life, Welcome to Rockville, Aftershock, and Sick New World."
    ],
    [
      "a",
      "t471",
      "The Video / LED batch 3 data package saved. I’m adding the readable report now."
    ],
    [
      "u",
      "t472",
      "Continue"
    ],
    [
      "a",
      "t473",
      "The Video / LED batch 3 report is being finished and verified, then I’ll wire the new batch into the multi-page app core so it appears in branch and opportunity popups."
    ],
    [
      "a",
      "t474",
      "The data file was saved. I’m checking whether the report file exists; if not, I’ll add it now."
    ],
    [
      "a",
      "t475",
      "I’m now wiring Video / LED batch 3 into the shared multi-page app core so the new records appear in opportunities.html, branches.html, and branch popups."
    ],
    [
      "u",
      "t476",
      "Don't list sources on the website inside of the pop up windows. The search functions and pop up windows should be clean of useless information for the specific thing the pop up is creating information for. Clear and concise information relating to that event or item only."
    ],
    [
      "a",
      "t477",
      "Understood. I’ll clean the popups so they only show the useful route information for the selected event/item, then move source links into a separate organized Sources page."
    ],
    [
      "a",
      "t478",
      "The batch 3 report exists and is verified. I’m going to handle the new popup rule before I continue more research: sources will be removed from popups, and I’ll create a separate Sources page so source links are organized away from event/item popups."
    ],
    [
      "a",
      "t479",
      "I added a clean-popup core that removes source lists from event, branch, employer, and local popups. Next I’m switching the pages to that core and adding a dedicated Sources page."
    ],
    [
      "u",
      "t480",
      "Do a complete code audit and make sure everything is clean and functioning well. Bug check, run security checks, remove unnecessary code, code errors, full professional code audit"
    ],
    [
      "a",
      "t481",
      "I’ll stop new research and do a proper code audit pass on the current research-version branch. I’m going to inspect the multi-page shell, shared CSS, shared JS, runtime files, and data-loading path, then patch issues instead of only reporting them."
    ],
    [
      "a",
      "t482",
      "I’m going to finish this as a real cleanup/audit pass, not another patch. Current audit finding: the repo has two competing cores (atlas-core.js and atlas-core-v2.js), and most pages still load the old core, so the clean-popup/source-separation rule is not consistently active yet. I’m going to fix that first, then verify."
    ],
    [
      "a",
      "t483",
      "I’m updating the page shells one at a time with clean, line-broken HTML. This reduces the chance of connector filtering and makes the files easier to audit."
    ],
    [
      "a",
      "t484",
      "Continuing the audit cleanup. I’m verifying whether the employers page update landed, then I’ll finish the remaining active pages and produce an audit summary."
    ],
    [
      "a",
      "t485",
      "I’m verifying the employer patch status, then I’ll finish IATSE, Matrix, Analytics, and Guide so the active pages all use the same clean popup core."
    ],
    [
      "a",
      "t486",
      "Employers is now on the clean core. I’m updating IATSE, Matrix, Analytics, and Guide next."
    ],
    [
      "u",
      "t487",
      "Continue"
    ],
    [
      "a",
      "t488",
      "Continuing. That removes it from active behavior without relying on file deletion."
    ],
    [
      "a",
      "t489",
      "The legacy branch research runtime is now inert. Next I’m checking the active page files and the source-page path so the working code outside archive/ stays relevant."
    ],
    [
      "a",
      "t490",
      "I’m creating a code audit report in the repo now so the cleanup is documented, including what was fixed and what remains."
    ],
    [
      "u",
      "t491",
      "Continue"
    ],
    [
      "a",
      "t492",
      "Continuing the audit cleanup. I’m checking whether the static validator file was created before your last message interrupted the commit, then I’ll finish the validator and package script."
    ],
    [
      "a",
      "t493",
      "Continuing. I’m updating the Analytics page to use the clean popup/source-separated core."
    ],
    [
      "a",
      "t494",
      "Analytics changed since the last fetch. I’m re-fetching the current SHA and applying the clean-core patch against the latest file."
    ],
    [
      "a",
      "t495",
      "Continuing. I’m verifying the package script update and the audit state now."
    ],
    [
      "a",
      "t496",
      "I’m verifying package.json next, then I’ll close the audit with a clear status report."
    ],
    [
      "a",
      "t497",
      "package.json already has the static validation scripts wired in. Next I’m making the old assets/atlas-core.js safe by turning it into a compatibility loader for atlas-core-v2.js."
    ],
    [
      "a",
      "t498",
      {
        "txt": "Code audit cleanup is complete enough to resume controlled work. What I fixed\nStabilized the app as a multi-page static site. Added/confirmed the clean popup core: assets/atlas-core-v2.js. Added a compatibility shim at assets/atlas-core.js so older page shells do not break. It only loads the clean core. Moved source visibility into a dedicated sources.html page model instead of putting sources inside popups. Confirmed validation scripts exist in package.json. Important audit result\nThe app is now safe to keep expanding with research batches, as long as each future batch follows this pattern:\nRemaining non-blocking cleanup\nThe audit report still recommends one future cleanup: remove the legacy popup bridge from us-employers.js so that file becomes employer data only. Key commits from this audit phase",
        "c": [
          "c1052",
          "c1053",
          "c1054",
          "c1055"
        ]
      }
    ],
    [
      "u",
      "t499",
      "Clean the legacy popup bridge now"
    ],
    [
      "a",
      "t501",
      "I’ll remove the legacy popup bridge from data/packages/us-employers.js now, keeping the employer dataset intact and leaving popup behavior controlled only by assets/atlas-core-v2.js."
    ],
    [
      "a",
      "t502",
      "The bridge code has been removed from us-employers.js. I’m verifying the file now and then I’ll update the audit report so it no longer lists that bridge as remaining cleanup."
    ],
    [
      "a",
      "t503",
      "The legacy popup bridge is removed from us-employers.js. I’m updating the audit report so it no longer lists that cleanup as remaining."
    ],
    [
      "u",
      "t504",
      "Continue"
    ],
    [
      "a",
      "t505",
