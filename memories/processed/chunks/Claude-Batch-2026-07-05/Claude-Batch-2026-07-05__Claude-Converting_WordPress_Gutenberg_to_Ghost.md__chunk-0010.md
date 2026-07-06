---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-Converting_WordPress_Gutenberg_to_Ghost.md__chunk-0010",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-Converting_WordPress_Gutenberg_to_Ghost.md",
  "chunk_index": 10,
  "chunk_count_for_source": 10,
  "char_start": 90093,
  "char_end": 91961,
  "source_sha256": "01f1d18c2a5e4f24238c921db4b6c64ceabbad019ef2f19537baf0f40c8d4384",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

adients on white backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character.
    37	
    38	Interpret creatively and make unexpected choices that feel genuinely designed for the context. No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices (Space Grotesk, for example) across generations.
    39	
    40	**IMPORTANT**: Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate code with extensive animations and effects. Minimalist or refined designs need restraint, precision, and careful attention to spacing, typography, and subtle details. Elegance comes from executing the vision well.
[43 lines total]Now I have everything I need. Let me build the Ghost-compatible HTML file:File created successfully: /mnt/user-data/outputs/crew-blueprint-ghost.htmlHere's your Ghost-ready file. Here's what was done and how to use it:

**What changed from WordPress:**
- All `<!-- wp:block -->` Gutenberg comments stripped out
- WordPress utility classes (`wp-block-*`, `alignfull`, `has-*-background-color`) removed
- PHP functions.php replaced — Google Fonts now load via a `<link>` tag in the HTML head
- CSS rewritten to use plain selectors instead of WordPress-specific ones
- The "Implementation Notes" info box was updated to reflect Ghost-specific advice (tags, sitemaps, etc.) instead of WordPress plugins

**How to add it to Ghost Free:**
1. Create a new **Page** in Ghost
2. Click the **+** to add a block → choose **HTML**
3. Paste the entire file contents into that HTML card
4. Hit **Publish**

The file is fully self-contained — one file, no external dependencies except Google Fonts. It will render the full hero, sitemap, safety manifesto, career roadmap, and SEO keyword section.
