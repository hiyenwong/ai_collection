---
name: spectral-transfer-cascade-kuramoto
description: Use for graph-spectral transfer analysis of Kuramoto sync.
---

# Spectral Transfer Dynamics and Cascades in Graph-Coupled Kuramoto Networks

**Paper**: arXiv:2609.28432 (Kowalczyk, Liò, Struzik — Univ. Warsaw / Cambridge / Univ. Tokyo, 23 Sep 2026)

## Core Idea

Project Kuramoto phase dynamics onto the graph Laplacian eigenbasis and quantify **how dynamical activity redistributes between structural scales** — beyond the order parameter. Synchronisation is reinterpreted as a process of *evolving spectral organisation* with persistent modes, inter-modal interactions, and cascade-like transfer events.

**Central finding**: highly structured, intermittent spectral transfer (forward/inverse cascades, directional reversals, bursts) persists even when the global order parameter R(t) is nearly stationary and featureless. Macroscopic coherence and microscopic spectral interactions **separate cleanly**.

## Mathematical Framework

### 1. Graph Fourier representation
- Laplacian `L = D − A`, eigenvectors `Lφ_m = λ_m φ_m`, eigenvalues ordered `0 = λ₀ ≤ λ₁ ≤ … ≤ λ_{N−1}`.
- Low-frequency modes = large-scale/community organisation; high-frequency = fine structural variation.
- Graph Fourier transform of phases: `a_m(t) = Σ_i θ_i(t) φ_mᵀ(i)`.
- **Spectral modal energy**: `E_m(t) = |a_m(t)|²`.

### 2. Transfer matrix (the central object)
For each source mode m:
1. Reconstruct node-domain contribution: `θ_i^(m)(t) = a_m(t)·φ_m(i)`
2. Propagate through the *nonlinear* coupling term only: `F_m(i,t) = K·Σ_j A_ij·sin(θ_j^(m) − θ_i^(m))`
3. Project forcing back onto full graph Fourier basis: `f_{m→k}(t) = Σ_i F_m(i,t)·φ_k(i)`
4. **Transfer element**: `T_{m→k}(t) = 2·a_k(t)·f_{m→k}(t)`

Interpretation: a directed interaction network whose nodes are graph Fourier modes. Diagonal = modal self-persistence; off-diagonal = cross-scale exchange.

### 3. Spectral flux and cascade directionality
`Π(t, K₀) = Σ_{k>K₀} Σ_{m≤K₀} T_{m→k}(t)` (spectral mode cutoff K₀)
- Π > 0 → **forward cascade** (activity toward higher modes)
- Π < 0 → **inverse cascade** (toward lower modes)
- NOTE: this is *not* physical transport across nodes — it is redistribution between structural scales.

### 4. Persistence vs interaction observables
- Persistence intensity: `D(t) = Σ_m |T_{m→m}(t)|`
- Interaction intensity: `I(t) = Σ_{m≠k} |T_{m→k}(t)|`
- **Interaction ratio**: `Q(t) = I/(D+I)` — Q≈0 persistence-dominated; Q≈1 interaction-dominated. Reveals dynamical regimes invisible to R(t) alone.

Additional observables: occupancy fractions, reversal rates, transfer volatility/burstiness.

## Experimental Setup
- Modular undirected graphs (stochastic-block-model type): 5 modules, sizes ~U(1,15), dense intra-community + sparse inter-community links, fixed seeds.
- Kuramoto dynamics `θ̇_i = ω_i + K·Σ_j A_ij·sin(θ_j − θ_i)`.
- Dynamical regimes mapped over (coupling K, frequency heterogeneity): ordered / disordered / metastable / mixed-transition. Transfer observables separate regimes better than synchronisation measures.

## Why It Matters (Neuroscience / Brain Networks)
- Modular topology ↔ brain community structure; low Laplacian modes ↔ large-scale functional organisation.
- Explains how multiscale reorganisation can proceed in neural systems without visible changes in global coherence measures (e.g., stable fMRI/EEG coherence during covert state transitions).
- Bridges graph signal processing (GSP) and synchronisation theory; complements spectral graph wavelets (which do NOT quantify inter-modal interactions).

## Implementation Notes

```python
import numpy as np

def transfer_matrix(theta, A, K, phi):
    """T[m,k] = 2 a_k f_{m->k}(t); phi columns = Laplacian eigenvectors."""
    N = len(theta)
    a = phi.T @ theta                       # modal amplitudes
    T = np.zeros((N, N))
    for m in range(N):
        th_m = a[m] * phi[:, m]              # reconstructed mode-m signal
        F = K * (A * np.sin(th_m[None,:] - th_m[:,None])).sum(axis=1)
        f = phi.T @ F                       # projections onto all k
        T[m,:] = 2 * a * f                  # T_{m->k}(t)
    return T

def spectral_flux(T, K0):
    return T[K0+1:, :K0+1].sum()            # Π(t, K0)

def interaction_ratio(T):
    D = np.abs(np.diag(T)).sum()
    I = np.abs(T - np.diag(np.diag(T))).sum()
    return I / (D + I)
```

Cost: O(N²) per source mode per timestep for the full matrix; for large graphs restrict to first K₀+P modes (truncated eigenbasis).

## Relationship to Existing Skills
- Complements `finite-size-fluctuation-response-kuramoto` (FRR): that addresses noise-driven deviations at finite N; this addresses *deterministic nonlinear inter-modal transfer*.
- Complements `kuramoto-brain-network` / `complex-valued-kuramoto-control`: those use phase dynamics for brain coupling/control; this adds a spectral observability layer.
- Related to `renormalization-scaling-brain-activity` (RG view): both multiscale; spectral cascades give mode-resolved transfer, not just scaling exponents.

## When to Use
- Analysing synchronisation dynamics on modular/hierarchical networks (brain connectomes, power grids, ecological webs).
- Detecting hidden state transitions beneath stationary global coherence.
- Characterising multiscale information redistribution in neural mass / Kuramoto-based whole-brain models.
- Designing graph-spectral features for network dynamics classification.

## Limitations (from authors)
- First step toward a broader theory: role of topology, modularity, graph size, and generality across nonlinear systems remain open.
- Demonstrated on Kuramoto dynamics only; extension to other oscillator/neural models is future work.
