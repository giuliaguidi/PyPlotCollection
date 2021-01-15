#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.cm as cm
import matplotlib.font_manager
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

plt.rcParams['font.family'] = 'serif'

# Then, just call

plt.figure(figsize=(8.5, 8.5))
plt.rcParams.update({'font.size': 23})

yhs = [
    103.2,
    108.5,
    98.1,
    144.7,
    123.6,
    168.6,
    160.2,
    177.1,
    149.2,
    195.4,
    169.5,
    198.1,
    144.8,
    99.9,
    101.7,
    94.4,
    104.2,
    104.4,
    100.6,
    51.3,
    51.6,
    51.3,
    51.5,
    51.4,
    51.3,
    51.3,
    51.4,
    51.1,
    45.1,
    38.9,
    32.3,
    26.9,
    26.9,
    26.9,
    26.9,
    26.9,
    26.9,
    26.9,
    26.9,
    26.9,
    26.8,
    26.7,
    26.7,
    26.7,
    26.7,
    26.7,
    26.7,
    26.7,
    26.7,
    15.0,
    9.9,
    30.3,
    23.4,
    18.9,
    17.4,
    16.6,
    16.6,
    16.6,
    16.6,
    16.6,
    16.6,
    16.6,
    16.6,
    16.6,
    ]
ykn = [
    9.5,
    12.4,
    15.7,
    19.0,
    15.0,
    18.7,
    21.3,
    23.9,
    25.0,
    30.1,
    30.1,
    33.5,
    34.8,
    36.3,
    37.1,
    37.0,
    38.6,
    37.5,
    37.0,
    26.5,
    26.6,
    27.3,
    27.3,
    27.7,
    21.0,
    21.3,
    21.4,
    21.5,
    21.6,
    21.7,
    21.8,
    21.9,
    21.9,
    21.8,
    21.9,
    21.8,
    19.6,
    13.0,
    12.5,
    12.3,
    12.2,
    12.2,
    12.2,
    12.2,
    12.2,
    12.2,
    12.2,
    12.2,
    12.2,
    12.2,
    12.2,
    12.2,
    12.2,
    12.2,
    12.2,
    12.2,
    12.2,
    12.2,
    12.2,
    12.2,
    12.2,
    12.2,
    12.1,
    12.1,
    ]
yr5 = [
    57.0,
    66.2,
    72.3,
    73.8,
    77.7,
    78.3,
    76.5,
    80.1,
    80.2,
    79.5,
    79.2,
    81.2,
    80.6,
    78.5,
    79.0,
    78.9,
    80.1,
    72.7,
    56.7,
    40.3,
    40.3,
    40.0,
    40.1,
    39.9,
    39.8,
    39.8,
    39.2,
    38.2,
    34.4,
    30.4,
    27.6,
    24.2,
    22.6,
    21.6,
    20.6,
    19.9,
    19.6,
    19.3,
    19.3,
    19.2,
    19.1,
    19.0,
    19.1,
    19.1,
    19.0,
    19.1,
    19.0,
    19.0,
    18.7,
    15.1,
    14.4,
    13.6,
    11.3,
    10.9,
    10.9,
    11.2,
    11.9,
    12.2,
    12.2,
    12.5,
    12.5,
    12.7,
    12.4,
    12.7,
    ]
yc5 = [
    60.7,
    67.8,
    72.1,
    71.7,
    87.0,
    100.5,
    101.0,
    102.5,
    103.9,
    103.9,
    104.5,
    104.9,
    104.5,
    105.3,
    105.3,
    105.2,
    105.5,
    101.8,
    83.9,
    65.3,
    67.1,
    66.9,
    67.3,
    65.9,
    67.2,
    62.0,
    62.3,
    61.6,
    62.0,
    42.7,
    27.4,
    18.7,
    15.8,
    14.2,
    12.5,
    11.6,
    10.8,
    10.4,
    10.3,
    10.1,
    10.1,
    10.1,
    10.1,
    10.1,
    10.0,
    10.0,
    10.0,
    10.1,
    10.0,
    10.0,
    9.8,
    9.7,
    9.5,
    9.5,
    9.4,
    9.4,
    9.2,
    9.2,
    9.2,
    9.3,
    9.2,
    9.2,
    9.1,
    9.2,
    ]

x = [
    2.0,
    2.7,
    3.4,
    4.1,
    5.4,
    6.8,
    8.2,
    10.9,
    13.6,
    16.4,
    21.8,
    27.3,
    32.8,
    43.6,
    54.6,
    65.5,
    87.4,
    109.2,
    131.1,
    174.7,
    218.4,
    262.1,
    349.5,
    436.9,
    524.3,
    699.0,
    873.8,
    1048.6,
    1398.1,
    1747.6,
    2097.2,
    2796.2,
    3495.2,
    4194.3,
    5592.4,
    6990.5,
    8388.6,
    11184.8,
    13981.0,
    16777.2,
    22369.6,
    27962.0,
    33554.4,
    44739.2,
    55924.0,
    67108.9,
    89478.5,
    111848.1,
    134217.7,
    178956.9,
    223696.2,
    268435.5,
    357913.9,
    447392.4,
    536870.9,
    715827.8,
    894784.8,
    1073741.8,
    1431655.7,
    1789569.7,
    2147483.6,
    2863311.5,
    3579139.4,
    4294967.3,
    ]

plt.plot(
    x,
    yhs,
    '-p',
    label='Cori-Haswell',
    color='#7D82B8',
    fillstyle='none',
    linewidth=2.0,
    markersize=10.0,
    )
plt.plot(
    x,
    ykn,
    '-s',
    label='Cori-KNL',
    color='#613F75',
    fillstyle='none',
    linewidth=2.0,
    markersize=8.0,
    )
plt.plot(
    x,
    yr5,
    '-^',
    label='AWS-R5',
    color='#C75146',
    fillstyle='none',
    linewidth=2.0,
    markersize=8.0,
    )
plt.plot(
    x,
    yc5,
    '-.D',
    label='AWS-C5',
    color='#EA8C55',
    fillstyle='none',
    linewidth=2.0,
    markersize=6.0,
    )

plt.axvline(x=64, color='r', label='L1')
plt.axvline(x=256, color='r', linestyle='--', label='Cori-Haswell-L2')
plt.axvline(x=1000, color='r', linestyle=':', label='Others-L2')
plt.axvline(x=4000, color='r', linestyle='-.', label='Cori-Haswell-L3')

plt.yscale('log')
plt.xscale('log')

plt.title('Memory Hierarchy Performance')

plt.xlabel('KByte')
plt.ylabel('GB/s')

plt.tight_layout()
plt.legend(fontsize='small')
plt.savefig('CacheBench.pdf')