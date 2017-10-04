import os
import sys
import re

def get_script_dir():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def get_files_from_dir(path):
    orig_dir = os.getcwd()
    os.chdir(path)
    files = os.listdir(path)
    os.chdir = orig_dir
    return files

def get_files_from_dir_r(path, filemask):
    files = [os.path.join(root, name)
             for root, dirs, files in os.walk(path)
             for name in files
             if name.endswith((filemask))]
    return files

def remove_tabs_and_newlines(text):
    return re.sub('\s+', ' ', text)
    