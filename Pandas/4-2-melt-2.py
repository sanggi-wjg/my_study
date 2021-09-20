import pandas as pd

dataset = pd.read_csv('datasets/billboard.csv')
"""
     year            artist                    track  ... wk74 wk75  wk76
0    2000             2 Pac  Baby Don't Cry (Keep...  ...  NaN  NaN   NaN
1    2000           2Ge+her  The Hardest Part Of ...  ...  NaN  NaN   NaN
2    2000      3 Doors Down               Kryptonite  ...  NaN  NaN   NaN
3    2000      3 Doors Down                    Loser  ...  NaN  NaN   NaN
4    2000          504 Boyz            Wobble Wobble  ...  NaN  NaN   NaN
..    ...               ...                      ...  ...  ...  ...   ...
312  2000       Yankee Grey     Another Nine Minutes  ...  NaN  NaN   NaN
313  2000  Yearwood, Trisha          Real Live Woman  ...  NaN  NaN   NaN
314  2000   Ying Yang Twins  Whistle While You Tw...  ...  NaN  NaN   NaN
315  2000     Zombie Nation            Kernkraft 400  ...  NaN  NaN   NaN
316  2000   matchbox twenty                     Bent  ...  NaN  NaN   NaN
[317 rows x 81 columns]
"""

dataset = pd.melt(dataset, id_vars = ['year', 'artist', 'track', 'time', 'date.entered'], var_name = 'week', value_name = 'rating')
"""
id_vars 열 고정하고 week 별 나머지 col을 row로 생성
       year            artist  ...  week rating
0      2000             2 Pac  ...   wk1   87.0
1      2000           2Ge+her  ...   wk1   91.0
2      2000      3 Doors Down  ...   wk1   81.0
3      2000      3 Doors Down  ...   wk1   76.0
4      2000          504 Boyz  ...   wk1   57.0
     ...               ...  ...   ...    ...
24087  2000       Yankee Grey  ...  wk76    NaN
24088  2000  Yearwood, Trisha  ...  wk76    NaN
24089  2000   Ying Yang Twins  ...  wk76    NaN
24090  2000     Zombie Nation  ...  wk76    NaN
24091  2000   matchbox twenty  ...  wk76    NaN
[24092 rows x 7 columns]
"""