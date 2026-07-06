---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-Organizing_files_for_new_workflow.md__chunk-0002",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-Organizing_files_for_new_workflow.md",
  "chunk_index": 2,
  "chunk_count_for_source": 5,
  "char_start": 11400,
  "char_end": 23307,
  "source_sha256": "6721daa7a9a91ea720f6569c904968ebcfea7797cc42064b0a7125abcc8cc514",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

 non-Excel writers omit the
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
   192	---
   193	
   194	## PPTX
   195	
   196	```bash
   197	extract-text /mnt/user-data/uploads/deck.pptx | head -200
   198	```
   199	
   200	**Legacy `.ppt`** — convert to `.pptx` first via LibreOffice; see the
   201	`pptx` skill for the sandbox-safe `scripts/office/soffice.py` wrapper
   202	(bare `soffice` hangs here because the seccomp filter blocks the
   203	`AF_UNIX` sockets LibreOffice uses for instance management).
   204	
   205	For anything beyond reading, go to the `pptx` skill.
   206	
   207	---
   208	
   209	## CSV / TSV
   210	
   211	**Do not** `cat` or `head` these blindly. A CSV with a 50KB quoted cell
   212	in row 1 will wreck your `head -5`. Use pandas with `nrows`:
   213	
   214	```python
   215	import pandas as pd
   216	df = pd.read_csv("/mnt/user-data/uploads/data.csv", nrows=5)
   217	print(df)
   218	print()
   219	print(df.dtypes)
   220	```
   221	
   222	Approximate row count without loading (over-counts if the file has
   223	RFC-4180 quoted newlines — the same quoted-cell case this section
   224	warned about above):
   225	
   226	```bash
   227	wc -l /mnt/user-data/uploads/data.csv
   228	```
   229	
   230	Full analysis only after you know the shape:
   231	
   232	```python
   233	df = pd.read_csv("/mnt/user-data/uploads/data.csv")
   234	print(df.describe())
   235	```
   236	
   237	TSV: same, with `sep="\t"`.
   238	
   239	---
   240	
   241	## JSON / JSONL
   242	
   243	Structure first, content second:
   244	
   245	```bash
   246	jq 'type' /mnt/user-data/uploads/data.json
   247	jq 'if type == "array" then length elif type == "object" then keys else . end' /mnt/user-data/uploads/data.json
   248	```
   249	
   250	(`keys` errors on scalar JSON roots — a bare `"hello"` or `42` is valid
   251	JSON per RFC 7159 — so guard the branch.)
   252	
   253	Then drill into what the user actually asked about.
   254	
   255	JSONL (one object per line) — do **not** `jq` the whole file; work line
   256	by line:
   257	
   258	```bash
   259	head -3 /mnt/user-data/uploads/data.jsonl | jq .
   260	wc -l /mnt/user-data/uploads/data.jsonl
   261	```
   262	
   263	---
   264	
   265	## Images (JPG / PNG / GIF / WEBP)
   266	
   267	**You can already see uploaded images.** They are injected into your
   268	context as vision inputs alongside the `<uploaded_files>` pointer. You
   269	do not need to read them from disk to describe them.
   270	
   271	The disk copy is only needed if you are going to **process** the image
   272	programmatically:
   273	
   274	```python
   275	from PIL import Image
   276	img = Image.open("/mnt/user-data/uploads/photo.jpg")
   277	print(img.size, img.mode, img.format)
   278	```
   279	
   280	For OCR on an image (text extraction, not description):
   281	
   282	```python
   283	import pytesseract
   284	print(pytesseract.image_to_string(img))
   285	```
   286	
   287	Note: the client resizes images larger than 2000×2000 down to that
   288	bound and re-encodes as JPEG before upload, so the disk copy may not
   289	be the user's original bytes. For most processing this doesn't matter;
   290	if the user is asking about original-resolution pixel data, flag it.
   291	
   292	---
   293	
   294	## Archives (ZIP / TAR / TAR.GZ)
   295	
   296	**List first. Extract never — unless the user explicitly asks.**
   297	Archives can be huge, contain path traversal, or nest forever.
   298	
   299	```bash
   300	unzip -l /mnt/user-data/uploads/bundle.zip
   301	tar -tf /mnt/user-data/uploads/bundle.tar
   302	```
   303	
   304	GNU tar auto-detects compression — `tar -tf` works on `.tar`,
   305	`.tar.gz`, `.tar.bz2`, `.tar.xz` alike. Don't hard-code `-z`.
   306	
   307	If the user wants one file from inside, extract just that one:
   308	
   309	```bash
   310	unzip -p /mnt/user-data/uploads/bundle.zip path/inside/file.txt
   311	```
   312	
   313	**Standalone `.gz`** (not a tar) compresses a single file — there is
   314	no manifest to list. Just peek at the decompressed content:
   315	
   316	```bash
   317	zcat /mnt/user-data/uploads/data.json.gz | head -50
   318	```
   319	
   320	---
   321	
   322	## EPUB / ODT
   323	
   324	```bash
   325	extract-text /mnt/user-data/uploads/book.epub | head -200
   326	```
   327	
   328	For long ebooks, pipe through `head` — you rarely need the whole thing
   329	to answer a question.
   330	
   331	---
   332	
   333	## RTF / IPYNB
   334	
   335	```bash
   336	extract-text /mnt/user-data/uploads/notes.rtf | head -200
   337	extract-text /mnt/user-data/uploads/notebook.ipynb | head -200
   338	```
   339	
   340	---
   341	
   342	## Plain text / code / logs
   343	
   344	Check the size first:
   345	
   346	```bash
   347	wc -c /mnt/user-data/uploads/app.log
   348	```
   349	
   350	- **Under ~20KB**: `cat` is fine.
   351	- **Over ~20KB**: `head -100` and `tail -100` to orient. If the user
   352	  asked about something specific, `grep` for it. Load the whole thing
   353	  only if you genuinely need all of it.
   354	
   355	For log files, the user almost always cares about the end:
   356	
   357	```bash
   358	tail -200 /mnt/user-data/uploads/app.log
   359	```
   360	
   361	---
   362	
   363	## Unknown extension
   364	
   365	```bash
   366	file /mnt/user-data/uploads/mystery.bin
   367	xxd /mnt/user-data/uploads/mystery.bin | head -5
   368	```
   369	
   370	`file` identifies most things. `xxd` head shows magic bytes. If `file`
   371	says "data" and the hex doesn't match anything you recognize, ask the
   372	user what it is instead of guessing.
   373	Good context. Now let me build you a solid Android folder schema first — clean, practical, and tailored to your two businesses.File created successfully: /mnt/user-data/outputs/ANDROID_FILE_STRUCTURE.mdHere's your Android schema. A few things to note before you implement it:

