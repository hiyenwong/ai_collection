---
name: neuromodulation-cpg
description: Neuromodulation-based control architecture for dynamically reconfiguring rhythmic activity in central pattern generators (CPGs) with fixed connectivity. Uses equivariant bifurcation theory to achieve reliable rhythm switching despite neuronal degeneracy.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [neuroscience, neuromodulation, CPG, rhythmic-patterns, bifurcation-theory, motor-control]
    source_paper: "Neuromodulation supports robust rhythmic pattern transitions in degenerate central pattern generators with fixed connectivity (arXiv:2604.08312)"
    citations: 0
    published: "2026-04-09"
---

# Neuromodulation for CPG Rhythm Control

## Overview

This skill implements a **neuromodulation-based control architecture** for dynamically reconfiguring rhythmic activity in neural networks with fixed connectivity. It addresses the challenge of achieving reliable rhythm switching despite **neuronal degeneracy**—where different parameter combinations produce similar functional output.

## Biological Context

### Central Pattern Generators (CPGs)
- Neural circuits that produce rhythmic motor patterns
- Control essential functions: breathing, locomotion, chewing
- Traditionally viewed as hardwired circuits with slow synaptic plasticity

### The Degeneracy Problem
- Multiple parameter sets can produce the same rhythmic output
- Makes precise control challenging
- Traditional approaches require structural connectivity changes

## Key Innovation

**Rapid Rhythm Switching via Neuromodulation**: Instead of slow synaptic plasticity, use fast neuromodulatory control to reconfigure network dynamics while maintaining fixed connectivity.

## Core Concepts

### 1. Equivariant Bifurcation Theory
Mathematical framework for analyzing how symmetries in neural networks affect their dynamical behavior:

```python
# Bifurcation analysis for CPG control
import numpy as np
from scipy.optimize import fsolve

def analyze_bifurcation(model, parameters):
    """
    Identify bifurcation points where rhythmic patterns change.
    
    Args:
        model: Neural network model (e.g., Kuramoto, Wilson-Cowan)
        parameters: Dictionary of neuromodulatory parameters
    
    Returns:
        bifurcation_points: List of parameter values where transitions occur
        stability: Stability of each rhythmic state
    """
    # Find fixed points
    fixed_points = find_fixed_points(model, parameters)
    
    # Compute Jacobian at each fixed point
    jacobians = [compute_jacobian(model, fp, parameters) for fp in fixed_points]
    
    # Identify bifurcations (eigenvalue crossings)
    bifurcation_points = detect_bifurcations(jacobians, parameters)
    
    return bifurcation_points
```

### 2. Neuromodulatory Control Space
```python
class NeuromodulatoryController:
    """
    Controller for reconfiguring CPG rhythms via neuromodulation.
    """
    
    def __init__(self, network, modulator_sites):
        """
        Args:
            network: CPG network model with fixed connectivity
            modulator_sites: List of neurons that can be modulated
        """
        self.network = network
        self.modulator_sites = modulator_sites
        self.bifurcation_map = self._compute_bifurcation_map()
    
    def _compute_bifurcation_map(self):
        """Pre-compute bifurcation structure for control planning."""
        # Analyze how neuromodulatory parameters affect network dynamics
        parameter_space = self._sample_parameter_space()
        bifurcation_map = {}
        
        for params in parameter_space:
            rhythm_type = self._classify_rhythm(params)
            bifurcation_map[params] = rhythm_type
        
        return bifurcation_map
    
    def switch_rhythm(self, target_rhythm, current_state):
        """
        Compute neuromodulatory input to switch to target rhythm.
        
        Args:
            target_rhythm: Desired rhythmic pattern (e.g., 'walk', 'trot', 'gallop')
            current_state: Current network state
        
        Returns:
            modulatory_input: Neuromodulatory parameters to apply
        """
        # Find path in bifurcation map to target rhythm
        path = self._plan_transition(current_state, target_rhythm)
        
        # Compute optimal neuromodulatory input
        modulatory_input = self._compute_control_signal(path)
        
        return modulatory_input
```

