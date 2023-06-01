-- creates the database hbtn_0d_usa and the table states
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTs `hbtn_0d_usa`.`state` (
	PRIMARY(`id`),
	`id` INT UNIQUE NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(256) NOT NULL
	);
