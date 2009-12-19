import sys, string
from xml.dom import minidom, Node

#user = sys_argv[1]
user = 'cwood'
user_info = {}
def parse_document(filename):
    return minidom.parse(filename)

try:
    # tunes_file = parse_document("/Users/%s/Music/iTunes/iTunes Music Library.xml" % user)
    tunes_file = parse_document("/Users/%s/Music/iTunes/test.xml" % user)
except:
    print("Could not locate itunes info for %s" % user)
    raise IOError()
    
#first get the main appleish node, which everything else is inside
plist = tunes_file.childNodes[1]

#info is the main <dict> node that holds the basic library
#information, and all the songs
info = plist.childNodes[1]

#first get the basic file/user info
print("------------------------------------------------------")
#counter is just in case there is some weird file that is messed up we don't want
#to get in some obnoxious loop, the main info shouldn't be more than like 20 nodes deep
x = 1
for node in info.childNodes:
    if x < 20:
        if node.nodeType == Node.ELEMENT_NODE:
            #print node.nodeName
            for child in node.childNodes:
                if child.nodeType == Node.TEXT_NODE and child.nodeValue != 'Playlists':
                    print(x%2)
                    print(child.nextSibling)
                    print(child.nodeValue)
                    # if x%2==0 and child.nextSibling != None:
                    #     #print(child.nodeValue)
                    #     valueNode = child.nextSibling
                    #     user_info[child.nodeValue] = valueNode.nodeValue
        x = x + 1
    else:
        break


        
print(user_info)

    

    
#cFile = open("../ctunes/test.xml","r")

