

// Initialize AOS (Animate On Scroll)
AOS.init({
    duration: 600,
    offset: 100,
    once: true
});

// Initialize Particles.js
particlesJS('particles-js', {
    particles: {
        number: {
            value: 80,
            density: {
                enable: true,
                value_area: 800
            }
        },
        color: {
            value: '#2563eb'
        },
        shape: {
            type: 'circle'
        },
        opacity: {
            value: 0.5,
            random: false
        },
        size: {
            value: 3,
            random: true
        },
        line_linked: {
            enable: true,
            distance: 150,
            color: '#2563eb',
            opacity: 0.2,
            width: 1
        },
        move: {
            enable: true,
            speed: 2,
            direction: 'none',
            random: false,
            straight: false,
            out_mode: 'out',
            bounce: false
        }
    },
    interactivity: {
        detect_on: 'canvas',
        events: {
            onhover: {
                enable: true,
                mode: 'grab'
            },
            onclick: {
                enable: true,
                mode: 'push'
            },
            resize: true
        },
        modes: {
            grab: {
                distance: 140,
                line_linked: {
                    opacity: 0.5
                }
            },
            push: {
                particles_nb: 4
            }
        }
    },
    retina_detect: true
});

// Dark Mode Toggle
// const darkModeToggle = document.getElementById('darkModeToggle');
// const html = document.documentElement;

// Check for saved dark mode preference
// const darkMode = localStorage.getItem('darkMode') === 'true';
// if (darkMode) {
//     html.classList.add('dark');
// }

// darkModeToggle.addEventListener('click', () => {
//     html.classList.toggle('dark');
//     localStorage.setItem('darkMode', html.classList.contains('dark'));
// });

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add fade-in animation to sections when they come into view
const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
};

const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('fade-in');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe all sections
document.querySelectorAll('section').forEach(section => {
    observer.observe(section);
});

// Add active state to navigation links based on scroll position
const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('nav a');

window.addEventListener('scroll', () => {
    let current = '';

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= sectionTop - 60) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('text-blue-600', 'dark:text-blue-400',);
        if (link.getAttribute('href').slice(1) === current) {
            link.classList.add('text-blue-600', 'dark:text-blue-400');
        }
    });
});

// Loading Animation
window.addEventListener('load', () => {
    const loader = document.querySelector('.loading');
    if (loader) {
        loader.style.opacity = '0';
        setTimeout(() => {
            loader.style.display = 'none';
        }, 300);
    }
});

// Parallax Effect for Hero Section
window.addEventListener('scroll', () => {
    const hero = document.querySelector('.hero-section');
    if (hero) {
        const scrolled = window.pageYOffset;
        hero.style.transform = `translateY(${scrolled * 0.5}px)`;
    }
});

// Typing Animation for Hero Text
const heroText = document.querySelector('.hero-text');
if (heroText) {
    const text = heroText.textContent;
    heroText.textContent = '';
    let i = 0;

    function typeWriter() {
        if (i < text.length) {
            heroText.textContent += text.charAt(i);
            i++;
            setTimeout(typeWriter, 100);
        }
    }

    typeWriter();
}

// Add hover effect to skill badges
// document.querySelectorAll('.skill-badge').forEach(badge => {
//     badge.addEventListener('mouseenter', () => {
//         badge.style.transform = 'translateY(-2px)';
//     });
//     badge.addEventListener('mouseleave', () => {
//         badge.style.transform = 'translateY(0)';
//     });
// });

// Add hover effect to project cards
// document.querySelectorAll('.project-card').forEach(card => {
//     card.addEventListener('mouseenter', () => {
//         card.style.transform = 'translateY(-5px)';
//     });
//     card.addEventListener('mouseleave', () => {
//         card.style.transform = 'translateY(0)';
//     });
// });

// Add hover effect to contact links
// document.querySelectorAll('.contact-link').forEach(link => {
//     link.addEventListener('mouseenter', () => {
//         link.style.transform = 'translateY(-3px)';
//     });
//     link.addEventListener('mouseleave', () => {
//         link.style.transform = 'translateY(0)';
//     });
// });

// Theme Management
const themes = ['theme-purple', 'theme-green', 'theme-red', 'theme-orange'];
let currentThemeIndex = 0;

// Function to set theme
function setTheme(themeName) {
    // Remove all theme classes
    themes.forEach(theme => document.body.classList.remove(theme));
    // Add the new theme class
    document.body.classList.add(themeName);
    // Update particles color
    updateParticlesColor();
    // Save theme preference
    localStorage.setItem('theme', themeName);
}

