---
name: multi-objective-snn-oscillation
description: Multi-objective genetic algorithm (NSGA-III) optimisation of spiking neural networks (RSNNs) to match neural firing rates and oscillation frequencies for computational neuroscience modeling.
tags: [spiking-neural-network, genetic-algorithm, neural-oscillation, brain-organoid, nsga-iii, computational-neuroscience, izhikevich-neuron]
category: ai_collection
version: "1.0"
source: "arXiv:2605.25224"
authors: ["Divyansh Sethi", "Muhammad Faraz", "KongFatt Wong-Lin"]
---

# Multi-Objective SNN Oscillation Optimization

## Overview

Use NSGA-III (non-dominated sorting genetic algorithm) to optimize recurrent SNN (RSNN) connectivity parameters for simultaneously matching multiple neural targets: firing rates, oscillation frequencies, and decision-making activity patterns. Validated on simulated RSNNs, brain organoids, and decision-making models.

**Trigger conditions:** Use when fitting SNNs to experimental neural data, modeling brain organoids, optimizing oscillatory dynamics in recurrent networks, multi-objective neural parameter search.

## Architecture

### Neuron Model
- **Izhikevich neurons**: Simple yet biologically realistic 2D model capturing diverse spiking patterns
  - Regular spiking (RS) for excitatory cortical neurons
  - Fast spiking (FS) for inhibitory interneurons
  - Parameters: a, b, c, d, I (input current)

### Network Structure
- **Recurrent SNN (RSNN)**: Excitatory + inhibitory cortical neuron populations
- **Spontaneous activity**: Network generates intrinsic firing without external drive
- **Decision-making variant**: Includes transient decision dynamics with multiple time epochs

### NSGA-III Multi-Objective Targets
1. **Firing rates**: Sub-population RMSEs for excitatory and inhibitory neurons
2. **Dominant oscillation frequencies**: Network-wide spectral power peaks (e.g., gamma, beta, theta)
3. **Decision epoch patterns**: Activity in pre-decision, decision, and post-decision windows

## Optimization Workflow

```python
import numpy as np
from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.core.problem import Problem
from pymoo.util.ref_dirs import get_reference_directions
import neuron_sim  # custom SNN simulator

class RSNNOptimizationProblem(Problem):
    """Multi-objective RSNN parameter optimization."""
    
    def __init__(self, target_firing_rates, target_oscillation_freqs, 
                 n_neurons_exc=800, n_neurons_inh=200):
        # Optimize: [w_EE, w_EI, w_IE, w_II, conn_prob, ...]
        n_vars = 6  # connectivity parameters
        n_objectives = 3  # firing rate RMSE + oscillation freq RMSE + epoch pattern RMSE
        
        xl = np.zeros(n_vars)  # lower bounds
        xu = np.ones(n_vars) * 5.0  # upper bounds
        
        super().__init__(n_var=n_vars, n_obj=n_objectives, xl=xl, xu=xu)
        
        self.target_fr = target_firing_rates
        self.target_osc = target_oscillation_freqs
        self.n_exc = n_neurons_exc
        self.n_inh = n_neurons_inh
    
    def _evaluate(self, X, out, *args, **kwargs):
        F = np.zeros((len(X), self.n_obj))
        
        for i, params in enumerate(X):
            # Run RSNN simulation
            results = neuron_sim.simulate_rsnn(
                params, self.n_exc, self.n_inh, 
                dt=0.1, T=2000  # ms
            )
            
            # Objective 1: Firing rate RMSE
            firing_rates = results['firing_rates']  # [exc_rate, inh_rate]
            F[i, 0] = np.sqrt(np.mean((firing_rates - self.target_fr)**2))
            
            # Objective 2: Oscillation frequency RMSE
            dominant_freq = compute_dominant_frequency(results['lfp'])
            F[i, 1] = np.abs(dominant_freq - self.target_osc)
            
            # Objective 3: Epoch activity RMSE (for decision model)
            epoch_patterns = extract_epoch_patterns(results['spikes'])
            F[i, 2] = np.sqrt(np.mean((epoch_patterns - self.target_epochs)**2))
        
        out["F"] = F

def optimize_rsnn(target_fr, target_osc, n_gen=200, pop_size=100):
    """Run NSGA-III optimization."""
    ref_dirs = get_reference_directions("das-dennis", 3, n_partitions=12)
    
    algorithm = NSGA3(
        pop_size=pop_size,
        ref_dirs=ref_dirs
    )
    
    problem = RSNNOptimizationProblem(target_fr, target_osc)
    
    from pymoo.optimize import minimize
    result = minimize(
        problem, algorithm,
        termination=('n_gen', n_gen),
        seed=42, verbose=True
    )
    
    return result.X, result.F  # Pareto-optimal solutions

def compute_dominant_frequency(lfp_signal, fs=1000):
    """Extract dominant oscillation frequency from LFP."""
    from scipy.signal import welch
    freqs, psd = welch(lfp_signal, fs=fs, nperseg=1024)
    dominant_idx = np.argmax(psd[1:]) + 1  # exclude DC
    return freqs[dominant_idx]
```

