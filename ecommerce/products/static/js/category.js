
$('input[type="checkbox"]').on('click', function() {
	debugger;
	window.location = $(this).val();
});


var acc = document.getElementsByClassName("accordion");
	var i;

	for (i = 0; i < acc.length; i++) {
	    acc[i].onclick = function(){
	        this.classList.toggle("active");
	        this.nextElementSibling.classList.toggle("show");
	  }
	}

function getCheckedBoxes(chkboxName) {
  var checkboxes = document.getElementsByClassName(chkboxName);
  var checkboxesChecked = [];
  // loop over them all
  for (var i=0; i<checkboxes.length; i++) {
     // And stick the checked ones onto an array...
     if (checkboxes[i].checked) {
        checkboxesChecked.push(checkboxes[i].name);
     }
  }
  // Return the array if it is non-empty, or null
  return checkboxesChecked;
}

$('.mycheckboxes').click(function() {
	debugger;
	var checkedBoxIds = getCheckedBoxes("mycheckboxes");

	$.ajax({
	  type: "POST",
	  url: $('#checkbox_id').attr('value'),
	  data: {
	        "brand_ids": checkedBoxIds,
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
    console.log(checkedBoxIds);
});


