#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""


# +++your code here+++
# Write functions and modify main() to call them
def get_path(dir):
    files = os.listdir(dir)
    paths = []
    for file in files:
        paths.append(os.path.abspath(os.path.join(dir, file)))
    return paths


def copy_to_dir(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    source_files = get_path(source_dir)
    for file in source_files:
        shutil.copy(file, dest_dir)

def zip_to(source_dir, zip_file):
    subprocess.call(['zip', '-r', zip_file, os.path.abspath(source_dir)])

def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

    # +++your code here+++
    # Call your functions
    source_dir = args[0]
    if todir:
        copy_to_dir(source_dir, todir)
    elif tozip:
        zip_to(source_dir, tozip)


if __name__ == "__main__":
    main()
