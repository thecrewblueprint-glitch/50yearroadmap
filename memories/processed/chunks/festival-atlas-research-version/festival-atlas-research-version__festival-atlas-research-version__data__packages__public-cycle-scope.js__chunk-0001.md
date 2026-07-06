---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__data__packages__public-cycle-scope.js__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/data/packages/public-cycle-scope.js",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 1384,
  "source_sha256": "14ef511469a0c22f7e2205f52562851f4fab2d2a8c68ad0ca6d34fcda04a0204",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

(function(){
  var DEFAULT_PUBLIC_CYCLE_YEAR = 2026;

  function parseLocalDate(value){
    if(!value) return null;
    var date = new Date(String(value) + 'T00:00:00');
    return isNaN(date.getTime()) ? null : date;
  }

  function recordCycleYear(record){
    if(!record) return null;
    var explicit = Number(record.publicCycleYear || record.eventYear || 0);
    if(explicit) return explicit;
    var start = parseLocalDate(record.startDate);
    return start ? start.getFullYear() : null;
  }

  function isFutureCycleRecord(record){
    var year = recordCycleYear(record);
    return !!(year && year !== DEFAULT_PUBLIC_CYCLE_YEAR);
  }

  function applyPublicCycleScope(){
    var scopedOut = [];
    var pool = window.RESOURCE_OPPORTUNITIES;
    if(!Array.isArray(pool)) return;

    pool.forEach(function(record){
      if(!record || !record.id) return;
      if(!isFutureCycleRecord(record)) return;
      if(record.keepInDefaultPublicCycle === true) return;

      record.visibleInActive2026View = false;
      record.defaultPublicCycleHidden = true;
      record.defaultPublicCycleYear = DEFAULT_PUBLIC_CYCLE_YEAR;
      scopedOut.push(record.id);
    });

    window.PRODUCTION_ATLAS_PUBLIC_CYCLE_SCOPE = {
      applied: true,
      defaultPublicCycleYear: DEFAULT_PUBLIC_CYCLE_YEAR,
      scopedOutOpportunityIds: scopedOut
    };
  }

  applyPublicCycleScope();
})();
