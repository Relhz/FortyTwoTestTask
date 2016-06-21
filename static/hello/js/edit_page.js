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


	$("#id_photo").change(function(){
    	readURL(this);
	});

    var bar = $('.bar');
    var percent = $('.percent');

    $('#sendpost').ajaxForm({
        beforeSend: function() {
            $('#status').empty();
            var percentVal = '0%';
            bar.width(percentVal);
            percent.html(percentVal);
        },
        uploadProgress: function(event, position, total, percentComplete) {
            var percentVal = percentComplete + '%';
            bar.width(percentVal);
            percent.html(percentVal);
        },
        complete: function(xhr) {
            $('#status').html(xhr.responseText);
        }
    }); 


    (function() {
        $("#id_Date_of_birth").datepicker({
          dateFormat: "yy-mm-dd"
        });
    });

})