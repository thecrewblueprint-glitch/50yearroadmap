---
{
  "chunk_id": "Perplexity-Batch-2026-07-05__Perplexity-Best_architecture_Frontend_Use_a_simple_web_app_hosted_on_your_subdomain__HTML_CSS_Ja__chunk-0002",
  "archive_id": "Perplexity-Batch-2026-07-05",
  "archive_filename": "Perplexity-Batch-2026-07-05.zip",
  "source_path": "Perplexity-Best_architecture_Frontend_Use_a_simple_web_app_hosted_on_your_subdomain__HTML_CSS_JavaScript_Static_invoice_template_PDF_generation_in_the_browser_Backend_Use_PHP_because_your_cPanel_already_supports.md",
  "chunk_index": 2,
  "chunk_count_for_source": 2,
  "char_start": 11349,
  "char_end": 17223,
  "source_sha256": "1807c639b79e51b11c4419f22e069fead09b335e445dc1118f8fe9494abcca1a",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

d HTML template). Build it on your subdomain and you'll have a functioning invoice generator in 1-2 days.

---

**[USER]**

That review confirms the general architecture, but do not use its sample code as-is. Several parts are incorrect or unnecessarily complicated.

What it got right

The correct system is:

> Conversational text → PHP AI parser → validated JSON → editable review → deterministic calculations → fixed invoice PDF → direct download



The right stack is still:

HTML

CSS

JavaScript

PHP

OpenRouter for text interpretation

Client-side PDF generation

One fixed invoice layout


No React, Ruby, database, cloud storage, OCR, or native Android application is necessary.

Corrections that matter

1. The OpenRouter PHP example is wrong

OpenRouter uses:

Authorization: Bearer YOUR_API_KEY

—not:

Authorization: API-Key YOUR_API_KEY

The response text is normally found under:

$result['choices'][0]['message']['content']

—not:

$jsonOutput['content'][0]['text']

OpenRouter also supports structured outputs using JSON Schema, which is preferable to merely telling the model to “return JSON.” 

2. pdfmake is not HTML-to-PDF

pdfmake generates documents from its own JavaScript document-definition structure. It does not take your finished invoice HTML and automatically reproduce it as a PDF. 

This matters because the review mixes two different strategies:

Building a PDF programmatically with pdfmake

Converting rendered HTML into a PDF


Those are not the same architecture.

3. Do not use three separate HTML pages

The app should be one page with three views:

Input
Review
Preview

JavaScript can hide and show each section. That avoids passing invoice data between pages and makes mobile use faster.

4. Do not add save.php yet

You said you want direct PDF output and no cloud functionality. Therefore, do not add server-side draft storage.

Use:

localStorage

for a simple current draft, or:

IndexedDB

only if the draft data becomes larger or more complex.

5. Do not use absolute CSS positioning for the entire invoice

Absolute positioning is suitable for a few fixed header fields, but line-item tables need normal document flow.

A better invoice layout uses:

CSS Grid for the header

A real table for work entries

Flexbox or Grid for totals

Fixed letter-page dimensions

Controlled page breaks


This allows the number of invoice entries to vary without overlapping the total section.

6. window.print() is not a dependable PDF generator

window.print() opens Android or desktop print controls, but browser print settings, margins, headers, and scaling can vary.

It may be acceptable as a temporary prototype, but it is not the best final export workflow.

Best PDF method for this app

Use pdfmake directly, not HTML conversion.

Why:

It supports browser-side PDF generation.

It supports tables, columns, images, styling, wrapping, and downloads.

It works in Android Chrome.

It creates structured text rather than merely taking a screenshot of the invoice.

It handles variable line-item rows more predictably. 


The web preview can use HTML and CSS, while the PDF uses an equivalent pdfmake document definition.

That technically creates two renderers, but for a simple fixed invoice, this is manageable and more dependable than browser HTML capture.

Final architecture

invoice.yourdomain.com/
│
├── index.html
├── css/
│   └── styles.css
├── js/
│   ├── app.js
│   ├── invoice-parser.js
│   ├── calculations.js
│   └── pdf-generator.js
├── api/
│   ├── parse-invoice.php
│   └── config.php
├── vendor/
│   ├── pdfmake.min.js
│   └── vfs_fonts.js
└── .htaccess

Exact responsibility of each part

Browser

The browser handles:

Conversational input

Review and corrections

Financial calculations

Invoice preview

PDF construction

PDF download

Temporary local draft storage


PHP

PHP handles only:

Receiving invoice instructions

Authenticating the request

Sending the text to OpenRouter

Enforcing the JSON response schema

Validating the returned structure

Returning clean JSON to the browser


AI

The AI handles only:

Recognizing the client

Interpreting dates

Separating work entries

Identifying hours and rates

Identifying expenses

Extracting invoice terms

Identifying missing or ambiguous information


The AI must not:

Calculate totals

Generate the PDF

Choose invoice field positions

Save files

Invent missing rates or hours


Corrected core workflow

1. Paste conversational invoice information.


2. Press Process Invoice.


3. PHP sends the text to OpenRouter.


4. OpenRouter returns JSON matching a strict schema.


5. PHP validates and sanitizes the JSON.


6. The browser shows every extracted field.


7. You correct anything necessary.


8. JavaScript calculates line totals, expenses, subtotal, and total.


9. The app displays the finished invoice preview.


10. pdfmake generates the final PDF.


11. The browser downloads it directly.



Recommendation

Proceed with:

> Single-page HTML/CSS/JavaScript frontend + minimal PHP parsing endpoint + OpenRouter structured output + pdfmake PDF generation.



That is the smallest architecture that still gives you genuinely conversational entry and dependable invoice output.

---

**[ASSISTANT]**

Perfect—this is a much clearer and more accurate architecture. I'll build out the **corrected implementation** with all your corrections applied.

## Final Corrected Architecture

```
invoice.yourdomain.com/
├── index.html (single page, 3 views)
├── css/styles.css
├── js/
│   ├── app.js (main flow)
│   ├── invoice-parser.js (schema definition)
│   ├── calculations.js (deterministic math)
│   └── pdf-generator.js (pdfmake)
├── api/
│   ├── parse-invoice.php (OpenRouter with JSON Schema)
│   └── config.php (API key only)
├── vendor/
│   ├── pdfmake.min.js
│   └── vfs_fonts.js
```

Let me create the complete, working implementation:
