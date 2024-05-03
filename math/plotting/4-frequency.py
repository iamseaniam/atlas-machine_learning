#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
"""Documentation"""



def frequency():
    """Documentation"""
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    # Plotting histogram
    plt.hist(student_grades, bins=np.arange(0, 101, 10), edgecolor='black')

    # Labels and titles
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.title("Project A")

    # Display plot
    plt.show()
