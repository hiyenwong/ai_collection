---
name: differential-dynamic-causal-nets---differential-dy
description: Skill for AI agent capabilities
---

# differential-dynamic-causal-nets - Differential Dynamic Causal Nets: Model Construction, Identification and Group Comparisons

## Description

A novel approach to construct differential causal networks directly from EEG data. The network is based on conditionally coupled neuronal circuits describing average behavior of interacting neuron populations. Features a hierarchical mixed-effects model structure and evolutionary optimization using Chen-Fliess expansions.

**Source:** arXiv:2601.21478v1
**Utility:** 0.91

## Activation Keywords

- differential causal network
- dynamic causal modeling
- EEG causal analysis
- neural population model
- Jansen-Rit model
- epileptic connectivity
- mixed-effects neural model
- Chen-Fliess expansion

## Core Concepts

### 1. Differential Causal Network Framework

```
EEG Data → Coupled Neural Circuits → Differential Causal Network → Parameter Inference → Group Comparisons
```

**Key insight:** Model average behavior of interacting neuron populations contributing to observed EEG.

### 2. Network Structure

| Component | Description |
|-----------|-------------|
| **Nodes** | Parameterized local neural systems (Jansen-Rit models) |
| **Edges** | Directed connections with transmission parameters |
| **Hierarchy** | Mixed-effects model (parameters vary across subjects) |

### 3. Parameter Inference

**Evolutionary optimization algorithm** using loss function from Chen-Fliess expansions of stochastic differential equations.

### 4. Applications

- **Epileptic activity tracking** - Detect network functional disruptions
- **Excitatory-inhibitory imbalance** - Characterize before/during seizure
- **Brain connectivity changes** - Monitor dynamic causality

## Step-by-Step Instructions

### 1. Construct Jansen-Rit Local Model

```python
import numpy as np

class JansenRitModel:
    """Jansen-Rit neural population model."""
    
    def __init__(self, params=None):
        # Default parameters
        self.params = {
            'A': 3.25,       # Excitatory gain
            'B': 22.0,       # Inhibitory gain
            'a': 0.1,        # Excitatory time constant
            'b': 0.05,       # Inhibitory time constant
            'C': 135.0,      # Connectivity constant
            'v0': 6.0,       # Sigmoid threshold
            'e0': 2.5,       # Sigmoid max firing rate
            'r': 0.56,       # Sigmoid slope
        }
        if params:
            self.params.update(params)
    
    def sigmoid(self, x):
        """Sigmoid function for firing rate."""
        v0 = self.params['v0']
        e0 = self.params['e0']
        r = self.params['r']
        return 2 * e0 / (1 + np.exp(r * (v0 - x)))
    
    def simulate(self, input_signal, dt=0.001, duration=10):
        """
        Simulate Jansen-Rit model dynamics.
        
        Args:
            input_signal: External input (e.g., from other nodes)
            dt: Time step
            duration: Simulation duration (seconds)
        
        Returns:
            EEG-like output signal
        """
        steps = int(duration / dt)
        
        # State variables
        y0 = np.zeros(steps)  # Excitatory population
        y1 = np.zeros(steps)  # Interneuron population
        y2 = np.zeros(steps)  # Inhibitory population
        
        # Simulate
        for i in range(1, steps):
            # Differential equations
            dy0 = y1[i-1] - y2[i-1]
            dy1 = self.params['A'] * self.sigmoid(y0[i-1]) - 2 * self.params['a'] * y1[i-1]
            dy2 = self.params['B'] * self.sigmoid(y0[i-1]) - 2 * self.params['b'] * y2[i-1]
            
            # Update
            y0[i] = y0[i-1] + dt * dy0 + dt * input_signal[i]
            y1[i] = y1[i-1] + dt * dy1
            y2[i] = y2[i-1] + dt * dy2
        
        # EEG-like output
        return y0
```

### 2. Build Differential Causal Network

