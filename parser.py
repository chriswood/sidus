import xml.sax.handler

#ContentHandler is the main built in class
#to subclass for sax applications
#booted element tree
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
            
    def endElement(self, name):
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

