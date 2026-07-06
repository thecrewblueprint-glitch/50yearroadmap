let roadmapData = {};

async function loadRoadmap() {
    try {
        const response = await fetch('roadmap.json');
        roadmapData = await response.json();
        renderDashboard();
    } catch (e) {
        console.error("Failed to load roadmap.json", e);
        document.body.innerHTML = "<h1>Error loading roadmap.json</h1>";
    }
}

function renderDashboard() {
    renderMetrics();
    renderPillars();
    renderFrontier();
    renderLaterQueue();
    renderCompleted();
}

function renderMetrics() {
    const counts = {
        active: roadmapData.projects.filter(p => p.status === 'active').length,
        completed: roadmapData.tasks.filter(t => t.status === 'completed').length,
        movedLater: roadmapData.movedLater.length
    };
    document.querySelector('.metrics').innerHTML = `
        <span>Active Projects: ${counts.active}</span> | 
        <span>Completed Tasks: ${counts.completed}</span> | 
        <span>Moved Later: ${counts.movedLater}</span>
    `;
}

function renderPillars() {
    const grid = document.getElementById('pillars-grid');
    grid.innerHTML = '';
    roadmapData.pillars.forEach(pillar => {
        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `
            <h3>${pillar.title}</h3>
            <p>${pillar.purpose}</p>
            <div class="meta">Status: ${pillar.status} | Priority: ${pillar.priority}</div>
        `;
        grid.appendChild(card);
    });
}

function renderFrontier() {
    // Simple logic: Find first active item in primary track
    const frontier = roadmapData.tasks.find(t => t.status === 'active' && t.progression_track === 'primary_path') || 
                     roadmapData.projects.find(p => p.status === 'active');
    
    const container = document.getElementById('frontier-container');
    if (frontier) {
        container.innerHTML = `
            <div class="card" style="border-color: var(--accent)">
                <span class="frontier-badge">YOU ARE NOW HERE</span>
                <h3>${frontier.title}</h3>
                <p>${frontier.summary || frontier.purpose}</p>
            </div>
        `;
    }
}

function renderLaterQueue() {
    const list = document.getElementById('later-list');
    list.innerHTML = roadmapData.movedLater.map(item => `
        <div class="card">
            <h4>${item.title}</h4>
            <p class="meta">Moved: ${item.moved_later_date}</p>
        </div>
    `).join('');
}

function renderCompleted() {
    const list = document.getElementById('completed-list');
    list.innerHTML = roadmapData.tasks.filter(t => t.status === 'completed').map(t => `
        <div class="card" style="opacity: 0.7">
            <h4>${t.title}</h4>
            <p class="meta">Completed</p>
        </div>
    `).join('');
}

document.getElementById('jump-to-now').addEventListener('click', () => {
    document.getElementById('frontier-container').scrollIntoView({ behavior: 'smooth' });
});

loadRoadmap();
