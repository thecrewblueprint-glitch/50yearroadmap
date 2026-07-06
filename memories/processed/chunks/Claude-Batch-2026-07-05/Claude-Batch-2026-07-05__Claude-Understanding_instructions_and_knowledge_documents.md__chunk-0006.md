---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-Understanding_instructions_and_knowledge_documents.md__chunk-0006",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-Understanding_instructions_and_knowledge_documents.md",
  "chunk_index": 6,
  "chunk_count_for_source": 8,
  "char_start": 56789,
  "char_end": 68752,
  "source_sha256": "65e87a3d270ee4eac97c07abf8587e5562fbcc5a4f76c918805e0be9b1fe2f8a",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

`extract-text <file>`. It emits markdown for docx/odt/epub (headings,
    49	bold, lists, links, tables), tab-separated rows under `## Sheet:`
    50	headers for xlsx, text under `## Slide N` headers for pptx, fenced
    51	code cells for ipynb, and plain text for rtf. Pass `--format <fmt>`
    52	when the extension is wrong or absent (e.g., `--format xlsx` on an
    53	`.xlsm`). If it errors on a file, `pandoc <file> -t plain` is a
    54	fallback; for xlsx/pptx, fall back to the dedicated skill's
    55	Python-based approach (openpyxl / python-pptx).
    56	
    57	## Dispatch table
    58	
    59	| Extension                         | First move                                           | Dedicated skill                           |
    60	| --------------------------------- | ---------------------------------------------------- | ----------------------------------------- |
    61	| `.pdf`                            | Content inventory (see PDF section)                  | `/mnt/skills/public/pdf-reading/SKILL.md` |
    62	| `.docx`                           | `extract-text`                                       | `/mnt/skills/public/docx/SKILL.md`        |
    63	| `.doc` (legacy)                   | Convert to `.docx` first                             | `/mnt/skills/public/docx/SKILL.md`        |
    64	| `.xlsx`                           | `extract-text`                                       | `/mnt/skills/public/xlsx/SKILL.md`        |
    65	| `.xlsm`                           | `extract-text --format xlsx`                         | `/mnt/skills/public/xlsx/SKILL.md`        |
    66	| `.xls` (legacy)                   | `pd.read_excel(engine="xlrd")` — openpyxl rejects it | `/mnt/skills/public/xlsx/SKILL.md`        |
    67	| `.ods`                            | `pd.read_excel(engine="odf")` — openpyxl rejects it  | `/mnt/skills/public/xlsx/SKILL.md`        |
    68	| `.pptx`                           | `extract-text`                                       | `/mnt/skills/public/pptx/SKILL.md`        |
    69	| `.ppt` (legacy)                   | Convert to `.pptx` first                             | `/mnt/skills/public/pptx/SKILL.md`        |
    70	| `.csv`, `.tsv`                    | `pandas` with `nrows`                                | — (below)                                 |
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
    87	Quick first move — get the page count and determine whether the PDF
    88	has an extractable text layer:
    89	
    90	```bash
    91	pdfinfo /mnt/user-data/uploads/report.pdf
    92	pdffonts /mnt/user-data/uploads/report.pdf
    93	```
    94	
    95	`pdffonts` tells you whether text extraction will work before you try it:
    96	
    97	- **No fonts listed** (empty table, just the header) → the PDF is a
    98	  scan or raster export. `pdftotext` and `PdfReader.extract_text()`
    99	  will return nothing useful. Go straight to page rasterization or OCR
   100	  — see `/mnt/skills/public/pdf-reading/SKILL.md` → "Scanned
   101	  documents".
   102	- **Fonts listed** → there is a text layer; extract it:
   103	  ```bash
   104	  pdftotext -f 1 -l 1 /mnt/user-data/uploads/report.pdf - | head -20
   105	  ```
   106	
   107	The reason to check `pdffonts` first is user-facing: running
   108	`pdftotext` on a scan produces an empty result, and in a visible
   109	transcript that reads as a failed first attempt before you fall back
   110	to OCR. The two-line diagnostic above costs one tool call and avoids
   111	that — you arrive at the right method on the first try, which is what
   112	a user perceives as "it just read my file."
   113	
   114	That also shapes how to open your reply. The diagnostic commands are
   115	plumbing, not content; lead with what the user asked about. On a
   116	scanned receipt that might be "This is a 3-page scanned invoice; the
   117	amount due on page 2 is $1,845.00," and on a digitally-authored report
   118	it might be "The Q3 report runs 28 pages; revenue on p. 4 is $12.3M,
   119	up 9% YoY." What you're steering away from is the "I'll examine the
   120	PDF" / "Let me check if this is extractable" preamble — the answer to
   121	their question is the first thing they should see.
   122	
   123	For anything beyond a quick peek — figures, tables, attachments,
   124	forms, scanned PDFs, visual inspection, or choosing a reading strategy
   125	— go read `/mnt/skills/public/pdf-reading/SKILL.md`. It covers
   126	content inventory, text extraction vs. page rasterization, embedded
   127	content extraction, and document-type-aware reading strategies.
   128	
   129	For PDF form filling, creation, merging, splitting, or watermarking,
   130	go read `/mnt/skills/public/pdf/SKILL.md`.
   131	
   132	---
   133	
   134	## DOCX / DOC
   135	
   136	The `docx` skill covers editing, creating, tracked changes, images.
   137	Read it if you need any of those. For a quick look:
   138	
   139	```bash
   140	extract-text /mnt/user-data/uploads/memo.docx | head -200
   141	```
   142	
   143	Legacy `.doc` (not `.docx`) must be converted first — see the `docx`
   144	skill.
   145	
   146	---
   147	
   148	## XLSX / XLS / spreadsheets
   149	
   150	The `xlsx` skill covers formulas, formatting, charts, creating. Read
   151	it if you need any of those. For a quick look at an `.xlsx`:
   152	
   153	```bash
   154	extract-text /mnt/user-data/uploads/data.xlsx | head -100
   155	```
   156	
   157	For `.xlsm`, add `--format xlsx` (same zip structure; only the
   158	extension differs). When you need a structured preview in Python:
   159	
   160	```python
   161	from openpyxl import load_workbook
   162	wb = load_workbook("/mnt/user-data/uploads/data.xlsx", read_only=True)
   163	print("Sheets:", wb.sheetnames)
   164	ws = wb.active
   165	for row in ws.iter_rows(max_row=5, values_only=True):
   166	    print(row)
   167	```
   168	
   169	`read_only=True` matters — without it, openpyxl loads the entire
   170	workbook into memory, which breaks on large files. Do not trust
   171	`ws.max_row` in read-only mode: many non-Excel writers omit the
   172	dimension record, so it comes back `None` or wrong. If you need a row
   173	count, iterate or use pandas.
   174	
   175	**Legacy `.xls`** — openpyxl raises `InvalidFileException`. Use:
   176	
   177	```python
   178	import pandas as pd
   179	df = pd.read_excel("/mnt/user-data/uploads/old.xls", engine="xlrd", nrows=5)
   180	```
   181	
   182	**`.ods` (OpenDocument)** — openpyxl also rejects this. Use:
   183	
   184	```python
   185	import pandas as pd
   186	df = pd.read_excel("/mnt/user-data/uploads/data.ods", engine="odf", nrows=5)
   187	```
   188	
   189	---
   190	
   191	## PPTX
   192	
   193	```bash
   194	extract-text /mnt/user-data/uploads/deck.pptx | head -200
   195	```
   196	
   197	**Legacy `.ppt`** — convert to `.pptx` first via LibreOffice; see
   198	`/mnt/skills/public/pptx/SKILL.md` for the sandbox-safe
   199	`scripts/office/soffice.py` wrapper (bare `soffice` hangs here because
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
