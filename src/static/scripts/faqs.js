$(document).ready(function() {
  $('.faq-header').on('click', function() {
    // Al hacer clic en el div .faq-header, obtenemos el párrafo hermano
    var paragraph = $(this).next('p');

    // Rotamos el icono usando la clase .rotate-icon
    $(this).find('.box-icon').toggleClass('rotate-icon');

    // Si hay un párrafo abierto previamente y no es el mismo que el que se hizo clic, se cierra
    $('.faq-header').not(this).find('.box-icon').removeClass('rotate-icon');
    $('.faq-header').not(this).next('p').slideUp();

    // Mostramos el párrafo del elemento actual
    paragraph.slideToggle();
  });
});
