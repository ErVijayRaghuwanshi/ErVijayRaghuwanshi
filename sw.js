const CACHE_NAME = 'vr-portfolio-v2';
const urlsToCache = [
    '/ErVijayRaghuwanshi/',
    '/ErVijayRaghuwanshi/index.html',
    '/ErVijayRaghuwanshi/styles.css',
    '/ErVijayRaghuwanshi/script.js',
    '/ErVijayRaghuwanshi/manifest.json',
    '/ErVijayRaghuwanshi/assets/profile.jpeg',
    '/ErVijayRaghuwanshi/assets/Vijay_Raghuwanshi_Resume.pdf',
    'https://cdn.tailwindcss.com',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css',
    'https://unpkg.com/aos@next/dist/aos.css',
    'https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.css',
    'https://unpkg.com/aos@next/dist/aos.js',
    'https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js'
];

// Add offline fallback
const offlinePage = '/ErVijayRaghuwanshi/offline.html';
urlsToCache.push(offlinePage);

// Install Service Worker
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                console.log('Opened cache');
                return cache.addAll(urlsToCache);
            })
    );
});

// Activate Service Worker
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (cacheName !== CACHE_NAME) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});

// Fetch Event
self.addEventListener('fetch', event => {
    if (event.request.mode === 'navigate') {
        event.respondWith(
            fetch(event.request).catch(() => {
                return caches.match(offlinePage);
            })
        );
        return;
    }

    const url = new URL(event.request.url);
    if (url.origin === location.origin) {
        event.respondWith(
            caches.match(event.request)
                .then(response => {
                    // Return cached version or fetch new
                    return response || fetch(event.request)
                        .then(response => {
                            // Check if we received a valid response
                            if (!response || response.status !== 200 || response.type !== 'basic') {
                                return response;
                            }

                            // Clone the response
                            const responseToCache = response.clone();

                            caches.open(CACHE_NAME)
                                .then(cache => {
                                    cache.put(event.request, responseToCache);
                                });

                            return response;
                        });
                })
        );
    }
});