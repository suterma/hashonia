# Creates a hash list for tree-wise file integrity checks
# Version 1.01: Directly outputs to a file. Uses a list output instead of a tree
# -------------------------------------------------------
# Credits: https://www.pythoncentral.io/hashing-files-with-python/
# Credits: https://github.com/phyyyl/py_essentials


# How it works:
# Walks the file tree from the current working directory. For each file encountered, a hash is calculated and written to a text file.
# It is optimised for large files and large trees, using block readings, and immediate file writes. Shows progress output.

import time, os, hashlib
from datetime import datetime

# prepare
start_time = time.time()
fileCount = 0
BLOCKSIZE = 65536 #TODO should be optimised. What is a optimal value on different OS, for different file sizes? Maybe also consider using mmap or memoryview
current_dir = os.getcwd()

# create a file with a date marker
dateMarker = datetime.today().strftime('%Y-%m-%d')
fileName = 'hashonia-list.' + dateMarker + '.' + "md5"
print("Creating hash list for path '" + current_dir + "' into file '" + fileName + "'")

# directly write each file's hash to the output file
with open(fileName, 'w') as outputFile:
	outputFile.write('{\n')

	for root,dirs,files in os.walk(current_dir):
		for f in files:		    
			current_file = os.path.join(root,f)
			hasher = hashlib.md5()

			with open(current_file, 'rb') as afile:
				buf = afile.read(BLOCKSIZE)
				while len(buf) > 0:
					hasher.update(buf)
					buf = afile.read(BLOCKSIZE)
			print (current_file + ": "+ hasher.hexdigest())
			outputFile.write('    "' + current_file + '":"' + hasher.hexdigest() + '",\n')
			fileCount += 1
	outputFile.write('}\n')

# write summary
print("done {} files in {} seconds.".format(fileCount, time.time() - start_time))
