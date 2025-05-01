from pyNN.random import RandomDistribution, NumpyRNG
from pyNN.utility.plotting import Figure, Panel
import pyNN.nest as sim

# simulation setup
sim.setup(timestep=0.1)  # 0.1ms resolution
random_num_generator = NumpyRNG(seed=69)

# configuring neuron model
cell_parameters = {
    'v_rest': RandomDistribution('normal', (-65.0, 1.0), rng),
    'v_thresh': RandomDistribution('normal', (-55.0, 1.0), rng),
    'v_reset': -65.0,
    'tau_refrac': 1.0,    # ms
    'tau_m': 10.0,        # ms
    'cm': 1.0,            # nF
    'i_offset': 1.1       # nA
}

# 100 integrate & fire neurons
population = sim.Population(100, sim.IF_curr_exp(**cell_parameters))
population.record('v')  # record membrane voltage

sim.run(100.0)      # run simulation for 100 ms

# data plotting!
data = population.get_data().segments[0]
Figure(
    Panel(data.filter(name='v')[0][:, 0],  # voltage of first neuron
          xlabel="Time (ms)", ylabel="Membrane potential (mV)"),
    title="PyNN simulation results",
    annotations=f"Simulated with {sim.__name__}"
).show()

sim.end()