---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__2026-06-23-production-atlas-research-prompt-c__chunk-0002",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/2026-06-23-production-atlas-research-prompt-current.md",
  "chunk_index": 2,
  "chunk_count_for_source": 2,
  "char_start": 11359,
  "char_end": 17741,
  "source_sha256": "d773febb46524073a814fb39fc1898a7c70a6a14d09ffd3ad3b6855943bca4dc",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

rld — Las Vegas NV — score 48
rocklahoma-2026 — Rocklahoma — Pryor OK — score 48
austin-city-limits-2026 — Austin City Limits — Austin TX — score 58
oceans-calling-2026 — Oceans Calling — Ocean City MD — score 48
dreamstate-socal-2026 — Dreamstate SoCal — Long Beach CA — score 44
portola-2026 — Portola Music Festival — San Francisco CA — score 44
governors-ball-2026 — Governors Ball — Queens NY — score 44
shaky-knees-2026 — Shaky Knees — Atlanta GA — score 42
kilby-block-party-2026 — Kilby Block Party — Salt Lake City UT — score 42
roots-picnic-2026 — Roots Picnic — Philadelphia PA — score 42
pickathon-2026 — Pickathon — Happy Valley OR — score 40
sea-hear-now-2026 — Sea.Hear.Now — Asbury Park NJ — score 44
telluride-bluegrass-2026 — Telluride Bluegrass — Telluride CO — score 54
ultra-miami-2026 — Ultra Music Festival — Miami FL — score 52
hard-summer-2026 — HARD Summer — Inglewood CA — score 40
```

### Tier 4 — Score 30–39

```text
beyond-wonderland-socal-2026 — Beyond Wonderland SoCal — San Bernardino CA — score 38
okechobee-2026 — Okechobee — Okeechobee FL — score 38
iii-points-2026 — III Points — Miami FL — score 38
railbird-2026 — Railbird Festival — Lexington KY — score 38
countdown-nye-2026 — Countdown NYE — San Bernardino CA — score 36
capitol-hill-block-party-2026 — Capitol Hill Block Party — Seattle WA — score 32
lights-all-night-2026 — Lights All Night — Dallas TX — score 32
levitate-2026 — Levitate Music Festival — Marshfield MA — score 34
m3f-2026 — M3F Fest — Phoenix AZ — score 30
levitation-austin-2026 — Levitation Austin — Austin TX — score 36
```

## Research by producer group

Use producer batching for efficient research.

### Insomniac / Live Nation EDM

```text
EDC Las Vegas
EDC Orlando
HARD Summer
Beyond Wonderland SoCal
Countdown NYE
Dreamstate SoCal
Electric Forest co-producer route
```

Likely repeated vendor and staffing patterns. Research once, apply carefully across shows only when public evidence supports it.

### Danny Wimmer Presents

```text
Louder Than Life
Bourbon & Beyond
Welcome to Rockville
Sonic Temple
Aftershock
Inkcarceration
```

DWP often has repeated festival production patterns. One strong production-profile source may inform multiple shows, but do not claim a vendor works a specific event unless the source supports that event or producer route clearly.

### C3 Presents / Live Nation

```text
Bonnaroo
Lollapalooza Chicago
Austin City Limits
Shaky Knees
Oceans Calling
Sea.Hear.Now
Roots Picnic
Railbird
```

Large producer family. Research producer route and venue/local route separately.

### Goldenvoice / AEG Presents

```text
Coachella
Stagecoach
Portola
```

Coachella and Stagecoach share the Indio desert site ecosystem. Treat Portola separately for San Francisco site/labor route.

### Newport Festivals Foundation

```text
Newport Folk Festival
Newport Jazz Festival
```

Same foundation and same venue ecosystem. Research once, apply carefully to both.

## Output format

For each event, output a structured JavaScript-style block that can be pasted into a data update plan.

```js
{
  id: '<event-id>',
  lodgingStatus: 'confirmed|possible|unknown|unlikely',
  lodgingNotes: '<public-safe summary>',
  lodgingSources: [
    { label: '<source label>', url: '<source URL>' }
  ],
  travelStatus: 'confirmed|possible|unknown|unlikely',
  travelNotes: '<public-safe summary>',
  travelSources: [
    { label: '<source label>', url: '<source URL>' }
  ],
  laborRouteStatus: 'confirmed|possible|unknown',
  laborRouteNotes: '<public-safe summary>',
  iatseJurisdictionNote: 'verify applicable IATSE/local jurisdiction for <city or site> (research local number before outreach)',
  nonUnionRouteNotes: '<public-safe non-union route notes or unknown publicly>',
  laborSources: [
    { label: '<source label>', url: '<source URL>' }
  ],
  vendorStackStatus: 'confirmed|partial|unknown',
  vendorStackNotes: '<public-safe summary>',
  vendors: [
    { department: 'audio', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' },
    { department: 'lighting', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' },
    { department: 'video_led', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' },
    { department: 'staging', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' },
    { department: 'rigging', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' },
    { department: 'site_ops_power', company: '<public company name>', status: 'confirmed|possible', source: '<source URL or unknown>' }
  ],
  vendorSources: [
    { label: '<source label>', url: '<source URL>' }
  ],
  publicSafetyNotes: 'No private contacts, pay rates, lodging details, or rumor-only claims included.'
}
```

If nothing was found for a section, write:

```text
Unknown publicly. Human verification needed.
```

Do not fill in guesses. `unknown` and `possible` are honest. A wrong confident value is worse than no value.

## Database handoff

After research, tell Claude Code:

```text
Here are research results for <event name> (ID: <event-id>). Update data/packages/opportunities-2026.js with these fields: <paste output block>. Run npm run validate:all before pushing.
```

## Suggested search queries

Crew accommodation:

```text
<festival name> crew camping production
<festival name> production crew lodging
<festival name> vendor camping crew
<producer name> production jobs lodging provided
<festival name> site crew housing
```

Travel and per diem:

```text
<producer name> production jobs per diem
<producer name> travel crew lodging production
<vendor name> festival crew travel per diem
<festival name> production manager crew logistics
```

Labor and staffing route:

```text
<festival name> production crew jobs 2026
<festival name> stagehand jobs
<festival name> labor provider
<venue name> IATSE
<city name> IATSE jurisdiction
<producer name> careers event production
```

Vendor stack:

```text
<festival name> TPi Magazine production
<festival name> Mondo dr production
<festival name> IQ Magazine production vendors
<festival name> audio lighting video staging vendor
<festival name> production credits vendors
<vendor name> <festival name> case study
```
