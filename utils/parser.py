"""Load sample data from a match
Build some functions to parse the data, and map
ID values to reference jsons for true data
(ie. champion names, runes, summoner spells)

Example:
    '../matchIdSamples/match_4728783388.json'
"""

import json


def load_match(file):
    """Given match json file, returns match dict j"""
    with open(file) as f:
        j = json.loads(f.read())
        f.close()
    return j


class Match:
    def __init__(self, file):
        """Extract key information from match data
        """
        self.data = load_match(file)
        self.champs = {
            p['championId']: p['teamId'] for p in self.data['participants']
        }

        self.bans = {}
        for team in self.data['teams']:
            if team['win'] == 'Win':
                self.winning_team = team['teamId']
            for ban in team['bans']:
                self.bans[ban] = team['teamId']

