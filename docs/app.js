let roadmapData = {};
let activeFilter = 'all';
let searchQuery = '';
let controlsBound = false;
let activeTimeframe = 'now';

const TIMEFRAMES = [
    { id: 'now', label: 'Now', horizon: 'Immediate', focus: 'Resolve the current frontier and avoid project sprawl.', decisions: 'Work only on items that reduce blockers, clarify direction, or protect the primary path.' },
    { id: '1y', label: '1Y', horizon: 'Foundation', focus: 'Stabilize the operating base: business admin, active software, content systems, and evidence workflows.', decisions: 'Choose concrete, low-drift work that can be finished or validated within the year.' },
    { id: '5y', label: '5Y', horizon: 'Working System', focus: 'Turn the core projects into reliable systems that can operate without constant rebuilding.', decisions: 'Prioritize repeatable processes, cleaner data pipelines, stronger public-safe boundaries, and stable toolchains.' },
    { id: '10y', label: '10Y', horizon: 'Scaled Platform', focus: 'Convert the ecosystem into a mature platform for production work, education, labor coordination, and support infrastructure.', decisions: 'Invest in durable architecture, governance, and role separation.' },
    { id: '20y', label: '20Y', horizon: 'Physical Bridge', focus: 'Translate digital and business systems into physical-world infrastructure and early land/community capacity.', decisions: 'Use deep-context principles to shape property, stewardship, and community standards.' },
    { id: '30y', label: '30Y', horizon: 'Network Formation', focus: 'Connect separate projects into a functioning network of labor, education, resources, and rest infrastructure.', decisions: 'Favor long-term resilience, succession, documentation, and cultural continuity.' },
    { id: '40y', label: '40Y', horizon: 'Legacy Stewardship', focus: 'Prepare the system to outlast direct day-to-day involvement by the founder.', decisions: 'Prioritize steward training, legal continuity, durable archives, and mission fidelity.' },
    { id: '50y', label: '50Y', horizon: 'Full Vision', focus: 'A complete life-architecture: independent work, land, learning, community care, and preserved roadmap DNA.', decisions: 'Protect the deepest mission while keeping the public systems practical and safe.' }
];

async function loadRoadmap() {
    try {
        const paths = ['roadmap.json', 'docs/roadmap.json'];
        let response;
        for (const path of paths) {
            try {
                response = await fetch(path, { cache: 'no-store' });
                if (response.ok) break;
            } catch (error) {}
        }
        if (!response || !response.ok) throw new Error('Could not load roadmap.json from any path');
        roadmapData = await response.json();
        ensureInteractiveShell();
        renderDashboard();
        bindControls();
    } catch (error) {
        console.error('Failed to load roadmap dashboard', error);
        document.body.innerHTML = '<main class="error"><h1>Error loading roadmap dashboard</h1><p>The roadmap data or dashboard shell failed to load.</p><p class="meta">Debug: ' + escapeHtml(error.message) + '</p></main>';
    }
}

function escapeHtml(value) {
    return String(value ?? '').replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;').replaceAll("'", '&#039;');
}

function normalizeList(value) { return Array.isArray(value) ? value : []; }
function normalizeSearch(value) { return String(value || '').toLowerCase(); }
function textMatches(...values) { return !searchQuery || values.some(value => normalizeSearch(value).includes(searchQuery)); }
function getById(id) { return document.getElementById(id); }
function addListener(id, eventName, handler) { const el = getById(id); if (el) el.addEventListener(eventName, handler); }
function timeframe() { return TIMEFRAMES.find(item => item.id === activeTimeframe) || TIMEFRAMES[0]; }

