---
name: non-gaussian-entanglement-hierarchy
description: "Non-Gaussian entanglement hierarchy based on Schmidt number methodology. Establishes bounds for continuous-variable quantum systems and characterizes entanglement beyond Gaussian operations. Activation: non-Gaussian entanglement, Schmidt number hierarchy, continuous-variable entanglement, quantum entanglement bounds, CV quantum systems."
---

# Non-Gaussian Entanglement Hierarchy Based on Schmidt Number

Establishes a rigorous hierarchy for classifying and bounding entanglement in continuous-variable (CV) quantum systems using the Schmidt number as the fundamental measure.

## Core Concept

Gaussian operations alone cannot distill entanglement in CV systems. This methodology introduces a non-Gaussian entanglement hierarchy that classifies states by their Schmidt number, providing computable bounds and operational criteria for entanglement detection beyond Gaussian regimes.

## Mathematical Framework

### Schmidt Number Hierarchy

The Schmidt number SN(ρ) classifies quantum states:
- SN(ρ) = 1: Separable states
- SN(ρ) = k: States requiring at least k-dimensional entanglement
- SN(ρ) → ∞: Infinite-dimensional entanglement (CV limit)

### Key Bounds

For a CV state ρ with non-Gaussian operations:
1. **Lower Bound**: SN(ρ) ≥ f(tr(Wρ)) where W is an entanglement witness
2. **Upper Bound**: SN(ρ) ≤ g(N(ρ)) where N is a non-Gaussianity measure
3. **Operational Bound**: Key rate R ≤ log₂(SN(ρ)) for quantum communication

## Implementation Steps

1. **State Preparation**: Generate or prepare the CV quantum state
2. **Non-Gaussianity Measurement**: Compute non-Gaussianity via:
   - Wigner function negativity
   - Quantum relative entropy to Gaussian reference
   - Higher-order cumulants
3. **Schmidt Number Estimation**: Use semidefinite programming (SDP)
4. **Hierarchy Classification**: Assign state to appropriate level
5. **Bound Computation**: Calculate operational bounds for the application

## Use Cases

- **Quantum Communication**: Bound on distillable key rate
- **Quantum Sensing**: Entanglement-enhanced precision limits
- **Quantum Computing**: Resource requirements for CV quantum algorithms
- **Quantum Metrology**: Non-Gaussian entanglement as a metrological resource

## Detection Criteria

### Witness-Based Detection

```python
def schmidt_witness(rho, k):
    """Test if Schmidt number exceeds k."""
    # Construct optimal witness W_k
    W_k = optimal_schmidt_witness(k)
    # If tr(W_k @ rho) < 0, then SN(rho) > k
    return np.trace(W_k @ rho) < 0
```

### Entropic Bounds

- Use Rényi entropies for experimental feasibility
- Logarithmic negativity as computable entanglement monotone
- Conditional entropy bounds for operational interpretations

## Practical Considerations

- Non-Gaussianity is resource-intensive (photon subtraction, cubic phase gates)
- Schmidt number estimation scales poorly with dimension
- Experimental verification requires full state tomography or clever witness design
- For large CV systems, use approximate bounds with limited measurements

## Relationship to Other Methods

- Extends Gaussian entanglement theory (PPT criterion, logarithmic negativity)
- Connects to discrete-variable entanglement theory via Schmidt decomposition
- Bridges with quantum resource theories (non-Gaussianity as a resource)