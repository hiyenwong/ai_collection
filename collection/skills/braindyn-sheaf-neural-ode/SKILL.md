---
name: braindyn-sheaf-neural-ode
description: Comprehensive methodology reference for BrainDyn — a Sheaf Neural ODE for Generative Brain Dynamics
arxiv: "2605.19324"
title: "BrainDyn: A Sheaf Neural ODE for Generative Brain Dynamics"
authors:
  - Siddharth Viswanath
  - Panayiotis Ketonis
  - Chen Liu
  - Michael Perlmutter
  - Dhananjay Bhaskar
  - Smita Krishnaswamy
date: 2026-05-19
subjects: ["cs.LG"]
---

# BrainDyn: A Sheaf Neural ODE for Generative Brain Dynamics

## Abstract

Efficient neural network models that generate brain-like dynamic activity can be a valuable resource for generating synthetic data, analyzing differences in brain transients under conditions such as testing perturbation activity or inferring the underlying generative dynamics. However, large language models (LLMs) or standard recurrent neural networks (RNNs) ignore the anatomical organization and therefore do not produce components that align with brain regions. On the other hand, graph-based networks often have very simple message passing rules that are not sufficiently expressive for brain-like dynamics. To address this, we introduce BrainDyn, a sheaf neural ordinary differential equation (neural ODE) model for continuous-time dynamics on structured brain graphs. BrainDyn encodes the recent activity history of each brain region using a long short-term memory (LSTM) model over a sliding temporal window to produce hidden states, or **stalks**, that are projected through learnable **restriction maps** into edge-specific shared spaces. Discrepancies between neighboring nodes in these shared spaces are characterized by a **sheaf Laplacian** that can facilitate message passing between neuronal units. The output of these messages is then fed to a neural ODE that governs the continuous-time evolution of neuronal activity. BrainDyn achieves strong forecasting ability across modalities, and the resulting representations support downstream tasks including in silico perturbation prediction.

---

## Methodology

### 1. Problem Formulation

**Input**: Time-series neural activity from structured brain graphs (fMRI, EEG, or simulated spiking data). Each brain region is a node; structural/functional connectivity defines edges.

**Goal**: Learn a continuous-time dynamical model that:
- Generates realistic brain-like activity trajectories
- Supports forecasting future activity
- Enables in silico perturbation analysis
- Preserves anatomical region alignment

### 2. Architecture Overview

BrainDyn consists of three main stages:

```
Raw time-series ─→ LSTM encoding ─→ Restriction maps ─→ Sheaf Laplacian ─→ Neural ODE ─→ Output dynamics
   (per node)        (stalks)         (edge projection)   (message passing)   (continuous evolution)
```

### 3. Temporal Encoding via LSTM (Stalk Construction)

**Sliding Window**: A temporal window of recent activity history slides over the input time-series for each brain region (node).

**LSTM Encoding**:
- Each node `v` has a time-series `x_v(t)` representing its neural activity
- The LSTM processes the sequence within each window to produce a hidden state `h_v`
- This hidden state serves as the **stalk** at node `v`: `s_v = h_v ∈ ℝ^d`
- The stalk dimension `d` is a hyperparameter controlling representation capacity

**Key properties**:
- Captures temporal dependencies within the sliding window
- Produces fixed-dimensional representations from variable-length activity histories
- Maintains per-node anatomical correspondence

### 4. Sheaf Structure: Restriction Maps

**Core Concept**: A cellular sheaf assigns a vector space (stalk) to each node and linear maps (restriction maps) to each edge that encode how information flows between adjacent nodes.

**Learnable Restriction Maps**:
- For each edge `e = (u, v)` in the brain graph, there are two restriction maps:
  - `D_{v⊲e}: ℝ^d → ℝ^{d_e}` — maps stalk at node `v` to the edge space
  - `D_{u⊲e}: ℝ^d → ℝ^{d_e}` — maps stalk at node `u` to the edge space
- `d_e` is the dimension of the edge-specific shared space
- These maps are **learned parameters** (not fixed), allowing the model to discover optimal information flow patterns

**Edge-Specific Shared Spaces**:
- Each edge has its own shared space where neighboring nodes can be compared
- The restriction maps project node stalks into these shared spaces
- Discrepancies in the shared space quantify disagreement between connected regions

### 5. Sheaf Laplacian for Message Passing

**Sheaf Laplacian** `Δ_F` generalizes the standard graph Laplacian to incorporate the sheaf structure:

For a sheaf with stalks and restriction maps, the sheaf Laplacian captures the **discrepancy** between neighboring nodes in their shared edge spaces.

**Computation**:
- For each edge `e = (u, v)`, compute the disagreement: `D_{u⊲e}(s_u) - D_{v⊲e}(s_v)`
- Aggregate these disagreements across all edges incident to each node
- The resulting operator `Δ_F` acts on the full stalk vector `s ∈ ℝ^{n·d}`

**Message Passing**:
- The sheaf Laplacian produces messages that encode how each node should update based on its neighbors
- Unlike standard GNN message passing, the sheaf Laplacian operates in the edge-specific shared spaces defined by the restriction maps
- This provides richer, more expressive communication than simple averaging or attention

