# poets_and_profit
## 

The scripts in this project work together to extract relevant information and data from xml-files from *dbnl* and put this data in a csv for further processing in Access, NVivo, etc.

- `dbnl_xml_to_csv` is the main script, which does what it says exactly: it processes all xml files in a given folder and puts the relvant data from these files in a single .csv file. Before it can do this, however, all html entities present in the xml will need to be removed / replaced. Enter a helper script.

- `remove_html_entities_from_xml` is a helper script that reads all xml files from a folder and replaces html-entities in them. Note that the list of html-entities replaced is not exhaustive (more below).


**Prerequisites:**

- Python 3

----------

## `remove_html_entities_from_xml`
This helperscript removes html-entities from a file by string replacement. Provide it with an input- and outputfolder and it will pick up all xml-files and process them, and write output to the given folder. Note the following:

1.     Not all html-entities are included in the core method (the string replacement). Any remaining html-entities are found by parsing each result file to xml. Any errors encountered during this process are saved and will be conveniently printed at the end of the script output. Add new html-entities that need to be replaced in `my_helpers.py` and run the script again.

### Execution
Simply call the script and provide an input- and outputfolder:	

    USAGE:
    remove_html_entities_from_xml.py [input_folder] [output_folder]
    Example: remove_html_entities_from_xml.py "C:\inputfiles" "C:\outputfiles"

----------
## `dbnl_xml_to_csv`
This is the main script, the one that collects relevant fields from the *dbnl* files and writes them to a csv file.
The methods that find the actual data can be found in `dbnl_xml_parser.py`.

### Execution
In addition to the inputfolder and output*FILE* (not folder!) a third argument can be provided to write each chapter from the souces to a new line in the csv output:

  
	USAGE:
    dbnl_xml_to_csv.py [input_folder] [output_file] optional: [-chapters]
    Provide the 'chapters' argument to print each chapter on a separate line in the csv
    Example: dbnl_xml_to_csv.py "C:\testfiles" "C:\output.csv" -chapters

----------
## Additional testdata
Note that in addition to the few test files present in the current project, there is much more testdata available in the Lab's SURFdrive: \Shared\DigitalHumanitiesLabatUU\Poetsandprofit\testbestanden