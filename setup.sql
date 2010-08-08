
CREATE TABLE songs (
    id INTEGER PRIMARY KEY NOT NULL,
    title TEXT NOT NULL, 
    artist TEXT,
    album TEXT,
    creation_date DATE DEFAULT (datetime('now','localtime'))
) 

CREATE TABLE users (
    id INTEGER PRIMARY KEY NOT NULL,
    name varchar(60) UNIQUE NOT NULL
)

#central
CREATE TABLE user_songs (
    song_id INTEGER NOT NULL,
    user_id varchar(60) NOT NULL,
    PRIMARY KEY (song_id, user_id)
)

#Sorry dbahulk!
#NOT 1986 SQL NO LONGER NEED LOOK LIKE COBOL. EASE UP ON CAPS.


#Ran using sqlite 3.4.0
