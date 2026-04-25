---
name: hippocampal-predictive-autoencoder-place-time-cells
description: "Hippocampal CA3 predictive autoencoder RNN methodology unifying place cells and time cells from a single recurrent network. Activation triggers: hippocampus, place cell, time cell, CA3, predictive autoencoder, spatial navigation, temporal coding."
---

# Hippocampal Predictive Autoencoder: Unified Place Cells and Time Cells

> A single RNN modeling CA3 as a predictive autoencoder generates both place cells and time cells from two dynamical regimes, suggesting a shared origin for spatial and temporal coding in the hippocampus.

## Metadata
- **Source**: arXiv:2604.00036
- **Authors**: Qiaorong S. Yu, Zhaoze Wang, Vijay Balasubramanian
- **Published**: 2026-03-22
- **Categories**: q-bio.NC, cs.AI, cs.LG, cs.NE, physics.bio-ph

## Core Methodology

### Key Innovation
Unifies hippocampal place cells and time cells — traditionally modeled with separate mechanisms (continuous attractors vs leaky integrators) — as two dynamical regimes of a single CA3 predictive autoencoder RNN.

### Technical Framework

1. **CA3 Predictive Autoencoder**: Recurrent neural network trained to reconstruct missing/occluded portions of input experience vectors
2. **Dual Input Modes**:
   - **Spatial patterns**: Location-specific activity sampled during environmental traversal → generates stable attractor-like place fields
   - **Temporal patterns**: Correlated activity pairs separated by "void" intervals → produces sequentially broadened fields (time cells)
3. **Smooth Transition**: Hidden units transition smoothly between time cell-like and place cell-like representations by varying spatio-temporal input patterning

### Network Architecture
- RNN with recurrent connections modeling CA3 auto-associative memory
- Input: simulated partially occluded "experience vectors"
- Training objective: reconstruct missing input (predictive coding)
- Hidden units develop either place-like or time-like tuning depending on input statistics

## Implementation Guide

### Prerequisites
- Python 3.x with PyTorch or JAX
- NumPy, SciPy for analysis

### Step-by-Step
1. Define experience vector generator with spatial and temporal modes
2. Implement CA3 RNN autoencoder with recurrent hidden state
3. Train on spatial navigation data → observe place field emergence
4. Train on temporal sequence data → observe time cell emergence
5. Analyze hidden unit tuning curves for place/time selectivity

### Code Example
```python
import torch
import torch.nn as nn

class CA3PredictiveAutoencoder(nn.Module):
    """Minimal CA3 predictive autoencoder for place/time cell emergence."""
    def __init__(self, input_dim, hidden_dim):
        super().__init__()
        self.encoder = nn.Linear(input_dim, hidden_dim)
        self.rnn = nn.RNN(hidden_dim, hidden_dim, batch_first=True)
        self.decoder = nn.Linear(hidden_dim, input_dim)
    
    def forward(self, x, hidden=None):
        # x: (batch, seq_len, input_dim) with occluded portions
        encoded = torch.relu(self.encoder(x))
        recurrent_out, hidden = self.rnn(encoded, hidden)
        reconstructed = self.decoder(recurrent_out)
        return reconstructed, hidden, recurrent_out  # recurrent_out for tuning analysis

# Training: reconstruct occluded experience vectors
# Spatial mode: location-specific patterns → place cells
# Temporal mode: correlated pairs with void intervals → time cells
```

## Applications
- **Computational neuroscience**: Unified model of hippocampal spatial-temporal coding
- **Brain-inspired AI**: Single network architecture for spatio-temporal representation learning
- **Robotics navigation**: Place/time cell representations for autonomous agents
- **Memory models**: Understanding how episodic memory encodes when-and-where information

## Key Findings
1. Place cells emerge as stable attractors during spatial navigation training
2. Time cells emerge as sequentially broadened fields during temporal training
3. Hidden units smoothly transition between regimes — not distinct cell types
4. Suggests shared neural substrate with task-driven differentiation

## Pitfalls
- Model assumes CA3 can be approximated as autoencoder — real CA3 has more complex circuitry
- Experience vectors are simplified abstractions of real sensory input
- Continuous attractor dynamics may not fully capture place cell remapping phenomena

## Related Skills
- hippocampal-phase-native-coding
- hippocampal-reactivation-memory-consolidation
- learning-hippo-biologically-detailed-ca3
