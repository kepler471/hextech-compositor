"""
Get matchlists from summoner ids
"""

import pandas as pd
from riotwatcher import RiotWatcher, ApiError
from pathlib import Path

df = pd.read_pickle('data/summoners.pkl')

API_KEY = open('API-KEY.txt')
watcher = RiotWatcher(API_KEY)
region = 'euw1'

limit = 4300000000
print(range(limit,0))
for i in range(limit,0,-1):
    try:
        match_info = watcher.match.by_id(region,i)
        print(match_info)
    except ApiError as err:
        if err.response.status_code == 429:
            # The 429 status code indicates that the user has sent too many requests
            # in a given amount of time ("rate limiting").
            print('Try in {} seconds.'.format(err.response.headers['Retry-After']))
            print('this retry-after is handled by default by the RiotWatcher library')
            print('future requests wait until the retry-after time passes')
        elif err.response.status_code == 404:
            print('match id not found')
        else:
            raise

match_info = watcher.match.by_id(region,3933336270)
print(type(match_info))
# print(match_info[0])
# print(len(match_info))
print(match_info.keys())
print(match_info['participants'])
# print(midf.shape)
# print(midf.columns)
# print(midf.index)
# print(midf['gameMode'])