---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-Organizing_files_for_new_workflow.md__chunk-0001",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-Organizing_files_for_new_workflow.md",
  "chunk_index": 1,
  "chunk_count_for_source": 5,
  "char_start": 0,
  "char_end": 12000,
  "source_sha256": "6721daa7a9a91ea720f6569c904968ebcfea7797cc42064b0a7125abcc8cc514",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

Original URL: https://claude.ai/chat/883ca9fa-5e74-4ec9-a599-62460678434d
Conversation Time: 6/28/2026, 9:25:46 PM
Export Time: 7/5/2026, 4:49:47 PM

**[USER]**

I need my files organized so I can continue working on projects in the new workflo I have begun

---

**[ASSISTANT]**

To point you in the right direction, what files or projects are we working with?

What type of organization do you need — by project, by file type, by client, something else?

---

**[USER]**

Thecrewblueprint and deadhang labor llc. And just the files on my phone and in my computer and my drive are all scattered and disorganized and I need to fix that so I can streamline my work

---

**[ASSISTANT]**

Got it. Before I build you an organization system, let me make sure I'm working with what actually exists.

A few quick questions — just pick what applies:

**1. What devices/locations are we dealing with?**
- Android phone (Termux-accessible)
- Laptop/desktop (Windows or Mac?)
- Google Drive

**2. For the phone specifically** — are we picking up where the Android File Organizer (Termux) left off, or starting fresh?

**3. What's the biggest pain point right now?**
- Can't find files when you need them
- Duplicates everywhere
- No consistent folder naming
- Work/personal files mixed together
- All of the above

One question: do you want a **single unified folder schema** that mirrors across phone, computer, and Drive — or do each of those need their own logic based on how you actually use them?

---

**[USER]**

Let's start something fresh. I need android first then windows and drive.

---

**[ASSISTANT]**

