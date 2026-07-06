---
{
  "chunk_id": "Perplexity-Batch-2026-07-05__Perplexity-how_to_find_and_track_festivals_in_the_United_States_and_create_a_live_RSS_data_feed___chunk-0002",
  "archive_id": "Perplexity-Batch-2026-07-05",
  "archive_filename": "Perplexity-Batch-2026-07-05.zip",
  "source_path": "Perplexity-how_to_find_and_track_festivals_in_the_United_States_and_create_a_live_RSS_data_feed_that_gives_me_a_comprehensive_resource_feed_about_all_festivals_in_the_United_States.md",
  "chunk_index": 2,
  "chunk_count_for_source": 2,
  "char_start": 11349,
  "char_end": 22051,
  "source_sha256": "b1190c37396e6d62b8918a58bba578698a6e4597c33dc8cb0ae38da63e852431",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

ction-related terms, then only publish items above a threshold. That lets you keep the feed focused on festivals where your labor and production knowledge is actually useful.[6][9][4][5]

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
