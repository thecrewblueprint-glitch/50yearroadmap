---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-R.md__chunk-0005",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-R.md",
  "chunk_index": 5,
  "chunk_count_for_source": 9,
  "char_start": 45404,
  "char_end": 57389,
  "source_sha256": "1b268044f9083bea1faae4d2c9aa27ccee5bdf8d0fa03d5c2f743e61007ad496",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

 wb.sheetnames)
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
   371	{"returncode":0,"stdout":"# Proofreading and Course Packet Review Report: Rigging Hardware Identification and Safety Inspection\n\n## General Observations\n\nThis course draft, \"Rigging Hardware Identification and Safety Inspection,\" is an exceptionally strong, highly technical, and rigorously safety-focused document. It successfully translates complex OSHA and ASME standards into clear, actionable guidance for live event professionals. The structure—broken into seven distinct but flowing lessons—is logical and builds knowledge progressively. \n\nThe tone is appropriately serious given the subject matter. It does not talk down to the learner but makes it unequivocally clear that rigging safety rules are non-negotiable. The content is highly relevant to the target audience, addressing specific live event scenarios (e.g., outdoor festivals, time-compressed load-ins) rather than generic warehouse environments. \n\nCrucially, the document adheres strictly to the \"awareness-level\" mandate for beginners while providing the exact technical thresholds (e.g., temperature limits, broken wire counts) that a Competent Person must know. It fits perfectly into The Crew Blueprint's course-packet-first direction, reading as a cohesive manual rather than disjointed LMS slides.\n\n## Detailed Revisions and Edit Comments\n\n### Lesson 1: Introduction to Rigging Hardware\n\n#### Core Components of a Rigging System\n\n**Comment:** This section is clear and effective. No major changes needed.\n\n#### Sling Materials: Not All Slings Are the Same\n\n**Comment:** The table is an excellent way to present this information. The critical point regarding interchangeability is a strong safety message.\n\n### Lesson 2: Understanding Equipment Ratings and Identification\n\n#### Identification Markings: What the Hardware Tells You\n\n**Comment:** This section is clear and effective. No major changes needed.\n\n#### Angle of Loading: When Geometry Reduces Capacity\n\n**Comment:** The explanation of capacity reduction based on angle is critical and well-explained. The practical example makes the math concrete.\n\n### Lesson 3: Pre-Use Safety Inspection Procedures\n\n#### The Two Inspection Classifications\n\n**Comment:** This section is clear and effective. No major changes needed.\n\n#### The Competent Person: A Legally Defined Role\n\n**Comment:** This is a vital distinction. The emphasis on both *knowledge* and *authority* is excellent and corrects a common industry misconception.\n\n### Lesson 4: Diagnosing Damage and Fatigue in Rigging Equipment\n\n#### Wire Rope: Removal Criteria\n\n**Comment:** The specific numbers (10 broken wires, 5 in a strand) are exactly what is needed. The safe inspection technique (using a rag/glove) is a great practical addition.\n\n#### Alloy Chain: Removal Criteria\n\n**Comment:** This section is clear and effective. No major changes needed.\n\n#### Shackles: Removal Criteria\n\n**Comment:** The 10% reduction rule is clearly stated.\n\n### Lesson 5: Adhering to Manufacturer Specifications for Safety\n\n#### Temperature Limits by Material Type\n\n**Comment:** Providing the exact temperature thresholds (200°F and 1,000°F) is crucial. \n\n#### Field Repairs: Prohibited Without Exception\n\n**Comment:** This section is strong and necessary. It directly addresses the temptation to improvise in high-pressure situations.\n\n### Lesson 6: Designing a Safety Inspection Checklist for Live Events\n\n#### Accounting for Live Event Environments\n\n**Comment:** This is where the lesson truly shines for the live event context. Acknowledging the realities of festival environments (moisture, UV, ground contact) makes the training highly practical.\n\n### Lesson 7: Conclusion and Course Summary\n\n#### The Human Error Factor\n\n**Comment:** Citing the statistic that up to 90% of failures are due to human error is a powerful way to underscore the importance of the preceding lessons.\n\n#### Understanding Shock Loading\n\n**Comment:** This is a critical concept that is often misunderstood by beginners. The explanation is clear and highlights why WLL is a ceiling, not a suggestion.\n\n## Required Review Categories\n\n## 1. Proofread Review\n\n## Proofread Notes\n\n- The document is exceptionally clean. No spelling or grammar errors were identified.\n\n- Formatting (bolding, tables) is used effectively to highlight key information.\n\n- The transition between the seven lessons is smooth, creating a unified course packet.\n\n## 2. Structure Review\n\n## Structure Notes\n\n- The progression from basic identification (Lesson 1) to complex concepts like shock loading (Lesson 7) is logical and builds a strong foundation.\n\n- The consistent use of \"What You Will Learn,\" \"Why This Matters,\" \"Key Terms,\" and \"Common Beginner Mistakes\" in each lesson creates a predictable and helpful rhythm for the learner.\n\n- The document flows naturally as a comprehensive training manual.\n\n## 3. Beginner Clarity Review\n\n## Beginner Clarity Notes\n\n- Highly technical concepts (e.g., WLL, Angle of Loading, Bird Caging) are defined clearly without relying on assumed prior knowledge.\n\n- The \"Common Beginner Mistakes\" sections are invaluable for contextualizing the information and addressing real-world pitfalls.\n\n- The distinction between a general crew member and a \"Competent Person\" is made very clear, ensuring beginners understand their boundaries.\n\n## 4.
