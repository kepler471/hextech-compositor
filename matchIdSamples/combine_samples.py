import glob

import pandas as pd

date = "27_10_20"
date_fmt = './' + date + '/'
batch = []
for f in glob.glob(date_fmt + '*.json'):
    data = pd.read_json(f).rename(columns={0: 'matchId'})
    print(f)
    print(f[:-5].split('_')[-1])
    # TODO: make this namer more robust
    data['region'] = f[:-5].split('_')[-1]
    batch.append(data)

df = pd.concat(batch, axis=0).reset_index()
df.to_json(date_fmt + 'matchlistSamples.json')
