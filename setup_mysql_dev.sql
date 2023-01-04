--Prepares a MySQL server for the project.
CREATE DATABASE IF NOT EXIST hbnb_dev_db;
CREATE USER IF NOT EXIST 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnd_dev_db.* TO 'hbnd_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnd_dev'@'localhost';

