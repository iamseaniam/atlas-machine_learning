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
    fig = plt.figure()
    fig.subplots_adjust(left=0.2, wspace=0.6)
    fig.suptitle('All in One')



    # 0-line.py
    ax0 = plt.subplot2grid((3,2), (0,0))
    ax0.plot(x0, y0, color='red')
    ax0.axis([0, 10, -50, 1050])
    ax0.set_ylim(0, 1000)



    # 1-scatter.py

    # plotting scatter graph
    ax1 = plt.subplot2grid((3,2), (0,1))
    s = [5]
    ax1.scatter(x1, y1, s, color="magenta")

    # Lables and titles for 1
    ax1.set_xlabel("Height (in)", fontsize="x-small")
    ax1.set_ylabel("Weight (lbs)", fontsize="x-small")
    ax1.set_title("Men's Height vs Weight", fontsize="x-small")



    # 2-change_scale.py
    
    # plotting line graph
    ax2 = plt.subplot2grid((3,2), (1,0))
    ax2.plot(x2, y2)
    ax2.set_yscale("log")
    ax2.set_xlim(0, 28650)

    # labels and titles for 2
    ax2.set_xlabel("Time (years)", fontsize="x-small")
    ax2.set_ylabel("Fraction Remaining", fontsize="x-small")
    ax2.set_title("Exponential Decay of C-14", fontsize="x-small")



    # 3-two.py

    # plotting multi line graph
    ax3 = plt.subplot2grid((3,2), (1,1))
    ax3.set_xlim(0, 20000)
    ax3.set_ylim(0, 1)
    ax3.plot(x3, y31, color="red", linestyle='dashed', label="C-14")
    ax3.plot(x3, y32, label="Ra-226", color="green")

    # lables, title and legend for 3
    ax3.set_xlabel("Time (years)", fontsize="x-small")
    ax3.set_ylabel("Fraction Remaining", fontsize="x-small")
    ax3.set_title("Exponential Decay of Radioactive Elements", fontsize="x-small")
    ax3.legend(fontsize="x-small")



    # 4-frequency.py

    #plotting histogram graph
    ax4 = plt.subplot2grid((3,2), (2,0), colspan=2)
    bins = np.arange(0, 101, 10)
    ax4.set_xlim(0, 100)
    ax4.set_xticks(np.arange(0, 101, 10))
    ax4.set_ylim(0, 30)
    ax4.hist(student_grades, bins=bins, edgecolor='black')

    #lables and title for 4
    ax4.set_xlabel('Grades', fontsize="x-small")
    ax4.set_ylabel('Number of Students', fontsize="x-small")
    ax4.set_title('Project A', fontsize="x-small")



    # Showing all plots
    plt.tight_layout()
    plt.show()
