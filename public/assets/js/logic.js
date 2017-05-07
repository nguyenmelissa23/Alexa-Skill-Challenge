console.log(document.location.href);

var parseQueryString = function() {

    var str = window.location.search;
    var objURL = {};

    str.replace(
        new RegExp( "([^?=&]+)(=([^&]*))?", "g" ),
        function( $0, $1, $2, $3 ){
            objURL[ $1 ] = $3;
        }
    );
    return objURL;
};
var urlObject = parseQueryString();

console.log(urlObject.redirect_uri);



// let params = (window.location).searchParams;
// let alexaURI = params.get("redirect_uri");
// console.log(alexaURI);
// function getQueryStringValue (key) {  
//   return decodeURIComponent(window.location.search.replace(new RegExp("^(?:.*[&\\?]" + encodeURIComponent(key).replace(/[\.\+\*]/g, "\\$&") + "(?:\\=([^&]*))?)?.*$", "i"), "$1"));  
// }  

// var queryString = getQueryStringValue();
// console.log(queryString);

// let searchParams = new URLSearchParams(paramsString);
// console.log(searchParams);



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
        var redirectQueryString = urlObject.redirect_uri + "#";
            redirectQueryString += "state=" + urlObject.state;
            redirectQueryString += "&access_token=" + data.token;
            redirectQueryString += "&token_type=bearer";
        window.location.assign(redirectQueryString);
    });

    request.fail(function(data){
        console.log("request.fail");
        console.log(data.token);
        
        
    });
});
