$(function () {
    initTopSwiper();

    initMeunSwiper();
})


function initTopSwiper() {
    var swiper = new Swiper("#topSwiper", {
        loop: true,
        pagination: '.swiper-pagination',
        autoloop: 4000
    })

}


function initMeunSwiper() {
    var swiper = new Swiper("#swiperMenu", {
        slidesPerView: 3
    })

}