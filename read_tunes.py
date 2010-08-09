
import sys
import os
import pwd
import xml.sax.handler
from db_functions import db_wrapper
from parser import ITunesHandler, Track
from utilities import user_exists, get_db_path, raise_error, set_up_dir, set_up_local_db
from central_handler import tunes_central
import ConfigParser

settings = ConfigParser.RawConfigParser()
settings.read('settings.py')

#TODO implement option parser (soon this sucks)
#########################################################
user = sys.argv[2] if len(sys.argv) > 2 else pwd.getpwuid(os.getuid())[0]
    
#first argument is ignore or update depending on whether you want to
#update the central server
if not (len(sys.argv) > 1 and sys.argv[1] in ['ignore', 'update']):
    print('Use format read_tunes.py [(ignore, update)] [user](default is current)')
    sys.exit(0)
else:
    update_main = True if sys.argv[1] == 'update' else False
#end ugliness
#########################################################

parser = xml.sax.make_parser() 
handler = ITunesHandler() 
parser.setContentHandler(handler) 
path = settings.get('itunes_data', 'path')
#path = settings.get('itunes_data', 'path_test') TEST
file_location = "/Users/%s/%s" % (user, path)
#file_location = "/Users/%s/%s" % ('cwood', path) TEST
db_path = get_db_path('central')   
central_db = db_wrapper(db_path)

#Is this a new user in the central db? Wipe out any existing local db if so
if not user_exists(user):
    #--------------------First Time User--------------------
    confirm = raw_input('''****************************************************
The directory /Users/%s/sidus/ is about to be created, if it already exists
it will be destroyed. Keep going? (y/n)''' % (user))

    if confirm[0].lower() == 'y':
        central_db.add_user(user)
        set_up_dir(user)
        set_up_local_db(user)
    else:
        raise_error('abort', '\nSidus user creation has been cancelled.\n')
        
#do a full parse of the itunes xml
parser.parse(file_location) 

#now we have a list of Track class objects in handler.tracks,
#so we can update the local db
#testing campfire
local_db = db_wrapper(get_db_path('local'))
central_db = db_wrapper(get_db_path('central'))

if update_main == 'update':
    main_handler = tunes_central()

for track in handler.tracks:
    #handle song...
    local_db.process_song_local(user, track)
    if update_main:
        central_db.process_song_central(user, track)

if update_main:
    print("There were %s rows updated in the central database." % central_db.get_total_changes())

