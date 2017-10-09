import os
import sys
from os import listdir, walk, path, unlink
from os.path import isfile, join

def get_script_dir():
    return path.dirname(path.realpath(sys.argv[0]))

def get_files_from_dir(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    return files

def get_files_from_dir_r(path, filemask):
    files = [path.join(root, name)
             for root, dirs, files in walk(path)
             for name in files
             if name.endswith((filemask))]
    return files

def delete_files_from_dir(path):
    print("Now deleting files from '{}'".format(path))
    
    for f in get_files_from_dir(path):
        file_path = os.path.join(path, f)
        try:
            if os.path.isfile(file_path):
                unlink(file_path)
        except Exception as e:
            print(e)

    print("done deleting")
   
def replace_html_entities(old_line):
    new_line = old_line.replace('&nbsp;', '')
    new_line = new_line.replace('&lsquo;', '\'')
    new_line = new_line.replace('&rsquo;', '\'')
    new_line = new_line.replace('&ldquo;', '\"')
    new_line = new_line.replace('&rdquo;', '\"')
    new_line = new_line.replace('&agrave;', 'à')
    new_line = new_line.replace('&acirc;', 'â')
    new_line = new_line.replace('&aacute;', 'á')
    new_line = new_line.replace('&alpha;', 'A')
    new_line = new_line.replace('&auml;', 'ä')
    new_line = new_line.replace('&AElig;', 'æ')        
    new_line = new_line.replace('&ccedil', 'ç') 
    new_line = new_line.replace('&eacute;', 'é')
    new_line = new_line.replace('&euml;', 'ë')
    new_line = new_line.replace('&egrave;', 'è')
    new_line = new_line.replace('&ecirc;', 'ê')
    new_line = new_line.replace('&eta;', 'η')
    new_line = new_line.replace('&epsilon;', 'ε')
    new_line = new_line.replace('&iacute;', 'í')
    new_line = new_line.replace('&icirc;', 'î')
    new_line = new_line.replace('&igrave;', 'ì')
    new_line = new_line.replace('&iuml;', 'ï')
    new_line = new_line.replace('&iota;', 'ι')
    new_line = new_line.replace('&kappa;', 'κ')
    new_line = new_line.replace('&mu;', 'μ')
    new_line = new_line.replace('&nu;', 'ν')
    new_line = new_line.replace('&nacute;', 'ń')
    new_line = new_line.replace('&ocirc;', 'ô')
    new_line = new_line.replace('&ograve;', 'ò')
    new_line = new_line.replace('&oacute;', 'ó')
    new_line = new_line.replace('&ouml;', 'ö')
    new_line = new_line.replace('&omicron;', 'ο')
    new_line = new_line.replace('&omega;', 'ω')        
    new_line = new_line.replace('&phi;', 'φ')
    new_line = new_line.replace('&pi;', 'π')  
    new_line = new_line.replace('&rho;', 'ρ')  
    new_line = new_line.replace('&sect;', '§')
    new_line = new_line.replace('&Sigma;', 'σ')
    new_line = new_line.replace('&sigma;', 'σ')
    new_line = new_line.replace('&sigmaf;', 'ς')
    new_line = new_line.replace('&tau;', 'τ')
    new_line = new_line.replace('&uacute;', 'ú')
    new_line = new_line.replace('&ugrave;', 'ù')
    new_line = new_line.replace('&ucirc;', 'ù')
    new_line = new_line.replace('&uuml;', 'ü')    
    return new_line