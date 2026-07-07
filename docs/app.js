let roadmapData = {};
let activeFilter = 'all';
let searchQuery = '';

async function loadRoadmap() {
    try {
        const paths = ['roadmap.json', 'docs/roadmap.json'];
        let response;

        for (const path of paths) {
            try {
                response = await fetch(path, { cache: 'no-store' });
                if (response.ok) break;
            } catch (error) {
                // Try next path.
            }
        }

        if (!response || !response.ok) {
            throw new Error('Could not load roadmap.json from any path');
        }

        roadmapData = await response.json();
        renderDashboard();
        bindControls();
    } catch (error) {
        console.error('Failed to load roadmap.json', error);
        document.body.innerHTML = '<main class="error"><h1>Error loading roadmap.json</h1><p>Check that docs/roadmap.json exists and is valid JSON.</p><p class="meta">Debug: ' + escapeHtml(error.message) + '</p></main>';
    }
}

function escapeHtml(value) {
    return String(value ?? '')
        .replaceAll('&', '&amp;')
        .replaceAll('<', '&lt;')
        .replaceAll('>', '&gt;')
        .replaceAll('"', '&quot;')
        .replaceAll("'", '&#039;');
}

function normalizeList(value) {
    return Array.isArray(value) ? value : [];
}

function slugify(value) {
    return String(value || 'item').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
}

function normalizeSearch(value) {
    return String(value || '').toLowerCase();
}

function textMatches(...values) {
    if (!searchQuery) return true;
    return values.some(value => normalizeSearch(value).includes(searchQuery));
}

function renderDashboard() {
    renderMetrics();
    renderFrontier();
    renderDecisionContext();
    renderPillars();
    renderBlockedItems();
    renderLaterQueue();
    renderCompleted();
}

function bindControls() {
    const search = document.getElementById('roadmap-search');
    const filter = document.getElementById('status-filter');
    const collapseAll = document.getElementById('collapse-all');
    const expandCritical = document.getElementById('expand-critical');
    const closeDetail = document.getElementById('close-detail');
    const detailPanel = document.getElementById('detail-panel');

    search.addEventListener('input', event => {
        searchQuery = event.target.value.trim().toLowerCase();
        renderDashboard();
    });

    filter.addEventListener('change', event => {
        activeFilter = event.target.value;
        renderDashboard();
    });

    collapseAll.addEventListener('click', () => {
        document.querySelectorAll('details').forEach(detail => detail.open = false);
        closeDetailPanel();
    });

    expandCritical.addEventListener('click', () => {
        document.querySelectorAll('details[data-priority="critical"], details[data-status="blocked"]').forEach(detail => detail.open = true);
    });

    closeDetail.addEventListener('click', closeDetailPanel);
    detailPanel.addEventListener('click', event => {
        if (event.target === detailPanel) closeDetailPanel();
    });

    document.addEventListener('keydown', event => {
        if (event.key === 'Escape') closeDetailPanel();
    });
}

function renderMetrics() {
    const summary = roadmapData.summary || {};
    document.querySelector('.metrics').innerHTML = `
        <button class="metric-pill" data-filter="all">Projects: ${summary.project_count ?? 0}</button>
        <button class="metric-pill" data-filter="all">Task Records: ${summary.task_count ?? 0}</button>
        <button class="metric-pill" data-filter="blocked">Blockers: ${summary.blocked_count ?? 0}</button>
        <button class="metric-pill" data-filter="completed">Completed: ${summary.completed_count ?? 0}</button>
        <button class="metric-pill" data-filter="moved_later">Moved Later: ${summary.moved_later_count ?? 0}</button>
    `;

    document.querySelectorAll('.metric-pill').forEach(button => {
        button.addEventListener('click', () => {
            activeFilter = button.dataset.filter;
            document.getElementById('status-filter').value = activeFilter;
            renderDashboard();
        });
    });
}

