#!/usr/bin/env python

import click
from mylib.filetools import find_files, find_pattern_in_file


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
        # use click colors to highlight the pattern in the file path
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
        ./fileToolsCLI.py count_files . "*.py" -i "venv" -i "test"
    """

    paths = list(find_files(directory, pattern, ignore_patterns))
    click.echo(f"Found {len(paths)} files")
    for path in paths:
        click.echo(click.style(str(path), fg="green"))


# buid a command that searches a file for a pattern and prints the line number and line
@cli.command("find")
@click.argument("file")
@click.argument("pattern")
def find(file, pattern):
    """Search a file for a pattern and print the line number and line

    Example:
        ./fileToolsCLI.py find ./mylib/filetools.py "import pathlib"
    """
    #count the number of times the pattern is found in the file
    count = 0

    for line_number, line in find_pattern_in_file(file, pattern):
        count += 1
        # use click colors to highlight the pattern in the file path
        click.echo(click.style(f"{line_number}: {line}", fg="green"))
    #print the number of times the pattern was found in the file using a different color
    click.echo(click.style(f"Found {count} matches", fg="red"))


if __name__ == "__main__":
    cli()
