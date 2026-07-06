---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__assets__atlas-core-v2.js__chunk-0005",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/assets/atlas-core-v2.js",
  "chunk_index": 5,
  "chunk_count_for_source": 5,
  "char_start": 43449,
  "char_end": 48142,
  "source_sha256": "f4caf46aede8bbe9400ff19424b9ce38f4855b8cb503f9804489636241a13d06",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

the available-worker list.</li><li><b>Get safety credentials early.</b> OSHA 10/30, rigging, fall-protection, and first-aid certs are often required to be callable.</li><li><b>Work calls and build hours.</b> Be reliable and get known by the steward and business agent.</li><li><b>Apply for membership.</b> When you meet the requirements set by Local '+esc(l.local)+' (hours, sponsorship, any vote), apply to join.</li></ol><div class="notice">Each IATSE local sets its own membership requirements and process. Verify current details directly with the local before relying on anything here.</div>')};
  window.openBranch=function(id){var b=branches.find(function(x){return x.id===id});if(!b)return;ensureBranchResearch().then(function(){var records=branchIndex.records.filter(function(r){return r.branchId===id});var cards=records.map(function(r){var o=opportunities.find(function(x){return norm(x.id)===norm(r.opportunityId)||norm(x.name)===norm(r.opportunityName)})||{id:r.opportunityId,name:r.opportunityName,departments:[id]};return '<div style="margin:0 0 4px"><p class="sub" style="margin:0 0 4px;color:var(--muted)"><b>'+esc(o.name||r.opportunityName||r.opportunityId)+'</b></p>'+branchCard(o,id)+'</div>'}).join('');var general=matchingEmployers(id).slice(0,12).map(employerRow).join('');openModal('<h2>'+esc(b.name)+'</h2><h3>Employers by festival</h3>'+(cards||'<p class="sub">No festival-specific companies listed yet.</p>')+(general?'<h3>Industry companies in this branch</h3><ul style="margin:0;padding:0">'+general+'</ul>':''))})};

  var _lastFocus=null;
  function openModal(html){var modal=$('#modal'),content=$('#modalContent');if(!modal||!content)return;content.innerHTML=html;modal.classList.add('open');modal.setAttribute('role','dialog');modal.setAttribute('aria-modal','true');var heading=content.querySelector('h1,h2,h3');if(heading){heading.id=heading.id||'modal-title';modal.setAttribute('aria-labelledby',heading.id)}else{modal.removeAttribute('aria-labelledby')}_lastFocus=document.activeElement;var box=modal.querySelector('.modalbox');if(box){box.setAttribute('tabindex','-1');box.focus()}
    if(!modal.dataset.trapBound){modal.dataset.trapBound='true';modal.addEventListener('keydown',function(e){if(e.key!=='Tab')return;var nodes=modal.querySelectorAll('a[href],button:not([disabled]),input,select,textarea,[tabindex]:not([tabindex="-1"])');if(!nodes.length)return;var first=nodes[0],last=nodes[nodes.length-1];if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus()}else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus()}})}}
  window.openModal=openModal;
  window.closeModal=function(){var modal=$('#modal');if(modal){modal.classList.remove('open');modal.removeAttribute('aria-modal')}if(_lastFocus&&typeof _lastFocus.focus==='function')_lastFocus.focus();_lastFocus=null};

  var EXTERNAL_RENDER_PAGES={calendar:1,map:1,employers:1,guide:1};
  function renderPage(){var page=document.body.dataset.page;if(EXTERNAL_RENDER_PAGES[page])return;({home:renderHome,opportunities:renderOpportunities,iatse:renderIatse,matrix:renderMatrix,branches:renderBranches,analytics:renderAnalytics,sources:renderSources,schedule:renderSchedule}[page]||renderHome)()}
  window.renderPage=renderPage;
  function init(){branches=window.RESOURCE_BRANCHES||[];allOpportunities=window.RESOURCE_OPPORTUNITIES||[];employers=window.RESOURCE_EMPLOYERS||[];iatseLocals=((window.IATSE_US_LOCAL_DIRECTORY||{}).locals)||[];opportunities=allOpportunities.filter(function(o){return o.visibleInActive2026View===true&&o.publishSafety!=='do_not_publish'&&o.visibility!=='do_not_publish'}).map(classify);window.branches=branches;window.employers=employers;window.scopedOpportunities=opportunities;window.iatseLocals=iatseLocals;fillFilters();applyUrlFilters();renderPage();var modal=$('#modal');if(modal)modal.addEventListener('click',function(e){if(e.target.id==='modal')window.closeModal()});document.addEventListener('keydown',function(e){if(e.key==='Escape'){var m=$('#modal');if(m&&m.classList.contains('open'))window.closeModal()}if(e.key!=='Enter'&&e.key!==' '&&e.key!=='Spacebar')return;if(!e.target||!e.target.closest)return;var el=e.target.closest('[data-keyclick]');if(!el)return;var tag=e.target.tagName;if((tag==='A'||tag==='BUTTON'||tag==='INPUT'||tag==='SELECT'||tag==='TEXTAREA')&&e.target!==el)return;e.preventDefault();el.click()});var page=document.body.dataset.page;var branchPages={home:1,branches:1,sources:1,analytics:1,opportunities:1};ensureBranchResearch().then(function(){if(branchPages[page])renderPage()})}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
