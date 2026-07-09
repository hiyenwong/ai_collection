---
name: quantum-probabilistic-differential-privacy
description: Quantum probabilistic local differential privacy methodology - structural properties, sample complexity bounds, and hypothesis testing applications for privacy-preserving quantum information processing.
category: quantum
tags: [quantum-privacy, differential-privacy, quantum-statistics, hypothesis-testing, quantum-information]
trigger_words: [quantum differential privacy, quantum local differential privacy, probabilistic privacy, quantum hypothesis testing, privacy sample complexity, quantum privacy loss]
source: arXiv:2607.06307
---

# Quantum Probabilistic Local Differential Privacy

## Overview

Quantum probabilistic local differential privacy (QPLDP) relaxes quantum local differential privacy by allowing the privacy constraint to fail on a spectral violation event with low probability. This quantity can be interpreted as the probability under the quantum superoperation of a quantum privacy-loss violation, closely related to the acceptance probability of the quantum Neyman-Pearson test at a small threshold.

## Core Methodology

### Definition

A quantum mechanism M satisfies (epsilon, delta)-QPLDP if for all input states rho, sigma:
- Pr[privacy-loss > epsilon] <= delta
- where the probability is over the quantum superoperation

### Structural Properties

1. **Tensor-Product Composition**: Properties under tensor-product composition
2. **Unitary Post-Processing**: Behavior under unitary transformations
3. **Non-Convexity**: Generally neither convex nor closed under arbitrary quantum channels
4. **Depolarizing Noise**: Characterization of when depolarizing noise satisfies QPLDP

### Sample Complexity Bounds

Connects quantum probabilistic privacy constraints with statistical inference by deriving lower bounds on probabilistically privatized contraction coefficients in terms of the hockey-stick divergence.

Applications: sample complexity bounds for probabilistically privatized asymmetric and symmetric quantum hypothesis testing.

## Implementation Patterns

### Pattern 1: QPLDP Verification

```python
import numpy as np
from scipy.linalg import eigvalsh

def check_qpldp(mechanism, epsilon, delta, input_states):
    """Verify if mechanism satisfies (epsilon, delta)-QPLDP."""
    violations = []
    for rho, sigma in input_states:
        # Compute privacy loss spectrum
        loss_spectrum = compute_privacy_loss(mechanism, rho, sigma)
        # Probability of violation
        violation_prob = compute_violation_probability(loss_spectrum, epsilon)
        violations.append(violation_prob)
    return max(violations) <= delta

def compute_privacy_loss(mechanism, rho, sigma):
    """Compute privacy loss spectrum for quantum mechanism."""
    # Apply mechanism to both states
    M_rho = mechanism(rho)
    M_sigma = mechanism(sigma)
    # Compute log-likelihood ratio spectrum
    # Uses generalized eigenvalue problem
    return eigvalsh(M_rho, M_sigma)
```

### Pattern 2: Hockey-Stick Divergence Bounds

```python
def hockey_stick_divergence(rho, sigma, epsilon):
    """Compute hockey-stick divergence D_epsilon(rho || sigma)."""
    # D_epsilon(rho || sigma) = Tr[(rho - e^epsilon * sigma)_+]
    diff = rho - np.exp(epsilon) * sigma
    # Positive part: eigenvalues > 0
    eigenvalues = eigvalsh(diff)
    return np.sum(np.maximum(eigenvalues, 0))

def contraction_coefficient_lower_bound(epsilon, delta):
    """Lower bound on privatized contraction coefficient."""
    # Based on hockey-stick divergence
    return 1 - 2 * delta / (np.exp(epsilon) + 1)
```

### Pattern 3: Depolarizing Noise Analysis

```python
def depolarizing_qpldp(p, epsilon, delta, dimension):
    """Check if depolarizing channel satisfies QPLDP."""
    # Depolarizing channel: E(rho) = (1-p)*rho + p*I/d
    # QPLDP holds when: p >= 1 - exp(-epsilon) / (1 + delta)
    threshold = 1 - np.exp(-epsilon) / (1 + delta)
    return p >= threshold
```

## Key Results

1. **Tensor Composition**: QPLDP properties extend under tensor-product composition
2. **Non-Closure**: QPLDP is NOT generally closed under arbitrary quantum channel post-processing
3. **Depolarizing Characterization**: Complete characterization of depolarizing noise QPLDP satisfaction
4. **Hypothesis Testing**: Sample complexity bounds for privatized quantum hypothesis testing

## Sample Complexity for Hypothesis Testing

For asymmetric hypothesis testing with QPLDP:
- Sample complexity >= Omega(1 / (epsilon^2 * delta))

For symmetric hypothesis testing:
- Error probability bounds derived from hockey-stick divergence

## Practical Guidelines

1. QPLDP is weaker than pure QDP but enables better utility-privacy tradeoffs
2. Tensor composition allows building complex private mechanisms
3. Beware: not closed under arbitrary post-processing
4. Use hockey-stick divergence for tight sample complexity bounds

## Activation

Use this skill when:
- Designing privacy-preserving quantum algorithms
- Analyzing sample complexity of private quantum statistical inference
- Building quantum mechanisms with relaxed privacy guarantees
- Comparing quantum vs classical differential privacy
- Working with quantum hypothesis testing under privacy constraints