**The logic behind it:**
- Two clean business roots, personal stays separate, and `INBOX/` acts as a weekly dump-and-sort buffer so random downloads don't pollute your organized folders
- Client folders under Deadhang let you keep gig docs separated by who hired you
- Festival Atlas has its own home under Crew Blueprint since it's a live dev project

**Before you start creating folders on your phone** — do you want me to generate a Termux shell script that builds this entire folder structure automatically in one shot? That's faster than tapping through it manually.

Once you confirm the Android structure looks right, I'll build the Windows + Drive schema to mirror it with sync logic between all three.

---

**[USER]**

For Deadhang Labor LLC folder. In clients. Add all hands on deck as a client.

---

**[ASSISTANT]**

Successfully replaced string in /mnt/user-data/outputs/ANDROID_FILE_STRUCTURE.mdDone — All_Hands_on_Deck is added to the Clients list. Any other clients to add, or are we good to move on to the Windows + Drive schema?

---

**[USER]**

Deadhang labor llc also has a website and should have all website documents sorted however they are needed.

---

**[ASSISTANT]**

Successfully replaced string in /mnt/user-data/outputs/ANDROID_FILE_STRUCTURE.mdAlso going to add the Affirmations calendar project since that lives under the Deadhang site:Successfully replaced string in /mnt/user-data/outputs/ANDROID_FILE_STRUCTURE.mdAdded a full `Website/` folder with subfolders covering source files, images, forms, legal docs, analytics, and backups. I also tucked the Affirmations Calendar in there since it lives at `deadhanglaborllc.com/affirmations` and has its own open bugs to track.

