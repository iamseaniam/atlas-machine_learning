#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
"""Documentation that does not work at all"""


def all_in_one():
    """STILL DOES NOT WORK"""
    # 0-line.py
    y0 = np.arange(0, 11) ** 3
    x0 = np.arange(0, 11)

    # 1-scatter.py
    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
    y1 += 180

    # 2-change_scale.py
    x2 = np.arange(0, 28651, 5730)
    r2 = np.log(0.5)
    t2 = 5730
    y2 = np.exp((r2 / t2) * x2)

    # 3-two.py
    x3 = np.arange(0, 21000, 1000)
    r3 = np.log(0.5)
    t31 = 5730
    t32 = 1600
    y31 = np.exp((r3 / t31) * x3)
    y32 = np.exp((r3 / t32) * x3)

    # 4-frequency
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)

    # setting subplots and other settings
    fig, axs = plt.subplots(3, 2)
    fig.suptitle('All in One')

    # 0-line.py
    axs[0, 0].plot(x0, y0, color='red')
    axs[0, 0].axis([0, 10, -50, 1050])

    # 1-scatter.py
    axs[0, 1].plot(x1, y1, 'o', color="magenta")
    axs[0, 1].set_xlabel("Height (in)", fontsize="x-small")
    axs[0, 1].set_ylabel("Weight (lbs)", fontsize="x-small")
    axs[0, 1].set_title("Men's Height vs Weight", fontsize="x-small")

    # 2-change_scale.py
    axs[1, 0].plot(x2, y2)
    axs[1, 0].set_xlabel("Time (years)", fontsize="x-small")
    axs[1, 0].set_ylabel("Fraction Remaining", fontsize="x-small")
    axs[1, 0].set_title("Exponential Decay of C-14", fontsize="x-small")
    axs[1, 0].set_yscale("log")
    axs[1, 0].set_xlim(0, 28650)

    # 3-two.py
    axs[1, 1].set_xlabel("Time (years)", fontsize="x-small")
    axs[1, 1].set_ylabel("Fraction Remaining", fontsize="x-small")
    axs[1, 1].set_title("Exponential Decay of Radioactive Elements", fontsize="x-small")
    axs[1, 1].set_xlim(0, 20000)
    axs[1, 1].set_ylim(0, 1)
    axs[1, 1].plot(x3, y31, color="red", linestyle='dashed', label="C-14")
    axs[1, 1].plot(x3, y32, label="Ra-226", color="green")
    axs[1, 1].legend()

    # 4-frequency.py
    bins = np.arange(0, 101, 10)
    axs[2, 0].set_xlim(0, 100)
    axs[2, 0].set_xticks(np.arange(0, 101, 10))
    axs[2, 0].set_ylim(0, 30)
    axs[2, 0].hist(student_grades, bins=bins, edgecolor='black')
    axs[2, 0].set_xlabel('Grades', fontsize="x-small")
    axs[2, 0].set_ylabel('Number of Students', fontsize="x-small")
    axs[2, 0].set_title('Project A', fontsize="x-small")

    # Showing all plots
    plt.tight_layout()
    plt.show()
