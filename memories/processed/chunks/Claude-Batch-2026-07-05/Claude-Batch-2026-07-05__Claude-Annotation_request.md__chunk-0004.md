---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-Annotation_request.md__chunk-0004",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-Annotation_request.md",
  "chunk_index": 4,
  "chunk_count_for_source": 13,
  "char_start": 31409,
  "char_end": 43409,
  "source_sha256": "186ac0494ab7dcbf74725a958409cf99f35d6edf14ed03be68cb24b110ec155d",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

ing
   144	4. **Save**: Write to file
   145	5. **Recalculate formulas (MANDATORY IF USING FORMULAS)**: Use the scripts/recalc.py script
   146	   ```bash
   147	   python scripts/recalc.py output.xlsx
   148	   ```
   149	6. **Verify and fix any errors**: 
   150	   - The script returns JSON with error details
   151	   - If `status` is `errors_found`, check `error_summary` for specific error types and locations
   152	   - Fix the identified errors and recalculate again
   153	   - Common errors to fix:
   154	     - `#REF!`: Invalid cell references
   155	     - `#DIV/0!`: Division by zero
   156	     - `#VALUE!`: Wrong data type in formula
   157	     - `#NAME?`: Unrecognized formula name
   158	
   159	### Creating new Excel files
   160	
   161	```python
   162	# Using openpyxl for formulas and formatting
   163	from openpyxl import Workbook
   164	from openpyxl.styles import Font, PatternFill, Alignment
   165	
   166	wb = Workbook()
   167	sheet = wb.active
   168	
   169	# Add data
   170	sheet['A1'] = 'Hello'
   171	sheet['B1'] = 'World'
   172	sheet.append(['Row', 'of', 'data'])
   173	
   174	# Add formula
   175	sheet['B2'] = '=SUM(A1:A10)'
   176	
   177	# Formatting
   178	sheet['A1'].font = Font(bold=True, color='FF0000')
   179	sheet['A1'].fill = PatternFill('solid', start_color='FFFF00')
   180	sheet['A1'].alignment = Alignment(horizontal='center')
   181	
   182	# Column width
   183	sheet.column_dimensions['A'].width = 20
   184	
   185	wb.save('output.xlsx')
   186	```
   187	
   188	### Editing existing Excel files
   189	
   190	```python
   191	# Using openpyxl to preserve formulas and formatting
   192	from openpyxl import load_workbook
   193	
   194	# Load existing file
   195	wb = load_workbook('existing.xlsx')
   196	sheet = wb.active  # or wb['SheetName'] for specific sheet
   197	
   198	# Working with multiple sheets
   199	for sheet_name in wb.sheetnames:
   200	    sheet = wb[sheet_name]
   201	    print(f"Sheet: {sheet_name}")
   202	
   203	# Modify cells
   204	sheet['A1'] = 'New Value'
   205	sheet.insert_rows(2)  # Insert row at position 2
   206	sheet.delete_cols(3)  # Delete column 3
   207	
   208	# Add new sheet
   209	new_sheet = wb.create_sheet('NewSheet')
   210	new_sheet['A1'] = 'Data'
   211	
   212	wb.save('modified.xlsx')
   213	```
   214	
   215	## Recalculating formulas
   216	
   217	Excel files created or modified by openpyxl contain formulas as strings but not calculated values. Use the provided `scripts/recalc.py` script to recalculate formulas:
   218	
   219	```bash
   220	python scripts/recalc.py <excel_file> [timeout_seconds]
   221	```
   222	
   223	Example:
   224	```bash
   225	python scripts/recalc.py output.xlsx 30
   226	```
   227	
   228	The script:
   229	- Automatically sets up LibreOffice macro on first run
   230	- Recalculates all formulas in all sheets
   231	- Scans ALL cells for Excel errors (#REF!, #DIV/0!, etc.)
   232	- Returns JSON with detailed error locations and counts
   233	- Works on both Linux and macOS
   234	
   235	## Formula Verification Checklist
   236	
   237	Quick checks to ensure formulas work correctly:
   238	
   239	### Essential Verification
   240	- [ ] **Test 2-3 sample references**: Verify they pull correct values before building full model
   241	- [ ] **Column mapping**: Confirm Excel columns match (e.g., column 64 = BL, not BK)
   242	- [ ] **Row offset**: Remember Excel rows are 1-indexed (DataFrame row 5 = Excel row 6)
   243	
   244	### Common Pitfalls
   245	- [ ] **NaN handling**: Check for null values with `pd.notna()`
   246	- [ ] **Far-right columns**: FY data often in columns 50+ 
   247	- [ ] **Multiple matches**: Search all occurrences, not just first
   248	- [ ] **Division by zero**: Check denominators before using `/` in formulas (#DIV/0!)
   249	- [ ] **Wrong references**: Verify all cell references point to intended cells (#REF!)
   250	- [ ] **Cross-sheet references**: Use correct format (Sheet1!A1) for linking sheets
   251	
   252	### Formula Testing Strategy
   253	- [ ] **Start small**: Test formulas on 2-3 cells before applying broadly
   254	- [ ] **Verify dependencies**: Check all cells referenced in formulas exist
   255	- [ ] **Test edge cases**: Include zero, negative, and very large values
   256	
   257	### Interpreting scripts/recalc.py Output
   258	The script returns JSON with error details:
   259	```json
   260	{
   261	  "status": "success",           // or "errors_found"
   262	  "total_errors": 0,              // Total error count
   263	  "total_formulas": 42,           // Number of formulas in file
   264	  "error_summary": {              // Only present if errors found
   265	    "#REF!": {
   266	      "count": 2,
   267	      "locations": ["Sheet1!B5", "Sheet1!C10"]
   268	    }
   269	  }
   270	}
   271	```
   272	
   273	## Best Practices
   274	
   275	### Library Selection
   276	- **pandas**: Best for data analysis, bulk operations, and simple data export
   277	- **openpyxl**: Best for complex formatting, formulas, and Excel-specific features
   278	
   279	### Working with openpyxl
   280	- Cell indices are 1-based (row=1, column=1 refers to cell A1)
   281	- Use `data_only=True` to read calculated values: `load_workbook('file.xlsx', data_only=True)`
   282	- **Warning**: If opened with `data_only=True` and saved, formulas are replaced with values and permanently lost
   283	- For large files: Use `read_only=True` for reading or `write_only=True` for writing
   284	- Formulas are preserved but not evaluated - use scripts/recalc.py to update values
   285	
   286	### Working with pandas
   287	- Specify data types to avoid inference issues: `pd.read_excel('file.xlsx', dtype={'id': str})`
   288	- For large files, read specific columns: `pd.read_excel('file.xlsx', usecols=['A', 'C', 'E'])`
   289	- Handle dates properly: `pd.read_excel('file.xlsx', parse_dates=['date_column'])`
   290	
   291	## Code Style Guidelines
   292	**IMPORTANT**: When generating Python code for Excel operations:
   293	- Write minimal, concise Python code without unnecessary comments
   294	- Avoid verbose variable names and redundant operations
   295	- Avoid unnecessary print statements
   296	
   297	**For Excel files themselves**:
   298	- Add comments to cells with complex formulas or important assumptions
   299	- Document data sources for hardcoded values
   300	- Include notes for key calculations and model sectionsGood — now let me read the actual file content properly.{"returncode":0,"stdout":"Sheets: ['Page 1 - Business Info', 'Page 2 - Signers 1-2', 'Page 3 - Signers 3-4', 'All Fields']\n\n=== Sheet: Page 1 - Business Info ===\n                                                                               0                                                                              1                                                                              2                                                                              3                                                                              4                                                                              5                                                                              6                                                                              7                                                                              8                                             9                                      10                                     11\n0                                                 Arizona Financial\\nCREDIT UNION                                                Arizona Financial\\nCREDIT UNION                                                Arizona Financial\\nCREDIT UNION                                                 Business Information Worksheet                                                 Business Information Worksheet                                                 Business Information Worksheet                                                 Business Information Worksheet                                                 Business Information Worksheet                                                 Business Information Worksheet                Business Information Worksheet         Business Information Worksheet         Business Information Worksheet\n1                                                 Arizona Financial\\nCREDIT UNION                                                Arizona Financial\\nCREDIT UNION                                                Arizona Financial\\nCREDIT UNION                                                 Business Information Worksheet                                                 Business Information Worksheet                                                 Business Information Worksheet                                                 Business Information Worksheet                                                 Business Information Worksheet                                                 Business Information Worksheet                Business Information Worksheet         Business Information Worksheet         Business Information Worksheet\n2                                                 Arizona Financial\\nCREDIT UNION                                                Arizona Financial\\nCREDIT UNION                                                Arizona Financial\\nCREDIT UNION                                                 Business Information Worksheet                                                 Business Information Worksheet                                                 Business Information Worksheet                                                 Business Information Worksheet                                                 Business Information Worksheet                                                 Business Information Worksheet                Business Information Worksheet         Business Information Worksheet         Business Information Worksheet\n3                                                                             NaN                                                                            NaN                                                                            NaN                                                                            NaN                                                                            NaN                                                                            NaN                                                                            NaN                                                                            NaN                                                                            NaN                                           NaN                                    NaN                                    NaN\n4                                                           Business Information:                                                          Business Information:                                                          Business Information:                                                          Business Information:                                                          Business Information:                                                          Business Information:                                                          Business Information:                                                          Business Information:                                                          Business Information:                         Business Information:                  Business Information:                  Business Information:\n5                                                                     Entity Name                                                                    Entity Name                                                                    Entity Name                       
