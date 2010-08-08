import sys
import sqlite3
import datetime

"""
    Class to handle basic functions with the sqlite db
    
    TODO: error handling
    
"""
class db_wrapper:
    def __init__(self, db_path):
        self.conn_obj = sqlite3.connect(db_path)
        self.cursor = self.conn_obj.cursor()
        
    #things ran regularly
    #---------------------------------------------------#
    
    def get_songs(self):
        sql = 'select * from songs'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
        
    def process_song_local(self, username, track):
        '''Adds song to local db'''
        if not self._song_exists(track.Name, track.Artist):
            self._add_song(track)

    def process_song_central(self, username, track):
        '''
            If this song does not exist at all in central, add it. Then
            handle the user song record
        '''       
        song_id = self._song_exists(track.Name, track.Artist)
        if not song_id:
            song_id = self._add_song(track)
        if not self._user_song_exists(song_id, username):
            self._add_user_song(song_id, username)   
        
    
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
        
    def get_total_changes(self):
        return self.conn_obj.total_changes
        
    #things used only by utilities and such. 
    #--------------------------------------------------#
    
    def get_user(self, username):
        params = (username,)
        sql = """SELECT * FROM users WHERE name = ?"""   
        self.cursor.execute(sql, params)
        return self.cursor.fetchone()
        
    def _song_exists(self, title, artist):
        '''
            If the song name and singer are the same, consider it a dupe. This
            returns None or the id of the song
        '''
        params = (title.lower(), artist.lower(), )
        sql = """SELECT id FROM songs 
                 WHERE LOWER(title) = ?
                 AND LOWER(artist) = ?"""
        
        self.cursor.execute(sql, params)
        song_id = self.cursor.fetchone()
        return(song_id if song_id == None else song_id[0])
    
    def _user_song_exists(self, song_id, user_id):
        params = (song_id, user_id, )
        sql = """SELECT 1 FROM user_songs 
                 WHERE song_id = ?
                 AND user_id = ?"""
        
        self.cursor.execute(sql, params)
        return(self.cursor.fetchone())
        
    def _add_song(self, track):
        print("adding %s" % track.Name)
        params = (track.Name, track.Artist, track.Album)
        sql = """INSERT INTO songs (title, artist, album, creation_date)
                 VALUES (?, ?, ?, datetime('NOW'))"""
                 
        self.cursor.execute(sql, params)
        self.conn_obj.commit()
        return(self.cursor.lastrowid)
    
    def _add_user_song(self, song_id, user_id):
        params = (song_id, user_id)
        sql = """INSERT INTO user_songs (song_id, user_id) VALUES (?, ?)"""           
        self.cursor.execute(sql, params)
        self.conn_obj.commit()
    
    
        
        
    