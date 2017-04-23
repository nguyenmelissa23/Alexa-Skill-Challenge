'use strict';

//REQUIRE NODE PACKAGES
const Alexa = require('alexa-sdk');

//DO WE NEED THIS
var APP_ID;

//ENGLISH ONLY for now
const languageStrings = {
    'en-US': {
        translation:{
            STATUS: 'You have successfully pulled your repository.',
            SKILL_NAME: 'Git Hub Voice', 
            GET_STATUS_MESSAGE: 'Here is your git status',
            HELP_MESSAGE: 'You can say git pull',
            HELP_REPROMPT: 'What can I help you with?',
            STOP_MESSAGE: 'Goodbye!'
        }
    }
};


//CREATE HANDLERS:
const handlers = {
    'LaunchRequest': function(){
        this.emit('GitPull');
    },

    'GetNewPullIntent': function(){
        this.emit('GitPull');
    }, 

    'GitPull': function(){
        let speechOutput = this.t('GET_STATUS_MESSAGE') + this.t('STATUS');
        this.emit(':tell', this.t('STATUS'));
    }, 

    'AMAZON.HelpIntent': function(){
        let speechOutput = this.t('HELP_MESSAGE');
        const reprompt = this.t('HELP_MESSAGE');
        this.emit(':ask', speechOutput, reprompt);
    }, 

    'AMAZON.CanceIntent': function(){
        this.emit(':tell', this.t('STOP_MESSAGE'));
    }, 

    'AMAZON.StopIntent': function(){
        this.emit(':tell', this.t('STOP_MESSAGE'));
    },

    'SessionEndedRequest': function(){
        this.emit(':tell', this.t('STOP_MESSAGE'));
    }
};

exports.handler = (event, context) => {
    const alexa =Alexa.handler(event,context);
    alexa.resources = languageStrings;
    alexa.registerHandlers(handlers);
    alexa.execute();
};