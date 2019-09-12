# Creates a hash list for tree-wise file integrity checks
# -------------------------------------------------------
# Credits: https://www.pythoncentral.io/hashing-files-with-python/
# Credits: https://github.com/phyyyl/py_essentials

import os, hashlib
BLOCKSIZE = 65536
current_dir = os.getcwd()


jsonstring = '{'+ "\r\n"

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

        jsonstring = jsonstring + '    "' + current_file + '":"' + hasher.hexdigest() + '",' + "\r\n"

if jsonstring[-1] == "{":
    jsonstring = jsonstring + "\r\n" + "}"
else:
    jsonstring = jsonstring[:-1] + "\r\n" + "}"

print(jsonstring)

with open("testoutput.txt", 'w') as outputFile:
    outputFile.write(jsonstring)
