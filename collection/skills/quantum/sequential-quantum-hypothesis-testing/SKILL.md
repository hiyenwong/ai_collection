---
name: sequential-quantum-hypothesis-testing
description: "Composite Sequential Quantum Hypothesis Testing (SQHT) methodology — adaptive measurement selection for distinguishing null quantum states from sets of alternatives using mixture-sequential quantum probability ratio tests. Achieves optimal Type-I and Type-II error exponents characterized by minimal measured relative entropies. Activation: sequential quantum hypothesis testing, SQHT, quantum probability ratio test, quantum state discrimination, composite hypothesis testing, quantum error exponents."
---

# Sequential Quantum Hypothesis Testing (SQHT)

Research methodology for composite sequential quantum hypothesis testing based on Simpson, Palias, and Jose (arXiv: 2605.04915).

## Overview

Sequential quantum hypothesis testing addresses the problem of distinguishing a null quantum state from a **set** of alternative quantum states (composite hypothesis). The key innovation is the **mixture-sequential quantum probability ratio test** that adaptively selects measurements based on the current mixture estimate of the alternative set, stopping upon the first threshold crossing of the mixture log-likelihood ratio.

## Key Concepts

### 1. Composite vs. Simple SQHT

- **Simple SQHT**: Distinguish one state from one alternative → well-understood
- **Composite SQHT**: Distinguish one state from a **set** of alternatives → significantly harder
- Need to handle the **worst-case** alternative in the set
- Adaptive measurement selection is crucial for optimality

### 2. Mixture-Sequential Quantum Probability Ratio Test

- Maintain a **mixture estimate** over the alternative set
- Adaptively select measurements based on current mixture
- Stop when mixture log-likelihood ratio crosses a threshold
- Simultaneously achieves optimal Type-I and worst-case Type-II error exponents

### 3. Error Exponents

- **Type-I error exponent**: Characterized by measured relative entropy to the closest alternative
- **Type-II error exponent**: Characterized by **minimal** measured relative entropy between null and alternative set
- Sample complexity at least as large as sequential testing between two fixed states

## Methodology

### Mixture-Sequential Test Algorithm

```python
import numpy as np
from scipy.optimize import minimize

def mixture_sequential_qpt(
    null_state,
    alternative_set,
    max_measurements=100,
    threshold_type1=10,
    threshold_type2=10,
    mixture_weights=None
):
    """
    Mixture-Sequential Quantum Probability Ratio Test.
    
    Adaptively selects measurements to distinguish null state
    from a set of alternatives with optimal error exponents.
    
    Args:
        null_state: Null quantum state (density matrix)
        alternative_set: List of alternative quantum states
        max_measurements: Maximum number of adaptive measurements
        threshold_type1: Threshold for Type-I error control
        threshold_type2: Threshold for Type-II error control
        mixture_weights: Initial weights over alternatives
    
    Returns:
        decision: 'null' or 'alternative'
        n_measurements: Number of measurements used
        log_likelihood_ratio: Final LLR value
    """
    if mixture_weights is None:
        mixture_weights = np.ones(len(alternative_set)) / len(alternative_set)
    
    llr = 0.0
    n_measurements = 0
    
    for step in range(max_measurements):
        # Step 1: Compute optimal measurement for current mixture
        mixture_state = sum(
            w * alt for w, alt in zip(mixture_weights, alternative_set)
        )
        measurement = optimal_measurement(null_state, mixture_state)
        
        # Step 2: Perform measurement and get outcome
        outcome = perform_measurement(measurement, true_state)
        
        # Step 3: Update log-likelihood ratio
        llr += log_likelihood_ratio(outcome, null_state, mixture_state, measurement)
        n_measurements += 1
        
        # Step 4: Update mixture weights (Bayesian update)
        mixture_weights = update_mixture_weights(
            mixture_weights, alternative_set, outcome, measurement
        )
        
        # Step 5: Check stopping conditions
        if llr >= threshold_type1:
            return 'alternative', n_measurements, llr
        if llr <= -threshold_type2:
            return 'null', n_measurements, llr
    
    # Timeout: return based on sign of LLR
    return 'alternative' if llr > 0 else 'null', n_measurements, llr
```

### Optimal Error Exponent Computation

