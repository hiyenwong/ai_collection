---
name: braindyn-sheaf-neural-ode
description: >
  BrainDyn: A Sheaf Neural ODE framework for modeling continuous-time neural dynamics on structured brain graphs.
  Combines cellular sheaf theory (learnable restriction maps, sheaf Laplacian) with neural ODEs for generative brain dynamics.
  Supports multi-modal neural data (fMRI, EEG, spiking neural network simulations), in silico perturbation prediction,
  and structured latent representations. Use when: (1) modeling brain dynamics as continuous-time ODEs on brain graphs,
  (2) implementing sheaf neural networks for heterogeneous inter-region communication, (3) building virtual brain models
  for perturbation analysis, (4) forecasting neural activity across modalities (fMRI/EEG/spiking), (5) studying
  sheaf Laplacians as generalization of graph Laplacians for brain networks. Activation: braindyn, sheaf neural ODE,
  sheaf neural network, brain dynamics forecasting, virtual brain model, in silico perturbation, cellular sheaf brain,
  sheaf Laplacian, generative brain dynamics, continuous-time neural dynamics.
---

# BrainDyn: A Sheaf Neural ODE for Generative Brain Dynamics

**Paper:** arXiv:2605.19324 | Viswanath et al. (Yale, Boise State, UW-Madison) | May 2026

## Overview

BrainDyn is a **sheaf neural ordinary differential equation (neural ODE)** model for continuous-time dynamics on structured brain graphs. First work to combine cellular sheaves with neural ODEs.

**Key insight:** Standard GNNs aggregate in a shared feature space (scalar summation), causing oversmoothing and erasing heterogeneous dynamics. Cellular sheaves equip each edge with **learnable restriction maps** that transform node features into edge-specific shared spaces, enabling brain regions to maintain distinct representational geometries while communicating.

## Architecture

### Three Core Components

```
[LSTM] → [Restriction Maps + Attention] → [Sheaf Laplacian Message Passing] → [Neural ODE]
```

1. **Memory-based Node Stalks** (Section 4.2)
   - LSTM encodes temporal window [x(tₚ), ..., x(tq)] into hidden state hᵢ(t) ∈ ℝᵈ
   - hᵢ(t) interpreted as stalk representation for node i
   - H(t) = [h₁ᵀ(t), ..., h_Nᵀ(t)]ᵀ stacks all node stalks

2. **Learnable Sheaf Restriction Maps with Attention** (Section 4.3)
   - For edge eᵢⱼ: learnable ρᵢ→ₑᵢⱼ, ρⱼ→ₑᵢⱼ ∈ ℝᵈˣᵈ project stalks to edge space
   - hᵢ→ₑᵢⱼ = ρᵢ→ₑᵢⱼ hᵢ (edge-specific transformation)
   - Attention: αᵢ = σ(aᵀ hᵢ→ₑᵢⱼ) modulates contribution
   - Edge discrepancy: δᵢⱼ = αᵢ hᵢ→ₑᵢⱼ − αⱼ hⱼ→ₑᵢⱼ
   - Sheaf Laplacian: (L_ℱ H)ᵢ = ∑_j ρᵢ→ₑᵢⱼᵀ δᵢⱼ

3. **Continuous-time Neural ODE** (Section 4.5)
   - dx/dt = f_θ(hᵢ⁽ᴸ⁾) = MLP_θ(hᵢ⁽ᴸ⁾) where h⁽ᴸ⁾ is post-message-passing state
   - Message passing: H⁽ˡ⁾ = (I − L_ℱ) H⁽ˡ⁻¹⁾ for L rounds
   - Solved via RK4 (torchdiffeq), step size Δt=1

### Prior Graph Construction (Section 4.1)
- Granger causality from input context window only (no future leakage)
- Top-k strongest edges retained
- Used to initialize sheaf structure and regularize learned interactions

