from coevolution import Evolution
import numpy as np
from plot_data import plot_evolution

def single_run(num_steps, host_start=None, para_start=None):
    evo = Evolution()
    host_data = []
    para_data = []
    for i in evo.run_evolution(num_steps, host_starting_hand=host_start, para_starting_hand=para_start):
        host_data.append(i[0][:])
        para_data.append(i[1][:])
    return host_data, para_data


def single_run_and_plot(num_steps, host_start=None, para_start=None):
    host_data, para_data = single_run(num_steps, host_start=host_start, para_start=para_start)
    plot_evolution(host_data, para_data)


def repeat_and_plot_avg(num_steps, num_repeats, host_start=None, para_start=None):
    host_avg_data = np.array([[0,0,0,0] for i in range(num_steps + 1)])
    para_avg_data = np.array([[0,0,0,0] for i in range(num_steps + 1)])
    for i in range(num_repeats):
        host_data, para_data = single_run(num_steps, host_start=host_start, para_start=para_start)
        host_avg_data = np.add(host_avg_data, host_data)
        para_avg_data = np.add(para_avg_data, para_data)
    plot_evolution(host_avg_data / num_repeats, para_avg_data / num_repeats)

# Uncomment code lines for simulation examples:

# Perform single run for a given number of timesteps - host and parasite start with random hands
single_run_and_plot(10)

# Perform single run for given number of timesteps - host and parasite start with given hands
#single_run_and_plot(10, host_start=[12,0,0,0], para_start=[3,3,3,3])

# Perform 100 repeats for 10 timesteps each - random starts
#repeat_and_plot_avg(10, 100)

# Perform 100 repeats for 1000 timesteps each - host has defined starting hand
#repeat_and_plot_avg(1000, 100, host_start=[12,0,0,0])