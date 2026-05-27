---
name: braindyn-sheaf-neural-ode
description: "BrainDyn: A Sheaf Neural ODE framework for modeling continuous-time brain dynamics on structured graphs. Combines LSTM stalks with sheaf Laplacian message passing and neural ODE evolution. Apply when: brain dynamics modeling, fMRI/EEG forecasting, generative brain models, neural ODEs, sheaf theory, brain graph networks, perturbation prediction, synthetic brain data. Keywords: sheaf neural ODE, brain dynamics, fMRI modeling, EEG forecasting, brain graphs, sheaf Laplacian, neural ODE, brain regions, generative dynamics."
---

# BrainDyn: Sheaf Neural ODE for Generative Brain Dynamics

A novel framework combining sheaf theory, neural ODEs, and structured brain graphs for continuous-time brain dynamics modeling.

## Overview

BrainDyn addresses the gap between LLM/RNNs (ignore anatomical organization) and simple graph networks (insufficient expressiveness for brain-like dynamics) by introducing:

1. **Sheaf Neural ODE**: Continuous-time dynamics on structured brain graphs
2. **LSTM Stalks**: Encode recent activity history per brain region
3. **Sheaf Laplacian**: Facilitate message passing between neuronal units

## Core Architecture

### Temporal Encoding
- **LSTM over Sliding Windows**: Produce hidden states (stalks) per brain region
- **Restriction Maps**: Project stalks through learnable maps to edge-specific shared spaces
- **Activity History**: Capture recent dynamics for each region

### Message Passing
- **Sheaf Laplacian**: Characterize discrepancies between neighboring nodes in shared spaces
- **Edge-Specific Spaces**: Different spaces for different connections
- **Expressive Dynamics**: Beyond simple message passing rules

### Continuous Evolution
- **Neural ODE**: Govern continuous-time evolution of neuronal activity
- **Smooth Dynamics**: Natural temporal progression
- **Brain-Region Aligned**: Components align with anatomical organization

## Key Innovations

1. **Sheaf Theory Integration**: Mathematical framework for multi-space consistency
2. **Anatomical Alignment**: Brain region correspondence maintained
3. **Continuous-Time Modeling**: Natural temporal dynamics (vs discrete steps)
4. **Multi-Modality Support**: fMRI, EEG, simulated spiking data

## Applications

### Data Modalities
- **Resting-state fMRI**: PNC dataset
- **Scalp EEG**: Focal epilepsy (TUSZ dataset)
- **Spiking Network**: NEST simulator output

### Downstream Tasks
- Brain activity forecasting
- In silico perturbation prediction
- Synthetic brain data generation
- Brain transient analysis
- Dynamics inference

## Implementation

### Model Components
```python
# Conceptual architecture
class BrainDyn:
    - LSTMEncoder: Per-region activity encoding
    - RestrictionMaps: Learnable stalk projections
    - SheafLaplacian: Multi-space message passing
    - NeuralODE: Continuous dynamics solver
```

### Training Approach
- Supervised forecasting across modalities
- Representation learning for downstream tasks
- Perturbation prediction evaluation

## Mathematical Framework

### Sheaf Structure
- **Stalks**: Hidden states per brain region (LSTM outputs)
- **Restriction Maps**: Learnable transformations to edge spaces
- **Sheaf Laplacian**: Aggregates discrepancies across edges
- **Neural ODE**: dx/dt = f(x, L_sheaf, θ)

### Expressiveness
- Captures region-specific dynamics
- Maintains anatomical structure
- Enables complex temporal patterns
- Supports perturbation analysis

## Biological Validity

- Brain region alignment
- Multi-modal applicability (fMRI, EEG, spikes)
- Continuous temporal dynamics
- Perturbation prediction capability

## Reference

**Paper**: "BrainDyn: A Sheaf Neural ODE for Generative Brain Dynamics"
**arXiv ID**: 2605.19324
**Authors**: Siddharth Viswanath, Panayiotis Ketonis, Chen Liu, Michael Perlmutter, Dhananjay Bhaskar, Smita Krishnaswamy
**Published**: 2026-05-19
**Category**: cs.LG (Machine Learning)

## Activation Keywords

`sheaf neural ODE`, `brain dynamics`, `fMRI modeling`, `EEG forecasting`, `brain graphs`, `sheaf Laplacian`, `neural ODE`, `brain regions`, `generative dynamics`, `brain transients`, `perturbation prediction`, `LSTM stalks`, `continuous dynamics`, `anatomical alignment`
