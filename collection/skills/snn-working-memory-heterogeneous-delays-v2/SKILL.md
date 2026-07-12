---
name: snn-working-memory-heterogeneous-delays-v2
version: v1.0.0
last_updated: 2026-04-17
description: "Working memory implementation in recurrent spiking neural networks with heterogeneous synaptic delays. Models synapses with multiple delays as weight tensors, trained with surrogate-gradient backpropagation through time. Enables precise temporal pattern storage and recall for energy-efficient neuromorphic edge deployment. Activation: working memory SNN, spiking neural network memory, heterogeneous delays, temporal pattern storage, recurrent SNN."
---

# SNN Working Memory with Heterogeneous Synaptic Delays

Working memory implementation for Spiking Neural Networks (SNNs) using heterogeneous synaptic delays to store and recall precise temporal patterns of neural activity.

## Overview

This methodology addresses the challenge of working memory in SNNs - the ability to store and recall precise temporal patterns. The approach models each synapse with multiple delays as a weight tensor, enabling the network to store arbitrary spike patterns through sequential chains of overlapping Spiking Motifs.

**Key Innovation:** Heterogeneous synaptic delays provide an efficient substrate for working memory in SNNs, enabling energy-efficient neuromorphic edge deployment.

## Activation Keywords

- working memory SNN
- spiking neural network memory
- heterogeneous delays
- temporal pattern storage
- recurrent SNN
- spiking motifs
- surrogate gradient BPTT
- neuromorphic memory
- SNN working memory

## Core Methodology

### Architecture

**Network Structure:**
- Recurrent SNN with $N$ neurons
- Each synapse equipped with $D$ delays (typically $D = 41$)
- Weight tensor: $\mathbf{W} \in \mathbb{R}^{N \times N \times D}$
- Trained end-to-end with surrogate-gradient backpropagation through time

### Spiking Motifs

**Pattern Representation:**
- Each pattern represented as sequential chain of overlapping Spiking Motifs
- Spiking Motif: Contiguous window of length $D$ that uniquely predicts spikes at next time step
- Multiple patterns ($M$) stored simultaneously

### Training Process

**Surrogate Gradient BPTT:**
1. Initialize network with $N$ recurrent neurons
2. Define $M$ target spike patterns
3. Train using surrogate-gradient through time
4. Optimize for pattern storage and recall

**Pattern Recall Dynamics:**
- Recall emerges first near clamped initialization window
- Propagates forward in time through the motif chain
- Achieves perfect recall (F1 = 1.0) on synthetic benchmarks

## Implementation Parameters

### Default Configuration

```python
config = {
    "neurons": 512,           # Network size (N)
    "delays": 41,             # Number of delay steps (D)
    "patterns": 16,           # Number of patterns to store (M)
    "time_steps": 1000,       # Simulation duration (T)
    "learning_rate": 0.001,   # Training learning rate
    "surrogate": "atan"       # Surrogate gradient function
}
```

### Performance Metrics

**Benchmark Results:**
- Mean F1 Score: 1.0 (perfect recall)
- Pattern capacity: 16 patterns with 512 neurons
- Temporal resolution: 1000 time steps
- Training: Converges with surrogate-gradient BPTT

## Workflow

### Step 1: Network Initialization

```python
# Initialize recurrent SNN with heterogeneous delays
network = RecurrentSNN(
    n_neurons=config["neurons"],
    n_delays=config["delays"]
)
```

### Step 2: Pattern Encoding

```python
# Encode target patterns as spiking motifs
for pattern in target_patterns:
    motifs = extract_spiking_motifs(pattern, window_size=config["delays"])
    network.store_pattern(motifs)
```

### Step 3: Training

```python
# Train with surrogate-gradient BPTT
trainer = SurrogateGradientBPTT(
    network=network,
    optimizer=Adam(lr=config["learning_rate"])
)
trainer.train(target_patterns, epochs=100)
```

### Step 4: Pattern Recall

```python
# Initialize with seed pattern
network.clamp(initial_window)
# Let dynamics propagate through motif chain
recalled_pattern = network.simulate(duration=config["time_steps"])
```

## Applications

### Primary Use Cases

1. **Neuromorphic Edge Computing**
   - Energy-efficient temporal pattern storage
   - Edge devices with limited power budgets
   - Real-time pattern recall

2. **Brain-Computer Interfaces**
   - Neural signal pattern storage
   - Temporal sequence learning
   - Online memory systems

3. **Robotic Control**
   - Motor pattern learning
   - Sequence generation
   - Temporal task encoding

## Technical Details

### Surrogate Gradient Functions

Common choices for surrogate gradients:
- **Arctan:** Smooth, biologically plausible
- **Sigmoid:** Bounded output range
- **Fast Sigmoid:** Computationally efficient

### Delay Distribution

**Heterogeneous Delays:**
- Linear spacing: $\tau_d = d \cdot \Delta t$ for $d = 1, ..., D$
- Logarithmic spacing for multi-timescale memory
- Learnable delays (advanced)

### Pattern Capacity

**Scaling Properties:**
- Theoretical capacity: $O(N \cdot D)$ patterns
- Practical limit depends on pattern overlap
- Sparse patterns enable higher capacity

## Advantages

1. **Energy Efficiency:** Event-driven computation reduces power consumption
2. **Temporal Precision:** Delay lines enable precise timing
3. **Biological Plausibility:** Inspired by synaptic delay lines in cortex
4. **Online Learning:** Compatible with neuromorphic hardware

## Limitations

1. **Training Complexity:** Surrogate gradient BPTT requires careful tuning
2. **Pattern Interference:** Similar patterns may interfere
3. **Fixed Delays:** Standard implementation uses fixed delay values
4. **Hardware Requirements:** Best performance on neuromorphic hardware

## Related Work

- **Delay-embedded Reservoir Computing:** Uses fixed random delays
- **Spiking Neural Networks:** Standard SNNs without explicit memory
- **Long Short-Term Memory (LSTM):** Analog counterpart in ANNs
- **Liquid State Machines:** Reservoir computing with delays

## References

- Paper: "Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays"
- arXiv: 2604.14096v1
- Published: 2026-04-15
- Author: Laurent U Perrinet
- Categories: q-bio.NC

## Implementation Notes

For practical implementation:
1. Use spiking frameworks like SpikingJelly or Norse
2. Implement custom surrogate gradient functions
3. Consider neuromorphic hardware (Loihi, TrueNorth) for deployment
4. Optimize delay distribution for target application
