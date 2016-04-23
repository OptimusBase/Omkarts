
$(document).ready(function() {



	$("#save_account_info").click(function(e){
	  var email = $('#email').val() 
	 $.ajax({
	      type: "POST",
	      url: $('#save_account_info_form').attr('action'),
	      data: {
	            "email": email,
	            "csrfmiddlewaretoken": $('input[type=hidden][name=csrfmiddlewaretoken]').attr('value'),
	          },
	      success: function(data){
	        var d = eval(data);
	        $("#displayEmail").text(d[0].fields.email);
	        $("#ModalFirst").modal("hide");
	      },
	      error: function(data){
	        var obj = data.responseJSON
	      },
	   });
	});


	$("#save_personal_info").click(function(e){
	  var name = $('#name').val()
	  var gender = $('input[type=radio][name=gender]:checked').attr('value')
	  // var birthdate = $('#birthdate').val()
	  var country = $('.select_option').val()
	 $.ajax({
	      type: "POST",
	      url: $('#save_personal_info_form').attr('action'),
	      data: {
	            "name": name,
	            "gender": gender,
	            // "birthdate": birthdate,
	            "country": country,
	            "csrfmiddlewaretoken": $('input[type=hidden][name=csrfmiddlewaretoken]').attr('value'),
	          },
	      success: function(data){
	        var d = eval(data);
	        $("#displayName").text(d[0].fields.name);
	        $("#displayGender").text(d[0].fields.gender);
	        $("#displayCountry").text(d[0].fields.country);
	        $("#ModalSecond").modal("hide");
	      },
	      error: function(data){
	        var obj = data.responseJSON
	      },
	   });
	});



	$(function() {
	  var loc = window.location.href; // returns the full URL
	  if(/account_settings/.test(loc)) {
	    $(".1").removeClass("active");
	    $(".2").removeClass("active");
	    $(".3").removeClass("active");
	    $(".4").addClass("active");
	  }
	});

});