### 3. Robustness to Degeneracy
```python
def handle_degeneracy(control_output, degenerate_set):
    """
    Select control input that works across degenerate parameter combinations.
    
    Args:
        control_output: Computed neuromodulatory input
        degenerate_set: Set of equivalent parameter combinations
    
    Returns:
        robust_control: Control input robust to degenerate variations
    """
    # Test control across degenerate set
    performances = []
    for params in degenerate_set:
        performance = test_control(control_output, params)
        performances.append(performance)
    
    # Optimize for worst-case performance (minimax)
    robust_control = optimize_minimax(control_output, degenerate_set)
    
    return robust_control
```

## Implementation Pattern

### CPG Network Model
```python
import numpy as np

class CPGNetwork:
    """
    Central Pattern Generator network with neuromodulatory control.
    Based on conductance-based neuron models.
    """
    
    def __init__(self, n_neurons, connectivity_matrix):
        self.n = n_neurons
        self.W = connectivity_matrix  # Fixed connectivity
        self.state = np.zeros(n_neurons)
        
        # Neuromodulatory parameters (controllable)
        self.g_mod = np.ones(n_neurons)  # Modulatory conductance
        self.E_mod = np.zeros(n_neurons)  # Modulatory reversal potential
        self.tau_mod = np.ones(n_neurons)  # Modulatory time constant
    
    def dynamics(self, state, t, external_input=0):
        """Network dynamics with neuromodulation."""
        # Intrinsic neuron dynamics
        I_intrinsic = self._intrinsic_current(state)
        
        # Synaptic input (fixed connectivity)
        I_synaptic = self.W @ self._synaptic_output(state)
        
        # Neuromodulatory input (controllable)
        I_modulatory = self.g_mod * (self.E_mod - state)
        
        # Total current
        I_total = I_intrinsic + I_synaptic + I_modulatory + external_input
        
        # State update
        dstate = (I_total - state) / self.tau_mod
        return dstate
    
    def apply_neuromodulation(self, mod_params):
        """Apply neuromodulatory control."""
        self.g_mod = mod_params['conductance']
        self.E_mod = mod_params['reversal_potential']
        self.tau_mod = mod_params['time_constant']
```

### Rhythm Classification
```python
def classify_rhythm(state_trajectory):
    """
    Classify rhythmic pattern from network activity.
    
    Args:
        state_trajectory: Time series of network states
    
    Returns:
        rhythm_type: Classification of rhythmic pattern
        features: Quantitative rhythm features
    """
    # Compute phase relationships between neurons
    phases = extract_phases(state_trajectory)
    
    # Analyze phase locking
    phase_diffs = compute_phase_differences(phases)
    
    # Classify based on phase relationships
    if is_synchronized(phase_diffs):
        return 'synchronous', {'phase_diff': 0}
    elif is_alternating(phase_diffs):
        return 'alternating', {'phase_diff': np.pi}
    else:
        return 'complex', {'phase_diffs': phase_diffs}
```

## Applications

1. **Robotics**: Adaptive locomotion control (walking, swimming, flying)
2. **Prosthetics**: Natural rhythmic movement restoration
3. **Neurorehabilitation**: Gait training and motor recovery
4. **Biomimetic Systems**: Bio-inspired rhythmic control

## Mathematical Framework

### Bifurcation Analysis
```
Given: Network dynamics dx/dt = f(x, μ)
Where: x = neural states, μ = neuromodulatory parameters

Find: Bifurcation points where qualitative behavior changes

Method:
1. Compute equilibrium points: f(x*, μ) = 0
2. Linearize: J = ∂f/∂x at (x*, μ)
3. Find eigenvalue crossings: Re(λ_i(J)) = 0
4. Classify bifurcation type (Hopf, pitchfork, etc.)
```

### Control Design
```
Objective: Switch from rhythm R1 to R2

Approach:
1. Identify regions in μ-space supporting each rhythm
2. Find bifurcation boundary between regions
3. Design μ(t) trajectory crossing boundary
4. Ensure robustness to degenerate variations
```

## References

- Fyon, A., et al. (2026). Neuromodulation supports robust rhythmic pattern transitions in degenerate central pattern generators with fixed connectivity. arXiv:2604.08312.
- Related: CPG theory (Marder & Calabrese, 1996), Neuromodulation (Marder, 2012)

## See Also

- `in-context-brain-decoding`: Brain decoding methods
- `eeg-cnn-autoencoder`: Neural signal processing
