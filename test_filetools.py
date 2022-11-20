from mylib.filetools import find_files
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
