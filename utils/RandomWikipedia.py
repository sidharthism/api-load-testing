import wikipedia
from pysondb import db
import random

DEFAULT_ARTICLE = { 
    "title": "Wikipedia",
    "summary": """Wikipedia is a multilingual free online encyclopedia written and maintained by 
                  a community of volunteers through open collaboration and a wiki-based editing system.
                  Its editors are known as Wikipedians. Wikipedia is the largest and most-read reference work in history.
                  It is consistently one dation, an American non-profit organization funded mainly through donations.
                  On January 15, 2001, Jimmy Wales and Larry Sanger launched Wikipedia."""
}


class RandomWikipedia:
    randomWikipediaPageSummaryDB = None
    _data = None

    def __init__(self, dbName = "data/db.json"):
        try:
            self.randomWikipediaArticleSummaryDB = db.getDb(dbName)
        except Exception as e:
            print(e)

    def load_data(self,):
        self._data = self.randomWikipediaArticleSummaryDB.getAll()

    def get_random_page_summary_from_wikipedia(self, ):
        try:
            randomPageTitle = wikipedia.random(1)
            randomPageSummary = wikipedia.summary(randomPageTitle)
            return {
                "title": randomPageSummary,
                "summary": randomPageSummary
            }          
        except Exception as e:
            print(e)
            return DEFAULT_ARTICLE

    def add_random_page_summary_to_db(self, page):
        try:
            self.randomWikipediaArticleSummaryDB.add(page)
        except Exception as e:
            print(e)
            self.randomWikipediaArticleSummaryDB.add(DEFAULT_ARTICLE)

    def get_random_page_summary_from_db(self):
        if self._data is None:
            self.load_data()
        idx = random.randint(0, len(self._data) -  1)
        return self._data[idx]


def generate_n_wikipedia_page_summary(n):
    randomWiki = RandomWikipedia("data/randomWikipediaPageSummaryDB.json")
    for _ in range(n):
        random_page_summary = randomWiki.get_random_page_summary_from_wikipedia()
        randomWiki.add_random_page_summary_to_db(random_page_summary)


if __name__ == '__main__':
    import sys
    n = 1
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    generate_n_wikipedia_page_summary(n)


