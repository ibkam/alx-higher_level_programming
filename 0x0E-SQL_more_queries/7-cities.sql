-- creates the database hbtn_0d_usa and the table states
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
	PRIMARY (`id`),
	`id` INT UNIQUE NOT NULL AUTO_INCREMENT,
  `state_id` INT NOT NULL,
	`name` VARCHAR(256) NOT NULL
  FOREIGN KEY (`state_id`) REFERENCE `hbtn_0d_usa`.`state`(`id`)
	);
