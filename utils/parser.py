"""Load sample data from a match
Build some functions to parse the data, and map
ID values to reference jsons for true data
(ie. champion names, runes, summoner spells)
"""

import json

f = open('../matchIdSamples/match_4728783388.json')
j = json.loads(f.read())
