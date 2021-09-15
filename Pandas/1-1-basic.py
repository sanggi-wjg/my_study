import pandas as pd

df = pd.read_csv('datasets/gapminder.tsv', sep = '\t')

type(df)
"""
<class 'pandas.core.frame.DataFrame'>
"""

type(df['country'])
"""
<class 'pandas.core.series.Series'>
"""

df.head()
"""
Return the first `n` rows.

       country continent  year  lifeExp       pop   gdpPercap
0  Afghanistan      Asia  1952   28.801   8425333  779.445314
1  Afghanistan      Asia  1957   30.332   9240934  820.853030
2  Afghanistan      Asia  1962   31.997  10267083  853.100710
3  Afghanistan      Asia  1967   34.020  11537966  836.197138
4  Afghanistan      Asia  1972   36.088  13079460  739.981106
"""

df.tail()
"""
Return the last `n` rows.

       country continent  year  lifeExp       pop   gdpPercap
1699  Zimbabwe    Africa  1987   62.351   9216418  706.157306
1700  Zimbabwe    Africa  1992   60.377  10704340  693.420786
1701  Zimbabwe    Africa  1997   46.809  11404948  792.449960
1702  Zimbabwe    Africa  2002   39.989  11926563  672.038623
1703  Zimbabwe    Africa  2007   43.487  12311143  469.709298
"""

df.shape
"""
Return a tuple of the shape of the underlying data.

(1704, 6)
"""

df.dtypes
"""
Return the dtype object of the underlying data.

country       object
continent     object
year           int64
lifeExp      float64
pop            int64
gdpPercap    float64
dtype: object
"""

df.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1704 entries, 0 to 1703
Data columns (total 6 columns):
 #   Column     Non-Null Count  Dtype  
---  ------     --------------  -----  
 0   country    1704 non-null   object 
 1   continent  1704 non-null   object 
 2   year       1704 non-null   int64  
 3   lifeExp    1704 non-null   float64
 4   pop        1704 non-null   int64  
 5   gdpPercap  1704 non-null   float64
dtypes: float64(2), int64(2), object(2)
memory usage: 80.0+ KB
"""

df.memory_usage(deep = True)
"""
Return the memory usage of each column in bytes.

Index           128
country      111360
continent    107184
year          13632
lifeExp       13632
pop           13632
gdpPercap     13632
dtype: int64
"""
