//to run, cd to the right folder, type in "npm install"
//next type in "node createAcct.js"

const inquirer = require('inquirer');

userAcct();

function userAcct(){
    inquirer.prompt([{
        'name': 'username', 
        'message': 'Username: '
    },{
        'type': 'password', 
        'name': 'password',
        'message': 'Password: '
    }]).then(function(ans){
        //do something
        console.log('Account created');
        console.log('Username', ans.username);
    });
}