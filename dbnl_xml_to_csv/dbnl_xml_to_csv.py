import xml.etree.ElementTree as ET
import os
import sys
import csv
import my_helpers
from entities import ParsedFile
from operator import attrgetter
from dbnl_xml_parser import *

def print_usage():
    print("    ******     DBNL-XML TO CSV      ******")
    print("    dbnl_xml_to_csv.py [input_folder] [output_file] optional: [-chapters]")
    print("    Provide the 'chapters' argument to print each chapter on a separate line in the csv")
    print("    Example: dbnl_xml_to_csv.py \"C:\\testfiles\" \"C:\\output.csv\" -chapters")
    print("\n")
    exit(1)

args = sys.argv

# validate args
if len(args) == 2 and (args[1] in ['?', '-?', 'help', '-help']):
    print_usage()
elif len(args) != 3 and len(args) != 4:
    print("incorrect number of arguments")
    print_usage()
elif len(args) == 4 and ((args[3].upper() != '-CHAPTERS') and (args[3].upper() != '-C')):
    print_usage()

input_folder = args[1] 
output_file = args[2] 
has_each_chapter_on_new_row = len(args) == 4

if not os.path.isdir(input_folder):
    print("'{}' is not a folder".format(input_folder))
    print_usage()

def parse_file(file):
    parsedFile = ParsedFile(file)
    
    tree = ET.parse(file)
    root = tree.getroot()
    
    set_author(root, parsedFile)
    set_title(root, parsedFile)
    set_publication_idno(root, parsedFile)
    set_used_copy(root, parsedFile)
    set_publisher(root, parsedFile)
    set_year_published(parsedFile)
    set_text(root, parsedFile)

    return parsedFile

with open(output_file, 'w', encoding='utf8') as csv_file:
    writer = csv.writer(csv_file, delimiter='$', lineterminator='\n')
    writer.writerow(ParsedFile.csv_title_row(has_each_chapter_on_new_row))
    
    for f in my_helpers.get_files_from_dir_r(input_folder, '.xml'):
        print("Now processing: '{}'".format(f))
        
        parsedFile = parse_file(f)

        if (has_each_chapter_on_new_row):
            for row in parsedFile.to_csv_rows_per_chapter():
                writer.writerow(row)
        else:
            writer.writerow(parsedFile.to_csv_row_complete_text())

print ('done!')
            