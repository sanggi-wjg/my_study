import pandas as pd

df1 = pd.read_csv('datasets/concat_1.csv')
df2 = pd.read_csv('datasets/concat_2.csv')
df3 = pd.read_csv('datasets/concat_3.csv')

df1.index = [0, 1, 2, 3]
df2.index = [0, 1, 4, 5]
df2.index = [2, 3, 6, 7]

dataset = pd.concat([df1, df2, df3], axis = 1, join = 'inner')
"""
join default 는 outer 이다.

    A   B   C   D   A   B   C   D    A    B    C    D
2  a2  b2  c2  d2  a4  b4  c4  d4  a10  b10  c10  d10
3  a3  b3  c3  d3  a5  b5  c5  d5  a11  b11  c11  d11
"""

person_df = pd.read_csv('datasets/survey_person.csv')
site_df = pd.read_csv('datasets/survey_site.csv')
survey_df = pd.read_csv('datasets/survey_survey.csv')
visited_df = pd.read_csv('datasets/survey_visited.csv')

merge_df = site_df.merge(visited_df, left_on = 'name', right_on = 'site')
"""
    name    lat    long  ident   site       dated
0   DR-1 -49.85 -128.57    619   DR-1  1927-02-08
1   DR-1 -49.85 -128.57    622   DR-1  1927-02-10
2   DR-1 -49.85 -128.57    844   DR-1  1932-03-22
3   DR-3 -47.15 -126.72    734   DR-3  1939-01-07
4   DR-3 -47.15 -126.72    735   DR-3  1930-01-12
5   DR-3 -47.15 -126.72    751   DR-3  1930-02-26
6   DR-3 -47.15 -126.72    752   DR-3         NaN
7  MSK-4 -48.87 -123.40    837  MSK-4  1932-01-14
"""
