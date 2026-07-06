---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__tools__validate-static-app.js__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/tools/validate-static-app.js",
  "chunk_index": 1,
  "chunk_count_for_source": 2,
  "char_start": 0,
  "char_end": 11986,
  "source_sha256": "8f6dbc097661ab7c09d13c612d3c11678b3ba8cb33ac8edd6b34a55dbad5bf17",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

const fs = require('fs');
const path = require('path');
const vm = require('vm');

const root = path.resolve(__dirname, '..');
const packagesDir = path.join(root, 'data', 'packages');
const researchDir = path.join(root, 'research');
const collaborationLogDir = path.join(root, 'ai-communication', 'collaboration-log');
const incompleteCollaborationLogDir = path.join(collaborationLogDir, 'incomplete');

const requiredCorePages = [
  'index.html',
  'calendar.html',
  'opportunities.html',
  'branches.html',
  'employers.html',
  'iatse.html',
  'matrix.html',
  'analytics.html',
  'sources.html',
  'guide.html',
  'map.html',
  'schedule.html'
];

const requiredPublicPages = [
  ...requiredCorePages,
  'about.html',
  'data-methodology.html',
  'employer-route-methodology.html',
  'date-work-window-disclaimer.html',
  'privacy-policy.html',
  'terms-and-conditions.html',
  'limitation-of-liability.html',
  'cookie-notice.html',
  'accessibility.html',
  'affiliate-disclosure.html',
  'contact-data-requests.html',
  'contribute.html',
  'feedback.html'
];

const requiredSharedFiles = [
  'assets/atlas.css',
  'assets/atlas-core-v2.js',
  'assets/approx-date-labels.js',
  'assets/calendar-interactive.js',
  'assets/map-page-static.js',
  'assets/employers-department-browser.js',
  'assets/sources-employer-links.js',
  'assets/festival-modal-public-safe.js',
  'assets/site-footer.js',
  'assets/icons.js',
  'data/packages/opportunity-taxonomy.js',
  'data/packages/research-queue-route-updates.js',
  'data/packages/opportunity-rollover-2027.js',
  'data/packages/branch-research-manifest.js',
  'data/packages/production-branches.js',
  'data/packages/opportunities-2026.js',
  'data/packages/us-employers.js',
  'data/packages/opportunity-coords.js',
  'data/iatse-us-local-directory.js',
  'data/iatse-organization-info.js',
  'archive/README.md',
  'ai-communication/collaboration-log/README.md',
  'ai-communication/collaboration-log/incomplete/README.md',
  'ai-communication/DOCUMENT_DRIFT_CONTROL_PROTOCOL.md'
];

const retiredRuntimeReferences = [
  'data/packages/branch-research-runtime.js',
  'data/packages/guide-for-use-runtime.js',
  'assets/opportunities-promoter-filter.js',
  'assets/opportunities-date-sort.js',
  'assets/iatse-page.js',
  'assets/confidence-badges.js'
];

const legacyBridgeMarkers = [
  '__branchPopupBridgeInstalled',
  'BRANCH_EMPLOYER_LEADS={branches:{}}',
  'window.BRANCH_EMPLOYER_LEADS={branches:{}}'
];

const headerNavPages = [
  ...requiredCorePages,
  'about.html',
  'contribute.html',
  'feedback.html',
  'sources.html'
];

let fail = [];
let warn = [];

function file(rel) {
  return path.join(root, rel);
}

function exists(rel) {
  return fs.existsSync(file(rel));
}

function read(rel) {
  return fs.readFileSync(file(rel), 'utf8');
}

function check(condition, message) {
  if (!condition) fail.push(message);
}

function caution(condition, message) {
  if (!condition) warn.push(message);
}

function listBranchPackages() {
  if (!fs.existsSync(packagesDir)) return [];
  return fs.readdirSync(packagesDir)
    .filter((name) => /^branch-research-batch-.*\.js$/.test(name))
    .sort();
}

