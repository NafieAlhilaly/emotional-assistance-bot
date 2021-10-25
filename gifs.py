"""
gifs from https://tenor.com/
"""

import os
import requests
import random


class RandomGifs:
    def __init__(self):
        self._API_KEY = os.getenv('TENOR_API_KEY')

    def get_api_key(self):
        return self._API_KEY

    def get_random_hug_gif(self) -> str:
        """
        sent request to get top 8 gifs in the result then
        select one of them randomly and get its url
        """

        search_lmt = 8
        search_term = "hug"

        response = requests.get(
            f"https://g.tenor.com/v1/search?q={search_term}&key={self.get_api_key()}&limit={search_lmt}").json()
        
        response = random.choice(response['results'])
        
        gif_url = response['media'][0]['tinygif']['url']
        
        return gif_url
