---
name: random-projection-quantum-algorithms
category: quantum-algorithms
description: Random projections framework for multi-copy quantum algorithms — estimating nonlinear properties of quantum states (multivariate traces, Rényi entropies) with reduced coherent operations. Use when designing multi-copy quantum algorithms, estimating nonlinear observables, or reducing circuit depth for state characterization.
trigger_words: ["random projections quantum", "multi-copy quantum", "nonlinear observables", "quantum state estimation", "Rényi entropy quantum", "multivariate traces", "swap test alternative"]
source: arxiv:2606.20238
---

# Random Projections for Multi-Copy Quantum Algorithms

## Overview

Framework for multi-copy quantum algorithms using random projections to estimate nonlinear properties of quantum states, reducing the coherent operations needed for multivariate traces and nonlinear observables.

**arXiv**: 2606.20238 (2026-06-18)  
**Authors**: Xiaoyu Liu, Jordi Tura, Johannes Knörzer

## Core Methodology

### The Problem

Estimating nonlinear properties of quantum states requires:
- Multivariate traces: Tr(ρ₁·ρ₂·...·ρ_K)
- Nonlinear observables: Tr(ρ^K) for integer K
- Standard approach: swap tests requiring coherent operations on full Hilbert space
- Becomes infeasible for large systems

### Random Projection Framework

**Key Insight**: Instead of operating on the full Hilbert space, use random projections to reduce dimensionality while preserving the nonlinear properties of interest.

### Core Steps

1. **Random projection design**: Construct random unitary transformations that project K-copy states into smaller subspaces
2. **Local measurement**: Perform measurements on the projected subspaces
3. **Statistical estimation**: Combine measurement outcomes to estimate the target nonlinear property
4. **Error bounds**: Concentration inequalities guarantee estimation accuracy with sufficient samples

### Mathematical Foundation

- **Multivariate trace estimation**: Tr(ρ₁...ρ_K) = Σ_i p_i · Tr(M_i · (ρ₁⊗...⊗ρ_K))
- **Random projections**: Replace global swap tests with randomized local measurements
- **Classical post-processing**: Combine outcomes using efficient classical algorithms

## Implementation Patterns

### Pattern 1: Nonlinear Observable Estimation
```python
def estimate_nonlinear_observable(state_copies, observable_type, 
                                   num_projections=1000, num_measurements=100):
    """Estimate Tr(ρ^K) using random projections"""
    results = []
    for _ in range(num_projections):
        # Apply random projection
        projected_state = apply_random_projection(state_copies)
        # Measure locally
        outcome = local_measurement(projected_state)
        results.append(outcome)
    return classical_post_process(results, observable_type)
```

### Pattern 2: Rényi Entropy Estimation
```python
def estimate_renyi_entropy(state, order=2, num_projections=500):
    """Estimate Rényi entropy S_α(ρ) = -1/(α-1) log Tr(ρ^α)"""
    trace_power = estimate_nonlinear_observable(
        [state] * order, "power", num_projections
    )
    return -1/(order-1) * np.log(trace_power)
```

### Pattern 3: State Fidelity Estimation
```python
def estimate_fidelity(state1, state2, num_projections=500):
    """Estimate fidelity F(ρ₁, ρ₂) = Tr(√(√ρ₁ ρ₂ √ρ₁))²"""
    # Use purified states and overlap estimation
    overlap = estimate_nonlinear_observable(
        [state1, state2], "overlap", num_projections
    )
    return overlap
```

## Application Patterns

### Multi-Copy Algorithm Design
1. **Identify target property**: What nonlinear property needs estimation?
2. **Choose projection ensemble**: Random Clifford, local random unitaries, or structured projections
3. **Determine sample complexity**: Based on desired precision and confidence
4. **Design measurement protocol**: Local measurements compatible with available hardware
5. **Classical post-processing**: Efficient algorithms for combining outcomes

### Hardware-Efficient Implementation
- **Shallow circuits**: Random projections require fewer gates than global swap tests
- **Local operations**: Measurements are local, compatible with NISQ hardware
- **Parallel execution**: Multiple projections can be run in parallel

## Key Parameters

| Parameter | Description | Typical Value |
|-----------|-------------|---------------|
| num_projections | Number of random projections | 500-5000 |
| num_measurements | Measurements per projection | 50-200 |
| projection_type | Type of random projection | Clifford, local random |
| confidence_level | Statistical confidence | 0.95-0.99 |

## Pitfalls

1. **Sample complexity**: High-dimensional states require many projections
   - Mitigation: Use structured projections that exploit state structure
2. **Projection quality**: Poor random projections may lose information
   - Mitigation: Verify projection preserves target property via concentration bounds
3. **Hardware noise**: Real hardware noise corrupts projection measurements
   - Mitigation: Error mitigation techniques, noise-aware projection design
4. **Classical overhead**: Post-processing may be computationally intensive
   - Mitigation: Use efficient classical algorithms, approximate when possible

## Verification

- Compare with exact swap test results for small systems
- Verify concentration inequalities hold empirically
- Test on known states (maximally mixed, pure, Bell states)
- Check convergence as num_projections increases

## Related Concepts

- Swap test and its variants
- Classical shadows
- Randomized benchmarking
- Quantum state tomography
- Concentration of measure
- Johnson-Lindenstrauss lemma (classical analogue)
