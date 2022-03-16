var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 30,
    loop: true,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
      },

    breakpoints: {
        // when window width is >= 768px
        768:{
            slidesPerView: 2,
            spaceBetweenSlides: 30
        },
        // when window width is >= 1440px
        1440:{
            slidesPerView: 3,
            spaceBetweenSlides: 30
        },
    },

    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});

