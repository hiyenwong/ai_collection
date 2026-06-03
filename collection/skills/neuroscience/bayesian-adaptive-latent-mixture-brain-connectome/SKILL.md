---
name: bayesian-adaptive-latent-mixture-brain-connectome
description: "Bayesian adaptive latent mixture model for zero-inflated weighted brain connectome analysis. Use when analyzing structural/functional brain networks with many zero-valued edges, modeling subject-level mixture of shared connectivity templates, or performing Bayesian inference on connectome data with Hurdle likelihoods."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.12901"
  published: "2026-05-13"
  authors: "Hsin-Hsiung Huang, Yuh-Haur Chen, Teng Zhang"
  tags: [bayesian, brain-connectome, zero-inflated, latent-mixture, HCP, hamiltonian-monte-carlo]
---

# Bayesian Adaptive Latent Mixture Model for Zero-Inflated Weighted Brain Connectome Analysis

**arXiv:2605.12901** | Submitted 13 May 2026 | stat.ME, stat.AP, stat.CO

## Core Concept

Replicated weighted brain networks exhibit many structural zeros (absent edges) alongside heterogeneous non-zero edge strengths. In structural connectomics, this zero-inflation coincides with subjects expressing overlapping (rather than discrete) connectivity patterns. This paper proposes a **Bayesian adaptive latent mixture model** that represents each subject network as a simplex mixture of shared low-rank latent score matrices, integrated with a **hurdle likelihood** that separates edge existence from conditional edge strength.

## Key Insights

1. **Zero-Inflated Weighted Networks**: Uses a Hurdle likelihood model that separates the binary event of edge existence from the conditional distribution of edge strength given existence. A sparsity-coupling parameter θ enables absent edges to be either independent of, or informative about, latent connectivity.

2. **Shared Low-Rank Templates**: Each subject's connectome is a convex combination (simplex mixture) of shared low-rank latent score matrices (templates), capturing overlapping rather than discrete connectivity patterns.

3. **Theoretical Guarantees**: Establishes posterior consistency, local asymptotic normality, a Bernstein-von Mises approximation, and predictive consistency for an identifiable quotient-space estimand under fixed-template scenarios.

4. **Computation via Transformed HMC**: Uses transformed Hamiltonian Monte Carlo on unconstrained coordinates. Selects number of templates via predictive fit, held-out link prediction, and template stability.

5. **Human Connectome Project Validation**: Applied to HCP data, the model recovers stable latent score patterns and heterogeneous subject-level mixtures. Behavioral analyses serve as exploratory annotations.

## Method Components

### Hurdle Likelihood
```
P(Y_ij | θ, π_ij, μ_ij) = 
  (1-π_ij)^(1-Y_ij) × [π_ij × f(Y_ij | μ_ij)]^(Y_ij)
```
Where Y_ij is edge weight, π_ij is edge existence probability, and μ_ij is conditional edge strength.

### Latent Mixture Model
Each subject network A^(s) is modeled as:
```
A^(s) = Σ_{k=1}^K w_k^(s) × L_k + ε
```
Where w^(s) is a simplex weight vector over K templates, L_k are shared low-rank latent score matrices.

## Applications

- **Structural connectome analysis** with tractography-derived edge weights (often zero-inflated)
- **Functional connectome analysis** where correlation thresholds induce zeros
- **Cross-subject connectome comparison** with heterogeneous connectivity patterns
- **Connectome-based behavioral prediction** with uncertainty quantification
- **Template discovery** in population-level brain network studies

## Activation Keywords

- zero-inflated brain connectome
- Bayesian latent mixture model
- Hurdle likelihood connectome
- structural connectome HCP
- Hamiltonian Monte Carlo connectome
- Bayesian adaptive mixture
- shared latent template brain network
- posterior consistency connectome
- overlapping connectivity patterns

## References

- Huang, Chen & Zhang (2026). A Bayesian Adaptive Latent Mixture Model for Zero-Inflated Weighted Brain Connectome Analysis. arXiv:2605.12901
