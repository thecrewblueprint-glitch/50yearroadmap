---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-Storing_lesson_plan_for_sequential_generation.md__chunk-0013",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-Storing_lesson_plan_for_sequential_generation.md",
  "chunk_index": 13,
  "chunk_count_for_source": 13,
  "char_start": 136334,
  "char_end": 140842,
  "source_sha256": "508042ffaf5287d0ffc17ebad33731043412864dcc8f21a5e99b6532520959db",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

del/>` inside `<w:pPr><w:rPr>`:
   499	```xml
   500	<w:p>
   501	  <w:pPr>
   502	    <w:numPr>...</w:numPr>  <!-- list numbering if present -->
   503	    <w:rPr>
   504	      <w:del w:id="1" w:author="Claude" w:date="2025-01-01T00:00:00Z"/>
   505	    </w:rPr>
   506	  </w:pPr>
   507	  <w:del w:id="2" w:author="Claude" w:date="2025-01-01T00:00:00Z">
   508	    <w:r><w:delText>Entire paragraph content being deleted...</w:delText></w:r>
   509	  </w:del>
   510	</w:p>
   511	```
   512	Without the `<w:del/>` in `<w:pPr><w:rPr>`, accepting changes leaves an empty paragraph/list item.
   513	
   514	**Rejecting another author's insertion** - nest deletion inside their insertion:
   515	```xml
   516	<w:ins w:author="Jane" w:id="5">
   517	  <w:del w:author="Claude" w:id="10">
   518	    <w:r><w:delText>their inserted text</w:delText></w:r>
   519	  </w:del>
   520	</w:ins>
   521	```
   522	
   523	**Restoring another author's deletion** - add insertion after (don't modify their deletion):
   524	```xml
   525	<w:del w:author="Jane" w:id="5">
   526	  <w:r><w:delText>deleted text</w:delText></w:r>
   527	</w:del>
   528	<w:ins w:author="Claude" w:id="10">
   529	  <w:r><w:t>deleted text</w:t></w:r>
   530	</w:ins>
   531	```
   532	
   533	### Comments
   534	
   535	After running `comment.py` (see Step 2), add markers to document.xml. For replies, use `--parent` flag and nest markers inside the parent's.
   536	
   537	**CRITICAL: `<w:commentRangeStart>` and `<w:commentRangeEnd>` are siblings of `<w:r>`, never inside `<w:r>`.**
   538	
   539	```xml
   540	<!-- Comment markers are direct children of w:p, never inside w:r -->
   541	<w:commentRangeStart w:id="0"/>
   542	<w:del w:id="1" w:author="Claude" w:date="2025-01-01T00:00:00Z">
   543	  <w:r><w:delText>deleted</w:delText></w:r>
   544	</w:del>
   545	<w:r><w:t> more text</w:t></w:r>
   546	<w:commentRangeEnd w:id="0"/>
   547	<w:r><w:rPr><w:rStyle w:val="CommentReference"/></w:rPr><w:commentReference w:id="0"/></w:r>
   548	
   549	<!-- Comment 0 with reply 1 nested inside -->
   550	<w:commentRangeStart w:id="0"/>
   551	  <w:commentRangeStart w:id="1"/>
   552	  <w:r><w:t>text</w:t></w:r>
   553	  <w:commentRangeEnd w:id="1"/>
   554	<w:commentRangeEnd w:id="0"/>
   555	<w:r><w:rPr><w:rStyle w:val="CommentReference"/></w:rPr><w:commentReference w:id="0"/></w:r>
   556	<w:r><w:rPr><w:rStyle w:val="CommentReference"/></w:rPr><w:commentReference w:id="1"/></w:r>
   557	```
   558	
   559	### Images
   560	
   561	1. Add image file to `word/media/`
   562	2. Add relationship to `word/_rels/document.xml.rels`:
   563	```xml
   564	<Relationship Id="rId5" Type=".../image" Target="media/image1.png"/>
   565	```
   566	3. Add content type to `[Content_Types].xml`:
   567	```xml
   568	<Default Extension="png" ContentType="image/png"/>
   569	```
   570	4. Reference in document.xml:
   571	```xml
   572	<w:drawing>
   573	  <wp:inline>
   574	    <wp:extent cx="914400" cy="914400"/>  <!-- EMUs: 914400 = 1 inch -->
   575	    <a:graphic>
   576	      <a:graphicData uri=".../picture">
   577	        <pic:pic>
   578	          <pic:blipFill><a:blip r:embed="rId5"/></pic:blipFill>
   579	        </pic:pic>
   580	      </a:graphicData>
   581	    </a:graphic>
   582	  </wp:inline>
   583	</w:drawing>
   584	```
   585	
   586	---
   587	
   588	## Dependencies
   589	
   590	- **pandoc**: Text extraction
   591	- **docx**: `npm install -g docx` (new documents)
   592	- **LibreOffice**: PDF conversion (auto-configured for sandboxed environments via `scripts/office/soffice.py`)
   593	- **Poppler**: `pdftoppm` for images
   594	{"returncode":0,"stdout":"npm notice\nnpm notice New major version of npm available! 10.9.7 -> 11.16.0\nnpm notice Changelog: https://github.com/npm/cli/releases/tag/v11.16.0\nnpm notice To update run: npm install -g npm@11.16.0\nnpm notice\n","stderr":""}File created successfully: /home/claude/build_course.js{"returncode":0,"stdout":"Done\n","stderr":""}{"returncode":0,"stdout":"\nParagraphs: 0 → 1892 (+1892)\nAll validations PASSED!\n","stderr":""}All 9 lessons, every formula, every table, every checklist — validated at 1,892 paragraphs. Download it and drag it straight into Google Drive to auto-convert.

**What's included:**
- Cover page
- Course overview with lesson index
- All 9 complete lessons word for word
- All formula blocks, comparison tables, scenario analyses, quizzes, and checklists
- Final standards reference page with formula quick-reference
