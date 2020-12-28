import matplotlib.pyplot as plt
import numpy as np


def plot_example(path):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

    ax1.set_title("1st subplot")
    ax1.set_ylabel("y1")
    ax1.set_xlabel("x1")
    ax1.plot(
        range(1, 101, 10),
        range(101, 201, 10),
        color="cyan",
        marker="o",
        alpha=0.3,
        label="plot",
    )
    ax1.scatter(
        range(101, 1, -2),
        range(81, 181, 2),
        color="orange",
        marker="*",
        label="scatter",
    )
    ax1.legend()
    ax1.grid()

    ax2.set_title("2nd subplot")
    ax2.set_ylabel("y2")
    ax2.set_xlabel("x2")
    ax2.hist(np.random.rand(100), label="hist", edgecolor="red")
    ax2.legend()

    fig.savefig(path)
