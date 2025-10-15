document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.slides');
    let currentIndex = 0;

    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.classList.remove('active');
        });
        slides[index].classList.add('active');
    }

    function nextSlide() {
        currentIndex = (currentIndex + 1) % slides.length;
        showSlide(currentIndex);
    }

    showSlide(currentIndex); // Mostrar la primera imagen

    setInterval(nextSlide, 3000); // Cambiar cada 3 segundos
 // ---- Menú hamburguesa ----
    const menuToggle = document.getElementById('menu-toggle');
    const container = document.getElementById('Container');

    if (menuToggle && container) {
        menuToggle.addEventListener('click', () => {
            container.classList.toggle('active');
        });
    }
});
