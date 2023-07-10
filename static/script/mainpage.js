function closeSideBar() {
     $('#openSidebarMenu').prop('checked', false);
}



// check if stats are visible, then run function
var uses = false;
$(window).scroll(function() {
     if (!uses) {
          if (checkVisible($('.years-of-experience-value'))) {
               anime({
                    targets: '.satisfied-customers-value',
                    innerHTML: [0,3000 + "+"],
                    easing: 'linear',
                    round: 1, // Will round the animated value to 1 decimal
                    duration: 2000
               });
               anime({
                    targets: '.delivery-time-value',
                    innerHTML: [0,24 + "h"],
                    easing: 'linear',
                    round: 1, // Will round the animated value to 1 decimal
                    duration: 2000
               });
               anime({
                    targets: '.years-of-experience-value',
                    innerHTML: [0,2],
                    easing: 'linear',
                    round: 1, // Will round the animated value to 1 decimal
                    duration: 2000
               });
               uses = true;
          } else {
               uses = false;
          }
     }
});
function checkVisible( elm, eval ) {
     eval = eval || "visible";
     var vpH = $(window).height(), // Viewport Height
          st = $(window).scrollTop(), // Scroll Top
          y = $(elm).offset().top,
          elementHeight = $(elm).height();
     
     if (eval == "visible") return ((y < (vpH + st)) && (y > (st - elementHeight)));
     if (eval == "above") return ((y < (vpH + st)));
}








// ---------- EXPAND FIRST QUESTION IN FAQ ---------------
var trigger = $("#first-question img");
var container = $("#first-question").parents(".faq-card");

$("#first-answer").animate({ height: "toggle" }, 100);

if (trigger.hasClass("icon-rotate")) {
     trigger.removeClass("icon-rotate");
} else {
     trigger.addClass("icon-rotate");
}

// ---------- EXPAND QUESTION IN FAQ ON CLICK ---------------
$(".question-wrapper").click(function () {
     var container = $(this).parents(".faq-card");
     var answer = container.find(".answer-wrapper");
     var trigger = container.find(".question-wrapper img");
     var state = container.find(".question-wrapper");
   
     answer.animate({ height: "toggle" }, 100);
   
     if (trigger.hasClass("icon-rotate")) {
       trigger.removeClass("icon-rotate");
     } else {
       trigger.addClass("icon-rotate");
     }
});







// // ----------------- SCROLL TO TOP ARROW ---------------------
// var opacityvalue = "";
// $(window).scroll(function() {
//      var scrollTop = $(this).scrollTop();
 
//          $('.scrolltotop').css({
//          opacity: function() {
//              var elementHeight = $(this).height(),
//              opacity = ((1000 - scrollTop) / elementHeight);
//              opacityvalue = opacity * -0.1;
//           //    console.log(opacityvalue);
//              return opacityvalue;
//          }
//      });
//      if (opacityvalue >= 0) {
//           document.getElementById("scrolltotop_ID").style.display = "flex";
//      }
//      else if (opacityvalue < 0) {
//           document.getElementById("scrolltotop_ID").style.display = "none";
//      }
// });

function ScrollToTop()
{
     document.body.scrollTop = 0;
     document.documentElement.scrollTop = 0;
}
   