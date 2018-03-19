import os

import numpy as np
import pandas

# Select the directory to output the text files to.
# Creates the directory if it does not exist yet.
OUTPUT_DIRECTORY = "poetsandprofits_output"
# Enter the original Excel filename here.
FILEPATH = "exportNVivo1550-1750handhaven.xlsx"


def createTextFile(filename, data):
    filepath = os.path.join(OUTPUT_DIRECTORY, filename + ".txt")
    with open(filepath, "w+", encoding='utf8') as outputFile:
        for item in data:
            print(item, file=outputFile)


if __name__ == "__main__":
    dataFrame = pandas.read_excel(FILEPATH, sheet_name=1, header=0, encoding='utf-8')
    # Replace NotANumber entries with an empty string.
    dataFrame = dataFrame.replace(np.nan, '', regex=True)

    if not os.path.exists(OUTPUT_DIRECTORY):
        os.makedirs(OUTPUT_DIRECTORY)

    for index, entry in dataFrame.iterrows():
        # Extract all the relevant field text.
        # Add or remove columns by accessing entry['columnName']
        filename = entry['document_id']
        title = entry['title']
        author = entry['author']
        chapterId = entry['chapter_id']
        publisherInfo = entry['publisher_info']
        yearPublished = entry['year_published']
        text = entry['text']

        # Create a list of fields that have to be written to the text file.
        data = [title, author, chapterId, publisherInfo, yearPublished, text]
        createTextFile(filename, data)
