-- This script sets up the MySQL development environment

-- Create the development database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the development user with a password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges on the development database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;

-- Create the states table
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128) NOT NULL
);
