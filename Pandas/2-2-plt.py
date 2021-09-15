import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

dataset = sns.load_dataset('tips')
"""
     total_bill   tip     sex smoker   day    time  size
0         16.99  1.01  Female     No   Sun  Dinner     2
1         10.34  1.66    Male     No   Sun  Dinner     3
2         21.01  3.50    Male     No   Sun  Dinner     3
3         23.68  3.31    Male     No   Sun  Dinner     2
4         24.59  3.61  Female     No   Sun  Dinner     4
..          ...   ...     ...    ...   ...     ...   ...
239       29.03  5.92    Male     No   Sat  Dinner     3
240       27.18  2.00  Female    Yes   Sat  Dinner     2
241       22.67  2.00    Male    Yes   Sat  Dinner     2
242       17.82  1.75    Male     No   Sat  Dinner     2
243       18.78  3.00  Female     No  Thur  Dinner     2
[244 rows x 7 columns]
"""

# Histogram
hist_fig: Figure = plt.figure()
axes: Axes = hist_fig.add_subplot(1, 1, 1)

axes.hist(dataset['total_bill'], bins = 10)
axes.set_title('Histogram of Total bill')
axes.set_xlabel('Total bill')
axes.set_ylabel('Frequency')
plt.show()

# Scatter
scatter_fig: Figure = plt.figure()
axes_2: Axes = scatter_fig.add_subplot(1, 1, 1)

axes_2.scatter(dataset['total_bill'], dataset['tip'])
axes_2.set_title('Scatter of Total bill vs Tip')
axes_2.set_xlabel('Total bill')
axes_2.set_ylabel('Tip')
plt.show()

# Scatter custom
dataset['sex_color'] = dataset['sex'].apply(func = lambda x: 1 if x == 'Male' else 0)
scatter_custom_fig: Figure = plt.figure()
axes_2_c: Axes = scatter_custom_fig.add_subplot(1, 1, 1)

axes_2_c.scatter(
    dataset['total_bill'], dataset['tip'],
    s = dataset['size'] * 20,
    c = dataset['sex_color'],
    alpha = 0.5
)

axes_2_c.set_title('Custom Scatter of Total bill vs Tip')
axes_2_c.set_xlabel('Total bill')
axes_2_c.set_ylabel('Tip')
plt.show()

# Box
box_fig: Figure = plt.figure()
axes_3: Axes = box_fig.add_subplot(1, 1, 1)

tip_dataset = dataset[['tip', 'sex']]
axes_3.boxplot(
    [
        tip_dataset[tip_dataset['sex'] == 'Male']['tip'],
        tip_dataset[tip_dataset['sex'] == 'Female']['tip']
    ], labels = ['Male', 'Female']
)
axes_3.set_title('Box of Tips by Sex')
axes_3.set_xlabel('Sex')
axes_3.set_ylabel('Tip')

plt.show()
