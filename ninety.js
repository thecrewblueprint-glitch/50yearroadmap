// Standalone 30 / 60 / 90 operating dashboard renderer.
// This keeps the first pass small: the UI can render immediately while the
// longer-term decision remains whether to promote this structure into
// roadmap.json as part of the formal data model.

const ninetyDayPlan = {
    title: '30 / 60 / 90 Day Operating Dashboard',
    summary: 'A near-term execution layer that keeps the roadmap linear while translating the current milestone into practical operating windows.',
    windows: [
        {
            id: 'day-30',
            label: 'Next 30 days',
            status: 'current',
            theme: 'Stabilize the business foundation',
            goal: "Get Deadhang's administrative base under control before adding more moving parts.",
            focus_step_ids: ['dh-1', 'dh-2', 'po-1'],
            outcomes: [
                'Business structure and compliance review is defined or underway',
                'Gig tracking workflow is documented enough to repeat',
                'Dashboard remains the active execution surface'
            ],
            guardrail: 'Do not start a large platform rebuild before the basic business and tracking foundation is clear.'
        },
        {
            id: 'day-60',
            label: 'Next 60 days',
            status: 'next',
            theme: 'Lock the money and workflow tools',
            goal: 'Define the smallest useful contractor tool set for invoices, payments, and scheduling.',
            focus_step_ids: ['ct-1', 'ct-2', 'ct-3', 'ct-4'],
            outcomes: [
                'Invoice generator scope is reduced to MVP requirements',
                'Payment tracking requirements are clear',
                'Calendar authorization risk has a concrete mitigation path'
            ],
            guardrail: 'Keep tools narrow: fixed invoice workflow, stable payment tracking, and scheduling reliability before enterprise features.'
        },
        {
            id: 'day-90',
            label: 'Next 90 days',
            status: 'later',
            theme: 'Connect labor, training, and job discovery',
            goal: 'Prepare the first usable loop between Deadhang Labor, Crew Blueprint, Production Atlas, and Contractor Tools.',
            focus_step_ids: ['pa-1', 'cb-1', 'cb-2', 'po-2'],
            outcomes: [
                'Production Atlas has public/private verification standards',
                'Crew Blueprint has a safer content authority boundary',
                'Anti-sprawl controls keep skipped work visible without breaking the linear path'
            ],
            guardrail: 'Do not turn the roadmap into a storage dump. Promote only public-safe, decision-ready work.'
        }
    ]
};

function ninetyEscape(value) {
    return String(value ?? '')
        .replaceAll('&', '&amp;')
        .replaceAll('<', '&lt;')
        .replaceAll('>', '&gt;')
        .replaceAll('"', '&quot;')
        .replaceAll("'", '&#039;');
}

function ninetyWorkItemsById(data) {
    const map = {};
    (data.branches || []).forEach(branch => {
        (branch.work_items || []).forEach(item => {
            map[item.id] = { ...item, branch_name: branch.name, branch_id: branch.id };
        });
    });
    return map;
}

function renderStandaloneNinetyDashboard(data, plan = ninetyDayPlan) {
    const section = document.getElementById('ninety-day-section');
    const container = document.getElementById('ninety-dashboard');
    const title = document.getElementById('ninety-title');
    const summary = document.getElementById('ninety-summary');
    if (!section || !container || !plan.windows?.length) return;

    section.style.display = 'block';
    if (title) title.textContent = plan.title;
    if (summary) summary.textContent = plan.summary;

    const itemsById = ninetyWorkItemsById(data);
    const branchesById = Object.fromEntries((data.branches || []).map(branch => [branch.id, branch]));

    container.innerHTML = plan.windows.map((windowItem, index) => {
        const steps = (windowItem.focus_step_ids || []).map(id => itemsById[id]).filter(Boolean);
        const branchLinks = [...new Set(steps.map(step => step.branch_id))]
            .map(id => branchesById[id])
            .filter(Boolean);
        const outcomes = windowItem.outcomes || [];

        return `
            <article class="ninety-card ninety-${index + 1}">
                <div class="ninety-card-head">
                    <span class="ninety-window">${ninetyEscape(windowItem.label)}</span>
                    <span class="ninety-status">${ninetyEscape(windowItem.status)}</span>
                </div>
                <h3>${ninetyEscape(windowItem.theme)}</h3>
                <p class="ninety-goal">${ninetyEscape(windowItem.goal)}</p>
                <div class="ninety-block">
                    <h4>Focus work</h4>
                    <div class="ninety-steps">
                        ${steps.map(step => `
                            <button class="ninety-step" data-branch-id="${ninetyEscape(step.branch_id)}">
                                <span class="tl-step-dot ${ninetyEscape(step.status || 'not_started')}"></span>
                                <span>${ninetyEscape(step.task)}</span>
                                <em>${ninetyEscape(step.status || 'not_started').replace(/_/g, ' ')}</em>
                            </button>
                        `).join('')}
                    </div>
                </div>
                ${outcomes.length ? `
                    <div class="ninety-block">
                        <h4>Done means</h4>
                        <ul class="ninety-outcomes">
                            ${outcomes.map(outcome => `<li>${ninetyEscape(outcome)}</li>`).join('')}
                        </ul>
                    </div>` : ''}
                ${windowItem.guardrail ? `<p class="ninety-guardrail"><strong>Guardrail:</strong> ${ninetyEscape(windowItem.guardrail)}</p>` : ''}
                ${branchLinks.length ? `<div class="ninety-branches">${branchLinks.map(branch => `<button data-branch-id="${ninetyEscape(branch.id)}">${ninetyEscape(branch.name)}</button>`).join('')}</div>` : ''}
            </article>
        `;
    }).join('');

    container.querySelectorAll('[data-branch-id]').forEach(el => {
        el.addEventListener('click', () => {
            if (typeof showBranchDetail === 'function') {
                showBranchDetail(el.getAttribute('data-branch-id'));
            } else {
                window.location.href = 'branch.html?branch=' + encodeURIComponent(el.getAttribute('data-branch-id'));
            }
        });
    });
}

async function loadStandaloneNinetyDashboard() {
    try {
        const response = await fetch('roadmap.json', { cache: 'no-store' });
        if (!response.ok) throw new Error('Could not load roadmap.json');
        const data = await response.json();
        renderStandaloneNinetyDashboard(data, data.thirty_sixty_ninety || ninetyDayPlan);
    } catch (error) {
        console.error('Failed to load 30 / 60 / 90 dashboard', error);
    }
}

loadStandaloneNinetyDashboard();
