import sys, string
from xml.dom import minidom, Node

def walk(parent, outFile):                               # [1]
    for node in parent.childNodes:
        if node.nodeType == Node.ELEMENT_NODE:
            # Write out the element name.
            outFile.write('Element: %s\n' % node.nodeName)
            # Walk over any text nodes in the current node.
            content = []                                        # [3]
            for child in node.childNodes:
                if child.nodeType == Node.TEXT_NODE:
                    content.append(child.nodeValue)
            if content:
                strContent = string.join(content)
                outFile.write('Content: "')
                outFile.write(strContent)
                outFile.write('"\n')
            # Walk the child nodes.
            walk(node, outFile)

def run(inFileName):                                            # [5]
    outFile = sys.stdout
    doc = minidom.parse(inFileName)
    rootNode = doc.documentElement.childNodes[1]
    walk(rootNode, outFile)

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print 'usage: python test.py infile.xml'
        sys.exit(-1)
    run(args[0])


if __name__ == '__main__':
    main()

