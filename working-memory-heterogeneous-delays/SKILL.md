---
name: working-memory-heterogeneous-delays
description: "Working memory implementation in recurrent spiking neural networks using heterogeneous synaptic delays. Each synapse has D=41 delay channels forming a weight tensor W∈R^(N×N×D), trained end-to-end with surrogate-gradient BPTT. Stores multiple temporal spike patterns with precise timing. Use for: SNN working memory, temporal pattern storage, delay-based computation. Keywords: working memory, SNN, heterogeneous delays, temporal patterns, surrogate gradient."
---

# Working Memory in Recurrent SNNs with Heterogeneous Synaptic Delays

## Overview

Implement working memory — the ability to store and recall precise temporal patterns of neural activity — in spiking neural networks (SNNs) using heterogeneous synaptic delays. Each synapse is equipped with D=41 delay channels, modeled as a weight tensor **W** ∈ ℝ^(N×N×D), trained end-to-end with surrogate-gradient backpropagation through time (BPTT). The network stores M arbitrary target spike patterns by representing each as a sequence of population vectors.

## Source Paper

- **Title:** Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays
- **Author:** Laurent U Perrinet
- **Published:** 2026
- **arXiv ID:** 2604.14096v1

## Key Contributions

1. **Heterogeneous Delay Architecture**: Each synapse has D=41 distinct delay channels, enabling the network to store temporal information in the delay structure rather than just weights
2. **Multi-Pattern Storage**: Network stores M arbitrary target spike patterns as sequences of population vectors, with precise temporal recall
3. **End-to-End Training**: Uses surrogate-gradient BPTT to jointly optimize weights and leverage delay diversity
4. **Biological Plausibility**: Matches biological finding that synaptic delays vary significantly across connections in real neural circuits

## Core Concepts

### Heterogeneous Delay Tensor

Instead of a standard weight matrix W ∈ ℝ^(N×N), the network uses a 3D weight tensor:

```
W[i, j, d] : connection from neuron j to neuron i with delay d
```

where d ∈ {0, 1, ..., D-1} and D=41 delay channels per synapse.

### Temporal Pattern Representation

Each target spike pattern is encoded as a sequence of population vectors:
```
P_m[t] ∈ {0,1}^N  for t = 0, ..., T-1
```
where N is the number of neurons and T is the pattern duration.

### Memory Storage Capacity

The network capacity scales with:
- Number of neurons N
- Number of delay channels D
- Pattern duration T
- Number of stored patterns M

### Working Memory Mechanism

1. **Encoding**: Target patterns are converted to spike sequences
2. **Storage**: Heterogeneous delays create multiple temporal pathways
3. **Recall**: Network reproduces stored patterns from partial cues
4. **Precision**: Exact timing is preserved through delay diversity

## Implementation

### LIF Neuron Model

