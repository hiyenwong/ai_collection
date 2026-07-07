---
name: flux-longitudinal-flow-matching
description: "Geometry-aware longitudinal flow matching framework for unpaired biological snapshot data. FLUX learns data-dependent metrics, constructs manifold-aware conditional paths, and uses mixture-of-experts velocity fields for joint transport modeling and unsupervised regime discovery. From Ortega Caro et al. 2026 (arXiv:2605.08648). Use when: modeling unpaired longitudinal biological data, flow matching on manifolds, neural dynamics trajectory reconstruction, cell differentiation modeling, calcium imaging analysis, regime discovery in time series."
---

# FLUX: Geometry-Aware Longitudinal Flow Matching with Mixture of Experts

Framework from **"FLUX: Geometry-Aware Longitudinal Flow Matching with Mixture of Experts"** (Josue Ortega Caro, Yongxu Zhang, Hannah M. Batchelor, Sizhuang He, Jessica Cardin, Shreya Saxena -- Yale University, arXiv:2605.08648, May 2026) for reconstructing longitudinal trajectories from unpaired population snapshots while discovering latent regime transitions.

## Core Problem

Many biological systems are observed only as **unpaired population snapshots** (not tracked trajectories):
- Widefield calcium imaging: neurons drift between sessions, trial structure not aligned
- Single-cell RNA-seq: measurement destroys the cell, no tracking across timepoints
- Data are sequences of marginal distributions mu_0, mu_1, ..., mu_{T-1} rather than matched trajectories

Two coupled challenges:
1. **Geometry**: Trajectories must respect curved low-dimensional manifolds embedded in high-dimensional space
2. **Regime switching**: The transport mechanism itself may change over time (learning phases, developmental stages)

## Architecture

### Three-Stage Training Pipeline

**Stage 1: Metric Learning**
- Learn data-dependent metric G(x) from pooled labeled + unlabeled observations
- Geometry model defines low-energy paths on the data manifold
- Supports RBF metrics (low-dim) and RBF-MLP deep-kernel metrics (high-dim)

**Stage 2: Bend Network Training**
- Train bend network B_psi with frozen metric
- Produces geometry-aware interpolants between adjacent-marginal endpoints
- Conditional paths: z_{k,alpha} = B_psi(x_k, x_{k+1}, alpha; G)
- Tangents: z_dot_{k,alpha} = partial B_psi / partial alpha

**Stage 3: Velocity Field Training**
- Geometry model and bend network frozen
- Train velocity experts and router on geometry-aware path points and tangents
- L_FM = E[||v_theta(t_{k,alpha}, z_{k,alpha}) - z_dot_{k,alpha}||^2]

### Regime-Switching Velocity Fields (MoE)

FLUX decomposes the longitudinal velocity field into M expert vector fields:
- f_m: [0,1] x R^d -> R^d, m = 1,...,M
- Router g: [0,1] x R^d -> R^M maps time+state to expert logits
- Straight-Through Gumbel-Softmax enables differentiable discrete routing
- At inference: regime = argmax_m l_m(t, x)

### Router Regularization

| Penalty | Purpose | Formula |
|---------|---------|---------|
| L_div | Prevent expert collapse | 1 - H(w_bar)/log(K) |
| L_sparse | Per-sample commitment | 1 - ||w||_2^2 / ||w||_1^2 |
| L_con | Temporal coherence | Var[w_i : i in group] |
| L_lb | Load balance | K * sum(F_j * P_j) |
| L_contig | Discourage temporal scattering | Var[s * w_bar_{s,j}] |

### Full Objective

L = L_FM + lambda*L2*L_L2 + lambda_vel*L_vel + L_routing

## Key Innovations

1. **Geometry-aware conditional paths**: Euclidean interpolants pass through low-density regions; learned metrics keep trajectories on the data manifold
2. **MoE velocity decomposition**: Single velocity field cannot capture regime changes; sparse expert routing discovers latent transitions
3. **Joint transport + regime discovery**: Regime discovery emerges from velocity field decomposition, not post-hoc clustering
4. **Multi-marginal longitudinal transport**: Extends flow matching beyond two-marginal settings

## Benchmarks and Results

### Stanford Bunny (Geometry)
- Tests manifold transport on known 3D surface
- FLUX with learned geometry stays on surface; Euclidean methods cut through interior
- Surface deviation metric validates manifold adherence

### Lorenz System (Regime Discovery)
- Controlled dynamical transition at known boundary
- FLUX recovers regime boundary from transport dynamics alone
- ARI and NMI for regime assignment

