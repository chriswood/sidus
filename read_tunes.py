import sys 
import xml.sax.handler

#Need to implement option parser
if len(sys.argv) > 1:
    user = sys.argv[1]
else:
    print("Need user argument") 
    sys.exit()   
    
#ContentHandler is the main built in class
#you are supposed to subclass for sax applications
class ITunesHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.parse = False
        self.tag = '' 
        self.value = '' 
        self.tracks = [] 
        self.track = None 
        #probably a better way to prevent handling unwanted things...
        self.first_key = 'Track ID'
        self.last_key = 'Album'
        #This is where you put what you want to store
        self.wanted_info = ['Artist', 'Name', self.last_key]

    def skippedEntity(self, name):
        #This gets called whenever an element is not parsed. 
        #If we have to skip a song for some reason, this would
        #be nice to keep somewhere in a log. For now I'm just 
        #printing it out
        if name == 'key':
            print "hey man we are skipping %s" (name)
        
    def startElement(self, name, attrs):
        #method to signify the start of an element, when you
        #aren't using namespacing 
        #I plan on implementing some other stuff to handle like the
        #user name and version stuff also in the xml file
        if name == 'key': 
            self.parse = True 
            
    def endElement(self,name):
        if name == 'key': 
            self.parse = False 
        else: 
            info_type = getattr(self, 'tag')
            if info_type == self.first_key: 
                # start of a new track, so a new object is needed. 
                self.track = Track() 
            elif self.track and info_type in self.wanted_info: 
                #if we have a legit track, and we want this info stored
                setattr(self.track, info_type, self.value)
                
            if info_type == self.last_key:
                self.tracks.append(self.track) 
                self.track = None 
                         
    def characters(self, content): 
        #This takes chunks of data from your document, various amounts at a time
        if self.parse: 
            self.tag = content
            self.value = '' 
        else: 
            self.value = self.value + content
                
class Track: 
    def __init__(self): 
        self.Name = '' 
        self.Artist = '' 
        self.Album = ''
        
    def __str__(self): 
        return "---------------------------------\
                \nTrack: %s\nArtist: %s\nAlbum: %s"\
                 % (self.Name, self.Artist, self.Album) 
        
        
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
        
        
        
