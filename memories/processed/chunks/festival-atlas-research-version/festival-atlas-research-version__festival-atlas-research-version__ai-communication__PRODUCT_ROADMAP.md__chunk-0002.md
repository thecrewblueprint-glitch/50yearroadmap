---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__PRODUCT_ROADMAP.md__chunk-0002",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/PRODUCT_ROADMAP.md",
  "chunk_index": 2,
  "chunk_count_for_source": 2,
  "char_start": 11383,
  "char_end": 13507,
  "source_sha256": "8fcb14a6d8ff0335c53cf0c7760a55be48fa617ad4fa81b2dc492e92ac777e33",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

el is separate year-specific records. The current rollover bridge creates `*-2027` records at runtime for verified public 2027 cycles and archives the corresponding active `*-2026` source records. `public-cycle-scope.js` keeps future-year records out of the default 2026 public view.

Future cleanup:

```text
Move verified *-2027 records into canonical opportunity data.
Shrink or retire data/packages/opportunity-rollover-2027.js.
Reassess data/packages/public-cycle-scope.js after core owner-file cycle controls exist.
Keep pending 2027 records hidden until public source dates are verified.
```

### 4.5 Future Unified Planning Workspace

Do not attempt the full merge until Schedule is mobile-usable.

Longer-term planning direction:

```text
pick festival
see map location
see public show dates
see approximate working window
add/remove from schedule
later compare travel distance/time when scope and source are approved
```

### 4.6 Improve Sources View

Sources page should remain the audit table.

Useful support:

```text
search by opportunity
filter by section if useful
show source label
open public source
avoid raw source links in popups
```

---

# Execution Order

Use this order unless Aaron reprioritizes:

```text
1. Run or trigger npm run validate:all in a real workspace or GitHub Actions environment.
2. Confirm the live site is serving research-version output.
3. Spot-check public pages on mobile, especially nav, filters, IATSE, Employers, Opportunities, Map, Analytics, and Schedule direct URL.
4. Improve Schedule mobile usability before restoring it to header nav.
5. Improve filter empty states.
6. Continue public source and producer/promoter verification for priority records.
7. Refine remaining map coordinates when exact public venue/location data is available.
8. Canonicalize verified 2027 records after validation/deploy are stable.
```

## What This Roadmap Excludes

Do not include these in this roadmap:

```text
backend architecture
login/authentication
private contact database
payment systems
scraping automation
Firecrawl restoration
LMS integration
general business planning
```
