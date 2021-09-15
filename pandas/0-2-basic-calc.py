import pandas as pd

scientists = pd.read_csv('datasets/scientists.csv')

ages = scientists['Age']
"""
<class 'pandas.core.series.Series'>

0    37
1    61
2    90
3    66
4    56
5    45
6    41
7    77
Name: Age, dtype: int64
"""

ages * 2
"""
0     74
1    122
2    180
3    132
4    112
5     90
6     82
7    154
Name: Age, dtype: int64
"""

ages[ages > ages.mean()]
"""
1    61
2    90
3    66
7    77
Name: Age, dtype: int64
"""

ages > ages.mean()
"""
0    False
1     True
2     True
3     True
4    False
5    False
6    False
7     True
Name: Age, dtype: bool
"""
