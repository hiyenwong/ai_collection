---
name: intrinsic-dimension-vmc-nqs
description: Intrinsic dimension of quantum wavefunction learning (VMC).
---

# Intrinsic Dimension of Learning a Quantum Wavefunction (Subspace-Restricted VMC)

**Source**: arXiv:2609.33193 (Wei, Wang, Cao, Ling, 2026-09-27)

## Method: Subspace-Restricted VMC

Train only a latent **z ∈ ℝ^d (d ≪ P)** through a frozen random map θ = g(z),
keeping the standard natural-gradient optimizer (minSR/SR) unmodified.

**Per-group linear construction (TC2)**: θ_k = θ_{0,k} + s_k·W_k·z_k where W_k has
orthonormal columns (QR of seeded Gaussian), s_k = std(θ_{0,k}) keeps perturbations at
the group's natural scale, latent budget split proportionally to group size.

Four configurations (equal steps, same init):
- TC1: full-parameter reference
- TC2: linear random subspace (primary instrument)
- TC3: nonlinear tanh map variant
- TC4: last-parameter-group-only (cheap control)

## Three Reusable Pieces

1. **Intrinsic-dimension measurement for sampled objectives**: smallest d reaching a
   target accuracy — defined by MEDIAN over seeds (subspace orientation selects the
   basin; single-seed values are bimodal and unreliable).
2. **Budget protocol**: separates "block has too few dimensions" from "block is hard
   to learn" via exact-sign controls.
3. **Variational-floor health guard**: abort latent training if energy falls below a
   known lower bound (E_0 or good bound) — costs nothing when E_0 is known, catches
   latent reparameterization pathologies.

## Key Findings

- **Apparent compression can be a variational bound**: on the 4×4 J1–J2 Heisenberg
  model at J2/J1=0.5, a non-negative-amplitude network reaches ε≈0.5271 (positive-cone
  bound E=−4, the diagonal minimum) in d=8 of P=28,642 directions (3,500× compression)
  — but NO such network can go lower. Small d* without sign capability says nothing
  about the ground state.
- **Neither sign nor amplitude is cheap**: with a sign block added (5.4% of params),
  proportional allocation gives it 28/512 dims → error 5.9× above exact-sign control;
  even 1/4 of the sign block leaves error 1.24× higher. **LoRA-style shape-proportional
  budgeting starves small high-demand blocks.**
- **d* tracks the quantum phase transition** (TFIM h/J scan) at ~100× less compute
  than scaling-law fits, but never falls below a **floor set by the random slice itself**.
- **Subspace training is a stabilizer**: zero divergences across 246 subspace runs
  vs repeated full-parameter divergence at 6×6 lattice with identical optimizer settings.
- **QGT conditioning is a poor proxy**: TC2 wins with condition number ~10^10 while
  TC3 loses with 10²–10⁴ — curvature conditioning does not predict optimization quality.
- Linear map (TC2) dominates the tanh nonlinear map (TC3) at every matched d on the
  frustrated system; roughly par on TFIM.

## Implementation Recipe

1. Start from a symmetry-preserving autoregressive ansatz (frozen map cannot break
   normalization/symmetry — no weight constraints needed).
2. Build per-group orthonormal W_k, allocate d proportionally with min 1 per group.
3. Run d-grid {8, 32, 128, 512} with ≥3 seeds; record median best ε_rel per d.
4. Define d* by median-over-seeds gate (e.g., 2× full-parameter reference error).
5. If a low-d success looks suspicious, compute the positive-cone/classical bound of H
   (min diagonal element when off-diagonals ≥ 0) and check whether the network class
   can beat it.
6. For sign-capable models, run exact-sign control (freeze sign to exact, train
   amplitude) to separate amplitude vs sign difficulty before interpreting budgets.

## Scope Caveats
- All results use ONE architecture family (ARNN); exact-sign control repetition in
  other families is the stated next step.
- d* includes the cost of the random slice — report as an upper-bound probe, not a
  pure difficulty measure.
- d* vs compute-scaling-law comparison on shared Hamiltonians still open.
