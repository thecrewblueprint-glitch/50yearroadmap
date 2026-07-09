let roadmapData = {};
let currentView = 'this-week';
let selectedBranch = null;
let branchesCurrentPage = 0;
let branchesItemsPerPage = 3;
let workItemsCurrentPage = 0;
let workItemsItemsPerPage = 3;

async function loadRoadmap() {
    try {
        const response = await fetch('roadmap.json', { cache: 'no-store' });
        if (!response.ok) throw new Error('Could not load roadmap.json');
        roadmapData = await response.json();
        renderDashboard();
    } catch (error) {
        console.error('Failed to load roadmap.json', error);
        document.body.innerHTML = '<main class="error"><h1>Error loading roadmap.json</h1><p>Check that roadmap.json exists and is valid JSON.</p></main>';
    }
}

function renderDashboard() {
    renderUltimateGoal();
    renderPhase();
    renderThisWeek();
    renderBranches();
    renderEcosystem();
    setupEventListeners();
}

function renderUltimateGoal() {
    const goal = document.getElementById('ultimate-goal-text');
    if (goal) {
        goal.textContent = roadmapData.ultimate_goal || '';
    }
}

function renderPhase() {
    document.getElementById('phase-title').textContent = roadmapData.phase || '';
    document.getElementById('phase-description').textContent = roadmapData.phase_description || '';
}

function renderThisWeek() {
    const container = document.getElementById('this-week-tasks');
    const focus = roadmapData.this_week_focus || {};
    const allBranches = roadmapData.branches || [];

    if (!focus.priority_1) {
        container.innerHTML = '<p class="meta">No focus items defined yet</p>';
        return;
    }

    // Parse task IDs from priority_1, priority_2, etc
    const taskIds = [];
    ['priority_1', 'priority_2', 'priority_3'].forEach(key => {
        if (focus[key]) {
            const ids = focus[key].split(',').map(s => s.trim());
            taskIds.push(...ids);
        }
    });

    // Find work items matching these IDs
    const focusItems = [];
    allBranches.forEach(branch => {
        (branch.work_items || []).forEach(item => {
            if (taskIds.includes(item.id)) {
                focusItems.push({ ...item, branch_name: branch.name, branch_id: branch.id });
            }
        });
    });

    setFocusHeading('Your Focus This Week');
    container.innerHTML = focusItems.map(taskCardHTML).join('');
}

// Single source of truth for a task card. Guards missing fields so a work
// item without a priority/branch does not throw.
function taskCardHTML(item) {
    const priority = item.priority || 'MEDIUM';
    return `
        <div class="task-card" role="button" tabindex="0" data-task-id="${item.id}" data-branch-id="${item.branch_id}">
            <div class="task-priority ${priority.toLowerCase()}">${escapeHtml(priority)}</div>
            <div class="task-title">${escapeHtml(item.task)}</div>
            <div class="task-why">${escapeHtml(item.why)}</div>
            <div class="task-branch">→ ${escapeHtml(item.branch_name)}</div>
        </div>
    `;
}

function renderAllWork() {
    const container = document.getElementById('this-week-tasks');
    const allBranches = roadmapData.branches || [];

    // Collect all work items from all branches
    const allItems = [];
    allBranches.forEach(branch => {
        (branch.work_items || []).forEach(item => {
            allItems.push({ ...item, branch_name: branch.name, branch_id: branch.id });
        });
    });

    // Sort by priority: CRITICAL, HIGH, MEDIUM, LOW
    const priorityOrder = { CRITICAL: 0, HIGH: 1, MEDIUM: 2, LOW: 3 };
    allItems.sort((a, b) => (priorityOrder[a.priority] || 99) - (priorityOrder[b.priority] || 99));

    setFocusHeading(`All Work (${allItems.length} items)`);
    container.innerHTML = allItems.map(taskCardHTML).join('');
}

function setFocusHeading(text) {
    const heading = document.getElementById('focus-heading');
    if (heading) heading.textContent = text;
}

