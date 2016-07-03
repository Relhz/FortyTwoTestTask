$(document).ready(function(){ 

    // update requests list    
    var old = parseInt($('.c').html())
    var past = parseInt($('.c').html())
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    setInterval(function(){

        $.ajax({

            url : window.location, 
            type : "GET", 
            success : function(data){

                var current = parseInt(data[0].id)
                var new_requests = current - old

                if(new_requests){
                    for(i = 0; i < new_requests; i++){

                        $('.path:eq(' + ($(".path").length - 1) + ')').remove()
                        $('.path:eq(0)').before(
                            '<div class="path">' + data[i].method + 
                            ' ' + data[i].path + ', ' + 
                            data[i].requests_date_time.slice(0, 16).replace(/T/i, ' ')
                            + ', <div class="priordiv">priority <span class="priorval">'
                            + data[i].priority + '</span></div>' +
                            '<form class="priorityform" method="post"' + 
                            ' action="/requests/' + data[i].id + '/">' + 
                            '<input type="hidden" name="csrfmiddlewaretoken" value="' 
                            + csrf + '">' +
                            '<input id="id_priority" name="priority" type="number"' +
                            ' min="1" max="999" value="' + data[i].priority + '" >' +
                            '<input class="okpriority" type="submit"' + 
                            ' value="ok"/></form>' +
                            '<span class="c" style="display: none">' + 
                            data[i].id + '</span></div>'
                        )

                    old = parseInt($('.c').html())
                    }
                    if(document.hidden){
                        $('.count').html('('+ (current - past) + ')')	  
                        document.title = '(' + (current - past) + ')Requests'
                    }
                    else{
                        past = parseInt($('.c').html())
                    }
                }
            },
        });

    }, 1000);

    $(window).focus(function(){
        
        document.title = 'Requests'
        past = parseInt($('.c').html())
        setTimeout(function(){
            $('.count').html('')
        }, 1500)
    })

    // show edit priority form
    $('.panel-body').on('click', '.priordiv', function(){
        $(this).hide()
        $(this).siblings('.err').remove()
        $(this).next().css('display', 'inline')
    })
    
    // submit edit priority form
    $('.panel-body').on('submit', '.priorityform', function() {

        $(this).ajaxSubmit({

            success: function(responseText, statusText, xhr, $form){
                console.log(xhr.responseText)
                $form.hide()
                $form.prev().children('.priorval').html($form.children('#id_priority').val())
                $form.prev().show()
                if(xhr.responseText != '{}'){
                    var message = xhr.responseText.split('priority":')[1].replace(/[\[\]']+|"|{|}/g, '')
                    console.log(xhr.responseText.split('priority":')[1])
                    $form.prev().after('<span class="err">' + message + '</span>')
                }
            }
        })
        return false; 
    });

    // sort elements by priority
    $('.bypriority').click(function(){
        requests = $('.path')
        requests.sort(function(a, b) {
            return parseInt($(a).find('.priorval').html()) - 
            parseInt($(b).find('.priorval').html())
        })
        $('.path').remove()
        $('.asusual').after(requests)
    })

    // sort elements as usual
    $('.asusual').click(function(){
        requests = $('.path')
        requests.sort(function(a, b) {
        	return parseInt($(b).find('.c').html()) - parseInt($(a).find('.c').html())
        })
        $('.path').remove()
        $('.asusual').after(requests)
    })
})
