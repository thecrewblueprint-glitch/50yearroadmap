---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__assets__atlas-core-v2.js__chunk-0003",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/assets/atlas-core-v2.js",
  "chunk_index": 3,
  "chunk_count_for_source": 5,
  "char_start": 20897,
  "char_end": 32831,
  "source_sha256": "f4caf46aede8bbe9400ff19424b9ce38f4855b8cb503f9804489636241a13d06",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

oppSig=sig;oppPage=0;}var pages=Math.max(1,Math.ceil(data.length/PER_PAGE));if(oppPage>=pages)oppPage=pages-1;if(oppPage<0)oppPage=0;var pageData=data.slice(oppPage*PER_PAGE,oppPage*PER_PAGE+PER_PAGE);var stateCount=uniq(data.filter(function(o){return o.state&&o.state!=='US'}).map(function(o){return o.state})).length;var pg=pgControls(oppPage,pages,data.length,PER_PAGE,'oppPageSet');var savedBtn=$('#savedOnly');if(savedBtn){var savedCount=getSavedIds().length;savedBtn.textContent=(savedOnly?'★':'☆')+' Saved'+(savedCount?' ('+savedCount+')':'')}var emptyMsg=savedOnly?'<p>No saved festivals yet. Tap the ☆ on any festival card to save it here.</p>':'<p>No festivals match the current filter.</p>';el.innerHTML='<h2>Festivals</h2><p class="lead">Browse festivals by date, city, venue, producer, production window, and public employer contacts.</p><div class="stats" style="grid-template-columns:repeat(2,1fr);margin:0 0 18px"><div class="stat"><b>'+data.length+'</b><span>festivals</span></div><div class="stat"><b>'+stateCount+'</b><span>states</span></div></div><div class="notice">Know an active festival that belongs here? Submit it on the <a href="contribute.html">Contribute page</a>.</div>'+pg+'<div class="grid">'+(data.length?pageData.map(opportunityCard).join(''):emptyMsg)+'</div>'+pg}
  window.oppPageSet=function(n){oppPage=Number(n)||0;renderOpportunities();var el=$('#app');if(el&&el.scrollIntoView)try{el.scrollIntoView({behavior:'smooth',block:'start'})}catch(e){}};
  var iatseTab='join',iatseLocPage=0,iatseLocSig='__init';
  window.iatseSetTab=function(t){iatseTab=t;if(t!=='find'){var qi=$('#q');if(qi)qi.value='';}renderIatse();var el=$('#app');if(el&&el.scrollIntoView)try{el.scrollIntoView({behavior:'smooth',block:'start'})}catch(e){}};
  window.iatseLocPageSet=function(n){iatseLocPage=Number(n)||0;renderIatse();var el=$('#app');if(el&&el.scrollIntoView)try{el.scrollIntoView({behavior:'smooth',block:'start'})}catch(e){}};
  function iatseTabBtn(id,label,active){return '<button class="iatse-tab'+(active===id?' active':'')+'" type="button" id="iatse-tab-'+id+'" role="tab" aria-selected="'+(active===id?'true':'false')+'" aria-controls="iatse-panel-'+id+'" tabindex="'+(active===id?'0':'-1')+'" onclick="iatseSetTab(\''+id+'\')">'+label+'</button>'}
  var IATSE_TAB_ORDER=['join','find','about'];
  document.addEventListener('keydown',function(e){
    if(e.key!=='ArrowRight'&&e.key!=='ArrowLeft')return;
    if(!e.target||!e.target.closest||!e.target.closest('.iatse-tabs'))return;
    var current=IATSE_TAB_ORDER.indexOf((e.target.id||'').replace('iatse-tab-',''));
    if(current<0)return;
    e.preventDefault();
    var next=(current+(e.key==='ArrowRight'?1:IATSE_TAB_ORDER.length-1))%IATSE_TAB_ORDER.length;
    window.iatseSetTab(IATSE_TAB_ORDER[next]);
    var btn=document.getElementById('iatse-tab-'+IATSE_TAB_ORDER[next]);
    if(btn)btn.focus();
  });
  function renderIatse(){
    var el=$('#app');if(!el)return;
    var info=window.IATSE_ORGANIZATION_INFO||{};var summary=info.officialSummary||{};var families=info.departmentFamilies||[];
    var q=(filterValues().q||'').trim().toLowerCase();
    var all=iatseLocals.slice();
    var matched=q?all.filter(function(l){return searchMatch(iatseText(l),q)}):all;
    var primary=[],secondary=[];matched.forEach(function(l){if(l.district==='National')secondary.push(l);else primary.push(l)});
    if(q!==iatseLocSig){iatseLocSig=q;iatseLocPage=0;}
    var tab=q?'find':iatseTab;
    var join='<p class="lead">Most live-event workers join by first working as extra or overhire crew for a local, building hours and a reputation, then applying for membership.</p>'+
      '<div class="steps">'+
        '<div class="step-card"><span class="step-n">1</span><h4>Find your local</h4><p>Use the <b>Find a local</b> tab to search by city and craft, then open the official IATSE directory for its website and contact.</p></div>'+
        '<div class="step-card"><span class="step-n">2</span><h4>Ask about overhire</h4><p>Contact the local and ask how to get on the available / extra list for permit or overhire calls.</p></div>'+
        '<div class="step-card"><span class="step-n">3</span><h4>Get safety certs</h4><p>OSHA 10/30, rigging, and first-aid certs make you callable and are often required.</p></div>'+
        '<div class="step-card"><span class="step-n">4</span><h4>Work calls, build hours</h4><p>Be reliable and get known by the steward and business agent.</p></div>'+
        '<div class="step-card"><span class="step-n">5</span><h4>Apply for membership</h4><p>When you meet the local requirements (hours, sponsorship, any vote), apply to join.</p></div>'+
      '</div>'+
      '<h3 class="section-kicker">Permit vs. member</h3><div class="grid">'+
        '<article class="card"><h3>Permit / overhire worker</h3><p>Not a union member. You work the calls a local fills with extra hands when its own members are already booked. You are dispatched on a permit, usually pay a permit or work-dues fee, and are typically paid under the local’s applicable agreement for that call. This is how most people start — it builds hours and relationships without full membership.</p></article>'+
        '<article class="card"><h3>Member</h3><p>A sworn-in member of the local. You pay an initiation fee and ongoing dues, and gain referral standing, voting rights, and access to benefits such as health and pension under the local agreements. Most workers become members after enough permit hours and meeting the local requirements.</p></article>'+
      '</div>'+
      '<h3 class="section-kicker">Other ways in</h3><div class="grid">'+
        '<article class="card"><h3>Apprenticeship &amp; training</h3><p>Some locals and the IATSE Training Trust Fund run skills and safety training — rigging, electrics, audio, and OSHA certifications. Recognized training makes you more callable and can shorten the path to membership.</p></article>'+
        '<article class="card"><h3>Organizing</h3><p>If you already work at a non-union venue, shop, or production company, IATSE can organize that workplace so the whole crew becomes union. Contact the nearest local or IATSE organizing about your workplace.</p></article>'+
        '<article class="card"><h3>Transfer &amp; traveling</h3><p>If you are already a member of one IATSE local and you move or tour, you can often work as a traveling member in another jurisdiction or transfer your membership. Ask both locals about the process.</p></article>'+
        '<article class="card"><h3>Craft guilds</h3><p>Film and TV crafts — camera, editors, art directors, scenic artists, and more — have national locals with their own qualification and roster requirements. Look up the specific guild for that craft.</p></article>'+
      '</div>'+
      '<h3 class="section-kicker">Official IATSE resources</h3><div class="home-links"><a class="btn" href="https://iatse.net/local-union-directory/" target="_blank" rel="noopener">Find your local (official directory) ↗</a><a class="btn" href="https://iatse.net/about/" target="_blank" rel="noopener">About IATSE ↗</a><a class="btn" href="https://iatsetrainingtrust.org/" target="_blank" rel="noopener">IATSE Training Trust ↗</a></div>'+
      '<div class="notice"><b>What to ask a local:</b> Do you keep an available / extra list, and how do I get on it? What is the permit or overhire process? What certifications do you require? When do you accept membership applications?</div>'+
      '<h3 class="section-kicker">Digital dispatch</h3>'+
      '<p class="lead">Many IATSE locals now run calls through dispatch software instead of a phone tree — you get texted or app-notified when a call opens and accept or decline from your phone. Two platforms several locals publicly use are <a href="https://www.callsteward.com/" target="_blank" rel="noopener">Call Steward ↗</a> and <a href="https://unionimpact.com/" target="_blank" rel="noopener">Union Impact ↗</a>; a few locals run their own custom app instead. There is no single system every local uses — ask your local directly which one (if any) they run and how to get set up on it.</p>'+
      '<div class="notice">Know which dispatch system a specific local uses? <a href="contribute.html">Submit it on the Contribute page</a> so this list can eventually show it per local.</div>';
    var pages=Math.max(1,Math.ceil(primary.length/PER_PAGE));if(iatseLocPage>=pages)iatseLocPage=pages-1;if(iatseLocPage<0)iatseLocPage=0;
    var pageLocals=primary.slice(iatseLocPage*PER_PAGE,iatseLocPage*PER_PAGE+PER_PAGE);
    var locPg=pgControls(iatseLocPage,pages,primary.length,PER_PAGE,'iatseLocPageSet');
    var find='<p class="lead">Search by local number, city, state, state abbreviation, craft, district, or organization family in the search box above — or browse all locals below. Queries like <b>local 26</b>, <b>IATSE 26</b>, <b>Grand Rapids MI</b>, and <b>stagehands Michigan</b> are supported.</p>'+
      (q?'<div class="notice">Showing '+matched.length+' result'+(matched.length===1?'':'s')+' for <b>'+esc(q)+'</b>.</div>':'')+
      (primary.length?locPg+'<div class="grid">'+pageLocals.map(iatseCard).join('')+'</div>'+locPg:'')+
      (secondary.length?'<h3 class="section-kicker">National / regional / craft organizations</h3><div class="grid">'+secondary.map(iatseCard).join('')+'</div>':'')+
      (!matched.length?'<p class="sub">No IATSE organizations match your search. Try a local number, city, state, state abbreviation, or craft.</p>':'');
    var districtCards=entries(countBy(all,function(l){return l.district})).map(function(p){return '<article class="card"><h3>'+esc(p[0])+'</h3><p class="sub">'+p[1]+' listed organization'+(p[1]===1?'':'s')+'</p></article>'}).join('');
    var craftCards=entries(countBy(all,iatseFamily)).map(function(p){return '<article class="card"><h3>'+esc(p[0])+'</h3><p class="sub">'+p[1]+' listed organization'+(p[1]===1?'':'s')+'</p></article>'}).join('');
    var about='<div class="grid">'+
        '<article class="card"><h3>IATSE International</h3><p class="sub">'+esc(summary.fullName||'International Alliance of Theatrical Stage Employees')+'</p><p>Founded: '+esc(summary.founded||'1893')+'. Public scope: '+esc(summary.workerCountPublicClaim||'more than 168,000 workers')+'.</p></article>'+
        '<article class="card"><h3>Local unions</h3><p class="sub">Geographic and craft jurisdiction</p><p>'+esc(summary.localUnionPublicClaim||'More than 360 Local Unions in the U.S. and Canada')+'. Verify direct local requirements before outreach.</p></article>'+
        '<article class="card"><h3>Districts</h3><p class="sub">Regional coordination layer</p><p>District labels help sort locals by region; they are not jurisdiction rulings.</p></article>'+
      '</div>'+
      '<div class="stats" style="grid-template-columns:repeat(4,1fr);margin:18px 0">'+stat('listed organizations',all.length)+stat('district / national groups',uniq(all.map(function(l){return l.district})).length)+stat('states / territories',uniq(all.flatMap(function(l){return l.states||[]})).length)+stat('craft families',uniq(all.map(iatseFamily)).length)+'</div>'+
      (families.length?'<h3 class="section-kicker">Organization families</h3><div class="grid">'+families.map(function(f){return '<article class="card"><h3>'+esc(f.label)+'</h3><p>'+esc(f.relevance)+'</p><p class="sub">Search terms: '+esc((f.searchTerms||[]).join(', '))+'</p></article>'}).join('')+'</div>':'')+
      '<h3 class="section-kicker">District / organization coverage</h3><div class="grid">'+districtCards+'</div>'+
      '<h3 class="section-kicker">Craft-family coverage</h3><div class="grid">'+craftCards+'</div>';
    el.innerHTML=
      '<p class="lead">'+esc(summary.workerScope||'IATSE is the union for live theater, concert, film/TV, and trade-show production crews across the U.S. and Canada.')+' Locals are autonomous and each sets its own membership process — there is no single national sign-up.</p>'+
