#build a function that searches the file system for a pattern and ignores patterns
#that are in a list of ignore patterns
#use pathlib.Path.glob() to search the file system

import pathlib


def find_files(directory, pattern, ignore_patterns):
    directory = pathlib.Path(directory)

    for path in directory.glob(pattern):
        for ignore_pattern in ignore_patterns:
            if ignore_pattern in str(path):
                break
        else:
            yield path

#build a function that reads a file and searches for a pattern
#use pathlib.Path.read_text() to read the file
#use string methods to search for the pattern
#return the line number and the line

def find_pattern_in_file(path, pattern):
    path = pathlib.Path(path)
    text = path.read_text()
    for i, line in enumerate(text.splitlines(), start=1):
        if pattern in line:
            yield i, line