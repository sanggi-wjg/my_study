import seaborn as sns
import matplotlib.pyplot as plt

dataset = sns.load_dataset("anscombe")

"""
   dataset     x      y
0        I  10.0   8.04
1        I   8.0   6.95
2        I  13.0   7.58
3        I   9.0   8.81
4        I  11.0   8.33
5        I  14.0   9.96
6        I   6.0   7.24
7        I   4.0   4.26
8        I  12.0  10.84
9        I   7.0   4.82
10       I   5.0   5.68
11      II  10.0   9.14
12      II   8.0   8.14
13      II  13.0   8.74
14      II   9.0   8.77
15      II  11.0   9.26
16      II  14.0   8.10
17      II   6.0   6.13
18      II   4.0   3.10
19      II  12.0   9.13
20      II   7.0   7.26
21      II   5.0   4.74
22     III  10.0   7.46
23     III   8.0   6.77
24     III  13.0  12.74
25     III   9.0   7.11
26     III  11.0   7.81
27     III  14.0   8.84
28     III   6.0   6.08
29     III   4.0   5.39
30     III  12.0   8.15
31     III   7.0   6.42
32     III   5.0   5.73
33      IV   8.0   6.58
34      IV   8.0   5.76
35      IV   8.0   7.71
36      IV   8.0   8.84
37      IV   8.0   8.47
38      IV   8.0   7.04
39      IV   8.0   5.25
40      IV  19.0  12.50
41      IV   8.0   5.56
42      IV   8.0   7.91
43      IV   8.0   6.89
"""

dataset_1 = dataset[dataset['dataset'] == 'I']
dataset_2 = dataset[dataset['dataset'] == 'II']
dataset_3 = dataset[dataset['dataset'] == 'III']
dataset_4 = dataset[dataset['dataset'] == 'IV']
"""
   dataset     x      y
0        I  10.0   8.04
1        I   8.0   6.95
2        I  13.0   7.58
3        I   9.0   8.81
4        I  11.0   8.33
5        I  14.0   9.96
6        I   6.0   7.24
7        I   4.0   4.26
8        I  12.0  10.84
9        I   7.0   4.82
10       I   5.0   5.68
"""

# plt.plot(dataset_1['x'], dataset_1['y'], 'o')

fig = plt.figure()
fig.suptitle('Anscombe Data')
fig.tight_layout()

axe1 = fig.add_subplot(2, 2, 1)
axe2 = fig.add_subplot(2, 2, 2)
axe3 = fig.add_subplot(2, 2, 3)
axe4 = fig.add_subplot(2, 2, 4)

axe1.set_title('dataset 1')
axe2.set_title('dataset 2')
axe3.set_title('dataset 3')
axe4.set_title('dataset 4')

axe1.plot(dataset_1['x'], dataset_1['y'], 'o')
axe2.plot(dataset_2['x'], dataset_2['y'], 'o')
axe3.plot(dataset_3['x'], dataset_3['y'], 'o')
axe4.plot(dataset_4['x'], dataset_4['y'], 'o')

plt.show()
# 2-1-1.PNG
