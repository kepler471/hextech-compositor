import pandas as pd
import glob

batch = []
for f in glob.glob('./matchIdSamples/*.json'):
    data = pd.read_json(f).rename(columns={0:'matchId'})
    data['region'] = f[:-5].split('_')[1]
    batch.append(data)
    
df = pd.concat(batch, axis=0).reset_index()
df.to_json('./matchIdSamples/matchlistSamples.json')
