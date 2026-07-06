---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-WordPress_sitemap_directory_setup.md__chunk-0036",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-WordPress_sitemap_directory_setup.md",
  "chunk_index": 36,
  "chunk_count_for_source": 53,
  "char_start": 381281,
  "char_end": 393253,
  "source_sha256": "94c6fa3b222f9e9d1a3418b26589de902cde3cac997f3b5cfd437f70e74973ff",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

ommon Work Environments
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

**Total new pages: ~20.** All lesson content is verbatim from your document and ready to post the moment the connection is live. Reconnect and we'll get it done.

---

**[USER]**

wordpress reconnected

---

**[ASSISTANT]**

Let me verify the connection and get the homepage content first.Tool 'WordPress.com:wpcom-mcp-content-authoring' not found.Loaded 5 tools:
  Airtable (2):
  Airtable:list_pages_for_base:
    baseId: string - The ID of the base to list pages from.
Must start with "app" and is 17 characters long.
Example: "appZfrNIUEip5MazD"....
  Airtable:get_record_for_page:
    baseId: string - The ID of the base (application) containing the page.
Must start with "app" and is 17 characters long.
Example: "appZ...
    interfaceId: string - The ID of the interface that contains the page.
Must start with "pbd" and is 17 characters long.
    path: object {root, edges} - The navigation path from the page where the record was listed.
Construct the root from the same pageId used in list_r...
    fieldIds?: array [string] - Only data for fields whose IDs are in this list will be included in the result.
If not provided, all fields visible o...
  Gmail (1):
  Gmail:list_drafts:
    pageSize?: integer - Optional. The maximum number of drafts to return. If unspecified, defaults to 20. The maximum allowed value is 50.
    pageToken?: string - Optional. A token received from a previous list_drafts call to retrieve the next page of results. Leave empty to fetc...
    query?: string - Examples: "subject:OneMCP Update" "from:gduser1@workspacesamples.dev" "to:gduser2@workspacesamples.dev AND newer_than...
  Google Calendar (1):
  Google Calendar:list_calendars:
    pageSize?: integer - Optional. Maximum number of entries returned on one result page. By default the value is 100 entries. The page size c...
    pageToken?: string - Optional. Token specifying which result page to return.
  Google Drive (1):
  Google Drive:list_recent_files:
    excludeContentSnippets?: boolean - If true, the content snippet will be excluded from the response.
    orderBy?: string - The sort order for the files.
    pageSize?: integer - The maximum number of files to return.
    pageToken?: string - The page token to use for pagination.
These tools are now available for you to call directly.

