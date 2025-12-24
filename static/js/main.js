// Smooth Scrolling for all anchor links
document.addEventListener('DOMContentLoaded', function() {
    
    // Smooth scroll for anchor links
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

    // Scroll to top button
    const scrollTopBtn = document.getElementById('scrollTopBtn');
    
    if (scrollTopBtn) {
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                scrollTopBtn.style.display = 'flex';
                scrollTopBtn.style.opacity = '1';
            } else {
                scrollTopBtn.style.opacity = '0';
                setTimeout(() => {
                    if (window.pageYOffset <= 300) {
                        scrollTopBtn.style.display = 'none';
                    }
                }, 300);
            }
        });

        scrollTopBtn.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Fade-in animation on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-visible');
            }
        });
    }, observerOptions);

    // Observe all cards and sections
    document.querySelectorAll('.card, .info-card, .about-card, .news-card, .rocket-card, .timeline-item').forEach(el => {
        el.classList.add('fade-in-element');
        observer.observe(el);
    });

    // Navbar background on scroll
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.style.background = 'rgba(10, 10, 10, 0.95)';
                navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.5)';
            } else {
                navbar.style.background = '#212529';
                navbar.style.boxShadow = 'none';
            }
        });
    }

    // Loading animation for images
    document.querySelectorAll('img').forEach(img => {
        // If image is already loaded (cached), show it immediately
        if (img.complete) {
            img.classList.add('loaded');
            img.style.opacity = '1';
        } else {
            // Otherwise wait for load event
            img.addEventListener('load', function() {
                this.classList.add('loaded');
                this.style.opacity = '1';
            });
            
            // Fallback: show image after 2 seconds even if load event doesn't fire
            setTimeout(() => {
                if (!img.classList.contains('loaded')) {
                    img.classList.add('loaded');
                    img.style.opacity = '1';
                }
            }, 2000);
        }
        
        // Handle image load errors
        img.addEventListener('error', function() {
            this.style.opacity = '1';
            this.classList.add('loaded');
        });
    });

    // Add active class to current page in navbar
    const currentPath = window.location.pathname;
    document.querySelectorAll('.nav-link').forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
});

// Preloader (optional)
window.addEventListener('load', function() {
    const preloader = document.getElementById('preloader');
    if (preloader) {
        setTimeout(() => {
            preloader.style.opacity = '0';
            setTimeout(() => {
                preloader.style.display = 'none';
            }, 300);
        }, 500);
    }
});

// Add hover sound effect (optional, fun addition)
function addHoverEffects() {
    const cards = document.querySelectorAll('.card, .rocket-card, .news-card, .about-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transition = 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)';
        });
    });
}

addHoverEffects();