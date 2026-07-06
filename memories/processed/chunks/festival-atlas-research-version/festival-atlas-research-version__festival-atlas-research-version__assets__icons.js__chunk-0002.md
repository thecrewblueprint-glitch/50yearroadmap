---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__assets__icons.js__chunk-0002",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/assets/icons.js",
  "chunk_index": 2,
  "chunk_count_for_source": 2,
  "char_start": 11362,
  "char_end": 15806,
  "source_sha256": "65f78a0d650234765747d59d30ac11582eeea33ceaf03bf7cdacda5b70aa82b3",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

.body;
    body.insertBefore(div, body.firstChild||null);
  }

  // ── Nav enhancement ──────────────────────────────────────────────────────
  function enhanceNav() {
    var links = document.querySelectorAll('.navInner a');
    for (var i=0;i<links.length;i++) {
      var a = links[i];
      if (a.querySelector('.pa-icon-nav')) continue;
      var href = a.getAttribute('href')||'';
      var iconId = null;
      for (var key in NAV_MAP) {
        if (href.indexOf(key)!==-1) { iconId=NAV_MAP[key]; break; }
      }
      if (!iconId && (href==='/'||href==='./'||href==='.')) iconId='ico-home';
      if (iconId) a.insertBefore(makeIcon(iconId,'pa-icon-nav'), a.firstChild);
    }
  }

  // ── Department heading enhancement ───────────────────────────────────────
  function enhanceDeptHeadings(root) {
    root = root || document;
    var sel = root.querySelectorAll('.branch h4,.pathway h4,.employer-dept-heading');
    for (var i=0;i<sel.length;i++) {
      var h = sel[i];
      if (h.querySelector('.pa-icon-dept')) continue;
      var id = deptIconId(h.textContent||'');
      if (id) h.insertBefore(makeIcon(id,'pa-icon-dept'), h.firstChild);
    }
  }

  // ── External-link indicators ─────────────────────────────────────────────
  function enhanceExternalLinks() {
    var links = document.querySelectorAll(
      '.page a[target="_blank"],.modalbox a[target="_blank"],footer a[target="_blank"]'
    );
    for (var i=0;i<links.length;i++) {
      var a = links[i];
      if (a.querySelector('.pa-icon-ext')) continue;
      if (a.classList.contains('btn')) continue;
      a.appendChild(makeIcon('ico-external','pa-icon-ext'));
    }
  }

  // ── Reset button icon ────────────────────────────────────────────────────
  function enhanceResetBtn() {
    var btns = document.querySelectorAll('#reset');
    for (var i=0;i<btns.length;i++) {
      var btn = btns[i];
      if (btn.querySelector('.pa-icon-btn')) continue;
      btn.insertBefore(makeIcon('ico-reset','pa-icon-btn'), btn.firstChild);
    }
  }

  // ── PWA meta ─────────────────────────────────────────────────────────────
  function addPWAMeta() {
    var head = document.head; if (!head) return;
    var base = (document.querySelector('link[href^="/assets/"]') ? '/' : '');
    if (!document.querySelector('meta[name="theme-color"]')) {
      var m=document.createElement('meta'); m.name='theme-color'; m.content='#f2b705';
      head.appendChild(m);
    }
    if (!document.querySelector('meta[name="mobile-web-app-capable"]')) {
      var ma=document.createElement('meta'); ma.name='mobile-web-app-capable'; ma.content='yes';
      head.appendChild(ma);
    }
    if (!document.querySelector('meta[name="apple-mobile-web-app-capable"]')) {
      var mi=document.createElement('meta'); mi.name='apple-mobile-web-app-capable'; mi.content='yes';
      head.appendChild(mi);
    }
    if (!document.querySelector('meta[name="apple-mobile-web-app-status-bar-style"]')) {
      var ms=document.createElement('meta'); ms.name='apple-mobile-web-app-status-bar-style'; ms.content='black-translucent';
      head.appendChild(ms);
    }
    if (!document.querySelector('link[rel="apple-touch-icon"]')) {
      var l=document.createElement('link'); l.rel='apple-touch-icon'; l.href=base+'favicon.svg';
      head.appendChild(l);
    }
    if (!document.querySelector('link[rel="manifest"]')) {
      var lm=document.createElement('link'); lm.rel='manifest'; lm.href=base+'manifest.json';
      head.appendChild(lm);
    }
  }

  // ── MutationObserver for dynamic content ─────────────────────────────────
  function watchEl(id, fn) {
    var el = document.getElementById(id);
    if (!el||el._paObs) return;
    el._paObs = true;
    var obs = new MutationObserver(function(){ fn(el); });
    obs.observe(el, {childList:true, subtree:true});
  }

  // ── Run ──────────────────────────────────────────────────────────────────
  function run() {
    if (!document.body) return;
    injectStyles();
    injectSprite();
    addPWAMeta();
    enhanceNav();
    enhanceDeptHeadings();
    enhanceExternalLinks();
    enhanceResetBtn();
    watchEl('modalContent', function(el){ enhanceDeptHeadings(el); enhanceExternalLinks(); });
    watchEl('app', function(el){ enhanceDeptHeadings(el); enhanceExternalLinks(); });
  }

  if (document.readyState==='loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
  setTimeout(run, 400);
})();
