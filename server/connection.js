// Set up MySQL connection.
var mysql = require("mysql");

var connection = mysql.createConnection({
  port: 3306,
  host: "rds-mysql-githubvoice.cegdamzfrq7x.us-east-1.rds.amazonaws.com",
  user: "xpression",
  password: "xpression",
  database: "client_db"
});

// Make connection.
connection.connect(function(err) {
  if (err) {
    console.error("error connecting: " + err.stack);
    return;
  }
  console.log("connected as id " + connection.threadId);
});

// Export connection for our ORM to use.
module.exports = connection;