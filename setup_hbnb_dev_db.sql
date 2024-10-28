-- Drop the database and tables if they exist
DROP DATABASE IF EXISTS hbnb_dev_db;

-- Create the development database
CREATE DATABASE hbnb_dev_db;

-- Use the newly created database
USE hbnb_dev_db;

-- Create the states table
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128) NOT NULL
);

-- Create the cities table
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(128) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);