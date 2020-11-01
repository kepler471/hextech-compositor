"""Load sample data from a match
Build some functions to parse the data, and map
ID values to reference jsons for true data
(ie. champion names, runes, summoner spells)

Example:
    '../matchIdSamples/match_4728783388.json'
"""

import json


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
