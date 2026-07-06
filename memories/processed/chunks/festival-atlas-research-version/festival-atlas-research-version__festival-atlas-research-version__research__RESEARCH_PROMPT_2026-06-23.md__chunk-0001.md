---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__research__RESEARCH_PROMPT_2026-06-23.md__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/research/RESEARCH_PROMPT_2026-06-23.md",
  "chunk_index": 1,
  "chunk_count_for_source": 2,
  "char_start": 0,
  "char_end": 11918,
  "source_sha256": "72f457e72dd24675d66606fa6698ac2307fd017bb0d2bc45143367bd91bd7730",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Production Atlas — Research Prompt (Current as of 2026-06-23)

**Use this prompt with any AI assistant (ChatGPT, Perplexity, Claude, etc.) or as a self-guided web research session.**

Copy this entire document and paste it as your first message. Then name the event(s) you want to research.

---

## What this is

I am building a scouting database for a 1099 live-event production contractor (stagehand / event technician). The database tracks music festivals and large live events happening in 2026 in the United States. For each event it tries to answer three questions a working technician actually needs answered before deciding to pursue a gig:

1. **Can I get there and afford to go?** — Is there crew lodging, camping, or hotel provided? Is there per diem or travel pay?
2. **Who do I actually call or apply to?** — Which staffing companies, labor brokers, or production vendors hire for this event?
3. **Is there a union route or a non-union route?** — Which IATSE local covers this venue/city, or is this an open-call non-union show?

All records have confirmed dates and source URLs. The gaps now are in crew logistics and labor routing.

---

## Absolute rules — do NOT research or record

- Private contact names, personal phone numbers, personal email addresses
- Pay rates, hourly rates, day rates, weekly rates (even if publicly posted)
- Hotel names, specific addresses, crew lodging booking details
- Private field notes, NDA-covered information, crew gossip, forum rumors
- Any information behind a login, paywall, or private Facebook group
- Raw scraped text — summarize and attribute, do not dump

---

## What I need for each event

### Section A — Crew accommodation

Is lodging, camping, or crew housing typically provided for **production crew** (not attendees)?

This is NOT about hotel blocks for ticket buyers. It is about whether the production company or festival organization provides or arranges a place for out-of-market crew to sleep during load-in, run-of-show, and strike.

**Research signals to look for:**
- Official festival "crew" or "vendor" pages mentioning crew camping or housing
- Production company job postings mentioning lodging, housing, camping, or accommodation (Goldenvoice, C3 Presents, Insomniac, Live Nation Productions, Danny Wimmer Presents, AEG Presents, Founders Entertainment, Milwaukee World Festival, Ultra Enterprises, Newport Festivals Foundation, Planet Bluegrass)
- TPi Magazine, Pollstar, IQ Magazine, Mondo*dr feature articles about the production build
- Industry-side Reddit communities (r/livesound, r/stagehands, r/lightingdesign) — use as research direction only, not as confirmed facts

**Output values:**
```
lodgingLikely: 'yes' | 'no' | 'possible' | 'unknown'
lodgingType:   'camping_provided' | 'crew_housing' | 'hotel_paid' | 'camping_or_crew_housing_unknown' | 'none' | 'unknown'
whoProvides:   [production company name] | 'venue_local' | 'self' | 'unknown'
notes:         One sentence summarizing what you found or didn't find.
```

**Patterns that strongly suggest crew lodging/camping:**
- Rural or remote venue with no hotels nearby (Bonnaroo TN, Electric Forest MI, Hulaween FL, High Sierra CA, FloydFest VA, Pickathon OR, Rock Fest WI, Okechobee FL, Hinterland IA)
- Festival explicitly sells camping to attendees AND has a large production footprint — crew camping is often bundled in
- Multi-week or multi-city tour where a traveling crew is standard (Summerfest WI runs 2.5 weeks; Breakaway is 14 cities; Country Thunder is 3 markets; ACL is 2 weekends; New Orleans Jazz Fest is 2 weekends)

**Patterns that suggest NO crew lodging:**
- Urban festival in a major metro with abundant hotels (Lollapalooza Chicago, Governors Ball NYC, CMA Fest Nashville, Roots Picnic Philadelphia, III Points Miami, Governors Ball NYC)
- Single-day or two-day run with a small footprint

