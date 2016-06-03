$(document).ready(function(){ 

	// update requests list
	var old = $('.c:eq(' + 0 + ')').html()
    setInterval(function(){
	
	    $.ajax({
	        url : "/forajax/", 
	        type : "GET", 
	        success : function(data) {

	        	for(i = 0; i < 10; i++){
			        var current = data[0].amount
			        if((current - past) > 0){
			        	$('.path:eq(' + i + ')').html(data[i].method + 
				        ' ' + data[i].path + ' ; ' + data[i].status_code + 
				        ' ; ' + data[i].date_and_time.slice(0, 16) + 
				        '<span class="c" style="display: none">' + data[i].amount 
				        + '</span>')
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
	var past = $('.c:eq(' + 0 + ')').html()
	interval = setInterval(function(){
	    $.ajax({
		    url: '/forajax/',
		    type: 'GET', 
		    success: function(data) {
		        
		        var current = data[0].amount
		        console.log(past, current, data)
		        if((current - past) > 0){
		        	$('.count').html('('+ (current - past) + ')')	  
			    	document.title = '(' + (current - past) + ')Requests'
		        }
	    	},
		});
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
		var past = $('.c:eq(' + 0 + ')').html()
		interval = setInterval(function(){
		    $.ajax({
			    url: '/forajax/',
			    type: 'GET', 
			    success: function(data) {

			        var current = data[0].amount
			        if((current - past) > 0){
			        	$('.count').html('('+ (current - past) + ')')	  
				    	document.title = '(' + (current - past) + ')Requests'
			        }

			    },
			});
		}, 1000);
	})
});
