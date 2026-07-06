---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__research__RESEARCH_PROMPT_FILL_GAPS.md__chunk-0002",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/research/RESEARCH_PROMPT_FILL_GAPS.md",
  "chunk_index": 2,
  "chunk_count_for_source": 2,
  "char_start": 11395,
  "char_end": 15402,
  "source_sha256": "02aa9c46a9bf57e17209a2393141092675a7c00c1a4d0d2876aa6e03617a88d5",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

RAVEL, PER DIEM, SOURCE URL |
| `kilby-block-party-2026` | Kilby Block Party | **NO DATE**, LODGING, TRAVEL, PER DIEM, SOURCE URL |
| `sea-hear-now-2026` | Sea.Hear.Now | **NO DATE**, LODGING, TRAVEL, PER DIEM, SOURCE URL |
| `shaky-knees-2026` | Shaky Knees | **NO DATE**, LODGING, TRAVEL, PER DIEM, SOURCE URL |
| `newport-folk-2026` | Newport Folk Festival | **NO DATE**, LODGING, TRAVEL, PER DIEM |
| `newport-jazz-2026` | Newport Jazz Festival | **NO DATE**, LODGING, TRAVEL, PER DIEM, SOURCE URL |
| `sick-new-world-2026` | Sick New World | **NO DATE**, LODGING, TRAVEL, PER DIEM, SOURCE URL |
| `portola-2026` | Portola Music Festival | LODGING, TRAVEL, PER DIEM, SOURCE URL |
| `dreamville-2026` | Dreamville Festival | LODGING, TRAVEL, PER DIEM, SOURCE URL |
| `roots-picnic-2026` | Roots Picnic | LODGING, TRAVEL, PER DIEM, SOURCE URL |
| `iii-points-2026` | III Points | LODGING, TRAVEL, PER DIEM, SOURCE URL |
| `hard-summer-2026` | HARD Summer | LODGING, TRAVEL, PER DIEM, SOURCE URL |
| `beyond-wonderland-socal-2026` | Beyond Wonderland SoCal | LODGING, TRAVEL, PER DIEM, SOURCE URL |
| `railbird-2026` | Railbird Festival | LODGING, TRAVEL, PER DIEM, SOURCE URL |
| `levitate-2026` | Levitate Music Festival | LODGING, TRAVEL, PER DIEM, SOURCE URL |
| `capitol-hill-block-party-2026` | Capitol Hill Block Party | LODGING, TRAVEL, PER DIEM, SOURCE URL |
| `m3f-2026` | M3F Fest | LODGING, TRAVEL, PER DIEM, SOURCE URL |
| `lights-all-night-2026` | Lights All Night | LODGING, TRAVEL, PER DIEM, SOURCE URL |
| `countdown-nye-2026` | Countdown NYE | LODGING, TRAVEL, PER DIEM, SOURCE URL |
| `dreamstate-socal-2026` | Dreamstate SoCal | LODGING, TRAVEL, PER DIEM, SOURCE URL |

---

## Quick wins — dates only, can be confirmed fast

These 14 events are missing dates. A quick search of the official festival website or Wikipedia should confirm them. No other research needed for a first pass:

1. `louder-than-life-2026` — Louisville KY, Danny Wimmer Presents
2. `welcome-to-rockville-2026` — Daytona Beach FL, Danny Wimmer Presents
3. `sonic-temple-2026` — Columbus OH, Danny Wimmer Presents
4. `inkcarceration-2026` — Mansfield OH, Danny Wimmer Presents
5. `aftershock-2026` — Sacramento CA, Danny Wimmer Presents
6. `governors-ball-2026` — Queens NY
7. `shaky-knees-2026` — Atlanta GA
8. `bottlerock-napa-2026` — Napa CA
9. `kilby-block-party-2026` — Salt Lake City UT
10. `hinterland-2026` — St. Charles IA
11. `sea-hear-now-2026` — Asbury Park NJ
12. `newport-folk-2026` — Newport RI
13. `newport-jazz-2026` — Newport RI
14. `sick-new-world-2026` — Las Vegas NV
15. `okechobee-2026` — Okeechobee FL (verify current active status — may not be running)

---

## How to handle "I can't find it"

If public sources don't confirm a field, **do not fill it in with a guess**. Leave it as `'unknown'` or `null`. The value of this database is its accuracy, not its completeness. A yellow "research" tag in the UI is honest. A wrong green tag is not.

---

## Suggested search queries per event type

**For dates:**
`"[festival name] 2026 dates"` — check official site first, then Wikipedia, then Pollstar

**For accommodation/crew lodging:**
`"[festival name] production crew" site:reddit.com`
`"[festival name] crew housing" OR "crew camping"`
`"[festival name] vendor" site:pollstar.com`
`"[festival name] 2026" site:tpi.media OR site:mondodr.com`

**For travel comp:**
`"[production company name]" "travel" OR "per diem" site:glassdoor.com`
`"[festival name]" "crew" "travel" site:reddit.com/r/festivals`
`"[festival name] crew jobs" OR "production jobs"`

**For source URL:**
`"[festival name] 2026"` — take the Wikipedia article URL or official fest URL

---

## After research — how to update the data

Hand off findings to Claude Code with:
> "Here are the research results for [event name]. Update `data/packages/opportunities-2026.js` for id `[event-id]` with these fields: [paste output block]"

Claude will apply the update, run `npm run validate:all`, and push to the working branch.