function renderBranches() {
    const container = document.getElementById('branches-grid');
    const branches = roadmapData.branches || [];

    // Keep the heading count in sync with the data
    const heading = document.getElementById('branches-heading');
    if (heading) {
        heading.textContent = branches.length === 1
            ? 'The 1 Branch'
            : `The ${branches.length} Branches`;
    }

    // Pagination logic
    const totalPages = Math.ceil(branches.length / branchesItemsPerPage);
    const startIndex = branchesCurrentPage * branchesItemsPerPage;
    const endIndex = startIndex + branchesItemsPerPage;
    const pageItems = branches.slice(startIndex, endIndex);

    container.innerHTML = pageItems.map(branch => `
        <div class="branch-card clickable" role="button" tabindex="0" data-branch-id="${branch.id}">
            <div class="branch-header">
                <div>
                    <h3 class="branch-name">${escapeHtml(branch.name)}</h3>
                    <p class="branch-role">${escapeHtml(branch.role)}</p>
                </div>
                <div class="branch-status">${Number(branch.status_percentage) || 0}%</div>
            </div>

            <div class="progress-bar">
                <div class="progress-fill" style="width: ${Number(branch.status_percentage) || 0}%"></div>
            </div>

            <p style="margin: 12px 0 0 0; font-size: 0.9rem; line-height: 1.5;">
                ${escapeHtml(branch.ultimate_goal)}
            </p>

            ${branch.critical_blocker ? `
                <div class="blocker-badge">
                    🚫 ${escapeHtml(branch.critical_blocker)}
                </div>
            ` : ''}
        </div>
    `).join('');

    // Update pagination UI
    updateBranchesPaginationUI(branchesCurrentPage, totalPages);

    // Add click + keyboard listeners
    document.querySelectorAll('.branch-card.clickable').forEach(card => {
        const open = () => showBranchDetail(card.getAttribute('data-branch-id'));
        card.addEventListener('click', open);
        card.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                open();
            }
        });
    });
}

function showBranchDetail(branchId) {
    const branch = roadmapData.branches.find(b => b.id === branchId);
    if (!branch) return;

    selectedBranch = branchId;
    workItemsCurrentPage = 0;

    // Populate detail section
    document.getElementById('branch-detail-title').textContent = branch.name;
    document.getElementById('branch-goal').textContent = branch.ultimate_goal || '';
    document.getElementById('branch-current').textContent = branch.current_state || '';
    const timeline = branch.timeline || {};
    document.getElementById('branch-timeline').textContent = timeline.phase_1_ready
        ? `${timeline.phase_1_ready}: ${timeline.description || ''}`
        : 'Not scheduled yet';

    // Blockers
    const blockersList = document.getElementById('branch-blockers');
    blockersList.innerHTML = (branch.blockers || []).map(b => `<li>${escapeHtml(b)}</li>`).join('');

    // Work items with pagination
    renderWorkItems(branch);

    // Show detail section
    document.getElementById('branch-detail-section').style.display = 'block';
    document.getElementById('branch-detail-section').scrollIntoView({ behavior: 'smooth' });
}

function renderWorkItems(branch) {
    const workItemsList = document.getElementById('branch-work-items');
    const items = branch.work_items || [];

    // Pagination logic
    const totalPages = Math.ceil(items.length / workItemsItemsPerPage);
    const startIndex = workItemsCurrentPage * workItemsItemsPerPage;
    const endIndex = startIndex + workItemsItemsPerPage;
    const pageItems = items.slice(startIndex, endIndex);

    workItemsList.innerHTML = pageItems.map(item => {
        const status = item.status || 'not_started';
        return `
        <div class="work-item">
            <div class="work-item-info">
                <div class="work-item-title">${escapeHtml(item.task)}</div>
                <div class="work-item-why">${escapeHtml(item.why)}</div>
            </div>
            <div class="work-item-status ${status}">${escapeHtml(status.replace(/_/g, ' '))}</div>
        </div>
    `;
    }).join('');

    // Update pagination UI
    updateWorkItemsPaginationUI(workItemsCurrentPage, totalPages);
}

function renderEcosystem() {
    const container = document.getElementById('ecosystem-flow');
    const flow = roadmapData.ecosystem_flow || {};

    if (!flow.flow || flow.flow.length === 0) {
        container.innerHTML = '<p class="meta">Ecosystem flow not defined</p>';
        return;
    }

    const items = flow.flow || [];
    container.innerHTML = items.map((item, i) => `
        <div class="flow-step">
            <span style="color: var(--accent); font-weight: 700; min-width: 20px;">${i + 1}</span>
            <span style="margin-left: 12px;">${escapeHtml(item)}</span>
            ${i < items.length - 1 ? '<span class="flow-arrow" style="margin-left: auto;">→</span>' : ''}
        </div>
    `).join('');
}

