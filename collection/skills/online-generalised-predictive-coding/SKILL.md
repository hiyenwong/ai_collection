---
name: online-generalised-predictive-coding
description: "Online Generalised Predictive Coding via Dynamic Expectation Maximisation (ODEM) for biologically plausible online learning. Activation: predictive coding, online learning, DEM, dynamic expectation maximisation, active inference."
---

# Online Generalised Predictive Coding

> Online Dynamic Expectation Maximisation (ODEM) — biologically plausible framework for online predictive coding and parameter estimation.

## Metadata
- **Source**: arXiv:2605.04242
- **Authors**: Mehran H. Z. Bazargani, Szymon Urbas, Adeel Razi, Thomas Brendan Murphy, Karl Friston
- **Published**: 2026-05-07
- **Categories**: stat.ML, cs.LG, q-bio.NC

## Core Methodology

### Online DEM (ODEM)
- Extends Generalised Predictive Coding to online/sequential setting
- Simultaneous state and parameter estimation via variational inference
- Biologically plausible update rules compatible with neural implementation
- Handles non-stationary environments with adaptive learning rates

### Technical Framework
1. Generalised coordinates of motion for temporal derivatives
2. Variational free energy minimisation online
3. Expectation step: update posterior over hidden states
4. Maximisation step: update model parameters
5. Recursive updates with forgetting factor for non-stationarity

## Applications
- Online brain state tracking
- Adaptive neural decoding
- Real-time fMRI/EEG analysis
- Active inference agents

## Pitfalls
- Requires careful tuning of learning rates
- Convergence guarantees depend on model complexity
- Computational cost scales with model dimensionality

## Related Skills
- free-energy-moe-routing
- autopoiesis-self-evolving-systems
- brain-digital-twins-execution-semantics-v3