**Key advantages over standard GNNs**:
- Edge-specific transformations (not just scalar edge weights)
- Directional information flow via asymmetric restriction maps
- The sheaf Laplacian spectrum provides geometric insight into the dynamics

### 6. Neural ODE for Continuous-Time Dynamics

**Neural ODE Layer**: The messages from the sheaf Laplacian are fed into a neural ODE that governs continuous-time evolution.

**Dynamics**:
```
dh/dt = f(h(t), Δ_F h(t); θ)
```

where:
- `h(t) ∈ ℝ^{n·d}` is the stacked vector of all node stalks at time `t`
- `Δ_F` is the sheaf Laplacian
- `f` is a neural network parameterized by `θ`
- The ODE is solved numerically (typically with an adaptive step-size solver)

**Properties**:
- Continuous-time formulation handles irregular sampling naturally
- Adaptive solvers can allocate computation where dynamics change rapidly
- Supports evaluation at arbitrary time points
- Memory-efficient backpropagation via adjoint sensitivity method

### 7. Training

**Loss Function**: The model is trained to forecast neural activity, likely using:
- MSE/MSE-like reconstruction loss between predicted and observed activity
- Possibly regularization terms (not specified in abstract)

**End-to-End Training**: All components (LSTM, restriction maps, neural ODE parameters) are trained jointly via backpropagation through the ODE solver.

### 8. Evaluation Modalities

The model was evaluated on three distinct datasets:

| Dataset | Modality | Description |
|---------|----------|-------------|
| **PNC** | Resting-state fMRI | Philadelphia Neurodevelopmental Cohort — measures BOLD signal across brain regions |
| **TUSZ** | Scalp EEG | Temple University Hospital Seizure Corpus — focal epilepsy EEG recordings |
| **NEST** | Spiking simulation | NEST spiking network simulator — ground-truth simulated neuronal activity |

**Evaluation Metrics**:
- Forecasting ability (predicting future neural activity)
- Downstream task performance (in silico perturbation prediction)
- Cross-modal generalization

### 9. Key Contributions

1. **Sheaf neural ODE architecture**: First application of cellular sheaves with neural ODEs for brain dynamics
2. **Anatomically-grounded representations**: Maintains brain region alignment unlike LLMs/standard RNNs
3. **Expressive message passing**: Sheaf Laplacian provides richer communication than standard GNNs
4. **Multi-modal validation**: Demonstrated on fMRI, EEG, and simulated spiking data
5. **Perturbation analysis**: Learned representations support in silico perturbation studies

---

## Key Definitions

| Term | Definition |
|------|-----------|
| **Stalk** | Vector space assigned to each node; in BrainDyn, the LSTM hidden state encoding temporal activity |
| **Restriction Map** | Linear map assigned to each edge that projects node stalks into edge-specific shared spaces |
| **Sheaf Laplacian** | Generalized Laplacian operator encoding disagreement between neighboring nodes in shared edge spaces |
| **Cellular Sheaf** | Mathematical structure: a graph with vector spaces at nodes and linear maps on edges |
| **Neural ODE** | Neural network layer defined by an ODE `dh/dt = f(h; θ)` solved numerically |
| **Adjoint Method** | Memory-efficient backpropagation through ODE solvers |

---

## Comparison to Related Approaches

| Method | Anatomical Alignment | Expressivity | Continuous Time | Brain-Specific |
|--------|---------------------|--------------|-----------------|----------------|
| LLMs | ❌ | High | ❌ | ❌ |
| Standard RNNs | ❌ | Moderate | ❌ | ❌ |
| Standard GNNs | ✅ | Limited (simple MP) | ❌ | Partial |
| **BrainDyn** | ✅ | High (sheaf MP) | ✅ | ✅ |

---

## Relevant Literature

- **Sheaf Theory**: Hansen & Ghrist (2019), "Sheaf-theoretic methods in data science"
- **Neural ODEs**: Chen et al. (2018), "Neural Ordinary Differential Equations" (NeurIPS)
- **Sheaf Neural Networks**: Hansen & Gebhart (2020), "Sheaf neural networks"
- **Sheaf Diffusion**: Bodnar et al. (2022), "Neural sheaf diffusion" (NeurIPS)
- **Brain Network Modeling**: Various works on fMRI/EEG time-series forecasting and perturbation analysis

---

## Practical Considerations

### Hyperparameters
- Stalk dimension `d`
- Edge space dimension `d_e`
- LSTM hidden size and sliding window length
- Neural ODE solver choice and tolerance
- Brain graph construction (structural vs. functional connectivity)

### Computational Complexity
- Restriction maps: `O(|E| · d · d_e)` per forward pass
- Sheaf Laplacian: `O(|E| · d_e)` to compute disagreements
- Neural ODE: depends on solver steps; typically `O(n · d · hidden_dim)` per step

### Implementation Notes
- Stalks are constructed per-node from temporal windows (can be parallelized)
- Restriction maps are learned matrices (one per edge, or parameterized)
- Sheaf Laplacian is sparse (graph-structured)
- Neural ODE adjoint method enables memory-efficient training
