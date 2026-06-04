---
name: arbor-tvb-multiscale-simulation
description: |
  Multi-scale brain simulation framework integrating microscopic neural dynamics (Arbor) 
  with macroscopic whole-brain models (The Virtual Brain/TVB). Enables bidirectional 
  real-time co-simulation between detailed spiking neurons and large-scale brain networks.
  
  Use when:
  - Modeling seizures at both neural and whole-brain scales
  - Bridging microscopic neuron dynamics with macroscopic brain region activity
  - Co-simulating detailed neuron populations within large-scale network models
  - Multi-scale neuroscience research requiring both levels of detail
  - Investigating neural disorder propagation mechanisms
  - MPI-based neural simulator integration

metadata:
  arxiv_id: "2505.16861"
  published: "2025-05-22"
  revised: "2025-12-16"
  authors: "Thorsten Hater, Juliette Courson, Han Lu, Sandra Diaz-Pier, Thanos Manos"
  doi: "10.48550/arXiv.2505.16861"
  tags: [multi-scale, neuroscience, brain-simulation, seizure, arbor, tvb, mpi]
  source: "arXiv:2505.16861v2 [q-bio.NC]"
  
license: Complete terms in LICENSE.txt
---

# Arbor-TVB: Multi-Scale Brain Co-Simulation Framework

## Overview

Arbor-TVB is a novel framework that bridges two traditionally isolated scales in computational neuroscience:

1. **Microscopic scale (Arbor)**: Detailed biophysical neuron models, single-compartment to population-level simulations
2. **Macroscopic scale (TVB)**: Whole-brain dynamics based on anatomical connectomes and mean neural activity

This integration enables studying how local neural events (like seizure onset) propagate to whole-brain phenomena.

## Core Innovation

### First Integration of Arbor + TVB

The framework links these simulators for real-time bidirectional interaction:
- **Arbor**: Generates discrete spike events from biologically realistic neurons
- **TVB**: Models continuous neural population activity at regional level
- **Translation layer**: Converts discrete spikes ↔ continuous activity via MPI intercommunicator

### Key Technical Components

#### 1. MPI Intercommunicator Architecture

Real-time bidirectional data exchange:

```
Arbor (Microscopic) ←→ MPI Intercommunicator ←→ TVB (Macroscopic)
     (Spikes)              (Translation)            (Mean Activity)
```

**Translation mechanism:**
- Arbor spikes → TVB mean firing rate per region
- TVB continuous activity → Arbor population input currents

#### 2. Modular Design

Independent model selection per scale:
- Replace any TVB node with Arbor neuron population
- Minimal effort to translate activity across simulators
- Scale-specific model configuration without global constraints

#### 3. Seizure Case Study Implementation

**Mouse Brain Connectome:**
- 38 brain regions from Allen Mouse Brain Connectivity Atlas
- Anatomically informed connectivity weights
- Region-specific Arbor populations embedded in TVB network

**Seizure modeling workflow:**
1. Define seizure-prone region (e.g., hippocampus)
2. Embed detailed Arbor neuron population with seizure-inducing parameters
3. Run co-simulation to observe:
   - Local seizure onset dynamics
   - Propagation pathways to connected regions
   - Whole-brain network response patterns

## Mathematical Framework

### Arbor: Hodgkin-Huxley Style Neurons

Single-compartment neuron dynamics:

```
C_m * dV/dt = -g_L*(V - E_L) - I_ion(V, t) + I_syn(t)
```

Where:
- C_m: Membrane capacitance
- g_L: Leak conductance
- E_L: Leak reversal potential
- I_ion: Ion channel currents (Na, K, etc.)
- I_syn: Synaptic input from connected neurons

### TVB: Neural Mass Models

Regional mean activity model:

```
dS(t)/dt = -S(t)/τ + (1 - S(t)) * H(S(t)) * r_in(t)
```

Where:
- S(t): Mean synaptic activity per region
- τ: Synaptic decay time
- H(S): Sigmoidal response function
- r_in: Input firing rate from connected regions

### Translation: Spike ↔ Mean Activity

**Arbor → TVB:**
```python
mean_firing_rate = spike_count / (population_size * simulation_time)
tvb_region_input = mean_firing_rate * weight_connection
```

**TVB → Arbor:**
```python
input_current = tvb_mean_activity * scaling_factor
for neuron in arbor_population:
    neuron.I_syn += input_current
```

## Implementation Guide

### Step 1: Install Arbor and TVB

```bash
# Arbor (C++ with Python bindings)
pip install arbor

# The Virtual Brain
pip install tvb-library tvb-framework
```

### Step 2: Configure MPI Intercommunicator

```python
import mpi4py.MPI as MPI

class ArborTVBCoupling:
    def __init__(self):
        self.comm = MPI.COMM_WORLD
        self.intercomm = self.comm.Split_type(MPI.COMM_TYPE_SHARED)
        
    def send_spikes_to_tvb(self, spikes, region_id):
        # Count spikes per population
        spike_rate = len(spikes) / self.time_window
        self.intercomm.send(spike_rate, dest=region_id, tag=0)
    
    def receive_activity_from_tvb(self, region_id):
        mean_activity = self.intercomm.recv(source=region_id, tag=1)
        return mean_activity
```

