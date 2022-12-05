import wikipedia
from yake import KeywordExtractor

# build a function the retrieves a list of wikipedia pages


def get_wikipedia_pages(search_term):
    return wikipedia.search(search_term)


# build a function that retrieves the summary of a wikipedia page


def get_wikipedia_summary(page):
    return wikipedia.summary(page)


# build a function that retrieves the content of a wikipedia page


def get_wikipedia_content(page):
    return wikipedia.page(page).content


# build a function that retrieves the keywords of a wikipedia page


def get_wikipedia_keywords(page):
    content = get_wikipedia_content(page)
    extractor = KeywordExtractor()
    return extractor.extract_keywords(content)[:10]
