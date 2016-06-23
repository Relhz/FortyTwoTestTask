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
                var message = xhr.responseText.replace(/[\[\]']+|"|{|}/g, '').split(':')
                message1 = message[0].charAt(0).toUpperCase() + 
                message[0].slice(1).replace(/_/g, ' ')
                message2 = message[1].charAt(1).toLowerCase() + message[1].slice(2)
                message = message1 + ' - ' + message2
                $('.status').html(message);
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