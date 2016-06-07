$(document).ready(function(){ 

	// update requests list
	var old = $('.c:eq(' + 0 + ')').html()
    setInterval(function(){
	
	    $.ajax({
	        url : "/forajax/", 
	        type : "GET", 
	        success : function(data) {
	        	console.log(data[0])
	        	console.log(data[0].split(' ')[1])
	        	console.log(data[0].split(' ')[3])
	        	console.log(data[0].split(' ')[5])
	        	console.log(data[0].split(' ')[7])
	        	console.log(data[0].split(' ')[9])

		        var current = data[0].split(' ')[7]
		        console.log(current)
		        new_requests = current - old
		        if(new_requests > 0){
		        	for(i = 0; i < new_requests; i++){
			        	$('.path:eq(' + ($(".path").length - 1) + ')').remove()
			        	
			        	$('.path:eq(0)').before(
			        		'<p class="path">' + data[i].split(' ')[9] + 
					        ' ' + data[i].split(' ')[1] + ' ; ' + data[i].split(' ')[5] +
					        ' ; ' + data[i].split(' ')[3] + 
					        '<span class="c" style="display: none">' + 
					        data[i].split(' ')[7] + '</span></p>'

		        		)
				        
				    old = $('.c:eq(' + 0 + ')').html()
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
		        
		        var current = data[0].split(' ')[7]
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

			        var current = data[0].split(' ')[7]
			        if((current - past) > 0){
			        	$('.count').html('('+ (current - past) + ')')	  
				    	document.title = '(' + (current - past) + ')Requests'
			        }

			    },
			});
		}, 1000);
	})
});
