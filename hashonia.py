# Creates a hash tree for tree-wise file integrity checks
# -------------------------------------------------------
# requires
# pip3 install py_essentials

from py_essentials import hashing as hs
algorithm = 'md5' 
dir = "./"

print("Creating hash tree for " + dir + " using " + algorithm + "...")

hashtree = hs.createHashtree(dir, algorithm)

from datetime import datetime
date = datetime.today().strftime('%Y-%m-%d')

filename = 'HashTree.' + date + '.' + algorithm
print("Saving to file " + filename)

import json
print(hashtree)
print(json.dumps(hashtree, sort_keys=True, indent=4))

with open(filename, 'w') as outfile:
	outfile.write(hashtree)
