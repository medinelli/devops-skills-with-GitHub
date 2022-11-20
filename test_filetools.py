from mylib.filetools import find_files, find_pattern_in_file
import pathlib

def test_find_files():
    """Test find_files() function"""
    # create a directory to search
    directory = pathlib.Path('__file__').parent
    pattern = '*.py'
    ignore_patterns = ['test_','__pycache__']
    paths = list(find_files(directory, pattern, ignore_patterns))
    assert len(paths) == 1
    assert paths[0].name == 'hello.py'

def test_find_pattern_in_file():
    """Test find_pattern_in_file() function"""
    path = pathlib.Path('__file__').parent / "mylib/filetools.py"
    
    pattern = 'def find_files'
    lines = list(find_pattern_in_file(path, pattern))
    assert len(lines) == 1
    assert lines[0][0] == 8
    assert lines[0][1] == 'def find_files(directory, pattern, ignore_patterns):'