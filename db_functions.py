import sqlite3

"""
    Class to handle basic functions with the sqlite db
    
    TODO: error handling
"""
class db_wrapper:
    def __init__(self, db_path):
        #no damn auto-commit here, and I don't put cream in my coffee neither
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
    
    #things ran initially by the first setup script
    #---------------------------------------------------#
    
    def add_user(self, username):
        params = (username,)
        sql = """insert into users (name) values (?)"""
        self.cursor.execute(sql, params)
        self.conn_obj.commit()
        
    def send_data():
        pass
        
    #things used only by utilities and such. 
    #--------------------------------------------------#
    
    def get_user(self, username):
        params = (username,)
        sql = """select * from users where name = ?"""   
        self.cursor.execute(sql, params)
        return self.cursor.fetchone()
        
    
        
        
    