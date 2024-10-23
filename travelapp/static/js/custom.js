
  (function ($) {
  
  "use strict";

    // NAVBAR
    $('.navbar-collapse a').on('click',function(){
      $(".navbar-collapse").collapse('hide');
    });

    // $(function() {
    //   $('.hero-slides').vegas({
    //       slides: [
    //         { src: '{% static "images/sincere-laugh-showing-picture-smartphone-casual-meeting-with-best-friends-restaurant-terrace.jpg" %}'.replace(/\\/g, '/') },
    //         { src: '{% static "images/happy-waitress-giving-coffee-customers-while-serving-them-coffee-shop.jpg" %}' },
    //         { src: '{% static "images/young-female-barista-wear-face-mask-serving-take-away-hot-coffee-paper-cup-consumer-cafe.jpg" %}' }
    //       ],
    //       timer: false,
    //       animation: 'kenburns',
    //   });
    // });

    // $(function() {
    //   $('.hero-slides').vegas({
    //     slides: [
    //       { src: '{% static "images/img1.jpg" %}', animation: 'kenburns' },
    //       { src: '{% static "images/img2.jpg" %}', animation: 'kenburns' },
    //       { src: '{% static "images/img3.jpg" %}', animation: 'kenburns' },
    //       { src: '{% static "images/img4.jpg" %}', animation: 'kenburns' }
    //     ],
    //     timer: false
    //   });
    // });
    
    // CUSTOM LINK
    $('.smoothscroll').click(function(){
      var el = $(this).attr('href');
      var elWrapped = $(el);
      var header_height = $('.navbar').height() + 60;
  
      scrollToDiv(elWrapped,header_height);
      return false;
  
      function scrollToDiv(element,navheight){
        var offset = element.offset();
        var offsetTop = offset.top;
        var totalScroll = offsetTop-navheight;
  
        $('body,html').animate({
        scrollTop: totalScroll
        }, 300);
      }
    });
  
  })(window.jQuery);


