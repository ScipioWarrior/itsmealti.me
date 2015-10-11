$(document).ready(function(){
	$("div#customBtn").click(function(){
		Login.connect();
	});
});

var UI = {
	showLogInfo: function(){
		$("img.user-info").attr("src", localStorage.getItem("picture"));
		$("p.user-info").html("Welcome " + localStorage.getItem("name") + "<br />" + localStorage.getItem("email"));
	},

	restaurantHandler: function(){
		
	}
};