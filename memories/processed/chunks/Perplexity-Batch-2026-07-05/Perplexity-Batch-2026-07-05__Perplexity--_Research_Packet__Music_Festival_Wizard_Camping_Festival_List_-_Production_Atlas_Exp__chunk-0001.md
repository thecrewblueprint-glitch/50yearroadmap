---
{
  "chunk_id": "Perplexity-Batch-2026-07-05__Perplexity--_Research_Packet__Music_Festival_Wizard_Camping_Festival_List_-_Production_Atlas_Exp__chunk-0001",
  "archive_id": "Perplexity-Batch-2026-07-05",
  "archive_filename": "Perplexity-Batch-2026-07-05.zip",
  "source_path": "Perplexity-#_Research_Packet__Music_Festival_Wizard_Camping_Festival_List_—_Production_Atlas_Expansion_##_Project_Context_I_am_building___Production_Atlas___Festival_Atlas__,_a_static_public-facing_work_resear.md",
  "chunk_index": 1,
  "chunk_count_for_source": 7,
  "char_start": 0,
  "char_end": 11998,
  "source_sha256": "cb50cec3794d13d4b67433a39def933e305f6b956d3b06ce41ddd683990eeb7e",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

Original URL: https://www.perplexity.ai/search/b6fdb0aa-5ac1-4a93-8991-7eec6b86adfb
Conversation Time: 6/29/2026, 2:46:37 AM
Export Time: 7/5/2026, 5:02:35 PM

**[USER]**

# Research Packet: Music Festival Wizard Camping Festival List — Production Atlas Expansion

## Project Context

I am building **Production Atlas / Festival Atlas**, a static public-facing work research app for live-event production opportunities.

The app is designed to help answer:

* Where is the work?
* When is it happening?
* Which production departments does the event likely touch?
* Who are the public employer, vendor, promoter, labor, venue, or union-route leads?
* What action should a worker or small labor company take next?

The current app is a **static public GitHub Pages app**. It has:

* No backend
* No login
* No database
* No private contact storage
* No scraping automation
* No pay-rate storage
* No private crew notes

This research packet is for adding or reviewing public festival opportunity records from Music Festival Wizard search results.

## Public-Safety Rules

Do **not** collect or publish:

* Private contacts
* Phone numbers
* Personal emails
* Pay rates
* Hotel or lodging details
* Crew rumors
* Private referrals
* Private field notes
* NDA information
* Client-sensitive information
* Non-public vendor lists

Use only:

* Official event websites
* Official promoter / producer websites
* Official venue websites
* Official careers / apply pages
* Public company websites
* Public source articles
* Public union/local directory pages
* Public city, venue, or permitting information when relevant

If something is not publicly confirmed, write:

> Unknown publicly. Human verification needed.

## Source Link Rule

Source links should be centralized for auditability.

Do not put raw source links inside:

* Opportunity popups
* Map popups
* Calendar cards
* Employer cards

Instead, collect source URLs for a central `sources.html` or source-audit page.

## Research Objective

Research the following festival list and produce clean, public-safe opportunity intelligence for Production Atlas.

For each festival, identify:

1. Official festival website
2. Official 2026 or 2027 event dates
3. City and state
4. Venue or site, if public
5. Festival organizer / promoter / producer, if public
6. Whether the organizer belongs to a known organizer category
7. Public ticket page
8. Public contact page
9. Public apply / volunteer / vendor / staff / careers route, if available
10. Likely production departments involved
11. Potential public employer / vendor / labor-route leads
12. Nearby IATSE local or public labor-route clue, if relevant
13. Confidence level
14. Next recommended public-safe action

## Organizer Categories to Use

Classify organizers under these categories when supported by public evidence:

* Independent
* AEG
* Live Nation
* Insomniac
* C3 Presents
* AC Entertainment
* Festival Republic
* Eventim
* Disco Donnie
* Relentless Beats
* Sixthman
* Superstruct
* I-Motion
* Danny Wimmer
* ID&T
* Unknown publicly

If a festival appears independent or local but no organizer is clearly confirmed, use:

> Unknown publicly. Human verification needed.

Do **not** guess organizer ownership.

## Production Department Taxonomy

Use these department categories:

* Staging / Structures
* Rigging
* Lighting
* Audio
* Video / LED
* Power / Electrical
* Site Operations
* Logistics / Equipment Movement
* Scenic / Carpentry
* Backline
* Stage Management
* Production Assistant / Production Office
* Security / Guest Services
* Vendor / Food / Market Operations
* Camping / Grounds / Parking
* Other / Unknown

Only mark departments that are reasonably relevant from public festival type, venue, scale, camping status, or known event infrastructure. Do not overstate.

## Confidence Labels

Use these labels:

### High confidence

Official event website or organizer page confirms date/location/organizer.

### Medium confidence

Reliable public event listing confirms the event, but organizer or operational route needs more verification.

### Low confidence

Only secondary listings are available, dates are incomplete, or official pages are missing/outdated.

## Required Output Format

For each festival, return a structured record in this format:

```text
Festival Name:
Year:
City:
State:
Venue / Site:
Dates:
Organizer / Promoter:
Organizer Category:
Official Website:
Ticket Page:
Public Contact Page:
Public Apply / Volunteer / Staff / Vendor Route:
Likely Production Departments:
Public Employer / Vendor / Labor Route Leads:
Nearby IATSE / Labor Route Notes:
Source Notes:
Confidence:
Next Recommended Action:
Public-Safe Notes:
```

## JSON-Ready Output Format

Also provide a JSON-ready version using this structure:

```json
{
  "name": "",
  "year": "",
  "city": "",
  "state": "",
  "venue": "",
  "startDate": "",
  "endDate": "",
  "organizer": {
    "name": "",
    "category": "",
    "confidence": ""
  },
  "links": {
    "officialWebsite": "",
    "tickets": "",
    "contact": "",
    "apply": "",
    "volunteer": "",
    "vendor": "",
    "careers": ""
  },
  "departments": [],
  "publicRoutes": [],
  "laborRouteNotes": "",
  "sources": [],
  "confidence": "",
  "nextAction": "",
  "publicSafeNotes": ""
}
```

## Festival List to Research

### 2026 Festivals

1. APOG 2026
2. Great Blue Heron Festival 2026
3. High Sierra Music Festival 2026
4. Roostertail Music Festival 2026
5. Desert Hearts Festival 2026
6. Calling All Magical People 2026
7. Briggs Farm Blues Festival 2026
8. Country Boom 2026
9. Country Concert 2026
10. ND Country Fest 2026
11. Pendleton Whisky Music Fest 2026
12. Vicki’s Camp N Country Jam 2026
13. Dead of Summer Festival 2026
14. Hodag Country Festival 2026
15. North Atlantic Blues Festival 2026
16. 4848 Festival 2026
17. Beaver Island Music Festival 2026
18. Country Jam Wisconsin 2026
19. Harefest 2026
20. Moe.Down 2026
21. Rock Fest Wisconsin 2026
22. Country Thunder Wisconsin 2026
23. Friendly Gathering 2026
24. GrassRoots Finger Lakes Festival 2026
25. Grey Fox Bluegrass Festival 2026
26. Inkcarceration Festival 2026
27. Levitate Festival 2026
28. Northern Nights 2026
29. Under the Big Sky Fest 2026
30. Wootick Festival 2026
31. Dean Claire’s 2026
32. Flood City Festival 2026
33. Headwaters Country Jam 2026
34. Night in the Country Nevada 2026
35. Big Dub Festival 2026
36. FloydFest 2026
37. Newport Folk Festival 2026
38. Red Ants Pants Festival 2026
39. RockyGrass Festival 2026
40. Summer Apex 2026
41. The Great Beyond 2026
42. Timber! 2026
43. County Line Country Fest 2026
44. Everwild Festival 2026
45. Hinterland Music Festival 2026
46. Oregon Jamboree 2026
47. Pickathon 2026
48. Rhythms on the Rio 2026
49. Salmonfest 2026
50. Sound Haven 2026
51. Terp Float Fest 2026
52. Beanstalk Music Festival 2026
53. Domefest 2026
54. People Fest 2026
55. Telluride Jazz Festival 2026
56. WE Fest 2026
57. XRoads41 2026
58. Elements Music Festival 2026
59. Grand Targhee Bluegrass Fest 2026
60. Re/Evolution Festival 2026
61. Rocky Mountain Folks Festival 2026
62. Summer’s End Smokeout 2026
63. Boots on the Bend 2026
64. Neon Nights 2026
65. Bass Canyon 2026
66. Black Bear Americana Music Fest 2026
67. Field of Vision Festival 2026
68. Green Mountain Bluegrass Fest 2026
69. Philadelphia Folk Festival 2026
70. Reggae on the River 2026
71. Gathering of the Juggalos 2026
72. Camp Redwoods 2026
73. Camp Alderwild 2026
74. Ionia Freak Fair 2026
75. Burning Man 2026
76. Caveman Music Festival 2026
77. Delaware Valley Bluegrass Festival 2026
78. Earl Scruggs Music Festival 2026
79. FarmJam Music Festival 2026
80. Front Porch Festival 2026
81. John Coltrane Jazz & Blues Fest 2026
82. Muddy Roots 2026
83. Rhythm and Roots 2026
84. Rocklahoma 2026
85. RPM Fest 2026
86. Secret Dreams Festival 2026
87. Shoe Fest 2026
88. Karnival of the Arts 2026
89. Shangri-La Festival 2026
90. Ghost Ranch Music Festival 2026
91. Healing Appalachia 2026
92. Infrasound Equinox 2026
93. Unbroken Circle Festival 2026
94. Dancefestopia 2026
95. Group Therapy Weekender 2026
96. Wheatland Music Festival 2026
97. Unison 2026
98. Born and Raised Festival 2026
99. Bear Music Festival 2026
100. Borderland Festival 2026
101. Cascade Equinox Festival 2026
102. Lost Lands 2026
103. Louder Than Life Festival 2026
104. Nocturnal Wonderland 2026
105. Pickin’ in the Pines 2026
106. Telluride Blues and Brews 2026
107. Wormtown Music Festival 2026
108. Yahn Dawn 2026
109. Fort Desolation Fest 2026
110. Nocturnal Valley 2026
111. Big Fam Festival 2026
112. Bourbon & Beyond 2026
113. Camp Deep End 2026
114. Rock the Locks 2026
115. Sisters Folk Festival 2026
116. Smalltown Gathering 2026
117. Same Same But Different 2026
118. Fête du Void 2026
119. Submersion Festival 2026
120. Symmetry Festival 2026
121. Wakaan Music Festival 2026
122. Huck Finn Jubilee 2026
123. Shakori Hills GrassRoots Festival Fall 2026
124. Weedstock 2026
125. Blue Highway Fest 2026
126. Form Arcosanti Festival 2026
127. Head Trip 2026
128. Hillberry 2026
129. Joshua Tree Festival Fall 2026
130. Moonshiner’s Ball 2026
131. Suwannee Roots Revival 2026
132. The Ramble Festival 2026
133. Valley of the Seven Stars 2026
134. Strawberry Music Festival Fall 2026
135. Astronox 2026
136. Off the Grid Campout Socal 2026
137. Suwannee Hulaween 2026
138. Beyond Existence 2026
139. Orange Blossom Revue 2026
140. Cascade Equinox Festival 2026

### 2027 Festivals

141. Gem and Jam 2027
142. Suwannee Amp Jam 2027
143. Outlaws & Legends 2027
144. Suwannee Spring Reunion 2027
145. Country Thunder Arizona 2027
146. Coachella Music Festival 2027
147. Old Settler’s Music Festival 2027
148. Stagecoach Festival 2027
149. MerleFest 2027
150. Sunshine Get Down 2027
151. Welcome to Rockville 2027
152. Sonic Temple Festival 2027
153. EDC Las Vegas 2027
154. Showcation 2027
155. Tico Time Bluegrass Festival 2027
156. Lightning in a Bottle 2027
157. Rooster Walk 2027
158. Michael Arnone’s Crawfish Fest 2027
159. Rise & Vibes Music Festival 2027
160. Beyond Wonderland Midwest 2027
161. FreshGrass Festival 2027

## Special Attention Items

### Duplicates / repeat records

Check whether the following are duplicate annual records, separate editions, or accidental duplicate listings:

* Cascade Equinox Festival 2026 appears twice in the collected list.
* Suwannee events may share venue/operator routes but should remain separate event records.
* Country Thunder events may be multi-market and should be categorized by state/market.
* GrassRoots-related festivals may share organization or network links but should be verified individually.

### Cancelled or uncertain events

Some screenshots showed “cancelled” or uncertain status. Confirm before including as active opportunities.

When cancelled:

```text
Status: Cancelled
Use in app: Do not treat as active work opportunity.
Next action: Track only if future edition is announced publicly.
```

### 2027 events

For 2027 events, confirm whether:

* Dates are officially announced
* Event is recurring but dates are inferred
* Ticket pages are active
* Venue is confirmed
* Organizer is confirmed

Do not assume 2027 dates from 2026 patterns.

## Research Method

For each festival, search in this order:

1. Official festival website
2. Festival official social media only if the website is unavailable or outdated
3. Official ticketing page
4. Official organizer / promoter page
5. Venue page
6. Public city / tourism / event calendar page
7. Reliable secondary event listing
8. Public company, employer, or careers page

Do not rely only on Music Festival Wizard. Use it as a discovery source, not final verification.

## What to Return First

Start with a smaller batch before processing the full list.

Return the first batch as:

```text
Batch 1: 20 festivals
```

For each batch include:

* Completed records
* Records needing human verification
* Records that appear cancelled
* Records with missing organizer
* Records with useful public apply/careers/volunteer/vendor routes

