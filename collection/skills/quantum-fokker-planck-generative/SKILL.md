---
name: quantum-fokker-planck-generative
description: "Use when quantum generative models train as FP solvers."
category: quantum-computing
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [quantum-machine-learning, generative-models, fokker-planck, langevin-dynamics, qsvt, block-encoding, quantum-simulation, model-discovery]
    related_skills: [qdiffusion-time-series, latent-conditioned-pqc-universal-approximator, lindbladian-learning-qec, jeffreys-flow-sampling, physics-guided-generative-optimization]
trigger: quantum generative model, Fokker-Planck, Langevin process, stationary density, quantum circuit Born machine alternative, barren plateaus, QSVT, quantum singular value transformation, block encoding, imaginary time evolution, ground state preparation, Hubbard-Stratonovich, linear combination of cosines, Gauss-Hermite quadrature, exponential family, physics-informed parameterization, quantum model discovery, Born rule sampling, MMD loss, parameter recovery, convex training, correlated multivariate distributions, potential parameterization
---

# Quantum Fokker–Planck Solvers as Trainable Generative Models

**Source**: "Quantum Fokker-Planck solvers as trainable generative models" — Tariq Mahassen, Marcin Jastrzebski, Oleksandr Kyriienko (University of Sheffield), arXiv:2610.31330 (quant-ph, cs.LG, 22 Oct 2026).

## When to Use

Use when building a **quantum generative model** that must stay trainable at scale (no barren plateaus, parameter count independent of Hilbert-space size); when a target distribution is plausibly the stationary law of a diffusive process (physical, chemical, financial data with a drift structure); when quantum model discovery — recovering the *dynamics* behind data, not just mimicking samples — is the goal; when designing QSVT/imaginary-time circuits for non-Hermitian PDEs (Fokker–Planck, Kolmogorov, Smoluchowski); when a classical MCMC sampler mixes badly (small σ, multi-well potentials).

## Core Idea

Do NOT train circuit angles. **Parameterize the potential of an overdamped Langevin process** and make the circuit a *solver* that prepares the stationary distribution:
```
dXt = −∇V(Xt)·dt + σ·dWt,   V(x;θ) = Σj θj·vj(x)   (fixed dictionary, e.g. monomials)
pss(x) = Z(θ)⁻¹ · exp(−2V(x;θ)/σ²)   →  pθ is an EXPONENTIAL FAMILY
   natural parameters: −2θj/σ²;  sufficient statistics: vj(x)
```
- **K trainable parameters fixed by the dictionary** (degree-r monomials: K ≤ C(d+r,r)−1), **independent of the N^d grid**; the prepared state spans dn = d·log₂N qubits. This unties parameter count from expressivity-vs-qubits coupling that cripples PQCs.
- Sampling = **computational-basis measurement** of the prepared state (Born rule); marginals by discarding registers; one shot per joint sample.
- Trained coefficients θ ARE the drift of an SDE consistent with the data → **quantum model discovery** (identifiable: V = −(σ²/2)·log pss + const).

## Pipeline (4 stages)

