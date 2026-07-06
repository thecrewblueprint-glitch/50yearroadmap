---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__tools__validate-data.js__chunk-0002",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/tools/validate-data.js",
  "chunk_index": 2,
  "chunk_count_for_source": 2,
  "char_start": 11384,
  "char_end": 12406,
  "source_sha256": "2ccca103a9938df07e2db5488bae144cb010b9817cb11ad7ddc6dd296fdfaf29",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

eck(bySeq[160] && bySeq[160].name === 'Cascade Equinox Festival' && bySeq[160].year === 2027,
        'festival master sequence 160 must be Cascade Equinox Festival 2027');
      check(bySeq[161] && bySeq[161].name === 'FreshGrass Festival' && bySeq[161].year === 2027,
        'festival master sequence 161 must be FreshGrass Festival 2027');
    }
  }
} else {
  warn.push(`Missing optional festival research intake asset: ${masterListFile}`);
}

if (warn.length) {
  console.warn('\nWarnings:');
  warn.forEach(m => console.warn(`  - ${m}`));
}

if (fail.length) {
  console.error('\nFailures:');
  fail.forEach(m => console.error(`  - ${m}`));
  process.exit(1);
}

console.log('Production Atlas data validation passed.');
console.log(`Total final records: ${records.length}`);
console.log(`Active: ${activeCount} (${sourcedCount} sourced, ${unsourcedCount} without source URL)`);
console.log(`Inactive (hidden): ${inactiveCount}`);
console.log('Separate 2027 rollover and festival master-list validation complete.');
