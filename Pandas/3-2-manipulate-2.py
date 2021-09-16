import pandas as pd

df1 = pd.read_csv('datasets/concat_1.csv')
df2 = pd.read_csv('datasets/concat_2.csv')
df3 = pd.read_csv('datasets/concat_3.csv')

dataset = pd.concat([df1, df2, df3], axis = 1)
"""
    A   B   C   D   A   B   C   D    A    B    C    D
0  a0  b0  c0  d0  a4  b4  c4  d4   a8   b8   c8   d8
1  a1  b1  c1  d1  a5  b5  c5  d5   a9   b9   c9   d9
2  a2  b2  c2  d2  a6  b6  c6  d6  a10  b10  c10  d10
3  a3  b3  c3  d3  a7  b7  c7  d7  a11  b11  c11  d11
"""

dataset['A']
"""
    A   A    A
0  a0  a4   a8
1  a1  a5   a9
2  a2  a6  a10
3  a3  a7  a11
"""

dataset['N'] = ['n1', 'n2', 'n3', 'n4']
"""
    A   B   C   D   A   B   C   D    A    B    C    D   N
0  a0  b0  c0  d0  a4  b4  c4  d4   a8   b8   c8   d8  n1
1  a1  b1  c1  d1  a5  b5  c5  d5   a9   b9   c9   d9  n2
2  a2  b2  c2  d2  a6  b6  c6  d6  a10  b10  c10  d10  n3
3  a3  b3  c3  d3  a7  b7  c7  d7  a11  b11  c11  d11  n4
"""

dataset = pd.concat([df1, df2, df3], axis = 1, ignore_index = True)
"""
   0   1   2   3   4   5   6   7    8    9    10   11
0  a0  b0  c0  d0  a4  b4  c4  d4   a8   b8   c8   d8
1  a1  b1  c1  d1  a5  b5  c5  d5   a9   b9   c9   d9
2  a2  b2  c2  d2  a6  b6  c6  d6  a10  b10  c10  d10
3  a3  b3  c3  d3  a7  b7  c7  d7  a11  b11  c11  d11
"""

df2.columns = ['E', 'F', 'G', 'H']
df3.columns = ['I', 'J', 'K', 'L']
dataset = pd.concat([df1, df2, df3], axis = 1)
"""
    A   B   C   D   E   F   G   H    I    J    K    L
0  a0  b0  c0  d0  a4  b4  c4  d4   a8   b8   c8   d8
1  a1  b1  c1  d1  a5  b5  c5  d5   a9   b9   c9   d9
2  a2  b2  c2  d2  a6  b6  c6  d6  a10  b10  c10  d10
3  a3  b3  c3  d3  a7  b7  c7  d7  a11  b11  c11  d11
"""
