---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__tools__validate-static-app.js__chunk-0002",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/tools/validate-static-app.js",
  "chunk_index": 2,
  "chunk_count_for_source": 2,
  "char_start": 11386,
  "char_end": 20523,
  "source_sha256": "8f6dbc097661ab7c09d13c612d3c11678b3ba8cb33ac8edd6b34a55dbad5bf17",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

 updates use non-normalized IATSE/local wording');
check(routeUpdates.includes('verify applicable IATSE/local jurisdiction'), 'route research updates missing preferred IATSE/local jurisdiction wording');

const css = exists('assets/atlas.css') ? read('assets/atlas.css') : '';
check(!/\.chip\b/.test(css), 'assets/atlas.css still contains chip badge styles');
check(!/\.chips\b/.test(css), 'assets/atlas.css still contains chip container styles');

const readme = exists('README.md') ? read('README.md') : '';
check(readme.includes('Source-of-truth rule'), 'README.md missing source-of-truth rule');
check(readme.includes('Collaboration log rule'), 'README.md missing collaboration log rule');
check(readme.includes('ai-communication/collaboration-log/'), 'README.md missing collaboration log folder path');
check(readme.includes('one new file per commit'), 'README.md missing one-file-per-commit collaboration log rule');
check(readme.includes('Status: complete | incomplete | blocked | superseded'), 'README.md missing collaboration log status metadata rule');
check(readme.includes('Two-week cleanup rule'), 'README.md missing collaboration log two-week cleanup rule');
check(readme.includes('ai-communication/collaboration-log/incomplete/'), 'README.md missing incomplete collaboration log folder path');
check(readme.includes('incomplete or blocked logs must remain auditable'), 'README.md missing incomplete/blocked audit retention rule');
check(readme.includes('data/packages/research-queue-route-updates.js'), 'README.md missing active route research update package');
check(readme.includes('data/iatse-organization-info.js'), 'README.md missing IATSE organization info asset');
check(readme.includes('Required runtime load order'), 'README.md missing required runtime load order section');
check(readme.includes('index.html        Home: quick explanation'), 'README.md missing current Home page role');
check(readme.includes('guide.html        Full Guide for Use'), 'README.md missing current Guide page role');
check(readme.includes('Guide and Sources are footer/reference links'), 'README.md missing current footer-only Guide/Sources rule');
check(readme.includes('Retired public helpers must not be reintroduced'), 'README.md missing retired helper rule');
check(readme.includes('verify applicable IATSE/local jurisdiction'), 'README.md missing normalized IATSE/local jurisdiction language rule');
check(readme.includes('README current when significant app behavior'), 'README.md missing strengthened README maintenance rule');

const driftProtocol = exists('ai-communication/DOCUMENT_DRIFT_CONTROL_PROTOCOL.md') ? read('ai-communication/DOCUMENT_DRIFT_CONTROL_PROTOCOL.md') : '';
check(driftProtocol.includes('main must never be edited'), 'DOCUMENT_DRIFT_CONTROL_PROTOCOL.md missing main-branch protection language');
check(driftProtocol.includes('research-version is the intended live working branch'), 'DOCUMENT_DRIFT_CONTROL_PROTOCOL.md missing research-version live branch rule');

const collaborationLogReadme = exists('ai-communication/collaboration-log/README.md') ? read('ai-communication/collaboration-log/README.md') : '';
check(collaborationLogReadme.includes('one collaboration log file per commit'), 'collaboration-log README missing one-file-per-commit purpose');
check(collaborationLogReadme.includes('YYYY-MM-DD-###-assistant-short-topic.md'), 'collaboration-log README missing filename pattern');
check(collaborationLogReadme.includes('Status: complete | incomplete | blocked | superseded'), 'collaboration-log README missing status metadata options');
check(collaborationLogReadme.includes('Review after: YYYY-MM-DD'), 'collaboration-log README missing review-after metadata');
check(collaborationLogReadme.includes('Every two weeks'), 'collaboration-log README missing two-week review cadence');
check(collaborationLogReadme.includes('Do not maintain one giant append-only ledger'), 'collaboration-log README missing no-giant-ledger rule');
check(collaborationLogReadme.includes('Do not delete incomplete or blocked logs'), 'collaboration-log README missing incomplete retention rule');

const incompleteReadme = exists('ai-communication/collaboration-log/incomplete/README.md') ? read('ai-communication/collaboration-log/incomplete/README.md') : '';
check(incompleteReadme.includes('Incomplete Collaboration Logs'), 'incomplete collaboration log README missing title');
check(incompleteReadme.includes('Do not delete files from this folder'), 'incomplete collaboration log README missing no-delete rule');
check(incompleteReadme.includes('Aaron can manually delete'), 'incomplete collaboration log README missing manual deletion rule');

