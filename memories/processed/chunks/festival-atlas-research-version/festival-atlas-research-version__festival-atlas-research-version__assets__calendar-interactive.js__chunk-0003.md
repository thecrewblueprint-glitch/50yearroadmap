---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__assets__calendar-interactive.js__chunk-0003",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/assets/calendar-interactive.js",
  "chunk_index": 3,
  "chunk_count_for_source": 3,
  "char_start": 22759,
  "char_end": 25530,
  "source_sha256": "538e908261a592e17e23d42351d08e042bf13a8416ddd490886ff74da91b0dc6",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

   '.cal-wm-events{padding:0 12px 10px}'+
      '.cal-wm-pill{display:block;width:100%;text-align:left;border-radius:8px;padding:8px 10px;margin:4px 0;cursor:pointer;font-size:.82rem;line-height:1.4;font-family:inherit;background:transparent}'+
      '.cal-wm-pill b{display:block;font-weight:900;margin-bottom:2px}'+
      '.cal-wm-pill span{display:block;font-size:.74rem;opacity:.8}'+
      '.cal-wm-show{border:1px solid rgba(242,183,5,.6);background:rgba(242,183,5,.1);color:#ffd66b}'+
      '.cal-wm-work{border:1px dashed rgba(127,183,255,.5);background:rgba(127,183,255,.08);color:#9dc8ff}'+
      '.cal-wm-empty{opacity:.5}'+
      // Responsive
      '@media(max-width:900px){.cal-app-toolbar{display:block}.cal-control-stack{justify-items:start;margin-top:12px}.calendar-app-frame{min-width:860px}.cal-status{display:block}.cal-status span{display:block;margin:2px 0}.cal-week-row{min-height:174px}}'+
      '@media(max-width:700px){'+
        '.cal-scroll{overflow:visible;border:none;border-radius:0;background:transparent;box-shadow:none}'+
        '.calendar-app-frame{min-width:0}'+
        '.cal-week-event-grid{display:none}'+
        '.cal-week-day-grid{position:relative;inset:auto}'+
        '.cal-week-row{min-height:0;border-bottom:1px solid var(--line)}'+
        '.cal-date-cell{display:flex;flex-direction:column;align-items:center;padding:8px 3px 9px}'+
        '.cal-day-num{min-width:24px;height:24px;font-size:.84rem}'+
        '.cal-dot-count{display:none}'+
        '.cal-ev-dots{display:flex}'+
        '.cal-weekdays>div,.cal-weekdays>button{padding:8px 2px;font-size:.68rem;letter-spacing:0}'+
      '}'+
      '@media(max-width:700px){.cal-nav-arrow{flex:0!important;min-width:0;width:36px;height:36px;padding:0;display:inline-flex;align-items:center;justify-content:center;background:rgba(255,255,255,.06)!important;color:#aeb9c7!important;border:1px solid rgba(255,255,255,.12)!important;border-radius:50%!important;font-size:1.1rem;box-shadow:none!important}}'+
      '@media(max-width:560px){.cal-nav-controls{width:100%;display:flex;align-items:center;gap:8px}.cal-nav-controls .btn:not(.cal-nav-arrow){flex:1}.cal-segment{width:100%}.cal-segment button{flex:1}}';
    document.head.appendChild(style);
  }
  var resizeTimer;
  function onResize(){clearTimeout(resizeTimer);resizeTimer=setTimeout(render,120);}
  function init(){
    installStyles();
    render();
    window.addEventListener('resize',onResize);
    ['input','change'].forEach(function(type){document.addEventListener(type,function(event){if(event.target&&event.target.closest&&event.target.closest('#filters')){state.cursor=null;render();}},true);});
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
