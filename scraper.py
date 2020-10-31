"""
Base class for interacting with the api
TODO work to move the `get_***.py` files to build from this class
"""
from riotwatcher import RiotWatcher, ApiError
import pandas as pd


class Scraper:
    def __init__(self):
        try:
            self.API_KEY = open('API-KEY.txt')
        except FileNotFoundError:
            print("No API KEY found")
        # TODO add exception for expired API key
        
        self.watcher = RiotWatcher(self.API_KEY)
