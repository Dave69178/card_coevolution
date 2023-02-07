import matplotlib.pyplot as plt
import numpy as np

def plot_evolution(host_data, para_data):
    fig, (ax1, ax2) = plt.subplots(1,2, sharey=True)

    host_lines = ax1.plot(host_data)
    ax2.plot(para_data)

    colours = ["red", "red", "black", "black"]
    linestyles = ["dotted", "solid", "dotted", "solid"]
    markers = ["", "d", "", "p"]

    for axis in [ax1, ax2]:
        for line, ls, c, m in zip(axis.get_lines(), linestyles, colours, markers):
            line.set_linestyle(ls)
            line.set_color(c)
            line.set_marker(m)

    ax1.set_title("Host")
    ax2.set_title("Parasite")
    fig.supxlabel("Timestep")
    ax1.set_ylabel("Count")
    ax1.legend(host_lines, ("H", "D", "C", "S"))
    ax1.set_ylim(0, 13)
    ax2.set_ylim(0, 13)

    plt.show()


def plot_suit_comparisons(host_data, para_data):
    suit_name = {
        0: "hearts",
        1: "diamonds",
        2: "spades",
        3: "clubs"
    }

    fig, ax = plt.subplots(2,2)

    row = 0
    col = 0
    for suit in range(4):
        ax[row, col].plot(np.array(host_data)[:, suit].tolist())
        ax[row, col].plot(np.array(para_data)[:, suit].tolist())
        if col == 0:
            col += 1
        elif col == 1:
            row += 1
            col = 0

    colours = ["green", "blue"]
    linestyles = ["solid", "solid"]

    suit = 0
    for axis in ax.reshape(-1):
        axis.set_title("Evolution of " + str(suit_name[suit]))
        axis.set_ylim(0, 13)
        for line, ls, c in zip(axis.get_lines(), linestyles, colours):
            line.set_linestyle(ls)
            line.set_color(c)
        suit += 1

    fig.supxlabel("Timestep")
    fig.supylabel("Count")
    fig.legend(["Host", "Parasite"])

    plt.show()