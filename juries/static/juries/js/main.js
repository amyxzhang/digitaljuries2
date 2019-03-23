/*------------------------------------*\
    TOGGLING CHECKBOXES
\*------------------------------------*/

/*!
 * toggleAttr() jQuery plugin
 * @link http://github.com/mathiasbynens/toggleAttr-jQuery-Plugin
 * @description Used to toggle selected="selected", disabled="disabled", checked="checked" etc…
 * @author Mathias Bynens <http://mathiasbynens.be/>
 */
jQuery.fn.toggleAttr = function(attr) {
 return this.each(function() {
  var $this = $(this);
  $this.attr(attr) ? $this.removeAttr(attr) : $this.attr(attr, attr);
 });
};

/*------------------------------------*\
    BOOTSTRAP FEATURES
\*------------------------------------*/

// Tooltips
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
});

// Popover
$(function () {
  $('[data-toggle="popover"]').popover({
    html: true,
    template: '<div class="popover" role="tooltip"><div class="arrow"></div><h5 class="popover-header dark"></h5><div class="popover-body"></div></div>'
  })
});

$(document).ready(function(){

  // Slick slider Carousel
  $('.slideshow').slick({
    autoplay: true,
    autoplaySpeed: 5000,
    arrows: true,
    infinite: false,
    pauseOnFocus: true,
    swipeToSlide: true,
    draggable: true,
    slidesToShow: 1,
    slidesToScroll: 1
  });
});


// COUNTDOWN TIMER
function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.text(minutes + ":" + seconds);

        if (--timer < 0) {
            timer = duration;
        }
    }, 1000);
}

jQuery(function ($) {
    var fiveMinutes = 60 * 5,
        display = $('#time');
    startTimer(fiveMinutes, display);
});