function renderFrontier() {
    const frontier = roadmapData.frontier;
    const container = document.getElementById('frontier-container');

    if (!frontier) {
        container.innerHTML = '<div class="card"><h3>No frontier calculated</h3><p class="meta">Run the watcher/build process.</p></div>';
        return;
    }

    container.innerHTML = `
        <article class="card frontier-card clickable" data-kind="frontier" tabindex="0">
            <span class="frontier-badge">YOU ARE NOW HERE</span>
            <h3>${escapeHtml(frontier.pillar_title)}</h3>
            <p>${escapeHtml(frontier.reasoning)}</p>
            <div class="meta">Priority: ${escapeHtml(frontier.priority)} · Active work: ${escapeHtml(frontier.active_work)} · Blockers: ${escapeHtml(frontier.blockers)}</div>
            <p class="card-hint">Click for detailed next steps.</p>
        </article>
    `;

    container.querySelector('[data-kind="frontier"]').addEventListener('click', () => openDetailPanel('frontier', frontier));
}

function renderDecisionContext() {
    const context = roadmapData.decision_context;
    const container = document.getElementById('decision-context-container');
    if (!container) return;

    if (!context || (activeFilter !== 'all' && activeFilter !== 'active')) {
        container.innerHTML = '';
        return;
    }

    if (!textMatches(context.policy, context.index, context.source_directory)) {
        container.innerHTML = '';
        return;
    }

    container.innerHTML = `
        <details class="card context-card" open data-priority="critical">
            <summary>
                <span>Deep-Context Decision Policy</span>
                <span class="summary-meta">required before direction changes</span>
            </summary>
            <p>${escapeHtml(context.policy)}</p>
            <div class="meta">Index: ${escapeHtml(context.index)} · Source: ${escapeHtml(context.source_directory)}</div>
        </details>
    `;
}

function renderPillars() {
    const grid = document.getElementById('pillars-grid');
    const pillars = normalizeList(roadmapData.pillars)
        .filter(pillar => activeFilter === 'all' || activeFilter === 'active')
        .filter(pillar => textMatches(pillar.title, pillar.id, pillar.status, pillar.priority, normalizeList(pillar.active_projects).join(' ')));

    grid.innerHTML = pillars.map((pillar) => {
        const activeProjects = normalizeList(pillar.active_projects);
        const slug = slugify(pillar.id);
        return `
            <details class="card pillar-card" data-priority="${escapeHtml(pillar.priority)}" data-status="${escapeHtml(pillar.status)}">
                <summary>
                    <span>${escapeHtml(pillar.title)}</span>
                    <span class="summary-meta">${escapeHtml(pillar.status)} · ${activeProjects.length} projects</span>
                </summary>
                <div class="meta">${escapeHtml(pillar.id)} · Priority: ${escapeHtml(pillar.priority)}</div>
                <div class="project-list">
                    ${activeProjects.map((project, index) => `
                        <button class="inline-task clickable" data-pillar="${escapeHtml(pillar.id)}" data-title="${escapeHtml(project)}" data-index="${index}">
                            <span>${escapeHtml(project)}</span>
                            <small>Open steps</small>
                        </button>
                    `).join('') || '<p class="meta">No active projects currently assigned.</p>'}
                </div>
                <button class="open-panel" data-detail="pillar" data-pillar-id="${escapeHtml(pillar.id)}">Open pillar detail</button>
            </details>
        `;
    }).join('');

    grid.querySelectorAll('.inline-task').forEach(button => {
        button.addEventListener('click', event => {
            event.preventDefault();
            const pillar = roadmapData.pillars.find(item => item.id === button.dataset.pillar);
            openDetailPanel('project', {
                title: button.dataset.title,
                pillar,
                index: Number(button.dataset.index || 0)
            });
        });
    });

    grid.querySelectorAll('.open-panel').forEach(button => {
        button.addEventListener('click', event => {
            event.preventDefault();
            const pillar = roadmapData.pillars.find(item => item.id === button.dataset.pillarId);
            openDetailPanel('pillar', pillar);
        });
    });
}