<functions>
<function>{"description": "Lists all interfaces and their pages for a base. Returns metadata about each interface and the pages within it, including page IDs, names, and page-type-specific fields describing the page's data model or content. Pages have a pageType: \"list\" pages support listing records directly, \"dashboard\" pages contain visualization elements (charts, big numbers, etc.) that aggregate data from source tables, \"overview\" pages contain static authored content (text, links) with no record data, and \"form\" pages create records in a single table. For record list pages, use sourceTableId and tablesByTableId to understand the data model. For dashboard pages, use dashboardElements to understand what each element visualizes. Each element's config describes the aggregation (e.g., a BigNumber with summaryFunction \"sum\" means \"sum the values of the referenced field\"). To compute these values, call list_records_for_page with the element's id as elementId to fetch the underlying records, then aggregate them according to the config. Overview pages are not backed by record data and cannot be used with list_records_for_page; read their content field directly. For form pages, use name, description, and sourceTableName to identify the relevant form. Call get_form_schema for the full form structure. Use this when the user asks about interfaces, pages, dashboards, or forms, or when a base has permissionLevel \"none\" (interface-only access). Do not assume baseId. Obtain it from search_bases or list_bases. {\"baseId\": \"appZfrNIUEip5MazD\"}", "name": "Airtable:list_pages_for_base", "parameters": {"$schema": "http://json-schema.org/draft-07/schema#", "additionalProperties": false, "properties": {"baseId": {"description": "The ID of the base to list pages from.\nMust start with \"app\" and is 17 characters long.\nExample: \"appZfrNIUEip5MazD\".\nDo not substitute user-facing names for baseId.\nTo get baseId, use the search_bases or list_bases tool.", "pattern": "^app[A-Za-z0-9]{14}$", "type": "string"}}, "required": ["baseId"], "type": "object"}}</function>
<function>{"description": "Gets a single record's details from an interface page element. Takes a navigation path with a root record and edges representing linked record relationships. With no edges, returns the root record. With edges, returns the last edge's linkedRecordId. For each edge, fieldId is the linked record field to follow, and linkedRecordId is the record it points to. Example: record A on page P has linked record field F pointing to record B. - Fetch A: path = {root: {pageId: P, recordId: A}, edges: []} - Fetch B: path = {root: {pageId: P, recordId: A}, edges: [{fieldId: F, linkedRecordId: B}]} Each subsequent call appends to the same path without changing root. For dashboard pages, include elementId in the root to identify the dashboard element. Obtain element IDs from the dashboardElements array in the list_pages_for_base response. The response includes navigationTargets listing which fieldIds can be expanded further. To navigate deeper, append a new edge. Requires baseId and path. Use this for bases with permissionLevel \"none\" (interface-only access), or when the user asks about interface/page data. Obtain pageId from list_pages_for_base. Do not assume baseId. Obtain it from search_bases or list_bases", "name": "Airtable:get_record_for_page", "parameters": {"$schema": "http://json-schema.org/draft-07/schema#", "additionalProperties": false, "properties": {"baseId": {"description": "The ID of the base (application) containing the page.\nMust start with \"app\" and is 17 characters long.\nExample: \"appZfrNIUEip5MazD\".\nDo not substitute user-facing names for baseId.\nTo get baseId, use the search_bases or list_bases tool.", "pattern": "^app[A-Za-z0-9]{14}$", "type": "string"}, "fieldIds": {"description": "Only data for fields whose IDs are in this list will be included in the result.\nIf not provided, all fields visible on the page will be returned.\nField IDs must start with \"fld\" and is 17 characters long.\nExample: \"fldGlRtkBNWfYnPOV\".\nDo not substitute user-facing names for IDs.\nTo get fieldId, use the list_tables_for_base tool.", "items": {"pattern": "^fld[A-Za-z0-9]{14}$", "type": "string"}, "type": "array"}, "interfaceId": {"description": "The ID of the interface that contains the page.\nMust start with \"pbd\" and is 17 characters long.", "pattern": "^pbd[A-Za-z0-9]{14}$", "type": "string"}, "path": {"additionalProperties": false, "description": "The navigation path from the page where the record was listed.\nConstruct the root from the same pageId used in list_records_for_page.", "properties": {"edges": {"description": "Linked record traversals leading to the target record.\nEmpty array if the record is directly listed on the root page.", "items": {"additionalProperties": false, "properties": {"fieldId": {"description": "The linked record field used to traverse to the detail page.\nField IDs must start with \"fld\" and is 17 characters long.\nExample: \"fldGlRtkBNWfYnPOV\".\nDo not substitute user-facing names for IDs.\nTo get fieldId, use the list_tables_for_base tool.", "pattern": "^fld[A-Za-z0-9]{14}$", "type": "string"}, "linkedRecordId": {"description": "The record to navigate to by following the linked record field.\nMust start with \"rec\" and is 17 characters long.\nExample: \"recZOTa3BDHxlJNzf\".\nDo not substitute user-facing names for IDs\nTo get recordId, use the list_records_for_table tool or display_records_for_table tools.", "pattern": "^rec[A-Za-z0-9]{14}$", "type": "string"}}, "required": ["fieldId", "linkedRecordId"], "type": "object"}, "type": "array"}, "root": {"additionalProperties": false, "description": "The page and starting record. Set once from list_records_for_page results;\nstays the same as edges are appended.", "properties": {"elementId": {"description": "The ID of the dashboard element to query. Required for dashboard pages.\nObtain element IDs from the dashboardElements array in the\nlist_pages_for_base response.\nMust start with \"pel\" and is 17 characters long.", "pattern": "^pel[A-Za-z0-9]{14}$", "type": "string"}, "pageId": {"description": "The page where the record was listed.\nMust start with \"pag\" and is 17 characters long.\nExample: \"pagXxYyZzAaBbCcDd\".", "pattern": "^pag[A-Za-z0-9]{14}$", "type": "string"}, "recordId": {"description": "A record from list_records_for_page results. With no edges, this is\nthe record returned. With edges, this is the starting point of the navigation.\nMust start with \"rec\" and is 17 characters long.\nExample: \"recZOTa3BDHxlJNzf\".\nDo not substitute user-facing names for IDs\nTo get recordId, use the list_records_for_table tool or display_records_for_table tools.", "pattern": "^rec[A-Za-z0-9]{14}$", "type": "string"}}, "required": ["pageId", "recordId"], "type": "object"}}, "required": ["root", "edges"], "type": "object"}}, "required": ["baseId", "interfaceId", "path"], "type": "object"}}</function>
<function>{"description": "Lists draft emails from the authenticated user's Gmail account. This tool can filter drafts based on a query string and supports pagination. It returns a list of drafts, including their IDs and subjects. `page_token` can be used to paginate the results. To retrieve subsequent pages of results, use the `page_token` returned in the previous response.", "name": "Gmail:list_drafts", "parameters": {"description": "Request message for ListDrafts RPC.", "properties": {"pageSize": {"description": "Optional. The maximum number of drafts to return. If unspecified, defaults to 20. The maximum allowed value is 50.", "format": "int32", "type": "integer"}, "pageToken": {"description": "Optional. A token received from a previous list_drafts call to retrieve the next page of results. Leave empty to fetch the first page. This is primarily used for pagination to continue fetching results from where the previous `ListDraft` call left off, especially when the number of drafts matching the query exceeds the page_size limit.", "type": "string"}, "query": {"description": "Examples: \"subject:OneMCP Update\" \"from:gduser1@workspacesamples.dev\" \"to:gduser2@workspacesamples.dev AND newer_than:7d\" \"project proposal has:attachment\" \"is:unread\" A space or a dash (`-`) will separate a number while a dot (`.`) will be a decimal. For example, `01.2047-100` is considered two numbers: `01.2047` and `100`. Note: If we want to ensure all drafts for the query are returned, we can paginate the results by making repeated calls to the tool until the response contains an empty list of drafts.", "type": "string"}}, "type": "object"}}</function>
<function>{"description": "Returns the calendars on the user's calendar list. Use this tool for queries like: * What are all my calendars? Example: list_calendars() # Returns all calendars the authenticated user has access to.", "name": "Google Calendar:list_calendars", "parameters": {"properties": {"pageSize": {"description": "Optional. Maximum number of entries returned on one result page.
