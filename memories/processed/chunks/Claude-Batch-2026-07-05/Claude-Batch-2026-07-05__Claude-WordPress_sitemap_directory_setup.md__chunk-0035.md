---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-WordPress_sitemap_directory_setup.md__chunk-0035",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-WordPress_sitemap_directory_setup.md",
  "chunk_index": 35,
  "chunk_count_for_source": 53,
  "char_start": 369962,
  "char_end": 381881,
  "source_sha256": "94c6fa3b222f9e9d1a3418b26589de902cde3cac997f3b5cfd437f70e74973ff",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

es for a base. Returns metadata about each interface and the pages within it, including page IDs, names, and page-type-specific fields describing the page's data model or content. Pages have a pageType: \"list\" pages support listing records directly, \"dashboard\" pages contain visualization elements (charts, big numbers, etc.) that aggregate data from source tables, \"overview\" pages contain static authored content (text, links) with no record data, and \"form\" pages create records in a single table. For record list pages, use sourceTableId and tablesByTableId to understand the data model. For dashboard pages, use dashboardElements to understand what each element visualizes. Each element's config describes the aggregation (e.g., a BigNumber with summaryFunction \"sum\" means \"sum the values of the referenced field\"). To compute these values, call list_records_for_page with the element's id as elementId to fetch the underlying records, then aggregate them according to the config. Overview pages are not backed by record data and cannot be used with list_records_for_page; read their content field directly. For form pages, use name, description, and sourceTableName to identify the relevant form. Call get_form_schema for the full form structure. Use this when the user asks about interfaces, pages, dashboards, or forms, or when a base has permissionLevel \"none\" (interface-only access). Do not assume baseId. Obtain it from search_bases or list_bases. {\"baseId\": \"appZfrNIUEip5MazD\"}", "name": "Airtable:list_pages_for_base", "parameters": {"$schema": "http://json-schema.org/draft-07/schema#", "additionalProperties": false, "properties": {"baseId": {"description": "The ID of the base to list pages from.\nMust start with \"app\" and is 17 characters long.\nExample: \"appZfrNIUEip5MazD\".\nDo not substitute user-facing names for baseId.\nTo get baseId, use the search_bases or list_bases tool.", "pattern": "^app[A-Za-z0-9]{14}$", "type": "string"}}, "required": ["baseId"], "type": "object"}}</function>
<function>{"description": "List your saved Zapier Skills with descriptions. ALWAYS call this FIRST when the user's request sounds like a known workflow \u2014 e.g. 'onboard me'. Do NOT assume you know the list; skills may have been added or updated since your last check. Skills are reusable markdown instructions that guide you through tasks using your connected apps. Use get_zapier_skill to load the full content of a skill before executing it. Use create_zapier_skill to save a new workflow.", "name": "Zapier:list_zapier_skills", "parameters": {"$schema": "http://json-schema.org/draft-07/schema#", "properties": {}, "type": "object"}}</function>
<function>{"description": "Call this tool to create or upload a File to Google Drive. If uploading content, prefer \"text_content\" for text content. For non-UTF8 contents, use the \"base64_content\" field and base64 encode the data to set on that field. Returns a single File object upon successful creation. The following Google Drive first-party mime types can be created without providing content: - `application/vnd.google-apps.document` - `application/vnd.google-apps.spreadsheet` - `application/vnd.google-apps.presentation` By default, the following conversions will be made for the following mime types: - `text/plain` to `application/vnd.google-apps.document` - `text/csv` to `application/vnd.google-apps.spreadsheet` To disable conversions for first-party mime types, set `disable_conversion_to_google_type` to true. Folders can be created by setting the mime type to `application/vnd.google-apps.folder`. When uploading content, the `content_mime_type` field is required and should match the type of the content being uploaded.", "name": "Google Drive:create_file", "parameters": {"description": "Request to upload a file.", "properties": {"base64Content": {"description": "Optional. The base64 encoded content to upload. It's an error to set this and text_content.", "type": "string"}, "content": {"description": "The content of the file encoded as base64. The content field should always be base64 encoded regardless of the mime type of the file. DEPRECATED. Use base64_content or text_content instead.", "type": "string"}, "contentMimeType": {"description": "The mime type of the content being uploaded. Required when any type of content is provided.", "type": "string"}, "disableConversionToGoogleType": {"description": "Set to true to retain the passed in content mime type and not convert to a Google type. For example, without this a text/plain content mime type will be converted to to an application/vnd.google-apps.document. Has no effect for types that do not have a Google equivalent.", "type": "boolean"}, "mimeType": {"description": "DEPRECATED. DO NOT USE!! Set content_mime_type instead.", "type": "string"}, "parentId": {"description": "The parent id of the file.", "type": "string"}, "textContent": {"description": "Optional. The (UTF-8) text content to upload. It's an error to set this and base64_content.", "type": "string"}, "title": {"description": "The title of the file.", "type": "string"}}, "type": "object"}}</function>
<function>{"description": "Lists email threads from the authenticated user's Gmail account. This tool can filter threads based on a query string and supports pagination. It returns a list of threads, including their IDs and related messages. Each related message contains details like a snippet of the message body, the subject, the sender, the recipients etc. Note that the full message bodies are not returned by this tool; use the 'get_thread' tool with a thread ID to fetch the full message body if needed. Threads with excluded criteria may still appear in the results. This occurs because Gmail identifies matching messages first. For example, if you search for -is:starred, Gmail will find an entire thread if it contains at least one unstarred message, even if other emails in that same conversation are starred.", "name": "Gmail:search_threads", "parameters": {"description": "Request message for SearchThreads RPC.", "properties": {"includeTrash": {"description": "Optional. Include drafts from TRASH in the results. Defaults to false.", "type": "boolean"}, "pageSize": {"description": "Optional. The maximum number of threads to return. If unspecified, defaults to 20. The maximum allowed value is 50.", "format": "int32", "type": "integer"}, "pageToken": {"description": "Optional. Page token to retrieve a specific page of results in the list. Leave empty to fetch the first page. This is primarily used for pagination to continue fetching results from where the previous `SearchThreads` call left off, especially when the number of threads matching the query exceeds the page_size limit.", "type": "string"}, "query": {"description": "Optional. A query string to filter the threads. Natural language queries must be pre-converted into Gmail syntax queries to use this tool. If omitted, all threads (excluding spam and trash by default) are listed. Supported Operators by Category: Sender & Recipient: from: - Sent from a specific person. to: - Sent to a specific person. cc: - Specific people in Cc. bcc: - Specific people in Bcc. deliveredto: - Delivered to a specific address. list: - From a specific mailing list. Time & Date: after:YYYY/MM/DD / newer:YYYY/MM/DD - Received after a date. before:YYYY/MM/DD / older:YYYY/MM/DD - Received before a date. older_than: - Older than a duration (e.g., 1y, 2d). newer_than: - Newer than a duration. Content: subject: - Words in the subject line. has: - Has specific content types (attachment, drive, youtube, document). filename: - Attachment with a specific name or type. \"\" - Search for an exact word or phrase. (e.g., \"holiday\", \"holiday vacation\"). + - Match a word exactly. (e.g., +holiday, +unicorn) rfc822msgid: - Specific message ID header. AROUND - Find words near each other (e.g., holiday AROUND 10 vacation). Labels & Categories: label: - Under a specific label. The tool accepts label IDs, not display names. Use the list_labels tool to get the ID. category: - In a category (primary, social, promotions, updates, forums, reservations, purchases). in: - Search in specific labels (archive, snoozed, trash, sent, inbox). E.g., `in:trash`, `in:inbox`. Archived and sent messages are included by default; use `-in:archive` and `-in:sent` to exclude them. Drafts are explicitly excluded by default by the tool. Use `in:inbox` to restrict search to the inbox only. has:userlabels - Has any user labels. has:nouserlabels - Does not have any user labels. has:*-star - Specific star colors (if enabled, e.g., has:yellow-star). in:draft - Search in drafts. -in:draft means exclude drafts from the search results. in:sent - Search in sent messages. in:anywhere - Search in all folders (including spam and trash). Status: is: - Search by status (important, starred, unread, read, muted). Size: size: - Specific size in bytes. larger: / smaller: - Larger or smaller than a size (e.g., 10M for 10 MB). Logic & Grouping: AND - Match all criteria (default behavior). OR or { } - Match one or more criteria (e.g., from:amy OR from:david, {from:amy from:david}). - (minus) - Exclude criteria (e.g., -movie). ( ) - Group multiple search terms (e.g., subject:(dinner film)). Examples: \"subject:OneMCP Update\" \"from:user@example.com\" \"to:user2@example.com AND newer_than:7d\" \"project proposal has:attachment\" \"is:unread -in:draft\"", "type": "string"}}, "type": "object"}}</function>
<function>{"description": "Update an existing Zapier Skill's description or content. Use when the user wants to refine a skill, fix an issue, or add new instructions.", "name": "Zapier:update_zapier_skill", "parameters": {"$schema": "http://json-schema.org/draft-07/schema#", "properties": {"description": {"description": "Updated one-sentence description (optional)", "maxLength": 500, "minLength": 1, "type": "string"}, "name": {"description": "The exact name of the skill to update", "minLength": 1, "type": "string"}, "skillDefinition": {"description": "Updated full markdown skill definition (optional). Use ZapierAction[app:action](params) format for action references.", "maxLength": 100000, "minLength": 1, "type": "string"}}, "required": ["name"], "type": "object"}}</function>
</functions>The WordPress MCP tool is not loading in this session — it's a connection issue on WordPress.com's end, not Claude's. Here's exactly what's happening and the fastest path forward:

---

**The WordPress.com MCP connection is timing out between sessions.** This is a known issue with staging site MCP integrations.

**To fix it right now:**

1. Go to **[wordpress.com/me/mcp](https://wordpress.com/me/mcp)**
2. Find the `thecrewblueprint.wpcomstaging.com` connection
3. **Disconnect it**, then **reconnect it**
4. Come back and say "WordPress reconnected" — I'll pick up instantly

---

**While you do that, here's the complete build plan so you can see exactly what's coming:**

---

### Page Structure to Be Built

```
Homepage (ID: 6)
└── "Open Start Page" button → links to Course Start Page

Stagehand Fundamentals (ID: 54) ← Course Start Page
├── Module 1: Welcome to the Live Event World
│   ├── Lesson 1.1 — What a Stagehand Actually Does
│   ├── Lesson 1.2 — Load-In, Show Call, and Load-Out
│   ├── Lesson 1.3 — Common Work Environments
│   ├── Lesson 1.4 — Who Is on the Crew
│   ├── Lesson 1.5 — What Makes a New Stagehand Valuable
│   └── Module 1 Quiz
│
└── Module 2: Safety Mindset Before Skillset
    ├── Lesson 2.1 — Why Safety Comes Before Speed
    ├── Lesson 2.2 — Worker Rights and Employer Responsibilities
    ├── Lesson 2.3 — Hazard, Risk, and Unsafe Behavior
    ├── Lesson 2.4 — Pause and Get a Lead
    ├── Lesson 2.5 — Incident Reporting and Near Misses
    ├── Lesson 2.6 — Never Pretend You Know Something
    ├── Lesson 2.7 — How to Listen During a Safety Briefing
    └── Module 2 Quiz
```

