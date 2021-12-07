#!/usr/bin/env python3

from mpl_toolkits.axes_grid1 import host_subplot
import matplotlib.pyplot as plt
import numpy as np

# one row, one column, plot number 1
host = host_subplot(111)
para = host.twinx()

host.set_xlabel("Months")
host.set_ylabel("Weight")
para.set_ylabel("Height")
para.set_yticks([10, 20, 30, 40, 50, 60, 70])

months = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
weight_s = np.array([3.5, 4.1, 4.7, 5.3, 5.9, 6.4, 6.9, 7.2, 7.6, 7.9, 8.1])
height_s = np.array([52.9, 55.8, 58.3, 60.5, 62.4, 64.1, 65.7, 67.0, 68.3, 69.6, 70.7])

with plt.style.context('fivethirtyeight'):
    p1, = host.plot(months, weight_s, label="Weight")
    p2, = para.plot(months, height_s, label="Height")
    legd = plt.legend()

plt.subplots_adjust(hspace=1.2)

host.yaxis.get_label().set_color(p1.get_color())
legd.texts[0].set_color(p1.get_color())

para.yaxis.get_label().set_color(p2.get_color())
legd.texts[1].set_color(p2.get_color())

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

plt.savefig('phy.png')
