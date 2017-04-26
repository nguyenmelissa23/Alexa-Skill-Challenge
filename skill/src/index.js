"use strict";

const Alexa = require("alexa-sdk");
var APP_ID = undefined;

const app = {
    skillname: "Git Hub Voice",
    WELCOME_MESSAGE: "Welcome to Git Hub Voice. You can say a git command to start.",
    REGISTER_ACCOUNT_MESSAGE: "Welcome to Git Hub Watch. I see that you have not linked your Git Hub Watch account with your Alexa App.",
    REGISTER_DEVICE_MESSAGE: "Please register your devices to start watching your repositories.",
    DESCRIPTION_STATE_HELP_MESSAGE: "Here are somethings you can say: Watch repo Homeword 12, Git pull, Git push", 
    SHUTDOWN_MESSAGE: "Goodbye", 
    EXIT_SKILL_MESSAGE: "Exit skill. Goodbye"
};

var states = {
    // REGISTERMODE: "_REGISTERMODE", 
    // DESCRIPTION: "_DESCRIPTION", 
    COMMANDMODE: "_COMMANDMODE"
};

const newSessionHandlers = {
    "LaunchRequest": function(){
        this.handler.state = states.COMMANDMODE;
        this.emit(":ask", app.WELCOME_MESSAGE);
    }, 
    "GitHubVoiceIntent": function(){
        console.log("GitHub Voice Intent");
        this.handler.state = states.COMMANDMODE;
        this.emitWithState("GitHubVoiceIntent");
    },

    "AMAZON.RepeatIntent": function(){
        this.emit(":ask", app.DESCRIPTION_STATE_HELP_MESSAGE);
    },
    "AMAZON.StopIntent": function(){
        this.emit(":ask", app.SHUTDOWN_MESSAGE);
    },
    "AMAZON.CancelIntent": function(){
        this.emit(":ask", app.EXIT_SKILL_MESSAGE );
    },
    "SessionEndedRequest": function(){
        this.emit("AMAZON.StopIntent");
    }, 
    "Unhandled": function(){
        this.handler.state = states.COMMANDMODE;
        this.emitWithState("GitCommandIntent");
    }
};

var gitCommandHandlers = Alexa.CreateStateHandler(states.COMMANDMODE,{
    "GitCommandIntent": function(){
        gitCommandIntentHandler.call(this);
    },
    "AMAZON.RepeatIntent": function(){
        this.emit(":ask", app.DESCRIPTION_STATE_HELP_MESSAGE);
    },
    "AMAZON.StopIntent": function(){
        this.emit(":ask", app.SHUTDOWN_MESSAGE);
    },
    "AMAZON.CancelIntent": function(){
        this.emit(":ask", app.EXIT_SKILL_MESSAGE );
    },
    "SessionEndedRequest": function(){
        this.emit("AMAZON.StopIntent");
    }, 
    "Unhandled": function(){
        console.log("Unhandled intent in gitCommandHandlers");
        this.emit(":ask",app.DESCRIPTION_STATE_HELP_MESSAGE);
    }
});


function gitCommandIntentHandler(){
    if (this.event.request.intent.slots.command.value){
        var gitCommand = this.event.request.intent.slots.command.value;
        console.log("gitCommand", gitCommand);
        this.emit(":tell", "You said " + gitCommand);
    } else 
        this.emit(":tell", "No command was found");
}

exports.handler = function(event, context, callback){
    var alexa = Alexa.handler(event, context);
    alexa.appId = APP_ID;
    alexa.registerHandlers(newSessionHandlers, gitCommandHandlers);
    alexa.execute();
};