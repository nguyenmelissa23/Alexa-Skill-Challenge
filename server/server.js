const connection = require("./connection");
const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const path = require("path");

const PORT = 3306;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.text());
app.use(bodyParser.json({ type: "application/vnd.api+json" }));
app.use(express.static(__dirname + "/public"));

//Routing 
app.get("/", function(req,res){
    res.sendFile(path.join(__dirname, "/login.html"));
});

app.post("/loggedin", function(request, response){
    console.log("app.get()");
});


//Listen:
app.listen(PORT, function(){
    console.log("Listening on port: " + PORT  + ". http://localhost:" + PORT)
});