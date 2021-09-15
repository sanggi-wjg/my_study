import pandas as pd

s = pd.Series(['sample', 10])
"""
0    sample
1        10
dtype: object
"""

s = pd.Series(['JayG', 'SangGi'], index = ['Person', 'Who'])
"""
Person    JayG
Who       SangGi
dtype: object
"""

scientists = pd.DataFrame({
    'Name'      : ['Rosaline Franklin', 'William Gosset'],
    'Occupation': ['Chemist', 'Statistician'],
    'Born'      : ['1920-07-25', '1876-06-13'],
    'Died'      : ['1958-04-16', '1937-10-16'],
    'Age'       : [37, 61]
})
"""
                Name    Occupation        Born        Died  Age
0  Rosaline Franklin       Chemist  1920-07-25  1958-04-16   37
1     William Gosset  Statistician  1876-06-13  1937-10-16   61
"""

scientists = pd.DataFrame(
    data = { 'Occupation': ['Chemist', 'Statistician'],
             'Born'      : ['1920-07-25', '1876-06-13'],
             'Died'      : ['1958-04-16', '1937-10-16'],
             'Age'       : [37, 61] },
    index = ['Rosaline Franklin', 'William Gosset'],
    columns = ['Occupation', 'Born', 'Age', 'Died'])
"""
                     Occupation        Born  Age        Died
Rosaline Franklin       Chemist  1920-07-25   37  1958-04-16
William Gosset     Statistician  1876-06-13   61  1937-10-16
"""

scientists.index
"""
Index(['Rosaline Franklin', 'William Gosset'], dtype='object')
"""

scientists.keys()
"""
Index(['Occupation', 'Born', 'Age', 'Died'], dtype='object')
"""

scientists.values
"""
array([['Chemist', '1920-07-25', 37, '1958-04-16'],
       ['Statistician', '1876-06-13', 61, '1937-10-16']], dtype=object)
"""

for occupation, born, age, died in scientists.values:
    print(occupation, born, age, died)
"""
Chemist      1920-07-25 37 1958-04-16
Statistician 1876-06-13 61 1937-10-16
"""

ages = scientists['Age']
ages.mean()
ages.min()
ages.max()
ages.std()
"""
49.0              <class 'numpy.float64'>
37                <class 'numpy.int64'>
61                <class 'numpy.int64'>
16.97056274847714 <class 'numpy.float64'>
"""
