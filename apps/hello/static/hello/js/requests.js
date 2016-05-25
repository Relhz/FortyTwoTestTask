$(document).ready(function(){

    // getting amount of the requests
	setInterval(function(){
	    $.ajax({
		    url: '/forajax_count/',
		    type: 'GET', 
		    success: function(data) {
		        
		        $('.amount').html('('+ data.amount + ')')	          
		    },
		});
	}, 1000);


})