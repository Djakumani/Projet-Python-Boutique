document.addEventListener('DOMContentLoaded', () => {

    // carrousel hero
    const hero = document.querySelector('.hero-carousel');
    if (hero) {
        const slides = hero.querySelectorAll('.hero-slide');
        const indicators = hero.querySelectorAll('.hero-indicator');
        let currentSlide = 0;
        let autoplay;

        function goToSlide(index) {
            currentSlide = index;
            hero.querySelector('.hero-track').style.transform = `translateY(-${index * 100}%)`;
            indicators.forEach((ind, i) => {
                ind.classList.toggle('active', i === index);
            });
        }

        function nextSlide() {
            const next = (currentSlide + 1) % slides.length;
            goToSlide(next);
        }

        function startAutoplay() {
            autoplay = setInterval(nextSlide, 4000); // change toutes les 4s
        }

        function stopAutoplay() {
            clearInterval(autoplay);
        }

        // on peut cliquer sur les petits ronds
        indicators.forEach((ind, i) => {
            ind.addEventListener('click', () => {
                goToSlide(i);
                stopAutoplay();
                startAutoplay();
            });
        });

        // gestion du swipe sur mobile
        let touchStartY = 0;
        hero.addEventListener('touchstart', (e) => {
            touchStartY = e.touches[0].clientY;
            stopAutoplay();
        }, { passive: true });

        hero.addEventListener('touchend', (e) => {
            const diff = touchStartY - e.changedTouches[0].clientY;
            if (Math.abs(diff) > 50) {
                if (diff > 0 && currentSlide < slides.length - 1) {
                    goToSlide(currentSlide + 1);
                } else if (diff < 0 && currentSlide > 0) {
                    goToSlide(currentSlide - 1);
                }
            }
            startAutoplay();
        }, { passive: true });

        // pause quand la souris est dessus
        hero.addEventListener('mouseenter', stopAutoplay);
        hero.addEventListener('mouseleave', startAutoplay);

        startAutoplay();
    }


    // zoom sur les images produits au hover
    document.querySelectorAll('.product-card').forEach(card => {
        const imageContainer = card.querySelector('.product-card-image');
        const img = imageContainer ? imageContainer.querySelector('img') : null;

        if (img) {
            card.addEventListener('mouseenter', () => {
                img.style.transform = 'scale(1.08)';
            });
            card.addEventListener('mouseleave', () => {
                img.style.transform = 'scale(1)';
            });
        }
    });


    // animation d'apparition quand on scrolle
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -40px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // chaque carte apparait avec un petit delai
    document.querySelectorAll('.product-card').forEach((card, index) => {
        card.classList.add('animate-on-scroll');
        card.style.transitionDelay = `${index * 0.1}s`;
        observer.observe(card);
    });

    document.querySelectorAll('.products-section h2, .purchase-page, .form-card, .admin-table-container, .confirm-card').forEach(el => {
        el.classList.add('animate-on-scroll');
        observer.observe(el);
    });


    // animation du bouton acheter
    const buyForm = document.querySelector('.purchase-form');
    if (buyForm) {
        buyForm.addEventListener('submit', function (e) {
            const btn = this.querySelector('.btn-red');
            if (!btn || btn.classList.contains('btn-loading')) return;

            btn.classList.add('btn-loading');
            btn.innerHTML = '<span class="spinner"></span> Traitement...';
            // le formulaire se soumet normalement, django gere la suite
        });
    }

    // petit effet ripple sur les boutons ajouter au panier
    document.querySelectorAll('.product-card-action .btn-primary').forEach(btn => {
        btn.addEventListener('click', function (e) {
            const ripple = document.createElement('span');
            ripple.classList.add('btn-ripple');
            const rect = this.getBoundingClientRect();
            ripple.style.left = `${e.clientX - rect.left}px`;
            ripple.style.top = `${e.clientY - rect.top}px`;
            this.appendChild(ripple);
            setTimeout(() => ripple.remove(), 600);
        });
    });


    // fermer les alertes
    document.querySelectorAll('.alert-close').forEach(btn => {
        btn.addEventListener('click', function () {
            const alert = this.parentElement;
            alert.style.opacity = '0';
            alert.style.transform = 'translateY(-10px)';
            setTimeout(() => alert.remove(), 300);
        });
    });

    // les alertes disparaissent toutes seules apres 5s
    document.querySelectorAll('.alert').forEach(alert => {
        setTimeout(() => {
            if (alert.parentElement) {
                alert.style.opacity = '0';
                alert.style.transform = 'translateY(-10px)';
                setTimeout(() => alert.remove(), 300);
            }
        }, 5000);
    });

});
