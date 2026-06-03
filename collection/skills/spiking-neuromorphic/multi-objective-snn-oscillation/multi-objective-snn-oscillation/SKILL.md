---
name: multi-objective-snn-oscillation
description: "Multi-objective genetic algorithm (NSGA-III) optimisation of recurrent spiking neural networks (RSNNs) to match observed neural firing rates and oscillation frequencies simultaneously, including brain organoid data."
triggers:
  - SNN oscillation fitting
  - RSNN optimisation
  - neural oscillation frequencies
  - NSGA-III neural network
  - brain organoid SNN
  - Izhikevich RSNN
  - multi-objective SNN
  - decision-making SNN
  - spiking network connectivity optimisation
  - fitting neural data SNN
category: neuroscience
tags:
  - SNN
  - RSNN
  - NSGA-III
  - oscillations
  - brain-organoid
  - multi-objective-optimization
  - Izhikevich-neurons
  - decision-making
  - neural-fitting
source: "arXiv:2605.25224"
authors: ["Divyansh Sethi", "Muhammad Faraz", "KongFatt Wong-Lin"]
---

# Multi-Objective SNN Optimisation: Oscillatory Dynamics & Firing Rates

## Overview

This skill encapsulates the methodology from arXiv:2605.25224 for **simultaneously optimising recurrent spiking neural networks (RSNNs) to match multiple neural observables** — both **firing rates** and **oscillation frequencies** — using **NSGA-III multi-objective genetic algorithms**.

**Key contribution**: Previous SNN fitting focused on firing rates alone. This work adds **oscillation frequency matching**, which is biologically crucial (gamma, theta, beta bands), validated on both simulated RSNNs and real **brain organoid** data.

## Core Architecture

### Izhikevich Neuron Model
```python
# Izhikevich neuron dynamics (2D ODE, biologically realistic)
# dv/dt = 0.04*v^2 + 5*v + 140 - u + I
# du/dt = a*(b*v - u)
# if v >= 30: v = c, u = u + d

NEURON_PARAMS = {
    'excitatory': {'a': 0.02, 'b': 0.2, 'c': -65.0, 'd': 8.0},
    'inhibitory': {'a': 0.1,  'b': 0.2, 'c': -65.0, 'd': 2.0}
}
```

### Network Architecture (Cortical E/I)
- **Excitatory neurons**: 80% of population (cortical pyramidal cells)
- **Inhibitory neurons**: 20% of population (interneurons)
- **Recurrent connectivity**: parameterized by weight matrices W_EE, W_EI, W_IE, W_II
- **Synaptic delays**: tau_AMPA, tau_GABA parameters

## Optimisation Methodology (NSGA-III)

### Objective Functions
```python
def fitness_rsnn(connectivity_params, target_firing_rates, target_oscillations):
    """
    Multi-objective fitness for RSNN parameter optimisation.
    
    Returns vector of RMSE values (to be minimised on Pareto frontier).
    """
    sim = run_rsnn_simulation(connectivity_params)
    
    # Objective 1: Firing rate RMSE
    rmse_firing = compute_firing_rate_rmse(
        sim.excitatory_rates, target_firing_rates['excitatory'],
        sim.inhibitory_rates, target_firing_rates['inhibitory']
    )
    
    # Objective 2: Oscillation frequency RMSE  
    dom_freq_sim = extract_dominant_frequency(sim.lfp)  # via FFT/Welch
    rmse_oscillation = np.sqrt(np.mean((dom_freq_sim - target_oscillations)**2))
    
    return [rmse_firing, rmse_oscillation]  # Multi-objective return
```

### NSGA-III Setup
```python
from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.util.ref_dirs import get_reference_directions

# Reference directions for 2 objectives
ref_dirs = get_reference_directions("das-dennis", 2, n_partitions=12)

algorithm = NSGA3(
    pop_size=100,
    ref_dirs=ref_dirs,
    # Crossover/mutation on connectivity parameters
    crossover=SBX(prob=0.9, eta=15),
    mutation=PM(eta=20),
    eliminate_duplicates=True
)

# Problem definition
class RSNNOptimisation(ElementwiseProblem):
    def __init__(self, target_rates, target_freqs):
        super().__init__(
            n_var=N_CONNECTIVITY_PARAMS,
            n_obj=2,  # firing rate RMSE + oscillation RMSE
            n_constr=0,
            xl=PARAM_LOWER_BOUNDS,
            xu=PARAM_UPPER_BOUNDS
        )
        self.target_rates = target_rates
        self.target_freqs = target_freqs
    
    def _evaluate(self, x, out, *args, **kwargs):
        rmse_rates, rmse_osc = fitness_rsnn(x, self.target_rates, self.target_freqs)
        out["F"] = [rmse_rates, rmse_osc]
```

## Step-by-Step Implementation

