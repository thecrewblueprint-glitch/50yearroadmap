---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__data__iatse-us-local-directory.js__chunk-0002",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/data/iatse-us-local-directory.js",
  "chunk_index": 2,
  "chunk_count_for_source": 2,
  "char_start": 10942,
  "char_end": 13004,
  "source_sha256": "a6d76dc61e821078afd83a6e2c79d608c999a80831498f75d55d21441ad709d4",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

al Wardrobe
794|District 10|New York, New York|Broadcast
829|District 10|New York, New York|Exhibition Employees, Bill Posters, Billers and Distributors
858|District 10|Rochester, New York|Theatrical Wardrobe
917|District 10|Atlantic City, New Jersey|Casino Hotel Employees
ACT|District 10|New York, New York|Associated Craft Technicians
B751|District 10|New York, New York|Mail Telephone Order Clerks
MAL|District 10|New York, New York|Member At Large
R&T|District 10|New York, New York|Radio and Television
18032|District 10|New York, New York|Association of Theatrical Press Agents and Managers`;
const states=['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','District of Columbia','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming','Puerto Rico','U.S. Virgin Islands'];
function stateFromJurisdiction(j){return states.filter(s=>j.includes(s));}
window.IATSE_US_LOCAL_DIRECTORY={meta:{name:'United States IATSE Local Directory',updated:'2026-06-21',scope:'United States, Puerto Rico, and U.S. Virgin Islands locals represented in available IATSE local directory research',sourceUrl:source,sourceNote:'Use the official IATSE local-union directory for final contact verification before outreach. This file is a worker-facing lookup aid, not a jurisdiction ruling.',recordCount:raw.trim().split('\n').length},locals:raw.trim().split('\n').map(line=>{const [local,district,jurisdiction,craft]=line.split('|');return{local,district,jurisdiction,craft,states:stateFromJurisdiction(jurisdiction),sourceUrl:source,verificationStatus:'directory_derived_contact_verify_before_outreach'}})};
})();
