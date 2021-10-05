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


# TODO Check https://developer.riotgames.com/docs/lol#data-dragon_champions for
#  latest reference file


def get_champion_map(path):
    """Invert the mapping in the champion.json reference document"""
    champion_ref = load_json(path)
    champions = list(champion_ref["data"].keys())
    return {champion_ref["data"][champ]["key"]: champ for champ in champions}


# TODO add champion classes and map champions


class Match:
    def __init__(self, match_file):
        """Extract key information from match data"""
        self.data = load_json(match_file)
        self.champs = {p["championId"]: p["teamId"] for p in self.data["participants"]}

        # self.bans = {}
        for team in self.data["teams"]:
            if team["win"] == "Win":
                self.winning_team = team["teamId"]
            # for ban in team["bans"]:
            #     self.bans[ban] = team["teamId"]
