"""Use the parser to start scraping through
match data, and calculate champion win rates.
"""

from utils.parser import *

CHAMPION_MAP = get_champion_map("ref/champion.json")

match = Match("matchIdSamples/match_4728783388.json")
