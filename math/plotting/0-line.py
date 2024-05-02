#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def line():

    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))

    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y = x*2

    plt.plot(x, y)
    plt.show()
