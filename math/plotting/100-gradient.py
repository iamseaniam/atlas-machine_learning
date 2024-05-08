#!/usr/bin/env python3
"""Documentation"""
import numpy as np
import matplotlib.pyplot as plt


def gradient():
    """Documentation"""
    np.random.seed(5)

    x = np.random.randn(2000) * 10
    y = np.random.randn(2000) * 10
    z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))

    scatter = plt.scatter(x, y, c=z, cmap='viridis')

    # Create a colorbar
    plt.colorbar(scatter, label="elevation (m)", orientation="vertical")

    # labels and title
    plt.xlabel("x coordinate (m)")
    plt.ylabel("y coordinate (m)")
    plt.title("Mountain Elevation")

    plt.show()
