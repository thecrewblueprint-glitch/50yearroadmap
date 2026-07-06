---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__handoffs__CLAUDE_CODE_HANDOFF.md__chunk-0002",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/handoffs/CLAUDE_CODE_HANDOFF.md",
  "chunk_index": 2,
  "chunk_count_for_source": 2,
  "char_start": 11368,
  "char_end": 16756,
  "source_sha256": "25644319d65efd9be5f2dd4c8a92c00e373d2123ca1eef453eaa6652423e24c5",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

type f -iname "*firecrawl*"
find tools -maxdepth 1 -type f -iname "*firecrawl*"
find research -maxdepth 1 -type f -iname "*firecrawl*"
```

Expected:

```text
No files found
```

### Task 2 — Run baseline validation

Run:

```bash
npm run validate:all
```

Fix all failures before changing feature code.

Expected likely failure:
- Missing matching `research/*.md` reports for batch-006 data packages.

### Task 3 — Create missing reports for existing batch-006 packages

Create concise reports for:

```text
research/branch-research-batch-006-lighting.md
research/branch-research-batch-006-audio.md
research/branch-research-batch-006-video-led.md
research/branch-research-batch-006-staging.md
research/branch-research-batch-006-rigging.md
```

Report format should include:

```text
# Branch Research Batch 006 — <Department>

Generated from reviewed supplemental refresh artifacts.
Public-safe summary only.
No private contacts, pay rates, lodging, rumors, or direct personal outreach data included.

## Included targets
- ...
## Confidence boundary
- ...
## Next verification actions
- ...
```

### Task 4 — Convert remaining artifacts into app-ready data

Create public-safe data packages and matching reports for:

```text
Power
Site Ops
Logistics
Stage Management
Production Office
Backline
```

Use the same data schema required by the validator:

```js
window.OPPORTUNITY_BRANCH_RESEARCH_BATCH_006_POWER = {
  batchId: 'branch-research-batch-006-power',
  researchedAt: '2026-06-22',
  branchId: 'power',
  branchName: 'Power',
  purpose: 'Supplemental Power refresh research from reviewed public artifacts. Adds route/context leads without overwriting prior research.',
  targets: [
    {
      opportunityId: '...',
      opportunityName: '...',
      status: 'supplemental_route_lead',
      confidence: '...',
      confirmedVendors: [],
      likelyResponsible: [],
      publicLeads: [],
      sourceLinks: [{ label: '...', url: '...' }],
      evidenceSummary: '...',
      branchDisplayText: '...',
      nextAction: '...'
    }
  ]
};
```

Important:
- `publicLeads` can contain text names, but if the app expects employer IDs for linking, use known employer IDs only where safe. Otherwise plain text is acceptable but will render as text.
- Keep `confirmedVendors: []` unless verified by a strong official/trade source.
- For job boards, social posts, forums, and generic event pages, use low-confidence labels.

### Task 5 — Update manifest

After adding new packages, update:

```text
data/packages/branch-research-manifest.js
```

Add the new filenames in department order:

```text
staging
rigging
lighting
audio
video-led
power
site-ops
logistics
scenic
backline
stage-mgmt
production-office
```

Note: Current manifest order does not yet include backline/stage-mgmt/production-office. Add them only after packages and reports exist.

### Task 6 — Update README

Update stale research status.

Replace the old Scenic batch-002 stop-point with the current state:

```text
Current app research:
- Scenic completed through batch 005.
- Supplemental refresh batch 006 exists for Lighting, Audio, Video/LED, Staging, and Rigging.
- Remaining refresh artifacts are ready for conversion: Power, Site Ops, Logistics, Stage Management, Production Office, Backline.
- Firecrawl access has been removed; no Firecrawl runner/workflow should remain active.
```

### Task 7 — Re-run validation

Run:

```bash
npm run validate:branch-research
npm run validate:static-app
npm run validate:all
```

All must pass.

### Task 8 — Check browser behavior

Open locally with a static server if possible:

```bash
python3 -m http.server 8000
```

Then check:

```text
/
branches.html
sources.html
opportunities.html
analytics.html
```

Confirm:
- Branch record count loads correctly.
- Sources page includes new source links.
- Opportunity popups do not show source links.
- Branch popups show supplemental route leads.
- No console errors for missing package/report files.
- No Firecrawl network calls.

### Task 9 — Commit changes

Suggested commit messages:

```text
Add supplemental refresh reports for batch 006
Add remaining supplemental branch research packages
Update branch research manifest
Update README research status
Remove Firecrawl access remnants
```

---

## 11. Acceptance Criteria

The handoff is complete when:

```text
1. No Firecrawl secret exists in GitHub repository settings.
2. No Firecrawl runner/workflow/control file remains active in the repo.
3. npm run validate:all passes.
4. Every branch-research-batch-*.js file has a matching research/*.md report.
5. Manifest references every branch package and no missing files.
6. README reflects the real current state.
7. Sources page loads source links from branch records.
8. Public popups remain free of raw source links and private data.
9. All new research is labeled as supplemental route/context unless independently verified.
```

---

## 12. Do Not Do

Do not:
- Re-add Firecrawl.
- Re-create FIRECRAWL_API_KEY.
- Add new network research automation.
- Publish raw Firecrawl artifact text.
- Mark social/forum/job-board results as confirmed vendors.
- Add private contacts, phone numbers, personal emails, pay rates, hotel/lodging, rumors, or private referrals.
- Remove older research packages unless validation proves they are broken and the user explicitly approves.
- Put source links inside popups.
