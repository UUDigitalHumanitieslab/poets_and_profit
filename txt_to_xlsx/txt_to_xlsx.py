import os
import csv
import re
from row import headers, row

INPUT_FILE = "input_orig.txt"
OUTPUT_FILE = "output.csv"



def parse_txt():
    all_rows = list()

    with open(INPUT_FILE, 'r') as input_file:
        lines = input_file.readlines()

        current_row = row()
        previous_header = ''

        for line in lines:
            if re.match(r'\s', line):
                current_row.data[previous_header] = current_row.data[previous_header] + ' ' + line.strip()
                continue

            if (line[2:].startswith('_')):
                header = line[:5]
                data = line[5:].strip()
            else:
                header = line[:3]
                data = line[3:].strip()
                          
            if (header == 'DAT'):
                all_rows.append(current_row)
                current_row = row()
            
            current_row.data[header] = data
            previous_header = header

    with open(OUTPUT_FILE, 'w', encoding='utf8') as csv_file:
        writer = csv.DictWriter(csv_file, headers, delimiter='\t', lineterminator='\n', dialect='excel')
        writer.writeheader()
    
        for r in all_rows:
            writer.writerow(r.data)        

parse_txt()     

                    





# # first find all headers / data-items present
# def find_headers():
#     all_headers = list()
    
#     with open(INPUT_FILE, 'r') as input_file:
#         lines = input_file.readlines()

#         for line in lines:
#             if (line[2:].startswith('_')):
#                 header = line[:5]
#             else:
#                 header = line[:3]

#             if not header in all_headers:
#                 all_headers.append(header)

#     with open(HEADERS_FILE, 'w') as csv_file:
#         writer = csv.writer(csv_file, delimiter='$', lineterminator='\n', dialect='excel')
#         writer.writerow(all_headers)
 