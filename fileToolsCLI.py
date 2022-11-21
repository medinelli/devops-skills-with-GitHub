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
        click.echo(path)


if __name__ == "__main__":
    cli()
