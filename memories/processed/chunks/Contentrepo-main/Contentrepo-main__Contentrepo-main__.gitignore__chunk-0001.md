---
{
  "chunk_id": "Contentrepo-main__Contentrepo-main__.gitignore__chunk-0001",
  "archive_id": "Contentrepo-main",
  "archive_filename": "Contentrepo-main.zip",
  "source_path": "Contentrepo-main/.gitignore",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 442,
  "source_sha256": "0a84c9ade1773b703096600959ab96212df9f3fb440c38118a3371e9b53e72fb",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Dependencies
node_modules/
*.npm
package-lock.json
yarn.lock

# Environment variables
.env
.env.local
.env.*.local

# Build outputs
dist/
build/
.next/
out/
*.tsbuildinfo

# IDE & Editor
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Logs
logs/
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Testing
coverage/
.nyc_output/

# OS files
Thumbs.db
.DS_Store

# Temporary files
*.tmp
*.temp
.cache/

# Development databases
*.db
*.sqlite
