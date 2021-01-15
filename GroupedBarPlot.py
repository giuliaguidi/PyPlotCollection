#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.cm as cm
import matplotlib.font_manager
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

plt.rcParams['font.family'] = 'Serif'

# Then, just call

plt.figure(figsize=(8.5, 8))
plt.rcParams.update({'font.size': 21.5})


def plot_clustered_stacked(
    dfall,
    labels=None,
    title='Compute Performance',
    H='.',
    **kwargs
    ):
    """Given a list of dataframes, with identical columns and index, create a clustered stacked bar plot. 
labels is a list of the names of the dataframe, used for the legend
title is a string for the title of the plot
H is the hatch used for identification of the different dataframe"""

    n_df = len(dfall)
    n_col = len(dfall[0].columns)

    # n_col = int(n_col/2)

    n_ind = len(dfall[0].index)
    axe = plt.subplot(111)

    for df in dfall:  # for each data frame
        axe = df.plot(  # make bar plots
            kind='bar',
            linewidth=0,
            stacked=False,
            ax=axe,
            legend=False,
            grid=False,
            **kwargs
            )

    width = 0.35  # the width of the bars

    (h, l) = axe.get_legend_handles_labels()  # get the handles we want to modify
    for i in range(0, n_df * n_col, n_col):  # len(h) = n_col * n_df
        for (j, pa) in enumerate(h[i:i + n_col]):
            for rect in pa.patches:  # for each index
                rect.set_x(rect.get_x())

    # axe.set_xticks((np.arange(0, 2 * n_ind, 2) + 1 / float(n_df + 1)) / 2.)

    axe.set_xticklabels(df.index, rotation=0)
    axe.set_title(title, fontsize=27.5)

    # Add invisible data to add another legend

    n = []
    for i in range(n_df):
        n.append(axe.bar(0, 0, color='lightgrey'))

    l1 = axe.legend(h[:n_col], l[:n_col], ncol=1, fontsize='small',
                    loc='upper left')

    # if labels is not None:
    #     l2 = plt.legend(n, labels, fontsize='small', loc=[0.55, 0.6])

    # axe.add_artist(l1)

    return axe


linpackx = pd.DataFrame(np.array([[934.206, 1177], [1835.60, 3046],
                        [2176.16, 2560], [2076.06, 3456]]),
                        index=['Cori-Haswell', 'Cori-KNL', 'AWS-R5',
                        'AWS-C5'], columns=['Linpack Peak',
                        'Theoretical Peak'])

plt.ylabel('GFlops/s')
plt.xlabel('Platform')

# mycmap5 = ListedColormap(["#E8C547", "#30323D", "#4D5061", "#5C80BC", "#CDD1C4", "#F15156", "#38A3A5", "#57CC99", "#DC758F"])
# mycmap6 = ListedColormap(["#30323D", "#4D5061", "#5C80BC", "#CDD1C4", "#F15156", "#38A3A5", "#57CC99", "#DC758F"])

mycmap2 = ListedColormap(['bisque', 'darkorange'])

plot_clustered_stacked([linpackx], cmap=mycmap2)
plt.tight_layout()
plt.tight_layout(pad=0.5)
plt.savefig('ComputePerformance.pdf')
