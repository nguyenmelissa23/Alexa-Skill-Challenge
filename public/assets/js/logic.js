//This is to register:
$("#submitRegister").on("click", function(){
    $.ajax({
            url: "https://rmkw7wi6z9.execute-api.us-west-1.amazonaws.com/Production/users", //api url
            method: "POST",
            data: {
                username: $("#registerUsername"),
                password: $("#registerPassword")
            }})
        .done(function(msg){
            console.log(msg);
    });
});

    

//This is to login:
// $.ajax({
//         url: "https://rmkw7wi6z9.execute-api.us-west-1.amazonaws.com/Production/users", //api url
//         method: "POST",
//         data: {
//             username: $("#createUsername"),
//             password: $("#createPassword")
//         }
//         })
//     .done(function(msg){
//         console.log(msg);
// });

