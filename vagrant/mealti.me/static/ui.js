$(document).ready(function(){
	$("div#customBtn").click(function(){
		Login.connect();
	});
});

var UI = {
	updateLogIn: function(){
		$('img.user-info').attr("src", localStorage.getItem("picture")).html("Welcome " + localStorage.getItem("email"));
	}
}
