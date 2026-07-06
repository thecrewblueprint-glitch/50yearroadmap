---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__sw.js__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/sw.js",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 2803,
  "source_sha256": "88fdf8239d68cc166be991dfe7623bf260bcbaab17d15494accb90102e0f7520",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

// Bump CACHE_VERSION whenever the precached list below changes.
var CACHE_VERSION = 'atlas-shell-v3';

var PRECACHE = [
  '/',
  '/index.html',
  '/manifest.json',
  '/favicon.svg',
  '/assets/icons/icon-192.png',
  '/assets/icons/icon-512.png',
  '/assets/atlas.css?v=atlas7',
  '/assets/atlas-core-v2.js?v=multi30',
  '/assets/site-footer.js?v=footer14',
  '/assets/icons.js?v=icons1'
];

var OFFLINE_HTML = '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Offline — Production Atlas</title></head><body><main><h1>You are offline</h1><p>This page has not been saved for offline use yet. Reconnect and try again.</p><p><a href="/">Back to Home</a></p></main></body></html>';

self.addEventListener('install', function(evt) {
  evt.waitUntil(
    caches.open(CACHE_VERSION)
      .then(function(cache) {
        return Promise.all(
          PRECACHE.map(function(url) {
            return cache.add(url).catch(function() {});
          })
        );
      })
      .then(function() {
        return self.skipWaiting();
      })
  );
});

self.addEventListener('activate', function(evt) {
  evt.waitUntil(
    caches.keys()
      .then(function(keys) {
        return Promise.all(
          keys
            .filter(function(k) {
              return k !== CACHE_VERSION;
            })
            .map(function(k) {
              return caches.delete(k);
            })
        );
      })
      .then(function() {
        return self.clients.claim();
      })
  );
});

self.addEventListener('fetch', function(evt) {
  var req = evt.request;
  if (req.method !== 'GET') return;

  var url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  if (req.mode === 'navigate' || req.destination === 'document') {
    evt.respondWith(
      fetch(req)
        .then(function(res) {
          var copy = res.clone();
          caches.open(CACHE_VERSION).then(function(cache) {
            cache.put(req, copy);
          });
          return res;
        })
        .catch(function() {
          return caches.match(req).then(function(cached) {
            return cached || caches.match('/index.html').then(function(idx) {
              return idx || new Response(OFFLINE_HTML, {
                headers: { 'Content-Type': 'text/html; charset=utf-8' }
              });
            });
          });
        })
    );
    return;
  }

  evt.respondWith(
    caches.match(req).then(function(cached) {
      if (cached) return cached;

      return fetch(req).then(function(res) {
        if (res && res.status === 200) {
          var copy = res.clone();
          caches.open(CACHE_VERSION).then(function(cache) {
            cache.put(req, copy);
          });
        }
        return res;
      }).catch(function() {
        return cached;
      });
    })
  );
});
