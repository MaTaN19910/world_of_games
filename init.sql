-- init.sql
CREATE SCHEMA games;
CREATE TABLE games.users_scores (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    score INT
);