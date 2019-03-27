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

// Show selected btn
$('[data-toggle="button"]').click(function() {
  $(this).button('toggle');
});


// Popover
$(function () {
  $('[data-toggle="popover"]').popover({
    html: true,
    template: '<div class="popover" role="tooltip"><div class="arrow"></div><h5 class="popover-header dark"></h5><div class="popover-body"></div></div>'
  })
});

// $(document).ready(function(){
//
//   // Slick slider Carousel
//   $('.slideshow').slick({
//     autoplay: true,
//     autoplaySpeed: 5000,
//     arrows: true,
//     infinite: false,
//     pauseOnFocus: true,
//     swipeToSlide: true,
//     draggable: true,
//     slidesToShow: 1,
//     slidesToScroll: 1
//   });
// });



function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}
