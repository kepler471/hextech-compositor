"""
Get match and match timeline data, given a matchId
"""
from riotwatcher import LolWatcher, ApiError
import pandas as pd


# API_KEY = open('API-KEY.txt')
watcher = LolWatcher('RGAPI-5cb19446-ab28-4560-bfe3-545a9f4f99c8')

ids = pd.read_json('matchIdSamples/10_08_20/matchlistSamples.json')
eu = pd.read_json('matchIdSamples/10_08_20/matchlist_euw1.json')

# game = watcher.match.by_id('euw1', eu.values[0][0])
# timeline = watcher.match.timeline_by_match('euw1', eu.values[0][0])
# print(eu.values[0])
# print(ids.region[0])
# game = watcher.match.by_id(ids.region[0], ids.matchId[0])
# timeline = watcher.match.timeline_by_match(ids.region[0], ids.matchId[0])

for n in range(lane(ids)):
    game = watcher.match.by_id(ids.region[n], ids.matchId[n])
    # timeline = game
