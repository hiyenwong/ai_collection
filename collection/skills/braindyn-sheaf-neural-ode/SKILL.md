---
id: braindyn-sheaf-neural-ode
title: BrainDyn: Sheaf Neural ODE for Generative Brain Dynamics
description: BrainDyn: Sheaf Neural ODE methodology for continuous-time dynamics on structured brain graphs. Combines LSTM history encoding, sheaf Laplacian message passing, and neural ODEs for brain-like generative dynamics across fMRI, EEG, and spike train modalities.
tags:
  - brain-dynamics
  - sheaf-neural-ode
  - generative-model
  - fmri
  - eeg
  - spiking-network
  - computational-neuroscience
  - graph-neural-networks
  - continuous-time
  - brain-modeling
arxiv: "2605.19324"
authors: "Siddharth Viswanath, Panayiotis Ketonis, Chen Liu, Michael Perlmutter, Dhananjay Bhaskar, Smita Krishnaswamy"
published: "2025-05-25"
---

# BrainDyn: Sheaf Neural ODE for Generative Brain Dynamics

## Overview

BrainDyn introduces a **Sheaf Neural Ordinary Differential Equation (Neural ODE)** model for continuous-time neural dynamics on anatomically structured brain graphs. It addresses the key limitation of existing models: LLMs/RNNs ignore anatomical organization; graph networks use overly simple message passing rules.

**Core Innovation**: Combining sheaf theory with neural ODEs to achieve expressive, structure-aware brain dynamics generation.

**arXiv**: 2605.19324 | Published: 2025-05-25

## Core Architecture

### 1. Stalk Construction (LSTM History Encoding)
```python
# For each brain region r, encode recent activity history
hidden_state_r = LSTM(activity_history_r[-T:])  # stalk s_r ∈ R^d
```

Each brain region's recent temporal activity window → LSTM → hidden state (stalk in sheaf terminology).

### 2. Restriction Maps (Learnable Edge Projections)
```python
# Project node stalks into edge-specific shared spaces
# For edge (u, v), learnable maps F_uv, F_vu
shared_u = F_uv @ stalk_u  # project node u into edge (u,v) space
shared_v = F_vu @ stalk_v  # project node v into edge (u,v) space
```

Restriction maps project neighboring nodes into common edge spaces for comparison.

### 3. Sheaf Laplacian (Discrepancy-Based Message Passing)
```python
# Sheaf coboundary operator δ measures discrepancies
discrepancy_uv = shared_u - shared_v  # in shared edge space
# Sheaf Laplacian: Δ = δᵀδ
# Message to node u from edge (u,v):
message_u += F_uv.T @ discrepancy_uv
```

The sheaf Laplacian captures directional, edge-specific feature discrepancies — more expressive than standard graph Laplacian.

### 4. Neural ODE Evolution
```python
# Continuous-time dynamics governed by neural ODE
def dynamics(t, state):
    messages = compute_sheaf_laplacian_messages(state)
    return neural_net(torch.cat([state, messages], dim=-1))

# Integrate using ODE solver (e.g., dopri5)
trajectory = odeint(dynamics, initial_state, time_points)
```

### Full BrainDyn Forward Pass
```python
class BrainDyn(nn.Module):
    def __init__(self, n_regions, hidden_dim, edge_dim, time_steps):
        self.lstm = nn.LSTM(1, hidden_dim, batch_first=True)
        self.restriction_maps = nn.ParameterDict(...)  # per-edge maps
        self.ode_func = ODEFunc(hidden_dim)
        
    def forward(self, activity_history, connectome):
        # 1. Encode history per region
        stalks = {r: self.lstm(activity_history[:, :, r])[0][:, -1] 
                  for r in range(n_regions)}
        
        # 2. Sheaf Laplacian message passing
        sheaf_messages = self.compute_sheaf_messages(stalks, connectome)
        
        # 3. Neural ODE evolution
        initial = torch.stack([stalks[r] for r in range(n_regions)], dim=1)
        trajectory = odeint(self.ode_func, initial, self.time_points)
        
        return trajectory
```

