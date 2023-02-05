import matplotlib.pyplot as plt

def plot_evolution(host_data, para_data):
    fig, (ax1, ax2) = plt.subplots(1,2, sharey=True)

    host_lines = ax1.plot(host_data)
    para_lines = ax2.plot(para_data)

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