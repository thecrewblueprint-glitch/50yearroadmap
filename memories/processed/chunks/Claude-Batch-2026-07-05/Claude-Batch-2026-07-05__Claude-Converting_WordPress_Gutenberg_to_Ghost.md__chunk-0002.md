---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-Converting_WordPress_Gutenberg_to_Ghost.md__chunk-0002",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-Converting_WordPress_Gutenberg_to_Ghost.md",
  "chunk_index": 2,
  "chunk_count_for_source": 10,
  "char_start": 11395,
  "char_end": 20437,
  "source_sha256": "01f1d18c2a5e4f24238c921db4b6c64ceabbad019ef2f19537baf0f40c8d4384",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

ve):
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
   351	{"returncode":0,"stdout":"51011 /mnt/user-data/uploads/crew-blueprint-gutenberg-blocks.html\n 3556 /mnt/user-data/uploads/crew-blueprint-functions-snippet_php.txt\n13550 /mnt/user-data/uploads/crew-blueprint-additional-css.css\n68117 total\n","stderr":""}{"returncode":0,"stdout":"<!-- ============================================================\n     THE CREW BLUEPRINT — Gutenberg Block Markup\n     HOW TO USE:\n     1. Create a new Page in WordPress.\n     2. Click ⋮ (top-right) → \"Code editor\" (or press Ctrl+Shift+Alt+M).\n     3. Select all existing text, delete it, paste this entire file.\n     4. Switch back to Visual editor and publish.\n     5. Add the companion CSS from crew-blueprint-theme-css.css\n        to Appearance → Customize → Additional CSS.\n     ============================================================ -->\n\n\n<!-- ═══════════════════════════════════════════════\n     HERO SECTION\n════════════════════════════════════════════════ -->\n\n<!-- wp:cover {\"overlayColor\":\"tcb-black\",\"minHeight\":100,\"minHeightUnit\":\"vh\",\"align\":\"full\",\"className\":\"tcb-hero\"} -->\n<div class=\"wp-block-cover alignfull tcb-hero\" style=\"min-height:100vh\">\n  <span aria-hidden=\"true\" class=\"wp-block-cover__background has-tcb-black-background-color has-background-dim-100 has-background-dim\"></span>\n  <div class=\"wp-block-cover__inner-container\">\n\n    <!-- wp:group {\"layout\":{\"type\":\"constrained\",\"contentSize\":\"900px\"},\"className\":\"tcb-hero__inner\"} -->\n    <div class=\"wp-block-group tcb-hero__inner\">\n\n      <!-- wp:paragraph {\"className\":\"tcb-eyebrow\",\"align\":\"center\"} -->\n      <p class=\"tcb-eyebrow has-text-align-center\">Senior Web Architect &amp; Content Strategist Deliverable</p>\n      <!-- /wp:paragraph -->\n\n      <!-- wp:heading {\"level\":1,\"textAlign\":\"center\",\"className\":\"tcb-display-title\"} -->\n      <h1 class=\"wp-block-heading has-text-align-center tcb-display-title\">THE CREW<br><span class=\"tcb-amber\">BLUEPRINT</span></h1>\n      <!-- /wp:heading -->\n\n      <!-- wp:paragraph {\"align\":\"center\",\"className\":\"tcb-hero__sub\"} -->\n      <p class=\"has-text-align-center tcb-hero__sub\">Production &amp; Staging Resource Hub — Complete build package including site architecture, safety manifesto, career roadmap, and SEO strategy.</p>\n      <!-- /wp:paragraph -->\n\n      <!-- wp:buttons {\"layout\":{\"type\":\"flex\",\"justifyContent\":\"center\"},\"className\":\"tcb-btn-row\"} -->\n      <div class=\"wp-block-buttons tcb-btn-row\">\n        <!-- wp:button {\"className\":\"tcb-btn tcb-btn--primary\"} -->\n        <div class=\"wp-block-button tcb-btn tcb-btn--primary\"><a class=\"wp-block-button__link\" href=\"#sitemap\">View Architecture</a></div>\n        <!-- /wp:button -->\n        <!-- wp:button {\"className\":\"tcb-btn tcb-btn--ghost\"} -->\n        <div class=\"wp-block-button tcb-btn tcb-btn--ghost\"><a class=\"wp-block-button__link\" href=\"#manifesto\">Read the Manifesto</a></div>\n        <!-- /wp:button -->\n      </div>\n      <!-- /wp:buttons -->\n\n    </div>\n    <!-- /wp:group -->\n  </div>\n</div>\n<!-- /wp:cover -->\n\n\n<!-- ═══════════════════════════════════════════════\n     SECTION DIVIDER\n════════════════════════════════════════════════ -->\n<!-- wp:separator {\"className\":\"tcb-divider\",\"align\":\"full\"} -->\n<hr class=\"wp-block-separator tcb-divider alignfull\"/>\n<!-- /wp:separator -->\n\n\n<!-- ═══════════════════════════════════════════════\n     SECTION 01 — SITE ARCHITECTURE / SITEMAP\n════════════════════════════════════════════════ -->\n\n<!-- wp:group {\"anchor\":\"sitemap\",\"backgroundColor\":\"tcb-steel\",\"align\":\"full\",\"className\":\"tcb-section tcb-section--sitemap\",\"layout\":{\"type\":\"constrained\",\"contentSize\":\"1200px\"}} -->\n<div id=\"sitemap\" class=\"wp-block-group alignfull tcb-section tcb-section--sitemap has-tcb-steel-background-color has-background\">\n\n  <!-- wp:paragraph {\"className\":\"tcb-section-label\"} -->\n  <p class=\"tcb-section-label\">Section 01 — WordPress / WooCommerce</p>\n  <!-- /wp:paragraph -->\n\n  <!-- wp:heading {\"level\":2,\"className\":\"tcb-section-title\"} -->\n  <h2 class=\"wp-block-heading tcb-section-title\">SITE ARCHITECTURE</h2>\n  <!-- /wp:heading -->\n\n  <!-- wp:paragraph {\"className\":\"tcb-section-intro\"} -->\n  <p class=\"tcb-section-intro\">Full sitemap for The Crew Blueprint. Structured for SEO authority, user journey clarity, and WooCommerce integration.