```python
import torch
import torch.nn as nn
import numpy as np

class LIFNeuron(nn.Module):
    """Leaky Integrate-and-Fire neuron with surrogate gradient."""
    
    def __init__(self, N, tau_mem=20.0, tau_syn=5.0, v_threshold=1.0):
        super().__init__()
        self.N = N
        self.tau_mem = tau_mem
        self.tau_syn = tau_syn
        self.v_threshold = v_threshold
        
    def forward(self, current_input, v, s, i_syn):
        """
        Args:
            current_input: Input current (N,)
            v: Membrane potential (N,)
            s: Spike output (N,)
            i_syn: Synaptic current (N,)
        Returns:
            new_v, new_s, new_i_syn
        """
        # Synaptic current decay
        i_syn_new = i_syn * np.exp(-1/self.tau_syn) + current_input
        
        # Membrane potential update
        v_new = v * np.exp(-1/self.tau_mem) + i_syn_new * (1 - s)
        
        # Spike generation with surrogate gradient
        spike = self.surrogate_spike(v_new - self.v_threshold)
        
        # Reset after spike
        v_new = v_new * (1 - spike)
        
        return v_new, spike, i_syn_new
    
    def surrogate_spike(self, x, sigma=0.5):
        """Sigmoid surrogate gradient for spike function."""
        return torch.sigmoid(x / sigma)

class HeterogeneousDelaySNN(nn.Module):
    """Recurrent SNN with heterogeneous synaptic delays."""
    
    def __init__(self, N, D=41, T=50, tau_mem=20.0, tau_syn=5.0):
        super().__init__()
        self.N = N  # Number of neurons
        self.D = D  # Number of delay channels
        self.T = T  # Time steps
        self.tau_mem = tau_mem
        self.tau_syn = tau_syn
        
        # Weight tensor: W[i, j, d] - connection from j to i with delay d
        self.W = nn.Parameter(torch.randn(N, N, D) * 0.1)
        
        # Readout weights
        self.W_out = nn.Parameter(torch.randn(N, N) * 0.01)
        
        self.lif = LIFNeuron(N, tau_mem, tau_syn)
        
    def forward(self, target_patterns, num_epochs=1000, lr=0.01):
        """
        Train the network to store multiple temporal patterns.
        
        Args:
            target_patterns: (M, T, N) tensor of M target patterns
            num_epochs: Training iterations
            lr: Learning rate
        """
        M, T, N = target_patterns.shape
        optimizer = torch.optim.Adam(self.parameters(), lr=lr)
        
        for epoch in range(num_epochs):
            optimizer.zero_grad()
            
            # Forward pass through all patterns
            total_loss = 0
            for m in range(M):
                pattern = target_patterns[m]  # (T, N)
                loss = self._train_pattern(pattern)
                total_loss += loss
            
            total_loss.backward()
            optimizer.step()
            
            if epoch % 100 == 0:
                print(f"Epoch {epoch}: Loss = {total_loss.item():.4f}")
        
        return total_loss
    
    def _train_pattern(self, target):
        """Train on a single temporal pattern with surrogate gradient BPTT."""
        T, N = target.shape
        
        # Initialize states
        v = torch.zeros(N)
        s = torch.zeros(N)
        i_syn = torch.zeros(N)
        
        # Delay line buffers for each delay channel
        delay_buffers = torch.zeros(self.D, self.N, self.N)  # (D, N, N)
        
        total_loss = 0
        
        for t in range(T):
            # Compute input from all delay channels
            current_input = torch.zeros(N)
            for d in range(self.D):
                if d == 0:
                    # Instantaneous connection
                    current_input += torch.sum(self.W[:, :, d] * s, dim=1)
                else:
                    # Delayed connection from buffer
                    current_input += torch.sum(
                        self.W[:, :, d] * delay_buffers[d-1], dim=1
                    )
            
            # Update delay buffers (shift)
            for d in range(self.D-1, 0, -1):
                delay_buffers[d] = delay_buffers[d-1]
            delay_buffers[0] = torch.outer(s, s)
            
            # Neuron dynamics
            v, s, i_syn = self.lif(current_input, v, s, i_syn)
            
            # Compute loss against target
            loss = nn.BCEWithLogitsLoss()(v, target[t])
            total_loss += loss
        
        return total_loss / T
    
    def recall(self, cue_pattern, num_steps=50):
        """Recall stored pattern from partial cue."""
        T = num_steps
        N = self.N
        
        v = torch.zeros(N)
        s = torch.zeros(N)
        i_syn = torch.zeros(N)
        delay_buffers = torch.zeros(self.D, self.N, self.N)
        
        spike_train = []
        
        for t in range(T):
            # Apply cue in first few steps
            if t < cue_pattern.shape[0]:
                s = cue_pattern[t]
            
            current_input = torch.zeros(N)
            for d in range(self.D):
                if d == 0:
                    current_input += torch.sum(self.W[:, :, d] * s, dim=1)
                else:
                    current_input += torch.sum(
                        self.W[:, :, d] * delay_buffers[d-1], dim=1
                    )
            
            for d in range(self.D-1, 0, -1):
                delay_buffers[d] = delay_buffers[d-1]
            delay_buffers[0] = torch.outer(s, s)
            
            v, s, i_syn = self.lif(current_input, v, s, i_syn)
            spike_train.append(s.detach().clone())
        
        return torch.stack(spike_train)

# Usage Example
N = 100  # Neurons
D = 41   # Delay channels
T = 50   # Time steps
M = 5    # Number of patterns to store

# Generate random target patterns
target_patterns = torch.randint(0, 2, (M, T, N)).float()

# Create and train network
model = HeterogeneousDelaySNN(N=N, D=D, T=T)
model(target_patterns, num_epochs=500, lr=0.001)

# Recall test
cue = target_patterns[0, :5]  # First 5 steps as cue
recalled = model.recall(cue, num_steps=T)
```