### Widefield Calcium Imaging (Neural Data)
- 12 mice, 451-dim cortical population activity, 22 marginals (learning sessions)
- Router separates early/intermediate training from late training
- Regime transition coincides with behavioral divergence of CS+/CS- lick indices

### Embryoid Body Differentiation (Single-Cell)
- RNA-seq profiles across developmental timepoints
- FLUX separates expression-evolution regimes: pluripotent vs differentiated
- Regime recovery depends on geometry-aware dynamics

## Baselines Compared

| Method | Type | Limitation |
|--------|------|------------|
| Linear interpolation | Adjacent pair | No shared velocity field |
| Static OT (Sinkhorn) | Adjacent pair | No continuous dynamics |
| Independent CFM | Adjacent pair | No parameter sharing across chain |
| IMMFM | Multi-marginal | Euclidean paths, no regime discovery |
| FLUX w/o Manifold | Multi-marginal + MoE | Euclidean paths, weak regime discovery |
| K-Means/GMM | Clustering | Static, no dynamics |
| rSLDS/SRNN | Switching dynamics | Require sequential inputs |

## Application Scenarios

1. **Neural dynamics trajectory reconstruction** -- Widefield calcium imaging across learning sessions
2. **Cell differentiation modeling** -- Single-cell RNA-seq developmental trajectories
3. **Flow matching on manifolds** -- Data concentrated near curved low-dimensional manifolds
4. **Regime discovery in time series** -- Unsupervised detection of dynamical phase transitions
5. **Longitudinal fMRI/EEG analysis** -- Tracking population-level changes across sessions

## Implementation Requirements

```python
# Key components
class GeometryBackend:  # Stage 0: Learn data-dependent metric
    def fit(self, X_pooled): ...
    def metric(self, x): ...

class BendNetwork:  # Stage 1: Geometry-aware interpolants
    def forward(self, x0, x1, alpha, G): ...

class MixtureVelocityNet:  # Stage 2: MoE velocity field
    def forward(self, t, x):
        logits = router(t, x)  # Expert logits
        experts = [v_m(t, x) for v_m in velocity_nets]  # Parallel
        weights = gumbel_softmax(logits, tau)  # ST-Gumbel
        return sum(w_m * f_m for w_m, f_m in zip(weights, experts))
```

## Training Protocol

1. Construct or load longitudinal marginals
2. Train geometry backend on pooled samples
3. Train bend network with frozen geometry
4. Train single-velocity or MoE velocity model with frozen geometry + bend
5. Evaluate one-hop, two-hop, and full-chain transport (Wasserstein distance)
6. Evaluate segment-level regime discovery (ARI, NMI) where labels available

## Key Hyperparameters

| Parameter | Lorenz | Neural Data | Embryoid Body |
|-----------|--------|-------------|---------------|
| Hidden dim | 64 | 256/128 | 128 |
| Experts K | 2 | 3 | 3 |
| Velocity layers | 2 | 2 | 2 |
| Time embed dim | 16 | 16 | 32 |

## Related Work

- **Flow matching**: Lipman et al. 2023, Tong et al. 2024 (Conditional Flow Matching)
- **Riemannian flow matching**: Chen & Lipman 2024 (known manifolds)
- **Metric Flow Matching**: Kapusniak et al. 2024 (learned data-dependent metrics)
- **Optimal transport**: Peyre & Cuturi 2019 (computational OT)
- **Mixture-of-experts**: Shazeer et al. 2017, Fedus et al. 2022 (Switch Transformers)
- **TrajectoryNet**: Tong et al. 2020 (continuous normalizing flows from snapshots)

## References

- Ortega Caro, J. et al. (2026). "FLUX: Geometry-Aware Longitudinal Flow Matching with Mixture of Experts." arXiv:2605.08648
- Lipman, Y. et al. (2023). "Flow matching for generative modeling." ICLR 2023
- Chen, R.T.Q. & Lipman, Y. (2024). "Flow matching on general geometries." ICLR 2024
- Kapusniak, V. et al. (2024). "Metric Flow Matching."

## Activation Keywords

- longitudinal flow matching, geometry-aware transport, unpaired snapshots
- biological trajectory reconstruction, mixture-of-experts velocity field
- regime discovery neural dynamics, calcium imaging trajectory
- cell differentiation modeling, FLUX framework, manifold-aware flow matching
- 纵向流匹配, 几何感知传输, 神经动力学重建
