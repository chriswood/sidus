
import sys
import os
import pwd
import xml.sax.handler
from db_functions import db_wrapper
from parser import ITunesHandler, Track
from utilities import user_exists, get_db_path, raise_error, set_up_dir, set_up_local_db

#TODO implement option parser
if len(sys.argv) > 1:
    user = sys.argv[1]
else:
    #unless a user is specified, get the one who started this process
    user = pwd.getpwuid(os.getuid())[0]
   
db_path = get_db_path('central')   

parser = xml.sax.make_parser() 
handler = ITunesHandler() 
parser.setContentHandler(handler) 
file_location = "/Users/%s/Music/iTunes/iTunes Music Library.xml" % user

central_db = db_wrapper(db_path)

#Is this a new user? Wipe out any existing db if so
if not user_exists(user):
    #--------------------First Time User--------------------
    #check if this is a legit user for this machine
    if not os.path.isdir('/Users/%s' %(user)):
        raise_error('Invalid User',"This machine does not have have the user %s" %(user))

    confirm = raw_input('''****************************************************
The directory /Users/%s/sidus/ is about to be created, if it already exists
it will be destroyed. Keep going? (y/n)''' % (user))

    if confirm[0].lower() == 'y':
        #add the guy
        central_db.add_user(user)
        
        # set up directory
        set_up_dir(user)
        
        #create local db
        set_up_local_db(user)

    else:
        raise_error('abort', '\nSidus user creation has been cancelled.\n')

        
#do a full parse of the itunes xml
parser.parse(file_location) 

#now we have a list of Track class objects in handler.tracks,
#so we can update the local db
local_path = get_db_path('local')
local_db = db_wrapper(local_path)

for track in handler.tracks:
    #handle song...
    local_db.process_song_local(user, track)
    
    #then update the central db
    #I guess there will be a button or something for "update main db"
              
