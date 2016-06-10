$(document).ready(function(){  

	function readURL(input) {

	    if (input.files && input.files[0]) {
	        var reader = new FileReader();

	        reader.onload = function (e) {
	            $('#preview').attr('src', e.target.result);
	        };

	        reader.readAsDataURL(input.files[0]);
	    };
	};


	$("#id_Photo").change(function(){
    	readURL(this);
	});

	$('#sendpost').submit(function(event){
	    event.preventDefault();
	    formdata = new FormData(); 
    	console.log($("#id_Photo")[0].files[0])
        var file = $("#id_Photo")[0].files[0];
        if (formdata) {
            formdata.append("photo", file);
            csrf = $('input[name=csrfmiddlewaretoken]').val()
            formdata.append("name", $('#id_Name').val());
            formdata.append("last_name", $('#id_Last_name').val());
            formdata.append("date_of_birth", $('#id_Date_of_birth').val());
            formdata.append("contacts", $('#id_Contacts').val());
            formdata.append("email", $('#id_Email').val());
            formdata.append("skype", $('#id_Skype').val());
            formdata.append("jabber", $('#id_Jabber').val());
            formdata.append("other_contacts", $('#id_Other_contacts').val());
            formdata.append("bio", $('#id_Bio').val());
            formdata.append("csrfmiddlewaretoken", csrf);

		    $.ajax({

		        url : "/forajax_edit/", 
		        type : "POST", 
		        data : formdata,
                processData: false,
                contentType: false,
		        success : function(json) {
		        	$('.success').show()
		        	console.log(json)
		        },

		    });
		}
	});

    $(function() {
        $("#id_Date_of_birth").datepicker({
      	  dateFormat: "yy-mm-dd"
        });
    });

})