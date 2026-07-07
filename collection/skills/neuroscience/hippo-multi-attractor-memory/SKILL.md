---
name: hippo-multi-attractor-memory
description: "Biologically detailed extension of Hopfield/Marr auto-associative memory model for CA3 hippocampus. Implements ten populations (two asymmetric pyramidal subtypes, eight GABAergic interneurons) to study multi-attractor dynamics and stability effects in memory circuits."
paper:
  arxiv_id: "2604.20679v1"
  title: "Learning Hippo: Multi-attractor Dynamics and Stability Effects in a Biologically Detailed CA3 Model"
  published: "2026-04-22"
  categories: ["q-bio.NC"]
---

# Hippo Multi-Attractor Memory Methodology

Biologically detailed extension of the classical Hopfield/Marr auto-associative memory model for CA3 hippocampus.

## Overview

**Paper:** Learning Hippo: Multi-attractor Dynamics and Stability Effects in a Biologically Detailed CA3 Model (arXiv:2604.20679v1)

**Published:** 2026-04-22

**Key Innovation:** Multi-population hippocampal model with asymmetric connectivity and diverse interneuron types for studying memory attractor dynamics.

## Biological Architecture

### Ten-Population Model Structure

```
CA3 Circuit Implementation:
├── Pyramidal Neurons (2 subtypes)
│   ├── Pyr-A: Asymmetric connectivity, strong recurrent excitation
│   └── Pyr-B: Weak recurrent, dominant feedforward input
└── GABAergic Interneurons (8 types)
    ├── PV+ basket cells: Perisomatic inhibition
    ├── PV+ axo-axonic cells: Axon initial segment control
    ├── SOM+ O-LM cells: Distal dendritic inhibition
    ├── SOM+ bistratified cells: Stratum radiatum inhibition
    ├── CCK+ basket cells: Modulated inhibition
    ├── CCK+ Schaffer-associated cells
    ├── NPY+ neurogliaform cells: Volume transmission
    └── Ivy cells: Dendritic inhibition
```

## Core Mechanisms

### 1. Asymmetric Pyramidal Subtypes

```python
class PyramidalNeuron:
    """Biologically detailed pyramidal neuron model"""
    
    def __init__(self, subtype='A'):
        self.subtype = subtype
        
        # Subtype-specific parameters
        if subtype == 'A':
            self.recurrent_strength = 0.8  # Strong recurrent
            self.ff_strength = 0.3         # Weak feedforward
            self.adaptation = 0.1
        else:  # subtype B
            self.recurrent_strength = 0.2
            self.ff_strength = 0.9
            self.adaptation = 0.05
    
    def compute_synaptic_current(self, pre_synaptic, connection_type):
        """Compute synaptic input based on connection type"""
        if connection_type == 'recurrent':
            return self.recurrent_strength * pre_synaptic
        elif connection_type == 'feedforward':
            return self.ff_strength * pre_synaptic
        else:
            return 0.0
```

### 2. Multi-Attractor Dynamics

