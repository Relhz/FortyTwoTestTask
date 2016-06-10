$(document).ready(function(){ 
    
    // update requests list    
    var old = parseInt($('.c').html())
    var past = parseInt($('.c').html())
    setInterval(function(){

        $.ajax({
            url : "/forajax/", 
            type : "GET", 
            success : function(data) {

                var current = parseInt(data[0].id)
                var new_requests = current - old

                if(new_requests){
                    for(i = 0; i < new_requests; i++){
                        $('.path:eq(' + ($(".path").length - 1) + ')').remove()
                        $('.path:eq(0)').before(
                            '<p class="path">' + data[i].method + 
                            ' ' + data[i].path + ', ' + 
                            data[i].date_and_time.slice(0, 16).replace(/T/i, ' ')
                            + '<span class="c" style="display: none">' + 
                            data[i].id + '</span></p>'
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

})