function escapeHtml(value) {
    return String(value ?? '').replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;').replaceAll("'", '&#039;');
}

function updatePaginationUI(prefix, currentPage, totalPages) {
    const container = document.getElementById(`${prefix}-pagination`);
    const prevBtn = document.getElementById(`${prefix}-prev`);
    const nextBtn = document.getElementById(`${prefix}-next`);
    const pageSpan = document.getElementById(`${prefix}-page`);
    const totalSpan = document.getElementById(`${prefix}-total`);

    // Hide the control entirely when everything fits on one page
    if (container) container.style.display = totalPages <= 1 ? 'none' : 'flex';

    if (pageSpan) pageSpan.textContent = currentPage + 1;
    if (totalSpan) totalSpan.textContent = totalPages;

    if (prevBtn) prevBtn.disabled = currentPage === 0;
    if (nextBtn) nextBtn.disabled = currentPage >= totalPages - 1;
}

function updateBranchesPaginationUI(currentPage, totalPages) {
    updatePaginationUI('branches', currentPage, totalPages);
}

function updateWorkItemsPaginationUI(currentPage, totalPages) {
    updatePaginationUI('work-items', currentPage, totalPages);
}

function setupEventListeners() {
    const viewAllButton = document.getElementById('view-all-work');
    const viewThisWeekButton = document.getElementById('view-this-week');
    const closeDetailButton = document.getElementById('close-detail');

    if (viewAllButton) {
        viewAllButton.addEventListener('click', () => {
            currentView = 'all';
            viewAllButton.classList.add('active');
            viewThisWeekButton.classList.remove('active');
            renderAllWork();
        });
    }

    if (viewThisWeekButton) {
        viewThisWeekButton.addEventListener('click', () => {
            currentView = 'this-week';
            viewThisWeekButton.classList.add('active');
            viewAllButton.classList.remove('active');
            renderThisWeek();
        });
    }

    if (closeDetailButton) {
        closeDetailButton.addEventListener('click', () => {
            document.getElementById('branch-detail-section').style.display = 'none';
            selectedBranch = null;
        });
    }

    // Branches pagination
    const branchesPrevBtn = document.getElementById('branches-prev');
    const branchesNextBtn = document.getElementById('branches-next');
    if (branchesPrevBtn) {
        branchesPrevBtn.addEventListener('click', () => {
            if (branchesCurrentPage > 0) {
                branchesCurrentPage--;
                renderBranches();
            }
        });
    }
    if (branchesNextBtn) {
        branchesNextBtn.addEventListener('click', () => {
            const branches = roadmapData.branches || [];
            const totalPages = Math.ceil(branches.length / branchesItemsPerPage);
            if (branchesCurrentPage < totalPages - 1) {
                branchesCurrentPage++;
                renderBranches();
            }
        });
    }

    // Work items pagination
    const workItemsPrevBtn = document.getElementById('work-items-prev');
    const workItemsNextBtn = document.getElementById('work-items-next');
    if (workItemsPrevBtn) {
        workItemsPrevBtn.addEventListener('click', () => {
            if (workItemsCurrentPage > 0) {
                workItemsCurrentPage--;
                const branch = roadmapData.branches.find(b => b.id === selectedBranch);
                if (branch) renderWorkItems(branch);
            }
        });
    }
    if (workItemsNextBtn) {
        workItemsNextBtn.addEventListener('click', () => {
            const branch = roadmapData.branches.find(b => b.id === selectedBranch);
            if (branch) {
                const items = branch.work_items || [];
                const totalPages = Math.ceil(items.length / workItemsItemsPerPage);
                if (workItemsCurrentPage < totalPages - 1) {
                    workItemsCurrentPage++;
                    renderWorkItems(branch);
                }
            }
        });
    }

    // Task card clicks + keyboard — delegated to the container so cards stay
    // interactive after re-renders (view toggles regenerate the cards).
    const tasksContainer = document.getElementById('this-week-tasks');
    if (tasksContainer) {
        const openFromEvent = (e) => {
            const card = e.target.closest('.task-card');
            if (card) showBranchDetail(card.getAttribute('data-branch-id'));
        };
        tasksContainer.addEventListener('click', openFromEvent);
        tasksContainer.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                if (e.target.closest('.task-card')) {
                    e.preventDefault();
                    openFromEvent(e);
                }
            }
        });
    }
}

loadRoadmap();
