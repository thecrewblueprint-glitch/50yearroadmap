---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__2026-06-29-chatgpt-full-repo-audit.md__chunk-0002",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/2026-06-29-chatgpt-full-repo-audit.md",
  "chunk_index": 2,
  "chunk_count_for_source": 2,
  "char_start": 11377,
  "char_end": 15047,
  "source_sha256": "9d666258131e49bd2c5b5b779835714fc2a7b50cde55ce14fa134a1a8d4da13c",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

, Sources, and Branches from header nav after page load. This protects pages that still have stale nav, but it also hides document drift by correcting DOM after load rather than ensuring HTML source is consistent.

Recommended fix:

```text
Use site-footer normalization as a guard only.
Update actual page HTML sources so nav is already correct before JS runs.
Then keep the normalizer as defensive cleanup.
```

## Low findings

### P3-1 — Search tooling can be misleading because repo default branch is main

The repository default branch is `main`, while the working branch is `research-version`. Some connector search/fetch operations can default to main unless `ref: research-version` is explicitly supplied. This is a recurring source of false negatives and confusion.

Required practice:

```text
Use fetch_file with ref: research-version for known files.
Treat GitHub code search results as diagnostic only unless the branch/ref is confirmed.
```

### P3-2 — Current compare shows research-version is far ahead of main

`research-version` is 374 commits ahead of `main` and 0 behind. That is expected under Aaron's current rule, but it increases risk that GitHub's default-branch UI and search results show stale code.

Do not merge or patch main unless Aaron explicitly says so.

## Public-safety audit

No issue found in the sampled current public rendering direction:

```text
private contacts: not observed in sampled renderers
phone numbers: not observed in sampled renderers
personal emails: not observed in sampled renderers
pay rates: not observed in sampled renderers
lodging/hotel details: not observed in sampled renderers
raw source links in opportunity modal: current core links to Sources page rather than raw source URLs
```

Continue to keep source URLs centralized on `sources.html`.

## Recommended repair order

### Step 1 — Fix validation/deploy blockers

```text
1. Update tools/validate-static-app.js to match the current nav decision.
2. Repair superseded collaboration logs or validator schema.
3. Update required shared files and runtime expectations.
4. Run/trigger npm run validate:all through a real workspace or GitHub Actions.
```

This is the highest priority because live deploy appears stale.

### Step 2 — Fix documentation drift

```text
README.md
ROADMAP.md
ai-communication/AI_COLLABORATION_PROTOCOL.md
ai-communication/PROJECT_CHAT_GROUP_INSTRUCTIONS.md
ai-communication/PRODUCT_ROADMAP.md
ai-communication/DOCUMENT_DRIFT_CONTROL_PROTOCOL.md
```

Key updates:

```text
main branch protection
research-version live source
footer-only Guide/Sources header rule
separate-year 2027 rollover decision
core-owned behavior after helper removal
current active shared files
current validation contract
```

### Step 3 — Trigger deploy and visually confirm live site

Check:

```text
Home: Guide card below nav, no Guide/Sources in header.
IATSE: repeated generic note replaced by useful research guidance.
Opportunities: date sort and filters.
Footer: Guide and Sources present.
```

### Step 4 — Then improve Schedule mobile UX

Do not start full Map/Calendar/Schedule merge yet. First make the Schedule page useful on mobile.

### Step 5 — Then canonicalize 2027 records

Move verified `*-2027` opportunities out of the runtime bridge into canonical data.

## Bottom line

The current repo is not failing because Aaron's requested UI edits were impossible. It is failing because validation, docs, deployment expectations, and live-source assumptions drifted apart.

Fix the validator and stale docs first. That should unblock deploy from `research-version` and allow Aaron's live visual review to reflect the actual current code.
