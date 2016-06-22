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

    $('#sendpost').ajaxForm({
        beforeSend: function() {
            $('input').attr('disabled', 'disabled');
            $('textarea').attr('disabled', 'disabled');
            $('.bar').show()
            $('.percent').show()
            $('.status').hide();
            $('.status').html('Changes have been saved')
            $('.status').css('color', 'green')
            var percentVal = '0%';
            $('.bar').width(percentVal);
            $('.percent').html(percentVal);
        },
        uploadProgress: function(event, position, total, percentComplete) {
            var percentVal = percentComplete + '%';
            $('.bar').width(percentVal);
            $('.percent').html(percentVal);
        },
        complete: function(xhr){

            if(xhr.responseText != '{}'){
                $('.status').css('color', 'red')
                $('.status').html(xhr.responseText.replace(/[\[\]']+|"|{|}/g, ''));
            }
            $('.status').show();
            $('input').removeAttr('disabled');
            $('textarea').removeAttr('disabled');
            setTimeout(function(){
                $('.bar').hide()
                $('.percent').hide()
            }, 3000)
        }
    }); 
})