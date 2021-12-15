#!/usr/bin/env python3

from mpl_toolkits.axes_grid1 import host_subplot
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import numpy as np

figure(figsize=(19, 14), dpi=80)

# one row, one column, plot number 1
host = host_subplot(111)
para = host.twinx()

font = {
    'weight': 'bold',
    'size': 18,
}

host.set_xlabel("Months", fontdict=font)
host.set_ylabel("Weight (kg)", fontdict=font)
para.set_ylabel("Height (cm)", fontdict=font)

months = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

weight_s = np.array([3.5, 4.1, 4.7, 5.3, 5.9, 6.4, 6.9, 7.2, 7.6, 7.9, 8.1])
weight_l = np.array([6.8, 7.7, 8.5, 9.2, 9.8, 10.3, 10.8, 11.3, 11.7, 12.0, 12.4])

height_s = np.array([52.9, 55.8, 58.3, 60.5, 62.4, 64.1, 65.7, 67.0, 68.3, 69.6, 70.7])
height_l = np.array([63.2, 66.4, 69.1, 71.3, 73.2, 74.8, 76.3, 77.3, 78.9, 80.2, 81.5])

months_anji = np.array([2])
weight_anji = np.array([5.1])
height_anji = np.array([59.0])

with plt.style.context('fivethirtyeight'):
    pw_s, = host.plot(months, weight_s, color="#ff8c00", linestyle=":")
    pw_l, = host.plot(months, weight_l, color="#ff8c00", linestyle=":")
    pw_anji, = host.plot(months_anji, weight_anji, color="#ff8c00", marker="o", ms=10, label="Weight")

    ph_s, = para.plot(months, height_s, color="#436eee", linestyle=":")
    ph_l, = para.plot(months, height_l, color="#436eee", linestyle=":")
    ph_anji, = para.plot(months_anji, height_anji, color="#436eee", marker="o", ms=10, label="Height")

    for m, w in zip(months_anji, weight_anji):
        host.annotate(f"{w:.1f}", (m, w), textcoords="offset points", xytext=(0, 10), ha="center")

    for m, h in zip(months_anji, height_anji):
        para.annotate(f"{h:.1f}", (m, h), textcoords="offset points", xytext=(0, 10), ha="center")

    legd = plt.legend(loc="upper left")

host.yaxis.get_label().set_color(pw_s.get_color())
host.set_xticks([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
host.set_yticks([3., 3.5, 4., 4.5, 5., 5.5, 6., 6.5, 7., 7.5, 8., 8.5, 9., 9.5,
                 10., 10.5, 11., 11.5, 12., 12.5, 13., 13.5, 14., 14.5, 15., 15.5, 16.])
legd.texts[0].set_color(pw_s.get_color())

para.yaxis.get_label().set_color(ph_s.get_color())
para.set_yticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])
legd.texts[1].set_color(ph_s.get_color())

plt.title("Anji's Physical Growth", fontdict={'fontsize': 24, 'fontweight': 'bold'})

plt.savefig('phy.png')
