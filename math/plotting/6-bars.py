#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
"""documentation"""


def bars():
    """documentation"""
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4,3))
    plt.figure(figsize=(6.4, 4.8))

    # Define colors, fruits, and people
    colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
    fruits = ['apples', 'bananas', 'oranges', 'peaches']
    people = ['Farrah', 'Fred', 'Felicia']

    # Plot stacked bars
    bottom = np.zeros(len(people))
    for i in range(len(fruit)):
        plt.bar(
            people,
            fruit[i],
            bottom=bottom,
            color=colors[i],
            label=fruits[i],
            width=0.5
        )
        bottom += fruit[i]

    # Legend, label, title, and ticks
    plt.legend()
    plt.ylabel('Quantity of Fruit')
    plt.title('Number of Fruit per Person')
    plt.yticks(np.arange(0, 81, 10))

    plt.show()
