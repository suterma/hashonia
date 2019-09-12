# hashonia
A mass file integrity checker for complete directory trees.

This tool creates and stores hash values for files in complete directory trees, allowing to monitor for changes over time. Use it to periodically verify the integrity of large file archives.

# Usage

python3 hashonia.py

This will walk the directory tree at the current position, calculatinng md5 hashes for all files encountered.


# Credits
Uses py_essentials (https://github.com/phyyyl/py_essentials) from phyyyl