if (fs.existsSync(collaborationLogDir)) {
  const logEntries = fs.readdirSync(collaborationLogDir)
    .filter(name => /^\d{4}-\d{2}-\d{2}-\d{3}-.*\.md$/.test(name));
  check(logEntries.length > 0, 'collaboration-log folder has no dated numbered log entries');
  logEntries.forEach(name => validateCollaborationEntry(path.join('ai-communication', 'collaboration-log', name)));
} else {
  fail.push('Missing collaboration-log folder');
}

if (fs.existsSync(incompleteCollaborationLogDir)) {
  const incompleteEntries = fs.readdirSync(incompleteCollaborationLogDir)
    .filter(name => /^\d{4}-\d{2}-\d{2}-\d{3}-.*\.md$/.test(name));
  incompleteEntries.forEach(name => validateCollaborationEntry(path.join('ai-communication', 'collaboration-log', 'incomplete', name)));
} else {
  fail.push('Missing incomplete collaboration-log folder');
}

const employersData = exists('data/packages/us-employers.js') ? read('data/packages/us-employers.js') : '';
legacyBridgeMarkers.forEach(marker => {
  check(!employersData.includes(marker), `us-employers.js still contains legacy branch bridge marker: ${marker}`);
});

const branchPackages = listBranchPackages();
check(branchPackages.length > 0, 'No branch research package files found');

let manifestFiles = [];
if (exists('data/packages/branch-research-manifest.js')) {
  const source = read('data/packages/branch-research-manifest.js');
  const sandbox = { window: {} };
  try {
    vm.runInNewContext(source, sandbox, { filename: 'branch-research-manifest.js' });
    if (Array.isArray(sandbox.window.BRANCH_RESEARCH_MANIFEST)) {
      manifestFiles = sandbox.window.BRANCH_RESEARCH_MANIFEST.slice().sort();
    } else {
      fail.push('branch-research-manifest.js does not export window.BRANCH_RESEARCH_MANIFEST as an array');
    }
  } catch (error) {
    fail.push(`branch-research-manifest.js syntax/runtime error: ${error.message}`);
  }
}

branchPackages.forEach(name => {
  check(manifestFiles.includes(name), `Manifest missing data package: ${name}`);
  const report = path.join(researchDir, name.replace(/\.js$/, '.md'));
  check(fs.existsSync(report), `Missing research report for data package: research/${name.replace(/\.js$/, '.md')}`);
});
manifestFiles.forEach(name => {
  check(branchPackages.includes(name), `Manifest references missing data package: ${name}`);
});

const legacyRuntime = exists('data/packages/branch-research-runtime.js') ? read('data/packages/branch-research-runtime.js') : '';
if (legacyRuntime) {
  check(legacyRuntime.includes('__branchResearchRuntimeArchived'), 'branch-research-runtime.js exists but is not inert/archived');
}

// --- Asset hygiene: no orphaned scripts, uniform cache versions ------------
// Catches two recurring agent mistakes: leaving dead scripts behind, and
// forgetting to bump a cache version uniformly after editing an asset.
const allHtml = fs.readdirSync(root).filter(f => f.endsWith('.html'));
const htmlBodies = allHtml.map(f => ({ file: f, content: fs.readFileSync(path.join(root, f), 'utf8') }));
const assetsPath = path.join(root, 'assets');
const assetScripts = fs.existsSync(assetsPath)
  ? fs.readdirSync(assetsPath).filter(f => f.endsWith('.js'))
  : [];
assetScripts.forEach(name => {
  const referenced = htmlBodies.some(h => h.content.includes('assets/' + name));
  check(referenced, `Orphaned asset (loaded by no page): assets/${name} — wire it into a page or delete it`);
  const versions = new Set();
  const re = new RegExp('assets/' + name.replace(/[.]/g, '\\.') + '\\?v=([A-Za-z0-9]+)', 'g');
  htmlBodies.forEach(h => { let m; while ((m = re.exec(h.content))) versions.add(m[1]); });
  check(versions.size <= 1,
    `Inconsistent cache version for assets/${name}: [${[...versions].join(', ')}] — bump the same ?v= on every page that loads it`);
});

if (warn.length) {
  console.warn('\nWarnings:');
  warn.forEach(message => console.warn(`- ${message}`));
}

if (fail.length) {
  console.error('\nFailures:');
  fail.forEach(message => console.error(`- ${message}`));
  process.exit(1);
}

console.log(`Production Atlas static app validation passed. ${branchPackages.length} branch package(s) are covered by the manifest and reports. Current header nav excludes Guide and Sources; Guide/Sources live in footer/reference flow; core owns opportunity sorting, promoter filtering, and IATSE rendering; README source-of-truth coverage, separate 2027 rollover, collaboration-log lifecycle, and public-safe route language are active.`);
