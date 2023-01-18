DROP DATABASE IF EXISTS pycrud;

CREATE DATABASE pycrud;

USE pycrud;

CREATE TABLE IF NOT EXISTS users(
    id INT AUTO_INCREMENT NOT NULL,
    username NVARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (email)
);

INSERT INTO users(username, email) VALUES ('Barry', 'barry@allen.com');
