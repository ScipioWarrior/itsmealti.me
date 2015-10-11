var Login = {
	
	/*
	* Holds info for the logged-in user's Google acc.
	* email is their email address, name is their full name, picture is a link to their profile pic
	*/
	sessionInfo: {
		email: "",
		name: "",
		picture: ""
	},
	
	/*
	* Makes the inital log in request, asking for an OAuth 2.0 token
	*/
	connect: function(){
		
		/*$.ajax({
			url: "https://accounts.google.com/o/oauth2/auth",
			data: {
				response_type: "token",
				client_id: "665577778199-dnfk2bkeb7s2c0esl6gomd0cvvubskur.apps.googleusercontent.com",
				
				// Change this line for production
				redirect_uri: "http://mealtime.elasticbeanstalk.com/start",
				dataType: "jsonp",
				
				scope: "email profile",
				approval_prompt: "force"
			},
				
			// Redirects user to give permissions to their Google account
			success: function(){
				window.location.href = this.url;
			},
			error: function(){
				console.log("Houston, we've got a problem");
			}
		});*/
		window.location.href = "https://accounts.google.com/o/oauth2/auth?response_type=token&client_id=665577778199-dnfk2bkeb7s2c0esl6gomd0cvvubskur.apps.googleusercontent.com&redirect_uri=http%3A%2F%2Fmealtime.elasticbeanstalk.com%2Fstart&scope=email+profile&approval_prompt=force";
	},
	
	/*
	* For security reasons, verifies the auth. token we recieved from the Login.connect() method
	* Returns a JSON object that on success, gives a bunch of useless info, and on failure, gives an error description
	*/
	verify: function(token){		
		$.ajax({
			url: "https://www.googleapis.com/oauth2/v1/tokeninfo",
			data: {
				access_token: token
			},
			
			success: function(response){
				console.log("We have the token!");
				Login.getInfo(token);
			},
			
			error: function(){
				console.log("Cannot verify token");
			},
		});
	},
	
	/*
	* Populates the Login.session{} object for the user using the auth token
	*/
	getInfo: function(token){
		console.log(token);
		$.ajax({
			url: "https://www.googleapis.com/userinfo/v2/me",
			data:{
				access_token: token
			},
			success: function(response){
				session["email"] = response["email"];
				session["name"] = response["name"];
				session["picture"] = response["picture"];
			},
			error: function(){
				console.log("Couldn't retrieve email info");
			}
		});
	}	
}