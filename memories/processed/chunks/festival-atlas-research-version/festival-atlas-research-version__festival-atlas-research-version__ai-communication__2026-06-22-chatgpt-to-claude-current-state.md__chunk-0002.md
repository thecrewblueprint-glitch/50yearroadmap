---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__2026-06-22-chatgpt-to-claude-current-state.md__chunk-0002",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/2026-06-22-chatgpt-to-claude-current-state.md",
  "chunk_index": 2,
  "chunk_count_for_source": 2,
  "char_start": 11391,
  "char_end": 16183,
  "source_sha256": "9a8f99afed87f38e9756eb61345dceb04bb7a99d50d094c8608024da09d0a58e",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

ntal publication of unreviewed source context.

## 20. Public Safety Rules

Do not publish:

```text
private contacts
phone numbers
personal emails
pay rates
hotel/lodging details
crew rumors
private field notes
NDA information
client-sensitive information
private referrals
```

Public app may show:

```text
official/public source links
general confidence labels
public route notes
public-safe employer homepages/careers links
next action notes
human verification needed language
```

Public app must not show:

```text
privateContacts
doNotPublish
unsanitized fieldNotes
unsanitized crewReferrals
sensitive work-call details that are not public
private referral information
```

If information is not public, use language like:

```text
Unknown publicly. Human verification needed.
```

If private field intelligence exists, use language like:

```text
Private field intelligence exists, but it is not published in the public app.
```

Do not turn private or word-of-mouth information into public claims.

## 21. Firecrawl Status

Current README says Firecrawl access has been removed and no Firecrawl runner, workflow, or control file remains active.

Do not:

```text
Re-add Firecrawl.
Re-create FIRECRAWL_API_KEY.
Add new network research automation.
Publish raw Firecrawl artifact text.
```

If you need to verify repo cleanup, run:

```bash
grep -RIn "FIRECRAWL_API_KEY\|firecrawl\|api.firecrawl.dev\|firecrawl-output\|firecrawl-run-control" . --exclude-dir=.git
find .github/workflows -maxdepth 1 -type f -iname "*firecrawl*"
find tools -maxdepth 1 -type f -iname "*firecrawl*"
find research -maxdepth 1 -type f -iname "*firecrawl*"
```

Acceptable results:

```text
No active workflow or executable runner references.
Historical mentions may exist only in clearly archived/handoff documentation.
```

## 22. Relationship Between Research Archive and App Code

The `research/` directory is document-heavy and should not be fully loaded just to work on the web app.

Use this priority order for catching up:

```text
1. README.md on research-version
2. package.json
3. assets/atlas-core-v2.js
4. assets/atlas.css
5. active HTML pages
6. data/packages/branch-research-manifest.js
7. tools/validate-branch-research-packages.js
8. tools/validate-static-app.js
9. data schema docs
10. handoffs/CLAUDE_CODE_HANDOFF.md
11. research archive only if the task requires it
```

## 23. Known Documentation Drift

Be careful: older handoff text may describe incomplete artifact conversion, missing batch-006 reports, or README staleness. The current README and manifest indicate those tasks have been resolved.

Before acting on any older task list, verify against:

```text
README.md
data/packages/branch-research-manifest.js
actual data/packages/branch-research-batch-*.js files
actual research/branch-research-batch-*.md files
npm run validate:all
```

## 24. Current Claude Catch-Up Task

Before doing any feature work, Claude should:

```text
1. Checkout or inspect research-version.
2. Read this handoff.
3. Read README.md.
4. Read package.json.
5. Read assets/atlas-core-v2.js.
6. Read data/packages/branch-research-manifest.js.
7. Read tools/validate-branch-research-packages.js.
8. Read tools/validate-static-app.js.
9. Read data/packages/OPPORTUNITY_RECORD_SCHEMA.md.
10. Read data/packages/INTELLIGENCE_CLASSIFICATION_SCHEMA.md.
11. Optionally skim handoffs/CLAUDE_CODE_HANDOFF.md, but treat it as potentially older than this file.
12. Run npm run validate:all before modifying merge-worthy code.
```

## 25. What Not To Do

Do not:

```text
Use main as current source of truth.
Deep-load/cache the research archive unless the task requires it.
Re-add Firecrawl or any network research automation.
Put source links inside public popups.
Publish private contacts, pay, lodging, rumors, private field notes, or referral data.
Mark social/forum/job-board results as confirmed vendors.
Delete older research packages without explicit user approval.
Merge PR #1 without explicit user approval.
Convert the app into a backend/auth/payment system inside this branch.
```

## 26. Bottom Line

Current state summary:

```text
Production Atlas is a static, manifest-driven GitHub Pages web app on research-version.
The app loads public-safe opportunity, employer, IATSE, and branch research data through JS packages.
Branch research packages are validated strictly and must be paired with matching research reports.
The manifest is authoritative.
Sources are centralized on sources.html.
Public popups must stay clean and public-safe.
Firecrawl is removed and must not be reintroduced.
The research archive is heavy; inspect it only when needed.
PR #1 contains the large unmerged research/app expansion from research work toward main.
Claude should catch up to this state before continuing.
```
