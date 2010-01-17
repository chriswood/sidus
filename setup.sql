CREATE TABLE songs (
    id INTEGER PRIMARY KEY NOT NULL,
    title TEXT UNIQUE NOT NULL, 
    artist TEXT,
    album TEXT,
    creation_date DATE DEFAULT (datetime('now','localtime'))
) 

#Ran using sqlite 3.4.0