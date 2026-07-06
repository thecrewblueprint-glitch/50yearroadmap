---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__data__packages__research-queue-route-updates.js__chunk-0002",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/data/packages/research-queue-route-updates.js",
  "chunk_index": 2,
  "chunk_count_for_source": 2,
  "char_start": 11297,
  "char_end": 14709,
  "source_sha256": "088c14574e2f10d50498dc0e0e8d050d40a50ea82776ff1c49e3fb6ffdcccb78",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

rk (research local number before outreach)',
        'research Nissan Stadium approved production vendor route separately from outdoor stages',
        'research multi-venue logistics across stadium, outdoor parks, and club venues',
        'verify country festival vendor stack specifics for Nashville production'
      ],
      researchQueueNote: 'Route research update: CMA Fest is produced by the Country Music Association and Live Nation across multiple Nashville venues (June 4-7, 2026). Main stage at Nissan Stadium uses a distinct production route from smaller outdoor and club-stage formats. Do not generalize vendor or labor routes across all venues without separate evidence for each venue type.'
    }
  ];

  function findRecord(id){
    var pools = [window.RESOURCE_OPPORTUNITIES, window.scopedOpportunities];
    for(var i=0;i<pools.length;i++){
      var pool = pools[i];
      if(!Array.isArray(pool)) continue;
      var record = pool.find(function(item){return item && item.id === id;});
      if(record) return record;
    }
    return null;
  }

  function mergeSources(record, sources){
    if(!record || !Array.isArray(sources)) return;
    if(!record.intelligence) record.intelligence = {};
    if(!Array.isArray(record.intelligence.publicSources)) record.intelligence.publicSources = [];
    sources.forEach(function(source){
      if(!source || !source.url) return;
      if(record.intelligence.publicSources.some(function(existing){return existing.url === source.url;})) return;
      record.intelligence.publicSources.push({label:source.label || 'route research public source',url:source.url});
    });
  }

  function applyRouteResearchUpdates(){
    routeUpdates.forEach(function(update){
      var record = findRecord(update.id);
      if(!record) return;
      record.routeResearchStatus = update.routeResearchStatus;
      record.researchQueueNote = update.researchQueueNote;
      if(Array.isArray(update.nextResearchActions)) record.nextResearchActions = update.nextResearchActions.slice();
      mergeSources(record, update.publicSources);
    });
    window.PRODUCTION_ATLAS_ROUTE_RESEARCH_UPDATES = routeUpdates;
  }

  function renderRouteNotice(){
    var app = document.querySelector('#app');
    var page = document.body ? document.body.dataset.page : '';
    if(!app || page !== 'analytics' || app.dataset.routeResearchNotice === 'applied') return;
    var note = document.createElement('div');
    note.className = 'notice route-research-update-note';
    note.style.margin = '0 0 16px';
    note.textContent = 'Route research updates applied: 12 events now have public producer/operator route leads — Summerfest, Breakaway, Country Thunder, BottleRock, Electric Forest, Lollapalooza, Coachella, Stagecoach, EDC Las Vegas, Ultra Miami, Bonnaroo, and CMA Fest. Vendor and labor-provider assignments remain verification-open for all records.';
    app.insertBefore(note, app.firstChild);
    app.dataset.routeResearchNotice = 'applied';
  }

  window.applyRouteResearchUpdates = applyRouteResearchUpdates;
  applyRouteResearchUpdates();
  document.addEventListener('DOMContentLoaded', function(){
    setTimeout(function(){
      applyRouteResearchUpdates();
      renderRouteNotice();
    }, 0);
  });
  document.addEventListener('click', function(){
    setTimeout(function(){
      applyRouteResearchUpdates();
      renderRouteNotice();
    }, 0);
  }, true);
})();
