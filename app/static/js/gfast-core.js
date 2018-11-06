$( document ).ready(function() {
    console.log( "ready!" );
    $('body').scrollspy({
        target: '.sidebar-nav',
        offset: 40
    });
    
    /* This is a class applied to <body> in base.html and defined in the core
       css as a workaround to prevent the sidebar from loading offscreen in IE.
       Here we remove it so that the sidebar transition works as intended. */
    $("body").removeClass("preload");
});


// LOGIN
$("#loginForm").bind('submit', function(e) {

    // prevent page refresh
    e.preventDefault();

     var $btn = $( "#btn-login-submit" ).button('loading')
     var mdlInfo = $('#modal-info'); //Prepare Modal in case we have information message for the user
    // post the data
    var ajax=$.ajax({
        type: "POST",
        data: $("#loginForm").serialize(),
        url: "/login/"
    }).done(function(result){
        console.log('tried logging in. Result:', result);
        $btn.button('reset')

	if (result["loggedIn"]){
	    
	    userid = result["userid"];
        
	    $('#login-icon').removeClass("glyphicon-log-in").addClass("glyphicon-log-out");
	    $('#login-text').text("Log out " + userid);
	    closeNav();
	} else {
  
         mdlInfo.find('.modal-body').text('Please check your username and password!');
         mdlInfo.modal('show');
         $btn.button('reset')                  
	    //alert("Could not log in. Please check your username/password.");
	}
    });
    ajax.fail(function(result){

        console.log('error reaching out to login server!', result);
        mdlInfo.find('.modal-body').text('Error reaching out to login server. Please try again and contact the site administrators if the issue persists');
        mdlInfo.modal('show');
        $btn.button('reset')
    });

});
function openNav() {
    if ($('#login-text').text().indexOf("Log out") >= 0){
	$.ajax({url: "/logout/",
		success: function(result){
		    if (!result["loggedIn"]) {
			$('#login-icon').removeClass("glyphicon-log-out").addClass("glyphicon-log-in");
			$('#login-text').text("Log in");
			userid = "";
		    };
		}})
    } else {
         
	$("#modal-login").modal('show');

    
}
};

function closeNav() {
   // document.getElementById("myNav").style.height = "0%";
   $("#modal-login").modal('hide');
};


