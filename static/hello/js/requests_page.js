$(document).ready(function(){ 

	// update requests list
    setInterval(function(){


		
	    $.ajax({
	        url : "/forajax2/", 
	        type : "GET", 	        
	        success : function(data) {

	        	for(i = 0; i < 10; i++){	        
	        		$('.path:eq(' + i + ')').html(data[i].method + 
		        ' ' + data[i].path + ' ; ' + data[i].status_code + 
		        ' ; ' + data[i].date_and_time.slice(0, 16)) + data[i].amount

	        	}
	        },
	    });
		
	}, 1000);

    // reset requests counter when page loaded
	setTimeout(function(){ 
		$('.count').html('')
		document.title = 'Requests'
		$.ajax({
		    url: '/forajax_count_reset/',
		    type: 'GET', 
		    success : function(data) {
		    }
		});
	}, 3000);

    // reset requests counter when user view page
	$(window).focus(function () {
    	setTimeout(function(){ 
    		$('.count').html('')
    		document.title = 'Requests'
			$.ajax({
			    url: '/forajax_count_reset/',
			    type: 'GET', 
			    success : function(data) {
			    }
			});
    	}, 2000);
        
    });

	// write the amount of requests to the header and the title
	$(window).blur(function () {
	    $.ajax({
		    url: '/forajax_count/',
		    type: 'GET', 
		    success: function(data) {
		        
		        $('.count').html('('+ data.amount + ')')	  
			    document.title = '('+ data.amount + ')' + 'Requests'        
		    },
		});
	})
});

