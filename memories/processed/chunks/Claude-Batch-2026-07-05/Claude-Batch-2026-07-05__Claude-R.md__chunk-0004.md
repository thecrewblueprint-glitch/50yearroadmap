---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-R.md__chunk-0004",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-R.md",
  "chunk_index": 4,
  "chunk_count_for_source": 9,
  "char_start": 34015,
  "char_end": 46004,
  "source_sha256": "1b268044f9083bea1faae4d2c9aa27ccee5bdf8d0fa03d5c2f743e61007ad496",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

rth the pick. Retire the gear, document it, and replace it.

The goal of this course is not to produce riggers who know the rules. It is to produce riggers who understand why the rules exist — and who apply them consistently, even under pressure, even at the end of a long call, even when no one is watching.

That is what a safe rigging culture looks like. That is the standard.

---

#### Key Terms

**Shock Loading** — The sudden, rapid application of force to rigging equipment, typically caused by abrupt engagement of loads, dropped loads that jerk to a stop, or dynamic movement during a lift. Shock loading can generate forces that significantly exceed the static weight of the load and may cause immediate failure of hardware that appears to be within its rated capacity.

---

#### Common Beginner Mistakes

**Treating inspection as a setup task rather than a daily practice.** Rigging inspection is not something that happens once at the start of a run and is then considered complete. It is a pre-use requirement for every shift, every day. The load you inspected yesterday was moved, transported, and handled overnight. Inspect it again.

---

*Lesson 7 of 7 — Rigging Hardware Identification and Safety Inspection*

---

*Course complete. All lesson content was developed from source-verified research facts. No removal criteria, temperature thresholds, capacity reduction figures, or accident statistics were invented or estimated beyond the cited source material.*

---

**[USER]**



---

**[ASSISTANT]**

Let me read the uploaded file first.     1	---
     2	name: file-reading
     3	description: "Use this skill when a file has been uploaded but its content is NOT in your context — only its path at /mnt/user-data/uploads/ is listed in an uploaded_files block. This skill is a router: it tells you which tool to use for each file type (pdf, docx, xlsx, csv, json, images, archives, ebooks) so you read the right amount the right way instead of blindly running cat on a binary. Triggers: any mention of /mnt/user-data/uploads/, an uploaded_files section, a file_path tag, or a user asking about an uploaded file you have not yet read. Do NOT use this skill if the file content is already visible in your context inside a documents block — you already have it."
     4	compatibility: "claude.ai, Claude Desktop, Cowork — any surface where uploads land at /mnt/user-data/uploads/"
     5	license: Proprietary. LICENSE.txt has complete terms
     6	---
     7	
     8	# Reading Uploaded Files
     9	
    10	## Why this skill exists
    11	
    12	When a user uploads a file in claude.ai, Claude Desktop, or Cowork,
    13	the file is written to `/mnt/user-data/uploads/<filename>` and you are told the path
    14	in an `<uploaded_files>` block. **The content is not in your context.**
    15	You must go read it.
    16	
    17	The naive thing — `cat /mnt/user-data/uploads/whatever` — is wrong for
    18	most files:
    19	
    20	- On a PDF it prints binary garbage.
    21	- On a 100MB CSV it floods your context with rows you will never use.
    22	- On a DOCX it prints the raw ZIP bytes.
    23	- On an image it does nothing useful at all.
    24	
    25	This skill tells you the right first move for each type, and when to
    26	hand off to a deeper skill.
    27	
    28	## General protocol
    29	
    30	1. **Look at the extension.** That is your dispatch key.
    31	2. **Stat before you read.** Large files need sampling, not slurping.
    32	   ```bash
    33	   stat -c '%s bytes, %y' /mnt/user-data/uploads/report.pdf
    34	   file /mnt/user-data/uploads/report.pdf
    35	   ```
    36	3. **Read just enough to answer the user's question.** If they asked
    37	   "how many rows are in this CSV", don't load the whole thing into
    38	   pandas — `wc -l` gives a fast approximation (it counts newlines,
    39	   not CSV records, so it may over-count if quoted fields contain
    40	   embedded newlines).
    41	4. **If a dedicated skill exists, go read it.** The table below tells
    42	   you when. The dedicated skills cover editing, creating, and advanced
    43	   operations that this skill does not.
    44	
    45	## `extract-text`
    46	
    47	For docx, odt, epub, xlsx, pptx, rtf, and ipynb the first move is
    48	`extract-text <file>`. It emits markdown for docx/odt/epub (headings,
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
