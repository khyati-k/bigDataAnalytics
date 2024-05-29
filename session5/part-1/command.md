gcloud config set project <PROJECT_ID>
gcloud sql connect <SQL-SERVER> --user=root

CREATE DATABASE film_db;
SHOW DATABASES;

CREATE TABLE actors (
actor_id INT(6),
actor_first_name VARCHAR(30),
actor_last_name VARCHAR(30),
actor_city VARCHAR(20),
PRIMARY KEY (actor_id)
);

DESCRIBE actors;

INSERT INTO actors (actor_id, actor_first_name, actor_last_name, actor_city) 
VALUES 	(1, 'Tom', 'Hanks', 'Los Angeles');

clear the terminal by pressing `ctl`+`L`

 ALTER TABLE actors ADD salary INT(10);

 part 1 completed!!