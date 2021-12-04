#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('classic')

s_boy = np.array([
    [3.5, 4.1, 4.7, 5.3, 5.9, 6.4, 6.9, 7.2, 7.6, 7.9, 8.1],
    [52.9, 55.8, 58.3, 60.5, 62.4, 64.1, 65.7, 67.0, 68.3, 69.6, 70.7]
])

small_boy = np.array([
    (3.5, 52.9),
    (4.1, 55.8),
    (4.7, 58.3),
    (5.3, 60.5),
    (5.9, 62.4),
    (6.4, 64.1),
    (6.9, 65.7),
    (7.2, 67.0),
    (7.6, 68.3),
    (7.9, 69.6),
    (8.1, 70.7)
], dtype=[('weight', 'f4'), ('height', 'f4')])

large_boy = np.array([
    (6.8, 63.2),
    (7.7, 66.4),
    (8.5, 69.1),
    (9.2, 71.3),
    (9.8, 73.2),
    (10.3, 74.8),
    (10.8, 76.3),
    (11.3, 77.3),
    (11.7, 78.9),
    (12.0, 80.2),
    (12.4, 81.5)
], dtype=[('weight', 'f4'), ('height', 'f4')])

s_boy_weight = np.array([3.5, 4.1, 4.7, 5.3, 5.9, 6.4, 6.9, 7.2, 7.6, 7.9, 8.1])
s_boy_height = np.array([52.9, 55.8, 58.3, 60.5, 62.4, 64.1, 65.7, 67.0, 68.3, 69.6, 70.7])

with plt.style.context('fivethirtyeight'):
    plt.plot('weight', 'height', data=small_boy, marker='.', ms=15, linestyle='-')
    plt.plot('weight', 'height', data=large_boy, marker='.', ms=15, linestyle='-')

plt.savefig('phy.png')