## Key Experimental Results

### Spontaneous RSNN
- NSGA-III successfully optimized for multiple firing rates simultaneously
- Oscillation frequencies more parameter-sensitive (harder to match precisely)
- Firing rates more robustly achieved than oscillation targets

### Brain Organoid Fitting
- Same framework applied to low-activation organoid recordings
- Model matched observed spontaneous dynamics without architectural changes
- Validates framework generalizes beyond purely simulated data

### Decision-Making Model
- Added transient dynamics for 3 temporal epochs (pre/during/post-decision)
- NSGA-III optimized for epoch-specific activity patterns
- Identified low-activity regime consistent with decision-making states

## Parameter Sensitivity Analysis

| Parameter | Sensitivity to Firing Rate | Sensitivity to Oscillation |
|-----------|---------------------------|---------------------------|
| w_EE (E→E weight) | High | Very High |
| w_IE (I→E weight) | High | Very High |
| w_EI (E→I weight) | Medium | High |
| w_II (I→I weight) | Low | Medium |
| Connection probability | Medium | Medium |
| Background input strength | High | Low |

**Key insight**: Oscillation frequencies are MORE sensitive to parameter changes than firing rates, requiring tighter optimization tolerances.

## Implementation Steps

1. **Choose neuron model**: Izhikevich (recommended), LIF, or AdEx for different trade-offs
2. **Set network architecture**: E/I ratio (typically 4:1), synaptic time constants
3. **Define objectives**: Choose from {firing rates, oscillation frequencies, decision patterns}
4. **Configure NSGA-III**: Population size ≥100, generations ≥100, Das-Dennis reference directions
5. **Run optimization**: Track Pareto frontier across objectives
6. **Evaluate solutions**: Use RMSE on Pareto frontier to select operating point
7. **Validate**: Test generalization to held-out conditions

## Pitfalls

- **Oscillation sensitivity**: Dominant frequencies are highly sensitive; use fine grid evaluation
- **Local optima**: Run multiple random seeds and take best Pareto front
- **Simulation time**: Each evaluation requires full network simulation (~seconds); total optimization takes hours
- **Decision-making epochs**: Transient dynamics require careful epoch boundary definition
- **Low-activity regimes**: Decision models have multiple attractor states; ensure exploration near low-activity solutions

## Connections

- Related: `multi-objective-quantum-workflow`, `spiking-oscillation-mapping`, `evolutionary-snn-classifier`
- Neuron model: `learning-neuron-dynamics-deep-snn`
- Brain organoid: `brain-organoid-molecular-communication`

## References

- Sethi, Faraz & Wong-Lin (2026). "Multi-Objective Optimisation with Oscillatory Dynamics in Spontaneous and Decision Spiking Neural Networks." arXiv:2605.25224
- Izhikevich (2003). Simple model of spiking neurons. IEEE TNN.
- Deb et al. (2014). An evolutionary many-objective optimization algorithm using reference-point-based nondominated sorting. IEEE TEVC (NSGA-III).
