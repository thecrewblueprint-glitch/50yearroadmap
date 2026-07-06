---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-Business_partner_AI_prompt_for_automation.md__chunk-0003",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-Business_partner_AI_prompt_for_automation.md",
  "chunk_index": 3,
  "chunk_count_for_source": 3,
  "char_start": 22675,
  "char_end": 26017,
  "source_sha256": "8ba51f6e6c6718c3037bd636304e81dfffe47be20cec522ff81430690dd04797",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

| Pink | #FBEAF0 | #F4C0D1 | #ED93B1 | #D4537E | #993556 | #72243E | #4B1528 |
| `c-gray` | Gray | #F1EFE8 | #D3D1C7 | #B4B2A9 | #888780 | #5F5E5A | #444441 | #2C2C2A |
| `c-blue` | Blue | #E6F1FB | #B5D4F4 | #85B7EB | #378ADD | #185FA5 | #0C447C | #042C53 |
| `c-green` | Green | #EAF3DE | #C0DD97 | #97C459 | #639922 | #3B6D11 | #27500A | #173404 |
| `c-amber` | Amber | #FAEEDA | #FAC775 | #EF9F27 | #BA7517 | #854F0B | #633806 | #412402 |
| `c-red` | Red | #FCEBEB | #F7C1C1 | #F09595 | #E24B4A | #A32D2D | #791F1F | #501313 |

**How to assign colors**: Color should encode meaning, not sequence. Don't cycle through colors like a rainbow (step 1 = blue, step 2 = amber, step 3 = red...). Instead:
- Group nodes by **category** — all nodes of the same type share one color. E.g. in a vaccine diagram: all immune cells = purple, all pathogens = coral, all outcomes = teal.
- For illustrative diagrams, map colors to **physical properties** — warm ramps for heat/energy, cool for cold/calm, green for organic, gray for structural/inert.
- Use **gray for neutral/structural** nodes (start, end, generic steps).
- Use **2-3 colors per diagram**, not 6+. More colors = more visual noise. A diagram with gray + purple + teal is cleaner than one using every ramp.
- **Prefer purple, teal, coral, pink** for general diagram categories. Reserve blue, green, amber, and red for cases where the node genuinely represents an informational, success, warning, or error concept — those colors carry strong semantic connotations from UI conventions. (Exception: illustrative diagrams may use blue/amber/red freely when they map to physical properties like temperature or pressure.)

**Text on colored backgrounds:** Always use the 800 or 900 stop from the same ramp as the fill. Never use black, gray, or --color-text-primary on colored fills. **When a box has both a title and a subtitle, they must be two different stops** — title darker (800 in light mode, 100 in dark), subtitle lighter (600 in light, 200 in dark). Same stop for both reads flat; the weight difference alone isn't enough. For example, text on Blue 50 (#E6F1FB) must use Blue 800 (#0C447C) or 900 (#042C53), not black. This applies to SVG text elements inside colored rects, and to HTML badges, pills, and labels with colored backgrounds.

**Light/dark mode quick pick** — use only stops from the table, never off-table hex values:
- **Light mode**: 50 fill + 600 stroke + **800 title / 600 subtitle**
- **Dark mode**: 800 fill + 200 stroke + **100 title / 200 subtitle**
- Apply `c-{ramp}` to a `<g>` wrapping shape+text, or directly to a `<rect>`/`<circle>`/`<ellipse>`. Never to `<path>` — paths don't get ramp fill. For colored connector strokes use inline `stroke="#..."` (any mid-ramp hex works in both modes). Dark mode is automatic for ramp classes. Available: c-gray, c-blue, c-red, c-amber, c-green, c-teal, c-purple, c-coral, c-pink.

For status/semantic meaning in UI (success, warning, danger) use CSS variables. For categorical coloring in both diagrams and UI, use these ramps.
Content rendered and shown to the user. Please do not duplicate the shown content in text because it's already visually represented.[This tool call rendered an interactive widget in the chat. The user can already see the result — do not repeat it in text or with another visualization tool.]
