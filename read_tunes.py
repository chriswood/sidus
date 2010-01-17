import sys 
import xml.sax.handler
from db_functions import db_wrapper
from parser import ITunesHandler, Track

#TODO implement option parser
if len(sys.argv) > 1:
    user = sys.argv[1]
else:
    print("Need user argument, like read_tunes.py <user>") 
    sys.exit()   
      

parser = xml.sax.make_parser() 
handler = ITunesHandler() 
parser.setContentHandler(handler) 
file_location = "/Users/%s/Music/iTunes/test.xml" % user
try:
    parser.parse(file_location) 
except:
    print("Could not open %s" % file_location)
#parser.parse('iTunes\ Music\ Library.xml')

for track in handler.tracks: 
    try:    
        print track
    except:
        pass
        
        
        