---

### Section B — Travel compensation

Does the event's production company pay for travel, mileage, flights, rental cars, or per diem for out-of-market crew?

**Research signals to look for:**
- Production company job postings mentioning "travel," "per diem," "mileage reimbursement," "housing provided," or "fly out"
- Glassdoor or Indeed reviews from production crew at the same company (not event-specific, company-level data is useful)
- TPi Magazine production profiles where the production manager mentions crew logistics
- Industry Reddit threads about specific companies' pay practices

**Output values:**
```
travelPaid:          'yes' | 'no' | 'possible' | 'unknown'
perDiem:             'yes' | 'no' | 'possible' | 'unknown'
mileage:             'yes' | 'no' | 'possible' | 'unknown'
flightProvided:      'yes' | 'no' | 'possible' | 'unknown'
rentalCarProvided:   'yes' | 'no' | 'possible' | 'unknown'
notes:               One sentence summarizing what you found or didn't find.
```

Use `'possible'` when a pattern strongly supports it (multi-week run, remote site, known touring company) but no direct public source confirms it. Use `'unknown'` when nothing is publicly available. Do not guess.

---

### Section C — Labor and staffing route

How does a production technician actually get hired for this event? This is the most useful section for the app's user.

**Three route types to research:**

**1. Union route (IATSE)**
- Which IATSE local covers the venue city?
- Is this a union call show?
- Which local's business agent or dispatch covers this venue?
- Do NOT list a specific local number unless confirmed from IATSE.org or a direct public source. Use "verify applicable IATSE local for [city]" if uncertain.

**Research approach:**
- Search `IATSE local [city name]` on iatse.net
- Search `[venue name] union call` or `[venue name] IATSE`
- Check venue's public labor agreements page if one exists

**2. Non-union labor broker / staffing company route**
- Which labor brokers or event staffing companies publicly advertise working this event?
- Which companies publicly list crew calls or job postings for this type of festival?
- Look for: Crew One Productions, Upstaging, PRG, VER (now LD Systems), Solotech, 8th Day Sound, Fifth Element, Squeek Lights, Clearwing Productions, Tait Towers, StageCo, etc.

**Research approach:**
- Search `[festival name] production crew jobs 2026`
- Search `[festival name] [production company] crew call`
- Search `[production company name] careers` for job listings mentioning the event

**3. Direct vendor application route**
- Which vendors (audio, lighting, rigging, staging, video/LED) publicly work this show?
- Which of those vendors have public job boards or application routes?

**Output:**
```
iatseNote:    'Verify applicable IATSE local for [city] (research local number before outreach)' 
              OR confirmed info from iatse.net
laborBrokers: ['company name (source: URL)']
vendorLeads:  ['vendor name — dept (source: URL or "industry pattern, verify")']
notes:        Brief summary of what was found.
```

---

### Section D — Vendor stack (which companies work the show)

What audio, lighting, video/LED, staging, rigging, and site ops companies publicly work this event?

**Priority departments:**
- Staging / structural: which company builds the main stages?
- Audio: which company provides PA and front-of-house systems?
- Lighting: which company provides production lighting?
- Video/LED: which company provides video walls and screens?
- Rigging: which company provides motors, chain, and overhead rigging?
- Site ops / fencing / power: which companies handle infrastructure?

**Research signals:**
- TPi Magazine, Mondo*dr, IQ Magazine production profiles (often list every department vendor)
- Official festival "partners" or "sponsors" pages sometimes list production vendors
- LinkedIn posts from production managers crediting their vendors
- Credit rolls in official festival recap videos
- SoundGirls.org or similar industry publications

**Output:**
```
vendorLeads: [
  { dept: 'audio', company: 'Company Name', confidence: 'confirmed' | 'likely' | 'possible', source: 'URL or description' },
  { dept: 'lighting', company: 'Company Name', confidence: '...', source: '...' },
  ...
]
```

---

## Priority events — research these first

The value score reflects long-term work potential for a traveling production technician (scale 0–100). Research higher-score events first.

### TIER 1 — Score 60+ (highest priority)