### Step 1: Simulate Izhikevich RSNN
```python
def run_rsnn_simulation(params, duration_ms=5000, dt=0.5):
    """
    Run recurrent Izhikevich SNN simulation.
    params: dict with connectivity weights and synaptic time constants
    """
    N_e = 800  # excitatory
    N_i = 200  # inhibitory
    N = N_e + N_i
    
    # Initialize state
    v = -65 * np.ones(N)
    u = NEURON_PARAMS['b'] * v
    
    W_EE = params['W_EE']  # E->E weight matrix
    W_EI = params['W_EI']  # E->I
    W_IE = params['W_IE']  # I->E
    W_II = params['W_II']  # I->I
    
    spike_times = {i: [] for i in range(N)}
    LFP = []
    
    for t in np.arange(0, duration_ms, dt):
        # Compute input currents from spikes
        I = compute_synaptic_currents(v, spike_times, W_EE, W_EI, W_IE, W_II, t)
        
        # Add background noise
        I[:N_e] += 5 * np.random.randn(N_e)
        I[N_e:] += 2 * np.random.randn(N_i)
        
        # Update Izhikevich dynamics
        fired = v >= 30
        v_new = v + dt * (0.04*v**2 + 5*v + 140 - u + I)
        u_new = u + dt * (NEURON_PARAMS['a'] * (NEURON_PARAMS['b']*v - u))
        
        # Reset fired neurons
        v_new[fired] = NEURON_PARAMS['c']
        u_new[fired] += NEURON_PARAMS['d']
        
        v, u = v_new, u_new
        for i in np.where(fired)[0]:
            spike_times[i].append(t)
        
        # LFP as mean membrane potential
        LFP.append(np.mean(v[:N_e]))
    
    return {'spike_times': spike_times, 'LFP': np.array(LFP), 'dt': dt}
```

### Step 2: Extract Neural Observables
```python
def extract_dominant_frequency(lfp, dt_ms, freq_range=(1, 100)):
    """Extract dominant oscillation frequency using Welch's method."""
    from scipy.signal import welch
    
    fs = 1000 / dt_ms  # Hz
    freqs, psd = welch(lfp, fs=fs, nperseg=1024)
    
    # Focus on physiological range
    mask = (freqs >= freq_range[0]) & (freqs <= freq_range[1])
    dom_freq = freqs[mask][np.argmax(psd[mask])]
    
    return dom_freq  # Hz

def compute_firing_rates(spike_times, N, duration_ms, bin_size_ms=100):
    """Compute mean firing rates for E and I populations."""
    rates = []
    for i in range(N):
        n_spikes = len([t for t in spike_times[i] if t > 500])  # skip transient
        rate = n_spikes / ((duration_ms - 500) / 1000)  # Hz
        rates.append(rate)
    return np.array(rates)
```

### Step 3: Multi-Objective Pareto Analysis
```python
def pareto_analysis(optimization_result):
    """
    Analyse Pareto frontier from NSGA-III results.
    Trade-off between firing rate accuracy vs oscillation accuracy.
    """
    F = optimization_result.F  # (n_solutions, 2) array of RMSE values
    X = optimization_result.X  # (n_solutions, n_params) parameter array
    
    # Find knee point (best compromise)
    from pymoo.decomposition.asf import ASF
    decomp = ASF()
    weights = np.array([0.5, 0.5])  # equal weight to both objectives
    i_knee = np.argmin(decomp.do(F, 1/weights))
    
    return {
        'pareto_front': F,
        'pareto_params': X,
        'knee_solution': X[i_knee],
        'knee_objectives': F[i_knee],
        'n_pareto': len(F)
    }
```

## Validated on Brain Organoid Data

### Brain Organoid-specific Notes
```python
# Brain organoids have lower baseline activity than adult cortex
# Target parameters for organoid fitting:
ORGANOID_TARGETS = {
    'excitatory_rate': 0.5,   # Hz (low activation)
    'inhibitory_rate': 0.8,   # Hz
    'dominant_frequency': 10, # Hz (alpha-like)
    'std_tolerance': 0.3      # Hz RMSE tolerance
}

# Key finding: NSGA-III identifies "low-activity regime" 
# characteristic of immature cortical tissue
```

## Key Findings from Paper

1. **NSGA-III succeeds**: Can simultaneously match firing rates AND oscillation frequencies
2. **Oscillation frequencies are more parameter-sensitive** than firing rates
3. **Firing rates are more robustly matched** across Pareto solutions
4. **Brain organoid**: Successfully fit with low-activity regime parameters
5. **Decision-making model**: Can fit activity patterns across different time epochs (pre-stimulus, post-stimulus, decision)

## Pitfalls

- **Oscillation frequency sensitivity**: Small changes in connectivity → large frequency shifts. Need tight parameter bounds
- **Simulation length**: Need ≥ 5000 ms for stable frequency estimation (Welch needs enough data)
- **Transient exclusion**: Exclude first 500 ms transient from rate/frequency computation
- **Population imbalance**: E/I ratio 80/20 is critical — changing this breaks oscillatory dynamics
- **GA population size**: Need ≥ 100 individuals for stable Pareto front convergence

## Decision-Making Extension

```python
# Transient decision dynamics: multiple time epochs
DECISION_EPOCHS = {
    'baseline': (0, 500),       # ms
    'stimulus': (500, 1000),    # stimulus onset
    'decision': (1000, 2000),   # decision period
    'post': (2000, 3000)        # post-decision
}

# Add 3rd objective: decision accuracy
def fitness_with_decision(params):
    sim = run_rsnn_simulation(params, duration_ms=3000)
    
    rmse_rates = compute_epoch_rate_rmse(sim, DECISION_EPOCHS)
    rmse_osc = compute_oscillation_rmse(sim)
    decision_acc = compute_decision_accuracy(sim)
    
    return [rmse_rates, rmse_osc, 1 - decision_acc]  # 3 objectives
```

## Citation

```bibtex
@article{sethi2026multiobjective,
  title={Multi-Objective Optimisation with Oscillatory Dynamics in Spontaneous and Decision Spiking Neural Networks},
  author={Sethi, Divyansh and Faraz, Muhammad and Wong-Lin, KongFatt},
  journal={arXiv:2605.25224},
  year={2026}
}
```
