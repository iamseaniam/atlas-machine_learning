#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
"""Also Documented for sissles"""


def line():
    """documented For sissles"""
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))
    x = np.arange(0, 11)

    plt.plot(x, y, color='red')
    plt.axis([0, 10, -50, 1050])
    plt.show()
