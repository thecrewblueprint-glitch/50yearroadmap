---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-Code_review_for_errors_and_security.md__chunk-0002",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-Code_review_for_errors_and_security.md",
  "chunk_index": 2,
  "chunk_count_for_source": 7,
  "char_start": 11400,
  "char_end": 23400,
  "source_sha256": "a53c55b61e675d1e937b744c2636a59161596cd7b83cefb90e959553fc734d29",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

fice uses for
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
   371	{"returncode":0,"stdout":"Archive:  /mnt/user-data/uploads/affirmation-calendar-repo.zip\n  Length      Date    Time    Name\n---------  ---------- -----   ----\n     1069  2026-06-13 01:46   affirmation-calendar/LICENSE\n     1118  2026-06-13 01:46   affirmation-calendar/README.md\n    20889  2026-06-13 01:46   affirmation-calendar/index.html\n---------                     -------\n    23076                     3 files\n","stderr":""}{"returncode":0,"stdout":"<!doctype html>\n<html lang=\"en\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n  <meta name=\"description\" content=\"Generate a 365-day positive affirmation calendar as a single ICS file.\">\n  <title>365-Day Affirmation Calendar</title>\n  <style>\n    :root {\n      color-scheme: light dark;\n      font-family: system-ui, -apple-system, BlinkMacSystemFont, \"Segoe UI\", sans-serif;\n      background: #f4f5f7;\n      color: #17181a;\n    }\n\n    * { box-sizing: border-box; }\n\n    body {\n      min-height: 100vh;\n      margin: 0;\n      display: grid;\n      place-items: center;\n      padding: 1.25rem;\n      background:\n        radial-gradient(circle at top, rgba(114, 86, 255, 0.12), transparent 42%),\n        #f4f5f7;\n    }\n\n    main {\n      width: min(100%, 42rem);\n      padding: clamp(1.5rem, 5vw, 3rem);\n      text-align: center;\n      background: rgba(255, 255, 255, 0.92);\n      border: 1px solid rgba(20, 22, 26, 0.10);\n      border-radius: 1.25rem;\n      box-shadow: 0 1.25rem 3rem rgba(20, 22, 26, 0.10);\n    }\n\n    h1 {\n      margin: 0 0 0.75rem;\n      font-size: clamp(2rem, 7vw, 3.5rem);\n      line-height: 1.05;\n      letter-spacing: -0.04em;\n    }\n\n    p {\n      max-width: 34rem;\n      margin: 0 auto 1.75rem;\n      color: #5b6069;\n      line-height: 1.6;\n    }\n\n    button {\n      width: min(100%, 31rem);\n      min-height: 3.5rem;\n      padding: 0.9rem 1.25rem;\n      border: 0;\n      border-radius: 0.8rem;\n      background: #5a45e8;\n      color: #fff;\n      font: inherit;\n      font-weight: 750;\n      cursor: pointer;\n      box-shadow: 0 0.65rem 1.3rem rgba(90, 69, 232, 0.28);\n      transition: transform 150ms ease, box-shadow 150ms ease, background 150ms ease;\n    }\n\n    button:hover {\n      background: #4936d0;\n      box-shadow: 0 0.8rem 1.5rem rgba(90, 69, 232, 0.34);\n      transform: translateY(-1px);\n    }\n\n    button:focus-visible {\n      outline: 3px solid #17181a;\n      outline-offset: 4px;\n    }\n\n    button:active { transform: translateY(0); }\n\n    #status {\n      min-height: 1.5rem;\n      margin-top: 1rem;\n      margin-bottom: 0;\n      font-size: 0.95rem;\n      color: #3f4450;\n    }\n\n    @media (prefers-reduced-motion: reduce) {\n      button { transition: none; }\n    }\n\n    @media (prefers-color-scheme: dark) {\n      :root {\n        background: #101114;\n        color: #f5f6f8;\n      }\n\n      body {\n        background:\n          radial-gradient(circle at top, rgba(130, 108, 255, 0.18), transparent 42%),\n          #101114;\n      }\n\n      main {\n        background: rgba(27, 29, 34, 0.94);\n        border-color: rgba(255, 255, 255, 0.10);\n        box-shadow: 0 1.25rem 3rem rgba(0, 0, 0, 0.35);\n      }\n\n      p, #status { color: #b8bdc7; }\n      button:focus-visible { outline-color: #fff; }\n    }\n  </style>\n</head>\n<body>\n  <main>\n    <h1>365 Days of Affirmations</h1>\n    <p>\n      Generate one calendar file containing a different all-day affirmation\n      for every day, beginning tomorrow.\n    </p>\n\n    <button id=\"generateButton\" type=\"button\">\n      Generate My 365-Day Affirmation Calendar\n    </button>\n\n    <p id=\"status\" role=\"status\" aria-live=\"polite\"></p>\n  </main>\n\n  <script>\n    (() => {\n      \"use strict\";\n\n      const affirmations = [\n      \"I am calm today.\",\n      \"I choose to be calm today.\",\n      \"I remain calm today.\",\n      \"I grow more calm today.\",\n      \"I welcome being calm today.\",\n      \"I am capable today.\",\n      \"I choose to be capable today.\",\n      \"I remain capable today.\",\n      \"I grow more capable today.\",\n      \"I welcome being capable today.\",\n      \"I am confident today.\",\n      \"I choose to be confident today.\",\n      \"I remain confident today.\",\n      \"I grow more confident today.\",\n      \"I welcome being confident today.\",\n      \"I am courageous today.\",\n      \"I choose to be courageous today.\",\n      \"I remain courageous today.\",\n      \"I grow more courageous today.\",\n      \"I welcome being courageous today.\",\n      \"I am creative today.\",\n      \"I choose to be creative today.\",\n      \"I remain creative today.\",\n      \"I grow more creative today.\",\n      \"I welcome being creative today.\",\n      \"I am disciplined today.\",\n      \"I choose to be disciplined today.\",\n      \"I remain disciplined today.\",\n      \"I grow more disciplined today.\",\n      \"I welcome being disciplined today.\",\n      \"I am focused today.\",\n      \"I choose to be focused today.\",\n      \"I remain focused today.\",\n      \"I grow more focused today.\",\n      \"I welcome being focused today.\",\n      \"I am grateful today.\",\n      \"I choose to be grateful today.\",\n      \"I remain grateful today.\",\n      \"I grow more grateful today.\",\n      \"I welcome being grateful today.\",\n      \"I am grounded today.\",\n      \"I choose to be grounded today.\",\n      \"I remain grounded today.\",\n      \"I grow more grounded today.\",\n      \"I welcome being grounded today.\",\n      \"I am hopeful today.\",\n      \"I choose to be hopeful today.\",\n      \"I remain hopeful today.\",\n      \"I grow more hopeful today.\",\n      \"I welcome being hopeful today.\",\n      \"I am patient today.\",\n      \"I choose to be patient today.\",\n      \"I remain patient today.\",\n      \"I grow more patient today.\",\n      \"I welcome being patient today.\",\n      \"I am peaceful today.\",\n      \"I choose to be peaceful today.\",\n      \"I remain peaceful today.\",\n      \"I grow more peaceful today.\",\n      \"I welcome being peaceful today.\",\n      \"I am prepared today.\",\n      \"I choose to be prepared today.\",\n      \"I remain prepared today.\",\n      \"I grow more prepared today.\",\n      \"I welcome being prepared today.\",\n      \"I am resilient today.\",\n      \"I choose to be resilient today.\",\n      \"I remain resilient today.\",\n      \"I grow more resilient today.\",\n      \"I welcome being resilient today.\",\n      \"I am resourceful today.\",\n      \"I choose to be resourceful today.\",\n      \"I remain resourceful today.\",\n      \"I grow more resourceful today.\"
