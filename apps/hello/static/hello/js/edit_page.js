$(document).ready(function(){  

    $(function() {
        $("#id_date_of_birth").datepicker({
            dateFormat: "yy-mm-dd"
        });
    });

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

    $('#sendpost').ajaxForm(); 

})