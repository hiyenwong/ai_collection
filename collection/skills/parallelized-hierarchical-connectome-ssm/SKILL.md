---
name: parallelized-hierarchical-connectome-ssm
description: "Parallelized Hierarchical Connectome (PHC) framework upgrading temporal State-Space Models (SSMs) into spatiotemporal recurrent networks. Maps SSM diagonal core to Neuron Layer and inter-neuronal communication to Synapse Layer, enabling parallel-scan-based brain-scale network simulation with O(T log T) complexity. Use when: brain-scale neural network simulation, spatiotemporal SSMs, connectome-constrained neural modeling, parallel scan recurrent networks, spiking SSMs, or efficient long-sequence neural dynamics modeling."
version: 1.0.0
---

# Parallelized Hierarchical Connectome (PHC)

Spatiotemporal recurrent framework that upgrades temporal-only SSMs into brain-scale parallel-scan networks.

## Core Innovation

Standard SSMs (Mamba, S4) only support temporal recurrence — no lateral/feedback connections within a timestep. PHC adds:
- **Neuron Layer**: Maps diagonal SSM core to individual neurons
- **Synapse Layer**: Encodes inter-neuronal communication (lateral + feedback)
- **Parallel Scan**: Maintains O(T log T) efficiency despite added recurrence

## Architecture
```python
def phc_layer(x, neurons, synapses):
    """PHC: Neuron + Synapse parallel processing."""
    # Neuron: diagonal SSM per neuron
    neuron_states = parallel_scan(neurons.diagonal, x)
    
    # Synapse: lateral/feedback communication
    synapse_input = synapses @ neuron_states
    
    # Combined output
    return neuron_states + synapse_input
```

## Efficiency
- Time: O(T log T) via parallel scan (vs O(T·N²) for standard RNN)
- Space: O(T·N) for state storage
- Brain-scale: supports 10K+ neuron simulations

## Connectome Integration
```python
def build_phc_from_connectome(adjacency):
    """Construct PHC from structural connectome matrix."""
    neurons = np.diag(adjacency.sum(axis=1))  # Self-connection strengths
    synapses = adjacency - np.diag(np.diag(adjacency))  # Lateral only
    return neurons, synapses
```

## Applications
- Whole-brain simulation with structural constraints
- Long neural sequence modeling (EEG, calcium imaging)
- Connectome-based disease modeling
- Spiking extensions via event-driven parallel scan

## Activation Keywords
- PHC framework
- parallelized connectome
- spatiotemporal SSM
- brain-scale SSM
- parallel scan neural network
- connectome SSM
- 并行化连接组

## References
- Chiang, "Parallelized Hierarchical Connectome: A Spatiotemporal Recurrent Framework for Spiking State-Space Models", arXiv:2604.01295, 2026
