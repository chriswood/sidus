import sys 
import xml.sax.handler

#ContentHandler is the main built in class
#you are supposed to subclass for sax applications
class ITunesHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.parse = False
        self.tag = '' 
        self.value = '' 
        self.tracks = [] 
        self.track = None 
        
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
            if self.tag == 'Track ID': 
                # start of a new track, so a new object
                # is needed. 
                self.track = Track() 
            elif self.tag == 'Name' and self.track: 
                self.track.track = self.value 
            elif self.tag == 'Artist' and self.track: 
                self.track.artist = self.value 
                #This code assumes Artist is the last thing we want,
                #I need to change this 
                self.tracks.append(self.track) 
                self.track = None 
                
    def characters(self, content): 
        #This takes chunks of data from your document and 
        if self.parse: 
            self.tag = content
            self.value = '' 
        else: 
            # could be multiple lines, so append data.
            self.value = self.value + content
                
class Track: 
    def __init__(self): 
        self.track = '' 
        self.artist = '' 
        
    def __str__(self): 
        return "Track = %s\nArtist = %s" % (self.track,self.artist) 
        
        
parser = xml.sax.make_parser() 
handler = ITunesHandler() 
parser.setContentHandler(handler) 
parser.parse('/Users/cwood/Music/iTunes/test.xml') 

for track in handler.tracks: 
    try:
        print track
    except:
        pass
        
        
        