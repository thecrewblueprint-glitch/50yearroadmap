# Data Cleanup and Redaction Guide

## Safe for Public Repo After Review

Usually safe to share after light review:

- general project descriptions
- brand guidelines
- non-sensitive roadmap structure
- public-safe research methodology
- code architecture notes
- generic technical handoff prompts
- UI/UX preferences with no personal data

## Needs Redaction Before Public Repo

Remove or redact:

- phone numbers
- emails
- home addresses
- DOB
- banking references
- payment card/account suffixes
- hotel bookings
- membership numbers
- private jobsite logistics
- personal travel records
- third-party names/contact details
- exact work schedules if not intended for publication

## Strongly Private

Keep private unless there is a specific reason:

- Gmail/account signals
- financial account details
- travel bookings
- identity documents
- W-9/signature files
- personal profile maps
- medical/mental health details
- business banking/tax details

## Recommended Repo Strategy

If adding documentation to a repo:

1. Create `docs/context/README.md`.
2. Create public-safe project docs only.
3. Keep personal data in a private repo or encrypted archive.
4. Do not commit this full export to a public repo.
5. Use a sanitized derivative for AI-agent handoff.
