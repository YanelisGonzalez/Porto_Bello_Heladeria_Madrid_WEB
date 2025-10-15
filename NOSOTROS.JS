/*

document.addEventListener("DOMContentLoaded", () => {
    const slides = document.querySelectorAll(".slides");
    let current = 0;
    let previous = slides.length - 1;

    // Mostrar primera imagen
    slides[current].classList.add("active");

    setInterval(() => {
        // Oculta la anterior
        slides[previous].classList.remove("active");

        // Avanza índice
        current = (current + 1) % slides.length;

        // Muestra la nueva
        slides[current].classList.add("active");

        // Actualiza índice anterior
        previous = current;
    }, 4000); // 4 segundos por imagen

*/

document.addEventListener("DOMContentLoaded", () => {
  // Carrusel de imágenes
  const slides = document.querySelectorAll(".slides");
  let current = 0;
  let previous = slides.length - 1;

  // Mostrar primera imagen
  slides[current].classList.add("active");

  setInterval(() => {
    slides[previous].classList.remove("active");
    current = (current + 1) % slides.length;
    slides[current].classList.add("active");
    previous = current;
  }, 4000); // 4 segundos por imagen

  // Menú hamburguesa
  const menuToggle = document.querySelector(".menu-toggle");
  const menuContainer = document.querySelector("#Container");

  if (menuToggle && menuContainer) {
    menuToggle.addEventListener("click", () => {
      menuContainer.classList.toggle("active");
    });
  }
});
