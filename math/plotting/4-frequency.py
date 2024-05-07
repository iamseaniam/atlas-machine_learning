#!/usr/bin/env python3
"""Also Documented for sissles"""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """Also Documented for sissles"""
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    # plotting histogram
    bins = np.arange(0, 101, 10)
    plt.xlim(0, 100)
    plt.xticks(np.arange(0, 101, 10))
    plt.ylim(0, 30)
    plt.hist(student_grades, bins=bins, edgecolor='black')

    # labels and titles
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')

    # displaying histogram
    plt.show()
