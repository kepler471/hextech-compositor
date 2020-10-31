import wget

regions = ['eun1', 'euw1', 'jp1', 'kr', 'na1']
urls = [f'http://canisback.com/matchId/matchlist_{r}.json' for r in regions]

date = "27_10_20"

for u in urls:
    wget.download(u, date)