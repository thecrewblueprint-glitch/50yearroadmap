---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__assets__atlas-core-v2.js__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/assets/atlas-core-v2.js",
  "chunk_index": 1,
  "chunk_count_for_source": 5,
  "char_start": 0,
  "char_end": 10501,
  "source_sha256": "f4caf46aede8bbe9400ff19424b9ce38f4855b8cb503f9804489636241a13d06",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

(function(){
  var MONTHS=['January','February','March','April','May','June','July','August','September','October','November','December'];
  var SHORT_MONTHS=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  var branchFiles=[];
  var branches=[];
  var allOpportunities=[];
  var opportunities=[];
  var employers=[];
  var iatseLocals=[];
  var branchIndex={records:[],byKey:{}};
  var branchDataReady=false;
  var SCH_KEY='production-atlas-schedule-v1';
  var UNKNOWN_PRODUCER='__unknown_promoter__';
  var STATE_ABBR={'Alabama':'AL','Alaska':'AK','Arizona':'AZ','Arkansas':'AR','California':'CA','Colorado':'CO','Connecticut':'CT','Delaware':'DE','District of Columbia':'DC','Florida':'FL','Georgia':'GA','Hawaii':'HI','Idaho':'ID','Illinois':'IL','Indiana':'IN','Iowa':'IA','Kansas':'KS','Kentucky':'KY','Louisiana':'LA','Maine':'ME','Maryland':'MD','Massachusetts':'MA','Michigan':'MI','Minnesota':'MN','Mississippi':'MS','Missouri':'MO','Montana':'MT','Nebraska':'NE','Nevada':'NV','New Hampshire':'NH','New Jersey':'NJ','New Mexico':'NM','New York':'NY','North Carolina':'NC','North Dakota':'ND','Ohio':'OH','Oklahoma':'OK','Oregon':'OR','Pennsylvania':'PA','Rhode Island':'RI','South Carolina':'SC','South Dakota':'SD','Tennessee':'TN','Texas':'TX','Utah':'UT','Vermont':'VT','Virginia':'VA','Washington':'WA','West Virginia':'WV','Wisconsin':'WI','Wyoming':'WY','Puerto Rico':'PR','U.S. Virgin Islands':'VI'};

  function $(selector){return document.querySelector(selector)}
  function $$(selector){return Array.prototype.slice.call(document.querySelectorAll(selector))}
  function esc(value){return String(value==null?'':value).replace(/[&<>'"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]})}
  function norm(value){return String(value||'').toLowerCase().replace(/&/g,'and').replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,'')}
  function normSearch(value){return String(value||'').toLowerCase().replace(/&/g,'and').replace(/[^a-z0-9]+/g,' ').replace(/\s+/g,' ').trim()}
  function searchMatch(haystack,query){var q=normSearch(query);if(!q)return true;var hay=' '+normSearch(haystack)+' ';if(hay.indexOf(' '+q+' ')>-1||hay.indexOf(q)>-1)return true;return q.split(' ').filter(Boolean).every(function(part){return hay.indexOf(' '+part+' ')>-1||hay.indexOf(part)>-1})}
  function text(obj){return JSON.stringify(obj||{}).toLowerCase()}
  function uniq(items){return Array.from(new Set(items||[])).filter(Boolean).sort()}
  function safeUrl(url){return url && /^https?:\/\//i.test(url) ? url : ''}
  function plainLink(label,url){var safe=safeUrl(url);return safe?'<a href="'+esc(safe)+'" target="_blank" rel="noopener" onclick="event.stopPropagation()">'+esc(label)+' ↗</a>':esc(label)}
  function debounce(fn,ms){var timer;return function(){var args=arguments,self=this;clearTimeout(timer);timer=setTimeout(function(){fn.apply(self,args)},ms)}}
  function parseDate(str){if(!str)return null;var d=new Date(String(str)+'T00:00:00');return isNaN(d.getTime())?null:d}
  function dateMs(str){var d=parseDate(str);return d?d.getTime():null}
  function inferredStartMs(o){var exact=dateMs(o&&o.startDate);if(exact!=null)return exact;var month=Number((o||{}).month||0);if(month>=1&&month<=12){var year=Number((o||{}).publicCycleYear||(o||{}).eventYear||2026);return new Date(year,month-1,1).getTime()}return Number.MAX_SAFE_INTEGER}
  function fmtShort(d,withYear){if(!d)return '';return SHORT_MONTHS[d.getMonth()]+' '+d.getDate()+(withYear?', '+d.getFullYear():'')}
  function festivalDates(o){var s=parseDate(o.startDate),e=parseDate(o.endDate);if(!s)return '';if(!e||e.getTime()===s.getTime())return fmtShort(s,true);return fmtShort(s,false)+' – '+fmtShort(e,true)}
  function productionWindow(o){var s=parseDate(o.startDate);if(!s)return '';var e=parseDate(o.endDate)||s;var big=(o.departments||[]).length>=9;var build=new Date(s.getTime()-(big?9:4)*86400000);var strike=new Date(e.getTime()+(big?3:2)*86400000);return fmtShort(build,false)+' – '+fmtShort(strike,true)}
  function sortOpportunities(list){return (list||[]).slice().sort(function(a,b){var ad=inferredStartMs(a),bd=inferredStartMs(b);if(ad!==bd)return ad-bd;var d=(b.longTermValueScore||0)-(a.longTermValueScore||0);if(d)return d;return String(a.name||'').localeCompare(String(b.name||''))})}

  function getSchedule(){try{return JSON.parse(localStorage.getItem(SCH_KEY)||'[]')}catch(e){return []}}
  function saveSchedule(ids){try{localStorage.setItem(SCH_KEY,JSON.stringify(ids))}catch(e){}}
  window.addGig=function(id){var s=getSchedule();if(s.indexOf(id)<0)s.push(id);saveSchedule(s);renderPage()};
  window.removeGig=function(id){saveSchedule(getSchedule().filter(function(x){return x!==id}));renderPage()};
  window.clearSchedule=function(){saveSchedule([]);renderPage()};

  function branchName(id){var b=branches.find(function(x){return x.id===id});return b?b.name:id}
  function bestLink(e){var links=e.links||{};return links.apply||links.careers||links.contact||links.directory||links.homepage||''}
  function knownProducer(o){var name=String(((o.producer||{}).name)||'').trim();if(!name)return '';var low=name.toLowerCase();if(low.indexOf('verify')>-1||low==='unknown'||low==='tbd')return '';return name.replace(/\s*[,/]?\s*verify.*$/i,'').replace(/\s*\/\s*partners$/i,'').trim()}
  function producerKey(o){return knownProducer(o)||UNKNOWN_PRODUCER}
  function branchSummary(o,limit){var names=(o.departments||[]).map(branchName);var shown=names.slice(0,limit||4);var extra=Math.max(0,names.length-shown.length);return esc(shown.join(' · ')+(extra?' +'+extra+' more':''))}
  function employerById(id){return employers.find(function(e){return e.id===id})}
  function matchingEmployers(branchId){return employers.filter(function(e){return (e.departments||[]).includes(branchId)})}
  function matchingOpportunities(branchId){return opportunities.filter(function(o){return (o.departments||[]).includes(branchId)})}
  function employerRow(e){var links=e.links||{};var url=links.apply||links.careers||links.contact||links.directory||links.homepage||'';var label=(links.apply||links.careers)?'Apply / careers':'Website / contact';var type=e.type?'<span class="sub" style="font-size:.74rem">'+esc(e.type)+'</span><br>':'';return '<li style="margin:0 0 9px;list-style:none"><b>'+esc(e.name)+'</b><br>'+type+plainLink(label,url)+'</li>'}

  function loadScript(src){return new Promise(function(resolve){if($('script[data-loader="'+src+'"]'))return resolve();var s=document.createElement('script');s.src=src;s.async=false;s.dataset.loader=src;s.onload=resolve;s.onerror=function(){console.warn('Could not load',src);resolve()};document.head.appendChild(s)})}
  function loadBranchManifest(){return loadScript('data/packages/branch-research-manifest.js?v=manifest2').then(function(){if(Array.isArray(window.BRANCH_RESEARCH_MANIFEST)&&window.BRANCH_RESEARCH_MANIFEST.length)branchFiles=window.BRANCH_RESEARCH_MANIFEST.slice()})}
  var _branchResearchPromise=null;
  function ensureBranchResearch(){if(_branchResearchPromise)return _branchResearchPromise;_branchResearchPromise=loadBranchManifest().then(function(){return Promise.all(branchFiles.map(function(file){return loadScript('data/packages/'+file+'?v=manifest2')}))}).then(buildBranchIndex);return _branchResearchPromise}
  function buildBranchIndex(){var records=[];Object.keys(window).forEach(function(key){if(!/^OPPORTUNITY_BRANCH_RESEARCH_BATCH_/.test(key))return;var ds=window[key];if(!ds||!Array.isArray(ds.targets))return;ds.targets.forEach(function(t){records.push(Object.assign({},t,{branchId:t.branchId||ds.branchId,branchName:t.branchName||ds.branchName,batchId:ds.batchId,datasetKey:key}))})});branchIndex={records:records,byKey:{}};records.forEach(function(r){branchIndex.byKey[norm(r.opportunityId)+'::'+r.branchId]=r;branchIndex.byKey[norm(r.opportunityName)+'::'+r.branchId]=r});branchDataReady=true}
  function classify(o){var hasSource=!!o.active2026SourceUrl;var copy=Object.assign({},o);copy.intelligence=Object.assign({publicSources:hasSource?[{label:'active status source',url:o.active2026SourceUrl}]:[]},o.intelligence||{});return copy}
  function findBranchRecord(o,branchId){return branchIndex.byKey[norm(o.id)+'::'+branchId]||branchIndex.byKey[norm(o.name)+'::'+branchId]||null}

  function filterValues(){return {q:(($('#q')||{}).value||'').trim().toLowerCase(),branch:(($('#branchFilter')||{}).value||''),region:(($('#regionFilter')||{}).value||''),month:(($('#monthFilter')||{}).value||''),type:(($('#employerTypeFilter')||{}).value||''),state:(($('#stateFilter')||{}).value||''),producer:(($('#producerFilter')||{}).value||''),festival:(($('#festivalFilter')||{}).value||''),employer:(($('#employerFilter')||{}).value||'')}}
  var SAVED_KEY='atlas_saved_opportunities';
  function getSavedIds(){try{var raw=JSON.parse(localStorage.getItem(SAVED_KEY)||'[]');return Array.isArray(raw)?raw:[]}catch(e){return []}}
  function isSaved(id){return getSavedIds().indexOf(id)>-1}
  function setSavedIds(arr){try{localStorage.setItem(SAVED_KEY,JSON.stringify(arr))}catch(e){}}
  window.toggleOppSave=function(id,evt){if(evt&&evt.stopPropagation)evt.stopPropagation();var arr=getSavedIds();var i=arr.indexOf(id);if(i>-1)arr.splice(i,1);else arr.push(id);setSavedIds(arr);renderPage()};
  function savedOnlyActive(){var b=$('#savedOnly');return !!(b&&b.getAttribute('aria-pressed')==='true')}
  window.toggleSavedOnly=function(){var b=$('#savedOnly');if(!b)return;var active=b.getAttribute('aria-pressed')==='true';b.setAttribute('aria-pressed',String(!active));b.classList.toggle('active',!active);b.textContent=(!active?'★ Saved':'☆ Saved');renderPage()};
  function oppHay(o){return String([o.name,o.city,o.state,o.venue,knownProducer(o),(o.departments||[]).map(branchName).join(' ')].join(' ')).toLowerCase()}
  function activeOpportunities(){var f=filterValues();var savedOnly=savedOnlyActive();return sortOpportunities(opportunities.filter(function(o){return (!f.q||searchMatch(oppHay(o),f.q))&&(!f.branch||(o.departments||[]).includes(f.branch))&&(!f.region||o.region===f.region)&&(!f.month||String(o.month)===f.month)&&(!f.state||o.state===f.state)&&(!f.producer||producerKey(o)===f.producer)&&(!savedOnly||isSaved(o.id))}))}
  function activeLocals(){var f=filterValues();return iatseLocals.filter(function(l){return (!f.q||searchMatch(iatseText(l),f.q))&&(!f.region||String(l.jurisdiction||'').includes(f.region)||String(l.states||'').includes(f.region)||l.district===f.region)})}

