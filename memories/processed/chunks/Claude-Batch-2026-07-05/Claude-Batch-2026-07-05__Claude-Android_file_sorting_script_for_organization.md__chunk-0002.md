---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-Android_file_sorting_script_for_organization.md__chunk-0002",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-Android_file_sorting_script_for_organization.md",
  "chunk_index": 2,
  "chunk_count_for_source": 12,
  "char_start": 11346,
  "char_end": 23306,
  "source_sha256": "ca3b2b0e32079007fbf9e90f6559244ee7846685caaa43ae8cb0e53e2cf818ab",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

55	            "Videos": {"extensions": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"]},
   156	            "Audio": {"extensions": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"]},
   157	            "Documents": {"extensions": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf"]},
   158	            "Archives": {"extensions": [".zip", ".rar", ".7z", ".tar", ".gz"]},
   159	            "Misc": {"extensions": []}
   160	        },
   161	        "NeedsReview": {
   162	            "Images": {"extensions": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".heic"]},
   163	            "Videos": {"extensions": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"]},
   164	            "Audio": {"extensions": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"]},
   165	            "Documents": {"extensions": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf"]},
   166	            "Archives": {"extensions": [".zip", ".rar", ".7z", ".tar", ".gz"]},
   167	            "Other": {"extensions": []}
   168	        }
   169	    },
   170	    "collision_strategy": "rename_suffix" 
   171	}
   172	```
   173	
   174	### Key Configuration Options:
   175	
   176	*   `scan_roots`: **CRITICAL**. A list of absolute paths to the top-level directories you want the script to scan. **Only files within these directories (and their subdirectories) will be considered.** Add or remove paths as needed.
   177	    *   *Example*: `"/sdcard/Download"`, `"/sdcard/MyBusinessDocs"`
   178	*   `exclude_paths`: A list of absolute paths to directories that should be completely ignored during scanning. **Do NOT remove `/sdcard/Android/data` or `/sdcard/Android/obb` from this list.**
   179	*   `output_base_dir`: The absolute path where the `Business`, `Personal`, and `NeedsReview` folders will be created.
   180	*   `categories`: This is the core of the classification logic. You can define:
   181	    *   **Business Categories**: Each business (e.g., `DeadhangLaborLLC`) can have its own `keywords` (for filename/content matching), `source_dirs` (files in these directories are always business), and `subfolders` (for finer-grained organization within the business category).
   182	    *   **Personal Categories**: Defined by `extensions` (e.g., `.jpg` for `Images`).
   183	    *   **NeedsReview Categories**: Files that don't clearly fit into Business or Personal will go here, also organized by `extensions`.
   184	*   `collision_strategy`: Currently set to `"rename_suffix"`. This means if `file.txt` is to be moved to a location where `file.txt` already exists, it will be renamed to `file_dup1.txt`, `file_dup2.txt`, etc.
   185	
   186	## 6. Usage
   187	
   188	Navigate to the script's directory in Termux:
   189	```bash
   190	cd /sdcard/Download/Organizer/
   191	```
   192	
   193	### Scan Mode (Dry Run)
   194	
   195	This is the **default and safest mode**. It scans your files, determines proposed moves, and generates a detailed HTML report, but **does not move any files**. This is essential for reviewing the script's decisions.
   196	
   197	```bash
   198	python organizer.py
   199	```
   200	
   201	After the scan, the script will print instructions to open the generated HTML report:
   202	
   203	```
   204	==================================================
   205	SCAN COMPLETE. ACTION REQUIRED.
   206	==================================================
   207	1. Please open this file in your web browser to review the proposed changes:
   208	   file:///sdcard/Download/manifests/report_YYYYMMDD_HHMMSS.html
   209	2. Review the 'Reason' column to see why files were classified.
   210	3. Check the log file for any warnings or errors: file:///sdcard/Download/file_organizer_system.log
   211	==================================================
   212	```
   213	
   214	Open the `report_*.html` file in your Android browser (e.g., Chrome) to review the proposed changes. If you are satisfied, return to Termux to proceed.
   215	
   216	### Execute Mode
   217	
   218	Once you have reviewed the HTML report and are confident in the proposed moves, run the script with the `--execute` flag:
   219	
   220	```bash
   221	python organizer.py --execute
   222	```
   223	
   224	The script will again prompt you for confirmation:
   225	
   226	```
   227	Have you reviewed the HTML report? Do you want to proceed with moving the files? (yes/no): 
   228	```
   229	
   230	Type `yes` and press Enter to start the file movements. Type `no` to cancel.
   231	
   232	### Undo Operation
   233	
   234	If you need to revert a previous execution, you can use the `undo.py` script with the manifest file generated during the execution.
   235	
   236	First, locate the manifest file for the run you want to undo. These are stored in `/sdcard/Download/manifests/` and named `manifest_YYYYMMDD_HHMMSS.json`.
   237	
   238	Then, run the `undo.py` script, providing the full path to the manifest file:
   239	
   240	```bash
   241	python undo.py /sdcard/Download/manifests/manifest_YYYYMMDD_HHMMSS.json
   242	```
   243	
   244	The `undo.py` script will attempt to move files back to their original locations, performing checksum verification during the process.
   245	
   246	## 7. Output Folder Structure
   247	
   248	The script will create the following structure under your `output_base_dir` (default: `/sdcard/Organized`):
   249	
   250	```
   251	/sdcard/Organized/
   252	  Business/
   253	    DeadhangLaborLLC/
   254	      Invoices/
   255	      Contracts/
   256	      CrewSchedules/
   257	      Other/ (for files matching DeadhangLaborLLC but not specific subfolders)
   258	    TheCrewBlueprint/
   259	      CourseMaterials/
   260	      Other/ (for files matching TheCrewBlueprint but not specific subfolders)
   261	    Code/ (for all identified code files)
   262	    GeneralBusiness/ (for general business files not tied to a specific LLC)
   263	      Documents/
   264	      Other/
   265	  Personal/
   266	    Images/
   267	    Videos/
   268	    Audio/
   269	    Documents/
   270	    Archives/
   271	    Misc/
   272	  NeedsReview/
   273	    Images/
   274	    Videos/
   275	    Audio/
   276	    Documents/
   277	    Archives/
   278	    Other/
   279	```
   280	
   281	## 8. Logging and Manifests
   282	
   283	*   **System Log**: `file_organizer_system.log` (located in `/sdcard/Download/`) records all script activities, warnings, and errors. This is crucial for debugging and understanding script behavior.
   284	*   **Manifests**: Each successful execution (when `--execute` is used and confirmed) generates a `manifest_YYYYMMDD_HHMMSS.json` file in `/sdcard/Download/manifests/`. This JSON file contains a record of every file moved, its original path, new path, checksum, and classification reason. It is essential for the undo functionality.
   285	
   286	## 9. Known Limitations
   287	
   288	*   **Scoped Storage**: Due to Android's scoped storage restrictions (Android 10+), Termux cannot access private data directories of other apps (e.g., `/sdcard/Android/data/*`, `/sdcard/Android/obb/*`). The script explicitly excludes these paths.
   289	*   **Encrypted Files**: The script cannot read the content of encrypted files. Classification for such files will rely solely on filename, extension, and source directory.
   290	*   **Non-Text Files**: Content-based classification is only effective for text-readable files. Binary files (images, videos, archives) are classified based on filename, extension, and source directory.
   291	*   **Active Projects**: Moving files that are part of active coding projects or app data might break those projects. Use caution and ensure such files are not actively in use or are backed up via other means (e.g., Git) before moving.
   292	
   293	## 10. Troubleshooting
   294	
   295	*   **"Permission denied" errors**: Ensure you have run `termux-setup-storage` and granted all necessary permissions to Termux. Also, check the `LOG_FILE` for specific permission errors.
   296	*   **Files not moving**: Always run in dry-run mode first and check the HTML report. Review the 'Reason' column for why a file might be skipped or classified unexpectedly. Check `file_organizer_system.log` for warnings or errors.
   297	*   **Script crashes**: Check the `file_organizer_system.log` for critical errors. Ensure your `config.json` is valid JSON and all paths are correctly specified.
   298	*   **Undo not working**: Verify that the manifest file you are using with `undo.py` is correct and corresponds to the execution you wish to revert. Check the log file for undo-specific errors.
   299	
   300	---
   301	
   302	*This tool was developed by Manus AI to provide a safe and robust file organization solution for Android users.*
   303	This file is only the README — it documents the script but contains no actual code. The two other files are likely the prompt. Let me check them to confirm there's no code anywhere.     1	# Build Prompt: Safe Android File Organizer (Business vs. Personal)
     2	
     3	Copy everything below this line into your AI coding agent.
     4	
     5	---
     6	
     7	## Role
     8	
     9	You are building a Python script that runs **on an Android phone via Termux** and safely sorts files in shared storage into clearly separated **business** and **personal** categories. Data safety is the top priority — this script will run against my real, irreplaceable files. Speed, cleverness, or "doing more automatically" are never worth a deletion or a corrupted file. When in doubt, the script should skip the file and log it for manual review rather than guess.
    10	
    11	Before writing any code, restate your understanding of the safety constraints below in your own words, then ask me any clarifying questions about folder paths or category names. Do not generate the final script until I confirm.
    12	
    13	## Platform Constraints (read first)
    14	
    15	- Target environment is **Termux** on Android (no root assumed). Python runs inside Termux; file access goes through `~/storage/shared` after the user runs `termux-setup-storage`, which symlinks to the standard public directories (`DCIM`, `Download`, `Documents`, `Pictures`, `Movies`, `Music`, etc.).
    16	- Since Android 10+, scoped storage means Termux **cannot** reliably access another app's private data folders (e.g., `Android/data/*`, `Android/obb/*`) without special permission grants that vary by OEM and Android version. The script must **never attempt to read/write inside `Android/data` or `Android/obb`** — treat these as hard exclusions regardless of config.
    17	- Do not assume access to system partitions (`/system`, `/data`) — the script should only ever operate inside paths explicitly passed to it within the shared storage tree.
    18	- If you hit a permission error, the script should log it and continue — never crash the whole run over one inaccessible folder.
    19	
    20	## Non-Negotiable Safety Requirements
    21	
    22	1. **No deletion, ever.** The script only **moves** (or optionally copies) files. There is no delete function anywhere in the codebase, including in cleanup/rollback code.
    23	2. **Dry-run by default.** Running the script with no flags produces a full preview report of every planned move and **changes nothing**. Actual moves only happen with an explicit `--execute` flag.
    24	3. **Checksum-verified moves.** Before removing a file from its source location, the script must: copy it to the destination, compute a SHA-256 hash of both source and destination, confirm they match, and only then remove the source. If hashes don't match, abort that file's move, leave the original untouched, and log it as an error.
    25	4. **Full manifest for every run.** Every single action (or skip) gets logged to a timestamped JSON or CSV manifest: original path, new path, checksum, timestamp, and outcome (moved / skipped / collision / error).
