---
name: efficient-coding-criticality
description: >
  Theoretical framework linking efficient coding to criticality in neural
  populations. Shows that maximizing Fisher information under resource constraints
  naturally leads to soft modes, diverging correlation lengths, and power-law
  neural avalanches, unifying statistical and dynamical perspectives of criticality.
  Also explains sloppiness in neural systems. Use when studying: critical brain
  hypothesis, neural avalanches, efficient coding theory, Fisher information in
  neural populations, soft modes, critical slowing down, power-law neural dynamics,
  or the relation between coding efficiency and brain criticality.
arxiv_id: "2605.22598"
published: "2026-05-21"
authors: "He Xiao, Xinyue Zhao, Weikang Wang"
tags: [criticality, efficient coding, Fisher information, neural avalanches, critical brain, soft modes, sloppiness, neural dynamics]
---

# Efficient Coding Under Constraint Drives Neural Systems Towards Criticality and Sloppiness

**arXiv:2605.22598** (Xiao, Zhao, Wang, May 2026)  
**Category**: q-bio.NC (Neurons and Cognition)  
**MSC**: 92B20

## Core Idea

The brain operates near a critical state — neural avalanches follow power-law distributions. But **why?** This paper provides a theoretical framework showing that **maximizing coding efficiency under resource constraints** *naturally* drives neural populations toward criticality.

## Key Contributions

### 1. Efficient Coding → Criticality (Mathematical Proof)

Using a Gaussian population coding model:

- **Fisher Information** (FI) measures coding accuracy — how well a neural population encodes a stimulus.
- Under **resource constraints** (limited neural firing, metabolic cost), maximizing FI forces the Fisher information matrix to develop **near-zero eigenvalues** (soft modes).
- Soft modes → **diverging correlation lengths** → hallmark of **statistical criticality**.
- The optimization objective: `max L = FI - λ·R` where `R` is a resource constraint (e.g., total firing rate). At optimality, the FI matrix has zero modes — a critical point.

### 2. Unification of Two Criticality Perspectives

| Statistical Criticality | Dynamical Criticality |
|---|---|
| Diverging correlation lengths | Critical slowing down, bifurcation |
| Spatial correlations span the system | Recovery from perturbation takes infinite time |
| Arises from FI matrix soft modes | Arises from spectral properties of the dynamical operator |

The framework **unifies** both: introducing spatial structure (neighboring neurons have correlated tuning) connects the static FI matrix soft modes to dynamical critical slowing down — the same resource-constrained optimization that produces spatial criticality also produces temporal criticality.

### 3. Explanation of Sloppiness

Sloppiness = the phenomenon where neural systems are insensitive to changes in most parameter directions (only a few "stiff" directions matter).

- The soft modes of the FI matrix define **sloppy directions** — parameter changes along these directions barely affect coding accuracy.
- This is a **natural consequence** of operating at criticality: the system sacrifices sensitivity along irrelevant dimensions to maximize coding along relevant ones.
- Provides a mechanistic link between the **critical brain hypothesis** and **sloppy model phenomenology**.

### 4. Numerical Verification

Power-law neural avalanches emerge from the optimization, confirming the theoretical predictions.

## Mathematical Framework

### Gaussian Population Code

Each neuron has a tuning curve: `r_i(s) = f_i(s) + ε_i` where `f_i(s)` is the mean response to stimulus `s`, and `ε_i` is noise (Gaussian with covariance `Σ`).

### Fisher Information Matrix

`FI_ij = E[∂log p(r|s)/∂θ_i · ∂log p(r|s)/∂θ_j]`

For Gaussian noise: `FI(s) = J(s)^T Σ⁻¹ J(s)` where `J` is the Jacobian of the tuning curves w.r.t. stimulus parameters.

### Resource-Constrained Optimization

`max_{θ} Tr(FI) - λ·||θ||²` or similar regularized objectives. The key is that the constraint prevents the system from having all eigenvalues large — some must go to zero.

### Soft Modes and Criticality

When `FI` has zero eigenvalues, the system is at a critical point in the sense of **parameter space**: changes along soft-mode directions don't affect the coding accuracy (neutral directions). These soft modes correspond to the diverging length scales of statistical criticality.

### Unification via Spatial Structure

Introduce spatial coupling between neurons (nearby neurons have similar tuning). The FI matrix becomes approximately:
`FI ≈ N·(I + α·L)` where `L` is the graph Laplacian of the neural network. Near criticality, `α → α_c` at which point `(I + α·L)` becomes singular — the correlation length diverges AND the dynamical time scale diverges.

## Relation to Existing Theories

| Theory | Connection |
|---|---|
| **Critical Brain Hypothesis** | Provides the *mechanistic why* — criticality is a consequence of optimal coding under constraints |
| **Self-Organized Criticality (SOC)** | The optimization process naturally self-organizes to criticality without fine-tuning |
| **Efficient Coding Hypothesis** | Directly linked — the efficiency objective itself drives criticality |
| **Sloppy Model Theory** | Sloppiness is a byproduct of criticality, not a separate phenomenon |

## Key Results

- Fisher information maximization under resource constraints → **soft modes** → **criticality**
- Spatial structure unifies **statistical** and **dynamical** criticality
- Sloppiness emerges naturally as a consequence of critical dynamics
- Power-law avalanches confirmed numerically

## Limitations

- **Gaussian approximation**: Real neural noise is not Gaussian — Poisson-like (mean-variance coupling). The framework may need extension to non-Gaussian noise.
- **Single population**: Model considers one neural population; real brains have hierarchical, multi-region organization.
- **Static optimization**: The optimization is at equilibrium — doesn't capture how the brain dynamically adapts to changing constraints in real time.

## Activation Keywords

- critical brain hypothesis
- neural avalanches
- efficient coding
- Fisher information neural population
- soft modes neural dynamics
- critical slowing down brain
- sloppiness neural systems
- power-law neural activity
- resource-constrained coding