| Event | ID | Score | City | Key producer | What's missing |
|-------|----|-------|------|--------------|----------------|
| Summerfest | `summerfest-2026` | 76 | Milwaukee WI | Milwaukee World Festival Inc. | Lodging, travel, labor route, vendor stack |
| Breakaway Music Festival | `breakaway-2026` | 74 | 14 US cities | Breakaway / multi-market | Per-market lodging, travel crew route, vendor stack |
| BottleRock Napa Valley | `bottlerock-napa-2026` | 66 | Napa CA | Latitude 38 Entertainment | Lodging, travel, labor route, vendor stack |
| Coachella | `coachella-2026` | 62 | Indio CA | Goldenvoice / AEG Presents | Lodging, travel, labor route, vendor stack |
| Electric Forest | `electric-forest-2026` | 62 | Rothbury MI | Insomniac / Madison House | Crew camping, travel, labor route, vendor stack |
| Country Thunder | `country-thunder-us-2026` | 62 | AZ / FL / WI | Country Thunder Music Festivals | Per-market lodging, travel crew route, vendor stack |
| New Orleans Jazz Fest | `new-orleans-jazz-heritage-2026` | 60 | New Orleans LA | NOJHF / partners | Two-weekend lodging, labor route, vendor stack |
| EDC Las Vegas | `edc-las-vegas-2026` | 60 | Las Vegas NV | Insomniac / Live Nation | Lodging, travel, labor route, vendor stack |
| Louder Than Life | `louder-than-life-2026` | 60 | Louisville KY | Danny Wimmer Presents | Lodging, travel, DWP labor route, vendor stack |

---

### TIER 2 — Score 50–59

| Event | ID | Score | City | Key producer | What's missing |
|-------|----|-------|------|--------------|----------------|
| CMA Fest | `cma-fest-2026` | 58 | Nashville TN | Country Music Association | Lodging, travel, labor route, vendor stack |
| Bourbon & Beyond | `bourbon-and-beyond-2026` | 56 | Louisville KY | Danny Wimmer Presents | Lodging, travel, DWP labor route, vendor stack |
| Hinterland | `hinterland-2026` | 56 | St. Charles IA | First Fleet / partners | Lodging, travel, Iowa labor route, vendor stack |
| Aftershock | `aftershock-2026` | 56 | Sacramento CA | Danny Wimmer Presents | Lodging, travel, DWP labor route, vendor stack |
| North Coast Music Festival | `north-coast-2026` | 56 | Bridgeview IL | North Coast / partners | Stadium labor route, vendor stack |
| FloydFest | `floydfest-2026` | 56 | Check VA | Across-the-Way Productions | Rural crew lodging, labor route, vendor stack |
| Bonnaroo | `bonnaroo-2026` | 56 | Manchester TN | C3 Presents / Live Nation | Crew camping/housing, labor route, vendor stack |
| Hulaween | `hulaween-2026` | 58 | Live Oak FL | Suwannee / partners | Camping/crew housing, labor route, vendor stack |
| Lollapalooza Chicago | `lollapalooza-chicago-2026` | 54 | Chicago IL | C3 Presents / Live Nation | Travel comp, IATSE route, vendor stack |
| CRSSD Festival | `crssd-2026` | 54 | San Diego CA | FNGRS CRSSD | Lodging, labor route, vendor stack |
| Stagecoach | `stagecoach-2026` | 54 | Indio CA | Goldenvoice / AEG Presents | Lodging, travel, labor route, vendor stack |
| Welcome to Rockville | `welcome-to-rockville-2026` | 58 | Daytona Beach FL | Danny Wimmer Presents | Speedway lodging, travel, DWP labor route |
| Newport Folk Festival | `newport-folk-2026` | 52 | Newport RI | Newport Festivals Foundation | Lodging, travel, RI labor route, vendor stack |
| Newport Jazz Festival | `newport-jazz-2026` | 52 | Newport RI | Newport Festivals Foundation | Lodging, travel, RI labor route, vendor stack |
| Rock Fest Wisconsin | `rock-fest-wisconsin-2026` | 52 | Cadott WI | Rock Fest / Chippewa Valley | Crew camping, WI labor route, vendor stack |
