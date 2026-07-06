---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-Storing_lesson_plan_in_memory.md__chunk-0008",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-Storing_lesson_plan_in_memory.md",
  "chunk_index": 8,
  "chunk_count_for_source": 9,
  "char_start": 79391,
  "char_end": 91286,
  "source_sha256": "a064d1994064ac6e33f07fbbf0766c638a373a3accc0b8e9852f3d51ce097a65",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

a personal mitigation plan. It names the risk, the context, the habit, and the phrase. It is specific enough to actually use.

---

## Building a Proactive Safety Culture

Your personal habits are stronger when the crew around you shares the same standard. That is what safety culture means at the crew level — not a policy posted on a wall, but the way the team actually behaves when conditions get difficult.

**A proactive safety culture at crew level looks like this:**

- Workers who speak up early, before the incident
- Leaders who thank people for raising concerns instead of dismissing them
- Crews that treat stop-work calls as professional behavior, not disruptions
- Huddles that identify real hazards and assign real owners
- Hazard reports that lead to corrective action, not filing cabinets
- Near misses shared across departments so the lesson travels
- New workers encouraged to ask questions rather than silently comply
- Experienced workers willing to rescan spaces they think they already know

Safety information that moves quickly through the crew catches hazards before they become incidents. A single person scanning well helps themselves. A crew that scans together and communicates early protects everyone.

> **A good crew member does not just work safely — they help the system see risk earlier.**

---

## Carrying the Course Forward

You are not expected to predict everything. No one is.

You are expected to notice change, ask better questions, speak up early, and act before a hazard becomes an incident. That is the full scope of what this course asked of you — and it is also the full scope of what the crews around you are counting on.

The course ends here. The scan does not.

---

## Final Takeaway

> **Predictive hazard recognition is not a one-time inspection. It is a repeatable habit of scanning, anticipating, communicating, and acting before the show environment changes.**

Scan the zones. Predict the phase change. Communicate the hazard. Use stop-work when conditions are unclear or unsafe. Turn your observations into tools. Carry that habit into every call.

The safest crews are not the ones that never encounter hazards. They are the ones that see hazards early, name them clearly, and control them before the show starts moving.

---

*The Crew Blueprint | Predictive Hazard Recognition | Lesson 7 of 7 | Course Complete*

---

**[USER]**

Create a docx for me

---

**[ASSISTANT]**

1	---
     2	name: docx
     3	description: "Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation."
     4	license: Proprietary. LICENSE.txt has complete terms
     5	---
     6	
     7	# DOCX creation, editing, and analysis
     8	
     9	## Overview
    10	
    11	A .docx file is a ZIP archive containing XML files.
    12	
    13	## Quick Reference
    14	
    15	| Task | Approach |
    16	|------|----------|
    17	| Read/analyze content | `extract-text`, or unpack for raw XML |
    18	| Create new document | Use `docx-js` - see Creating New Documents below |
    19	| Edit existing document | Unpack → edit XML → repack - see Editing Existing Documents below |
    20	
    21	### Converting .doc to .docx
    22	
    23	Legacy `.doc` files must be converted before editing:
    24	
    25	```bash
    26	python scripts/office/soffice.py --headless --convert-to docx document.doc
    27	```
    28	
    29	### Reading Content
    30	
    31	```bash
    32	# Text extraction as markdown
    33	extract-text document.docx
    34	
    35	# Show tracked changes instead of accepting them
    36	pandoc --track-changes=all document.docx -o output.md
    37	
    38	# Raw XML access
    39	python scripts/office/unpack.py document.docx unpacked/
    40	```
    41	
    42	### Converting to Images
    43	
    44	```bash
    45	python scripts/office/soffice.py --headless --convert-to pdf document.docx
    46	pdftoppm -jpeg -r 150 document.pdf page
    47	```
    48	
    49	### Accepting Tracked Changes
    50	
    51	To produce a clean document with all tracked changes accepted (requires LibreOffice):
    52	
    53	```bash
    54	python scripts/accept_changes.py input.docx output.docx
    55	```
    56	
    57	---
    58	
    59	## Creating New Documents
    60	
    61	Generate .docx files with JavaScript, then validate. Install: `npm install -g docx`
    62	
    63	### Setup
    64	```javascript
    65	const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, ImageRun,
    66	        Header, Footer, AlignmentType, PageOrientation, LevelFormat, ExternalHyperlink,
    67	        InternalHyperlink, Bookmark, FootnoteReferenceRun, PositionalTab,
    68	        PositionalTabAlignment, PositionalTabRelativeTo, PositionalTabLeader,
    69	        TabStopType, TabStopPosition, Column, SectionType,
    70	        TableOfContents, HeadingLevel, BorderStyle, WidthType, ShadingType,
    71	        VerticalAlign, PageNumber, PageBreak } = require('docx');
    72	
    73	const doc = new Document({ sections: [{ children: [/* content */] }] });
    74	Packer.toBuffer(doc).then(buffer => fs.writeFileSync("doc.docx", buffer));
    75	```
    76	
    77	### Validation
    78	After creating the file, validate it. If validation fails, unpack, fix the XML, and repack.
    79	```bash
    80	python scripts/office/validate.py doc.docx
    81	```
    82	
    83	### Page Size
    84	
    85	```javascript
    86	// CRITICAL: docx-js defaults to A4, not US Letter
    87	// Always set page size explicitly for consistent results
    88	sections: [{
    89	  properties: {
    90	    page: {
    91	      size: {
    92	        width: 12240,   // 8.5 inches in DXA
    93	        height: 15840   // 11 inches in DXA
    94	      },
    95	      margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } // 1 inch margins
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
