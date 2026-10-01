---
name: greens-operator-multitask-rnn
description: Green's operator analysis of task reuse in multitask RNNs.
category: ai_collection
---

# Green's Operator for Multi-Task RNN Analysis

**Source**: arXiv:2609.40292 — "Disentangling Computation in Multi-Task Neural Networks with the Green's Operator" (James Hazelden, UW Applied Math / Allen Institute; accepted at NeurReps 2026, NeurIPS Workshop on Symmetry and Geometry in Neural Representations)

**Use when**: analyzing how computation is organized/reused across tasks or time in trained recurrent networks; comparing task similarity beyond activity geometry; mapping causal perturbation pathways; complementing fixed-point / Lyapunov / representational-similarity analyses.

## Core Idea

The **finite-horizon Green's operator P** is the global linear map from perturbations injected across a trajectory to their first-order downstream state responses. Its blocks `P_{t,s}` directly encode source-to-destination perturbation routing:

```
P_{t,s} = J_{t-1} J_{t-2} ... J_s          (t > s; identity on diagonal)
δh = P u                                    (stacked over finite horizon)
```

Global implicit form for any model written as constraint `F(h, x, θ) = 0`:
```
P = [D_h F]^{-1} = (I - L)^{-1} = I + L + L² + ... + L^K
```
where L holds one-step state dependencies (nilpotent for finite horizon); term L^k collects all length-k paths through the computation graph.

**Key dissociation**: routing is NOT determined by activity or local spectrum. Two systems can share (a) the exact unperturbed trajectory and (b) the same eigenvalues, yet differ in whether a perturbation in y influences x (triangular toy: off-diagonal term `c(a^k - b^k)/(a-b)` is the exact lag-k response). Activity geometry and Lyapunov spectra cannot see this; P records it directly.

## Two Complementary Reductions

P is naturally indexed by (task, trial, time, unit) — never build the full tensor. Reduce along different axes:

1. **Task-level reduction** `G_τ = R_task(P_τ)` → answers *which computations are reused?*
   Compare task pairs with normalized Frobenius similarity:
   `S(τ,τ') = ⟨G_τ, G_τ'⟩_F / (‖G_τ‖_F ‖G_τ'‖_F)`
   Block structure aligns with known motif families; disagrees partially with hidden-state covariance (related but non-equivalent views).

2. **Time-level reduction** `R_τ(t,s)` (retain source time s, target time t) → answers *when is influence routed?*
   Before training: response near causal diagonal. After training: memory-demanding tasks (MemoryPro, DMS) develop delay-spanning pathways; reactive tasks (ReactPro) stay local. Training organizes temporal routing by persistence demands — not merely revealing init structure.

## Matrix-Free Evaluation (the practical trick)

Full P is T²N² — never construct it. Only products are needed:

**Forward product y = Pu** (single forward recurrence):
```
y_0 = u_0
y_{t+1} = J_t y_t + u_{t+1}        for t = 0..T-2
return stacked y
```

**Adjoint product z = P*v** (reverse recurrence):
```
z_{T-1} = v_{T-1}
z_t = v_t + J_t* z_{t+1}
```
Cost: linear in horizon × cost of JVP/VJP. These products support randomized range-finding, randomized SVD, Gram products, stochastic traces — i.e., low-rank summaries of the full operator.

**Learning connection**: differentiating the constraint gives `D_θ h = -P D_θ F` — parameter-to-state learning operators are parameter-selected sketches of the global response geometry.

## Benchmark Numbers (256-unit leaky RNN, 15-task family of Driscoll et al. 2024, checkpoint 680k)

| Representation | ROC-AUC / AP (8-trial fair) |
|---|---|
| Green response similarity | 0.920 / 0.765 |
| Hidden covariance | 0.852 / 0.591 |
| Laura-style task variance | 0.941 / 0.812 |
| Local gain-spectrum | 0.785 / 0.573 |
| Epoch-permuted null | 0.812 ± 0.017 (observed 0.920, p=2e-4) |

- Trial reliability: pairwise Green maps from disjoint 16-trial sets correlate 0.959.
- Frobenius-energy controls (basis-invariant): long-range response fraction at 680k — ReactPro 0.017 vs MemoryPro 0.353 (both ~5e-4 at init); near-diagonal 0.660 vs 0.167 (~0.83 at init).

## Honest Limitations (from the paper)

- First-order, finite-horizon; every reduction discards information — claim is deliberately narrow (descriptive map, not universal replacement).
- Task-level Green organization is **model-dependent** across networks.
- Failure case: DMC vs DNMC can share nearly identical singular-value spectra while response directions differ substantially — gain spectra and routing geometry answer different questions.
- Green similarity correlates with gradient alignment but NOT uniquely after controlling for task variance → do **not** claim it predicts transfer or interference.

## Implementation Checklist

1. Train or load a task-conditioned RNN; collect trajectories per task condition.
2. Compute Jacobians `J_t` along each trajectory (or JVP/VJP functions directly).
3. Choose reduction: task-level (reduce over time/units → G_τ) or time-level (retain s,t).
4. Estimate via forward/adjoint recurrences with random probe vectors; use randomized SVD for low-rank views.
5. Compare with normalized Frobenius similarity; control with epoch-preserving permutations and covariance baselines.
6. For temporal claims, use basis-invariant Frobenius response RMS rather than uniform-direction projections (the latter is a visualization, not a trace).

## Related Skills

- `low-rank-rnn-learning-dynamics`, `neural-population-dynamics`, `gain-vs-off-manifold-decomposition` — complementary geometric/dynamical analyses of trained RNNs.
