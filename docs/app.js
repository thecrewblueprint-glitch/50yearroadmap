let roadmapData = {};
let filteredBlockers = [];
let currentFilters = { pillar: 'all', type: 'all', severity: 'all', search: '' };

async function loadRoadmap() {
    try {
        const paths = ['roadmap.json', 'docs/roadmap.json'];
        let response;

        for (const path of paths) {
            try {
                response = await fetch(path, { cache: 'no-store' });
                if (response.ok) break;
            } catch (e) {}
        }

        if (!response || !response.ok) throw new Error('Could not load roadmap.json');
        roadmapData = await response.json();
        renderDashboard();
    } catch (error) {
        console.error('Failed to load roadmap.json', error);
        document.body.innerHTML = '<main class="error"><h1>Error loading roadmap.json</h1><p>Check that docs/roadmap.json exists and is valid JSON.</p></main>';
    }
}

function escapeHtml(value) {
    return String(value ?? '').replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;').replaceAll("'", '&#039;');
}

function normalizeList(value) {
    return Array.isArray(value) ? value : [];
}

function renderDashboard() {
    renderMetrics();
    renderFrontier();
    renderDecisionContext();
    renderPillars();
    renderBlockerControls();
    renderBlockedItems();
    renderLaterQueue();
    renderCompleted();
    setupEventListeners();
}

function renderMetrics() {
    const summary = roadmapData.summary || {};
    document.querySelector('.metrics').innerHTML = `
        <span>Projects: ${summary.project_count ?? 0}</span>
        <span>Task Records: ${summary.task_count ?? 0}</span>
        <span>Blockers: ${summary.blocked_count ?? 0}</span>
        <span>Completed: ${summary.completed_count ?? 0}</span>
        <span>Moved Later: ${summary.moved_later_count ?? 0}</span>
    `;
}

function renderFrontier() {
    const frontier = roadmapData.frontier;
    const container = document.getElementById('frontier-container');

    if (!frontier) {
        container.innerHTML = '<div class="card"><h3>No frontier calculated</h3></div>';
        return;
    }

    container.innerHTML = `
        <div class="card frontier-card">
            <span class="frontier-badge">YOU ARE NOW HERE</span>
            <h3>${escapeHtml(frontier.pillar_title)}</h3>
            <p>${escapeHtml(frontier.reasoning)}</p>
            <div class="meta">Priority: ${escapeHtml(frontier.priority)} · Active: ${escapeHtml(frontier.active_work)} · Blockers: ${escapeHtml(frontier.blockers)}</div>
        </div>
    `;
}

function renderDecisionContext() {
    const context = roadmapData.decision_context;
    const container = document.getElementById('decision-context-container');
    if (!container) return;

    if (!context) {
        container.innerHTML = '<div class="card"><h3>No deep-context policy registered</h3></div>';
        return;
    }

    container.innerHTML = `
        <div class="card context-card">
            <h3>Deep-Context Decision Policy</h3>
            <p>${escapeHtml(context.policy)}</p>
            <div class="meta">Index: ${escapeHtml(context.index)}</div>
        </div>
    `;
}

function renderPillars() {
    const grid = document.getElementById('pillars-grid');
    const pillars = normalizeList(roadmapData.pillars);

    grid.innerHTML = pillars.map((pillar) => {
        const activeProjects = normalizeList(pillar.active_projects);
        return `
            <article class="card pillar-card" data-pillar-id="${pillar.id}">
                <h3>${escapeHtml(pillar.title)}</h3>
                <div class="meta">${escapeHtml(pillar.status)} · ${escapeHtml(pillar.priority)}</div>
                <p><strong>${activeProjects.length} active project${activeProjects.length === 1 ? '' : 's'}</strong></p>
                <ul>
                    ${activeProjects.slice(0, 5).map(p => `<li>${escapeHtml(p)}</li>`).join('')}
                </ul>
                ${activeProjects.length > 5 ? `<p class="meta">+ ${activeProjects.length - 5} more</p>` : ''}
            </article>
        `;
    }).join('');
}

