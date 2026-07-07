let roadmapData = {};

async function loadRoadmap() {
    try {
        const response = await fetch('roadmap.json', { cache: 'no-store' });
        roadmapData = await response.json();
        renderDashboard();
    } catch (error) {
        console.error('Failed to load roadmap.json', error);
        document.body.innerHTML = '<main class="error"><h1>Error loading roadmap.json</h1><p>Check that docs/roadmap.json exists and is valid JSON.</p></main>';
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

function renderDashboard() {
    renderMetrics();
    renderFrontier();
    renderDecisionContext();
    renderPillars();
    renderBlockedItems();
    renderLaterQueue();
    renderCompleted();
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
        container.innerHTML = '<div class="card"><h3>No frontier calculated</h3><p class="meta">Run the watcher/build process.</p></div>';
        return;
    }

    container.innerHTML = `
        <div class="card frontier-card">
            <span class="frontier-badge">YOU ARE NOW HERE</span>
            <h3>${escapeHtml(frontier.pillar_title)}</h3>
            <p>${escapeHtml(frontier.reasoning)}</p>
            <div class="meta">
                Priority: ${escapeHtml(frontier.priority)} · Active work: ${escapeHtml(frontier.active_work)} · Blockers: ${escapeHtml(frontier.blockers)}
            </div>
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
            <div class="meta">Index: ${escapeHtml(context.index)} · Source: ${escapeHtml(context.source_directory)}</div>
        </div>
    `;
}

function renderPillars() {
    const grid = document.getElementById('pillars-grid');
    const pillars = normalizeList(roadmapData.pillars);

    grid.innerHTML = pillars.map((pillar) => {
        const activeProjects = normalizeList(pillar.active_projects);
        return `
            <article class="card pillar-card">
                <h3>${escapeHtml(pillar.title)}</h3>
                <div class="meta">${escapeHtml(pillar.id)} · ${escapeHtml(pillar.status)} · ${escapeHtml(pillar.priority)}</div>
                <p>${activeProjects.length} active project${activeProjects.length === 1 ? '' : 's'}</p>
                <ul>
                    ${activeProjects.slice(0, 8).map(project => `<li>${escapeHtml(project)}</li>`).join('')}
                </ul>
                ${activeProjects.length > 8 ? `<p class="meta">+ ${activeProjects.length - 8} more</p>` : ''}
            </article>
        `;
    }).join('');
}

function renderBlockedItems() {
    const list = document.getElementById('blocked-list');
    if (!list) return;

    const blockers = normalizeList(roadmapData.blocked_items);
    list.innerHTML = blockers.map((item) => `
        <article class="card blocker-card">
            <h4>${escapeHtml(item)}</h4>
            <p class="meta">Blocked · needs decision, scheduling, or move-later handling</p>
        </article>
    `).join('');
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

document.getElementById('jump-to-now').addEventListener('click', () => {
    document.getElementById('frontier-section').scrollIntoView({ behavior: 'smooth' });
});

loadRoadmap();
