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

plt.figure(figsize=(8.5, 8.5))
plt.rcParams.update({'font.size': 23})


def plot_clustered_stacked(
    dfall,
    labels=None,
    title='N-Body Strong Scaling',
    H='.',
    **kwargs
    ):
    """Given a list of dataframes, with identical columns and index, create a clustered stacked bar plot. 
labels is a list of the names of the dataframe, used for the legend
title is a string for the title of the plot
H is the hatch used for identification of the different dataframe"""

    n_df = len(dfall)
    n_col = len(dfall[0].columns)
    n_ind = len(dfall[0].index)
    axe = plt.subplot(111)

    for df in dfall:  # for each data frame
        axe = df.plot(  # make bar plots
            kind='bar',
            linewidth=0,
            stacked=True,
            ax=axe,
            legend=False,
            grid=False,
            **kwargs
            )

    (h, l) = axe.get_legend_handles_labels()  # get the handles we want to modify
    for i in range(0, n_df * n_col, n_col):  # len(h) = n_col * n_df
        for (j, pa) in enumerate(h[i:i + n_col]):
            for rect in pa.patches:  # for each index
                rect.set_x(rect.get_x() + 1 / float(n_df + 1) * i
                           / float(n_col))
                rect.set_hatch(H * int(i / n_col))  # edited part
                rect.set_width(1 / float(n_df + 1))

    # axe.set_xticks((np.arange(0, 2 * n_ind, 2) + 1 / float(n_df + 1)) / 2.)

    axe.set_xticklabels(df.index, rotation=0)
    axe.set_title(title, fontsize=25.5)

    # Add invisible data to add another legend

    n = []
    for i in range(n_df):
        n.append(axe.bar(0, 0, color='lightgrey', hatch=H * i))

    l1 = axe.legend(
        h[:n_col],
        l[:n_col],
        ncol=1,
        fontsize='small',
        loc=[0.55, 0.85],
        borderpad=0.5,
        )

    if labels is not None:
        l2 = plt.legend(n, labels, fontsize='small', loc=[0.55, 0.6])

    axe.add_artist(l1)
    return axe


nbodyhs = pd.DataFrame(np.array([[21.13055, 0.0], [9.33885, 0.650429],
                       [3.85851, 0.4817905], [0.7385655, 0.229862]]),
                       index=['1', '2', '4', '8'],
                       columns=['Computation', 'Communication'])

nbodykn = pd.DataFrame(np.array([[23.0521, 0.0], [9.92478, 1.76877],
                       [4.79884, 1.1324], [2.16072, 0.878426]]),
                       index=['1', '2', '4', '8'],
                       columns=['Computation', 'Communication'])

nbodyr5 = pd.DataFrame(np.array([[15.33635, 0.0], [6.37743, 0.28650],
                       [2.2107, 0.28985], [0.620329, 0.35165]]),
                       index=['1', '2', '4', '8'],
                       columns=['Computation', 'Communication'])

nbodyc5 = pd.DataFrame(np.array([[9.85467, 0.0], [7.66376, 0.3513955],
                       [2.81266, 0.31519], [0.719194, 0.3217135]]),
                       index=['1', '2', '4', '8'],
                       columns=['Computation', 'Communication'])

plt.ylabel('Time (s)')
plt.xlabel('Number of Nodes')

# mycmap5 = ListedColormap(["#E8C547", "#30323D", "#4D5061", "#5C80BC", "#CDD1C4", "#F15156", "#38A3A5", "#57CC99", "#DC758F"])
# mycmap6 = ListedColormap(["#30323D", "#4D5061", "#5C80BC", "#CDD1C4", "#F15156", "#38A3A5", "#57CC99", "#DC758F"])

mycmap2 = ListedColormap(['#E8C547', '#F15156'])

plot_clustered_stacked([nbodyhs, nbodykn, nbodyr5, nbodyc5],
                       ['Cori-Haswell-32', 'Cori-KNL-64', 'AWS-R5-32',
                       'AWS-C5-32'], cmap=mycmap2)
plt.tight_layout()
plt.tight_layout(pad=0.5)
plt.savefig('StrongScalingNBody.pdf')