### Memory Capacity Analysis

```python
def analyze_capacity(N_values, D_values, pattern_sparsity=0.1):
    """
    Analyze memory capacity as function of N and D.
    
    Returns capacity curves for different configurations.
    """
    import matplotlib.pyplot as plt
    
    results = {}
    
    for N in N_values:
        for D in D_values:
            # Theoretical capacity estimate
            # Each delay channel provides ~N^2 degrees of freedom
            # Capacity scales with N^2 * D
            capacity = (N**2 * D * pattern_sparsity) / (N * 50)  # patterns
            
            results[(N, D)] = {
                'N': N,
                'D': D,
                'estimated_capacity': capacity,
                'dof': N**2 * D
            }
    
    return results

# Analyze different configurations
configs = analyze_capacity(
    N_values=[50, 100, 200, 500],
    D_values=[1, 10, 20, 41, 100]
)

for (N, D), info in sorted(configs.items(), key=lambda x: x[1]['dof']):
    print(f"N={N}, D={D}: DoF={info['dof']}, "
          f"Capacity≈{info['estimated_capacity']:.1f} patterns")
```

### Biological Delay Distribution Modeling

```python
def generate_biological_delays(N, distribution='lognormal'):
    """
    Generate biologically-plausible delay distributions.
    
    In biological networks, delays follow skewed distributions
    with most delays short and a long tail of slow connections.
    """
    if distribution == 'lognormal':
        # Lognormal distribution as observed in cortex
        delays = np.random.lognormal(mean=1.5, sigma=0.8, size=N*N)
        delays = np.clip(delays, 0, 40).astype(int)
    elif distribution == 'exponential':
        # Exponential decay
        delays = np.random.exponential(scale=10, size=N*N)
        delays = np.clip(delays, 0, 40).astype(int)
    elif distribution == 'uniform':
        delays = np.random.randint(0, 41, size=N*N)
    
    return delays.reshape(N, N)

# Compare distributions
N = 100
delays_lognormal = generate_biological_delays(N, 'lognormal')
delays_exponential = generate_biological_delays(N, 'exponential')

print(f"Lognormal delays: mean={delays_lognormal.mean():.1f}, "
      f"std={delays_lognormal.std():.1f}")
print(f"Exponential delays: mean={delays_exponential.mean():.1f}, "
      f"std={delays_exponential.std():.1f}")
```

## Practical Applications

### 1. Temporal Pattern Memory
Store and recall precise spike timing patterns — useful for sequence learning, motor pattern generation, and temporal prediction.

### 2. Working Memory Tasks
Implement delay-period activity in prefrontal cortex models, maintaining information across seconds-long gaps.

### 3. Sequence Generation
Generate complex temporal sequences (music, speech patterns, motor commands) from compact stored representations.

### 4. Neuromorphic Hardware
Heterogeneous delays map naturally to neuromorphic chips with configurable routing, enabling efficient temporal processing.

## Comparison with Alternatives

| Method | Temporal Precision | Storage Capacity | Biological Plausibility |
|--------|-------------------|-----------------|------------------------|
| Standard RNN | Low | Moderate | Low |
| LSTM/GRU | Low | High | Low |
| Delay-line SNN | High | Moderate | Moderate |
| **Heterogeneous Delay SNN** | **High** | **High** | **High** |

## Limitations

1. **Memory Complexity**: O(N²×D) parameters can be large for big networks
2. **Training Time**: BPTT with delays requires longer backpropagation horizons
3. **Delay Channel Selection**: Optimal D depends on task temporal scale
4. **Gradient Vanishing**: Long delays may cause gradient issues during training

## Related Work

- **STDP-based learning**: Alternative training method using spike-timing dependent plasticity
- **Reservoir computing**: Fixed random weights with trainable readout
- **Liquid state machines**: Similar temporal processing with random recurrent networks
- **Echo state networks**: Reservoir computing with specific spectral radius constraints

## Activation Keywords
- working memory SNN
- heterogeneous synaptic delays
- temporal pattern storage
- surrogate gradient BPTT
- recurrent spiking neural network
- delay-based memory
- Laurent Perrinet SNN
