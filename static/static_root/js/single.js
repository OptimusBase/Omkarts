
$(document).ready(function() {

	$('#data-wrapper').prop('disabled', false);

	var variant = $('#variant').val();
	$.ajax({
			type: "POST",
			url: $('#product-variation-form').attr('action'),
			data: {
				"variation": variant,
				"csrfmiddlewaretoken": $('input[type=hidden][name=csrfmiddlewaretoken]').attr('value'),
			},
			success: function(data){
				debugger;
  				if (data.stock == true){
  					$("#update-price").html("Rs. " + JSON.stringify(data.price));
  					$("#update-stock").html("" + data.qty);
  					$('#add-to-cart').prop('disabled', false);
  					$('.AddWishList').attr('id', data.variation_id)
  					$('#option-1').attr('value', data.variation_id)
  				}
  				else{
  					$('#add-to-cart').prop('disabled', true);
  					$("#update-price").html("Rs. " + JSON.stringify(data.price));
  					$("#update-stock").html("" + data.qty);
  					$('.AddWishList').attr('id', data.variation_id)
  					$('#option-1').attr('value', data.variation_id)
  				}
			},
	      	error: function(data){
	        	var obj = data.responseJSON
	      	},
		});


		$('#variant').change(function(){
			// $('#loader').show();
			var variant = $('#variant').val();
			window.location = $('#variant').val();
			// $.ajax({
			// 	type: "POST",
			// 	url: $('#product-variation-form').attr('action'),
			// 	data: {
			// 		"variation": variant,
			// 		"variant-changed": true,
			// 		"csrfmiddlewaretoken": $('input[type=hidden][name=csrfmiddlewaretoken]').attr('value'),
			// 	},
			// 	success: function(data){
	  // 				if (data.stock == true){
	  // 					$("#update-price").html("Rs. " + JSON.stringify(data.price));
	  // 					$("#update-stock").html("" + data.qty);
	  // 					$('#add-to-cart').prop('disabled', false);
	  // 					$('.AddWishList').attr('id', data.variation_id)
	  // 					$('#option-1').attr('value', data.variation_id)
	  // 				}
	  // 				else{
	  // 					$('#add-to-cart').prop('disabled', true);
	  // 					$("#update-price").html("Rs. " + JSON.stringify(data.price));
	  // 					$("#update-stock").html("" + data.qty);
	  // 					$('.AddWishList').attr('id', data.variation_id)
	  // 					$('#option-1').attr('value', data.variation_id)
	  // 				}

			// 	},
		 //      	error: function(data){
		 //        	var obj = data.responseJSON
		 //      	},
			// });
			// $('#loader').hide();
		});




	$('.AddWishList').click(function(e){
		debugger;
		var product_variation_id = $('.AddWishList').attr('id')
		$.ajax({
			type: "POST",
			url: $('#wishList').attr('action'),
			data: {
				"product_variation_id": product_variation_id,
				"csrfmiddlewaretoken": $('input[type=hidden][name=csrfmiddlewaretoken]').attr('value'),
			},
			success: function(data){
  				$('.MsgWishList').show();
  				$("#MsgWishList").html("" + data)
			},
	      	error: function(data){
	        	var obj = data.responseJSON
	      	},
		});
	});


	// owl carousel
    var product_slider = $(".popular-products");

    product_slider.owlCarousel({
      rewindNav : false,
      pagination : false,
      items : 5,
      loop: false,
      responsiveClass: true,
      margin: 20,
      slideBy: 2,
      // nav: true,
      dotsEach: true,
      lazyLoad: false,
      responsive:{
          0:{ 
              center: true,
              stagePadding: 10,
              loop: true,
              items: 1, // display 2 items in small device
          },
          480:{
              center: true,
              stagePadding: 10,
              loop: true,
              items: 3, // display 4 items in a small-medium device
          },
          768:{
              center: true,
              stagePadding: 10,
              loop: true,
              items: 5, // display 6 items in a medium device
          },
          992:{
              items: 5, // display 8 items in large device
          }
      },

    });
    

    $(".popular-products").owlCarousel(); // Owl initializer function

	// $("#save_account_info").click(function(e){
	//   var email = $('#email').val() 
	//  $.ajax({
	//       type: "POST",
	//       url: $('#save_account_info_form').attr('action'),
	//       data: {
	//             "email": email,
	//             "csrfmiddlewaretoken": $('input[type=hidden][name=csrfmiddlewaretoken]').attr('value'),
	//           },
	//       success: function(data){
	//         var d = eval(data);
	//         $("#displayEmail").text(d[0].fields.email);
	//         $("#ModalFirst").modal("hide");
	//       },
	//       error: function(data){
	//         var obj = data.responseJSON
	//       },
	//    });
	// });


	// $("#save_personal_info").click(function(e){
	//   var name = $('#name').val()
	//   var gender = $('input[type=radio][name=gender]:checked').attr('value')
	//   // var birthdate = $('#birthdate').val()
	//   var country = $('.select_option').val()
	//  $.ajax({
	//       type: "POST",
	//       url: $('#save_personal_info_form').attr('action'),
	//       data: {
	//             "name": name,
	//             "gender": gender,
	//             // "birthdate": birthdate,
	//             "country": country,
	//             "csrfmiddlewaretoken": $('input[type=hidden][name=csrfmiddlewaretoken]').attr('value'),
	//           },
	//       success: function(data){
	//         var d = eval(data);
	//         $("#displayName").text(d[0].fields.name);
	//         $("#displayGender").text(d[0].fields.gender);
	//         $("#displayCountry").text(d[0].fields.country);
	//         $("#ModalSecond").modal("hide");
	//       },
	//       error: function(data){
	//         var obj = data.responseJSON
	//       },
	//    });
	// });



	// $(function() {
	//   var loc = window.location.href; // returns the full URL
	//   if(/account_settings/.test(loc)) {
	//     $(".1").removeClass("active");
	//     $(".2").removeClass("active");
	//     $(".3").removeClass("active");
	//     $(".4").addClass("active");
	//   }
	// });

});