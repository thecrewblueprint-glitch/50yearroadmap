---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-WordPress_sitemap_directory_setup.md__chunk-0016",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-WordPress_sitemap_directory_setup.md",
  "chunk_index": 16,
  "chunk_count_for_source": 53,
  "char_start": 161865,
  "char_end": 173037,
  "source_sha256": "94c6fa3b222f9e9d1a3418b26589de902cde3cac997f3b5cfd437f70e74973ff",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

                      |
    71	| `.json`, `.jsonl`                 | `jq` for structure                                   | — (below)                                 |
    72	| `.jpg`, `.png`, `.gif`, `.webp`   | Already in your context as vision input              | — (below)                                 |
    73	| `.zip`, `.tar`, `.tar.gz`         | List contents, do **not** auto-extract               | — (below)                                 |
    74	| `.gz` (single file)               | `zcat \| head` — no manifest to list                 | — (below)                                 |
    75	| `.epub`, `.odt`                   | `extract-text`                                       | — (below)                                 |
    76	| `.rtf`                            | `extract-text`                                       | — (below)                                 |
    77	| `.ipynb`                          | `extract-text`                                       | — (below)                                 |
    78	| `.txt`, `.md`, `.log`, code files | `wc -c` then `head` or full `cat`                    | — (below)                                 |
    79	| Unknown                           | `file` then decide                                   | —                                         |
    80	
    81	---
    82	
    83	## PDF
    84	
    85	**Never** `cat` a PDF — it prints binary garbage.
    86	
    87	Quick first move — get the page count and check if text is extractable:
    88	
    89	```bash
    90	pdfinfo /mnt/user-data/uploads/report.pdf
    91	pdftotext -f 1 -l 1 /mnt/user-data/uploads/report.pdf - | head -20
    92	```
    93	
    94	Then peek at the text content:
    95	
    96	```python
    97	from pypdf import PdfReader
    98	r = PdfReader("/mnt/user-data/uploads/report.pdf")
    99	print(f"{len(r.pages)} pages")
   100	print(r.pages[0].extract_text()[:2000])
   101	```
   102	
   103	For anything beyond a quick peek — figures, tables, attachments,
   104	forms, scanned PDFs, visual inspection, or choosing a reading strategy
   105	— go read `/mnt/skills/public/pdf-reading/SKILL.md`. It covers
   106	content inventory, text extraction vs. page rasterization, embedded
   107	content extraction, and document-type-aware reading strategies.
   108	
   109	For PDF form filling, creation, merging, splitting, or watermarking,
   110	go read `/mnt/skills/public/pdf/SKILL.md`.
   111	
   112	---
   113	
   114	## DOCX / DOC
   115	
   116	The `docx` skill covers editing, creating, tracked changes, images.
   117	Read it if you need any of those. For a quick look:
   118	
   119	```bash
   120	extract-text /mnt/user-data/uploads/memo.docx | head -200
   121	```
   122	
   123	Legacy `.doc` (not `.docx`) must be converted first — see the `docx`
   124	skill.
   125	
   126	---
   127	
   128	## XLSX / XLS / spreadsheets
   129	
   130	The `xlsx` skill covers formulas, formatting, charts, creating. Read
   131	it if you need any of those. For a quick look at an `.xlsx`:
   132	
   133	```bash
   134	extract-text /mnt/user-data/uploads/data.xlsx | head -100
   135	```
   136	
   137	For `.xlsm`, add `--format xlsx` (same zip structure; only the
   138	extension differs). When you need a structured preview in Python:
   139	
   140	```python
   141	from openpyxl import load_workbook
   142	wb = load_workbook("/mnt/user-data/uploads/data.xlsx", read_only=True)
   143	print("Sheets:", wb.sheetnames)
   144	ws = wb.active
   145	for row in ws.iter_rows(max_row=5, values_only=True):
   146	    print(row)
   147	```
   148	
   149	`read_only=True` matters — without it, openpyxl loads the entire
   150	workbook into memory, which breaks on large files. Do not trust
   151	`ws.max_row` in read-only mode: many non-Excel writers omit the
   152	dimension record, so it comes back `None` or wrong. If you need a row
   153	count, iterate or use pandas.
   154	
   155	**Legacy `.xls`** — openpyxl raises `InvalidFileException`. Use:
   156	
   157	```python
   158	import pandas as pd
   159	df = pd.read_excel("/mnt/user-data/uploads/old.xls", engine="xlrd", nrows=5)
   160	```
   161	
   162	**`.ods` (OpenDocument)** — openpyxl also rejects this. Use:
   163	
   164	```python
   165	import pandas as pd
   166	df = pd.read_excel("/mnt/user-data/uploads/data.ods", engine="odf", nrows=5)
   167	```
   168	
   169	---
   170	
   171	## PPTX
   172	
   173	```bash
   174	extract-text /mnt/user-data/uploads/deck.pptx | head -200
   175	```
   176	
   177	**Legacy `.ppt`** — convert to `.pptx` first via LibreOffice; see
   178	`/mnt/skills/public/pptx/SKILL.md` for the sandbox-safe
   179	`scripts/office/soffice.py` wrapper (bare `soffice` hangs here because
   180	the seccomp filter blocks the `AF_UNIX` sockets LibreOffice uses for
   181	instance management).
   182	
   183	For anything beyond reading, go to `/mnt/skills/public/pptx/SKILL.md`.
   184	
   185	---
   186	
   187	## CSV / TSV
   188	
   189	**Do not** `cat` or `head` these blindly. A CSV with a 50KB quoted cell
   190	in row 1 will wreck your `head -5`. Use pandas with `nrows`:
   191	
   192	```python
   193	import pandas as pd
   194	df = pd.read_csv("/mnt/user-data/uploads/data.csv", nrows=5)
   195	print(df)
   196	print()
   197	print(df.dtypes)
   198	```
   199	
   200	Approximate row count without loading (over-counts if the file has
   201	RFC-4180 quoted newlines — the same quoted-cell case this section
   202	warned about above):
   203	
   204	```bash
   205	wc -l /mnt/user-data/uploads/data.csv
   206	```
   207	
   208	Full analysis only after you know the shape:
   209	
   210	```python
   211	df = pd.read_csv("/mnt/user-data/uploads/data.csv")
   212	print(df.describe())
   213	```
   214	
   215	TSV: same, with `sep="\t"`.
   216	
   217	---
   218	
   219	## JSON / JSONL
   220	
   221	Structure first, content second:
   222	
   223	```bash
   224	jq 'type' /mnt/user-data/uploads/data.json
   225	jq 'if type == "array" then length elif type == "object" then keys else . end' /mnt/user-data/uploads/data.json
   226	```
   227	
   228	(`keys` errors on scalar JSON roots — a bare `"hello"` or `42` is valid
   229	JSON per RFC 7159 — so guard the branch.)
   230	
   231	Then drill into what the user actually asked about.
   232	
   233	JSONL (one object per line) — do **not** `jq` the whole file; work line
   234	by line:
   235	
   236	```bash
   237	head -3 /mnt/user-data/uploads/data.jsonl | jq .
   238	wc -l /mnt/user-data/uploads/data.jsonl
   239	```
   240	
   241	---
   242	
   243	## Images (JPG / PNG / GIF / WEBP)
   244	
   245	**You can already see uploaded images.** They are injected into your
   246	context as vision inputs alongside the `<uploaded_files>` pointer. You
   247	do not need to read them from disk to describe them.
   248	
   249	The disk copy is only needed if you are going to **process** the image
   250	programmatically:
   251	
   252	```python
   253	from PIL import Image
   254	img = Image.open("/mnt/user-data/uploads/photo.jpg")
   255	print(img.size, img.mode, img.format)
   256	```
   257	
   258	For OCR on an image (text extraction, not description):
   259	
   260	```python
   261	import pytesseract
   262	print(pytesseract.image_to_string(img))
   263	```
   264	
   265	Note: the client resizes images larger than 2000×2000 down to that
   266	bound and re-encodes as JPEG before upload, so the disk copy may not
   267	be the user's original bytes. For most processing this doesn't matter;
   268	if the user is asking about original-resolution pixel data, flag it.
   269	
   270	---
   271	
   272	## Archives (ZIP / TAR / TAR.GZ)
   273	
   274	**List first. Extract never — unless the user explicitly asks.**
   275	Archives can be huge, contain path traversal, or nest forever.
   276	
   277	```bash
   278	unzip -l /mnt/user-data/uploads/bundle.zip
   279	tar -tf /mnt/user-data/uploads/bundle.tar
   280	```
   281	
   282	GNU tar auto-detects compression — `tar -tf` works on `.tar`,
   283	`.tar.gz`, `.tar.bz2`, `.tar.xz` alike. Don't hard-code `-z`.
   284	
   285	If the user wants one file from inside, extract just that one:
   286	
   287	```bash
   288	unzip -p /mnt/user-data/uploads/bundle.zip path/inside/file.txt
   289	```
   290	
   291	**Standalone `.gz`** (not a tar) compresses a single file — there is
   292	no manifest to list. Just peek at the decompressed content:
   293	
   294	```bash
   295	zcat /mnt/user-data/uploads/data.json.gz | head -50
   296	```
   297	
   298	---
   299	
   300	## EPUB / ODT
   301	
   302	```bash
   303	extract-text /mnt/user-data/uploads/book.epub | head -200
   304	```
   305	
   306	For long ebooks, pipe through `head` — you rarely need the whole thing
   307	to answer a question.
   308	
   309	---
   310	
   311	## RTF / IPYNB
   312	
   313	```bash
   314	extract-text /mnt/user-data/uploads/notes.rtf | head -200
   315	extract-text /mnt/user-data/uploads/notebook.ipynb | head -200
   316	```
   317	
   318	---
   319	
   320	## Plain text / code / logs
   321	
   322	Check the size first:
   323	
   324	```bash
   325	wc -c /mnt/user-data/uploads/app.log
   326	```
   327	
   328	- **Under ~20KB**: `cat` is fine.
   329	- **Over ~20KB**: `head -100` and `tail -100` to orient. If the user
   330	  asked about something specific, `grep` for it. Load the whole thing
   331	  only if you genuinely need all of it.
   332	
   333	For log files, the user almost always cares about the end:
   334	
   335	```bash
   336	tail -200 /mnt/user-data/uploads/app.log
   337	```
   338	
   339	---
   340	
   341	## Unknown extension
   342	
   343	```bash
   344	file /mnt/user-data/uploads/mystery.bin
   345	xxd /mnt/user-data/uploads/mystery.bin | head -5
   346	```
   347	
   348	`file` identifies most things. `xxd` head shows magic bytes. If `file`
   349	says "data" and the hex doesn't match anything you recognize, ask the
   350	user what it is instead of guessing.
   351	{"returncode":0,"stdout":"Course overview\n\n## **Course Title**\n\n**Stagehand Fundamentals: How to Work Your First Load-In, Show Call, and Load-Out**\n\nAlternative titles:\n\n**The Crew Blueprint: Entry-Level Stagehand Training**\n **Concert Crew Basics: A Beginner’s Guide to Live Event Production**\n **Stagehand 101: Safety, Gear, Load-In, Load-Out, and Crew Etiquette**\n\nMy favorite for a public marketplace is:\n\n**Stagehand Fundamentals: How to Work Your First Load-In, Show Call, and Load-Out**\n\nIt is clear, searchable, and beginner-friendly.\n\n## **Course Positioning**\n\nThis should be an **entry-level career-readiness course**, not an official OSHA course.\n\nI would include OSHA-style safety awareness, worker rights, PPE, hazard recognition, and jobsite expectations, but avoid claiming it gives an OSHA card or certification. OSHA says Outreach courses are basic hazard-awareness classes and are not considered certifications or licenses; OSHA cards come from OSHA-authorized trainers after completing 10-hour or 30-hour Outreach classes.\n\nA good disclaimer would be:\n\nThis course is a stagehand orientation and safety-awareness course.