### Training Objective
```
ℒ = ℒ_MSE + λ₁ ℒ_sparse + λ₂ ℒ_prior
```
- ℒ_MSE: reconstruction error
- ℒ_sparse: L1 penalty on edge discrepancy signals (parsimonious communication)
- ℒ_prior: learned interactions close to prior Granger graph

## Evaluation Results

### Multi-modal Forecasting

| Method | fMRI MSE ↓ | EEG MSE ↓ | NEST MSE ↓ |
|--------|-----------|----------|-----------|
| CNN-LSTM | 0.89 | 0.55 | 0.896 |
| BIOT | 1.99 | 1.16 | 1.041 |
| EvolveGCN | 1.00 | 0.65 | 1.029 |
| ODEBRAIN | 0.85 | 0.47 | 0.702 |
| RiTINI | 1.91 | 1.02 | 0.904 |
| **BrainDyn** | **0.66** | **0.44** | **0.671** |

- **fMRI (PNC, 1188 subjects, 400 regions):** 22% better than ODEBRAIN
- **EEG (TUSZ, 315 patients, 19 channels):** best across all metrics
- **NEST spiking (perturbation, 10K networks):** best out-of-distribution generalization

### In Silico Perturbation
- Models trained on unperturbed activity, evaluated on single-neuron silencing
- BrainDyn extrapolates to perturbed OOD dynamics; both sheaf + LSTM essential

## Implementation Guide

### Key Equations

**Sheaf Laplacian block structure:**
- Diagonal: ℒ_F(i,i) = ∑_j ρᵢ→ₑᵢⱼᵀ ρᵢ→ₑᵢⱼ
- Off-diagonal: L_F(i,j) = −ρᵢ→ₑᵢⱼᵀ ρⱼ→ₑᵢⱼ

**Message passing update:**
H⁽ˡ⁾ = (I − L_ℱ) H⁽ˡ⁻¹⁾

### Datasets
- **PNC fMRI:** Philadelphia Neurodevelopmental Cohort, 400 Schaefer regions, TR=3s
- **TUSZ EEG:** Temple University Hospital Seizure Corpus, 19 channels, 200 Hz
- **NEST:** 100 iaf_psc_alpha neurons, small-world graph (k=8, β=0.1, 400 edges)

### Hyperparameters
- AdamW, lr=1e-3, weight_decay=1e-5, ReduceLROnPlateau
- ODE solver: RK4 (torchdiffeq), Δt=1
- LSTM: per-node, sliding window encoding
- Sheaf dimension d: learnable
- Batch size: 64, 5-fold CV, single H200 GPU

### Dependencies
```python
import torch
import torch.nn as nn
from torchdiffeq import odeint  # Neural ODE solver
# Graph construction: use Granger causality (statsmodels or custom)
```

### Complexity
Per-sample: O(NT(FD+LD²)) + O(EDM) + O(4SHV²)
- N nodes, T time steps, F features, D stalk dimension, E edges
- L message passing rounds, M sheaf dimension, V MLP width, H horizon, S RK4 steps

## Biological Interpretation

The sheaf framework encodes a biologically motivated hypothesis: **communication between brain regions involves transformation, not just summation.** Each restriction map ρᵢ→ₑᵢⱼ represents how region i's signal is transformed before entering the communication channel with region j — analogous to synaptic transformations, receptor-specific filtering, or modulatory gating.

The sheaf Laplacian measures **disagreement after alignment** — the brain's tendency to reduce representational mismatches across connected regions, driving synchronization/desynchronization patterns.

## Limitations

- Currently models resting dynamics only (self-sustaining, minimal sensory input)
- Not yet tested on stimulus-driven dynamics (movie-watching, audio inputs)
- Requires simultaneous perturbation of multiple neuronal units for training on sensory tasks

## Activation Keywords

- braindyn
- sheaf neural ode
- sheaf neural network
- cellular sheaf brain
- sheaf Laplacian
- brain dynamics forecasting
- virtual brain model
- in silico perturbation
- continuous-time neural dynamics
- generative brain dynamics