function validateCollaborationEntry(relPath) {
  const text = read(relPath);
  check(/^Status: (complete|incomplete|blocked|superseded|superseded in part)$/m.test(text), `${relPath} missing valid Status metadata`);
  check(/^Created: \d{4}-\d{2}-\d{2}$/m.test(text), `${relPath} missing Created date metadata`);
  check(/^Review after: \d{4}-\d{2}-\d{2}$/m.test(text), `${relPath} missing Review after date metadata`);
  check(/^Assistant: /m.test(text), `${relPath} missing Assistant metadata`);
  check(/^Branch: research-version$/m.test(text), `${relPath} missing research-version branch metadata`);
  // Accept "Commit:", "Commits:" or "Commit range:" — connector-only sessions
  // can't know a hash before committing, so any traceable form is valid.
  check(/^Commit(s|\srange)?:\s/m.test(text), `${relPath} missing Commit metadata`);
  check(text.includes('## Validation status'), `${relPath} missing Validation status section`);
  check(text.includes('## Next action'), `${relPath} missing Next action section`);
}

requiredPublicPages.forEach(page => check(exists(page), `Missing required page: ${page}`));
requiredSharedFiles.forEach(sharedFile => check(exists(sharedFile), `Missing required shared file: ${sharedFile}`));

const corePageText = requiredCorePages.filter(exists).map(page => ({ file: page, content: read(page) }));
const allPageText = requiredPublicPages.filter(exists).map(page => ({ file: page, content: read(page) }));

corePageText.forEach(({ file, content }) => {
  check(content.includes('assets/atlas.css'), `${file} does not load shared CSS`);
  check(content.includes('assets/atlas-core-v2.js'), `${file} does not load direct atlas-core-v2.js`);
  check(content.includes('assets/approx-date-labels.js'), `${file} does not load approximate date helper`);
  check(content.includes('data/packages/opportunity-taxonomy.js'), `${file} does not load opportunity taxonomy package`);
  check(content.includes('data/packages/research-queue-route-updates.js'), `${file} does not load route research updates package`);
  check(content.includes('data/packages/opportunity-rollover-2027.js'), `${file} does not load 2027 rollover package`);
  check(content.includes('assets/site-footer.js'), `${file} does not load site footer normalizer`);
  check(!content.includes('Home / Guide'), `${file} still uses combined Home / Guide nav label`);
  retiredRuntimeReferences.forEach(retired => {
    check(!content.includes(retired), `${file} still loads retired runtime: ${retired}`);
  });
  legacyBridgeMarkers.forEach(marker => {
    check(!content.includes(marker), `${file} still contains legacy branch bridge marker: ${marker}`);
  });
});

headerNavPages.filter(exists).forEach(page => {
  const content = read(page);
  if (!content.includes('navInner')) return;
  check(content.includes('href="index.html"') || content.includes('href="./index.html"'), `${page} missing Home header nav link`);
  check(content.includes('opportunities.html'), `${page} missing Opportunities header nav link`);
  check(content.includes('calendar.html'), `${page} missing Calendar header nav link`);
  check(content.includes('map.html'), `${page} missing Map header nav link`);
  check(content.includes('employers.html'), `${page} missing Employers header nav link`);
  check(content.includes('iatse.html'), `${page} missing IATSE header nav link`);
  // Schedule feature temporarily removed (to be rebuilt); no header nav link required.
  check(content.includes('contribute.html'), `${page} missing Contribute header nav link`);
  check(!/<nav[\s\S]*href="(?:\.\/)?guide\.html"[\s\S]*<\/nav>/i.test(content), `${page} puts Guide in header nav; Guide belongs on home top and footer`);
  check(!/<nav[\s\S]*href="(?:\.\/)?sources\.html"[\s\S]*<\/nav>/i.test(content), `${page} puts Sources in header nav; Sources belongs in footer/contextual links`);
});

allPageText.forEach(({ file, content }) => {
  retiredRuntimeReferences.forEach(retired => {
    check(!content.includes(retired), `${file} references retired runtime/helper: ${retired}`);
  });
  if (content.includes('<footer')) {
    check(content.includes('assets/site-footer.js'), `${file} has a footer but does not load site-footer.js`);
  }
});

const footer = exists('assets/site-footer.js') ? read('assets/site-footer.js') : '';
check(footer.includes('guide.html'), 'site-footer.js does not include Guide footer link');
check(footer.includes('sources.html'), 'site-footer.js does not include Sources footer link');
check(footer.includes('normalizeNav'), 'site-footer.js does not normalize header nav');
check(footer.includes('guide.html') && footer.includes('sources.html'), 'site-footer.js missing footer-only Guide/Sources support');

