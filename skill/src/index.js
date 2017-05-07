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
    REPOMODE: "_REPOMODE", 
    COMMANDMODE: "_COMMANDMODE"
};

//=============Handlers=======================
const newSessionHandlers = {
    "LaunchRequest": function(){
        checkAlexaToken.call(this);
        this.emit(":ask", app.WELCOME_MESSAGE);
        this.handler.state = states.REPOMODE;
    }, 

    "GitRepoListIntent": function(){
        console.log("Git Repo List Intent");
        this.handler.state = states.REPOMODE;
        this.emitWithState("GitRepoListIntent");
        // this.handler.state = states.COMMANDMODE;
    },

    "GitCommandIntent": function(){
        console.log("GitHub Voice Intent");
        this.handler.state = states.COMMANDMODE;
        this.emitWithState("GitCommandIntent");
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
        this.handler.state = states.REPOMODE;
        this.emitWithState("GitRepoListIntent");
    }
};

var gitCommandHandlers = Alexa.CreateStateHandler(states.COMMANDMODE,{
    "GitCommandIntent": function(){
        checkAlexaToken.call(this);
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

var gitRepoHandlers = Alexa.CreateStateHandler(states.REPOMODE,{
    "GitRepoListIntent": function(){
        checkAlexaToken.call(this);
        gitRepoList.call(this);
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

//FUNCTIONS

function gitRepoList(){
    var queryURL =  "https://rmkw7wi6z9.execute-api.us-west-1.amazonaws.com/Production/repositories/get";
    var alexaToken;
    if (this.event.session.user.accessToken){
        alexaToken = this.event.session.user.accessToken;
        this.emit(":tell", "Alexa token is available");
    } else {
        this.emit(":tell", "Unable to get Alexa token");
    }
     
    console.log(alexaToken);

    var request = $.post(queryURL, JSON.stringify(alexaToken));

    request.done(function(data){
        console.log("request.done");
        console.log(data);

        this.emit(":tell", "Here are your repositories");
    });

    request.fail(function(data){
        console.log("request.fail");
        console.log(data);
        
        
    });
}

function checkAlexaToken(){
    if (this.event.session.user.accessToken == undefined){
        this.emit(":tellwithLinkAccountCard", "To start using this app, please use the Alexa app to authenticate on Amazon");
    } 
    return;
}

function gitCommandIntentHandler(){
    if (this.event.request.intent.slots.command.value){
        var gitCommand = this.event.request.intent.slots.command.value;
        var gitRepo = this.event.request.intent.slots.repo.value;
        console.log("gitCommand", gitCommand, gitRepo);
        this.emit(":tell", "You said git" + gitCommand + gitRepo);
    } else 
        this.emit(":tell", "No command was found");
}

exports.handler = function(event, context, callback){
    var alexa = Alexa.handler(event, context);
    alexa.appId = APP_ID;
    alexa.registerHandlers(newSessionHandlers,gitRepoHandlers, gitCommandHandlers);
    alexa.execute();
};