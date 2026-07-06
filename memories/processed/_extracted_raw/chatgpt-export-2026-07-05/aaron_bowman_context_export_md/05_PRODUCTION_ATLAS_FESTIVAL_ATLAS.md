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
