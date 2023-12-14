-- Script that creates the database hbtn_0d_usa and the table states.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(256) NOT NULL
);
