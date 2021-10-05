"""
Building 'summoner _info' dataset
by searching through ranked tiers
with fields:
            'leagueId',
            'queueType',
            'tier',
            'rank',
            'summonerId',
            'summonerName',
            'leaguePoints',
            'wins',
            'losses',
            'veteran',
            'inactive',
            'freshBlood',
            'hotStreak',
            'miniSeries'
 """

from pathlib import Path
from time import sleep

import pandas as pd
from riotwatcher import RiotWatcher, ApiError

API_KEY = open('API-KEY')
watcher = RiotWatcher(API_KEY)

my_region = 'euw1'
me = watcher.summoner.by_name(my_region, 'Doom Mons')
# print(me)

my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
# print(my_ranked_stats)

# leagues = watcher.league.entries('EUW1', 'RANKED_SOLO_5x5', 'DIAMOND', 'I',1)
# print(leagues[0])
# print(f'length of leagues is {len(leagues)}')
# test = pd.DataFrame(data = leagues)
# print(test.shape)

# Loop through all tiers: [Silver IV, Diamond I]
tiers = ['DIAMOND', 'PLATINUM', 'GOLD', 'SILVER']
divisions = ['I', 'II', 'III', 'IV']

page_num = 1
summoner_info = pd.DataFrame()
for tier in tiers:
    for division in divisions:
        page_num = 1

        while True:
            sleep(0.5)

            try:
                league = watcher.league.entries('EUW1', 'RANKED_SOLO_5x5',
                                                tier, division, page_num)
            except ApiError as err:
                if err.response.status_code == 429:
                    # The 429 status code indicates that the user has sent too many requests
                    # in a given amount of time ("rate limiting").
                    print('Try in {} seconds.'.format(err.response.headers['Retry-After']))
                    print('this retry-after is handled by default by the RiotWatcher library')
                    print('future requests wait until the retry-after time passes')
                else:
                    raise

            if league == []:
                print(f'Page {page_num} in {tier} {division} is empty')
                break
            else:
                print(f'Data found on {page_num} in {tier} {division} ')
                summoner_info = summoner_info.append(league, ignore_index=True)
                page_num += 1

        print(f'Current dataframe shape is {summoner_info.shape}')

directory = Path.cwd()
summoner_info.to_pickle(directory / 'summoner_info.pkl')
summoner_info.to_csv(directory / 'summoner_info.csv')
print(f'Final dataframe shape is {summoner_info.shape}')
print(summoner_info['summonerName'].tail())
