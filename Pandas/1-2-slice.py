import pandas as pd

df = pd.read_csv('datasets/gapminder.tsv', sep = '\t')

subset = df[['country', 'continent', 'year']]
"""
dataset dataframe 에서 일부 column 만 가져옴
"""

foo = df.loc[0]
"""
<class 'pandas.core.series.Series'>

country      Afghanistan
continent           Asia
year                1952
lifeExp           28.801
pop              8425333
gdpPercap     779.445314
Name: 0, dtype: object
"""

foo['country']
"""
'Afghanistan'
"""

df.loc[df.shape[0] - 1]
"""
country        Zimbabwe
continent        Africa
year               2007
lifeExp          43.487
pop            12311143
gdpPercap    469.709298
Name: 1703, dtype: object
"""

df.loc[[0, 1, 2]]
"""
       country continent  year  lifeExp       pop   gdpPercap
0  Afghanistan      Asia  1952   28.801   8425333  779.445314
1  Afghanistan      Asia  1957   30.332   9240934  820.853030
2  Afghanistan      Asia  1962   31.997  10267083  853.100710
"""

df.at[0, 'country']
df.loc[0]['country']
df.loc[0].at['country']
"""
'Afghanistan'
"""

df.loc[:, ['country', 'year']]
"""
          country  year
0     Afghanistan  1952
1     Afghanistan  1957
2     Afghanistan  1962
3     Afghanistan  1967
4     Afghanistan  1972
           ...   ...
1699     Zimbabwe  1987
1700     Zimbabwe  1992
1701     Zimbabwe  1997
1702     Zimbabwe  2002
1703     Zimbabwe  2007
"""

df.iloc[0]
"""
country      Afghanistan
continent           Asia
year                1952
lifeExp           28.801
pop              8425333
gdpPercap     779.445314
Name: 0, dtype: object
"""

"""
loc 과 iloc 은 기본적으로 데이터 행을 가져오는 것은 동일하나
index를 다루는 것에서 차이가 난다.

loc 은 컬럼명이나 특정 조건식 등의 사람이 읽기 좋은 것
iloc 는 컴퓨터가 읽기 좋으것 으로 숫자를 넣는다

df.loc[0]['country']
'Afghanistan'

df.iloc[0, 0]
'Afghanistan'
"""

df.iloc[-1]
"""
country        Zimbabwe
continent        Africa
year               2007
lifeExp          43.487
pop            12311143
gdpPercap    469.709298
Name: 1703, dtype: object
"""

df.loc[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']]
df.iloc[[0, 99, 999], [0, 3, 5]]
"""
         country  lifeExp    gdpPercap
0    Afghanistan   28.801   779.445314
99    Bangladesh   43.453   721.186086
999     Mongolia   51.253  1226.041130
"""
