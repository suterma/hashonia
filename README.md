# hashonia
A mass file integrity checker for complete directory trees.

Use it to periodically verify the integrity of files in large archives. This tool creates and stores hash values for all files in complete directory trees, allowing you to monitor for changes over time. 

# Usage
```bash
python3 hashonia.py
```
This will walk the directory tree at the current position, calculatinng md5 hashes for all files encountered.

# How it works:
Walks the file tree from the current working directory. For each file encountered, a hash is calculated and written to a text file.
It is optimised for large files and large trees, using block readings, and immediate file writes. Shows progress output.

# Credits
Uses py_essentials (https://github.com/phyyyl/py_essentials) from phyyyl
