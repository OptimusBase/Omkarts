
$(document).ready(function() {

	$(function() {
	  var loc = window.location.href; // returns the full URL
	  if(/orders/.test(loc)) {
	    $(".1").addClass("active");
	    $(".2").removeClass("active");
	    $(".3").removeClass("active");
	    $(".4").removeClass("active");
	  }
	});

});