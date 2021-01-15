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
    1.60,
    3.19,
    6.45,
    12.98,
    25.95,
    52.78,
    103.81,
    210.81,
    420.97,
    803.92,
    1232.58,
    1874.89,
    2511.45,
    5013.28,
    8031.93,
    8796.36,
    9453.84,
    9699.59,
    9811.70,
    9891.44,
    9917.75,
    9917.84,
    9273.74,
    ]
ykn = [
    0.48,
    0.96,
    1.90,
    3.82,
    7.57,
    15.20,
    30.25,
    59.57,
    117.18,
    232.42,
    337.70,
    564.90,
    871.71,
    1525.24,
    2977.24,
    6020.70,
    6874.82,
    7264.29,
    7605.28,
    7881.76,
    8036.62,
    8086.89,
    8098.91,
    ]
yr5 = [
    7.29,
    14.96,
    29.98,
    60.09,
    118.91,
    239.59,
    309.33,
    384.52,
    670.46,
    1293.38,
    2370.28,
    4042.90,
    3255.70,
    5815.38,
    8625.46,
    12950.30,
    17012.97,
    20394.48,
    22346.43,
    21157.04,
    13922.04,
    10807.90,
    10865.02,
    ]
yc5 = [
    7.62,
    15.40,
    30.90,
    61.87,
    112.76,
    237.87,
    316.92,
    402.05,
    719.07,
    1280.19,
    2380.28,
    4170.01,
    3614.82,
    6453.26,
    9560.88,
    14165.66,
    18637.28,
    22092.10,
    24231.37,
    22802.64,
    14614.72,
    11288.82,
    11313.46,
    ]

x = [
    1,
    2,
    4,
    8,
    16,
    32,
    64,
    128,
    256,
    512,
    1024,
    2048,
    4096,
    8192,
    16384,
    32768,
    65536,
    131072,
    262144,
    524288,
    1048576,
    2097152,
    4194304,
    ]

plt.plot(
    x,
    yhs,
    '-p',
    label='Cori-Haswell',
    color='#7D82B8',
    fillstyle='none',
    linewidth=2.0,
    markersize=12.0,
    )
plt.plot(
    x,
    ykn,
    '-s',
    label='Cori-KNL',
    color='#613F75',
    fillstyle='none',
    linewidth=2.0,
    markersize=10.0,
    )
plt.plot(
    x,
    yr5,
    '-^',
    label='AWS-R5',
    color='#C75146',
    fillstyle='none',
    linewidth=2.0,
    markersize=10.0,
    )
plt.plot(
    x,
    yc5,
    '-.D',
    label='AWS-C5',
    color='#EA8C55',
    fillstyle='none',
    linewidth=2.0,
    markersize=8.0,
    )

plt.yscale('log')
plt.xscale('log')

plt.title('OSU MPI Point-to-Point Bandwidth')

plt.xlabel('Packet Size in Bytes')
plt.ylabel('MB/s (Log Scale)')

plt.tight_layout()
plt.legend(fontsize='small')
plt.savefig('OSUPointToPointBandwidth.pdf')