**A. Hermitianization.** FP generator is non-Hermitian. Similarity transform p = e^{−V/σ²}ψ casts it as imaginary-time Schrödinger:
```
∂tψ = −Hψ,   H = −(σ²/2)∇² + Veff,   Veff = |∇V|²/(2σ²) − ΔV/2   (self-adjoint)
Guarantee H ⪰ 0 by FACTORIZATION H = A†A,   A = (σ/√2)∂x + V′(x)/(√2·σ)  (1d)
Ground state of H encodes √pθ.  NOTE: the model generates STATIONARY states only — ITE dynamics ≠ FP relaxation transients.
```
**B. Block encoding of A.** Central-difference discretization → A = periodic tridiagonal (shift part (S+−S−) via QFT-conjugated shifts + diagonal V′(xi)):
```
Diagonal grid operator G = diag(x0..xN−1) via LCU  →  QSVT polynomial transformation maps xi → V′(xi)
TRAINABLE θ ENTER AS QSVT PHASE ANGLES {φk} (parameter re-uploaded through the sequence)
LCU combines S± and UV′ into block encoding UA.
```
**C. Ground state via linear combination of cosines (LCCO).** Imaginary-time filter e^{−tH} = e^{−tB²} on the Hermitian dilation B:
```
Hubbard–Stratonovich:  e^{−B²t} = (1/√π)∫ e^{−χ²}·e^{−i2√t·χ·B} dχ
Gauss–Hermite quadrature (Stieltjes + Golub–Welsch, D nodes) + node symmetry χ−j=−χj, w−j=wj → imaginary terms cancel EXACTLY:
e^{−B²t} ≈ (2/√π)·Σ_{χj>0} wj·cos(2√t·χj·B)
```
Cosines are real even functions — **native QSVT**, no protocol extensions; symmetry halves LCU branches. Convergence: t = O(log(1/ε)/Δ) (spectral gap Δ = E1−E0); D even for convenience (χ=0 branch folds into the polynomial).
**D. Measure & train.** Sample by basis measurement; update θ via MMD² or KL between generated and empirical samples.

## Training Geometry

- Exponential-family likelihood in natural params η = −2θ/σ² → **convex, sample-efficient** for in-distribution targets regardless of dimension; sufficient statistics vj(x) are the only data statistics needed in principle.
- Empirics: single-basin loss landscape with **anisotropic curvature** (partially compensating coefficients form weakly-constrained valleys — e.g. larger quadratic + smaller quartic give similar widths); coefficients still individually identifiable.
- MMD² and KL reach comparable optima (KL usually fewer iterations); 2d/3d correlated, multimodal, crescent targets recovered to residuals orders of magnitude below target amplitude in 10–150 iterations.

## Pitfalls

- **Finite filter displaces the minimum**: with imaginary time t or quadrature order D too small, excited states survive and the loss landscape's argmin is SHIFTED from true θ — train only after the filter converges (validate landscape vs exact ground state first).
- **σ is not identified by pss alone**: only natural params η* = −2θ*/σ² are recoverable from the stationary density; separate trajectory data needed for σ (or absorb σ into θ and reinterpret).
- **Gate count > QCBM**: this is a fault-tolerant-device architecture, not NISQ — the payoff is trainability at scale + correlated high-d targets, not near-term deployment.
- **Model class = FP-reachable distributions**: data outside the potential-dictionary family is out-of-distribution; the convexity guarantee is in-distribution only.
- Classical baselines: grid evaluation of Z(θ) is exponential in d; MCMC mixing degrades for small σ / well-separated minima — the regime where the quantum sampler is most attractive.

## Recipe

1. Choose potential dictionary (monomials up to degree r; couplings like x1x2 for correlations); set σ or plan to absorb it.
2. Discretize [−L,L]^d, N=2^n per coordinate; assemble A; verify H=A†A ⪰ 0.
3. Fix imaginary time t ≥ c·log(1/ε)/Δ and even D; build LCCO schedule (Gauss–Hermite weights).
4. Optimize θ (MMD² with a fixed kernel, or KL / exponential-family likelihood on sufficient stats) until landscape converges; monitor for the valley anisotropy.
5. Sample: repeat basis measurements; verify marginals by register discarding.
6. Report recovered SDE drift −∇V(x;θ̂) as the discovered model.

## Connections

- QSVT-as-training-substrate: parameter re-upload generalizes LCU/QSVT blocks from fixed functions to trainable maps (cf. latent-conditioned PQCs).
- Hubbard–Stratonovich/LCCO is a general trick for implementing non-unitary e^{−tH} filters whenever H = B² or H = A†A — reusable beyond FP (Kolmogorov backward equations, reaction–diffusion, optimization filters).
- Versus QCBMs: same Born-rule sampling, but parameters live in a physics dictionary instead of rotation angles — kills barren plateaus by construction and decouples parameter count from qubit count.
- Finance bridge: stationary densities of mean-reverting/resilient-market processes are exactly pss of Langevin dynamics — a quantum FP solver is a candidate sampler for correlated financial scenarios once fault-tolerant hardware exists.
