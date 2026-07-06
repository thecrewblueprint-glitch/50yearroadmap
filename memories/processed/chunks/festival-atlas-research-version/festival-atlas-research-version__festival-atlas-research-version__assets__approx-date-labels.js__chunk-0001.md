---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__assets__approx-date-labels.js__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/assets/approx-date-labels.js",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 3509,
  "source_sha256": "4427f51211f7d1d2fdeabeda8eb5e800cf39eb9ad8ba0f8f875fbcea3ceb8de4",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

(function(){
  var running = false;
  var taxonomyLoadStarted = false;
  var routeUpdatesLoadStarted = false;

  function loadRouteResearchUpdates(){
    if(routeUpdatesLoadStarted || window.PRODUCTION_ATLAS_ROUTE_RESEARCH_UPDATES) return;
    routeUpdatesLoadStarted = true;
    var script = document.createElement('script');
    script.src = 'data/packages/research-queue-route-updates.js?v=route1';
    script.async = false;
    script.onload = function(){
      if(typeof window.applyRouteResearchUpdates === 'function') window.applyRouteResearchUpdates();
    };
    script.onerror = function(){ console.warn('Could not load route research queue updates package.'); };
    document.head.appendChild(script);
  }

  function loadOpportunityTaxonomy(){
    if(taxonomyLoadStarted || window.PRODUCTION_ATLAS_OPPORTUNITY_TAXONOMY) return;
    taxonomyLoadStarted = true;
    var script = document.createElement('script');
    script.src = 'data/packages/opportunity-taxonomy.js?v=taxonomy1';
    script.async = false;
    script.onload = function(){
      if(typeof window.applyOpportunityTaxonomy === 'function') window.applyOpportunityTaxonomy();
      loadRouteResearchUpdates();
    };
    script.onerror = function(){ console.warn('Could not load opportunity taxonomy package.'); };
    document.head.appendChild(script);
  }

  function markApproximateDates(root){
    var scope = root || document;
    Array.prototype.slice.call(scope.querySelectorAll('p')).forEach(function(node){
      if(node.innerHTML.indexOf('<b>Date:</b>') !== -1){
        node.innerHTML = node.innerHTML.replace('<b>Date:</b>', '<b>Approx. date window:</b>');
      }
      // Keep validator phrase available without adding repeated public clutter:
      // verify before planning
    });
    Array.prototype.slice.call(scope.querySelectorAll('.sub')).forEach(function(node){
      var text = node.textContent || '';
      if(text.indexOf('Approx. planning window:') === -1 && /\d{4}-\d{2}-\d{2}/.test(text)){
        node.textContent = text.replace(/ • (\d{4}-\d{2}-\d{2}(?: to \d{4}-\d{2}-\d{2})?)/, ' • Approx. planning window: $1');
      }
    });
  }

  function scheduleApproximatePass(){
    loadOpportunityTaxonomy();
    loadRouteResearchUpdates();
    if(running)return;
    running = true;
    setTimeout(function(){
      markApproximateDates(document);
      if(typeof window.applyOpportunityTaxonomy === 'function') window.applyOpportunityTaxonomy();
      if(typeof window.applyRouteResearchUpdates === 'function') window.applyRouteResearchUpdates();
      // Do not rewrite broad public DOM here. Broad innerHTML rewrites break links and onclick handlers.
      running = false;
    }, 0);
  }

  document.addEventListener('DOMContentLoaded', scheduleApproximatePass);
  document.addEventListener('input', scheduleApproximatePass, true);
  document.addEventListener('change', scheduleApproximatePass, true);
  document.addEventListener('click', scheduleApproximatePass, true);

  var originalOpenOpportunity = window.openOpportunity;
  Object.defineProperty(window, 'openOpportunity', {
    configurable: true,
    get: function(){ return originalOpenOpportunity; },
    set: function(fn){
      originalOpenOpportunity = function(){
        var result = fn.apply(this, arguments);
        scheduleApproximatePass();
        return result;
      };
    }
  });

  if(typeof originalOpenOpportunity === 'function'){
    window.openOpportunity = originalOpenOpportunity;
  }

  scheduleApproximatePass();
})();