const core = exists('assets/atlas-core-v2.js') ? read('assets/atlas-core-v2.js') : '';
check(core.includes('function loadBranchManifest'), 'atlas-core-v2.js does not load branch-research-manifest.js');
check(core.includes('BRANCH_RESEARCH_MANIFEST'), 'atlas-core-v2.js does not reference BRANCH_RESEARCH_MANIFEST');
check(core.includes('function renderSources'), 'atlas-core-v2.js is missing the Sources page renderer');
check(core.includes('function branchCard'), 'atlas-core-v2.js is missing branch card rendering');
check(core.includes('function sortOpportunities'), 'atlas-core-v2.js is missing core opportunity date sorting');
// IATSE guidance moved from per-card "research use" text to the tabbed join flow:
// card CTA + per-local modal join steps. Validate the current guidance markers.
check(core.includes('How to join / get work'), 'atlas-core-v2.js is missing the IATSE card join CTA');
check(core.includes('How to join or get work with this local'), 'atlas-core-v2.js is missing the IATSE per-local join guidance');
check(core.includes('not affiliated with or endorsed by IATSE'), 'atlas-core-v2.js is missing the IATSE independence disclaimer');
check(core.includes('guide-home-callout'), 'atlas-core-v2.js is missing the home Guide callout');
check(!core.includes('function chip('), 'atlas-core-v2.js still contains public badge/chip rendering helper');
check(!core.includes('Verify directly before outreach.</p></article>'), 'IATSE cards still contain repeated generic verify-before-outreach line');

const approx = exists('assets/approx-date-labels.js') ? read('assets/approx-date-labels.js') : '';
check(approx.includes('Approx. date window'), 'approx-date-labels.js does not label cards as approximate date windows');
check(approx.includes('Approx. planning window'), 'approx-date-labels.js does not label modals as approximate planning windows');
check(approx.includes('verify before planning'), 'approx-date-labels.js does not add verification language');

const rollover = exists('data/packages/opportunity-rollover-2027.js') ? read('data/packages/opportunity-rollover-2027.js') : '';
check(rollover.includes("rolloverModel = 'separate_year_records'"), 'opportunity-rollover-2027.js does not declare separate_year_records model');
check(rollover.includes('build2027Record'), 'opportunity-rollover-2027.js does not build separate 2027 records');
check(rollover.includes('archiveSourceRecord'), 'opportunity-rollover-2027.js does not archive source 2026 records');

const taxonomy = exists('data/packages/opportunity-taxonomy.js') ? read('data/packages/opportunity-taxonomy.js') : '';
check(taxonomy.includes('PRODUCTION_ATLAS_OPPORTUNITY_TAXONOMY'), 'opportunity-taxonomy.js does not export PRODUCTION_ATLAS_OPPORTUNITY_TAXONOMY');
check(taxonomy.includes('applyOpportunityTaxonomy'), 'opportunity-taxonomy.js does not expose active display behavior');

const routeUpdates = exists('data/packages/research-queue-route-updates.js') ? read('data/packages/research-queue-route-updates.js') : '';
check(routeUpdates.includes('PRODUCTION_ATLAS_ROUTE_RESEARCH_UPDATES'), 'research-queue-route-updates.js does not expose route research updates');
check(routeUpdates.includes('applyRouteResearchUpdates'), 'research-queue-route-updates.js does not expose applyRouteResearchUpdates');
check(!/verify IATSE jurisdiction/i.test(routeUpdates), 'route research updates use non-normalized IATSE jurisdiction wording');
check(!/verify [A-Za-z-]+ IATSE\/local jurisdiction route/i.test(routeUpdates), 'route research updates use non-normalized IATSE/local wording');
check(routeUpdates.includes('verify applicable IATSE/local jurisdiction'), 'route research updates missing preferred IATSE/local jurisdiction wording');

const css = exists('assets/atlas.css') ? read('assets/atlas.css') : '';
check(!/\.chip\b/.test(css), 'assets/atlas.css still contains chip badge styles');
check(!/\.chips\b/.test(css), 'assets/atlas.css still contains chip container styles');

const readme = exists('README.md') ? read('README.md') : '';
check(readme.includes('Source-of-truth rule'), 'README.md missing source-of-truth rule');
