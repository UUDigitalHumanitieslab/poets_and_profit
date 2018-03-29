import os

import numpy as np
import pandas as pd

# Select the directory to output the text files to.
# Creates the directory if it does not exist yet.
OUTPUT_DIRECTORY = "poetsandprofits_output"
# Enter the original Excel filename here.
FILEPATH = "plusAliesveldenexportNVivo1550-1750handhaven.xlsx"

if __name__ == "__main__":
    dataFrame = pd.read_excel(FILEPATH, sheet_name=1, header=0, encoding='utf-8')
    # Replace NotANumber entries with an empty string.
    dataFrame = dataFrame.replace(np.nan, '', regex=True)

    if not os.path.exists(OUTPUT_DIRECTORY):
        os.makedirs(OUTPUT_DIRECTORY)

    for index, entry in dataFrame.iterrows():
        # Extract all the relevant field text.
        # Add or remove columns by adding or removing the headers.
        headers = ['document_id',
                   'Author',
                   'Title',
                   'publisher_info',
                   'Place',
                   'Printer',
                   'Date',
                   'Language',
                   'Value',
                   'Reflectionon',
                   'Genre',
                   'Explicitorimplicit',
                   'Theme',
                   'Wordcount',
                   'Origin',
                   'Edition',
                   'Signature',
                   'Details',
                   'text']

        # Create a list of fields that have to be written to the text file.
        data = [{header: entry[header] for header in headers}]
        # Create a new dataframe from this dictionary.
        fileDataFrame = pd.DataFrame(data)

        # Save the file as [document_id].csv
        filename = fileDataFrame['document_id'][0]
        filepath = os.path.join(OUTPUT_DIRECTORY, filename + ".csv")
        fileDataFrame.to_csv(filepath, encoding="utf-8", index=False)