```python
class DifferentialCausalNetwork:
    """Differential causal network from EEG data."""
    
    def __init__(self, num_nodes, coupling_params=None):
        self.num_nodes = num_nodes
        self.nodes = [JansenRitModel() for _ in range(num_nodes)]
        self.coupling = coupling_params or np.zeros((num_nodes, num_nodes))
    
    def simulate(self, external_inputs, dt=0.001, duration=10):
        """
        Simulate network dynamics.
        
        Args:
            external_inputs: External input to each node
            dt: Time step
            duration: Duration (seconds)
        
        Returns:
            Network outputs (EEG-like signals from each node)
        """
        steps = int(duration / dt)
        outputs = np.zeros((self.num_nodes, steps))
        
        for node_idx in range(self.num_nodes):
            # Coupled inputs from other nodes
            coupled_input = np.zeros(steps)
            for other_idx in range(self.num_nodes):
                if self.coupling[node_idx, other_idx] > 0:
                    coupled_input += self.coupling[node_idx, other_idx] * outputs[other_idx]
            
            # Total input
            total_input = external_inputs[node_idx] + coupled_input
            
            # Simulate node
            outputs[node_idx] = self.nodes[node_idx].simulate(total_input, dt, duration)
        
        return outputs
```

### 3. Parameter Inference (Evolutionary Optimization)

```python
def chen_fliess_loss(params, observed_eeg, simulated_eeg):
    """
    Loss function based on Chen-Fliess expansion.
    
    Args:
        params: Network parameters to optimize
        observed_eeg: Observed EEG data
        simulated_eeg: Simulated EEG from model
    
    Returns:
        Loss value
    """
    # Chen-Fliess expansion approximation
    # Compare derivatives and Volterra kernels
    
    # First-order derivative match
    d1_obs = np.gradient(observed_eeg)
    d1_sim = np.gradient(simulated_eeg)
    loss1 = np.mean((d1_obs - d1_sim)**2)
    
    # Second-order derivative match
    d2_obs = np.gradient(d1_obs)
    d2_sim = np.gradient(d1_sim)
    loss2 = np.mean((d2_obs - d2_sim)**2)
    
    # Total loss
    return loss1 + 0.5 * loss2

def evolutionary_optimize(network, observed_eeg, generations=100, population_size=50):
    """
    Evolutionary algorithm for parameter inference.
    
    Args:
        network: DifferentialCausalNetwork
        observed_eeg: Observed EEG data
        generations: Number of generations
        population_size: Population size
    
    Returns:
        Optimized parameters
    """
    import random
    
    # Initialize population (coupling parameters)
    dim = network.num_nodes * network.num_nodes
    population = [np.random.rand(dim) for _ in range(population_size)]
    
    best_params = None
    best_loss = float('inf')
    
    for gen in range(generations):
        # Evaluate fitness
        fitness = []
        for params in population:
            # Set parameters
            network.coupling = params.reshape(network.num_nodes, network.num_nodes)
            
            # Simulate
            simulated = network.simulate(np.zeros(network.num_nodes))
            
            # Compute loss
            loss = chen_fliess_loss(params, observed_eeg[0], simulated[0])
            fitness.append(loss)
            
            if loss < best_loss:
                best_loss = loss
                best_params = params
        
        # Selection + Mutation
        sorted_indices = np.argsort(fitness)
        survivors = [population[i] for i in sorted_indices[:population_size//2]]
        
        # Crossover
        new_population = survivors.copy()
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(survivors, 2)
            child = (parent1 + parent2) / 2 + np.random.randn(dim) * 0.01
            new_population.append(child)
        
        population = new_population
    
    return best_params.reshape(network.num_nodes, network.num_nodes), best_loss
```

### 4. Group Comparison (Mixed-Effects Model)

