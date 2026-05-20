---
name: braindyn-sheaf-neural-ode
description: >
  BrainDyn: Sheaf Neural ODE methodology for generative brain dynamics modeling.
  Combines cellular sheaf theory with neural ODEs to model continuous-time neural
  dynamics on structured brain graphs. Use when working with brain dynamics
  forecasting, sheaf neural networks, neural ODEs, spatiotemporal brain modeling,
  in silico perturbation prediction, or multi-modal neural signal analysis (fMRI,
  EEG, spiking networks). Triggered by: braindyn, sheaf neural network, neural ODE
  brain dynamics, generative brain model, sheaf Laplacian, continuous-time neural
  dynamics, brain signal forecasting, perturbation prediction on brain graphs.
---

# BrainDyn: A Sheaf Neural ODE for Generative Brain Dynamics

arXiv:2605.19324 (Viswanath et al., Yale University, May 2026)

## Core Idea

Standard GNNs aggregate all nodes in the same feature space. **Cellular sheaves** equip each edge with **restriction maps** — linear transformations that project node features into an **edge-specific shared space** before aggregation. This lets different brain connections transform and modulate signals in distinct ways, matching biological reality.

BrainDyn combines: (1) LSTM-encoded temporal history → (2) sheaf restriction maps for heterogeneous inter-region coupling → (3) neural ODE for continuous-time evolution.

## Architecture (3 Components)

### 1. Memory-based Node Stalks
Each brain region's recent temporal history (sliding window) is encoded by an LSTM into a hidden state (stalk). Neural activity is history-dependent — the current state reflects accumulated past dynamics.

### 2. Edge Modulation via Sheaf Restriction Maps
Learnable restriction maps ρ: ℝ^dᵢ → ℝ^dₑ project node features into edge-specific shared spaces. Combined with feature-wise gating for channel-specific and direction-dependent coupling. Disagreements between neighboring nodes in shared spaces are measured by the **sheaf Laplacian**.

### 3. Continuous-time Evolution via Neural ODE
The sheaf Laplacian output feeds into a neural ODE (two-layer MLP vector field) integrated via 4th-order Runge-Kutta (RK4) with step size Δt=1. Governs continuous-time evolution of neuronal activity.

## Sheaf Laplacian (Key Math)

For graph G=(V,E), cellular sheaf assigns:
- Node stalks: F(i) ≅ ℝ^dᵢ
- Edge stalks: F(eᵢⱼ) ≅ ℝ^dₑ
- Restriction maps: ρᵢ→ₑᵢⱼ, ρⱼ→ₑᵢⱼ

The sheaf Laplacian L = BᵀB where B is the sheaf coboundary operator. It generalizes the graph Laplacian by measuring disagreement **only after** features are transformed through restriction maps into edge-specific spaces.

## Graph Construction

Prior graph P built from **Granger causality** computed from the input context window. Connections with sufficiently strong Granger causality are retained. Sheaf restriction maps then learn expressive edge-specific transformations on top of this prior.

## Datasets & Evaluation

- **PNC fMRI**: 1188 subjects, 400-region Schaefer parcellation, resting-state BOLD
- **TUSZ EEG**: 19-channel scalp EEG, binary seizure/non-seizure windows
- **NEST simulations**: 100 iaf_psc_alpha neurons, directed small-world network

Outperforms CNN-LSTM, BIOT (transformer), EvolveGCN, ODEBRAIN, RiTINI across both fMRI and EEG modalities.

## Perturbation Analysis

The sheaf-based representations generalize to out-of-distribution perturbed dynamics. When a brain region's input is perturbed in silico, BrainDyn predicts how the perturbation propagates through the network — enabling virtual testbeds for stimulation studies.

## Computational Complexity

Per-sample cost decomposes:
- LSTM encoder: O(NT(FD + LD²)) — N nodes, window T, signal dim F, hidden D, L layers
- Sheaf Laplacian: O(EDM) — E edges, map dim M
- Neural ODE: O(SV²) — S RK4 steps, vector field width V
- Trained with AdamW, 100 epochs, batch 64, single NVIDIA H200 GPU

## Implementation Pattern

```python
# Conceptual BrainDyn forward pass
import torch
from torchdiffeq import odeint

class BrainDyn(torch.nn.Module):
    def __init__(self, n_nodes, n_edges, d_stalk, d_map, d_hidden):
        super().__init__()
        # LSTM per node for temporal encoding
        self.lstm = torch.nn.LSTM(input_size=1, hidden_size=d_stalk, num_layers=2)
        # Learnable restriction maps per edge
        self.restriction_maps = torch.nn.Parameter(torch.randn(n_edges, d_stalk, d_map))
        # Neural ODE vector field (2-layer MLP)
        self.ode_func = torch.nn.Sequential(
            torch.nn.Linear(n_nodes * d_map, d_hidden),
            torch.nn.ReLU(),
            torch.nn.Linear(d_hidden, n_nodes)
        )
    
    def sheaf_laplacian(self, stalks, edge_index):
        """Compute sheaf Laplacian: L = B^T B"""
        # Project node features through restriction maps to edge spaces
        # Measure disagreement in edge-specific spaces
        # Pull back to node space
        pass
    
    def ode_rhs(self, t, y):
        """Neural ODE right-hand side"""
        return self.ode_func(y)
    
    def forward(self, x, edge_index, t_eval):
        # 1. Encode temporal history via LSTM → stalks
        stalks = self.lstm(x)[0]
        # 2. Compute sheaf Laplacian with restriction maps
        sheaf_output = self.sheaf_laplacian(stalks, edge_index)
        # 3. Integrate neural ODE
        y0 = sheaf_output
        y_pred = odeint(self.ode_rhs, y0, t_eval, method='rk4')
        return y_pred
```

## Key Advantages over Prior Work

| Method | Anatomical Awareness | Edge Heterogeneity | Continuous Time |
|--------|---------------------|-------------------|-----------------|
| CNN-LSTM | ❌ | ❌ | ❌ |
| BIOT (Transformer) | ❌ | ❌ | ❌ |
| EvolveGCN | ✅ (static) | ❌ | ❌ |
| ODEBRAIN | ✅ | ❌ | ✅ |
| **BrainDyn** | ✅ | ✅ | ✅ |

## When to Use

- Building generative models of brain dynamics (fMRI, EEG, spiking)
- Need edge-specific message passing (not uniform GNN aggregation)
- Continuous-time modeling of neural signals
- In silico perturbation/ stimulation prediction
- Multi-modal neural signal analysis (one model, multiple signal types)

## Activation

braindyn, sheaf neural ODE, brain dynamics forecasting, neural ODE brain, sheaf Laplacian, generative brain model, in silico perturbation, continuous-time neural dynamics, restriction map neural network, spatiotemporal brain modeling
