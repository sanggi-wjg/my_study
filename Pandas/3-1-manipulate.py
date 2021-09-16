import pandas as pd

df1 = pd.read_csv('datasets/concat_1.csv')
df2 = pd.read_csv('datasets/concat_2.csv')
df3 = pd.read_csv('datasets/concat_3.csv')

dataset = pd.concat([df1, df2, df3], ignore_index = True)
"""
      A    B    C    D
0    a0   b0   c0   d0
1    a1   b1   c1   d1
2    a2   b2   c2   d2
3    a3   b3   c3   d3
4    a4   b4   c4   d4
5    a5   b5   c5   d5
6    a6   b6   c6   d6
7    a7   b7   c7   d7
8    a8   b8   c8   d8
9    a9   b9   c9   d9
10  a10  b10  c10  d10
11  a11  b11  c11  d11
"""

# new_series = pd.Series(['n1', 'n2', 'n3', 'n4'])
# dataset = pd.concat([dataset, new_series])
"""
      A    B    C    D    0
0    a0   b0   c0   d0  NaN
1    a1   b1   c1   d1  NaN
2    a2   b2   c2   d2  NaN
3    a3   b3   c3   d3  NaN
4    a4   b4   c4   d4  NaN
5    a5   b5   c5   d5  NaN
6    a6   b6   c6   d6  NaN
7    a7   b7   c7   d7  NaN
8    a8   b8   c8   d8  NaN
9    a9   b9   c9   d9  NaN
10  a10  b10  c10  d10  NaN
11  a11  b11  c11  d11  NaN
0   NaN  NaN  NaN  NaN   n1
1   NaN  NaN  NaN  NaN   n2
2   NaN  NaN  NaN  NaN   n3
3   NaN  NaN  NaN  NaN   n4
"""

# 1
new_df = pd.DataFrame([['n1', 'n2', 'n3', 'n4']], columns = ['A', 'B', 'C', 'D'])
dataset = pd.concat([dataset, new_df], ignore_index = True)

# 2
dataset.append(new_df, ignore_index = True)

# 3
data_dict = { 'A': 'n1', 'B': 'n2', 'C': 'n3', 'D': 'n4' }
dataset.append(data_dict, ignore_index = True)
"""
      A    B    C    D
0    a0   b0   c0   d0
1    a1   b1   c1   d1
2    a2   b2   c2   d2
3    a3   b3   c3   d3
4    a4   b4   c4   d4
5    a5   b5   c5   d5
6    a6   b6   c6   d6
7    a7   b7   c7   d7
8    a8   b8   c8   d8
9    a9   b9   c9   d9
10  a10  b10  c10  d10
11  a11  b11  c11  d11
12   n1   n2   n3   n4
"""

