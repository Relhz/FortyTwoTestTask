$(document).ready(function(){ 
    
    // update requests list    
    var old = parseInt($('.c:eq(' + 0 + ')').html())
    setInterval(function(){

        $.ajax({
            url : "/forajax/", 
            type : "GET", 
            success : function(data) {

                var current = parseInt(data[0].split(' ')[7])
                var new_requests = current - old

                if(new_requests > 0){
                    for(i = 0; i < new_requests; i++){
                        $('.path:eq(' + ($(".path").length - 1) + ')').remove()

                        $('.path:eq(0)').before(
                            '<p class="path">' + 
                            data[i].split(' ')[9].replace(/"/gi, '').replace(/}/gi, '') + 
                            ' ' + data[i].split(' ')[1].replace(/"/gi, '') + 
                            ' ' + data[i].split(' ')[5].replace(/"/gi, '') + ' ' + 
                            data[i].split(' ')[3].slice(0, 17).replace(/"/gi, '').replace(/T/gi, ' ')
                            + '<span class="c" style="display: none">' + 
                            data[i].split(' ')[7].replace(/"/gi, '') + '</span></p>'
                        )

                    old = parseInt($('.c:eq(' + 0 + ')').html())
                    }
                }
            },
        });
    
    }, 1000);

    // reset requests counter	    
    $(window).mouseenter(function () {
        clearInterval(interval)
        $('.count').html('')
        document.title = 'Requests'    
    })

    // write amount of the requests to a header and a title
    var past = parseInt($('.c:eq(' + 0 + ')').html())
    interval = setInterval(function(){
        
        var current = parseInt($('.c:eq(' + 0 + ')').html())
        if((current - past) > 0){
            $('.count').html('('+ (current - past) + ')')	  
            document.title = '(' + (current - past) + ')Requests'
        }

    }, 1000);

    // reset requests counter when user view page
    $(window).focus(function () {
        clearInterval(interval)
        setTimeout(function(){ 
            $('.count').html('')
            document.title = 'Requests'
        }, 2000);
        
    });

    // write amount of the requests to a header and a title
    // when user switches out this tab
    $(window).blur(function () {
        clearInterval(interval)
        var past = parseInt($('.c:eq(' + 0 + ')').html())

        interval = setInterval(function(){

            var current = parseInt($('.c:eq(' + 0 + ')').html())
            if((current - past) > 0){
                $('.count').html('('+ (current - past) + ')')	  
                document.title = '(' + (current - past) + ')Requests'
            }

        }, 500);
    })
});
