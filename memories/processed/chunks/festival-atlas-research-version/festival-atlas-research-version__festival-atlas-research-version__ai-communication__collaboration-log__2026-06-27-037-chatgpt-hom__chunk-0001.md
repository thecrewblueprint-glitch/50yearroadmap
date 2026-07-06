---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__collaboration-log__2026-06-27-037-chatgpt-hom__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/collaboration-log/2026-06-27-037-chatgpt-home-upcoming-sort.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 1527,
  "source_sha256": "7d229916cec25d60a7daf3369498693ba2b03adb08ba13d2f3496a94b7ea83c6",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Collaboration Log Entry — Home Upcoming Festival Sort

Status: incomplete
Created: 2026-06-27
Review after: 2026-07-11
Assistant: ChatGPT
Branch: research-version
Commit: 3c6353d44fbcbd641d7e9272f93e3c6ba4376fec and 229b443f8c86311829b90bd2ef107e4281c44cc6

## Files changed

```text
assets/home-upcoming.js
index.html
```

## What changed

Aaron requested that the festivals shown on the home page be ordered by upcoming date from today forward, until the app later becomes a live feed.

A narrow home-page script was added and loaded only on `index.html`.

## Behavior

```text
- Reads existing public `window.scopedOpportunities`.
- Uses the visitor/browser current date.
- Sorts active festivals from today forward by `startDate`.
- Past festivals move behind upcoming festivals.
- Shows the first 6 records in the home page upcoming festival grid.
- Keeps cards clickable through `openOpportunity(id)`.
```

## Public display

Home cards show only useful public information:

```text
festival name
city/state
dates
producer when publicly known
department summary
Open festival action
```

## Scope preserved

```text
No backend
No live feed yet
No private data
No broad DOM rewrite
No header/filter changes
```

## Validation status

Validation not run; connector session cannot run local repo validation.

Required next command:

```bash
npm run validate:all
```

## Next action

Validate and hard refresh the home page. Confirm the visible home festival cards start with upcoming events from the current date forward.
