---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-GitHub_connection_to_thecrewblueprint-glitch.md__chunk-0002",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-GitHub_connection_to_thecrewblueprint-glitch.md",
  "chunk_index": 2,
  "chunk_count_for_source": 2,
  "char_start": 11227,
  "char_end": 13816,
  "source_sha256": "5dcd0d38d11416deaf6752d3386982e773880c3e84a6e00a192efb8aaeff65e9",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

onUrl": "https://www.google.com/s2/favicons?domain=exa.ai&sz=64", "directoryUuid": "91408932-1110-4350-97c7-2d6b3a6d9694", "installedServerId": null, "customOAuthClientId": null, "installState": "not_installed", "isAuthless": false, "tools": ["web_search_exa", "get_code_context_exa"], "connected": false}]}That search didn't surface an actual GitHub connector — the registry returned a bunch of unrelated tools (Digits, alphaXiv, Freshservice, etc.), none of which is GitHub itself.

A couple of notes:

- A "GitHub" connector isn't showing up as installable through this registry search right now.
- Separately, I do have access to deferred tools for **GitHub** under a different path (`tool_search` lists `Google Calendar`, `Google Drive`, etc., but not GitHub either — it wasn't in that list).

Given that, the most reliable way to connect GitHub is directly through Claude's settings rather than through me:

1. Go to **claude.ai → Settings → Connectors** (or **Settings → Features** depending on your plan).
2. Look for **GitHub** in the connector list and click **Connect**.
3. Authorize with the account that has access to `thecrewblueprint-glitch`.

Once that's connected, I'll be able to see it as a tool. If you don't see GitHub listed there at all, that likely means it's not yet enabled for your account/workspace tier — in that case you could let me know and I can point you to where to check on availability.

Want me to check Anthropic's docs for the current GitHub connector setup steps, in case there's a more specific path (like an organization approval step)?

---

**[USER]**

Are you connected now?

---

**[ASSISTANT]**

Let me check again.No matching tools found.Still no GitHub connection showing up. A few possibilities:

1. **The connection didn't complete** — make sure you finished the OAuth authorization flow all the way through (it usually ends with a confirmation screen).
2. **It may require a page refresh** — try starting a new conversation after connecting, since MCP connectors are loaded at the start of a session.
3. **GitHub may not be available in the registry yet** — Anthropic is still expanding the connector catalog, and GitHub isn't confirmed available through claude.ai's built-in connector system as of my knowledge.

What you *can* do right now as a workaround: paste code, file contents, or repo structure directly into chat and I'll work with it. That's the most reliable path until an official GitHub connector is available.

Did the Settings → Connectors page actually show GitHub as an option, or was it absent from the list entirely?
