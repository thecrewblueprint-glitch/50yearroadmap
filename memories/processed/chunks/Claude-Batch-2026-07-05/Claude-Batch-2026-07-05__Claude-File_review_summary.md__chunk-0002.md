---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-File_review_summary.md__chunk-0002",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-File_review_summary.md",
  "chunk_index": 2,
  "chunk_count_for_source": 19,
  "char_start": 11331,
  "char_end": 23331,
  "source_sha256": "3653d16a82eee3313973f143fc993c21304b0aa1ab3762cd8fe90ad6a364e785",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

ere because
   200	the seccomp filter blocks the `AF_UNIX` sockets LibreOffice uses for
   201	instance management).
   202	
   203	For anything beyond reading, go to `/mnt/skills/public/pptx/SKILL.md`.
   204	
   205	---
   206	
   207	## CSV / TSV
   208	
   209	**Do not** `cat` or `head` these blindly. A CSV with a 50KB quoted cell
   210	in row 1 will wreck your `head -5`. Use pandas with `nrows`:
   211	
   212	```python
   213	import pandas as pd
   214	df = pd.read_csv("/mnt/user-data/uploads/data.csv", nrows=5)
   215	print(df)
   216	print()
   217	print(df.dtypes)
   218	```
   219	
   220	Approximate row count without loading (over-counts if the file has
   221	RFC-4180 quoted newlines — the same quoted-cell case this section
   222	warned about above):
   223	
   224	```bash
   225	wc -l /mnt/user-data/uploads/data.csv
   226	```
   227	
   228	Full analysis only after you know the shape:
   229	
   230	```python
   231	df = pd.read_csv("/mnt/user-data/uploads/data.csv")
   232	print(df.describe())
   233	```
   234	
   235	TSV: same, with `sep="\t"`.
   236	
   237	---
   238	
   239	## JSON / JSONL
   240	
   241	Structure first, content second:
   242	
   243	```bash
   244	jq 'type' /mnt/user-data/uploads/data.json
   245	jq 'if type == "array" then length elif type == "object" then keys else . end' /mnt/user-data/uploads/data.json
   246	```
   247	
   248	(`keys` errors on scalar JSON roots — a bare `"hello"` or `42` is valid
   249	JSON per RFC 7159 — so guard the branch.)
   250	
   251	Then drill into what the user actually asked about.
   252	
   253	JSONL (one object per line) — do **not** `jq` the whole file; work line
   254	by line:
   255	
   256	```bash
   257	head -3 /mnt/user-data/uploads/data.jsonl | jq .
   258	wc -l /mnt/user-data/uploads/data.jsonl
   259	```
   260	
   261	---
   262	
   263	## Images (JPG / PNG / GIF / WEBP)
   264	
   265	**You can already see uploaded images.** They are injected into your
   266	context as vision inputs alongside the `<uploaded_files>` pointer. You
   267	do not need to read them from disk to describe them.
   268	
   269	The disk copy is only needed if you are going to **process** the image
   270	programmatically:
   271	
   272	```python
   273	from PIL import Image
   274	img = Image.open("/mnt/user-data/uploads/photo.jpg")
   275	print(img.size, img.mode, img.format)
   276	```
   277	
   278	For OCR on an image (text extraction, not description):
   279	
   280	```python
   281	import pytesseract
   282	print(pytesseract.image_to_string(img))
   283	```
   284	
   285	Note: the client resizes images larger than 2000×2000 down to that
   286	bound and re-encodes as JPEG before upload, so the disk copy may not
   287	be the user's original bytes. For most processing this doesn't matter;
   288	if the user is asking about original-resolution pixel data, flag it.
   289	
   290	---
   291	
   292	## Archives (ZIP / TAR / TAR.GZ)
   293	
   294	**List first. Extract never — unless the user explicitly asks.**
   295	Archives can be huge, contain path traversal, or nest forever.
   296	
   297	```bash
   298	unzip -l /mnt/user-data/uploads/bundle.zip
   299	tar -tf /mnt/user-data/uploads/bundle.tar
   300	```
   301	
   302	GNU tar auto-detects compression — `tar -tf` works on `.tar`,
   303	`.tar.gz`, `.tar.bz2`, `.tar.xz` alike. Don't hard-code `-z`.
   304	
   305	If the user wants one file from inside, extract just that one:
   306	
   307	```bash
   308	unzip -p /mnt/user-data/uploads/bundle.zip path/inside/file.txt
   309	```
   310	
   311	**Standalone `.gz`** (not a tar) compresses a single file — there is
   312	no manifest to list. Just peek at the decompressed content:
   313	
   314	```bash
   315	zcat /mnt/user-data/uploads/data.json.gz | head -50
   316	```
   317	
   318	---
   319	
   320	## EPUB / ODT
   321	
   322	```bash
   323	extract-text /mnt/user-data/uploads/book.epub | head -200
   324	```
   325	
   326	For long ebooks, pipe through `head` — you rarely need the whole thing
   327	to answer a question.
   328	
   329	---
   330	
   331	## RTF / IPYNB
   332	
   333	```bash
   334	extract-text /mnt/user-data/uploads/notes.rtf | head -200
   335	extract-text /mnt/user-data/uploads/notebook.ipynb | head -200
   336	```
   337	
   338	---
   339	
   340	## Plain text / code / logs
   341	
   342	Check the size first:
   343	
   344	```bash
   345	wc -c /mnt/user-data/uploads/app.log
   346	```
   347	
   348	- **Under ~20KB**: `cat` is fine.
   349	- **Over ~20KB**: `head -100` and `tail -100` to orient. If the user
   350	  asked about something specific, `grep` for it. Load the whole thing
   351	  only if you genuinely need all of it.
   352	
   353	For log files, the user almost always cares about the end:
   354	
   355	```bash
   356	tail -200 /mnt/user-data/uploads/app.log
   357	```
   358	
   359	---
   360	
   361	## Unknown extension
   362	
   363	```bash
   364	file /mnt/user-data/uploads/mystery.bin
   365	xxd /mnt/user-data/uploads/mystery.bin | head -5
   366	```
   367	
   368	`file` identifies most things. `xxd` head shows magic bytes. If `file`
   369	says "data" and the hex doesn't match anything you recognize, ask the
   370	user what it is instead of guessing.
   371	{"returncode":0,"stdout":"Archive:  /mnt/user-data/uploads/rigging-market-research.zip\n  Length      Date    Time    Name\n---------  ---------- -----   ----\n        0  2026-06-15 13:19   rigging-market-research/\n    11168  2026-06-15 13:18   rigging-market-research/market_research_data.md\n    14541  2026-06-15 13:18   rigging-market-research/competitive_analysis.md\n    15091  2026-06-15 13:18   rigging-market-research/financial_projections.md\n    13178  2026-06-15 13:18   rigging-market-research/insurance_checklist.md\n    18872  2026-06-15 13:18   rigging-market-research/startup_guide.md\n    22234  2026-06-15 13:19   rigging-market-research/WEBSITE_CASE_STUDY.md\n---------                     -------\n    95084                     7 files\n","stderr":""}{"returncode":0,"stdout":"# Market Research: US Specialized Rigging & Stagehand Services\n\n## Executive Summary\n\nThe US live events industry represents a massive and rapidly growing market opportunity for specialized rigging and stagehand services. With the overall US live events market valued at approximately **$466 billion in 2025** and projected to reach **$651 billion by 2032**, the specialized labor segment—particularly high-skill rigging crews and lead technicians—represents a premium, high-margin niche within this broader ecosystem.\n\n## Market Size & Growth Projections\n\n### Overall Live Events Market\n- **2025 Market Size**: $466.13 billion USD\n- **2026 Market Size**: $489.90 billion USD\n- **2032 Projected Size**: $651.53 billion USD\n- **CAGR (2025-2032)**: Approximately 5.2%\n\n### Live Music & Concert Touring Segment\n- **2025 US Live Music Market**: $19.7 billion USD\n- **2031 Projected Size**: $26.93 billion USD\n- **CAGR (2025-2031)**: 6.45%\n\n### Music Festival Market (North America)\n- **2024 Market Size**: $863.28 million USD\n- **2031 Projected Size**: Significant growth at 22.2% CAGR\n- **Key Insight**: Festival market is one of the fastest-growing segments within live events\n\n### Music Tourism Market (US)\n- **2025 Market Size**: $65.11 billion USD\n- **2033 Projected Size**: $125.54 billion USD\n- **CAGR (2025-2033)**: 8.6%\n\n## Competitive Landscape\n\n### Tier 1: Global Integrated Providers\n**PRG (Production Resource Group)**\n- Services: Full-scale production (rigging, lighting, video, labor, engineering)\n- Reach: Global, with major US presence\n- Notable Clients: Post Malone, Drake, Ghost, major touring acts\n- Positioning: Premium, full-service, high-budget productions\n- Estimated Annual Revenue: $500M+ (global)\n\n**Rhino Staging**\n- Services: Nationwide stagehand labor, rigging, event staffing\n- Reach: All major US cities\n- Positioning: General labor provider with rigging capabilities\n- Market Position: Mid-tier to upper-mid-tier\n\n### Tier 2: Specialized Labor Providers\n**Show Support USA**\n- Services: Certified riggers, event staffing, nationwide coverage\n- Positioning: 24/7 operations, flexible scheduling, fair compensation\n- Reach: Major US cities and regional areas\n- Notable Feature: Crew portal and app for booking management\n\n**Upstaging**\n- Services: Touring production, rigging, crewing\n- Positioning: Specialized touring support\n- Market Position: Premium boutique provider\n\n**Tri-Point Rigging**\n- Services: Equipment rental, rigging solutions, skilled crew hire\n- Notable Clients: U2, Rolling Stones, Green Day, AC/DC, Metallica\n- Positioning: Equipment + labor hybrid model\n\n### Tier 3: Engineering & Consulting\n**Thornton Tomasetti**\n- Services: Rigging engineering, structural load evaluation, venue assessment\n- Positioning: High-level technical consulting for major venues and tours\n- Notable Work: 1,500+ rigging analyses performed\n- Market Position: Premium engineering services\n\n### Market Gap Opportunity\nThe research identifies a clear market gap for a **boutique, specialized traveling crew provider** that focuses exclusively on:\n- ETCP-certified lead riggers and high-skill specialists\n- Traveling teams that move between major festivals and tours\n- Premium positioning with emphasis on safety, certification, and expertise\n- Direct relationships with festival production managers and touring companies\n\n## Labor Market Benchmarks\n\n### Day Rates by Experience Level\n\n| Role | Entry Level | Mid-Level | Senior/Lead |\n|------|------------|-----------|------------|\n| General Stagehand | $200-$250 | $300-$350 | $400-$500 |\n| Certified Rigger | $300-$350 | $400-$500 | $600-$800+ |\n| High-Altitude Specialist | $350-$400 | $450-$550 | $700-$1,000+ |\n| Lead Tech/Rig Manager | $400-$500 | $550-$700 | $800-$1,500+ |\n\n### IATSE Union Rates (Reference)\n- **Pipe Rigging (Local 798)**: $40.20/hour base (approximately $320/8-hour day)\n- **Arena Riggers**: Premium rates for ETCP-certified specialists\n- **Travel Days**: Typically 50% of standard rate\n\n### Industry Insights\n- Non-union festival work typically ranges from $23-$31/hour ($184-$248 for 8-hour day)\n- Specialized touring riggers command premium rates due to ETCP certification and experience\n- Lead technicians on major tours can earn $600-$1,500+ per day\n- Travel days are often compensated at reduced rates (50% of working rate)\n\n## Startup Requirements & Costs\n\n### Legal & Business Structure\n- **Entity Type**: LLC or S-Corp recommended for liability protection\n- **Registration Costs**: $100-$500 (varies by state)\n- **Business License**: $50-$250 annually\n\n### Insurance (Critical)\n- **General Liability**: $1M/$2M coverage = $500-$1,500/year\n- **Riggers Liability**: $1M coverage = $2,000-$5,000/year (covers equipment under care)\n- **Workers' Compensation**: $1,500-$3,000/year (varies by state and payroll)\n- **Total Insurance Budget**: $4,000-$9,500 annually\n\n### Certifications & Training\n- **ETCP Exam Fee**: $650 per person (members of IATSE/ESTA pay reduced rates)\n- **OSHA 30 Certification**: $200-$500 per person\n- **Climbing/Rigging Recertification**: $300-$800 annually per person\n\n### Initial Equipment & Tools\n- **Personal Rigger Kit** (per person): $1,500-$3,000\n  - Harness, lanyard, carabiners, load cells, motor controllers, climbing gear\n- **Team of 5 Riggers**: $7,500-$15,000 in equipment\n\n### Startup Capital Estimate\n- **Year 1 Total**: $20,000-$40,000\n  - Legal/registration: $500\n  - Insurance: $7,000\n  - Certifications (5 people): $4,500\n  - Equipment (5 people): $10,000\n  - Marketing/Website: $2,000\n  - Operating capital: $5,000\n\n## ETCP Certification & Industry Standards\n\n### ETCP Recognized Employer Status\n- **Benefit**: Industry credibility and marketing advantage\n- **Requirements**: Employ ETCP-certified riggers, maintain safety standards, documen
