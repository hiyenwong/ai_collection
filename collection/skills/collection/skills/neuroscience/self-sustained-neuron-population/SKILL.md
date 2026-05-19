---
name: self-sustained-neuron-population
version: v1.0.0
last_updated: 2026-04-17
description: "Modeling self-sustained neural activity in recurrent networks without external stimulus. Hodgkin-Huxley neurons with STDP maintain autonomous sparse firing after brief initialization. Applicable to neuromorphic computing, neural autonomy, and brain simulation. 触发词: self-sustained activity, autonomous neural network, Hodgkin-Huxley, STDP, sparse firing"
---

# Self-Sustained Neuron Population

## Description

Self-sustained neural activity is the ability of neural networks to maintain autonomous firing patterns without ongoing external input. This skill implements a recurrent network of Hodgkin-Huxley neurons with spike-timing-dependent plasticity (STDP) and intrinsic stochasticity that can sustain sparse, irregular activity after brief transient stimulation.

Based on: Karakaş et al., "Modeling of Self-sustained Neuron Population without External Stimulus", arXiv:2604.13719 (2026)

## Key Components

### Network Architecture
- **Neuron Model**: Hodgkin-Huxley (biophysically grounded)
- **Network Size**: 200 neurons (160 excitatory, 40 inhibitory)
- **Connectivity**: 80% connection probability
- **Plasticity**: Excitatory and inhibitory STDP
- **Stochasticity**: Probabilistic vesicle release and synapse formation

### Dynamics Characteristics
- **Sparse Firing**: 67% of neurons fire <1 Hz
- **Mean Rate**: ~1.13 Hz population average
- **Irregularity**: Fano factors near 1-2
- **Self-organization**: Spontaneous pattern reorganization over time

## Activation Keywords

- self-sustained activity
- autonomous neural network
- Hodgkin-Huxley model
- STDP self-organization
- sparse firing regime
- 自持续神经活动
- 自主神经网络
- 神经稳定性

## Tools Used

- `python`: Simulation with Brian2 or NEURON
- `numpy`: Numerical computations
- `matplotlib`: Raster plots and rate analysis

## Workflow

### Step 1: Initialize Network

```python
import numpy as np
from brian2 import *

# Network parameters
N_exc = 160  # Excitatory neurons
N_inh = 40   # Inhibitory neurons
N = N_exc + N_inh
connection_prob = 0.8

# Hodgkin-Huxley equations
# (Simplified for illustration - use full HH for production)
eqs = '''
dv/dt = (I_ext + I_syn - I_Na - I_K - I_L) / C_m : volt
I_Na = g_Na * m**3 * h * (v - E_Na) : amp
I_K = g_K * n**4 * (v - E_K) : amp
I_L = g_L * (v - E_L) : amp
'''
```

### Step 2: Configure STDP Rules

```python
# Excitatory STDP
tau_pre_exc = 20*ms
tau_post_exc = 20*ms
Apost_exc = -0.05  # Depression
Apre_exc = 0.05    # Potentiation

# Inhibitory STDP
tau_pre_inh = 10*ms
tau_post_inh = 10*ms
Apost_inh = 0.02   # Inverse of excitatory
Apre_inh = -0.02
```

### Step 3: Add Stochasticity

```python
# Probabilistic vesicle release
release_prob = 0.8

# Probabilistic synapse formation
synapse_formation_prob = 0.9

# Receptor variability (Gaussian noise on conductances)
g_noise_std = 0.1  # 10% variability
```

### Step 4: Apply Initialization Stimulus

```python
# Brief 200ms stimulation to 30 excitatory neurons
stimulus_duration = 200*ms
stimulus_targets = np.random.choice(N_exc, 30, replace=False)
I_stim = 1*nA  # Stimulation current
```

### Step 5: Run Autonomous Simulation

```python
# No external input after initialization
run(1800*second, report='text')

# Monitor firing rates and patterns
# Expected: sustained sparse, irregular activity
```

### Step 6: Analyze Activity Patterns

```python
# Calculate firing rates
firing_rates = spike_monitor.count / (1800*second)
sparse_neurons = np.sum(firing_rates < 1*Hz) / N  # Should be ~67%

# Calculate Fano factors (irregularity measure)
def fano_factor(spike_times, window=100*ms):
    counts = np.histogram(spike_times, bins=np.arange(0, 1800, 0.1))[0]
    return np.var(counts) / np.mean(counts)

# Expected Fano factors: 1-2
```

## Key Findings

1. **Sustained Activity**: Network maintains firing for 1800+ seconds without external drive
2. **Sparse Regime**: Most neurons (67%) fire below 1 Hz
3. **Irregular Timing**: Fano factors near 1-2 indicate cortical-like irregularity
4. **Pattern Reorganization**: Spontaneous qualitative changes in collective firing over time
5. **STDP Balance**: Plasticity maintains stable self-organized state

## Implementation Notes

### Critical Parameters
- **STDP Time Constants**: Balance potentiation and depression windows
- **E/I Ratio**: 4:1 excitatory to inhibitory ratio
- **Connectivity**: High connection probability (80%) enables recurrence
- **Initialization**: Brief stimulation of subset (30/160) of excitatory neurons

### Common Issues
- **Silent Networks**: Increase initialization strength or connectivity
- **Runaway Excitation**: Strengthen inhibitory STDP or increase I/E ratio
- **Rate Collapse**: Ensure receptor variability and stochastic release

## Applications

1. **Neuromorphic Computing**: Energy-efficient autonomous processing
2. **Brain Simulation**: Understanding resting-state dynamics
3. **Neural Prosthetics**: Self-sustained neural interfaces
4. **Theoretical Neuroscience**: Study of neural criticality

## References

- Karakaş, İ.E., Özel, Ö., Ulusoy, İ., & Koçak, O.M. (2026). Modeling of Self-sustained Neuron Population without External Stimulus. arXiv:2604.13719.
- Hodgkin, A.L. & Huxley, A.F. (1952). A quantitative description of membrane current.
- Markram, H. et al. (1997). Regulation of synaptic efficacy by coincidence of postsynaptic APs and EPSPs.

## Code Example

```python
"""
Self-Sustained Neural Activity Simulation
Based on Karakaş et al. 2026
"""

from brian2 import *
import numpy as np

# Parameters
defaultclock.dt = 0.1*ms

# Neuron model
neuron_eqs = '''
dv/dt = (I_syn + I_noise - I_Na - I_K - I_L) / C_m : volt
I_Na = g_Na*m**3*h*(v - E_Na) : amp
I_K = g_K*n**4*(v - E_K) : amp
I_L = g_L*(v - E_L) : amp
dm/dt = alpha_m*(1-m) - beta_m*m : 1
dh/dt = alpha_h*(1-h) - beta_h*h : 1
dn/dt = alpha_n*(1-n) - beta_n*n : 1
I_syn : amp
I_noise : amp
'''

# STDP equations
stdp_eqs = '''
w : 1
dapre/dt = -apre/tau_pre : 1 (event-driven)
dapost/dt = -apost/tau_post : 1 (event-driven)
'''

stdp_on_pre = '''
v_post += w * release_prob
apre += Apre
w = clip(w + apost, 0, w_max)
'''

stdp_on_post = '''
apost += Apost
w = clip(w + apre, 0, w_max)
'''

# Run simulation
print("Initializing self-sustained network...")
# (Full implementation requires Brian2 setup)
```
