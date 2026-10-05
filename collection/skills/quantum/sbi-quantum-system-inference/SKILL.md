---
name: sbi-quantum-system-inference
description: Quantum inference via simulation-based neural posteriors.
---

# Simulation-Based Quantum System Inference with Neural Posterior Estimation

**Source**: arXiv:2609.34995 (Zou, Frisk Kockum, Rahm, Olsson — Chalmers, 2026-09-28)

## Core Framework

Cast quantum characterization as a unified Bayesian inverse problem specified
by a 4-tuple **(θ, π, x, S)**:
- **θ**: latent parameters (noise probabilities, Hamiltonian couplings, state params)
- **π(θ)**: prior over physically admissible values (e.g., uniform [0, θ_max])
- **x**: observation vector (expectation values from measurement ensemble)
- **S**: scalable classical forward simulator approximating the quantum map

The likelihood p(x|θ) is intractable (exponential Hilbert space), so treat the
simulator as the statistical model: sample θ~π → simulate x~S(θ) → train a
conditional density estimator q_φ(θ|x) on pairs via max-likelihood.

## Key Design Decisions

1. **Amortized NPE**: train ONCE on N simulated pairs; any new measurement record
   maps to its posterior in one forward pass. Turns per-experiment inference into
   fixed up-front cost (reusable estimator).
2. **SNPE (sequential)**: use previous posterior as proposal for the next round —
   cheaper for a single target x_0, but the model cannot be reliably reused.
3. **Neural spline flows**: rational-quadratic splines (monotonic invertible) +
   autoregressive transforms for tractable Jacobians → exact density evaluation.
4. **Polynomial-cost simulators**: Pauli propagation (O(n²), ~0.1s for n=50 on one
   CPU thread) or tensor networks/MPS — never density-matrix evolution.

## Demonstrated Applications

| Task | θ dim | Simulator | Result |
|------|-------|-----------|--------|
| Sparse Pauli noise learning | 735 (15(n−1), n=50, 2-local channels) | Pauli propagation | tight posteriors; broad posteriors = gauge ambiguity |
| QEM (ZNE/PEC) | inferred noise params | PEC/ZNE sampling | posterior mean/median ≈ ground-truth noise performance |
| Digital-twin ML-QEM | posterior samples → sim pairs | noisy-ideal pairs | denoiser trained on synthetic pairs, zero-shot correction |
| Tomography (PQC) | Cholesky-parameterized states | circuits | accurate + uncertainty diagnostics |
| Rydberg Hamiltonian learning | 162 (81 atoms × 2D) | truncated Pauli prop. (weight≤5) | MAE 12.2±9.8 nm, R²=0.983 |

## Reusable Insights

- **Posterior width = non-identifiability diagnostic**: broad posteriors on specific
  parameters (e.g., Pauli gauge) flag where more characterization is needed —
  evaluate metrics on the gauge-free subset separately.
- **Gauge robustness for QEM**: QEM protocols work with inferred noise despite gauge
  freedom, provided the model represents the same effective channel.
- **Stationary Markovian noise assumption** lets noise learned on one layer be reused
  across deep circuits (key scaling trick).
- **Short-time probes**: single Trotter step (δt=0.01 µs) keeps circuits classically
  tractable while remaining informative (Rydberg case).
- **Classically-tractable substructures** extend reach when full circuits can't be
  simulated: repeated layers, partial tomography, circuit cutting fragments.

## Implementation Recipe

1. Define (θ, π, x, S) for the target characterization task.
2. Generate N=10⁴–10⁵ (θ, x) pairs with the polynomial simulator.
3. Train conditional neural spline flow q_φ(θ|x); monitor nMAE and R² per round (SNPE).
4. Validate: posterior mean/median vs ground truth; check R²_gauge-free ≥ 0.99.
5. Deploy: real QPU data x_0 → posterior in one forward pass; use posterior samples
   to parameterize downstream protocols (QEM, calibration feedback).

## Limitations / Open Issues
- Markovian noise + idealized SPAM in noise learning; gate-set tomography integration open.
- **Model misspecification**: estimator trained entirely on simulations — simulator-
  device discrepancy biases posteriors on real data; calibration needed.
- Fixed-size models (no size generalization); GNN estimators proposed for size-agnostic
  inference; flow matching proposed for high-dim NPE scaling.
