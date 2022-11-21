#!/usr/bin/env python

import click
from mylib.filetools import find_files


@click.group()
def cli():
    """A command line interface for mylib.filetools module."""

@cli.command("search")
@click.argument("directory")
@click.argument("pattern")
@click.option("--ignore-patterns", "-i", multiple=True)

def search(directory, pattern, ignore_patterns):
    """Search for files in DIRECTORY that match PATTERN.

    Ignore files that match any of the IGNORE_PATTERNS.

    Example:
        ./fileToolsCLI.py search . "*.py" -i "venv" -i "test"
    """

    for path in find_files(directory, pattern, ignore_patterns):
        #use click colors to highlight the pattern in the file path
        click.echo(click.style(str(path), fg="green"))

@cli.command("count_files")
@click.argument("directory")
@click.argument("pattern")
@click.option("--ignore-patterns", "-i", multiple=True)

def count_files(directory, pattern, ignore_patterns):
    """Count the number of files in DIRECTORY that match PATTERN.

    Ignore files that match any of the IGNORE_PATTERNS.

    return a tuple of the number of files and the paths of the files


    Example:
        ./fileToolsCLI.py count . "*.py" -i "venv" -i "test"
    """
    
    paths = list(find_files(directory, pattern, ignore_patterns))
    click.echo(f"Found {len(paths)} files")
    for path in paths:
        click.echo(click.style(str(path), fg="green"))
    
    



if __name__ == "__main__":
    cli()
