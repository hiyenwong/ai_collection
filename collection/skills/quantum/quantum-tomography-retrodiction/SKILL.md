---
name: "quantum-tomography-retrodiction"
description: "Methodology connecting quantum state tomography and quantum retrodiction through the Petz recovery map. Shows Petz map is precisely the gradient update of log-likelihood in maximum-likelihood tomography. Includes noncommutative generalization for arbitrary quantum channels. Use for quantum state estimation, quantum error correction, quantum metrology, or measurement channel recovery."
metadata:
  arxiv_id: "2606.23777"
  published: "2026-06-22"
  authors: "Sebastian Murk, Ian Tan, Fabian M\u00fcller, Dominik \u0160afr\u00e1nek"
  tags: [quantum, tomography, retrodiction, statistics, estimation, petz-map]
---

# Quantum Tomography-Retrodiction Framework

## Core Concept

Quantum state tomography and quantum retrodiction are manifestations of the same underlying principle: the Petz recovery map associated with a measurement channel is precisely the gradient update of the log-likelihood used in maximum-likelihood tomography.

## Mathematical Framework

### Petz Map as Gradient Update

Given a measurement channel E and measurement outcomes, the Petz recovery map P_E applied to the observed statistics equals the gradient ascent step on the log-likelihood function:

```
P_E(\rho) = argmax_\rho log L(\rho | data)
```

### Key Properties

1. **Monotonic Likelihood**: Repeated applications of the Petz map monotonically increase the likelihood
2. **Noncommutative Generalization**: The Petz map generalizes from measurement channels to arbitrary quantum channels
3. **Unified View**: Tomography (forward estimation) and retrodiction (backward inference) share the same mathematical structure

## Usage Patterns

### Pattern 1: Maximum-Likelihood Tomography via Petz Map

When performing quantum state tomography, use the Petz recovery map as an iterative optimization procedure:

1. Define the measurement channel E from the POVM elements
2. Initialize with a prior state (often maximally mixed)
3. Apply Petz map iteratively: \rho_{n+1} = P_E(\rho_n)
4. Convergence guaranteed by monotonic likelihood property

### Pattern 2: Retrodiction for Error Correction

When a quantum error channel E has occurred:

1. Model the error as a quantum channel E
2. Construct the Petz recovery map P_E
3. Apply P_E to the corrupted state for optimal recovery
4. This generalizes beyond measurement channels to arbitrary noise

### Pattern 3: Connection to Bayesian Inference

The Petz retrodiction map is the quantum analogue of Bayesian inference:
- Classical: P(A|B) = P(B|A)P(A)/P(B)
- Quantum: P_E(\rho) = \sqrt{\rho} E^*(\sigma^{-1}) \sqrt{\rho}
- Where \sigma = E(\rho) is the reference state

## Methodology Steps

1. **Identify the channel**: Determine the measurement or noise channel E
2. **Compute the Petz map**: P_E(\cdot) = \sqrt{\rho} E^*(E(\rho)^{-1/2} (\cdot) E(\rho)^{-1/2}) \sqrt{\rho}
3. **Iterate for convergence**: Repeated application monotonically improves likelihood
4. **Verify positivity**: Petz map preserves complete positivity by construction

## Pitfalls

### Numerical Stability

- The Petz map requires matrix inversion (E(\rho)^{-1/2}) which can be numerically unstable
- Regularize with small identity term: (E(\rho) + \epsilon I)^{-1/2}
- Use SVD-based inversion for ill-conditioned channels

### Channel Representation

- Ensure the channel E is completely positive and trace-preserving (CPTP)
- For measurement channels, verify the POVM elements sum to identity
- For general channels, verify Kraus representation validity

## Activation

- quantum tomography, quantum retrodiction, Petz recovery map, maximum likelihood tomography, quantum state estimation, measurement channel recovery, quantum error correction, noncommutative Bayes, 量子态层析, 量子回溯推断
