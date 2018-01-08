import sys
import os
# we retrieve the folder as the first positional argument
# to the command-line call
if len(sys.argv) > 1:
    folder = sys.argv[1]
    # we list all files in the specified folder
    files = os.listdir(folder)
    # ids contains the sorted list of all unique idenfitiers
    ids = [ int(file.split('.')[0]) for file in files if 'edges' in file] 
    ids.sort()
else: 
    raise Exception("No folder is specified.")