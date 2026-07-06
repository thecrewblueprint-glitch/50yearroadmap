---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-Storing_lesson_plan_in_memory.md__chunk-0009",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-Storing_lesson_plan_in_memory.md",
  "chunk_index": 9,
  "chunk_count_for_source": 9,
  "char_start": 90686,
  "char_end": 101694,
  "source_sha256": "a064d1994064ac6e33f07fbbf0766c638a373a3accc0b8e9852f3d51ce097a65",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

2	      ]
   203	    })
   204	  ]
   205	})
   206	```
   207	
   208	**Table width calculation:**
   209	
   210	Always use `WidthType.DXA` — `WidthType.PERCENTAGE` breaks in Google Docs.
   211	
   212	```javascript
   213	// Table width = sum of columnWidths = content width
   214	// US Letter with 1" margins: 12240 - 2880 = 9360 DXA
   215	width: { size: 9360, type: WidthType.DXA },
	< truncated lines 216-378 >
   379	```
   380	
   381	### Critical Rules for docx-js
   382	
   383	- **Set page size explicitly** - docx-js defaults to A4; use US Letter (12240 x 15840 DXA) for US documents
   384	- **Landscape: pass portrait dimensions** - docx-js swaps width/height internally; pass short edge as `width`, long edge as `height`, and set `orientation: PageOrientation.LANDSCAPE`
   385	- **Never use `\n`** - use separate Paragraph elements
   386	- **Never use unicode bullets** - use `LevelFormat.BULLET` with numbering config
   387	- **PageBreak must be in Paragraph** - standalone creates invalid XML
   388	- **ImageRun requires `type`** - always specify png/jpg/etc
   389	- **Always set table `width` with DXA** - never use `WidthType.PERCENTAGE` (breaks in Google Docs)
   390	- **Tables need dual widths** - `columnWidths` array AND cell `width`, both must match
   391	- **Table width = sum of columnWidths** - for DXA, ensure they add up exactly
   392	- **Always add cell margins** - use `margins: { top: 80, bottom: 80, left: 120, right: 120 }` for readable padding
   393	- **Use `ShadingType.CLEAR`** - never SOLID for table shading
   394	- **Never use tables as dividers/rules** - cells have minimum height and render as empty boxes (including in headers/footers); use `border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "2E75B6", space: 1 } }` on a Paragraph instead. For two-column footers, use tab stops (see Tab Stops section), not tables
   395	- **TOC requires HeadingLevel only** - no custom styles on heading paragraphs
   396	- **Override built-in styles** - use exact IDs: "Heading1", "Heading2", etc.
   397	- **Include `outlineLevel`** - required for TOC (0 for H1, 1 for H2, etc.)
   398	
   399	---
   400	
   401	## Editing Existing Documents
   402	
   403	**Follow all 3 steps in order.**
   404	
   405	### Step 1: Unpack
   406	```bash
   407	python scripts/office/unpack.py document.docx unpacked/
   408	```
   409	Extracts XML, pretty-prints, merges adjacent runs, and converts smart quotes to XML entities (`&#x201C;` etc.) so they survive editing. Use `--merge-runs false` to skip run merging.
   410	
   411	### Step 2: Edit XML
   412	
   413	Edit files in `unpacked/word/`. See XML Reference below for patterns.
   414	
   415	**Use "Claude" as the author** for tracked changes and comments, unless the user explicitly requests use of a different name.
   416	
   417	**Use the Edit tool directly for string replacement. Do not write Python scripts.** Scripts introduce unnecessary complexity. The Edit tool shows exactly what is being replaced.
   418	
   419	**CRITICAL: Use smart quotes for new content.** When adding text with apostrophes or quotes, use XML entities to produce smart quotes:
   420	```xml
   421	<!-- Use these entities for professional typography -->
   422	<w:t>Here&#x2019;s a quote: &#x201C;Hello&#x201D;</w:t>
   423	```
   424	| Entity | Character |
   425	|--------|-----------|
   426	| `&#x2018;` | ‘ (left single) |
   427	| `&#x2019;` | ’ (right single / apostrophe) |
   428	| `&#x201C;` | “ (left double) |
   429	| `&#x201D;` | ” (right double) |
   430	
   431	**Adding comments:** Use `comment.py` to handle boilerplate across multiple XML files (text must be pre-escaped XML):
   432	```bash
   433	python scripts/comment.py unpacked/ 0 "Comment text with &amp; and &#x2019;"
   434	python scripts/comment.py unpacked/ 1 "Reply text" --parent 0  # reply to comment 0
   435	python scripts/comment.py unpacked/ 0 "Text" --author "Custom Author"  # custom author name
   436	```
   437	Then add markers to document.xml (see Comments in XML Reference).
   438	
   439	### Step 3: Pack
   440	```bash
   441	python scripts/office/pack.py unpacked/ output.docx --original document.docx
   442	```
   443	Validates with auto-repair, condenses XML, and creates DOCX. Use `--validate false` to skip.
   444	
   445	**Auto-repair will fix:**
   446	- `durableId` >= 0x7FFFFFFF (regenerates valid ID)
   447	- Missing `xml:space="preserve"` on `<w:t>` with whitespace
   448	
   449	**Auto-repair won't fix:**
   450	- Malformed XML, invalid element nesting, missing relationships, schema violations
   451	
   452	### Common Pitfalls
   453	
   454	- **Replace entire `<w:r>` elements**: When adding tracked changes, replace the whole `<w:r>...</w:r>` block with `<w:del>...<w:ins>...` as siblings. Don't inject tracked change tags inside a run.
   455	- **Preserve `<w:rPr>` formatting**: Copy the original run's `<w:rPr>` block into your tracked change runs to maintain bold, font size, etc.
   456	
   457	---
   458	
   459	## XML Reference
   460	
   461	### Schema Compliance
   462	
   463	- **Element order in `<w:pPr>`**: `<w:pStyle>`, `<w:numPr>`, `<w:spacing>`, `<w:ind>`, `<w:jc>`, `<w:rPr>` last
   464	- **Whitespace**: Add `xml:space="preserve"` to `<w:t>` with leading/trailing spaces
   465	- **RSIDs**: Must be 8-digit hex (e.g., `00AB1234`)
   466	
   467	### Tracked Changes
   468	
   469	**Insertion:**
   470	```xml
   471	<w:ins w:id="1" w:author="Claude" w:date="2025-01-01T00:00:00Z">
   472	  <w:r><w:t>inserted text</w:t></w:r>
   473	</w:ins>
   474	```
   475	
   476	**Deletion:**
   477	```xml
   478	<w:del w:id="2" w:author="Claude" w:date="2025-01-01T00:00:00Z">
   479	  <w:r><w:delText>deleted text</w:delText></w:r>
   480	</w:del>
   481	```
   482	
   483	**Inside `<w:del>`**: Use `<w:delText>` instead of `<w:t>`, and `<w:delInstrText>` instead of `<w:instrText>`.
   484	
   485	**Minimal edits** - only mark what changes:
   486	```xml
   487	<!-- Change "30 days" to "60 days" -->
   488	<w:r><w:t>The term is </w:t></w:r>
   489	<w:del w:id="1" w:author="Claude" w:date="...">
   490	  <w:r><w:delText>30</w:delText></w:r>
   491	</w:del>
   492	<w:ins w:id="2" w:author="Claude" w:date="...">
   493	  <w:r><w:t>60</w:t></w:r>
   494	</w:ins>
   495	<w:r><w:t> days.</w:t></w:r>
   496	```
   497	
   498	**Deleting entire paragraphs/list items** - when removing ALL content from a paragraph, also mark the paragraph mark as deleted so it merges with the next paragraph. Add `<w:del/>` inside `<w:pPr><w:rPr>`:
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
   594	{"returncode":0,"stdout":"/home/claude/.npm-global/lib\n`-- docx@9.6.1\n\n","stderr":""}File created successfully: /home/claude/build_course.js{"returncode":0,"stdout":"Done.\n","stderr":""}{"returncode":0,"stdout":"\nParagraphs: 0 → 732 (+732)\nAll validations PASSED!\n","stderr":""}All 7 lessons packaged into a single clean Word doc. Here's what's included:

- **Cover page** with course title and metadata
- **Course overview table** mapping all 7 lessons
- **Each lesson** with its full structure — overview, objectives, body content, tables, blockquotes, and takeaway
- **Formatting** consistent throughout — dark/gold color scheme, proper heading hierarchy, bullet and numbered lists, all tables with header rows

732 paragraphs, validated clean. Ready to use as a training document, upload to a course builder, or hand off to a designer.
