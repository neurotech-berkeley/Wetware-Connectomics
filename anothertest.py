# import pyNN.nest as sim

# # Set up simulation
# sim.setup(timestep=0.1)

# # Define neuron model
# cell_params = {
#     'cm': 0.25, 'i_offset': 0.1,
#     'tau_m': 10.0, 'tau_refrac': 2.0,
#     'tau_syn_E': 2.5, 'tau_syn_I': 2.5,
#     'v_reset': -70.0, 'v_rest': -65.0,
#     'v_thresh': -50.0
# }

# # === Define Segment Template ===
# def create_segment(segment_id):
#     SN = sim.Population(5, sim.IF_curr_exp(**cell_params), label=f"SN_{segment_id}")
#     IN_exc = sim.Population(15, sim.IF_curr_exp(**cell_params), label=f"IN_exc_{segment_id}")
#     IN_inh = sim.Population(5, sim.IF_curr_exp(**cell_params), label=f"IN_inh_{segment_id}")
#     MN = sim.Population(10, sim.IF_curr_exp(**cell_params), label=f"MN_{segment_id}")

#     # Local connections (simplified probabilities)
#     sim.Projection(SN, IN_exc, sim.FixedProbabilityConnector(0.5), sim.StaticSynapse(weight=0.05))
#     sim.Projection(SN, IN_inh, sim.FixedProbabilityConnector(0.3), sim.StaticSynapse(weight=0.03))
#     sim.Projection(IN_exc, MN, sim.FixedProbabilityConnector(0.4), sim.StaticSynapse(weight=0.1))
#     sim.Projection(IN_inh, MN, sim.FixedProbabilityConnector(0.4), sim.StaticSynapse(weight=-0.1))

#     return {'SN': SN, 'IN_exc': IN_exc, 'IN_inh': IN_inh, 'MN': MN}

# # === Create Segments ===
# segments = [create_segment(i) for i in range(3)]  # A1 to A3

# # === Intersegmental connections ===
# for i in range(2):
#     sim.Projection(segments[i]['IN_exc'], segments[i+1]['IN_exc'],
#                    sim.FixedProbabilityConnector(0.3),
#                    sim.StaticSynapse(weight=0.05, delay=1.0))
#     sim.Projection(segments[i]['IN_inh'], segments[i+1]['MN'],
#                    sim.FixedProbabilityConnector(0.2),
#                    sim.StaticSynapse(weight=-0.07, delay=1.5))

# # === Stimulus ===
# stim = sim.Population(1, sim.SpikeSourceArray(spike_times=[5.0, 10.0, 20.0]), label="Stim")
# sim.Projection(stim, segments[0]['SN'], sim.AllToAllConnector(), sim.StaticSynapse(weight=0.1))

# # === Record Activity ===
# for seg in segments:
#     seg['MN'].record('spikes')

# # === Run Simulation ===
# sim.run(50.0)

# # === Get Data ===
# for i, seg in enumerate(segments):
#     data = seg['MN'].get_data().segments[0].spiketrains
#     print(f"Segment {i} MN activity:", data)

# sim.end()




# import pyNN.nest as sim

# # Set up simulation
# sim.setup(timestep=0.1)

# # Define neuron model
# cell_params = {
#     'cm': 0.25, 'i_offset': 0.1,
#     'tau_m': 10.0, 'tau_refrac': 2.0,
#     'tau_syn_E': 2.5, 'tau_syn_I': 2.5,
#     'v_reset': -70.0, 'v_rest': -65.0,
#     'v_thresh': -50.0
# }

# # === Define Segment Template ===
# def create_segment(segment_id):
#     SN = sim.Population(5, sim.IF_curr_exp(**cell_params), label=f"SN_{segment_id}")
#     IN_exc = sim.Population(15, sim.IF_curr_exp(**cell_params), label=f"IN_exc_{segment_id}")
#     IN_inh = sim.Population(5, sim.IF_curr_exp(**cell_params), label=f"IN_inh_{segment_id}")
#     MN = sim.Population(10, sim.IF_curr_exp(**cell_params), label=f"MN_{segment_id}")

#     # Local connections (with increased weights)
#     sim.Projection(SN, IN_exc, sim.FixedProbabilityConnector(0.5), sim.StaticSynapse(weight=0.1))  # Increased from 0.05
#     sim.Projection(SN, IN_inh, sim.FixedProbabilityConnector(0.3), sim.StaticSynapse(weight=0.03))
#     sim.Projection(IN_exc, MN, sim.FixedProbabilityConnector(0.4), sim.StaticSynapse(weight=0.2))  # Increased from 0.1
#     sim.Projection(IN_inh, MN, sim.FixedProbabilityConnector(0.4), sim.StaticSynapse(weight=-0.1))
    
#     # Add recurrent excitation to help sustain activity
#     sim.Projection(IN_exc, IN_exc, sim.FixedProbabilityConnector(0.2), sim.StaticSynapse(weight=0.05))

#     return {'SN': SN, 'IN_exc': IN_exc, 'IN_inh': IN_inh, 'MN': MN}

# # === Create Segments ===
# segments = [create_segment(i) for i in range(3)]  # A1 to A3