Let's do it clean from scratch.     1	---
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
    59	Where a dedicated skill is named below, invoke it by name if you have a
    60	Skill tool, or Read its SKILL.md (listed in your available skills, or in
    61	the same skills directory as this file).
    62	
    63	| Extension                         | First move                                           | Dedicated skill |
    64	| --------------------------------- | ---------------------------------------------------- | --------------- |
    65	| `.pdf`                            | Content inventory (see PDF section)                  | `pdf-reading`   |
    66	| `.docx`                           | `extract-text`                                       | `docx`          |
    67	| `.doc` (legacy)                   | Convert to `.docx` first                             | `docx`          |
    68	| `.xlsx`                           | `extract-text`                                       | `xlsx`          |
    69	| `.xlsm`                           | `extract-text --format xlsx`                         | `xlsx`          |
    70	| `.xls` (legacy)                   | `pd.read_excel(engine="xlrd")` — openpyxl rejects it | `xlsx`          |
    71	| `.ods`                            | `pd.read_excel(engine="odf")` — openpyxl rejects it  | `xlsx`          |
    72	| `.pptx`                           | `extract-text`                                       | `pptx`          |
    73	| `.ppt` (legacy)                   | Convert to `.pptx` first                             | `pptx`          |
    74	| `.csv`, `.tsv`                    | `pandas` with `nrows`                                | — (below)       |
    75	| `.json`, `.jsonl`                 | `jq` for structure                                   | — (below)       |
    76	| `.jpg`, `.png`, `.gif`, `.webp`   | Already in your context as vision input              | — (below)       |
    77	| `.zip`, `.tar`, `.tar.gz`         | List contents, do **not** auto-extract               | — (below)       |
    78	| `.gz` (single file)               | `zcat \| head` — no manifest to list                 | — (below)       |
    79	| `.epub`, `.odt`                   | `extract-text`                                       | — (below)       |
    80	| `.rtf`                            | `extract-text`                                       | — (below)       |
    81	| `.ipynb`                          | `extract-text`                                       | — (below)       |
    82	| `.txt`, `.md`, `.log`, code files | `wc -c` then `head` or full `cat`                    | — (below)       |
    83	| Unknown                           | `file` then decide                                   | —               |
    84	
    85	---
    86	
    87	## PDF
    88	
    89	**Never** `cat` a PDF — it prints binary garbage.
    90	
    91	Quick first move — get the page count and determine whether the PDF
    92	has an extractable text layer:
    93	
    94	```bash
    95	pdfinfo /mnt/user-data/uploads/report.pdf
    96	pdffonts /mnt/user-data/uploads/report.pdf
    97	```
    98	
    99	`pdffonts` tells you whether text extraction will work before you try it:
   100	
   101	- **No fonts listed** (empty table, just the header) → the PDF is a
   102	  scan or raster export. `pdftotext` and `PdfReader.extract_text()`
   103	  will return nothing useful. Go straight to page rasterization or OCR
   104	  — see the `pdf-reading` skill → "Scanned documents".
   105	- **Fonts listed** → there is a text layer; extract it:
   106	  ```bash
   107	  pdftotext -f 1 -l 1 /mnt/user-data/uploads/report.pdf - | head -20
   108	  ```
   109	
   110	The reason to check `pdffonts` first is user-facing: running
   111	`pdftotext` on a scan produces an empty result, and in a visible
   112	transcript that reads as a failed first attempt before you fall back
   113	to OCR. The two-line diagnostic above costs one tool call and avoids
   114	that — you arrive at the right method on the first try, which is what
   115	a user perceives as "it just read my file."
   116	
   117	That also shapes how to open your reply. The diagnostic commands are
   118	plumbing, not content; lead with what the user asked about. On a
   119	scanned receipt that might be "This is a 3-page scanned invoice; the
   120	amount due on page 2 is $1,845.00," and on a digitally-authored report
   121	it might be "The Q3 report runs 28 pages; revenue on p. 4 is $12.3M,
   122	up 9% YoY." What you're steering away from is the "I'll examine the
   123	PDF" / "Let me check if this is extractable" preamble — the answer to
   124	their question is the first thing they should see.
   125	
   126	For anything beyond a quick peek — figures, tables, attachments,
   127	forms, scanned PDFs, visual inspection, or choosing a reading strategy
   128	— go read the `pdf-reading` skill. It covers content inventory, text
   129	extraction vs. page rasterization, embedded content extraction, and
   130	document-type-aware reading strategies.
   131	
   132	For PDF form filling, creation, merging, splitting, or watermarking,
   133	go read the `pdf` skill.
   134	
   135	---
   136	
   137	## DOCX / DOC
   138	
   139	The `docx` skill covers editing, creating, tracked changes, images.
   140	Read it if you need any of those. For a quick look:
   141	
   142	```bash
   143	extract-text /mnt/user-data/uploads/memo.docx | head -200
   144	```
   145	
   146	Legacy `.doc` (not `.docx`) must be converted first — see the `docx`
   147	skill.
   148	
   149	---
   150	
   151	## XLSX / XLS / spreadsheets
   152	
   153	The `xlsx` skill covers formulas, formatting, charts, creating. Read
   154	it if you need any of those. For a quick look at an `.xlsx`:
   155	
   156	```bash
   157	extract-text /mnt/user-data/uploads/data.xlsx | head -100
   158	```
   159	
   160	For `.xlsm`, add `--format xlsx` (same zip structure; only the
   161	extension differs). When you need a structured preview in Python:
   162	
   163	```python
   164	from openpyxl import load_workbook
   165	wb = load_workbook("/mnt/user-data/uploads/data.xlsx", read_only=True)
   166	print("Sheets:", wb.sheetnames)
   167	ws = wb.active
   168	for row in ws.iter_rows(max_row=5, values_only=True):
   169	    print(row)
   170	```
   171	
   172	`read_only=True` matters — without it, openpyxl loads the entire
   173	workbook into memory, which breaks on large files. Do not trust
   174	`ws.max_row` in read-only mode: many non-Excel writers omit the
   175	dimension record, so it comes back `None` or wrong. If you need a row
   176	count, iterate or use pandas.
   177	
   178	**Legacy `.xls`** — openpyxl raises `InvalidFileException`. Use:
   179	
   180	```python
   181	import pandas as pd
   182	df = pd.read_excel("/mnt/user-data/uploads/old.xls", engine="xlrd", nrows=5)
   183	```
   184	
   185	**`.ods` (OpenDocument)** — openpyxl also rejects this. Use:
   186	
   187	```python
   188	import pandas as pd
   189	df = pd.read_excel("/mnt/user-data/uploads/data.ods", engine="odf", nrows=5)
   190	```
   191	
