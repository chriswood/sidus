import sqlite3

"""
    Class to handle basic functions with the sqlite db
    
    TODO: error handling
"""
class db_wrapper:
    def __init__(self, db_path):
        conn = sqlite3.connect(db_path)
        self.c = conn.cursor()
        
    
        
        
    