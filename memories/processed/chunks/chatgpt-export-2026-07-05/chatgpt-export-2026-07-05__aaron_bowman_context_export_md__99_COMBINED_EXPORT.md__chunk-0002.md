---
{
  "chunk_id": "chatgpt-export-2026-07-05__aaron_bowman_context_export_md__99_COMBINED_EXPORT.md__chunk-0002",
  "archive_id": "chatgpt-export-2026-07-05",
  "archive_filename": "chatgpt-export-2026-07-05.zip",
  "source_path": "aaron_bowman_context_export_md/99_COMBINED_EXPORT.md",
  "chunk_index": 2,
  "chunk_count_for_source": 3,
  "char_start": 11383,
  "char_end": 23352,
  "source_sha256": "8084e827df42c64c5fa1d16548343be09d89d960e37221bc7750a0acfe58afbd",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

rs

## Course 1

Known title:

**Stagehand Fundamentals: How to Work Your First Load-In, Show Call, and Load-Out**

Core structure:

- initially 10 modules
- later references to an 83-lesson outline
- end-of-module quizzes
- quiz pass threshold: 80%
- retakes allowed

## Lesson Structure

Canonical lesson blocks:

- In This Lesson You Will Learn
- Short Answer
- What This Looks Like on a Call
- Beginner Mistakes
- Professional Habit
- Key Takeaway

Later additions:

- Safety Notes
- Reflection Questions
- Key Takeaways styled box

## Safety / Compliance Positioning

Important language rules:

- The course is orientation/job-readiness, not certification.
- Specialized work requires proper training and employer authorization.
- Safety disclaimer should appear on relevant pages.
- Avoid OSHA certification claims unless authorized.
- Do not issue unauthorized certificates.

## LMS / Technical History

Earlier WordPress/LMS context:

- thecrewblueprint.com via IONOS / WordPress Grow
- theme: Extendable
- plugins included Crew Blueprint Core, Site Shell, LMS, Resource Hub, Safety Notices
- LMS used shortcode and JSON-based workflows
- direct-fetch split JSON consumer was tested
- Module files included manifest, lessons, and quiz JSON

Split JSON model:

- `module-XX-manifest.json`
- `module-XX-lessons.json`
- `module-XX-quiz.json`

Important later decision:

- Aaron disabled the LMS completely on 2026-06-11.
- Reason: display/transfer pattern did not preserve written course packet flow.
- Direction shifted toward content creation workflow first.
- Robust LMS rebuild paused.
- Create/store course packets now; build simpler MVP display later.

## Content Creation Workflow

Original workflow:

1. Gemini asks for/reframes a topic.
2. ChatGPT / Course Studio creates core structure or lesson outline.
3. Claude creates Research Guide with core subjects and key topics.
4. ChatGPT Scholar researches key topics and compiles packets.
5. Claude drafts full lesson.
6. Manus proofreads and reviews scoring system.
7. Claude finalizes revisions and generates `.docx`.

Updated decision:

- Aaron approved the revised workflow previously provided by ChatGPT.
- Manus can be used temporarily until access ends.
- Alternatives such as DeepSearch/Qwen/Meta Llama were mentioned for later.

## Brand / Visual System

Approved direction:

- Dark industrial training-platform look.
- Near-black / charcoal backgrounds.
- Industrial yellow/gold and amber accents.
- White/off-white body text.
- Muted gray secondary text.
- Subtle borders and shadows.
- Condensed/industrial headings.
- Clean readable body.
- Mobile-first layout.

Known color references:

- Background: `#050708`
- Panel: `#0e1216`
- Card: `#151a20`
- Gold: `#f5b400`
- Amber: `#ffcf3a`
- Text: `#f4f6f8`
- Muted: `#b7bec6`

Avoid:

- generic school look
- white pages
- cluttered dashboard
- tiny mobile text
- neon
- gaming-site look
- rewriting lesson content without permission

## Pages / Legal Content

Additional pages requested:

- Accessibility
- Affiliate Disclosure
- Cookies Disclaimer
- Limitation of Liability
- Privacy policy / cookie compliance content


<!-- END 04_THE_CREW_BLUEPRINT.md -->


---

<!-- BEGIN 05_PRODUCTION_ATLAS_FESTIVAL_ATLAS.md -->

# Production Atlas / Festival Atlas

## Project Identity

Production Atlas / Festival Atlas is a public-safe scouting dashboard for live-event production workers.

Audience:

- stagehands
- riggers
- audio crew
- lighting crew
- video crew
- staging/carpentry workers
- traveling 1099 live-event contractors

Purpose:

- find festivals, venues, producers, and production routes worth researching for work
- identify public application paths and vendor routes
- understand rough event timing and production opportunity windows
- avoid private, unsafe, or rumor-based data

Known repo:

- GitHub: `thecrewblueprint-glitch/festival-atlas`
- Active branch previously referenced: `research-version`
- Stable branch/main should remain frozen unless explicitly instructed.

## Public-Safe Research Rules

Do not include:

- private contacts
- phone numbers
- personal emails
- pay rates
- hotel/lodging details
- rumors
- login-only information
- copied scraped text

Focus on:

1. crew lodging / camping / accommodation signals
2. travel / per diem / mileage / housing support signals
3. labor and staffing routes
4. IATSE/local jurisdiction verification language
5. public production vendor stack

If not publicly confirmed, use:

> Unknown publicly. Human verification needed.

Use “possible” only when the pattern is strong but not directly confirmed.

## Research Handoff Improvements

Known revisions made to the research handoff:

- Add event status.
- Add event dates: load-in start, show dates, strike end, total days on site.
- Add per-event `lastVerified`.
- Add `not_applicable` status.
- Add rubric for `possible`.
- Add `evidenceLevel` for sources.
- Split site ops and power.
- Add `other` vendor department.
- Add advanced search operators.
- Add `unknownsList`.
- Add human verification protocol.
- Document scoring methodology.
- Define public-safe sources positively.

## Batch 1 Research Context

Danny Wimmer Presents / Batch 1 included:

- Louder Than Life
- Bourbon & Beyond
- Welcome to Rockville
- Sonic Temple
- Aftershock
- Inkcarceration

Known research result pattern:

- Brown Note Productions confirmed/identified as key audio vendor pattern across DWP festivals in public sources.
- Crew lodging and travel support mostly unknown publicly.
- Labor routes mostly require human verification.
- Non-audio vendor stacks were usually partial/unknown.

## Research Plan Problem Identified

Public production crew data is thin. Many sources are attendee-facing.

Observed issue:

- festivals publish attendee camping, lineups, tickets, travel packages, and accessibility information
- they rarely publish production crew logistics, travel, per diem, or full vendor stack

Recommended better approach:

- public-source research for vendor stacks, IATSE jurisdiction language, producer patterns
- structured unknown fields for human verification
- prioritize high-value events and lodging-sensitive remote festivals
- build an assisted human-verification tool/workflow later

## Public Search/UI Simplification

Aaron wants the public search/filter UI limited to:

- date
- producer

Remove or hide other public search dimensions because they are not useful enough.

Future feature idea:

- schedule-planning feature where users enter desired availability/schedule
- see where events fit across the year
- link to map
- show projected travel distances, travel times, and required locations together

## Roadmap / Task Navigation Requirement

Aaron wants a roadmap/task framework with:

- linear progression of how work should move forward
- a “you are now here” jumper that jumps directly to the point where the roadmap is completed through
- ability to mark tasks as “move to later”
- moved-later tasks should remain in the system without derailing the primary linear path
- goal: prevent chasing too many ideas while half-finished projects get forgotten


<!-- END 05_PRODUCTION_ATLAS_FESTIVAL_ATLAS.md -->


---

<!-- BEGIN 06_TECHNICAL_PROJECTS_AND_APPS.md -->

# Technical Projects and Apps

## Custom Invoice Generator

Known requested framework:

- custom invoice generator
- links to payment processor
- links to bank account
- likely integrations discussed: Stripe and Plaid
- output should include comprehensive architecture and step-by-step build guide
- security concerns: do not store raw card data; use processor-hosted/PCI-safer flows; encrypt banking tokens; use webhook verification and idempotency

Aaron later preferred:

- Android-only invoice app
- offline capability
- static invoice
- fixed positions
- paste text mapped into fields
- PDF only
- no drag/click builder

## 365-Day Affirmation Calendar App

Known context:

- app creates 365 all-day calendar events
- integrates with Google Calendar
- uses OAuth token refresh
- scheduler / APScheduler concepts were discussed
- background sync, token health checks, and calendar event creation were discussed

Important technical points from pasted handoff material:

- `GoogleCalendarService` should refresh tokens automatically before API calls.
- Stored refresh token and expiry need safe handling.
- Background tasks should not reuse request-scoped DB sessions.
- Scheduler should have graceful shutdown and prevent overlapping jobs.
- Sync should include duplicate prevention and retry handling.

## Private Task App

Known desired features:

- single-user private task app
- secure backend
- OpenRouter.ai or AI backend support
- task cleanup
- priority sorting
- risk flagging
- breaking tasks into steps
- daily plan generation
- API keys server-side only
- potential migration of reminders/tasks into this app later

## Database / Backend Ideas

Known discussions:

- backend apps can use AI
- sensitive business documents in an admin dashboard require secure design
- file/image upload to notes may be useful
- login/local upload/security concerns exist
- AWS Aurora/RDS/EC2 and database connection steps were discussed
- Laravel/RAG via cPanel was considered for long-term sturdy systems

## GitHub Workflow Context

Known preference:

- user often wants complete replacement files/packages, not snippets
- user does not want half-copies or “inject this into another piece”
- user wants full copy/paste-ready or downloadable artifacts

Repo references:

- `festival-atlas`
- `thecrewblueprint-glitch/festival-atlas`
- active branch often `research-version`
- stable `main` should not be touched unless explicitly requested

Important boundary:

- No repo changes should be made unless Aaron explicitly asks for that exact repo operation.


<!-- END 06_TECHNICAL_PROJECTS_AND_APPS.md -->


---

<!-- BEGIN 07_ACTIVE_LOGS_REMINDERS_AND_TRACKING.md -->

# Active Logs, Reminders, and Tracking

## Michigan Trip / Festival Run Hour Log

Known entries and corrections:

- June 22, 2026: 10 hours worked with ARS. Notes: did a few rigging tasks and ran their motors for 2 of those hours.
- June 23, 2026: 9 hours worked.
- June 24, 2026: 10 hours worked.
- Last 5-day update interpreted as June 24–28, 2026 unless corrected:
  - four days with 5 overtime hours each
  - one day with 2 regular hours and 5 overtime hours
  - total added in that update: 22 hours, including 20 overtime and 2 regular
- June 29, 2026: 10 hours worked.
- June 30, 2026: 10 hours worked.
- July 1, 2026: 10 hours worked.
- July 2, 2026: 10 hours worked.
- Correction: June 28, 2026 was the only day off.
- Correction: July 2, 2026 was the last day worked.
- Correction: July 3, 2026 should not be counted as a worked day, replacing a previous July 3 final-day entry.

## Website / Business Active Items

Current/deprioritized state based on stored context:

- Deadhang Labor LLC business email works.
- Remove/deprioritize email/Gmail send-as troubleshooting unless reopened.
- Only remaining Deadhang website/cPanel project: SSL/security.
- Portfolio cleanup, image/caption organization, sitemap/page updates, and email setup were removed/deprioritized from active tracking.

## Open Business/Admin Items

Previously active/unresolved:

- insurance provider selection
- OSHA training/provider selection
- invoice app/system finalization
- business document organization
- tax debt/monthly tax payment reminders
- website MVP error review

## Travel / Work Context

Known recent travel/work context included:

- Electric Forest / Michigan festival run
- Crew One schedules and Electric Forest work emails
- Grand Rapids/Rodeway Inn travel/stay references
- possible future work travel mentions around Country Thunder, Elements, and Rock The Country

These contain sensitive jobsite and travel details. Review before sharing.


<!-- END 07_ACTIVE_LOGS_REMINDERS_AND_TRACKING.md -->


---

<!-- BEGIN 08_PREFERENCES_CONSTRAINTS_AND_OPERATING_RULES.md -->

