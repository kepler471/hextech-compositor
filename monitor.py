import pandas as pd
from pathlib import Path
from time import sleep

# Can run while API is being used to check on the progress of data collection

while True:
	df = pd.read_csv(Path.cwd() / 'data/summoners.csv')
	print(df[['accountId','name']].tail())
	sleep(2)
