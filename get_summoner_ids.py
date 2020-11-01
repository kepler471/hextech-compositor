"""
Get further fields by summonerId search:
            'accountId',
            'id',
            'name',
            'profileIconId',
            'puuid',
            'revisionDate',
            'summonerLevel'
"""

from pathlib import Path

import pandas as pd
from riotwatcher import RiotWatcher, ApiError

df = pd.read_pickle('data/summoner_info.pkl')
# print(df.columns.values)
# print(df[df['summonerName'] == 'Araxios']['summonerId'])
# print(df[df['summonerName'] == 'Araxios'][['summonerName','tier','rank']])
# print(df['tier'].value_counts())
# print(df[df['summonerName'] == 'Araxios'].values)

API_KEY = open('API-KEY')
watcher = RiotWatcher(API_KEY)
region = 'euw1'
# araxios = watcher.summoner.by_id(region,'42Rrp5DutjGtxrz2yNFaYFnFzD1koHIRKLQXrzrD8Q6mef4')
# print(araxios)
# print(araxios['id'])
# print(type(araxios))

print(len(df['summonerId']))


def build_summoner_table(dataframe, watcher, region):
    summoners = pd.DataFrame()
    directory = Path.cwd() / 'data'

    for n, i in enumerate(dataframe['summonerId']):
        try:
            account = watcher.summoner.by_id(region, i)
        except ApiError as err:
            if err.response.status_code == 429:
                # The 429 status code indicates that the user has sent too many requests
                # in a given amount of time ("rate limiting").
                print('Try in {} seconds.'.format(err.response.headers['Retry-After']))
                print('this retry-after is handled by default by the RiotWatcher library')
                print('future requests wait until the retry-after time passes')
            else:
                raise
        summoners = summoners.append(account, ignore_index=True)
        # print(account['name'])
        if n % 100 == 0:
            print(n)

        if n % 1000 == 0:
            summoners.to_pickle(directory / 'summoners.pkl')
            summoners.to_csv(directory / 'summoners.csv')

    summoners.to_pickle(directory / 'summoners.pkl')
    summoners.to_csv(directory / 'summoners.csv')
    print(f'Final dataframe shape is {summoners.shape}')


build_summoner_table(df.iloc[48001:], watcher, region)

# limit = 4300000000
# print(range(limit,0))
# for i in range(limit,0,-1):
#     try:
#         match_info = watcher.match.by_id(region,i)
#         print(match_info)
#     except ApiError as err:
#         if err.response.status_code == 429:
#             # The 429 status code indicates that the user has sent too many requests
#             # in a given amount of time ("rate limiting").
#             print('Try in {} seconds.'.format(err.response.headers['Retry-After']))
#             print('this retry-after is handled by default by the RiotWatcher library')
#             print('future requests wait until the retry-after time passes')
#         elif err.response.status_code == 404:
#             print('match id not found')
#         else:
#             raise

# match_info = watcher.match.by_id(region,3933336270)
# print(type(match_info))
# # print(match_info[0])
# # print(len(match_info))
# print(match_info.keys())
# print(match_info['participants'])
# # print(midf.shape)
# # print(midf.columns)
# # print(midf.index)
# # print(midf['gameMode'])
