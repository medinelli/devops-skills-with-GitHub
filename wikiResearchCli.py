#!/usr/bin/env python

import click
from mylib.research import (
    get_wikipedia_pages,
    get_wikipedia_summary,
    get_wikipedia_keywords,
)


@click.group()
def cli():
    """A command line interface for mylib.research module."""


@cli.command("search")
@click.argument("search_term")
def search(search_term):
    """Search wikipedia for SEARCH_TERM.

    Example:
        ./wikiResearchCli.py search "python"
    """

    # search wikipedia for the search term
    pages = get_wikipedia_pages(search_term)
    # pint the pages that were found using colors to highlight the search term
    for page in pages:
        click.echo(click.style(page, fg="green"))


# bluild a command that retrieves the summary of a wikipedia page
@cli.command("summary")
@click.argument("page")
def summary(page):
    """Retrieve the summary of a wikipedia page.

    Example:
        ./wikiResearchCli.py summary "Python (programming language)"
    """
    # use click colors to highlight the page
    page = click.style(page, fg="green")
    # count the number of characters in the summary
    # use click colors to highlight the number of characters

    # retrieve the summary of the page
    summary_temp = get_wikipedia_summary(page)
    click.echo(
        click.style(
            f"Wikipedia Page: [{page}] has a number of characters: {len(summary_temp)}",
            fg="green",
        )
    )
    # print the summary using colors to highlight the page
    click.echo(click.style(summary_temp, fg="green"))


# build a command that retrieves the keywords of a wikipedia page
@cli.command("keywords")
@click.argument("page")
def keywords(page):
    """Retrieve the keywords of a wikipedia page.

    Example:
        ./wikiResearchCli.py keywords "Python (programming language)"
    """

    # retrieve the keywords of the page
    keywords_temp = get_wikipedia_keywords(page)
    # print the keywords using colors to highlight the page
    for keyword in keywords_temp:
        click.echo(click.style(keyword, fg="green"))


# call click to run the cli
if __name__ == "__main__":
    cli()
