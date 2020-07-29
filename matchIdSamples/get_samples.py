import os

regions = ['eun1', 'euw1', 'jp1', 'kr', 'na1']
urls = [f'http://canisback.com/matchId/matchlist_{r}.json' for r in regions]

for u in urls:
    os.system(f'wget {u}')
