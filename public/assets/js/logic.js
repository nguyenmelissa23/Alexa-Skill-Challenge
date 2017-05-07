//This is to register:
$("#submitRegister").on("click", function(event){
    event.preventDefault();
    var queryURL =  "https://rmkw7wi6z9.execute-api.us-west-1.amazonaws.com/Production/users";
    var userInfoObj = {
                        "username": $("#registerUsername").val(),
                        "password": $("#registerPassword").val()
                    };

    console.log("queryURL", queryURL);
    console.log("userInfoObj", userInfoObj);


    var request = $.post(queryURL, JSON.stringify(userInfoObj));

    request.done(function(data){
        console.log("request.done");
        console.log(data);
    });

    request.fail(function(data){
        console.log("request.fail");
        console.log(data);
    });
});

    

//This is to login:
$("#submitLogin").on("click", function(event){
    event.preventDefault();
    var queryURL =  "https://rmkw7wi6z9.execute-api.us-west-1.amazonaws.com/Production/alexa";
    var userInfoObj = {
                        "username": $("#loginUsername").val(),
                        "password": $("#loginPassword").val()
                    };

    console.log("queryURL", queryURL);
    console.log("userInfoObj", userInfoObj);


    var request = $.post(queryURL, JSON.stringify(userInfoObj));

    request.done(function(data){
        console.log("request.done");
        console.log(data);
    });

    request.fail(function(data){
        console.log("request.fail");
        console.log(data);
        var alexaQueryString = ""
    });
});
