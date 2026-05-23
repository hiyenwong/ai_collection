---
name: non-gaussian-entanglement-hierarchy
description: "Schmidt number-based hierarchy for characterizing and classifying non-Gaussian entanglement in continuous variable quantum systems. Provides a framework for understanding entanglement structures beyond Gaussian states. Trigger words: non-Gaussian entanglement, Schmidt number hierarchy, continuous variable entanglement, entanglement classification, CV quantum entanglement, Schmidt number characterization."
---

# Non-Gaussian Entanglement Hierarchy

## Description
A hierarchical framework for characterizing non-Gaussian entanglement in continuous variable (CV) quantum systems based on the Schmidt number. This methodology extends entanglement classification beyond Gaussian states, providing tools to understand and quantify complex entanglement structures in photonic and bosonic systems.

## Activation Keywords
- non-Gaussian entanglement
- Schmidt number hierarchy
- continuous variable entanglement
- entanglement classification
- CV quantum entanglement
- Schmidt number characterization
- 非高斯纠缠层次
- bosonic entanglement hierarchy

## Core Concepts

### 1. Schmidt Number for CV Systems
The Schmidt number generalizes to continuous variable systems:

```
Schmidt Number K:
K = 1 / Σ_i λ_i²
where λ_i are Schmidt coefficients

For bipartite state |ψ⟩ = Σ_i λ_i |i_A⟩|i_B⟩

Interpretation:
- K = 1: product state (no entanglement)
- K → ∞: maximally entangled
- Larger K = more complex entanglement structure
```

### 2. Non-Gaussian Entanglement Hierarchy
Classification beyond Gaussian states:

```
Level 0: Product states (K=1)
Level 1: Gaussian entangled states (squeezed, two-mode)
Level 2: Weakly non-Gaussian (small photon additions/subtractions)
Level 3: Moderately non-Gaussian (cat states, GKP states)
Level 4: Strongly non-Gaussian (complex superpositions)
Level n: Arbitrary non-Gaussian entanglement
```

### 3. Characterization Tools
For classifying entanglement at each level:

- **Gaussian states**: Covariance matrix analysis, logarithmic negativity
- **Weakly non-Gaussian**: Perturbation theory, photon statistics
- **Moderately non-Gaussian**: Wigner function negativity, fidelity measures
- **Strongly non-Gaussian**: Full state tomography, Schmidt decomposition

### 4. Applications
- **Quantum communication**: Higher Schmidt numbers enable better channel capacity
- **Quantum metrology**: Non-Gaussian entanglement surpasses Gaussian limits
- **Quantum computing**: Resource states for CV quantum computation
- **Quantum sensing**: Enhanced sensitivity through non-Gaussian correlations

## Usage Patterns

### Pattern 1: Entanglement Classification
1. Obtain quantum state description (density matrix or wavefunction)
2. Compute Schmidt decomposition
3. Calculate Schmidt number K
4. Classify into hierarchy level
5. Determine appropriate characterization tools

### Pattern 2: Resource Assessment
1. Identify target quantum protocol/application
2. Determine required entanglement level
3. Compare available states using Schmidt number hierarchy
4. Select optimal resource states
5. Quantify gap between available and required entanglement

## Instructions for Agents

### When analyzing entanglement papers:
1. Check if the paper addresses non-Gaussian entanglement
2. Identify the classification framework (Schmidt number or other)
3. Extract quantitative measures (K values, negativity, etc.)
4. Note the specific CV system (optical, mechanical, etc.)
5. Map results to the hierarchy levels

### When designing quantum protocols:
1. Determine entanglement requirements (Gaussian vs non-Gaussian)
2. Use Schmidt number hierarchy to assess resource states
3. Consider practical generation methods for each level
4. Account for decoherence effects on entanglement structure

## Error Handling
### Schmidt Number Computation
- For infinite-dimensional CV systems, truncate basis appropriately
- Verify convergence of Schmidt coefficient series
- Use numerical methods for complex states

### Classification Ambiguity
- Some states may span multiple hierarchy levels
- Use multiple characterization tools for cross-validation
- Consider the specific application context

## Resources
- arXiv: 2605.18605 - "Non-Gaussian Entanglement Hierarchy Based on the Schmidt Number"
- Continuous variable quantum information theory
- Schmidt decomposition for bipartite systems
- Gaussian vs non-Gaussian quantum states

## Related Skills
- quantum-entanglement-detection: General entanglement detection
- bosonic-gkp-parity-encoding: GKP state encoding
- quantum-neuromorphic-patterns: Quantum resources for neuromorphic
