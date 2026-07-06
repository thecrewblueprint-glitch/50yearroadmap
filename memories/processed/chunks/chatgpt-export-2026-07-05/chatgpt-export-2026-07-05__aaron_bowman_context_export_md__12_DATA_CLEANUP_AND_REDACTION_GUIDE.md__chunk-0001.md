---
{
  "chunk_id": "chatgpt-export-2026-07-05__aaron_bowman_context_export_md__12_DATA_CLEANUP_AND_REDACTION_GUIDE.md__chunk-0001",
  "archive_id": "chatgpt-export-2026-07-05",
  "archive_filename": "chatgpt-export-2026-07-05.zip",
  "source_path": "aaron_bowman_context_export_md/12_DATA_CLEANUP_AND_REDACTION_GUIDE.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 1264,
  "source_sha256": "056223058ffc7ed8bf334105763f4010dd40a4c26b71bdbee9f8b85586040047",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

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