Anything else to add or adjust before we move to Windows and Drive?

---

**[USER]**

Ok. Help me create this folder structure and move all of my phones files without breaking my phone

---

**[ASSISTANT]**

Smart move to be cautious — let's do this right. Before we touch anything, I need to know what we're actually working with on your phone.

**Step 1 — Let's take inventory first.**

Open Termux and run these commands one at a time. Paste the output back here and I'll tell you exactly what to do next.

---

**Check Termux storage access is set up:**
```bash
ls ~/storage/
```

---

**See what's currently in your Internal Storage root:**
```bash
ls ~/storage/shared/
```

---

**Check how much storage is used vs available:**
```bash
df -h ~/storage/shared/
```

---

**See if the old Android File Organizer files are still present:**
```bash
ls ~/
```

---

Once I see those outputs I'll know:
- Whether storage permissions are already granted
- What folders already exist (so we don't overwrite anything)
- How much space we have to work with
- Whether we can reuse the old organizer or need a fresh script

**Do not run any move commands yet.** Inventory first, then we build the script together and do a dry run before anything actually moves. Nothing gets touched until you approve it.

---

**[USER]**



---

**[ASSISTANT]**

Storage permissions aren't granted yet — that's why it can't find the directory. Easy fix. Run this command:

```bash
termux-setup-storage
```

**What will happen:**
Your phone will pop up a permission dialog asking Termux to access your files. **Tap Allow** (or **Allow Access** if it opens a folder picker — select your phone's internal storage root and confirm).

Then run:
```bash
ls ~/storage/shared/
```

Screenshot that output and send it here. That'll show us what's actually on your phone before we touch anything.

---

**[USER]**



---

**[ASSISTANT]**

Good — storage is connected and I can see exactly what we're working with. Here's the situation:

**What I see:**
- 107GB total, 76GB used, 31GB free — plenty of room to work
- Standard Android folders: DCIM, Documents, Download, Music, Pictures, Movies, etc.
- Two mystery folders: `"Why folder"` and `"web apps"` — those need investigating
- No existing business folder structure yet — clean slate

**Before we build anything, let's peek inside the folders that matter.** Run these one at a time and screenshot each:

```bash
ls ~/storage/shared/Documents/
```

```bash
ls ~/storage/shared/Download/
```

```bash
ls ~/storage/shared/DCIM/
```

```bash
ls "~/storage/shared/Why folder/"
```

```bash
ls "~/storage/shared/web apps/"
```

This tells us where your actual files currently live so we know what needs to move where. Don't skip this step — 76GB of used space means there's a lot on this phone and we want to know what it is before we reorganize anything.

---

**[USER]**



---

**[ASSISTANT]**

Now I have a clear picture. Your Download folder is the problem — it's basically your entire phone's working directory with hundreds of unsorted files. Here's what I see:

**What's in there:**
- Deadhang LLC business docs (W9s, operating agreement, business plan, invoices, contracts)
- Crew Blueprint course content (TCB-RIG-201, bridle math, hazard recognition, course packets)
- Festival Atlas files and zip archives
- Android File Organizer versions (multiple duplicates)
- Website files (deadhanglabor-site folder, affirmation calendar)
- Financial docs (1099s, receipts, DB bills)
- Security-sensitive files (`openai-recovery-keys`, `github-recovery-codes.txt`, `backup-codes.txt`)
- UHaul images, FB video, misc junk
- DCIM only has Camera and Facebook — that's clean

**Two things before we write the script:**

---

