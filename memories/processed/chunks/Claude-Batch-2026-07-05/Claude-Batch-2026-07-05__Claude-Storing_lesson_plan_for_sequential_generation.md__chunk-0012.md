---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-Storing_lesson_plan_for_sequential_generation.md__chunk-0012",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-Storing_lesson_plan_for_sequential_generation.md",
  "chunk_index": 12,
  "chunk_count_for_source": 13,
  "char_start": 124985,
  "char_end": 136934,
  "source_sha256": "508042ffaf5287d0ffc17ebad33731043412864dcc8f21a5e99b6532520959db",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

, bottom: 1440, left: 1440 } // 1 inch margins
    96	    }
    97	  },
    98	  children: [/* content */]
    99	}]
   100	```
   101	
   102	**Common page sizes (DXA units, 1440 DXA = 1 inch):**
   103	
   104	| Paper | Width | Height | Content Width (1" margins) |
   105	|-------|-------|--------|---------------------------|
   106	| US Letter | 12,240 | 15,840 | 9,360 |
   107	| A4 (default) | 11,906 | 16,838 | 9,026 |
   108	
   109	**Landscape orientation:** docx-js swaps width/height internally, so pass portrait dimensions and let it handle the swap:
   110	```javascript
   111	size: {
   112	  width: 12240,   // Pass SHORT edge as width
   113	  height: 15840,  // Pass LONG edge as height
   114	  orientation: PageOrientation.LANDSCAPE  // docx-js swaps them in the XML
   115	},
   116	// Content width = 15840 - left margin - right margin (uses the long edge)
   117	```
   118	
   119	### Styles (Override Built-in Headings)
   120	
   121	Use Arial as the default font (universally supported). Keep titles black for readability.
   122	
   123	```javascript
   124	const doc = new Document({
   125	  styles: {
   126	    default: { document: { run: { font: "Arial", size: 24 } } }, // 12pt default
   127	    paragraphStyles: [
   128	      // IMPORTANT: Use exact IDs to override built-in styles
   129	      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
   130	        run: { size: 32, bold: true, font: "Arial" },
   131	        paragraph: { spacing: { before: 240, after: 240 }, outlineLevel: 0 } }, // outlineLevel required for TOC
   132	      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
   133	        run: { size: 28, bold: true, font: "Arial" },
   134	        paragraph: { spacing: { before: 180, after: 180 }, outlineLevel: 1 } },
   135	    ]
   136	  },
   137	  sections: [{
   138	    children: [
   139	      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("Title")] }),
   140	    ]
   141	  }]
   142	});
   143	```
   144	
   145	### Lists (NEVER use unicode bullets)
   146	
   147	```javascript
   148	// ❌ WRONG - never manually insert bullet characters
   149	new Paragraph({ children: [new TextRun("• Item")] })  // BAD
   150	new Paragraph({ children: [new TextRun("\u2022 Item")] })  // BAD
   151	
   152	// ✅ CORRECT - use numbering config with LevelFormat.BULLET
   153	const doc = new Document({
   154	  numbering: {
   155	    config: [
   156	      { reference: "bullets",
   157	        levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
   158	          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
   159	      { reference: "numbers",
   160	        levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
   161	          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
   162	    ]
   163	  },
   164	  sections: [{
   165	    children: [
   166	      new Paragraph({ numbering: { reference: "bullets", level: 0 },
   167	        children: [new TextRun("Bullet item")] }),
   168	      new Paragraph({ numbering: { reference: "numbers", level: 0 },
   169	        children: [new TextRun("Numbered item")] }),
   170	    ]
   171	  }]
   172	});
   173	
   174	// ⚠️ Each reference creates INDEPENDENT numbering
   175	// Same reference = continues (1,2,3 then 4,5,6)
   176	// Different reference = restarts (1,2,3 then 1,2,3)
   177	```
   178	
   179	### Tables
   180	
   181	**CRITICAL: Tables need dual widths** - set both `columnWidths` on the table AND `width` on each cell. Without both, tables render incorrectly on some platforms.
   182	
   183	```javascript
   184	// CRITICAL: Always set table width for consistent rendering
   185	// CRITICAL: Use ShadingType.CLEAR (not SOLID) to prevent black backgrounds
   186	const border = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
   187	const borders = { top: border, bottom: border, left: border, right: border };
   188	
   189	new Table({
   190	  width: { size: 9360, type: WidthType.DXA }, // Always use DXA (percentages break in Google Docs)
   191	  columnWidths: [4680, 4680], // Must sum to table width (DXA: 1440 = 1 inch)
   192	  rows: [
   193	    new TableRow({
   194	      children: [
   195	        new TableCell({
   196	          borders,
   197	          width: { size: 4680, type: WidthType.DXA }, // Also set on each cell
   198	          shading: { fill: "D5E8F0", type: ShadingType.CLEAR }, // CLEAR not SOLID
   199	          margins: { top: 80, bottom: 80, left: 120, right: 120 }, // Cell padding (internal, not added to width)
   200	          children: [new Paragraph({ children: [new TextRun("Cell")] })]
   201	        })
   202	      ]
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
