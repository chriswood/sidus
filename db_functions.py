import sqlite3

"""
    Class to handle basic functions with the sqlite db
    
    TODO: error handling
    
    Right now all of these functions pertain to the main db, which will be on
    a central server
"""
class db_wrapper:
    def __init__(self, db_path):
        self.conn_obj = sqlite3.connect(db_path)
        self.cursor = self.conn_obj.cursor()
        
    #things ran regularly
    #---------------------------------------------------#
    
    #probably need to do some paging. I'm not sure but I don't think
    #I can avoid the total result load, like in sqlalchemy when you
    #avoid the .all() and just get what you need
    def get_songs(self):
        sql = 'select * from songs'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
        
    #this one will take the user's xml info and update the central db
    def update_data():
        pass
        
    def process_song_local(self, username, track):
        #First check to see if this user has previously added this song

        if self._user_has_song(track.Name, track.Artist):
            return
        
        #add to users local db
        self._add_song(track)
        return
    
    #things ran initially by the first setup script
    #---------------------------------------------------#
    
    def add_user(self, username):
        params = (username,)
        sql = """insert into users (name) values (?)"""
        self.cursor.execute(sql, params)
        self.conn_obj.commit()
        
    def create_songs_table(self):
        sql = """CREATE TABLE songs(
            id INTEGER PRIMARY KEY NOT NULL,
            title TEXT NOT NULL,
            artist TEXT,
            album TEXT,
            creation_date DATE DEFAULT (datetime('now','localtime'))
        )"""
        self.cursor.execute(sql)
        self.conn_obj.commit()
        
    #things used only by utilities and such. 
    #--------------------------------------------------#
    
    def get_user(self, username):
        params = (username,)
        sql = """SELECT * FROM users WHERE name = ?"""   
        self.cursor.execute(sql, params)
        return self.cursor.fetchone()
        
    def check_dup(self, title, artist):
        return False
        
    def _user_has_song(self, title, artist):
        '''
            If the song name and singer are the same,
            consider it a dupe
        '''
        params = (title.lower(), artist.lower(), )
        sql = """SELECT 1 FROM songs 
                 WHERE LOWER(title) = ?
                 AND LOWER(artist) = ?"""
        
        self.cursor.execute(sql, params)
        return(self.cursor.fetchone())
        
    def _add_song(self, track):
        print(track.Name)
        import datetime
        params = (track.Name, track.Artist, track.Album)
        sql = """INSERT INTO songs (title, artist, album, creation_date)
                 VALUES (?, ?, ?, datetime('NOW'))"""
                 
        self.cursor.execute(sql, params)
        self.conn_obj.commit()
        return True
    
    
        
        
    