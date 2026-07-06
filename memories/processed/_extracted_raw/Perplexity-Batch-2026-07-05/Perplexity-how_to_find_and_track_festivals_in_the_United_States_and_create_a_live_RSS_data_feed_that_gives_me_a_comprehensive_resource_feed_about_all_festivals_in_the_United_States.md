Original URL: https://www.perplexity.ai/search/51282d3a-e5e6-4512-a004-aff00c5ce95f
Conversation Time: 6/28/2026, 5:50:56 AM
Export Time: 7/5/2026, 5:02:35 PM

**[USER]**

how to find and track festivals in the United States and create a live RSS data feed that gives me a comprehensive resource feed about all festivals in the United States

---

**[ASSISTANT]**

You can build this as a **two-layer system**: a festival discovery pipeline that collects events from many sources, and a feed layer that normalizes them into one live RSS stream. The best practical approach is to combine authoritative sources like FestivalNet’s nationwide database, city open-data event/permit portals, and direct RSS or API sources, then publish your own curated feed from that unified dataset.[1][2][3]

## Source strategy

Start by defining what counts as a “festival,” because the U.S. has everything from food festivals and film festivals to music, arts, and cultural events. A broad resource feed usually works best when you include multiple categories and then tag each item by type, state, city, date, and source quality.[2][4]

Good source types include:
- Large festival directories such as FestivalNet, which advertises 26,000+ festival and art-show listings across the U.S. and Canada.[1][2]
- City open-data portals and permit datasets, such as Seattle’s special events permits and Data.gov festival-related datasets.[3][4][5]
- Venue or organizer calendars that already expose RSS or calendar feeds, which can be aggregated directly into your system.[6][7]
- RSS generator services or feed builders for sites that do not publish RSS natively.[8][9][10]

## Build the pipeline

Your pipeline should do four jobs: discover, extract, normalize, and publish. Discovery finds event pages or feeds, extraction pulls the raw details, normalization converts everything into one schema, and publishing exposes the result as RSS, JSON, and maybe an HTML directory.[9][10][8]

A good normalized festival schema would include:
- Title.
- Start and end date.
- Location name, city, state, and ZIP.
- Festival category.
- Organizer or source name.
- Ticket or official website URL.
- Last seen date.
- Confidence score or source reliability tag.

That structure lets you merge duplicate listings from different sources while keeping the canonical official event link.[2][3][1]

## RSS feed design

RSS works best when each item represents one festival listing, and each item links to a canonical detail page on your own site or database. Keep the feed updated frequently, but avoid changing item GUIDs unless the underlying festival meaningfully changes, or readers will see duplicates.[7][6]

A practical feed setup is:
- One master RSS feed for all U.S. festivals.
- Optional subfeeds by state, month, or category.
- Optional filtered feeds for music, food, cultural, film, art, or family events.
- A “recently added” feed for new or changed listings.

If you want broad adoption, also generate an Atom feed and a JSON feed alongside RSS, since some apps prefer those formats.[8][9]

## Data collection methods

You will usually need a mix of methods because no single source covers all U.S. festivals completely. For sites with RSS or XML exports, ingest the feed directly; for sites without feeds, use HTML scraping only where allowed, and prefer APIs or official downloads when available.[11][6][7]

For a scalable stack, I’d use:
- Scheduled crawlers for known festival directories.
- API connectors for event platforms and open-data portals.
- Feed parsers for RSS/ICS/XML sources.
- Deduplication rules based on title, date range, and location.
- Manual review for low-confidence matches.

That approach fits your Laravel and WordPress workflow well, because Laravel can handle ingestion and deduplication while WordPress can serve the public-facing directory and RSS endpoints.

## Suggested architecture

A clean implementation could look like this:
1. Source registry in a database table.
2. Fetch jobs running on a schedule.
3. Parser classes per source type.
4. Normalization service that maps all records to one model.
5. Deduplication and ranking.
6. RSS endpoint that renders the latest approved records.
7. Optional WordPress front end for browsing and search.

Laravel is a strong fit for the backend because it gives you queues, scheduled tasks, models, and API endpoints in one place. WordPress can then act as the content presentation layer if you want fast publishing and SEO-friendly pages.

## Practical tooling

For no-code or low-code feed creation, services like RSS.app, FetchRSS, and similar feed generators can help you prototype quickly, especially for websites that lack a native feed. For a production-grade resource feed, though, you will want your own backend so you control filtering, deduplication, and update logic.[10][9][8]

If you want the feed to feel “comprehensive,” you also need a quality policy:
- Prefer official organizer pages over scraped summaries.
- Tag uncertain records clearly.
- Drop expired listings automatically.
- Refresh future events more often than past archives.
- Keep source attribution in each item.

## Best next step