function ensureInteractiveShell() {
    const header = document.querySelector('header');
    const main = document.querySelector('main');
    if (header && !getById('collapse-all')) {
        const actions = document.createElement('div');
        actions.className = 'header-actions';
        actions.innerHTML = '<button id="collapse-all" class="secondary-button">Collapse All</button><button id="expand-critical" class="secondary-button">Expand Critical</button>';
        const jump = getById('jump-to-now');
        if (jump && jump.parentElement) { jump.parentElement.classList.add('header-actions'); jump.parentElement.append(...actions.children); }
        else header.appendChild(actions);
    }
    if (main && !getById('timeframe-section')) {
        const section = document.createElement('section');
        section.id = 'timeframe-section';
        section.innerHTML = '<h2>Milestone Lens</h2><p class="section-intro">Zoom the same roadmap between immediate work and the 50-year vision.</p><div id="timeframe-nav" class="timeframe-nav"></div><div id="timeframe-lens"></div>';
        main.insertBefore(section, main.firstChild);
    }
    if (main && !getById('controls-section')) {
        const controls = document.createElement('section');
        controls.id = 'controls-section';
        controls.className = 'toolbar';
        controls.innerHTML = '<label for="roadmap-search">Search roadmap</label><input id="roadmap-search" type="search" placeholder="Search pillars, blockers, completed items..."><label for="status-filter">View</label><select id="status-filter"><option value="all">All</option><option value="active">Active pillars</option><option value="blocked">Blockers</option><option value="moved_later">Moved later</option><option value="completed">Completed</option></select>';
        const pillarsSection = getById('pillars-section');
        main.insertBefore(controls, pillarsSection || main.firstChild);
    }
    [['decision-context-section','Decision Context','decision-context-container'],['blocked-section','Blockers','blocked-list'],['later-section','Moved Later','later-list'],['completed-section','Completed','completed-list']].forEach(([sectionId,title,containerId]) => {
        if (main && !getById(sectionId)) {
            const section = document.createElement('section');
            section.id = sectionId;
            section.innerHTML = `<h2>${title}</h2><div id="${containerId}" class="grid"></div>`;
            main.appendChild(section);
        }
    });
    if (!getById('detail-panel')) {
        const panel = document.createElement('aside');
        panel.id = 'detail-panel';
        panel.className = 'detail-panel';
        panel.setAttribute('aria-hidden','true');
        panel.innerHTML = '<div class="detail-panel-inner"><button id="close-detail" class="close-button" aria-label="Close detail panel">×</button><div id="detail-content"></div></div>';
        document.body.appendChild(panel);
    }
}

function renderDashboard() {
    renderMetrics();
    renderTimeframeLens();
    renderFrontier();
    renderDecisionContext();
    renderPillars();
    renderBlockedItems();
    renderLaterQueue();
    renderCompleted();
}

