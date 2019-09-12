# hashonia
A mass file integrity checker for complete directory trees.

Use it to periodically verify the integrity of files in large archives. This tool creates and stores hash values for all files in complete directory trees, allowing you to monitor for changes over time. 

# Usage
```bash
python3 hashonia.py
```
This will walk the directory tree at the current position, calculatinng md5 hashes for all files encountered.


# Credits
Uses py_essentials (https://github.com/phyyyl/py_essentials) from phyyyl