The most effective starting point is to build a U.S. festival database around a handful of high-value sources like FestivalNet plus city event datasets, then expand source coverage over time. The result should be your own searchable festival index with a live RSS feed generated from that index, not a feed that depends on one external website.[4][3][1][2]

Would you like a Laravel database schema and ingestion workflow for this?

---

**[USER]**

I want to solely focus on music and arts festivals that need hands that have production knowledge

---

**[ASSISTANT]**

That narrows the target a lot: you want **music and arts festivals where production skills matter**, not just attendee-facing event listings. The best feed for you should prioritize festivals that need stagehands, production managers, technical crew, rigging, audio, lighting, site logistics, and backstage support.[1][2][3]

## What to track

Focus on festivals that regularly publish production-related needs or have large enough operations to require crews. That includes music festivals, performing arts festivals, classical festivals, outdoor arts festivals, and multi-venue event series where stage setup, PA, seating, transport, and pack-down are part of the operation.[2][1]

Useful filters for your resource feed:
- Music festivals.
- Arts and performing arts festivals.
- Festivals with “production,” “stagehand,” “crew,” “technical,” or “site ops” language.
- Seasonal or touring festivals.
- Festivals that mention lighting, sound, staging, rigging, or logistics.[3][1][2]

## Best source types

For this niche, you will get better quality from production-aware sources than from generic event directories. Job boards and festival career pages reveal which festivals actually need hands with real production knowledge, while directory sites help you discover which events exist in the first place.[4][5][2]

A strong source mix would be:
- Festival production job pages and crew calls.[1][2]
- Large festival directories for discovery, such as FestivalNet.[6][7]
- Job aggregates like Indeed, ZipRecruiter, and LinkedIn for production roles tied to festivals.[8][3][4]
- Official festival and arts-organization sites that describe crew needs directly.[2][1]

## Feed structure

Instead of making one giant “all festivals” feed, make a curated **production-opportunity feed**. Each item should represent a festival and include why it matters to someone with production knowledge: what kind of crew is needed, what systems are involved, and whether the work is hands-on, supervisory, or technical.[1][2]

Recommended fields:
- Festival name.
- Category: music, arts, or mixed.
- Production relevance score.
- Crew type needed.
- City, state, and date.
- Source page.
- Status: upcoming, hiring, seasonal, recurring.
- Notes on physical/logistical demands.

## Filtering rules

To keep the feed useful, exclude festivals that are mainly vendor fairs or generic community events unless they clearly need production staff. Also exclude listings that do not mention live production, stage operations, technical setup, or backstage logistics.[2][1]

Good inclusion signals:
- “Production manager.”
- “Stage crew.”
- “Technical production.”
- “Lighting, sound, staging, rigging.”
- “Pack-down.”
- “Site safety.”
- “Operational delivery.”
- “Contractors and suppliers”.[1][2]

## Practical build approach

A good implementation would use three layers:
1. Discovery layer for festival listings.
2. Production-intent layer that detects crew/technical language.
3. RSS output layer that publishes only the filtered matches.

If you build this in Laravel, you can score each festival automatically based on the text on the source page. A simple rule-based classifier will already work well: if a listing contains production keywords, it gets surfaced; if it mentions crew roles, it gets a higher score; if it has no operational language, it gets dropped.

## Best next move

The most efficient next step is to build a **production-only festival RSS feed** for the U.S. that highlights:
- music and arts festivals,
- official crew calls,
- festivals with technical or stage operations,
- and recurring festivals likely to need contractors or seasonal hands.[3][4][2][1]

Would you like me to outline the exact database schema, keyword filters, and RSS fields for that production-focused feed?

---

**[USER]**

yes

---

**[ASSISTANT]**

Yes — the cleanest way to do this is to build a **production-focused festival feed** with a narrow schema and strong filters, then generate RSS from only the items that match music/arts + production intent. RSS 2.0 supports the fields you need for this kind of feed, including `title`, `link`, `description`, `guid`, and `pubDate`, and Laravel can generate that XML directly or through a package like `spatie/laravel-feed`.[1][2][3]

## Feed scope

Your feed should only include festivals that are both:
- music or arts oriented, and
- likely to need hands with production knowledge.

That means your source pages should explicitly mention things like stage crew, production manager, technical production, audio, lighting, rigging, site operations, or logistics. Festival production job listings and crew calls are a strong signal, while generic event calendars are too broad unless they contain those terms.[4][5][6]

## Database schema

Use one `festivals` table plus one `sources` table, or split into `events`, `event_sources`, and `event_tags` if you want more flexibility. For your use case, the festival record should store the event itself, the production relevance score, and the raw source evidence so you can explain why it was included.[5][7][8]

Suggested fields:
- `id`
- `name`
- `category` (`music`, `arts`, `mixed`)
- `subtype` (`festival`, `arts festival`, `music festival`)
- `start_date`
- `end_date`
- `city`
- `state`
- `venue`
- `official_url`
- `source_url`
- `source_name`
- `production_keywords_found`
- `production_score`
- `crew_type`
- `status`
- `last_seen_at`
- `published_at`