function renderBlockerControls() {
    const blockers = normalizeList(roadmapData.blocked_items);
    const pillars = normalizeList(roadmapData.pillars);

    const pillarOptions = ['<option value="all">All Pillars</option>'] + pillars.map(p => `<option value="${p.id}">${p.title}</option>`).join('');

    const container = document.getElementById('blocker-controls');
    if (!container) return;

    container.innerHTML = `
        <div class="filter-controls">
            <input type="text" id="search-blockers" placeholder="Search blockers..." class="search-input">
            <select id="filter-pillar" class="filter-select">
                ${pillarOptions}
            </select>
            <select id="filter-type" class="filter-select">
                <option value="all">All Types</option>
                <option value="NEEDS_DECISION">Needs Decision</option>
                <option value="BLOCKED_ON">Blocked On</option>
                <option value="RESOURCE_CONSTRAINT">Resource Constraint</option>
            </select>
            <select id="filter-severity" class="filter-select">
                <option value="all">All Severities</option>
                <option value="CRITICAL">🔴 Critical</option>
                <option value="HIGH">🟠 High</option>
                <option value="MEDIUM">🟡 Medium</option>
                <option value="LOW">🟢 Low</option>
            </select>
            <div class="filter-status" id="filter-status"></div>
        </div>
    `;
}

function applyFilters() {
    currentFilters.search = document.getElementById('search-blockers')?.value?.toLowerCase() || '';
    currentFilters.pillar = document.getElementById('filter-pillar')?.value || 'all';
    currentFilters.type = document.getElementById('filter-type')?.value || 'all';
    currentFilters.severity = document.getElementById('filter-severity')?.value || 'all';

    const blockers = normalizeList(roadmapData.blocked_items);

    filteredBlockers = blockers.filter(blocker => {
        const matchSearch = !currentFilters.search || blocker.title.toLowerCase().includes(currentFilters.search);
        const matchPillar = currentFilters.pillar === 'all' || blocker.pillar_id === currentFilters.pillar;
        const matchType = currentFilters.type === 'all' || blocker.type === currentFilters.type;
        const matchSeverity = currentFilters.severity === 'all' || blocker.severity === currentFilters.severity;

        return matchSearch && matchPillar && matchType && matchSeverity;
    });

    // Sort by severity then by date
    const severityOrder = { CRITICAL: 0, HIGH: 1, MEDIUM: 2, LOW: 3 };
    filteredBlockers.sort((a, b) => {
        if (severityOrder[a.severity] !== severityOrder[b.severity]) {
            return severityOrder[a.severity] - severityOrder[b.severity];
        }
        return new Date(a.created_date) - new Date(b.created_date);
    });

    renderBlockedItems();
    updateFilterStatus();
}

function updateFilterStatus() {
    const status = document.getElementById('filter-status');
    if (status) {
        const total = normalizeList(roadmapData.blocked_items).length;
        const shown = filteredBlockers.length;
        status.textContent = `${shown}/${total} blockers`;
        if (shown !== total) status.style.color = '#f5b400';
    }
}

function getSeverityIcon(severity) {
    const icons = { CRITICAL: '🔴', HIGH: '🟠', MEDIUM: '🟡', LOW: '🟢' };
    return icons[severity] || '⚪';
}

function getTypeLabel(type) {
    const labels = {
        NEEDS_DECISION: '⚠️ Decision Needed',
        BLOCKED_ON: '⏸️ Blocked On',
        RESOURCE_CONSTRAINT: '📦 Resource'
    };
    return labels[type] || type;
}

