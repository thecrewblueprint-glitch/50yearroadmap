---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__data__packages__opportunity-rollover-2027.js__chunk-0002",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/data/packages/opportunity-rollover-2027.js",
  "chunk_index": 2,
  "chunk_count_for_source": 2,
  "char_start": 11382,
  "char_end": 12143,
  "source_sha256": "4c47def7aa2f18d11ffa99c80dc4ab19b054ac3d931e3f0aa188b8633bf3b4c3",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

 2027 date/source','create separate 2027 opportunity record if official/public source is available','keep private assumptions out of public app until verified'];
    });
  }

  function applyRollover(){
    verified2027.forEach(applyVerified);
    pending2027.forEach(markPending);
    var createdIds = verified2027.map(function(item){return nextYearId(item.id);});
    window.PRODUCTION_ATLAS_2027_ROLLOVER = {
      generatedAt: generatedAt,
      cutoffDate: cutoffDate,
      model: rolloverModel,
      sourceIds: verified2027.map(function(item){return item.id;}),
      createdIds: createdIds,
      verifiedIds: createdIds,
      pendingIds: pending2027.slice()
    };
  }

  window.applyOpportunityRollover2027 = applyRollover;
  applyRollover();
})();
