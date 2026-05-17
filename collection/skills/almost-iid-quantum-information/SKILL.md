---
name: almost-iid-quantum-information
description: "Almost i.i.d. information theory methodology — alternative frameworks for quantum information analysis using Wasserstein distance and k-body marginals, relaxing the stringent i.i.d. assumption for practical quantum protocols under realistic noise conditions. Use when analyzing quantum information theory, quantum protocols under non-i.i.d. conditions, quantum Wasserstein distance, k-body marginals, or quantum resource manipulation."
---

# Almost i.i.d. Quantum Information Theory

## Methodology

Relax the stringent i.i.d. (independent and identically distributed) assumption in quantum information theory using two alternative definitions:

### 1. Quantum Wasserstein Distance Framework

Define almost i.i.d. states via normalized quantum Wasserstein distance:

$$\text{Almost-i.i.d.} \iff \frac{1}{n} \|\rho_n - \sigma^{\otimes n}\|_W \leq \epsilon$$

where $\|\cdot\|_W$ is the quantum Wasserstein distance and $\sigma^{\otimes n}$ is the i.i.d. reference.

### 2. Average k-body Marginals Framework

Define almost i.i.d. states via convergence of k-body marginals:

$$\frac{1}{\binom{n}{k}} \sum_{S:|S|=k} \|\rho_S - \sigma^{\otimes k}\|_1 \leq \epsilon_k$$

### Key Results

- Strict hierarchical relationship between the two definitions
- Wasserstein distance definition implies k-body marginal definition
- Both frameworks are strictly weaker than the i.i.d. assumption
- Enable analysis of quantum protocols under realistic correlated noise

## Application Patterns

### Quantum Protocol Analysis

1. Replace i.i.d. assumption with almost-i.i.d. framework
2. Bound protocol performance using Wasserstein or marginal distance
3. Derive finite-size corrections for non-i.i.d. settings

### Resource Manipulation

1. Characterize target states via almost-i.i.d. approximations
2. Compute distillation rates under correlated noise
3. Apply composite generalized quantum Stein's lemma for rate bounds

## Activation Keywords
- almost i.i.d., quantum Wasserstein distance, k-body marginals
- non-i.i.d. quantum protocols, quantum information theory
- quantum resource distillation, composite Stein's lemma

## References
- arXiv:2605.15114 — "New approaches to almost i.i.d. information theory"
- Girardi, De Palma, Lami (2026)
