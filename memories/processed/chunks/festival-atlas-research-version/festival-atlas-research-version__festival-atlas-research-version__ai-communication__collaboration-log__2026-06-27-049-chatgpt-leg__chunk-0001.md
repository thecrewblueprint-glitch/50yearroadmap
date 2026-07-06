---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__collaboration-log__2026-06-27-049-chatgpt-leg__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/collaboration-log/2026-06-27-049-chatgpt-legal-footer-pages.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 1930,
  "source_sha256": "62f642c6da378b2a503e1463ed3079150cf9caaa0b522eaf68505cc0235b12a5",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Collaboration Log Entry — Legal Footer Pages

Status: incomplete
Created: 2026-06-27
Review after: 2026-07-11
Assistant: ChatGPT
Branch: research-version
Commit: d810b62

## Files added

```text
privacy-policy.html
terms-and-conditions.html
limitation-of-liability.html
cookie-notice.html
accessibility.html
affiliate-disclosure.html
contact-data-requests.html
```

## Files updated

```text
assets/site-footer.js
```

## What changed

Aaron requested that the global footer include legal pages such as Privacy Policy, Terms & Conditions, Limitation of Liability, and any other pages needed for legal compliance and information collection.

## Legal footer links added

The global footer now includes a Legal section with:

```text
Privacy Policy
Terms & Conditions
Limitation of Liability
Cookie Notice
Accessibility Statement
Affiliate Disclosure
Contact & Data Requests
```

## Static app assumptions reflected in page copy

The legal pages are written for the current public static app boundary:

```text
No login
No public visitor accounts
No backend database for public visitors
No payment processing
No intentional collection of names, phone numbers, emails, or private employment information through the app
Some browser-local planning data may be stored locally on the visitor's device
External links have their own privacy practices and terms
```

## Important note

These pages are public-facing baseline legal/compliance copy for the static app. They should be reviewed by a qualified attorney before being treated as final legal advice or relied on as complete compliance coverage.

## Validation status

Validation not run; connector session cannot run local repo validation.

Required next command:

```bash
npm run validate:all
```

## Next action

Validate, wait for GitHub Pages deploy, then hard refresh several public pages and confirm the footer shows the Legal section and each legal page opens correctly.