```python
class MultiAttractorNetwork:
    """
    Multi-attractor dynamics in hippocampal CA3
    Supports multiple co-existing stable states
    """
    
    def __init__(self, n_patterns=10, n_neurons=1000):
        self.n_patterns = n_patterns
        self.n_neurons = n_neurons
        
        # Pattern-specific connectivity
        self.pattern_weights = np.zeros((n_patterns, n_neurons, n_neurons))
        
        # Baseline connectivity
        self.W = np.zeros((n_neurons, n_neurons))
        
        # Attractor states
        self.attractors = []
        self.basins = []
    
    def store_patterns(self, patterns):
        """
        Store multiple patterns using Hebbian learning
        Creates overlapping attractor basins
        """
        for i, pattern in enumerate(patterns):
            # Hebbian learning with pattern-specific weight matrix
            self.pattern_weights[i] = np.outer(pattern, pattern) / len(pattern)
        
        # Combine pattern weights with competition
        self.W = self.combine_pattern_weights()
    
    def combine_pattern_weights(self):
        """
        Combine multiple pattern weights ensuring stable multi-attractor landscape
        """
        W_total = np.zeros_like(self.pattern_weights[0])
        
        for W_pattern in self.pattern_weights:
            # Normalize to prevent domination by single pattern
            W_total += W_pattern / self.n_patterns
        
        # Apply Dale's law (excitatory only for pyramidal)
        W_total = np.maximum(W_total, 0)
        
        # Sparse connectivity (biologically realistic ~10%)
        mask = np.random.rand(*W_total.shape) < 0.1
        W_total *= mask
        
        return W_total
    
    def network_dynamics(self, initial_state, dt=0.1, T=100):
        """
        Simulate network dynamics converging to attractor
        """
        state = initial_state.copy()
        trajectory = [state.copy()]
        
        for t in range(int(T/dt)):
            # Membrane potential dynamics
            I_syn = np.dot(self.W, state)
            I_inh = self.compute_inhibition(state)
            
            # Update with leak and adaptation
            dV = (-state + I_syn - I_inh - self.adaptation_current(state)) * dt
            state = np.maximum(state + dV, 0)  # ReLU-like activation
            
            trajectory.append(state.copy())
        
        return np.array(trajectory)
    
    def compute_inhibition(self, state):
        """
        Compute multi-population inhibition
        """
        inhibition = 0
        
        # PV+ basket cells: fast, strong perisomatic inhibition
        inhibition += self.pv_basket_gain * np.mean(state) * np.ones_like(state)
        
        # SOM+ cells: slower, dendritic targeting
        inhibition += self.som_gain * np.mean(state) * 0.5 * np.ones_like(state)
        
        # NPY+ neurogliaform: volume transmission
        inhibition += self.npy_gain * np.mean(state) * 0.3 * np.ones_like(state)
        
        return inhibition
```

### 3. Stability Analysis

```python
class StabilityAnalysis:
    """
    Analyze multi-attractor stability using Jacobian and Lyapunov methods
    """
    
    def __init__(self, network):
        self.network = network
    
    def compute_jacobian(self, fixed_point):
        """
        Compute Jacobian matrix at fixed point for stability analysis
        """
        n = len(fixed_point)
        J = np.zeros((n, n))
        
        # Numerical Jacobian computation
        eps = 1e-6
        for i in range(n):
            perturbed = fixed_point.copy()
            perturbed[i] += eps
            
            # Compute dynamics difference
            f_original = self.network.dynamics_step(fixed_point)
            f_perturbed = self.network.dynamics_step(perturbed)
            
            J[:, i] = (f_perturbed - f_original) / eps
        
        return J
    
    def analyze_attractor_stability(self, attractor):
        """
        Determine stability of attractor via eigenvalue analysis
        """
        J = self.compute_jacobian(attractor)
        eigenvalues = np.linalg.eigvals(J)
        
        # Attractor is stable if all eigenvalues have negative real part
        max_real = np.max(np.real(eigenvalues))
        
        return {
            'stable': max_real < 0,
            'max_eigenvalue_real': max_real,
            'eigenvalues': eigenvalues,
            'basin_size_estimate': self.estimate_basin_size(attractor)
        }
    
    def estimate_basin_size(self, attractor, n_samples=1000):
        """
        Estimate basin of attraction via Monte Carlo sampling
        """
        converged = 0
        
        for _ in range(n_samples):
            # Random initial condition
            initial = np.random.randn(len(attractor))
            
            # Simulate to convergence
            final = self.network.network_dynamics(initial)[-1]
            
            # Check if converged to target attractor
            if np.linalg.norm(final - attractor) < 0.1:
                converged += 1
        
        return converged / n_samples
```

## Multi-Attractor Phenomena

### 1. Pattern Completion

```python
def demonstrate_pattern_completion(network, partial_pattern, target_pattern):
    """
    Show how CA3 completes partial input patterns
    """
    # Initialize with partial cue
    initial_state = partial_pattern.copy()
    
    # Run dynamics
    trajectory = network.network_dynamics(initial_state)
    final_state = trajectory[-1]
    
    # Measure completion accuracy
    accuracy = np.corrcoef(final_state, target_pattern)[0, 1]
    
    return {
        'initial': partial_pattern,
        'final': final_state,
        'accuracy': accuracy,
        'convergence_time': len(trajectory)
    }
```

### 2. Pattern Separation

