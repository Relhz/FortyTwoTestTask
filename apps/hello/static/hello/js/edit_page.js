$(document).ready(function(){ 

	function readURL(input) {

	    if (input.files && input.files[0]) {
	        var reader = new FileReader();

	        reader.onload = function (e) {
	            $('#preview').attr('src', e.target.result);
	        }

	        reader.readAsDataURL(input.files[0]);
	    }
	}

	$("#id_Photo").change(function(){
    	readURL(this);
	});

	$('#sendpost').submit(function(event){
	    event.preventDefault();
	    console.log("form submitted!")  // sanity check
	    send_post();
	});

	function send_post() {
	    var val = $('#id_txt').val()
	    $.ajax({

	        url : "/adding/", // the endpoint
	        type : "POST", // http method
	        data : { 
	        	txt: $('#id_txt').val(), 
	        	csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
	        	},


	        // handle a successful response
	        success : function(json) {
	        	console.log(json)
	            $('#id_txt').val(''); 
	            $('body').append('<div id="newdiv">' + json.txt + '</div>')
	        },


	    });
	};

    $(function() {
      $("#id_Date_of_birst").datepicker();
    });

})