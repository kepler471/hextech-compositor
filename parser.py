"""Load sample data from a match
Build some functions to parse the data, and map
ID values to reference jsons for true data
(ie. champion names, runes, summoner spells)

Example:
    '../matchIdSamples/match_4728783388.json'

The original json will be stored in raw form,
in a separate table.
"""

import json

import pandas as pd
from sqlalchemy import create_engine


def load_json(file):
    """Given json file, returns dict j"""
    with open(file) as f:
        j = json.loads(f.read())
        f.close()
    return j


def champion_id(name):
    """Returns champion id given name"""
    for cid in champion_map:
        if champion_map[cid] == name:
            return cid


def champion_name(cid):
    """Returns champion name given id"""
    return champion_map[cid]


champion_map = load_json('../ref/champions.json')


class Match:
    def __init__(self, match_file):
        """Extract key information from match data
        """
        self.data = load_json(match_file)
        self.champs = {
            p['championId']: p['teamId'] for p in self.data['participants']
        }

        self.bans = {}
        for team in self.data['teams']:
            if team['win'] == 'Win':
                self.winning_team = team['teamId']
            for ban in team['bans']:
                self.bans[ban] = team['teamId']


if __name__ == '__main__':

    engine = create_engine('sqlite')
    rows = []

    game = load_json("matches/4887737431.json")
    data = {
        'gameId': game['gameId'],
        'platformId': game['platformId'],
        'gameCreation': game['gameCreation'],
        'gameDuration': game['gameDuration'],
        'queueId': game['queueId'],
        'mapId': game['mapId'],
        'seasonId': game['seasonId'],
        'gameVersion': game['gameVersion'],
        'gameMode': game['gameMode'],
        'gameType': game['gameType'],
    }
    for p in game['participants']:
        data['participantId'] = p['participantId']
        data['teamId'] = p['teamId']
        data['championId'] = p['championId']
        data['role'] = p['role']
        data['lane'] = p['lane']
        data['win'] = p['stats']['win']
        rows.append(data)

    df = pd.DataFrame(rows)