```python
def analyze_pattern_separation(network, pattern1, pattern2):
    """
    Measure how network separates similar input patterns
    """
    # Initial overlap
    initial_overlap = np.dot(pattern1, pattern2) / (np.linalg.norm(pattern1) * np.linalg.norm(pattern2))
    
    # Run dynamics
    final1 = network.network_dynamics(pattern1)[-1]
    final2 = network.network_dynamics(pattern2)[-1]
    
    # Final overlap (should be lower if good separation)
    final_overlap = np.dot(final1, final2) / (np.linalg.norm(final1) * np.linalg.norm(final2))
    
    separation_ratio = initial_overlap / (final_overlap + 1e-6)
    
    return {
        'initial_overlap': initial_overlap,
        'final_overlap': final_overlap,
        'separation_ratio': separation_ratio
    }
```

### 3. Attractor Switching

```python
def study_attractor_switching(network, current_attractor, target_attractor, perturbation_strength):
    """
    Study transitions between attractors
    """
    # Start in one attractor
    state = current_attractor.copy()
    
    # Apply perturbation toward target
    perturbation = perturbation_strength * (target_attractor - current_attractor)
    perturbed_state = state + perturbation
    
    # Run dynamics
    trajectory = network.network_dynamics(perturbed_state)
    final_state = trajectory[-1]
    
    # Determine which attractor was reached
    dist_to_current = np.linalg.norm(final_state - current_attractor)
    dist_to_target = np.linalg.norm(final_state - target_attractor)
    
    return {
        'switched': dist_to_target < dist_to_current,
        'trajectory': trajectory,
        'final_attractor': 'target' if dist_to_target < dist_to_current else 'original'
    }
```

## Biological Insights

### Key Findings

1. **Asymmetric Connectivity Enables Multi-Stability**
   - Pyr-A neurons maintain strong recurrent connections for pattern completion
   - Pyr-B neurons provide flexible feedforward gating

2. **Interneuron Diversity Supports Stable Attractors**
   - PV+ basket cells: Fast inhibition prevents runaway excitation
   - SOM+ cells: Dendritic inhibition controls plasticity
   - NPY+ cells: Modulate overall network excitability

3. **Stability-Plasticity Trade-off**
   - Strong recurrent weights: Better pattern completion but harder switching
   - Inhibition strength: Controls attractor basin size
   - Adaptation currents: Enable temporal dynamics

## Applications

### 1. Memory Modeling
- Episodic memory formation and retrieval
- Pattern completion in familiar contexts
- Context-dependent recall

### 2. Pathological States
- Epileptic seizure dynamics (runaway attractors)
- Memory disorders (weak attractors)
- Schizophrenia (unstable attractor switching)

### 3. Neuromorphic Computing
- Energy-efficient associative memory
- Fault-tolerant pattern storage
- Brain-inspired AI architectures

## Implementation Guidelines

### Simulation Parameters

```python
# Recommended biophysical parameters
params = {
    'n_pyramidal': 800,          # Total pyramidal neurons
    'n_interneurons': 200,        # Total interneurons (20%)
    'connection_prob': 0.1,       # Sparse connectivity
    'excitatory_ratio': 0.8,      # Excitatory dominance
    'tau_membrane': 20e-3,        # 20 ms membrane time constant
    'tau_synapse': 5e-3,          # 5 ms synaptic time constant
    'adaptation_strength': 0.1,   # Spike-frequency adaptation
}
```

### Validation

1. **Single Neuron Properties**
   - Match experimental I-F curves
   - Reproduce adaptation dynamics
   - Validate synaptic time constants

2. **Network Properties**
   - Oscillation frequencies (theta, gamma)
   - Place cell characteristics
   - Sharp-wave ripple events

3. **Behavioral Predictions**
   - Memory capacity
   - Pattern completion accuracy
   - Recall latency

## References

- Learning Hippo: Multi-attractor Dynamics and Stability Effects in a Biologically Detailed CA3 Model. arXiv:2604.20679v1 (2026)
- Marr, D. (1971). Simple memory: A theory for archicortex.
- Hopfield, J.J. (1982). Neural networks and physical systems with emergent collective computational abilities.

## Activation Keywords

- Multi-attractor dynamics
- Hippocampal CA3 model
- Hopfield network extension
- Memory attractors
- Pattern completion
- Biological neural circuits
- Auto-associative memory
