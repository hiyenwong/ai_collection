---
name: developmental-minimal-neural-circuits
description: Developmental generation of minimal neural circuits from structure-function relationships. Shows how network structure performs computation through developmental processes. Trigger words: developmental neural circuits, structure computation, minimal circuits, neural wiring, structure-function.
---

# Developmental Minimal Neural Circuits

## Paper Reference
- **arXiv**: [2604.15143v1](https://arxiv.org/abs/2604.15143)
- **Authors**: Duan Zhou et al.
- **Published**: 2026-04-16
- **Citations**: 0

## Core Insight

Neural circuit structure itself encodes computation. Through developmental processes that grow and prune connections based on functional demands, minimal circuits emerge performing complex computations with few neurons but highly specific connectivity.

## Key Mechanism

1. **Structure IS Computation**: Wiring pattern, not just weights, determines function
2. **Developmental Growth**: Circuits grow through activity-dependent processes
3. **Minimal Sufficiency**: Smallest circuit that performs a task is optimal
4. **Emergent Specialization**: Specific connectivity patterns emerge for specific computations

## Implementation Pattern

```python
import numpy as np

class DevelopmentalCircuit:
    def __init__(self, n_max=50):
        self.n_max = n_max
        self.active_neurons = 2
        self.adjacency = np.zeros((n_max, n_max))
        self.neuron_types = np.zeros(n_max)
    
    def developmental_step(self, input_pattern, target_output, lr=0.01):
        n = self.active_neurons
        activity = self._run(input_pattern)
        output = activity[-1]
        error = target_output - output
        for i in range(n):
            for j in range(n):
                if self.adjacency[i,j] != 0:
                    self.adjacency[i,j] += lr * activity[i] * activity[j] * np.sign(error)
        self.adjacency[np.abs(self.adjacency) < 0.001] = 0
        if np.abs(error) > 0.5 and self.active_neurons < self.n_max:
            self._add_neuron()
        return np.abs(error)
    
    def _run(self, inp, steps=50):
        n = self.active_neurons
        activity = np.zeros(n); activity[:len(inp)] = inp
        for _ in range(steps):
            activity = 0.9 * activity + 0.1 * np.tanh(self.adjacency[:n,:n] @ activity)
        return activity
    
    def _add_neuron(self):
        idx = self.active_neurons
        self.neuron_types[idx] = np.random.choice([0, 1])
        for j in range(idx):
            if np.random.random() < 0.1:
                s = 1 if self.neuron_types[idx] == 0 else -1
                self.adjacency[idx, j] = s * np.random.random() * 0.1
            if np.random.random() < 0.1:
                s = 1 if self.neuron_types[j] == 0 else -1
                self.adjacency[j, idx] = s * np.random.random() * 0.1
        self.active_neurons += 1
```

## Applications

- Understanding developmental brain wiring
- Minimal circuit design for specific computations
- Neural architecture search inspired by development
- Neurodevelopmental disorder modeling

## Related Skills

- [[developmental-minimal-neural-circuits]]
- [[brain-inspired-neural-cellular-automata]]
- [[morphsnn-structural-plasticity]]
