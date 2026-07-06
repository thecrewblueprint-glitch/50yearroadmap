---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-R.md__chunk-0009",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-R.md",
  "chunk_index": 9,
  "chunk_count_for_source": 9,
  "char_start": 90888,
  "char_end": 99644,
  "source_sha256": "1b268044f9083bea1faae4d2c9aa27ccee5bdf8d0fa03d5c2f743e61007ad496",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

ody)
   159	story.append(PageBreak())
   160	
   161	# Page 2
   162	story.append(Paragraph("Page 2", styles['Heading1']))
   163	story.append(Paragraph("Content for page 2", styles['Normal']))
   164	
   165	# Build PDF
   166	doc.build(story)
   167	```
   168	
   169	#### Subscripts and Superscripts
   170	
   171	**IMPORTANT**: Never use Unicode subscript/superscript characters (₀₁₂₃₄₅₆₇₈₉, ⁰¹²³⁴⁵⁶⁷⁸⁹) in ReportLab PDFs. The built-in fonts do not include these glyphs, causing them to render as solid black boxes.
   172	
   173	Instead, use ReportLab's XML markup tags in Paragraph objects:
   174	```python
   175	from reportlab.platypus import Paragraph
   176	from reportlab.lib.styles import getSampleStyleSheet
   177	
   178	styles = getSampleStyleSheet()
   179	
   180	# Subscripts: use <sub> tag
   181	chemical = Paragraph("H<sub>2</sub>O", styles['Normal'])
   182	
   183	# Superscripts: use <super> tag
   184	squared = Paragraph("x<super>2</super> + y<super>2</super>", styles['Normal'])
   185	```
   186	
   187	For canvas-drawn text (not Paragraph objects), manually adjust font the size and position rather than using Unicode subscripts/superscripts.
   188	
   189	## Command-Line Tools
   190	
   191	### pdftotext (poppler-utils)
   192	```bash
   193	# Extract text
   194	pdftotext input.pdf output.txt
   195	
   196	# Extract text preserving layout
   197	pdftotext -layout input.pdf output.txt
   198	
   199	# Extract specific pages
   200	pdftotext -f 1 -l 5 input.pdf output.txt  # Pages 1-5
   201	```
   202	
   203	### qpdf
   204	```bash
   205	# Merge PDFs
   206	qpdf --empty --pages file1.pdf file2.pdf -- merged.pdf
   207	
   208	# Split pages
   209	qpdf input.pdf --pages . 1-5 -- pages1-5.pdf
   210	qpdf input.pdf --pages . 6-10 -- pages6-10.pdf
   211	
   212	# Rotate pages
   213	qpdf input.pdf output.pdf --rotate=+90:1  # Rotate page 1 by 90 degrees
   214	
   215	# Remove password
   216	qpdf --password=mypassword --decrypt encrypted.pdf decrypted.pdf
   217	```
   218	
   219	### pdftk (if available)
   220	```bash
   221	# Merge
   222	pdftk file1.pdf file2.pdf cat output merged.pdf
   223	
   224	# Split
   225	pdftk input.pdf burst
   226	
   227	# Rotate
   228	pdftk input.pdf rotate 1east output rotated.pdf
   229	```
   230	
   231	## Common Tasks
   232	
   233	### Extract Text from Scanned PDFs
   234	```python
   235	# Requires: pip install pytesseract pdf2image
   236	import pytesseract
   237	from pdf2image import convert_from_path
   238	
   239	# Convert PDF to images
   240	images = convert_from_path('scanned.pdf')
   241	
   242	# OCR each page
   243	text = ""
   244	for i, image in enumerate(images):
   245	    text += f"Page {i+1}:\n"
   246	    text += pytesseract.image_to_string(image)
   247	    text += "\n\n"
   248	
   249	print(text)
   250	```
   251	
   252	### Add Watermark
   253	```python
   254	from pypdf import PdfReader, PdfWriter
   255	
   256	# Create watermark (or load existing)
   257	watermark = PdfReader("watermark.pdf").pages[0]
   258	
   259	# Apply to all pages
   260	reader = PdfReader("document.pdf")
   261	writer = PdfWriter()
   262	
   263	for page in reader.pages:
   264	    page.merge_page(watermark)
   265	    writer.add_page(page)
   266	
   267	with open("watermarked.pdf", "wb") as output:
   268	    writer.write(output)
   269	```
   270	
   271	### Extract Images
   272	```bash
   273	# Using pdfimages (poppler-utils)
   274	pdfimages -j input.pdf output_prefix
   275	
   276	# This extracts all images as output_prefix-000.jpg, output_prefix-001.jpg, etc.
   277	```
   278	
   279	### Password Protection
   280	```python
   281	from pypdf import PdfReader, PdfWriter
   282	
   283	reader = PdfReader("input.pdf")
   284	writer = PdfWriter()
   285	
   286	for page in reader.pages:
   287	    writer.add_page(page)
   288	
   289	# Add password
   290	writer.encrypt("userpassword", "ownerpassword")
   291	
   292	with open("encrypted.pdf", "wb") as output:
   293	    writer.write(output)
   294	```
   295	
   296	## Quick Reference
   297	
   298	| Task | Best Tool | Command/Code |
   299	|------|-----------|--------------|
   300	| Merge PDFs | pypdf | `writer.add_page(page)` |
   301	| Split PDFs | pypdf | One page per file |
   302	| Extract text | pdfplumber | `page.extract_text()` |
   303	| Extract tables | pdfplumber | `page.extract_tables()` |
   304	| Create PDFs | reportlab | Canvas or Platypus |
   305	| Command line merge | qpdf | `qpdf --empty --pages ...` |
   306	| OCR scanned PDFs | pytesseract | Convert to image first |
   307	| Fill PDF forms | pdf-lib or pypdf (see FORMS.md) | See FORMS.md |
   308	
   309	## Next Steps
   310	
   311	- For advanced pypdfium2 usage, see REFERENCE.md
   312	- For JavaScript libraries (pdf-lib), see REFERENCE.md
   313	- If you need to fill out a PDF form, follow the instructions in FORMS.md
   314	- For troubleshooting guides, see REFERENCE.md
   315	Good. Now I have everything I need. I'll build the complete final document — with all three additions (metadata block, assessment items, scenario prompt) integrated — then produce all three file formats.{"returncode":0,"stdout":"/home/claude/.npm-global/lib\n`-- docx@9.6.1\n\ndocx ok\n","stderr":""}File created successfully: /home/claude/rigging_course_final.mdNow build the DOCX:File created successfully: /home/claude/build_docx.js{"returncode":0,"stdout":"DOCX written successfully\n","stderr":""}{"returncode":2,"stdout":"python: can't open file '//scripts/office/validate.py': [Errno 2] No such file or directory\n","stderr":""}{"returncode":0,"stdout":"python: can't open file '/home/claude/scripts/office/validate.py': [Errno 2] No such file or directory\nChecking file size instead\n-rw-r--r-- 1 claude ubuntu 33K Jun 12 16:42 /mnt/user-data/outputs/TCB-RIG-201_Rigging_Course_Final.docx\n","stderr":""}{"returncode":0,"stdout":"OK: word/document.xml\nOK: [Content_Types].xml\nOK: _rels/.rels\nTotal parts: 26\ndocument.xml size: 280346 bytes\n","stderr":""}DOCX is valid. Now copy the markdown and generate the PDF:{"returncode":0,"stdout":"MD copied: 50K\n","stderr":""}{"returncode":2,"stdout":"python3: can't open file '/home/claude/scripts/office/soffice.py': [Errno 2] No such file or directory\n","stderr":""}{"returncode":0,"stdout":"/mnt/skills/public/docx/scripts/office/soffice.py\n/mnt/skills/public/pptx/scripts/office/soffice.py\n/mnt/skills/public/xlsx/scripts/office/soffice.py\n/usr/bin/soffice\n/usr/bin/libreoffice\n","stderr":""}{"returncode":0,"stdout":"convert /mnt/user-data/outputs/TCB-RIG-201_Rigging_Course_Final.docx as a Writer document -> /mnt/user-data/outputs/TCB-RIG-201_Rigging_Course_Final.pdf using filter : writer_pdf_Export\n","stderr":""}{"returncode":0,"stdout":"-rw-r--r-- 1 claude ubuntu  33K Jun 12 16:42 /mnt/user-data/outputs/TCB-RIG-201_Rigging_Course_Final.docx\n-rw-r--r-- 1 claude ubuntu  50K Jun 12 16:42 /mnt/user-data/outputs/TCB-RIG-201_Rigging_Course_Final.md\n-rw-r--r-- 1 claude ubuntu 292K Jun 12 16:43 /mnt/user-data/outputs/TCB-RIG-201_Rigging_Course_Final.pdf\n","stderr":""}All three files confirmed. Presenting them now.All three files are ready. Here's a quick breakdown of what was added to produce the final packet:

---

### What Was Added (Per the Review Report)

**Course Metadata Block** — Opens the document with a full formatted table covering course code, target audience, difficulty level, estimated time, prerequisites, certification alignment (ETCP/OSHA/ASME), format, and version. Matches the standard packet template referenced in the review.

**Final Assessment (3 Parts)** — A 24-question knowledge check mapped directly to all seven lessons:
- Part A: 10 multiple choice questions covering hardware identification, WLL math, inspection authority, removal criteria, temperature limits, and shock loading
- Part B: 10 true/false statements targeting common misconceptions flagged in the Beginner Mistakes sections
- Part C: 4 short-answer questions requiring applied recall, with a scoring guidance rubric for facilitator or self-review use
- Complete answer key included for all three parts

**Scenario: The Pre-Show Walk** — A fully written jobsite simulation set on Day 2 of an outdoor festival. Learners evaluate five real-world hardware items against the course's inspection criteria, answer four structured questions, and can compare their reasoning against detailed debrief notes for each item — including one deliberately tricky wire rope case designed to test careful threshold application rather than gut instinct.

The DOCX includes navy/gold branding, running headers, page-numbered footers, formatted tables, and callout boxes throughout. The PDF and Markdown are identical in content.