function renderBlockedItems() {
    const list = document.getElementById('blocked-list');
    if (!list) return;

    const blockers = normalizeList(roadmapData.blocked_items)
        .filter(item => activeFilter === 'all' || activeFilter === 'blocked')
        .filter(item => textMatches(item));

    list.innerHTML = blockers.map((item, index) => `
        <details class="card blocker-card" data-status="blocked">
            <summary>
                <span>${escapeHtml(item)}</span>
                <span class="summary-meta">blocked</span>
            </summary>
            <ol class="step-list">
                ${stepsFor('blocked', item).map(step => `<li>${escapeHtml(step)}</li>`).join('')}
            </ol>
            <button class="open-panel" data-detail="blocked" data-index="${index}">Open full blocker plan</button>
        </details>
    `).join('');

    list.querySelectorAll('.open-panel').forEach(button => {
        button.addEventListener('click', event => {
            event.preventDefault();
            openDetailPanel('blocked', blockers[Number(button.dataset.index)]);
        });
    });
}

function renderLaterQueue() {
    const list = document.getElementById('later-list');
    const items = normalizeList(roadmapData.moved_later_items)
        .filter(item => activeFilter === 'all' || activeFilter === 'moved_later')
        .filter(item => textMatches(item));

    list.innerHTML = items.map((item, index) => `
        <details class="card moved-card" data-status="moved_later">
            <summary>
                <span>${escapeHtml(item)}</span>
                <span class="summary-meta">moved later</span>
            </summary>
            <ol class="step-list">
                ${stepsFor('moved_later', item).map(step => `<li>${escapeHtml(step)}</li>`).join('')}
            </ol>
            <button class="open-panel" data-detail="moved_later" data-index="${index}">Open saved-later detail</button>
        </details>
    `).join('');

    list.querySelectorAll('.open-panel').forEach(button => {
        button.addEventListener('click', event => {
            event.preventDefault();
            openDetailPanel('moved_later', items[Number(button.dataset.index)]);
        });
    });
}

function renderCompleted() {
    const list = document.getElementById('completed-list');
    const items = normalizeList(roadmapData.completed_items)
        .filter(item => activeFilter === 'all' || activeFilter === 'completed')
        .filter(item => textMatches(item));

    list.innerHTML = items.map((item, index) => `
        <details class="card completed-card" data-status="completed">
            <summary>
                <span>${escapeHtml(item)}</span>
                <span class="summary-meta">completed</span>
            </summary>
            <ol class="step-list">
                ${stepsFor('completed', item).map(step => `<li>${escapeHtml(step)}</li>`).join('')}
            </ol>
            <button class="open-panel" data-detail="completed" data-index="${index}">Open completion record</button>
        </details>
    `).join('');

    list.querySelectorAll('.open-panel').forEach(button => {
        button.addEventListener('click', event => {
            event.preventDefault();
            openDetailPanel('completed', items[Number(button.dataset.index)]);
        });
    });
}

function stepsFor(kind, title) {
    const base = String(title || '').toLowerCase();

    if (kind === 'frontier') {
        return [
            'Review active Production Atlas blockers before starting unrelated work.',
            'Pick the highest-impact blocker that can be resolved with current information.',
            'Move side quests to moved-later instead of letting them compete with the frontier.',
            'Update the digest or roadmap state after a decision is made.',
            'Rebuild the roadmap snapshot so the “You Are Now Here” point remains current.'
        ];
    }

    if (kind === 'completed') {
        return [
            'Keep the completed item visible as proof of progress.',
            'Confirm no follow-up blocker was created by the completed work.',
            'Use the completion as evidence if a future agent questions project history.'
        ];
    }

    if (kind === 'moved_later') {
        return [
            'Preserve the idea without letting it interrupt the active frontier.',
            'Define the trigger that would bring this back into active work.',
            'Review after the current frontier blocker count drops or the project becomes dependency-relevant.'
        ];
    }

    if (base.includes('source') || base.includes('verification') || base.includes('public')) {
        return [
            'Identify the exact field or claim that lacks public evidence.',
            'Find or mark a public source for that field.',
            'If no source exists, label it as unknown or human-verification-needed.',
            'Update the relevant digest or data package with the evidence boundary.',
            'Rebuild the roadmap so the blocker count stays accurate.'
        ];
    }

    if (base.includes('homes for hands') || base.includes('homestead') || base.includes('values')) {
        return [
            'Consult the deep-context decision index before changing direction.',
            'Separate public-safe operating policy from private mission meaning.',
            'Define the minimum practical rule or decision needed now.',
            'Store deeper philosophy in roadmap-deep-context, not public dashboard copy.',
            'Convert only actionable operating decisions into raw-report digests.'
        ];
    }

    if (base.includes('crew blueprint') || base.includes('curriculum') || base.includes('lms')) {
        return [
            'Confirm whether this is content, platform, safety, or scope work.',
            'Protect the technical education boundary from roadmap philosophy drift.',
            'Identify the smallest next content or structure decision.',
            'Avoid rebuilding the LMS until the content-first layer is stable.',
            'Update the roadmap after the blocker is resolved, deferred, or split.'
        ];
    }

    if (base.includes('deadhang') || base.includes('invoice') || base.includes('admin')) {
        return [
            'Identify the business/admin decision required.',
            'Separate urgent compliance or money movement from nice-to-have tooling.',
            'Document the decision in a digest or roadmap task record.',
            'Move non-critical tool expansion later if it competes with the current frontier.',
            'Recheck whether the item affects tax, client, insurance, or operating risk.'
        ];
    }

    return [
        'Clarify what decision or evidence is missing.',
        'Check the relevant digest, deep-context file, or source archive.',
        'Choose one of three outcomes: resolve, schedule, or move later.',
        'Record the outcome in the roadmap data layer.',
        'Rebuild the live roadmap snapshot.'
    ];
}

