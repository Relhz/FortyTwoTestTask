$(document).ready(function(){ 
    
    // update requests list    
    var old = parseInt($('.c:eq(' + 0 + ')').html())
    var past = parseInt($('.c:eq(' + 0 + ')').html())
    setInterval(function(){

        $.ajax({
            url : "/forajax/", 
            type : "GET", 
            success : function(data) {
 
                var current = parseInt(data[0].split(' ')[5])
                var new_requests = current - old

                if(new_requests){
                    for(i = 0; i < new_requests; i++){
                        $('.path:eq(' + ($(".path").length - 1) + ')').remove()

                        $('.path:eq(0)').before(
                            '<p class="path">' + 
                            data[i].split(' ')[7].replace(/"/gi, '').replace(/}/gi, '') + 
                            ' ' + data[i].split(' ')[1].replace(/"/gi, '') + 
                            ' ' + 
                            data[i].split(' ')[3].slice(0, 17).replace(/"/gi, '').replace(/T/gi, ' ')
                            + '<span class="c" style="display: none">' + 
                            data[i].split(' ')[5].replace(/"/gi, '') + '</span></p>'
                        )

                    old = parseInt($('.c:eq(' + 0 + ')').html())
                    }
	                if(document.hidden){
	                	console.log('lol')
	                    $('.count').html('('+ (current - past) + ')')	  
	                    document.title = '(' + (current - past) + ')Requests'
	                }
	                else{
	                	past = parseInt($('.c:eq(' + 0 + ')').html())
	                }
                }
            },
        });

    }, 1000);

    $(window).focus(function(){
        
        document.title = 'Requests'
        past = parseInt($('.c:eq(' + 0 + ')').html())
        setTimeout(function(){
        	$('.count').html('')
        }, 1500)
    })

})

