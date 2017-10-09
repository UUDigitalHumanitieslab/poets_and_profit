import os
import html
from my_helpers import *
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError

args = sys.argv

def print_usage():
    print("    ******     Remove HTML-entities from xml      ******")
    print("    Removes html entities from xml and writes result to new file (of same name)")
    print("    Note that the result will be parsed to (an) xml (object),")
    print("    and that any errors occuring during this process will be printed in the end")
    print("\n")
    print("    USAGE:")
    print("    remove_html_entities_from_xml.py [input_folder] [output_folder]")
    print("    Example: remove_html_entities_from_xml.py \"C:\\inputfiles\" \"C:\\outputfiles\"")
    print("\n")
    exit(1)

def check_folder_exists(folder):
    if not os.path.isdir(folder):
        print("'{}' is not a folder".format(folder))
        print_usage()

# validate args
if len(args) == 2 and (args[1] in ['?', '-?', 'help', '-help']):
    print_usage()
elif len(args) != 3:
    print("incorrect number of arguments")
    print_usage()

input_folder = args[1]
check_folder_exists(input_folder)

result_folder = args[2]
check_folder_exists(result_folder)

input_files = get_files_from_dir(input_folder)

problems_found = []

for mfilename in input_files:
    if mfilename.endswith('.xml'):
       original_file = path.join(input_folder, mfilename) 

       # bestand opschonen en nieuw bestand terug geven
       with  open(original_file,'r', encoding='utf8') as inputFile:
            resultfile = path.join(result_folder, mfilename)
            
            print ("Now processing: '{}'".format(mfilename))
            
            with open(resultfile, 'w', encoding='utf8') as result:
                for line in inputFile.readlines():
                    new_line = replace_html_entities(line)
                    result.write(new_line)

                try:
                    tree = ET.parse(resultfile)
                except ParseError as e:
                    error = e.msg.__str__()
                    if (error.startswith('undefined entity')):
                        problems_found.append(e.msg)
                        print(error)

print ('done!')

for e in problems_found:
    print(e)



