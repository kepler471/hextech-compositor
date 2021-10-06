"""Use the parser to start scraping through
match data, and calculate champion win rates.
"""

from utils.parser import *
import pandas as pd


def produce_winrates_data(path):
    match_data = {
        "champs": [],
        "team": [],
        "win": [],
        "gameId": [],
    }

    for f in path.glob("*"):
        # Select only match files
        if not f.suffix == ".json" or "timeline" in f.stem or "response" in f.stem:
            continue

        match = Match(f)

        # Append each 10 champions to match_data, along with important info
        match_data["champs"] += list(match.champs.keys())
        match_data["team"] += list(match.champs.values())
        match_data["win"] += [
            True if match.champs[x] == match.winning_team else False
            for x in match.champs
        ]
        match_data["gameId"] += 10 * [match.data["gameId"]]

    return pd.DataFrame(data=match_data)
