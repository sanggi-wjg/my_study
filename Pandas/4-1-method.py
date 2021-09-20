import pandas as pd

dataset = pd.read_csv('datasets/pew.csv')
"""
                   religion  <$10k  ...  >150k  Don't know/refused
0                  Agnostic     27  ...     84                  96
1                   Atheist     12  ...     74                  76
2                  Buddhist     27  ...     53                  54
3                  Catholic    418  ...    633                1489
4        Don’t know/refused     15  ...     18                 116
5          Evangelical Prot    575  ...    414                1529
6                     Hindu      1  ...     54                  37
7   Historically Black Prot    228  ...     78                 339
8         Jehovah's Witness     20  ...      6                  37
9                    Jewish     19  ...    151                 162
10            Mainline Prot    289  ...    634                1328
11                   Mormon     29  ...     42                  69
12                   Muslim      6  ...      6                  22
13                 Orthodox     13  ...     46                  73
14          Other Christian      9  ...     12                  18
15             Other Faiths     20  ...     41                  71
16    Other World Religions      5  ...      4                   8
17             Unaffiliated    217  ...    258                 597
[18 rows x 11 columns]
"""

dataset = dataset.iloc[:, 0:2]
"""
                   religion  <$10k
0                  Agnostic     27
1                   Atheist     12
2                  Buddhist     27
3                  Catholic    418
4        Don’t know/refused     15
5          Evangelical Prot    575
6                     Hindu      1
7   Historically Black Prot    228
8         Jehovah's Witness     20
9                    Jewish     19
10            Mainline Prot    289
11                   Mormon     29
12                   Muslim      6
13                 Orthodox     13
14          Other Christian      9
15             Other Faiths     20
16    Other World Religions      5
17             Unaffiliated    217
"""

# dataset = pd.melt(dataset, id_vars = 'religion')
"""
                   religion variable  value
0                  Agnostic    <$10k     27
1                   Atheist    <$10k     12
2                  Buddhist    <$10k     27
3                  Catholic    <$10k    418
4        Don’t know/refused    <$10k     15
5          Evangelical Prot    <$10k    575
6                     Hindu    <$10k      1
7   Historically Black Prot    <$10k    228
8         Jehovah's Witness    <$10k     20
9                    Jewish    <$10k     19
10            Mainline Prot    <$10k    289
11                   Mormon    <$10k     29
12                   Muslim    <$10k      6
13                 Orthodox    <$10k     13
14          Other Christian    <$10k      9
15             Other Faiths    <$10k     20
16    Other World Religions    <$10k      5
17             Unaffiliated    <$10k    217
"""

dataset = pd.melt(dataset, id_vars = 'religion', var_name = 'income', value_name = 'count')
"""
                   religion income  count
0                  Agnostic  <$10k     27
1                   Atheist  <$10k     12
2                  Buddhist  <$10k     27
3                  Catholic  <$10k    418
4        Don’t know/refused  <$10k     15
5          Evangelical Prot  <$10k    575
6                     Hindu  <$10k      1
7   Historically Black Prot  <$10k    228
8         Jehovah's Witness  <$10k     20
9                    Jewish  <$10k     19
10            Mainline Prot  <$10k    289
11                   Mormon  <$10k     29
12                   Muslim  <$10k      6
13                 Orthodox  <$10k     13
14          Other Christian  <$10k      9
15             Other Faiths  <$10k     20
16    Other World Religions  <$10k      5
17             Unaffiliated  <$10k    217
"""