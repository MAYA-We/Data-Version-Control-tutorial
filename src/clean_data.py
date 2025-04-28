import pandas as pd
df = pd.read_csv('data/raw/28.csv', sep=';')
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df.to_csv('data/prepare/cleaned_data.csv', index=False)