CREATE TABLE songs (
    id INTEGER PRIMARY KEY NOT NULL,
    title TEXT UNIQUE NOT NULL, 
    artist TEXT,
    album TEXT,
    creation_date DATE DEFAULT (datetime('now','localtime'))
) 

CREATE TABLE users (
    id INTEGER PRIMARY KEY NOT NULL,
    name varchar(60) UNIQUE NOT NULL
)

#Ran using sqlite 3.4.0