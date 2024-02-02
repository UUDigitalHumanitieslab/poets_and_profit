# poets_and_profit

The scripts in this project work together to extract relevant information and data from xml files from [*dbnl*](https://www.dbnl.org/) and put this data in a csv for further processing in Access, NVivo, etc.

These scripts were developed for the [Poets and Profits](https://www.nwo.nl/en/projects/275-30-032) project.

*Current status:* We do not currently maintain or use these scripts ourselves, but they should remain functional as long as DBNL's data format does not change significantly. If you are interested in CSV files of DBNL data, we currently make these available through [I-analyzer](https://github.com/UUDigitalHumanitieslab/I-analyzer).

## Prerequisites

- [Python 3](https://www.python.org/). If you are having issues with compatibility, try using python 3.6.

`Split documents` requires the pip packages [numpy](https://numpy.org/) and [pandas](https://pandas.pydata.org/).

DBNL data can be downloaded from [DBNL-dataset](https://www.kb.nl/onderzoeken-vinden/datasets/dbnl-dataset).

## Usage

- `dbnl_xml_to_csv` is the main script, which does what it says exactly: it processes all xml files in a given folder and puts the relvant data from these files in a single .csv file. Before it can do this, however, all html entities present in the xml will need to be removed / replaced. Enter a helper script.

- `remove_html_entities_from_xml` is a helper script that reads all xml files from a folder and replaces html-entities in them. Note that the list of html-entities replaced is not exhaustive (more below).

- `split_documents` is a script that extracts rows from an Excelsheet and writes the content of each row to a separate txt file.

- `txt_to_xlsx` is a script to convert data from txt to xlsx


### `remove_html_entities_from_xml`
This helperscript removes html-entities from a file by string replacement. Provide it with an input- and outputfolder and it will pick up all xml-files and process them, and write output to the given folder. Note the following:

1.     Not all html-entities are included in the core method (the string replacement). Any remaining html-entities are found by parsing each result file to xml. Any errors encountered during this process are saved and will be conveniently printed at the end of the script output. Add new html-entities that need to be replaced in `my_helpers.py` and run the script again.

#### Execution
Simply call the script and provide an input- and outputfolder:	

    USAGE:
    remove_html_entities_from_xml.py [input_folder] [output_folder]
    Example: remove_html_entities_from_xml.py "C:\inputfiles" "C:\outputfiles"

### `dbnl_xml_to_csv`
This is the main script, the one that collects relevant fields from the *dbnl* files and writes them to a csv file.
The methods that find the actual data can be found in `dbnl_xml_parser.py`.

#### Execution
In addition to the inputfolder and output*FILE* (not folder!) a third argument can be provided to write each chapter from the souces to a new line in the csv output:

  
	USAGE:
    dbnl_xml_to_csv.py [input_folder] [output_file] optional: [-chapters]
    Provide the 'chapters' argument to print each chapter on a separate line in the csv
    Example: dbnl_xml_to_csv.py "C:\testfiles" "C:\output.csv" -chapters

### `split_documents`
This is a script that was created to extract each row from an Excelsheet and write it to a txt file. You can change the inputfile and output directory at the top of the script and simply run it with your debugger (or such).

### `txt_to_xlsx`
This script was written to convert data in txts. Note that not every record has the same fields. Change the input- and outputfile at the top of the script and simply run it with your debugger (or such).

## Licence

This code is shared under a [BSD 3-Clause licence](/LICENSE).