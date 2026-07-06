---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-WordPress_sitemap_directory_setup.md__chunk-0002",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-WordPress_sitemap_directory_setup.md",
  "chunk_index": 2,
  "chunk_count_for_source": 53,
  "char_start": 11381,
  "char_end": 23295,
  "source_sha256": "94c6fa3b222f9e9d1a3418b26589de902cde3cac997f3b5cfd437f70e74973ff",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

e == "object" then keys else . end' /mnt/user-data/uploads/data.json
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
   351	{"returncode":0,"stdout":"(99, 5)\n['Department', 'Course Title', 'Module 1', 'Module 2', 'Module 3']\n\n      Department               Course Title                 Module 1                   Module 2                       Module 3\n0   General Site     Stagehand Fundamentals     Cable Mgmt & Tool ID   Scenic Handling & Safety         Etiquette & Crew Roles\n1   General Site  Truck Loading & Logistics     Load-in & Truck Pack          Weight & Stacking          Sequencing & Planning\n2   General Site             Jobsite Safety       Hazard Recognition        PPE & Communication  Site Boundaries & Emergencies\n3   General Site       Intro to Live Events   Dept. Roles & Workflow    Venue Types & Timelines            Industry Vocabulary\n4   General Site     Interdisciplinary Comm   Radio & Call Structure      Handoffs & Escalation            Doc Reading & Coord\n5         Safety             OSHA Awareness          OSHA Principles     Hazard & Documentation          Safety Culture & Resp\n6         Safety         Event Safety Fund.   Risk & Crowd Awareness              Weather & PPE            Emergency & Systems\n7         Safety         Hazard Recognition    Hazard Identification               Risk Ranking           Mitigation & Control\n8         Safety         Incident Reporting      Reporting Standards          Timelines & Notes    Escalation & Best Practices\n9         Safety         Emergency Planning      Procedures & Egress             Response Roles             Comm & Contingency\n10        Safety               Crowd Safety       Egress & Occupancy    Public Assembly Hazards          Crowd Flow & Behavior\n11        Safety             Severe Weather       Weather Monitoring      Lightning/Wind Policy         Shelter & Cancellation\n12        Safety           Venue Compliance          Rules & Systems       Signage & Boundaries             Venue Coordination\n13        Safety              PPE Awareness        Types & Use Cases   Limitations & Inspection                Selection & Fit\n14        Safety              Crowd Manager       Observation & Comm         Assembly Standards                Managing Egress\n15        Safety           Insurance Basics            Risk Transfer         Liability & Claims       Responsibility Structure\n16       Rigging             Ground Rigging  Hardware Identification        Inspection Criteria            Motor & Comm Basics\n17       Rigging            Stage Carpentry  Scenic Build Vocabulary     Deck & Modular Systems          Automation & Assembly\n18       Rigging                 Up-Rigging  Fall Protection Systems          Geometry & Rescue           Overhead Hazard Mgmt\n19       Rigging            Site Operations     Temporary Structures     Machinery & Barricades        Load Zones & Site Coord\n20       Rigging               Head Rigging              Vector Math  Load Paths & Distribution             Authority & Theory\n21       Rigging            Applied Physics          Force & Tension    Gravity & Load Capacity        Dynamic/Static Behavior\n22       Rigging                  ETCP Prep       Exam Review & Term        Structural Concepts           Math & Code Strategy\n23       Rigging        CM-ET Motor Service   Op Principles & Brakes              Failure Modes       Maint. & Troubleshooting\n24     Electrics               Basic Theory      Voltage Current Res      AC/DC & Circuit Logic              Grounding & Vocab\n25     Electrics          Three-Phase Power       Three-Phase Theory             Load Balancing        Distro Logic & Concepts\n26     Electrics          Temp Power Distro    Distro & Feeder Paths     Tie-in & Breaker Logic        Routing & System Layout\n27     Electrics            Electrical Code           NEC Compliance          Safe Installation          Temp Power Compliance\n28     Electrics           Generator Basics          Generator Types           Fuel & Grounding           Distro Relationships\n29     Electrics             Load Balancing     Phase & Circuit Plan              Power Mapping          Strategy & Power Math\n","stderr":""}{"returncode":0,"stdout":"<StringArray>\n[  'General Site',         'Safety',        'Rigging',      'Electrics',\n          'Audio',       'Lighting',          'Video', 'Infrastructure',\n     'Production',   'Show Control',  'Business/Risk',     'Leadership']\nLength: 12, dtype: str\n\nDepartment\nAudio             19\nBusiness/Risk     11\nElectrics         10\nGeneral Site       5\nInfrastructure     6\nLeadership         3\nLighting          11\nProduction         4\nRigging            8\nSafety            11\nShow Control       3\nVideo              8\ndtype: int64\n","stderr":""}{"returncode":0,"stdout":"        Department               Course Title                 Module 1                   Module 2                       Module 3\n0     General Site     Stagehand Fundamentals     Cable Mgmt & Tool ID   Scenic Handling & Safety         Etiquette & Crew Roles\n1     General Site  Truck Loading & Logistics     Load-in & Truck Pack          Weight & Stacking          Sequencing & Planning\n2     General Site             Jobsite Safety       Hazard Recognition        PPE & Communication  Site Boundaries & Emergencies\n3     General Site       Intro to Live Events   Dept. Roles & Workflow    Venue Types & Timelines            Industry Vocabulary\n4     General Site     Interdisciplinary Comm   Radio & Call Structure      Handoffs & Escalation            Doc Reading & Coord\n5           Safety             OSHA Awareness          OSHA Principles     Hazard & Documentation          Safety Culture & Resp\n6           Safety         Event Safety Fund.   Risk & Crowd Awareness              Weather & PPE            Emergency & Systems\n7           Safety         Hazard Recognition    Hazard Identification               Risk Ranking           Mitigation & Control\n8           Safety         Incident Reporting      Reporting Standards          Timelines & Notes    Escalation & Best Practices\n9           Safety         Emergency Planning      Procedures & Egress             Response Roles             Comm & Contingency\n10          Safety               Crowd Safety       Egress & Occupancy    Public Assembly Hazards          Crowd Flow & Behavior\n11          Safety             Severe Weather       Weather Monitoring      Lightning/Wind Policy         Shelter & Cancellation\n12          Safety           Venue Compliance          Rules & Systems       Signage & Boundaries             Venue Coordination\n13          Safety              PPE Awareness        Types & Use Cases   Limitations & Inspection                Selection & Fit\n14          Safety              Crowd Manager       Observation & Comm         Assembly Standards                Managing Egress\n15          Safety           Insurance Basics            Risk Transfer         Liability & Claims       Responsibility Structure\n16         Rigging             Ground Rigging  Hardware Identification        Inspection Criteria            Motor & Comm Basics\n17         Rigging            Stage Carpentry  Scenic Build Vocabulary     Deck & Modular Systems          Automation & Assembly\n18         Rigging                 Up-Rigging  Fall Protection Systems          Geometry & Rescue           Overhead Hazard Mgmt\n19         Rigging            Site Operations     Temporary Structures     Machinery & Barricades        Load Zones & Site Coord\n20         Rigging               Head Rigging              Vector Math  Load Paths & Distribution             Authority & Theory\n21         Rigging            Applied Physics          Force & Tension    Gravity & Load Capacity        Dynamic/Static Behavior\n22         Rigging                  ETCP Prep       Exam Review & Term        Structural Concepts           Math & Code Strategy\n23         Rigging        CM-ET Motor Service   Op Principles & Brakes              Failure Modes       Maint.
