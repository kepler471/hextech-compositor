"""
Base class for interacting with the api
TODO work to move the `get_***.py` files to build from this class
"""
from riotwatcher import LolWatcher, ApiError


class Scraper:
    # TODO: move watcher initialisation outside of scraper, this will allow
    #   generic endpoint to be passed to fetch()
    def __init__(self):
        try:
            with open('API-KEY') as f:
                self.API_KEY = f.read()
                f.close()
        except FileNotFoundError:
            print("No API KEY found")
        # TODO add exception for expired API key

        self.watcher = LolWatcher(self.API_KEY)

    def fetch(self, endpoint, **kwargs):
        try:
            return endpoint(**kwargs)
        except ApiError as err:
            if err.response.status_code == 429:
                # The 429 status code indicates that the user has sent too many requests
                # in a given amount of time ("rate limiting").
                print('Try in {} seconds.'.format(err.response.headers['Retry-After']))
                print('this retry-after is handled by default by the RiotWatcher library')
                print('future requests wait until the retry-after time passes')
            elif err.response.status_code == 404:
                print('match id not found')
            elif err.response.status_code == 504:
                # TODO: find out how to get generic response url
                print(
                    f"requests.exceptions.HTTPError: 504 Server Error: "
                    f"Gateway Timeout for url: "
                    # f"https://{kwargs['region']}.api.riotgames.com/lol/match/v4/matches/{kwargs['match_id']}"
                )
            elif 500 <= err.response.status_code < 600:
                print(
                    f"requests.exceptions.HTTPError: {err.response.status_code} Server Error: "
                    f"Service Unavailable for url:"
                    # f"https://{kwargs['region']}.api.riotgames.com/lol/match/v4/matches/{kwargs['match_id']}"
                )
            else:
                raise
