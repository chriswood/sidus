#This is the file that will get ran initially by the user.
#things it does...
#    (1) parse your itunes xml file
#    (2) if that is cool, add your user (right now your profile username)
#            I know this sucks it'll get changed, I hate having to use that
#    (3) send all your info to the central server
#    (4) ...

import sys 
import xml.sax.handler
from db_functions import db_wrapper
from parser import ITunesHandler, Track
from utilities import user_exists, get_db_path

#TODO implement option parser
if len(sys.argv) > 1:
    user = sys.argv[1]
else:
    print("Need user argument, like read_tunes.py <user>") 
    sys.exit()   
   
db_path = get_db_path()   

parser = xml.sax.make_parser() 
handler = ITunesHandler() 
parser.setContentHandler(handler) 
file_location = "/Users/%s/Music/iTunes/iTunes Music Library.xml" % user

try:
    parser.parse(file_location) 
except:
    print("Could not open %s" % file_location)

tunes_db = db_wrapper(db_path)
# songs = tunes_db.get_songs()
# 
# for song in songs:
#     print(song)
# 
# if not user_exists(user):
#     tunes_db.add_user(user)
# else:
#     print("There is already a user with that name. ")
    
for track in handler.tracks: 
    try:    
        print track
    except:
        pass
        
        
        
