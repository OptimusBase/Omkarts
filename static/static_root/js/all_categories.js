  $(document).ready(function() {




    var product_slider = $(".owl-carousel");

    product_slider.owlCarousel({
      rewindNav : false,
      pagination : false,
      // items : 2,
      loop: false,
      responsiveClass: true,
      // margin: 20,
      slideBy: 2,
      dotsEach: true,
      lazyLoad: false,
      responsive:{
          0:{ 
              // center: true,
              // stagePadding: 10,
              loop: true,
              items: 1, // display 2 items in small device
          },
          480:{
              // center: true,
              // stagePadding: 10,
              loop: true,
              items: 3, // display 4 items in a small-medium device
          },
          768:{
              // center: true,
              // stagePadding: 10,
              loop: true,
              items: 5, // display 5 items in a medium device
          },
          992:{
              items: 4, // display 5 items in large device
          }
      },

    });
    

    $(".owl-carousel").owlCarousel(); // Owl initializer function
});