---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__tools__validate-branch-research-packages.js__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/tools/validate-branch-research-packages.js",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 3343,
  "source_sha256": "d068ea4e61b0c941e9f66af5b5963523dd17369d8a6da81c28945c17e78d3094",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

const fs = require('fs');
const path = require('path');
const vm = require('vm');

const packagesDir = path.join(__dirname, '..', 'data', 'packages');
const files = fs.readdirSync(packagesDir)
  .filter((file) => /^branch-research-batch-.*\.js$/.test(file))
  .sort();

const requiredDatasetFields = [
  'batchId',
  'researchedAt',
  'branchId',
  'branchName',
  'purpose',
  'targets'
];

const requiredTargetFields = [
  'opportunityId',
  'opportunityName',
  'status',
  'confidence',
  'confirmedVendors',
  'likelyResponsible',
  'publicLeads',
  'sourceLinks',
  'evidenceSummary',
  'branchDisplayText',
  'nextAction'
];

let failures = 0;

for (const file of files) {
  const fullPath = path.join(packagesDir, file);
  const source = fs.readFileSync(fullPath, 'utf8');
  const sandbox = { window: {} };

  try {
    vm.runInNewContext(source, sandbox, { filename: file });
  } catch (error) {
    failures += 1;
    console.error(`[syntax] ${file}: ${error.message}`);
    continue;
  }

  const exports = Object.entries(sandbox.window);
  if (exports.length !== 1) {
    failures += 1;
    console.error(`[export] ${file}: expected exactly one window export, found ${exports.length}`);
    continue;
  }

  const [exportName, dataset] = exports[0];
  if (!/^OPPORTUNITY_BRANCH_RESEARCH_BATCH_/.test(exportName)) {
    failures += 1;
    console.error(`[export] ${file}: unexpected export name ${exportName}`);
  }

  if (!dataset || typeof dataset !== 'object') {
    failures += 1;
    console.error(`[dataset] ${file}: ${exportName} is not an object`);
    continue;
  }

  for (const field of requiredDatasetFields) {
    if (!(field in dataset)) {
      failures += 1;
      console.error(`[dataset-field] ${file}: missing ${field}`);
    }
  }

  const expectedBatchId = file.replace(/\.js$/, '');
  if (dataset.batchId !== expectedBatchId) {
    failures += 1;
    console.error(`[batchId] ${file}: expected ${expectedBatchId}, found ${dataset.batchId}`);
  }

  if (!Array.isArray(dataset.targets) || dataset.targets.length === 0) {
    failures += 1;
    console.error(`[targets] ${file}: targets must be a non-empty array`);
    continue;
  }

  for (const [index, target] of dataset.targets.entries()) {
    for (const field of requiredTargetFields) {
      if (!(field in target)) {
        failures += 1;
        console.error(`[field] ${file}: target ${index} missing ${field}`);
      }
    }
    if (!Array.isArray(target.confirmedVendors)) {
      failures += 1;
      console.error(`[type] ${file}: target ${index} confirmedVendors must be an array`);
    }
    if (!Array.isArray(target.likelyResponsible)) {
      failures += 1;
      console.error(`[type] ${file}: target ${index} likelyResponsible must be an array`);
    }
    if (!Array.isArray(target.publicLeads)) {
      failures += 1;
      console.error(`[type] ${file}: target ${index} publicLeads must be an array`);
    }
    if (!Array.isArray(target.sourceLinks)) {
      failures += 1;
      console.error(`[type] ${file}: target ${index} sourceLinks must be an array`);
    }
  }

  console.log(`[ok] ${file} -> ${exportName} (${dataset.targets.length} targets)`);
}

if (failures > 0) {
  console.error(`Validation failed with ${failures} issue(s).`);
  process.exit(1);
}

console.log(`Validated ${files.length} branch research package(s).`);