## Key Concepts

### Sheaf Theory Applied to Brain Networks
- **Stalk**: Vector space attached to each node (brain region) — represents local dynamics state
- **Restriction maps**: Linear maps encoding how neighboring regions "see" each other in a common edge space
- **Sheaf Laplacian**: Generalized Laplacian capturing local consistency between neighboring nodes
- **Coboundary**: Measures how much neighboring nodes disagree in shared edge spaces

### Why Sheaves for Brain Networks?
| Standard Graph | Sheaf Graph |
|---|---|
| Single shared feature space | Edge-specific shared spaces |
| Symmetric message passing | Asymmetric, direction-aware |
| Global Laplacian | Local restriction map learning |
| Less expressive | More expressive for heterogeneous regions |

## Applications & Datasets

### 1. Resting-State fMRI (PNC Dataset)
- **Task**: Forecast future BOLD activity from past
- **Graph**: Structural/functional connectivity atlas
- **Result**: Strong forecasting + supports in-silico perturbation

### 2. Scalp EEG with Focal Epilepsy (TUSZ Dataset)
- **Task**: Continuous-time EEG dynamics generation
- **Challenge**: Highly non-stationary, seizure vs. non-seizure
- **Result**: Cross-modal generalization of sheaf ODE framework

### 3. NEST Spiking Network Simulator
- **Task**: Predict population-level spike dynamics
- **Advantage**: Ground truth available from simulator
- **Result**: Validates generative accuracy

## Use Cases

### Generate Synthetic Brain Data
```python
# Given initial brain state and connectome
synthetic_activity = braindyn.generate(
    initial_state=resting_baseline,
    connectome=subject_structural_connectivity,
    duration=300  # 300 time steps
)
```

### In Silico Perturbation Prediction
```python
# Test what happens if region X is perturbed
perturbed_activity = braindyn.forward(
    activity_history=baseline_history,
    perturbation={region_X: +2.0}  # stimulation
)
delta = perturbed_activity - baseline_activity
```

### Brain Dynamics Inference
```python
# Infer underlying generative dynamics from recordings
latent_trajectory = braindyn.encode(observed_fmri)
# Analyze sheaf restriction maps for connectivity insights
attention_weights = braindyn.get_restriction_map_weights()
```

## When to Use This Skill

- Generating realistic synthetic brain activity (fMRI/EEG/spikes)
- Modeling continuous-time brain dynamics with anatomical structure
- In-silico brain stimulation/perturbation experiments
- Cross-modal brain dynamics generalization
- Building digital brain twins
- Comparing brain dynamics across conditions (rest vs. task, healthy vs. disease)
- Graph-structured neural dynamics with expressive message passing

**Trigger keywords**: brain dynamics, generative brain model, sheaf neural ODE, fMRI forecasting, EEG dynamics, brain graph, continuous-time brain, neural ODE brain

## Key Results

- Outperforms standard RNN, GNN, and graph ODE baselines on forecasting
- Sheaf Laplacian provides more expressive message passing than standard graph conv
- Representations support downstream tasks (perturbation prediction, classification)
- Works across modalities: fMRI, EEG, spiking simulator data

## Connections to Related Work

- **Neural ODEs** (Chen et al. 2018): Continuous-time dynamics via ODE solvers
- **Sheaf Neural Networks** (Hansen & Ghrist 2020): Sheaf theory for GNNs
- **Brain-informed GNNs**: Using connectome structure for neural models
- **Digital Brain Twins**: Generative models for individualized brain simulation

## Implementation Notes

1. **Sheaf Laplacian computation** is the key differentiator — O(E × d²) memory
2. ODE solver choice matters: `dopri5` for accuracy, `euler` for speed
3. Sliding LSTM window size T is a critical hyperparameter (try T=10-30 time steps)
4. Restriction maps can be initialized from structural connectivity as prior
5. Loss: MSE on activity + regularization on sheaf consistency
