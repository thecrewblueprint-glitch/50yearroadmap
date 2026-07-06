---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__assets__employers-department-browser.js__chunk-0002",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/assets/employers-department-browser.js",
  "chunk_index": 2,
  "chunk_count_for_source": 2,
  "char_start": 11275,
  "char_end": 12838,
  "source_sha256": "9efa10c4fd8c5f652fb71190f73cd5623d22783529cad577f03834104e20e382",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

the current filters.</p>';return;}
    var pages=Math.max(1,Math.ceil(filtered.length/EMP_PER_PAGE));
    if(empPage>=pages)empPage=pages-1;if(empPage<0)empPage=0;
    var pageData=filtered.slice(empPage*EMP_PER_PAGE,empPage*EMP_PER_PAGE+EMP_PER_PAGE);
    var pg=empPager(empPage,pages,filtered.length,EMP_PER_PAGE);
    var heading=f.department?'<h3>'+esc(branchName(f.department))+'</h3>':'';
    var ctx=f.department?branchName(f.department):'';
    app.innerHTML=intro+heading+pg+'<div class="grid">'+pageData.map(function(employer){return employerCard(employer,ctx)}).join('')+'</div>'+pg;
  }
  window.empPageSet=function(n){empPage=Number(n)||0;render();var app=$('#app');if(app&&app.scrollIntoView)try{app.scrollIntoView({behavior:'smooth',block:'start'})}catch(e){}};
  function install(){
    var month=$('#monthFilter');
    if(month)month.remove();
    populateFilters();
    render();
    var filtersEl=$('#filters');
    if(filtersEl && !filtersEl.dataset.employerDepartmentBrowser){
      filtersEl.dataset.employerDepartmentBrowser='true';
      filtersEl.addEventListener('input',function(){setTimeout(render,0)},true);
      filtersEl.addEventListener('change',function(){setTimeout(render,0)},true);
      var reset=$('#reset');
      if(reset)reset.onclick=function(){Array.prototype.slice.call(filtersEl.querySelectorAll('input,select')).forEach(function(input){input.value=''});render();};
    }
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',install);else install();
  setTimeout(install,900);
})();
