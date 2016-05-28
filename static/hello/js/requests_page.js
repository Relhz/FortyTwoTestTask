$(document).ready(function(){

	// load list of all requests
	function requests_list(data) {

    	for(i = 0; i < 10; i++){	        
    		$('.path:eq(' + i + ')').html(data[i].method + 
        ' ' + data[i].path + ' ; ' + data[i].status_code + 
        ' ; ' + data[i].date_and_time.slice(0, 16))
    	}
    }

    // reset requests amount
    function reset(){
	    $('.count').html('')
		document.title = 'Requests'
		$.ajax({
		    url: '/forajax_count_reset/',
		    type: 'GET', 
    	})
    }

    $.ajax({
        url : "/forajax2/", 
        type : "GET", 	        
        success : function(data){ requests_list(data) }
    });

	// write the amount of requests to the header and the title
    $.ajax({
	    url: '/forajax_count/',
	    type: 'GET', 
	    success: function(data) {
	        $('.count').html('('+ data.amount + ')')	  
		    document.title = '('+ data.amount + ')' + 'Requests'        
	    },
	});

	// checking for new requests
    setInterval(function(){ 
		
	    $.ajax({
	        url : "/forajax2/", 
	        type : "GET", 	        
	        success : function(data){ requests_list(data) }
	    })	
	}, 1000);

    // if user look at this page, reset requests counter
	$(window).focus(function () {
    	setTimeout(reset, 3000);
    })
    
	setTimeout(reset, 3000);

	$('.path').bind("DOMSubtreeModified",function(){

		$.ajax({
		    url: '/forajax_count/',
		    type: 'GET', 
		    success : function(data) {
		    	$('.count').html('('+ data.amount + ')')	  
	    		document.title = '('+ data.amount + ')' + 'Requests'

		    }
		});       
    });
});

