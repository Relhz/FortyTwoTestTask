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
	    console.log("form submitted!");
	    send_post();
	});

	function send_post() {

	    $.ajax({

	        url : "/forajax_edit/", 
	        type : "POST", 
	        data : { 
	        	name: $('#id_Name').val(),
	        	last_name: $('#id_Last_name').val(), 
	        	date_of_birst: $('#id_Date_of_birst').val(), 
	        	photo: $('#id_Photo').val(), 
	        	contacts: $('#id_Contacts').val(), 
	        	email: $('#id_Email').val(), 
	        	skype: $('#id_Skype').val(), 
	        	jabber: $('#id_Jabber').val(), 
	        	other_contacts: $('#id_Other_contacts').val(), 
	        	bio: $('#id_Bio').val(), 
	        	csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
	        	},

	        success : function(json) {
	        	console.log(json)
	        },


	    });
	};

    $(function() {
      $("#id_Date_of_birst").datepicker();
    });

})