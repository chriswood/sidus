from db_functions import db_wrapper
import ConfigParser

settings = ConfigParser.RawConfigParser()
settings.read('settings.py')
db_path = settings.get('db_settings','path')

db = db_wrapper(db_path)

#just a boolean yay or nay for whether a user already exists
def user_exists(username):
    user = db.get_user(username)
    
    if user == None:
        return False
    return True
    
def get_db_path():
    return(db_path)
    
    
