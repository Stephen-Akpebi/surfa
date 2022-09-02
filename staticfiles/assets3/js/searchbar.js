// (function($, window){
//   var arrowWidth = 30;
//   $.fn.resizeselect = function(settings) {
//     return this.each(function() {
//       $(this).change(function(){
//         var $this = $(this);
//         // create test element
//         var text = $this.find("option:selected").text();
//
//         var $test = $("<span>").html(text).css({
//             "font-size": $this.css("font-size"), // ensures same size text
//          // "visibility": "hidden"                              // prevents FOUC
//         });
//
//         // add to body, get width, and get out
//         $test.appendTo($this.parent());
//         var width = $test.width();
//                 console.log(width);
//         $test.remove();
//         // set select width
//         $this.width(width + arrowWidth);
//         // run on start
//       }).change();
//     });
//   };
//   // run by default
//   $("select.resizeselect").resizeselect();
// })(jQuery, window);

$(document).ready(function(e){
       $('.search-panel .dropdown-menu').find('a').click(function(e) {
       e.preventDefault();
       var param = $(this).attr("href").replace("#","");
       var concept = $(this).text();
       $('.search-panel span#search_concept').text(concept);
       $('.input-group #search_param').val(param);
       });
       });
var a = document.getElementByTagName('a').item(0);
$(a).on('keyup', function(evt){
 console.log(evt);
 if(evt.keycode === 13){

   alert('search?');
 }
});