function bindControls() {
    if (controlsBound) return;
    controlsBound = true;
    addListener('roadmap-search','input', e => { searchQuery = e.target.value.trim().toLowerCase(); renderDashboard(); });
    addListener('status-filter','change', e => { activeFilter = e.target.value; renderDashboard(); });
    addListener('collapse-all','click', () => { document.querySelectorAll('details').forEach(d => d.open = false); closeDetailPanel(); });
    addListener('expand-critical','click', () => { document.querySelectorAll('details[data-priority="critical"], details[data-status="blocked"]').forEach(d => d.open = true); });
    addListener('close-detail','click', closeDetailPanel);
    const panel = getById('detail-panel');
    if (panel) panel.addEventListener('click', e => { if (e.target === panel) closeDetailPanel(); });
    addListener('jump-to-now','click', () => { activeTimeframe = 'now'; renderDashboard(); const frontier = getById('frontier-section'); if (frontier) frontier.scrollIntoView({ behavior:'smooth' }); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape') closeDetailPanel(); });
}

function renderMetrics() {
    const metrics = document.querySelector('.metrics');
    if (!metrics) return;
    const s = roadmapData.summary || {};
    metrics.innerHTML = `<button class="metric-pill" data-filter="all">Projects: ${s.project_count ?? 0}</button><button class="metric-pill" data-filter="all">Task Records: ${s.task_count ?? 0}</button><button class="metric-pill" data-filter="blocked">Blockers: ${s.blocked_count ?? 0}</button><button class="metric-pill" data-filter="completed">Completed: ${s.completed_count ?? 0}</button><button class="metric-pill" data-filter="moved_later">Moved Later: ${s.moved_later_count ?? 0}</button><button class="metric-pill active-lens">Lens: ${escapeHtml(timeframe().label)}</button>`;
    metrics.querySelectorAll('.metric-pill[data-filter]').forEach(button => button.addEventListener('click', () => { activeFilter = button.dataset.filter; const filter = getById('status-filter'); if (filter) filter.value = activeFilter; renderDashboard(); }));
}

function renderTimeframeLens() {
    const nav = getById('timeframe-nav');
    const lens = getById('timeframe-lens');
    if (!nav || !lens) return;
    const tf = timeframe();
    const frontier = roadmapData.frontier || {};
    nav.innerHTML = TIMEFRAMES.map(item => `<button class="timeframe-button ${item.id === activeTimeframe ? 'active' : ''}" data-timeframe="${item.id}"><span>${item.label}</span><small>${item.horizon}</small></button>`).join('');
    nav.querySelectorAll('.timeframe-button').forEach(button => button.addEventListener('click', () => { activeTimeframe = button.dataset.timeframe; renderDashboard(); }));
    lens.innerHTML = `
        <article class="card lens-card">
            <div class="lens-heading"><span class="frontier-badge">${escapeHtml(tf.label)} LENS</span><h3>${escapeHtml(tf.horizon)}</h3></div>
            <p>${escapeHtml(tf.focus)}</p>
            <details open><summary>How this translates the vision</summary><p>${escapeHtml(timeframeTranslation())}</p></details>
            <details><summary>Decision rule at this zoom level</summary><p>${escapeHtml(tf.decisions)}</p></details>
            <details><summary>Current anchor</summary><p>${escapeHtml(frontier.pillar_title || 'No frontier calculated')} — ${escapeHtml(frontier.reasoning || 'Run the watcher/build process.')}</p></details>
        </article>
    `;
}

function timeframeTranslation() {
    const id = activeTimeframe;
    if (id === 'now') return 'The 50-year vision is reduced to today’s control point: reduce blockers, preserve the primary path, and avoid splitting attention into unfinished side systems.';
    if (id === '1y') return 'The vision becomes operating stability: the roadmap, memory pipeline, Production Atlas, Deadhang admin, and Crew Blueprint content boundaries need to become usable instead of theoretical.';
    if (id === '5y') return 'The vision becomes an integrated working stack: public-safe data, education content, contractor operations, and reusable tooling should support one another without constant rebuilds.';
    if (id === '10y') return 'The vision becomes platform maturity: the projects should have durable architecture, defined audiences, safer data boundaries, and clearer roles.';
    if (id === '20y') return 'The vision begins crossing into physical infrastructure: Homes for Hands and land/community ideas should be translated from meaning into practical rules, property requirements, and stewardship models.';
    if (id === '30y') return 'The vision becomes network behavior: the separate parts should function as an ecosystem for work, training, resources, rest, and continuity.';
    if (id === '40y') return 'The vision becomes legacy design: systems, culture, archives, and stewardship should be strong enough to survive leadership transition.';
    return 'The full vision is visible: Deadhang, Crew Blueprint, Production Atlas, tools, land, Homes for Hands, skills, and personal operations resolve into one long-term life architecture.';
}

function renderFrontier() {
    const frontier = roadmapData.frontier;
    const container = getById('frontier-container');
    if (!container) return;
    if (!frontier) { container.innerHTML = '<div class="card"><h3>No frontier calculated</h3><p class="meta">Run the watcher/build process.</p></div>'; return; }
    container.innerHTML = `<article class="card frontier-card clickable" data-kind="frontier" tabindex="0"><span class="frontier-badge">YOU ARE NOW HERE</span><h3>${escapeHtml(frontier.pillar_title)}</h3><p>${escapeHtml(frontier.reasoning)}</p><div class="meta">Priority: ${escapeHtml(frontier.priority)} · Active work: ${escapeHtml(frontier.active_work)} · Blockers: ${escapeHtml(frontier.blockers)} · Lens: ${escapeHtml(timeframe().label)}</div><p class="card-hint">Click for detailed next steps.</p></article>`;
    const card = container.querySelector('[data-kind="frontier"]');
    if (card) card.addEventListener('click', () => openDetailPanel('frontier', frontier));
}

function renderDecisionContext() {
    const context = roadmapData.decision_context;
    const container = getById('decision-context-container');
    if (!container) return;
    if (!context || (activeFilter !== 'all' && activeFilter !== 'active') || !textMatches(context.policy, context.index, context.source_directory)) { container.innerHTML = ''; return; }
    container.innerHTML = `<details class="card context-card" open data-priority="critical"><summary><span>Deep-Context Decision Policy</span><span class="summary-meta">required before direction changes</span></summary><p>${escapeHtml(context.policy)}</p><div class="meta">Index: ${escapeHtml(context.index)} · Source: ${escapeHtml(context.source_directory)}</div></details>`;
}

function renderPillars() {
    const grid = getById('pillars-grid');
    if (!grid) return;
    const pillars = normalizeList(roadmapData.pillars).filter(p => activeFilter === 'all' || activeFilter === 'active').filter(p => textMatches(p.title, p.id, p.status, p.priority, normalizeList(p.active_projects).join(' ')));
    grid.innerHTML = pillars.map(pillar => {
        const projects = normalizeList(pillar.active_projects);
        return `<details class="card pillar-card" data-priority="${escapeHtml(pillar.priority)}" data-status="${escapeHtml(pillar.status)}"><summary><span>${escapeHtml(pillar.title)}</span><span class="summary-meta">${escapeHtml(pillar.status)} · ${projects.length} projects</span></summary><div class="meta">${escapeHtml(pillar.id)} · Priority: ${escapeHtml(pillar.priority)} · Lens: ${escapeHtml(timeframe().label)}</div><p>${escapeHtml(pillarTranslation(pillar))}</p><div class="project-list">${projects.map((project,index) => `<button class="inline-task clickable" data-pillar="${escapeHtml(pillar.id)}" data-title="${escapeHtml(project)}" data-index="${index}"><span>${escapeHtml(project)}</span><small>Open steps</small></button>`).join('') || '<p class="meta">No active projects currently assigned.</p>'}</div><button class="open-panel" data-detail="pillar" data-pillar-id="${escapeHtml(pillar.id)}">Open pillar detail</button></details>`;
    }).join('');
    grid.querySelectorAll('.inline-task').forEach(button => button.addEventListener('click', e => { e.preventDefault(); const pillar = normalizeList(roadmapData.pillars).find(item => item.id === button.dataset.pillar); openDetailPanel('project', { title: button.dataset.title, pillar, index: Number(button.dataset.index || 0) }); }));
    grid.querySelectorAll('.open-panel').forEach(button => button.addEventListener('click', e => { e.preventDefault(); const pillar = normalizeList(roadmapData.pillars).find(item => item.id === button.dataset.pillarId); openDetailPanel('pillar', pillar); }));
}

function pillarTranslation(pillar) {
    const title = String(pillar?.title || '').toLowerCase();
    const tf = activeTimeframe;
    if (tf === 'now') return title.includes('homes') || title.includes('homestead') ? 'Keep this as tracked context unless it affects a current decision.' : 'Only do work here if it reduces the current blocker load or supports the frontier.';
    if (tf === '1y') return 'Define the minimum stable version that can exist within one year.';
    if (tf === '5y') return 'Convert repeated work into a system, workflow, or reusable operating habit.';
    if (tf === '10y') return 'Build toward a mature platform with clear roles, standards, and boundaries.';
    if (tf === '20y') return title.includes('homes') || title.includes('land') || title.includes('homestead') ? 'Begin translating the physical-world version into property, governance, and stewardship requirements.' : 'Support the larger physical-world transition by becoming stable infrastructure.';
    if (tf === '30y') return 'Function as one node in a broader network rather than a standalone project.';
    if (tf === '40y') return 'Prepare this pillar to be stewarded by others without losing its purpose.';
    return 'Show how this pillar contributes to the completed 50-year life architecture.';
}

function renderBlockedItems() {
    const list = getById('blocked-list'); if (!list) return;
    const blockers = normalizeList(roadmapData.blocked_items).filter(i => activeFilter === 'all' || activeFilter === 'blocked').filter(i => textMatches(i));
    list.innerHTML = blockers.map((item,index) => `<details class="card blocker-card" data-status="blocked"><summary><span>${escapeHtml(item)}</span><span class="summary-meta">blocked · ${escapeHtml(timeframe().label)}</span></summary><ol class="step-list">${stepsFor('blocked', item).map(step => `<li>${escapeHtml(step)}</li>`).join('')}</ol><button class="open-panel" data-index="${index}">Open full blocker plan</button></details>`).join('');
    list.querySelectorAll('.open-panel').forEach(button => button.addEventListener('click', e => { e.preventDefault(); openDetailPanel('blocked', blockers[Number(button.dataset.index)]); }));
}

function renderLaterQueue() {
    const list = getById('later-list'); if (!list) return;
    const items = normalizeList(roadmapData.moved_later_items).filter(i => activeFilter === 'all' || activeFilter === 'moved_later').filter(i => textMatches(i));
    list.innerHTML = items.map((item,index) => `<details class="card moved-card" data-status="moved_later"><summary><span>${escapeHtml(item)}</span><span class="summary-meta">moved later</span></summary><ol class="step-list">${stepsFor('moved_later', item).map(step => `<li>${escapeHtml(step)}</li>`).join('')}</ol><button class="open-panel" data-index="${index}">Open saved-later detail</button></details>`).join('');
    list.querySelectorAll('.open-panel').forEach(button => button.addEventListener('click', e => { e.preventDefault(); openDetailPanel('moved_later', items[Number(button.dataset.index)]); }));
}

function renderCompleted() {
    const list = getById('completed-list'); if (!list) return;
    const items = normalizeList(roadmapData.completed_items).filter(i => activeFilter === 'all' || activeFilter === 'completed').filter(i => textMatches(i));
    list.innerHTML = items.map((item,index) => `<details class="card completed-card" data-status="completed"><summary><span>${escapeHtml(item)}</span><span class="summary-meta">completed</span></summary><ol class="step-list">${stepsFor('completed', item).map(step => `<li>${escapeHtml(step)}</li>`).join('')}</ol><button class="open-panel" data-index="${index}">Open completion record</button></details>`).join('');
    list.querySelectorAll('.open-panel').forEach(button => button.addEventListener('click', e => { e.preventDefault(); openDetailPanel('completed', items[Number(button.dataset.index)]); }));
}

function stepsFor(kind, title) {
    const base = String(title || '').toLowerCase();
    const lens = timeframe().label;
    if (kind === 'frontier') return [`Read the frontier through the ${lens} lens.`, 'Choose the smallest action that protects the primary path.', 'Reduce a blocker before starting new side work.', 'Update the digest or roadmap state after the decision.', 'Rebuild the live roadmap snapshot.'];
    if (kind === 'completed') return ['Keep it visible as proof of progress.', 'Confirm it did not create a new blocker.', 'Use it as evidence in future roadmap review.'];
    if (kind === 'moved_later') return ['Preserve the idea without activating it.', 'Define what milestone lens would make it relevant again.', 'Review after current frontier pressure drops.'];
    if (base.includes('source') || base.includes('verification') || base.includes('public')) return ['Identify the unsupported claim.', 'Find or mark a public source.', 'Label unknown fields honestly.', 'Update the evidence boundary.', 'Rebuild the roadmap.'];
    if (base.includes('homes for hands') || base.includes('homestead') || base.includes('values')) return ['Consult deep-context decision sources.', 'Separate public-safe operations from private meaning.', 'Define the minimum practical rule needed at this timeframe.', 'Store deeper philosophy in roadmap-deep-context.', 'Extract only actionable claims into digests.'];
    if (base.includes('crew blueprint') || base.includes('curriculum') || base.includes('lms')) return ['Classify as content, platform, safety, or scope.', 'Protect the technical education boundary.', 'Choose the smallest next structure decision.', 'Do not rebuild the LMS until content-first is stable.', 'Update the roadmap after resolving or deferring.'];
    if (base.includes('deadhang') || base.includes('invoice') || base.includes('admin')) return ['Identify the business/admin decision.', 'Separate urgent risk from tooling expansion.', 'Document the decision in a digest or task record.', 'Move non-critical expansion later if needed.', 'Check tax, client, insurance, or operating risk.'];
    return ['Clarify what decision or evidence is missing.', 'Check the relevant digest, deep-context file, or source archive.', 'Resolve, schedule, or move later.', 'Record the outcome.', 'Rebuild the live roadmap snapshot.'];
}

function openDetailPanel(kind, payload) {
    const panel = getById('detail-panel'); const content = getById('detail-content'); if (!panel || !content) return;
    const safe = payload || {}; const title = safe.title || safe.pillar_title || String(payload || 'Roadmap Item');
    if (kind === 'pillar') {
        const projects = normalizeList(safe.active_projects);
        content.innerHTML = `<p class="eyebrow">Pillar Detail · ${escapeHtml(timeframe().label)} Lens</p><h2>${escapeHtml(safe.title || 'Pillar')}</h2><p>${escapeHtml(pillarTranslation(safe))}</p><p class="meta">${escapeHtml(safe.id || 'pillar')} · ${escapeHtml(safe.status || 'unknown')} · ${escapeHtml(safe.priority || 'unknown')}</p><details open><summary>Active projects</summary><ul>${projects.map(project => `<li>${escapeHtml(project)}</li>`).join('') || '<li>No active projects assigned.</li>'}</ul></details><details open><summary>Milestone steps</summary><ol class="step-list">${stepsFor('pillar', safe.title).map(step => `<li>${escapeHtml(step)}</li>`).join('')}</ol></details>`;
    } else if (kind === 'project') {
        content.innerHTML = detailTemplate('Project · ' + timeframe().label + ' Lens', title, `${safe.pillar?.id || 'unknown pillar'} · ${safe.pillar?.title || ''}`, stepsFor('project', title));
    } else if (kind === 'frontier') {
        content.innerHTML = detailTemplate('Current Frontier · ' + timeframe().label + ' Lens', safe.pillar_title || 'Current Frontier', `${safe.priority || 'unknown'} priority · ${safe.active_work ?? 0} active · ${safe.blockers ?? 0} blockers`, stepsFor('frontier', safe.pillar_title), safe.reasoning);
    } else {
        content.innerHTML = detailTemplate(kind.replace('_',' ') + ' · ' + timeframe().label + ' Lens', title, 'Generated from current roadmap snapshot', stepsFor(kind, title));
    }
    panel.classList.add('open'); panel.setAttribute('aria-hidden','false');
}

function detailTemplate(label, title, meta, steps, description = '') {
    return `<p class="eyebrow">${escapeHtml(label)}</p><h2>${escapeHtml(title)}</h2>${description ? `<p>${escapeHtml(description)}</p>` : ''}<p class="meta">${escapeHtml(meta)}</p><details open><summary>Step-by-step plan</summary><ol class="step-list">${steps.map(step => `<li>${escapeHtml(step)}</li>`).join('')}</ol></details><details><summary>How to use this card</summary><ul><li>Resolve it if it is actionable now.</li><li>Move it later if it competes with the current frontier.</li><li>Convert raw evidence into a curated digest before changing roadmap state.</li></ul></details>`;
}

function closeDetailPanel() { const panel = getById('detail-panel'); if (!panel) return; panel.classList.remove('open'); panel.setAttribute('aria-hidden','true'); }

loadRoadmap();
