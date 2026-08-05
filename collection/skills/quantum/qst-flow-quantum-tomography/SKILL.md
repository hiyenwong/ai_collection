---
name: qst-flow-quantum-tomography
description: "QST-Flow framework for continuous-variable quantum state tomography using flow-based generative modeling. Models Husimi-Q functions with QST-QFlow and Wigner functions with QST-WFlow as difference of normalized flows. Use when working with non-Gaussian bosonic states, phase-space tomography, or quantum state reconstruction."
metadata:
  arxiv_id: "2607.21584"
  published: "2026-07-23"
  authors: "Owen Dugan, Rumen Dangovski, Peter Y. Lu, Di Luo"
  tags: [quantum, tomography, flow-based, continuous-variable, Wigner, Husimi-Q]
license: Complete terms in LICENSE.txt
---

# QST-Flow: Flow-based Phase-space Tomography

## Overview

QST-Flow is a quantum state tomography framework that uses flow-based generative modeling to represent experimentally accessible phase-space quasiprobability distributions. Instead of truncating density matrices or using fixed grids, QST-Flow represents quantum states with normalized, samplable neural densities.

## Key Components

### QST-QFlow
- Models the positive Husimi-Q function with a single normalizing flow
- Provides normalized probability model for coherent-state measurements
- Enables exact density evaluation and direct sampling

### QST-WFlow  
- Models sign-changing Wigner functions as a trainable difference of two normalized flows
- Explicitly captures negativity while preserving normalization
- Handles interference fringes and negative lobes that carry non-classical information

## Methodology

1. **Phase-space representation**: Work directly in continuous phase space without grid discretization
2. **Flow-based modeling**: Use invertible transformations with tractable Jacobians
3. **Normalization preservation**: Ensure quasiprobability distributions remain properly normalized
4. **Importance sampling**: Learn from finite phase-space measurements without fixed grid constraints
5. **Difference-of-flows construction**: For Wigner functions, represent as Q₁(α) - Q₂(α) where both Q₁ and Q₂ are normalized flows

## Applications

- Single-mode non-Gaussian state reconstruction (cat, binomial, GKP, number, Fock states)
- Extension to multimode states
- Robust reconstruction from noisy Wigner data
- Measurement-efficient tomography of nonclassical bosonic systems

## Advantages over Prior Methods

- Avoids Fock-basis truncation limitations
- No fixed grid resolution constraints
- Exact density evaluation and direct sampling capabilities
- Improved reconstruction error compared to QST-CGAN and other ML tomography methods
- Scalable to higher-dimensional phase spaces

## Implementation Considerations

- Requires normalizing flow architectures with invertible transformations
- Training uses importance-sampled likelihood estimates from experimental measurements
- For Wigner functions, ensure both component flows are properly normalized
- Validate reconstruction quality using quantum fidelity bounds

## Activation Keywords
- qst-flow
- quantum tomography flow
- phase-space tomography
- continuous-variable tomography
- Wigner flow modeling
- Husimi-Q flow

## References
- Original paper: arXiv:2607.21584
- Related: quantum-state-tomography, flow-based-generative-modeling, continuous-variable-quantum