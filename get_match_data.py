"""
Get match and match timeline data, given a matchId
"""
import json

import pandas as pd
from riotwatcher import LolWatcher, ApiError

# TODO: Get all match and timeline data, for every matchId
API_KEY = open('API-KEY').read()
# TODO: close file?

watcher = LolWatcher(API_KEY)

ids = pd.read_json('matchIdSamples/27_10_20/matchlistSamples.json')


# game = watcher.match.by_id(ids.region[0], ids.matchId[0])
# timeline = watcher.match.timeline_by_match(ids.region[0], ids.matchId[0])


def get_match(region, match_id):
    try:
        game = watcher.match.by_id(region, match_id)
        return game
    except ApiError as err:
        if err.response.status_code == 429:
            # The 429 status code indicates that the user has sent too many requests
            # in a given amount of time ("rate limiting").
            print('Try in {} seconds.'.format(err.response.headers['Retry-After']))
            print('this retry-after is handled by default by the RiotWatcher library')
            print('future requests wait until the retry-after time passes')
        else:
            raise


def get_timeline(region, match_id):
    try:
        game = watcher.match.timeline_by_match(region, match_id)
        return game
    except ApiError as err:
        if err.response.status_code == 429:
            # The 429 status code indicates that the user has sent too many requests
            # in a given amount of time ("rate limiting").
            print('Try in {} seconds.'.format(err.response.headers['Retry-After']))
            print('this retry-after is handled by default by the RiotWatcher library')
            print('future requests wait until the retry-after time passes')
        else:
            raise


for n, m_id in enumerate(ids.matchId.values):
    match = get_match(ids.region[n], m_id)
    with open('matches/' + str(m_id) + '.json', 'w') as fp_match:
        json.dump(match, fp_match, indent=4)
    fp_match.close()
    timeline = get_timeline(ids.region[n], m_id)
    with open('matches/' + str(m_id) + '_timeline.json', 'w') as fp_timeline:
        json.dump(timeline, fp_timeline, indent=4)
    fp_timeline.close()
