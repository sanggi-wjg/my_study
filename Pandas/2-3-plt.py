import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from pandas import DataFrame
from pandas.core.groupby import DataFrameGroupBy

dataset: DataFrame = sns.load_dataset('tips')

# Group By -> Count
dataset_by_day: DataFrameGroupBy = dataset.groupby('day')['tip']
colors = sns.color_palette('hls', dataset_by_day.ngroups)
sum_by_day = dataset_by_day.sum()
"""
# dataset_by_day
day
Thur    62
Fri     19
Sat     87
Sun     76
Name: day, dtype: int64

# sum_by_day
day
Thur    171.83
Fri      51.96
Sat     260.40
Sun     247.39
Name: tip, dtype: float64
"""

# Bar
bar_fig: Figure = plt.figure()
axes: Axes = bar_fig.add_subplot(1, 1, 1)

axes.bar(sum_by_day.index, sum_by_day, color = colors)
axes.set_xlabel('Day')
axes.set_xlabel('Total Tips')
plt.show()

# Violin
violin_fig = plt.figure()
axes_2: Axes = violin_fig.add_subplot(1, 1, 1)

axes_2.violinplot(dataset['total_bill'])
plt.show()

# Line
line_fig = plt.figure()
axes_3: Axes = line_fig.add_subplot(1, 1, 1)

axes_3.plot(dataset['total_bill'], label = 'Total bill')
axes_3.plot(dataset['tip'], label = 'Tip')

plt.legend(loc = 'upper right')
plt.show()
plt.close()
