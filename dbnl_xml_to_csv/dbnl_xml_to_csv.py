import xml.etree.ElementTree as ET
import os
import my_helpers
import entities
from operator import attrgetter
from dbnl_xml_parser import *

output_file = os.path.join(my_helpers.get_script_dir(), 'output.csv')

xml_dir = os.path.join(my_helpers.get_script_dir(), '..\\testbestanden') #'test_xml_weinig_files')

for f in my_helpers.get_files_from_dir_r(xml_dir, '.xml'):
    #print("Now processing: '{}'".format(f))
    parsedFile = entities.ParsedFile(f)
    
    tree = ET.parse(f)
    root = tree.getroot()
    
    set_author(root, parsedFile)
    set_title(root, parsedFile)
    set_publication_idno(root, parsedFile)
    set_used_copy(root, parsedFile)
    set_publisher(root, parsedFile)
    set_year_published(parsedFile)

    parsedFile.print()

print ('done!')
            