function renderBlockedItems() {
    const list = document.getElementById('blocked-list');
    if (!list) return;

    if (filteredBlockers.length === 0) {
        list.innerHTML = '<div class="card"><p class="meta">No blockers match filters</p></div>';
        return;
    }

    const pillars = normalizeList(roadmapData.pillars);
    const pillarMap = Object.fromEntries(pillars.map(p => [p.id, p.title]));

    list.innerHTML = filteredBlockers.map((blocker) => {
        const createdDate = new Date(blocker.created_date);
        const daysOpen = Math.floor((new Date() - createdDate) / (1000 * 60 * 60 * 24));

        return `
            <article class="card blocker-card" data-blocker-id="${blocker.id}">
                <div class="blocker-header">
                    <h4>${escapeHtml(blocker.title)}</h4>
                    <span class="severity-badge">${getSeverityIcon(blocker.severity)} ${blocker.severity}</span>
                </div>
                <div class="blocker-meta">
                    <span class="badge type-badge">${getTypeLabel(blocker.type)}</span>
                    <span class="badge pillar-badge">${escapeHtml(pillarMap[blocker.pillar_id] || 'Unknown')}</span>
                    <span class="badge age-badge">Open ${daysOpen}d</span>
                </div>
                <p class="resolution">${escapeHtml(blocker.resolution)}</p>
                ${blocker.blocked_by ? `<p class="meta">Blocked by: blocker-${blocker.blocked_by}</p>` : ''}
                ${blocker.gates ? `<p class="meta">Gates: ${blocker.gates.join(', ')}</p>` : ''}
            </article>
        `;
    }).join('');
}

function renderLaterQueue() {
    const list = document.getElementById('later-list');
    const items = normalizeList(roadmapData.moved_later_items);

    list.innerHTML = items.map((item) => `
        <article class="card">
            <h4>${escapeHtml(item)}</h4>
            <p class="meta">Moved later · preserved, not deleted</p>
        </article>
    `).join('');
}

function renderCompleted() {
    const list = document.getElementById('completed-list');
    const items = normalizeList(roadmapData.completed_items);

    list.innerHTML = items.map((item) => `
        <article class="card completed-card">
            <h4>${escapeHtml(item)}</h4>
            <p class="meta">Completed</p>
        </article>
    `).join('');
}

function setupEventListeners() {
    // Blocker filters
    const searchInput = document.getElementById('search-blockers');
    const filterPillar = document.getElementById('filter-pillar');
    const filterType = document.getElementById('filter-type');
    const filterSeverity = document.getElementById('filter-severity');
    const jumpToNow = document.getElementById('jump-to-now');

    if (searchInput) searchInput.addEventListener('input', applyFilters);
    if (filterPillar) filterPillar.addEventListener('change', applyFilters);
    if (filterType) filterType.addEventListener('change', applyFilters);
    if (filterSeverity) filterSeverity.addEventListener('change', applyFilters);

    if (jumpToNow) {
        jumpToNow.addEventListener('click', () => {
            document.getElementById('frontier-section').scrollIntoView({ behavior: 'smooth' });
        });
    }

    // Global search (future implementation - placeholder)
    const roadmapSearch = document.getElementById('roadmap-search');
    if (roadmapSearch) {
        roadmapSearch.addEventListener('input', (e) => {
            // TODO: Implement global search across pillars, projects, blockers
        });
    }

    // Status filter (future implementation - placeholder)
    const statusFilter = document.getElementById('status-filter');
    if (statusFilter) {
        statusFilter.addEventListener('change', (e) => {
            // TODO: Implement status-based filtering
        });
    }

    // Detail panel close button
    const closeDetail = document.getElementById('close-detail');
    if (closeDetail) {
        closeDetail.addEventListener('click', () => {
            const detailPanel = document.getElementById('detail-panel');
            if (detailPanel) {
                detailPanel.classList.remove('open');
                detailPanel.setAttribute('aria-hidden', 'true');
            }
        });
    }

    // Collapse all button (placeholder)
    const collapseAll = document.getElementById('collapse-all');
    if (collapseAll) {
        collapseAll.addEventListener('click', () => {
            // TODO: Collapse all expandable sections
        });
    }

    // Expand critical button (placeholder)
    const expandCritical = document.getElementById('expand-critical');
    if (expandCritical) {
        expandCritical.addEventListener('click', () => {
            // TODO: Expand only CRITICAL severity blockers
        });
    }

    // Initialize filters
    applyFilters();
}

loadRoadmap();