# # === Intersegmental connections ===
# for i in range(2):
#     sim.Projection(segments[i]['IN_exc'], segments[i+1]['IN_exc'],
#                    sim.FixedProbabilityConnector(0.3),
#                    sim.StaticSynapse(weight=0.1, delay=1.0))  # Increased from 0.05
#     sim.Projection(segments[i]['IN_inh'], segments[i+1]['MN'],
#                    sim.FixedProbabilityConnector(0.2),
#                    sim.StaticSynapse(weight=-0.07, delay=1.5))

# # === Add background noise to increase baseline activity ===
# for seg in segments:
#     noise = sim.Population(5, sim.SpikeSourcePoisson(rate=15.0))
#     sim.Projection(noise, seg['SN'], sim.AllToAllConnector(), 
#                   sim.StaticSynapse(weight=0.15))

# # === Stimulus with more spikes ===
# stim = sim.Population(1, sim.SpikeSourceArray(
#     spike_times=[5.0, 7.0, 9.0, 11.0, 13.0, 15.0, 20.0, 25.0, 30.0, 35.0]), 
#     label="Stim")
# sim.Projection(stim, segments[0]['SN'], sim.AllToAllConnector(), 
#               sim.StaticSynapse(weight=0.5))  # Increased from 0.1

# # === Record Activity ===
# for seg in segments:
#     seg['MN'].record('spikes')
#     seg['SN'].record('spikes')  # Also record sensory neuron activity
#     seg['IN_exc'].record('spikes')  # Record excitatory interneuron activity

# # === Run Simulation ===
# sim.run(100.0)  # Increased from 50.0

# # === Get Data and Print Summary ===
# for i, seg in enumerate(segments):
#     mn_data = seg['MN'].get_data().segments[0].spiketrains
#     sn_data = seg['SN'].get_data().segments[0].spiketrains
#     in_data = seg['IN_exc'].get_data().segments[0].spiketrains
    
#     # Count total spikes
#     mn_spike_count = sum(len(st) for st in mn_data)
#     sn_spike_count = sum(len(st) for st in sn_data)
#     in_spike_count = sum(len(st) for st in in_data)
    
#     print(f"Segment {i} activity:")
#     print(f"  - SN: {sn_spike_count} spikes from {len(sn_data)} neurons")
#     print(f"  - IN_exc: {in_spike_count} spikes from {len(in_data)} neurons")
#     print(f"  - MN: {mn_spike_count} spikes from {len(mn_data)} neurons")

# # === Optional: Plot raster if matplotlib is available ===
# try:
#     import matplotlib.pyplot as plt
    
#     plt.figure(figsize=(12, 8))
    
#     # Plot spikes for each segment with different colors
#     colors = ['red', 'blue', 'green']
#     markers = ['o', 's', '^']
    
#     for i, seg in enumerate(segments):
#         # Get spike data
#         mn_data = seg['MN'].get_data().segments[0].spiketrains
        
#         # Plot each neuron's spikes
#         for j, spiketrain in enumerate(mn_data):
#             if len(spiketrain) > 0:  # Only plot if there are spikes
#                 plt.plot(spiketrain, 
#                          [i*10 + j] * len(spiketrain), 
#                          markers[i], 
#                          color=colors[i],
#                          markersize=4,
#                          label=f"Segment {i}" if j == 0 else "")
    
#     plt.xlabel('Time (ms)')
#     plt.ylabel('Neuron Index')
#     plt.title('Motor Neuron Activity Across Segments')
    
#     # Remove duplicate labels
#     handles, labels = plt.gca().get_legend_handles_labels()
#     by_label = dict(zip(labels, handles))
#     plt.legend(by_label.values(), by_label.keys(), loc='best')
    
#     plt.tight_layout()
#     plt.savefig('segmental_activity.png')
#     print("Raster plot saved as 'segmental_activity.png'")
# except ImportError:
#     print("Matplotlib not available for plotting. Install with 'pip install matplotlib'")

# sim.end()


"""Basic PyNN simulation with random neuron parameters"""
from pyNN.random import RandomDistribution, NumpyRNG
from pyNN.utility.plotting import Figure, Panel
import pyNN.nest as sim  # Can replace 'nest' with 'neuron' or 'brian2'

# Simulation setup
sim.setup(timestep=0.1)  # 0.1ms resolution
rng = NumpyRNG(seed=42)  # Random number generator

# Neuron model configuration
cell_parameters = {
    'v_rest': RandomDistribution('normal', (-65.0, 1.0), rng),
    'v_thresh': RandomDistribution('normal', (-55.0, 1.0), rng),
    'v_reset': -65.0,
    'tau_refrac': 1.0,    # ms
    'tau_m': 10.0,        # ms
    'cm': 1.0,            # nF
    'i_offset': 1.1       # nA
}

# Create 100 integrate-and-fire neurons
population = sim.Population(100, sim.IF_curr_exp(**cell_parameters))
population.record('v')  # Record membrane voltage

# Run simulation for 100ms
sim.run(100.0)

# Retrieve and plot data
data = population.get_data().segments[0]
Figure(
    Panel(data.filter(name='v')[0][:, 0],  # First neuron's voltage
          xlabel="Time (ms)", ylabel="Membrane potential (mV)"),
    title="PyNN simulation results",
    annotations=f"Simulated with {sim.__name__}"
).show()

sim.end()  # Cleanup