function openDetailPanel(kind, payload) {
    const panel = document.getElementById('detail-panel');
    const content = document.getElementById('detail-content');
    const title = payload?.title || payload?.pillar_title || payload?.title || String(payload || 'Roadmap Item');
    let meta = '';
    let steps = stepsFor(kind, title);

    if (kind === 'pillar') {
        const projects = normalizeList(payload.active_projects);
        meta = `${payload.id} · ${payload.status} · ${payload.priority}`;
        content.innerHTML = `
            <p class="eyebrow">Pillar Detail</p>
            <h2>${escapeHtml(payload.title)}</h2>
            <p class="meta">${escapeHtml(meta)}</p>
            <details open>
                <summary>Active projects</summary>
                <ul>${projects.map(project => `<li>${escapeHtml(project)}</li>`).join('') || '<li>No active projects assigned.</li>'}</ul>
            </details>
            <details open>
                <summary>Recommended next steps</summary>
                <ol class="step-list">${stepsFor('pillar', payload.title).map(step => `<li>${escapeHtml(step)}</li>`).join('')}</ol>
            </details>
        `;
    } else if (kind === 'project') {
        meta = `${payload.pillar?.id || 'unknown pillar'} · ${payload.pillar?.title || ''}`;
        content.innerHTML = detailTemplate('Project', title, meta, stepsFor('project', title));
    } else if (kind === 'frontier') {
        meta = `${payload.priority} priority · ${payload.active_work} active · ${payload.blockers} blockers`;
        content.innerHTML = detailTemplate('Current Frontier', payload.pillar_title, meta, stepsFor('frontier', payload.pillar_title), payload.reasoning);
    } else {
        content.innerHTML = detailTemplate(kind.replace('_', ' '), title, 'Generated from current roadmap snapshot', steps);
    }

    panel.classList.add('open');
    panel.setAttribute('aria-hidden', 'false');
}

function detailTemplate(label, title, meta, steps, description = '') {
    return `
        <p class="eyebrow">${escapeHtml(label)}</p>
        <h2>${escapeHtml(title)}</h2>
        ${description ? `<p>${escapeHtml(description)}</p>` : ''}
        <p class="meta">${escapeHtml(meta)}</p>
        <details open>
            <summary>Step-by-step plan</summary>
            <ol class="step-list">${steps.map(step => `<li>${escapeHtml(step)}</li>`).join('')}</ol>
        </details>
        <details>
            <summary>How to use this card</summary>
            <ul>
                <li>Resolve it if it is actionable now.</li>
                <li>Move it later if it competes with the current frontier.</li>
                <li>Convert raw evidence into a curated digest before changing roadmap state.</li>
            </ul>
        </details>
    `;
}

function closeDetailPanel() {
    const panel = document.getElementById('detail-panel');
    panel.classList.remove('open');
    panel.setAttribute('aria-hidden', 'true');
}

document.getElementById('jump-to-now').addEventListener('click', () => {
    document.getElementById('frontier-section').scrollIntoView({ behavior: 'smooth' });
});

loadRoadmap();
