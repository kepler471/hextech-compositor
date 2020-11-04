"""
Get match and match timeline data, given a matchId
"""
import datetime
import json
import os

import pandas as pd
from riotwatcher import LolWatcher, ApiError

# TODO: Get all match and timeline data, for every matchId
API_KEY = open('API-KEY').read()
# TODO: close file?

watcher = LolWatcher(API_KEY)

ids = pd.read_json('matchIdSamples/27_10_20/matchlistSamples.json')


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
        elif err.response.status_code == 504:
            print(
                f"requests.exceptions.HTTPError: 504 Server Error: Gateway Timeout for url: "
                f"https://{region}.api.riotgames.com/lol/match/v4/matches/{match_id}"
            )
        elif 500 <= err.response.status_code < 600:
            print(
                f"requests.exceptions.HTTPError: {err.response.status_code} Server Error: Service Unavailable for url:"
                f" https://{region}.api.riotgames.com/lol/match/v4/matches/{match_id}"
            )
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
        elif err.response.status_code == 504:
            print(
                f"requests.exceptions.HTTPError: 504 Server Error: Gateway Timeout for url: "
                f"https://{region}.api.riotgames.com/lol/match/v4/matches/{match_id}"
            )
        elif 500 <= err.response.status_code < 600:
            print(
                f"requests.exceptions.HTTPError: {err.response.status_code} Server Error: Service Unavailable for url:"
                f" https://{region}.api.riotgames.com/lol/match/v4/matches/{match_id}"
            )
        else:
            raise


for n, m_id in enumerate(ids.matchId.values):
    # TODO: Split by region?
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    print("index:", n)
    match_name = 'matches/' + str(ids.matchId[n]) + '.json'
    timeline_name = 'matches/' + str(ids.matchId[n]) + '_timeline.json'

    if not os.path.isfile(match_name):
        print("Getting match data for:", ids.matchId[n])
        match = get_match(ids.region[n], ids.matchId[n])
        with open(match_name, 'w') as fp_match:
            json.dump(match, fp_match, indent=4)
        fp_match.close()
    else:
        print("Match data already exists for:", ids.matchId[n])

    if not os.path.isfile(timeline_name):
        print("Getting timeline data for:", ids.matchId[n])
        timeline = get_timeline(ids.region[n], ids.matchId[n])
        with open(timeline_name, 'w') as fp_timeline:
            json.dump(timeline, fp_timeline, indent=4)
        fp_timeline.close()
    else:
        print("Timeline data already exists for:", ids.matchId[n])
