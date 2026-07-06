---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__2026-06-23-claude-to-chatgpt-stage5-complete.__chunk-0002",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/2026-06-23-claude-to-chatgpt-stage5-complete.md",
  "chunk_index": 2,
  "chunk_count_for_source": 2,
  "char_start": 11399,
  "char_end": 16364,
  "source_sha256": "e272e0a4d4d1a2062054f15a3fe935066cc2c580f5ae5f11d765ac258d58b5da",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

ng each modal.

**Target:** `opportunityCard()` (or equivalent card render function) in `assets/atlas-core-v2.js`.

**Fix:** Add a small indicator — a second dot or a text chip — when `routeResearchStatus` is set on a record. Example: `● route lead` in a muted or blue color, distinct from the green source dot.

**Route data source:** Each opportunity record has `routeResearchStatus` set on it after `research-queue-route-updates.js` runs its patch. Check `o.routeResearchStatus` on the record object inside the card renderer.

**Do not** add new CSS classes that mimic existing chip/badge classes. Use inline style or existing `vtier-*` / `accom-*` classes if appropriate.

---

## What Not to Do

### Code safety rules
- **Do not** add, re-add, or reference `Firecrawl`, `FIRECRAWL_API_KEY`, or any network research automation
- **Do not** create new HTML pages unless adding them to the validator's `requiredPages` array in the same commit
- **Do not** create new JS packages unless loading them in all 12 HTML pages and adding them to `requiredSharedFiles` in the validator in the same commit
- **Do not** add `<script async>` or `<script defer>` for data packages — all data packages must be synchronous so they execute before `atlas-core-v2.js` reads `window.RESOURCE_OPPORTUNITIES`
- **Do not** remove or alter the load order in HTML pages:
  ```
  opportunity-taxonomy.js → research-queue-route-updates.js → atlas-core-v2.js → approx-date-labels.js
  ```
- **Do not** add a `chip()` function or `.chip` / `.chips` CSS rules — these are explicitly banned by the validator
- **Do not** merge `research-version` into `main` without explicit user instruction
- **Do not** push to any branch other than `research-version`

### Data safety rules
- **Do not** publish: private contacts, phone numbers, personal emails, pay rates, hotel/lodging details, crew rumors, private field notes, NDA information, client-sensitive information, private referrals
- **Do not** mark a vendor or labor provider as confirmed without a direct public source (not social media, not forums, not job boards)
- **Do not** name specific IATSE local numbers in route notes — use "verify applicable IATSE/local jurisdiction for [city] (research local number before outreach)"
- **Do not** put source URLs inside popup modals — modal links go to `sources.html`, not raw external URLs
- **Do not** delete existing branch research packages without explicit user instruction

### Architecture rules
- **Do not** split `opportunity-taxonomy.js` unless it is part of a validated refactor that updates the validator, all 12 HTML pages, and `approx-date-labels.js` in the same commit
- **Do not** convert the app to a backend, auth, or payment system
- **Do not** add real-time data fetching — this is a static site

---

## Collaboration Protocol Reference

Full protocol: `ai-communication/AI_COLLABORATION_PROTOCOL.md`

**Conflict resolution order (when files say different things):**
```
Actual files > validators > README > latest ai-communication handoff > user instruction > older docs > chat memory
```

**Division of labor:**
- Claude Code: large-scale edits, validation loop, batch data changes, multi-file refactors
- ChatGPT: UI improvements, smaller focused edits, state review, planning

**Shared coordination folder:** `ai-communication/`

**Status labels:** Use CURRENT / ASSUMED / STALE RISK / BLOCKED / VALIDATED / UNVALIDATED on shared documents.

---

## Validation Reference

```bash
npm run validate:all
```

This runs two checks:
1. `validate:branch-research` — 56 branch packages, each must have a `research/*.md` report and be in `data/packages/branch-research-manifest.js`
2. `validate:static-app` — all 12 HTML pages, all required shared files, required IDs in taxonomy and route-updates packages, no chip styles in CSS, correct function names in atlas-core-v2.js

**The validator now explicitly checks that every HTML page loads:**
```html
<script src="data/packages/opportunity-taxonomy.js?v=taxonomy1">
<script src="data/packages/research-queue-route-updates.js?v=route1">
```
...before `atlas-core-v2.js`. Any new page must follow this pattern or validation fails.

---

## Files That Must Not Be Modified Without Understanding

| File | Why |
|------|-----|
| `data/packages/opportunities-2026.js` | Primary data source — wraps records in `opp()` function with template defaults. Syntax errors here silently break all pages. |
| `data/packages/branch-research-manifest.js` | Must stay in sync with actual files in `data/packages/branch-research-batch-*.js`. Validator checks both directions. |
| `assets/approx-date-labels.js` | Handles re-application of patches on user interaction. Has skip guards for double-loading. Do not add dynamic script loading for packages that are now synchronous. |
| `tools/validate-static-app.js` | The contract. Adding new required files or IDs here means those things must exist before validation can pass. |

---

— Claude Code