### Step 3: Define Mouse Brain Model

```python
from tvb.datatypes import connectivity

# Load mouse connectome
mouse_connectome = connectivity.Connectivity.from_file(
    "allen_mouse_brain_connectivity.h5"
)

# Define 38 brain regions
regions = [
    "Hippocampus", "Cortex_visual", "Cortex_frontal",
    "Thalamus", "Amygdala", "Striatum", ...
]

# Connectivity matrix
weights = mouse_connectome.weights  # Region-to-region connections
```

### Step 4: Embed Arbor Population in TVB Node

```python
import arbor

# Create Arbor neuron population for hippocampus
hippocampus_cells = arbor.make_cells(
    morphology='pyramidal_cell.swc',
    mechanisms=['hh', 'synapse'],
    n_cells=1000
)

# Configure seizure-inducing parameters
for cell in hippocampus_cells:
    cell.set_parameter('gNa', 150)  # Elevated Na conductance
    cell.set_parameter('gK', 5)     # Reduced K conductance
    
# Embed in TVB model
tvb_model.replace_node('Hippocampus', arbor_population=hippocampus_cells)
```

### Step 5: Run Co-Simulation

```python
# Initialize co-simulator
simulator = ArborTVBCoSimulator(
    arbor_model=arbor_cells,
    tvb_model=tvb_network,
    coupling_interval=10ms
)

# Run simulation with seizure trigger
simulator.inject_current('Hippocampus', 5nA, duration=100ms)
simulator.run(duration=5000ms)

# Analyze propagation
propagation_pathway = simulator.get_seizure_propagation()
# Expected: Hippocampus → Amygdala → Thalamus → Cortex
```

## Seizure Propagation Results

### Observed Patterns

1. **Onset**: Seizure begins in Arbor-embedded region (e.g., hippocampus)
2. **Propagation**: Spreads via anatomical connections to neighboring regions
3. **Whole-brain effect**: Network-level oscillations emerge from local hyperactivity

### Key Insights

- Seizure propagation follows anatomical connectivity weights
- Detailed neuron dynamics affect propagation speed and pattern
- Intervention timing depends on both local and network state

## Advantages over Single-Scale Models

1. **Biological realism**: Detailed neurons + anatomical connectivity
2. **Causal inference**: Trace seizures from origin to whole-brain effect
3. **Intervention testing**: Simulate treatments at appropriate scale
4. **Computational efficiency**: Detailed only where needed, mean-field elsewhere
5. **Modularity**: Swap models per region without global redesign

## Use Cases

| Task | Approach |
|------|----------|
| Study seizure onset mechanisms | Arbor population in focal region |
| Model drug effects on networks | Modify Arbor neuron parameters |
| Test intervention strategies | Simulate stimulation timing |
| Understand propagation pathways | Trace TVB network activity |
| Validate clinical hypotheses | Compare with patient EEG/fMRI |

## Technical Requirements

- **MPI**: For parallel intercommunicator (mpi4py)
- **Arbor**: >=0.6 (Python bindings)
- **TVB**: >=2.0 (framework and library)
- **Hardware**: Multi-core CPU for MPI parallelism
- **Connectome data**: Allen Mouse Brain Atlas (or human connectome)

## Pitfalls

1. **MPI synchronization**: Ensure both simulators run at same timestep
2. **Translation scaling**: Spike rate ↔ mean activity conversion must match population size
3. **Parameter tuning**: Arbor neuron params affect TVB network stability
4. **Computational cost**: Detailed regions expensive; limit number of Arbor nodes
5. **Connectome accuracy**: Anatomical weights critical for propagation patterns

## Connection to Neuroscience

- **Multi-scale modeling**: Addresses long-standing scale integration challenge
- **Seizure research**: Clinical relevance for epilepsy studies
- **Mouse brain**: Translates to human with appropriate connectome
- **Neural mass models**: TVB foundation grounded in mean-field theory
- **Biophysical detail**: Arbor neurons follow Hodgkin-Huxley formalism

## References

```bibtex
@article{hater2025arbor-tvb,
  title={Arbor-TVB: A Novel Multi-Scale Co-Simulation Framework with a Case Study on Neural-Level Seizure Generation and Whole-Brain Propagation},
  author={Hater, Thorsten and Courson, Juliette and Lu, Han and Diaz-Pier, Sandra and Manos, Thanos},
  journal={arXiv preprint arXiv:2505.16861},
  year={2025}
}
```

**Knowledge Graph Integration**: See [references/knowledge-graph-schema.md](references/knowledge-graph-schema.md) for verified kg.db schema and insert patterns.

## Related Tools

- Arbor: https://arbor.readthedocs.io
- The Virtual Brain: https://www.thevirtualbrain.org
- Allen Mouse Brain Connectivity: https://connectivity.brain-map.org

---

*This skill is based on research published on arXiv:2505.16861v2 (May 2025, revised December 2025)*