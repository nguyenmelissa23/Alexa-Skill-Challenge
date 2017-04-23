const inquirer = require('inquirer');

function userAcct(){
    inquirer.prompt([{
        type: 'input',
        name: 'username',
        message: 'Username: '
    },{
        type: 'password', 
        name: 'password',
        message: 'Password: '
    }]).then(function(ans){
        //do something
        console.log('Account created');
        console.log('Username', ans.username);
    });
}