## Production filter

A simple keyword scoring system is enough to start, and you can improve it later with NLP. Assign points when the source text contains production-related terms, then only publish items above a threshold. That lets you keep the feed focused on festivals where your labor and production knowledge is actually useful.[6][9][4][5]

Example scoring rules:
- `music festival` or `arts festival`: +2.
- `production`, `stagehand`, `crew`, `technical`, `logistics`: +2 each.
- `lighting`, `sound`, `rigging`, `site ops`, `backstage`: +3 each.
- `production manager` or `crew call`: +5.
- No production terms: exclude.

## Ingestion pipeline

Build the ingestion system in this order:
1. Pull from festival directories and official festival pages.
2. Pull from job boards and crew-call pages to detect production-heavy festivals.
3. Normalize the text into a single internal record.
4. Score relevance.
5. Deduplicate by date range, city, and official name.
6. Publish only approved items to RSS.[7][9][10][5]

This is especially useful because festival directories discover the event, while crew-call pages tell you whether production knowledge is actually needed.[5][6][7]

## RSS output

Your RSS feed should contain one item per festival, not one item per job post. The RSS item should point to your own detail page, and that page can show the official event link, production notes, and source references.[2][11][1]

Recommended RSS item content:
- Title: festival name plus state.
- Description: short summary of why it matters to production people.
- Link: your festival detail page.
- GUID: stable URL for the festival record.
- PubDate: when the record was first published or last materially updated.
- Category: music or arts.
- Optional custom fields if you also generate Atom or JSON feeds.

## Laravel implementation

A straightforward Laravel setup is:
- `php artisan make:model Festival -m`
- `php artisan make:model Source -m`
- A scheduled command to fetch and score sources.
- A controller or route that renders `/feed.xml`.
- Cache the generated XML for performance.

Laravel can write RSS XML directly, or you can use an RSS package to simplify feed generation. The simplestweb example shows the pattern clearly: query records, render an RSS view, and save or serve the XML output.[3][11][12][13]

## Source priority

Rank your sources like this:
1. Official festival websites.
2. Official crew-call or production pages.
3. City permits or open-data event records.
4. Major festival directories.
5. General job boards only when they clearly tie a role to a festival.[8][9][7][5]

That order keeps the feed accurate and prevents it from becoming a generic job aggregator.

## First build plan

The fastest useful version is:
- one U.S. feed,
- music and arts only,
- production-heavy only,
- 50 to 200 source sites,
- daily refresh,
- manual approval for borderline items.

That gives you a focused resource feed instead of a noisy database dump. Would you like the Laravel migration files and the RSS controller/view template next?

---

**[USER]**

write me a comprehensive build plan and a framework for a coding agent to build this on GitHub if that is possible.

---

**[ASSISTANT]**

Yes — it is absolutely possible to build this on GitHub, and the best way is to treat GitHub as the source control, issue tracker, and CI/CD layer for a Laravel app that ingests festival data, scores production relevance, and publishes an RSS feed. A coding agent can build it effectively if you give it a strict project blueprint, a repository structure, clear acceptance criteria, and a staged work order.[1][2][3]

## Build goals

The product should become a U.S. festival intelligence system focused only on music and arts festivals that need production knowledge. Its job is to discover festival listings, identify production-heavy opportunities, normalize the data, deduplicate it, and publish a live RSS feed plus a browsable directory.[4][5][6]

Primary outputs:
- A searchable festival database.
- A live RSS feed.
- Optional category feeds by state, month, and production role.
- An admin review queue for low-confidence matches.
- A clean public page for each festival listing.

## Recommended architecture

Use Laravel as the backend application because it handles scheduling, queues, Eloquent models, and feed endpoints cleanly. Use `spatie/laravel-feed` or a similar feed package to speed up RSS delivery, and let the app generate the feed from database records rather than from raw scraped pages.[2][7][1]

Suggested architecture:
- **Ingestion layer:** fetches data from official festival sites, open-data portals, and relevant job/crew pages.
- **Normalization layer:** converts all source records into one schema.
- **Scoring layer:** measures whether the festival is likely to need hands with production knowledge.
- **Deduplication layer:** merges duplicates across sources.
- **Publication layer:** renders RSS, Atom, and a website directory.

## Source strategy

The coding agent should prioritize sources that are most likely to reveal real production needs. That means official festival sites, crew-call pages, festival directories like FestivalNet, and job boards where “production crew” language appears.[5][8][9][4]

Source ranking:
1. Official festival websites.
2. Official production or crew pages.
3. City event/permit open-data portals.
4. Major festival directories.
5. Job boards only when they directly reference festival production roles.

## Data model

