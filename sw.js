const CACHE_NAME = "simple-pwa-cache-v1";
const urlsToCache = [
  "ErVijayRaghuwanshi/",
  "ErVijayRaghuwanshi/index.html", 
  "ErVijayRaghuwanshi/manifest.json", 
  "ErVijayRaghuwanshi/sw.js",
  "ErVijayRaghuwanshi/script.js", 
  "ErVijayRaghuwanshi/style.css",
  "ErVijayRaghuwanshi/assets/profile.jpeg",
  "ErVijayRaghuwanshi/assets/Vijay_Raghuwanshi_Resume.pdf",
  "ErVijayRaghuwanshi/assets/screenshots/desktop.png",
  "ErVijayRaghuwanshi/assets/icon-32x32.png", 
  "ErVijayRaghuwanshi/assets/icon-48x48.png",
  "ErVijayRaghuwanshi/assets/icon-72x72.png",
  "ErVijayRaghuwanshi/assets/icon-96x96.png", 
  "ErVijayRaghuwanshi/assets/icon-144x144.png",
  "ErVijayRaghuwanshi/assets/icon-152x152.png",
  "ErVijayRaghuwanshi/assets/icon-128x128.png",
  "ErVijayRaghuwanshi/assets/icon-192x192.png",
];

self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener("fetch", event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});
