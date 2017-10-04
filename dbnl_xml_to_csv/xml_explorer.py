import xml.etree.ElementTree as ET
import os
from helpers.my_helpers import *
from helpers.entities import *

output_file = os.path.join(get_script_dir(), 'output.txt')

xml_dir = os.path.join(get_script_dir(), '..\Testbestandenmappie')
files = get_files_from_dir(xml_dir)

exploration_result = ExplorationResult()

def processChildren(xml_node, node_object):    
    for child in xml_node:
        mSubnode = SubNode(child.tag)
        node_object.add_subnode(mSubnode)

def processNode(xml_node, parentdepth, parentpath):
    #print("Now processing node: '{}'".format(xml_node.tag))
    currentpath = "{}/{}".format(parentpath, xml_node.tag)
    currentdepth = parentdepth + 1

    mNode = Node(xml_node.tag, currentdepth, currentpath)
    exploration_result.add_node(mNode)
    processChildren(xml_node, mNode)

    for child in xml_node:        
        processNode(child, currentdepth, currentpath)

for f in files:
    if f.endswith('.xml'):        
        print("Now processing: '{}'".format(f))
        
        tree = ET.parse(f)
        root = tree.getroot()
        
        for xml_child in root:
            processNode(xml_child, 1, 'root')

with open(output_file, 'a') as f:
    exploration_result.print(f)

print("done!")
    