The agent should create a model that supports both festival discovery and production relevance. Keep the schema simple at first, but preserve the source text and score so you can explain why something was included.[10][2][5]

Core tables:
- `festivals`
- `sources`
- `festival_source_links`
- `tags`
- `festival_tags`
- `ingestion_runs`
- `review_queue`

Key fields:
- Festival identity and dates.
- Location and official URL.
- Source URL and source type.
- Production keywords found.
- Production score.
- Crew type.
- Status and approval state.
- Last seen and last checked timestamps.

## Scoring framework

The agent should not try to “understand” every source perfectly on day one. A keyword-and-weight scoring system is safer and easier to debug, and it matches the production-heavy niche well.[6][9][11][5]

Example scoring rules:
- `festival`, `music`, `arts`: base relevance.
- `production`, `crew`, `stagehand`, `technical`, `logistics`: positive points.
- `sound`, `lighting`, `rigging`, `site ops`, `backstage`: stronger points.
- `production manager`, `tour manager`, `crew call`: highest points.
- No production language: exclude unless manually approved.

## GitHub repository structure

Give the coding agent a repo structure that cleanly separates app logic, ingestion, tests, and deployment. A clear structure reduces confusion and makes CI easier to maintain.[12][1]

Recommended layout:
- `app/Models`
- `app/Services/Ingestion`
- `app/Services/Scoring`
- `app/Services/Deduplication`
- `app/Console/Commands`
- `app/Http/Controllers`
- `resources/views/feeds`
- `tests/Feature`
- `tests/Unit`
- `.github/workflows`
- `docs/`

## GitHub workflow

GitHub should manage development through issues, pull requests, and actions. The coding agent should work from a milestone-based issue list, create small pull requests, and run tests on every push.[3][13][1]

Suggested workflow:
1. Create a GitHub repo.
2. Add a product brief in `README.md`.
3. Open issues for schema, ingestion, scoring, feed output, UI, and deployment.
4. Have the agent implement one issue per branch.
5. Run CI on every PR.
6. Merge only after tests and acceptance checks pass.

## Agent task framework

The agent should be given a strict task ladder so it builds in the correct order. This is important because scraping, scoring, and RSS output depend on a stable schema and test suite.[14][2][12]

Task order:
1. Set up Laravel project and base environment.
2. Create database schema and Eloquent models.
3. Build source ingestion services.
4. Implement keyword scoring and deduplication.
5. Create RSS feed output.
6. Build searchable public pages.
7. Add admin review tools.
8. Add scheduled refresh jobs.
9. Write tests.
10. Add deployment workflow.

## Acceptance criteria

Every coding task should have an explicit definition of done. That prevents the agent from stopping at “it compiles” when you really need a production-ready pipeline.[7][1][2]

Examples:
- New festivals can be imported from at least one official source.
- Production-heavy listings are scored and surfaced.
- Duplicate records are merged.
- RSS validates against RSS 2.0 expectations.
- Feed updates automatically on schedule.
- Tests cover ingestion, scoring, and feed generation.

## GitHub Actions

Use GitHub Actions for linting, tests, and deployment checks. The agent should produce a workflow that runs PHPUnit, PHPStan or Pint if you choose them, and any feed validation tests you add.[1][2][3]

A solid CI pipeline should:
- Install dependencies.
- Run static analysis.
- Run unit and feature tests.
- Build assets if needed.
- Fail the pull request if the feed or schema tests break.

## Prompt framework for the coding agent

Use a structured prompt that tells the agent exactly what to build and in what order. The more precise the instructions, the less likely it is to drift into generic festival directory behavior.[12][14][1]

Prompt framework:
- **Role:** Senior Laravel engineer building a festival intelligence platform.
- **Goal:** Build a U.S. music and arts festival feed focused on production-heavy opportunities.
- **Constraints:** Only include festivals with production relevance; prioritize official sources; preserve source provenance.
- **Output:** Code, migrations, models, tests, feed endpoints, and deployment workflow.
- **Rules:** Do not add generic festival listings unless they pass the production filter.
- **Definition of done:** Working RSS feed, working import pipeline, passing tests, documented setup.

## First milestone plan

Start with a narrow MVP so the agent can finish something useful quickly. A focused first release is much better than trying to solve every festival source in the country at once.[4][5][10]

MVP milestone:
- One Laravel app.
- One RSS feed.
- Three source types.
- One keyword scoring engine.
- One admin approval screen.
- Daily scheduled ingestion.
- Test suite for the feed and scorer.

## Practical note on feasibility

GitHub is a very good place to run this project, but GitHub itself is not the application runtime; it is the development and deployment platform. The app should run on your own hosting, while GitHub stores the code, manages pull requests, and automates builds and tests.[2][3][1]

I can turn this into a ready-to-paste GitHub issue set, a repo README, and a coding-agent master prompt next.