import requests
import random


# more about this API @ https://github.com/ywalia01/dune-api
class RandomQuotes:
    def __init__(self):
        self._RANDOM_QUOTES_API = "https://the-dune-api.herokuapp.com"
        self._QUOTE_TYPES = ["quotes",
                                "books",
                                "movies",
                                "series",
                                "shortStories",
                                "comics"]

    def get_random_quote(self) -> str:
        quote = requests.get(f"{self._RANDOM_QUOTES_API}/quotes").json()
        return quote[0]['quote']

