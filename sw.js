const CACHE_NAME = "simple-pwa-cache-v2"; // bump version on updates
const urlsToCache = [
  "/ErVijayRaghuwanshi/",
  "/ErVijayRaghuwanshi/index.html", 
  "/ErVijayRaghuwanshi/manifest.json", 
  "/ErVijayRaghuwanshi/sw.js",
  "/ErVijayRaghuwanshi/script.js", 
  "/ErVijayRaghuwanshi/style.css",
  "/ErVijayRaghuwanshi/assets/profile.jpeg",
  "/ErVijayRaghuwanshi/assets/Vijay_Raghuwanshi_Resume.pdf",
  "/ErVijayRaghuwanshi/assets/screenshots/desktop.png",
  "/ErVijayRaghuwanshi/assets/icon-32x32.png", 
  "/ErVijayRaghuwanshi/assets/icon-48x48.png",
  "/ErVijayRaghuwanshi/assets/icon-72x72.png",
  "/ErVijayRaghuwanshi/assets/icon-96x96.png", 
  "/ErVijayRaghuwanshi/assets/icon-144x144.png",
  "/ErVijayRaghuwanshi/assets/icon-152x152.png",
  "/ErVijayRaghuwanshi/assets/icon-128x128.png",
  "/ErVijayRaghuwanshi/assets/icon-192x192.png",
];

// Install → cache assets
self.addEventListener("install", event => {
  console.log("Service Worker installing...");
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(urlsToCache))
  );
  self.skipWaiting(); // activate immediately
});

self.addEventListener("message", event => {
  if (event.data.action === "skipWaiting") {
    self.skipWaiting();
  }
});


// Activate → remove old caches
self.addEventListener("activate", event => {
  console.log("Service Worker activating...");
  event.waitUntil(
    self.clients.claim().then(() => {
      return self.clients.matchAll({ type: "window" }).then(clients => {
        clients.forEach(client => client.navigate(client.url));
      });
    }),
    caches.keys().then(keys =>
      Promise.all(
        keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key))
      )
    )
  );
  return self.clients.claim();
});

// Fetch → network-first for HTML, cache-first for others
self.addEventListener("fetch", event => {
  if (event.request.mode === "navigate") {
    // Always try network first for HTML
    event.respondWith(
      fetch(event.request).catch(() => caches.match("/ErVijayRaghuwanshi/index.html"))
    );
  } else {
    // Cache-first for static files
    event.respondWith(
      caches.match(event.request).then(res => res || fetch(event.request))
    );
  }
});