// Function to update particles color based on current theme
function updateParticlesColor() {
    const computedStyle = getComputedStyle(document.body);
    const primaryColor = computedStyle.getPropertyValue('--theme-primary').trim();

    particlesJS('particles-js', {
        particles: {
            number: {
                value: 80,
                density: {
                    enable: true,
                    value_area: 800
                }
            },
            color: {
                value: primaryColor
            },
            shape: {
                type: 'circle'
            },
            opacity: {
                value: 0.5,
                random: false
            },
            size: {
                value: 3,
                random: true
            },
            line_linked: {
                enable: true,
                distance: 150,
                color: primaryColor,
                opacity: 0.2,
                width: 1
            },
            move: {
                enable: true,
                speed: 2,
                direction: 'none',
                random: false,
                straight: false,
                out_mode: 'out',
                bounce: false
            }
        },
        interactivity: {
            detect_on: 'canvas',
            events: {
                onhover: {
                    enable: true,
                    mode: 'grab'
                },
                onclick: {
                    enable: true,
                    mode: 'push'
                },
                resize: true
            },
            modes: {
                grab: {
                    distance: 140,
                    line_linked: {
                        opacity: 0.5
                    }
                },
                push: {
                    particles_nb: 4
                }
            }
        },
        retina_detect: true
    });
}

// // Theme toggle event listener
// document.getElementById('themeToggle').addEventListener('click', () => {
//     currentThemeIndex = (currentThemeIndex + 1) % themes.length;
//     setTheme(themes[currentThemeIndex]);
// });

// Load saved theme preference
const savedTheme = localStorage.getItem('theme');
if (savedTheme && themes.includes(savedTheme)) {
    currentThemeIndex = themes.indexOf(savedTheme);
    setTheme(savedTheme);
}


// // Mobile menu toggle
// const menuToggle = document.getElementById("menuToggle");
// const mobileMenu = document.getElementById("mobileMenu");

// menuToggle.addEventListener("click", () => {
//   mobileMenu.classList.toggle("hidden");

//   // Switch hamburger <-> close icon
//   const icon = menuToggle.querySelector("i");
//   icon.classList.toggle("fa-bars");
//   icon.classList.toggle("fa-times");
// });


const menuToggle = document.getElementById("menuToggle");
const mobileMenu = document.getElementById("mobileMenu");
const mobileLinks = mobileMenu.querySelectorAll("a");

function toggleMenu() {
    if (mobileMenu.classList.contains("max-h-0")) {
        // Open menu
        mobileMenu.classList.remove("max-h-0");
        mobileMenu.classList.add("max-h-96"); // adjust depending on menu height
    } else {
        // Close menu
        mobileMenu.classList.add("max-h-0");
        mobileMenu.classList.remove("max-h-96");
    }

    // Toggle icon (hamburger <-> X)
    const icon = menuToggle.querySelector("i");
    icon.classList.toggle("fa-bars");
    icon.classList.toggle("fa-times");
}

menuToggle.addEventListener("click", toggleMenu);

// Close menu when a link is clicked
mobileLinks.forEach(link => {
    link.addEventListener("click", () => {
        if (!mobileMenu.classList.contains("max-h-0")) {
            toggleMenu();
        }
    });
});





if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("/ErVijayRaghuwanshi/sw.js").then(reg => {
        // Listen for updates
        reg.addEventListener("updatefound", () => {
            const newWorker = reg.installing;
            newWorker.addEventListener("statechange", () => {
                if (newWorker.state === "installed" && navigator.serviceWorker.controller) {
                    // New version available
                    showUpdateToast(newWorker);
                }
            });
        });
    });
}




// leetcode stats update
async function loadLeetCodeStats() {
    try {
        const res = await fetch("https://leetcode-stats-api.herokuapp.com/ervijayraghuwanshi");
        const data = await res.json();

        // Update stats dynamically
        document.getElementById("totalSolved").textContent = `${data.totalSolved} / ${data.totalQuestions}`;
        document.getElementById("easySolved").textContent = data.easySolved;
        document.getElementById("mediumSolved").textContent = data.mediumSolved;
        document.getElementById("hardSolved").textContent = data.hardSolved;

    } catch (error) {
        console.error("Error fetching LeetCode stats:", error);
    }
}

loadLeetCodeStats();

// JavaScript for keyboard shortcuts

document.addEventListener("keydown", (e) => {
    // Ignore typing in input fields
    if (["INPUT", "TEXTAREA"].includes(document.activeElement.tagName)) return;

    const key = e.key.toUpperCase();
    const link = document.querySelector(`.nav-link[data-key="${key}"]`);
    if (link) {
        link.click(); // simulate click
        e.preventDefault(); // prevent default behavior
    }
});


let altPressed = false;

document.addEventListener('keydown', (e) => {
    if (e.key === "Alt") {
        altPressed = true;
        document.body.classList.add("show-keytips");
    }
});

document.addEventListener('keyup', (e) => {
    if (e.key === "Alt") {
        altPressed = false;
        document.body.classList.remove("show-keytips");
    }
});



