USE client_db; 

CREATE TABLE `client_account`(
	`id` INT(11) auto_increment NOT NULL,
	`username` VARCHAR(256) NOT NULL,
    `pwd_key` VARCHAR(256) NOT NULL, 
    `token` VARCHAR(512) NOT NULL,
    PRIMARY KEY (`id`)
); 