```python
def compute_optimal_error_exponents(null_state, alternative_set):
    """
    Compute the optimal Type-I and Type-II error exponents
    for composite SQHT.
    
    The exponents are characterized by the minimal measured
    relative entropies between the null state and the alternative set.
    
    Returns:
        type1_exponent, type2_exponent
    """
    # Type-II exponent: min over alternatives of measured relative entropy
    type2_exponent = min(
        measured_relative_entropy(null_state, alt)
        for alt in alternative_set
    )
    
    # Type-I exponent: determined by the geometry of the alternative set
    # Involves solving a convex optimization over the set
    type1_exponent = compute_type1_exponent(null_state, alternative_set)
    
    return type1_exponent, type2_exponent


def measured_relative_entropy(rho, sigma):
    """
    Compute the measured relative entropy between two quantum states.
    
    D_M(rho || sigma) = sup_{M} D(P_rho^M || P_sigma^M)
    
    where the supremum is over all POVMs M, and D is the
    classical relative entropy of the outcome distributions.
    """
    # For commuting states: reduces to classical KL divergence
    # For general states: requires optimization over measurements
    return optimize_measurement_relative_entropy(rho, sigma)
```

### Sample Complexity Lower Bound

```python
def sample_complexity_lower_bound(null_state, alternative_set, target_error):
    """
    Compute the minimum expected sample complexity required
    to achieve vanishing error probabilities.
    
    Theorem: Composite SQHT requires expected sample complexity
    at least as large as sequential testing between two fixed states.
    
    Args:
        null_state: Null quantum state
        alternative_set: Set of alternative states
        target_error: Desired error probability
    
    Returns:
        Minimum expected number of measurements
    """
    # Lower bound from simple SQHT between null and closest alternative
    closest_alt = min(alternative_set, 
                       key=lambda alt: measured_relative_entropy(null_state, alt))
    
    D_min = measured_relative_entropy(null_state, closest_alt)
    
    # Sample complexity ~ |log(error)| / D_min
    return np.abs(np.log(target_error)) / D_min
```

## Applications

### 1. Quantum State Verification

- Verify prepared quantum states match target specifications
- Handle uncertainty in the set of possible errors
- Minimizes measurement resources while guaranteeing error bounds

### 2. Quantum Channel Discrimination

- Distinguish quantum channels from a set of possible alternatives
- Adaptive measurement selection maximizes discrimination power
- Applications in quantum communication and sensing

### 3. Quantum Metrology

- Sequential hypothesis testing for parameter estimation
- Adaptive measurements achieve better precision than fixed strategies
- Connects to quantum Cramér-Rao bounds

### 4. Quantum Anomaly Detection

- Detect deviations from expected quantum behavior
- Handle composite alternatives (any deviation from nominal)
- Sample-efficient detection with guaranteed error rates

## Design Patterns

### Pattern 1: Mixture-Based Adaptivity

When facing a composite hypothesis (set of alternatives):
1. Maintain a probability mixture over the alternative set
2. Select measurements that are optimal for the current mixture
3. Update mixture weights based on measurement outcomes
4. The mixture automatically focuses on the most likely alternative

### Pattern 2: Sequential Stopping with Thresholds

For resource-efficient quantum state discrimination:
1. Compute running log-likelihood ratio after each measurement
2. Set thresholds based on desired error probabilities
3. Stop as soon as a threshold is crossed
4. This achieves optimal sample complexity asymptotically

### Pattern 3: Measured Relative Entropy as Figure of Merit

For quantum hypothesis testing performance analysis:
1. Measured relative entropy D_M characterizes optimal error exponents
2. D_M ≥ standard quantum relative entropy (with equality for commuting states)
3. Optimizing over measurements gives the best achievable performance
4. Connects to operational quantities in quantum information theory

## Connection to Classical Statistics

| Classical Concept | Quantum Analogue |
|-------------------|------------------|
| Likelihood ratio | Quantum probability ratio |
| KL divergence | Measured relative entropy |
| Wald's SPRT | Mixture-sequential quantum test |
| Error exponents | Minimal measured relative entropy |
| Sample complexity | Expected number of quantum measurements |

## Error Analysis

### Finite-Sample Behavior

- Asymptotic results assume unlimited measurements
- For finite samples, use concentration inequalities
- Bootstrap methods for confidence interval estimation

### Measurement Optimization

- Finding optimal measurements is computationally hard in general
- Use convex relaxation or iterative algorithms
- For small systems, exact optimization via semidefinite programming

## References

- Simpson, J.P., Palias, E., & Jose, S.T. (2026). Optimal Error Exponents for Composite Sequential Quantum Hypothesis Testing. arXiv: 2605.04915.
- Related: `quantum-statistical-estimation`, `quantum-f-divergence-contraction`, `quantum-proper-scoring-rules`
