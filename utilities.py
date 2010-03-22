import os
import sys
from db_functions import db_wrapper
import ConfigParser

settings = ConfigParser.RawConfigParser()
settings.read('settings.py')

def user_exists(username):
    '''
        just a boolean yay or nay for whether a user already exists
    '''
    db = db_wrapper(get_db_path('central'))
    return(not (db.get_user(username) == None))
    
def get_db_path(db):
    '''
        takes a string db name for a parameter and returns the corresonding
        connection, either 'central' or 'local'
    '''
    return(settings.get('db_settings', '_'.join((db,'db_path'))))
    
def set_up_dir(user):
    '''
        cleans out the directory if it exists, and creates it if not
    '''
    local_db_path = settings.get('db_settings', 'local_db_dir')
    if os.path.isdir(local_db_path):
        files = os.listdir(local_db_path)
        for file in files:
            if file == '.' or file == '..': 
                continue
            path = local_db_path + os.sep + file
            print("removing file %s ..." %(path))
            os.unlink(path)
    else:
        print("Creating directory %s ..." %(local_db_path))
        os.mkdir(local_db_path)
    
def raise_error(err_type, message):
    '''
        handles all command line, non python exception raising errors
    '''
    error_str = "An error of type %s has occured.\n%s" %(err_type, message)
    print(error_str)
    sys.exit(0)
    
def set_up_local_db(user):
    '''
        sets up local sqllite db, and adds the songs table
    '''
    local_path = get_db_path('local')
    local_db = db_wrapper(local_path)
    local_db.create_songs_table()
    
    