```python
import scipy.stats as stats

def mixed_effects_comparison(group_params, control_params):
    """
    Compare parameters between groups using mixed-effects model.
    
    Args:
        group_params: Parameters for patient group (list of matrices)
        control_params: Parameters for control group
    
    Returns:
        Statistical comparison results
    """
    num_nodes = group_params[0].shape[0]
    results = {}
    
    # Compare each connection
    for i in range(num_nodes):
        for j in range(num_nodes):
            group_values = [p[i,j] for p in group_params]
            control_values = [p[i,j] for p in control_params]
            
            # t-test
            t_stat, p_value = stats.ttest_ind(group_values, control_values)
            
            if p_value < 0.05:
                results[f'connection_{i}_{j}'] = {
                    'group_mean': np.mean(group_values),
                    'control_mean': np.mean(control_values),
                    't_stat': t_stat,
                    'p_value': p_value,
                    'significant': True
                }
    
    return results
```

### 5. Epileptic Activity Analysis

```python
def track_epileptic_changes(pre_seizure_params, during_seizure_params):
    """
    Track parameter changes during epileptic activity.
    
    Args:
        pre_seizure_params: Network parameters before seizure
        during_seizure_params: Network parameters during seizure
    
    Returns:
        Change analysis
    """
    changes = during_seizure_params - pre_seizure_params
    
    analysis = {
        'excitatory_inhibitory_balance': np.sum(changes) / changes.size,
        'strongest_increase': np.argmax(changes),
        'strongest_decrease': np.argmin(changes),
        'connectivity_disruption': np.sum(np.abs(changes) > 0.1) / changes.size
    }
    
    return analysis
```

## Tools Used

- `numpy` - Numerical computations
- `scipy.stats` - Statistical tests
- `exec` - Run analysis scripts
- `read` - Load EEG data

## Example Use Cases

### 1. Simulate Single Node

```python
# Jansen-Rit model simulation
model = JansenRitModel()
input_signal = np.random.randn(10000) * 0.1
output = model.simulate(input_signal)
print(f"EEG-like output shape: {output.shape}")
```

### 2. Network Simulation

```python
# 3-node network
network = DifferentialCausalNetwork(num_nodes=3)
network.coupling = np.array([[0, 0.5, 0], [0, 0, 0.3], [0.2, 0, 0]])

outputs = network.simulate(np.zeros(3))
print(f"Network outputs: {outputs.shape}")
```

### 3. Parameter Inference

```python
# Optimize network parameters
observed_eeg = outputs  # Use observed data
best_params, loss = evolutionary_optimize(network, observed_eeg)
print(f"Best loss: {loss:.4f}")
print(f"Optimized coupling:\n{best_params}")
```

### 4. Epileptic Analysis

```python
# Track changes before/during seizure
pre_params = np.array([[0, 0.5, 0], [0, 0, 0.3], [0.2, 0, 0]])
during_params = np.array([[0, 0.8, 0], [0, 0, 0.1], [0.5, 0, 0]])

analysis = track_epileptic_changes(pre_params, during_params)
print(f"E/I balance change: {analysis['excitatory_inhibitory_balance']:.2f}")
print(f"Connectivity disruption: {analysis['connectivity_disruption']:.1%}")
```

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Construct Jansen-Rit Local Model

## Examples

### Example 1: Basic Application

**User:** I need to apply differential-dynamic-causal-nets - Differential Dynamic Causal Nets: Model Construction, Identification and Group Comparisons to my analysis.

**Agent:** I'll help you apply differential-dynamic-causal-nets. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for differential-dynamic-causal-nets?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- `ccep-causal-brain-network` - CCEP causal brain network
- `linear-structure-function-coupling` - Structure-function coupling
- `time-varying-brain-connectivity` - Time-varying connectivity

## References

- Zhang, J. (2026). "Differential Dynamic Causal Nets: Model Construction, Identification and Group Comparisons" arXiv:2601.21478v1 [q-bio.NC]

---

**Created:** 2026-03-29 16:05
**Author:** Aerial (from arXiv:2601.21478v1)