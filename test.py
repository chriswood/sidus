import sys
from xml.dom import minidom, Node

def showNode(node):
    if node.nodeType == Node.ELEMENT_NODE:
        print 'Element name: %s' % node.nodeName
        for (name, value) in node.attributes.items():
            print '    Attr -- Name: %s  Value: %s' % (name, value)
        if node.attributes.get('ID') is not None:
            print '    ID: %s' % node.attributes.get('ID').value

def main():
    doc = minidom.parse(sys.argv[1])
    node = doc.documentElement.childNodes[1]
    node = node.childNodes[1]
    showNode(node)
    for child in node.childNodes:
        showNode(child)

if __name__ == '__main__':
    main()

