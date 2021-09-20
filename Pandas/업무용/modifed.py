from pprint import pprint

import pandas as pd

modified_stcs = []
df = pd.read_csv('change.csv')

for idx, series in df.iterrows():
    after_stc = series['after']

    dup = df[df['before'] == after_stc]['before']
    if not dup.empty:
        before_stc = df.loc[idx]['before']
        modified_stcs.append([f"{before_stc} → {after_stc}"])

pprint(modified_stcs)