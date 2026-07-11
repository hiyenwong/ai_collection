# Dendritic In-Context Learning (DendriCL) — arXiv: 2607.02289

## Paper Summary
DendriCL: single-layer compartmental spiking neural network implementing in-context learning via dendritic subthreshold dynamics. Proves ICL requires neither attention, depth, nor inference-time synaptic plasticity.

## Key Results

### The Breakthrough
- Subthreshold dynamics of a **single dendritic compartment** implement complete online LMS (Widrow-Hoff) algorithm
- ICL does NOT require: attention mechanisms, architectural depth, inference-time plasticity
- Seed-stable at super-dimensional Garg-2022 benchmark (where dense Transformers fail with grokking-style instability)
- Linear probe recovers reference online-LMS trajectory directly from apical membrane at R² = 0.93

### Prior SNN Failure Mode
- Previous SNN designs failed Garg-2022 at non-trivial task dimensions
- Root cause: routed adaptation through inference-time synaptic plasticity, treating dendrites as passive conduits for error/teacher signals
- Correction: dendrites are the computational substrate

### Architecture
- Single-layer compartmental spiking architecture
- Apical recurrence structurally identical to leaky online Widrow-Hoff LMS
- Dynamics-based update collapses ICL architectural depth to a single layer
- No explicit weight update needed — the dynamics ARE the algorithm

## Implementation Pattern
```
For each time step t:
  1. Compute dendritic subthreshold potential from apical recurrence
  2. Generate spike if threshold crossed  
  3. Dendritic dynamics automatically implement: w ← w + η·e·x
  4. No explicit backprop or plasticity rules needed
```
