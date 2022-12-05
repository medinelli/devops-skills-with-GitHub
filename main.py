from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from mylib.research import (
    get_wikipedia_pages,
    get_wikipedia_summary,
    get_wikipedia_keywords,
)


app = FastAPI()


class Wiki(BaseModel):
    name: str


@app.get("/")
async def root():
    """Home Page with GET HTTP Method"""

    return {"message": "Hello FastAPI"}


@app.post("/search")
async def search(wiki: Wiki):
    """Search Wikipedia for a name

    Parameters
    ----------
    wiki : Wiki
        A Wiki object with a name attribute
    returns : list
    """

    return get_wikipedia_pages(wiki.name)


@app.post("/page")
async def page(wiki: Wiki):
    """Get a summary page from Wikipedia
    Parameters
    ----------
    wiki : Wiki
        A Wiki object with a name attribute
    returns : dict
    """

    return get_wikipedia_summary(wiki.name)


@app.post("/keywords")
async def keywords(wiki: Wiki):
    """Get keywords from Wikipedia
    Parameters
    ----------
    wiki : Wiki
        A Wiki object with a name attribute
    returns : list
    """

    return get_wikipedia_keywords(wiki.name)


if __name__ == "__main__":
    print("I was here")
    uvicorn.run(app, port=8080, host="0.0.0.0")
