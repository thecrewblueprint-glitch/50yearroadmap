# Data Safety Policy

**Effective:** 2026-07-06  
**Last updated:** 2026-07-09  
**Scope:** All roadmap data committed to this repository and all data published by the GitHub Pages dashboard

---

## Purpose

The Deadhang Labor roadmap dashboard is public at:

https://thecrewblueprint-glitch.github.io/50yearroadmap/

This policy keeps the public roadmap business-safe, project-safe, and free of private owner, client, travel, financial, contact, or credential data.

The live dashboard is served from the **repository root** and reads `roadmap.json` directly. The current live model is the **branch/journey model** described in `AGENTS.md`.

---

## What IS allowed in public roadmap data

Allowed in `roadmap.json` and dashboard-facing files:

- Public-safe project names
- Branch names and branch roles
- General goals, blockers, and current-state summaries
- Priority levels: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`
- Work statuses: `not_started`, `in_progress`, `blocked`, `completed`
- Phase and lifecycle information
- General evidence references by file path or digest category
- Non-sensitive strategic summaries

Examples:

```text
Deadhang website SSL/security implementation
Crew Blueprint course content workflow
Production Atlas verification standards
Contractor invoice MVP scope
```

---

## What is never allowed in public roadmap data

Forbidden in `roadmap.json`, dashboard files, and presentation-facing text:

| Category | Do not include | Why |
|---|---|---|
| Contact data | phone numbers, emails, mailing addresses | privacy and spam risk |
| Financial data | bank accounts, card numbers, routing numbers, tax amounts, pay rates | security and privacy |
| Credentials | passwords, API keys, tokens, secrets | security |
| Personal identity | owner personal name, private names, personal relationships | privacy |
| Travel details | hotel names, exact routes, lodging dates, private trip details | personal security |
| Work-confidential details | private client/jobsite details, crew identities, unpublished logistics | confidentiality |
| Health/personal context | medical, mental health, DOB, family/relationship details | privacy |
| Raw memory content | direct quotes or sensitive details from archives | evidence protection |

If the information would be harmful or uncomfortable if shared publicly, it does not belong in the live roadmap.

---

## Current validation gate

Before committing any change to `roadmap.json`, run:

```bash
python3 scripts/validate-roadmap.py
```

The validator checks:

- valid JSON
- required branch/journey top-level keys
- valid branch IDs, work-item IDs, phase references, milestone references, and `this_week_focus` references
- valid enum values for branch lifecycle, phase status, milestone state, work-item priority, and work-item status
- duplicate work-item IDs
- public-safety patterns, including email, phone, SSN, card-like values, API keys, real street addresses, and HTML/angle brackets
- owner-name warnings for manual review

Exit code `0` means pass. Exit code `1` means errors were found and the change must not be committed until fixed.

---

## Human review standard

Automated checks are not enough. Before pushing public roadmap changes, review the text manually:

- Is it safe for the public dashboard?
- Is it generic enough to avoid exposing clients, contacts, travel, or finances?
- Does it avoid overstating unconfirmed strategy as decided direction?
- Does it preserve the owner as the decision-maker?
- Does it keep raw memories and curated digests as evidence instead of publishing sensitive details?

When unsure, rewrite more generally or ask the owner.

---

## Evidence and memory policy

`memories/` is immutable evidence. Do not overwrite, silently delete, or casually rewrite raw memory archives.

`data/raw-reports/` contains curated digests. Treat them as evidence summaries. Do not overwrite them to force the roadmap to say something different.

Allowed public references:

- digest file names
- general evidence categories
- high-level source descriptions

Not allowed:

- direct sensitive quotes from memory archives
- private names or contact data from memories
- financial, tax, lodging, travel, or credential details
- private client/jobsite specifics

---

## Roadmap watcher safety model

`scripts/roadmap-watcher.py` is a proposal generator for the current branch/journey model.

It:

- reads `data/raw-reports/*-digest.md`
- extracts candidate work items and blockers
- maps candidates to current branches from `roadmap.json`
- filters unsafe candidates using `data/schema/roadmap-public-safety.json`
- writes proposals to `data/roadmap/watcher-proposals.json`

It does **not** edit `roadmap.json`. The owner or agent promotes approved proposals by hand, in public-safe wording, then validates `roadmap.json`.

---

## If validation fails

Do not commit failing roadmap data.

Fix by:

1. Removing or generalizing the sensitive text.
2. Moving private detail out of the public roadmap.
3. Re-running `python3 scripts/validate-roadmap.py`.
4. Committing only after the validator passes.

No emergency override should be used for public roadmap data.

---

## Retired model warning

The old pillar/docs build flow is retired.

Do not treat these as live publication targets:

- `vision.json`
- `pillars.json`
- old `pillar_id`-keyed proposals
- `/docs` dashboard output
- `docs/roadmap.json`
- `scripts/build-roadmap.py` as a live roadmap builder

The current source of truth is root-level `roadmap.json` using the branch/journey model.
