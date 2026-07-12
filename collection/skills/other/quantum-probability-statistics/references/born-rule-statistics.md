# Born Rule in Statistics

## Overview

The Born rule is the fundamental rule of quantum mechanics that connects quantum amplitudes to observable probabilities. In statistical applications, it offers a new perspective on probability and uncertainty.

## Mathematical Definition

**Born Rule:**
```
P(state = |n⟩) = |⟨n|ψ⟩|² = |αₙ|²
```

where:
- |ψ⟩ = α₁|₁⟩ + α₂|₂⟩ + ... + αₙ|n⟩ is the quantum state
- αₙ are probability amplitudes (complex numbers)
- |αₙ|² gives the actual probability

## Statistical Interpretation

### Classical vs Quantum Probability

| Classical | Quantum |
|-----------|---------|
| Probability P(x) | Amplitude ψ(x) |
| P(x) ∈ [0, 1] | ψ(x) ∈ ℂ |
| ∑P(x) = 1 | ∑|ψ(x)|² = 1 |
| No interference | Interference effects |
| Bayes: P(H|D) = P(D|H)·P(H) | Quantum: preserves phase |

### Key Insight

The Born rule introduces **amplitude** as a precursor to probability:
- Amplitude = "potential" or "pre-probability"
- Squaring creates actual probability
- Amplitudes are complex → can interfere

## Applications in Statistics

### 1. Interference Effects

**Classical probability combination:**
```
P_total = P₁ + P₂  (linear combination)
```

**Quantum interference:**
```
P_total = |ψ₁ + ψ₂|² = P₁ + P₂ + 2·Re(ψ₁*·ψ₂)
```

The interference term `2·Re(ψ₁*·ψ₂)` can be:
- **Constructive**: Enhanced probability (positive interference)
- **Destructive**: Suppressed probability (negative interference)

### 2. Multi-modal Distributions

**Classical mixture model:**
```python
P(x) = w₁·P₁(x) + w₂·P₂(x)
```

**Quantum superposition:**
```python
ψ(x) = √w₁·ψ₁(x) + √w₂·ψ₂(x)
P(x) = |ψ(x)|² = w₁·P₁(x) + w₂·P₂(x) + 2·√w₁·√w₂·Re(ψ₁*·ψ₂)
```

Advantage: interference term captures interactions between modes.

### 3. Bayesian Inference

**Classical Bayes:**
```python
P(H|D) = P(D|H)·P(H) / P(D)
```

**Quantum Bayes:**
```python
|ψ_H⟩' = M_D·|ψ_H⟩ / √P(D)
```

where `M_D` is measurement operator that preserves phase.

Advantage:
- Phase information enables sequential interference
- Better captures context-dependent updates

### 4. Correlation Modeling

Quantum entanglement enables correlations beyond classical limits:

**Bell inequality (classical bound):**
```
|C(A,B) - C(A,B')| + |C(A',B) + C(A',B')| ≤ 2
```

**Quantum violations:**
```
Quantum correlations can reach 2√2 > 2
```

Application: modeling stronger correlations in data.

## Practical Guidelines

### When to Use Born Rule

Use quantum probability (Born rule) when:
1. **Multi-modal uncertainty** with interactions
2. **Strong correlations** exceeding classical bounds
3. **Sequential updates** with interference effects
4. **Context-dependent** probability adjustments

### When Classical is Better

Stick with classical probability when:
1. Simple, well-defined distributions
2. Independence assumptions hold
3. No interference effects needed
4. Computational simplicity preferred

## Example Applications

### Example 1: Quantum Bayesian Network

```python
class QuantumBayesianNetwork:
    """
    Bayesian network using quantum probability.
    
    Nodes: quantum states |ψ_node⟩
    Edges: quantum correlations (entanglement)
    Inference: quantum measurement operations
    """
    
    def update(self, evidence):
        # Quantum measurement on evidence node
        # Propagate through entangled connections
        # Born rule for final probabilities
        pass
    
    def infer(self, query_node):
        # Compute quantum state for query
        # Apply Born rule: P = |ψ|²
        # Return probability distribution
        pass
```

### Example 2: Quantum Monte Carlo Sampling

```python
def quantum_sampling(distribution, n_samples):
    """
    Generate samples using quantum probability.
    
    Uses quantum random walk for exploration.
    Quantum tunneling for escaping local minima.
    Born rule for sample probabilities.
    """
    # Initialize quantum state for distribution
    psi = initialize_quantum_state(distribution)
    
    # Quantum random walk
    for i in range(n_samples):
        psi = quantum_walk(psi)
        sample = measure(psi)  # Born rule
        yield sample
```

### Example 3: Quantum Anomaly Detection

```python
def quantum_anomaly_score(data, model):
    """
    Anomaly detection using Born rule.
    
    Compute quantum state distance.
    Born rule deviation as anomaly score.
    """
    # Model quantum state
    psi_model = model.quantum_state()
    
    # Data quantum state
    psi_data = data_quantum_state(data)
    
    # Distance in amplitude space
    distance = abs(psi_model - psi_data)
    
    # Born rule anomaly score
    anomaly = 1 - |⟨psi_model|psi_data⟩|²
    return anomaly
```

## Mathematical Details

### State Normalization

Quantum state must satisfy:
```
⟨ψ|ψ⟩ = ∑|αₙ|² = 1
```

This ensures Born rule yields valid probabilities.

### Unitary Evolution

Quantum state evolves unitarily:
```
|ψ(t)⟩ = U(t)|ψ(0)⟩
```

where U(t) is unitary operator: U†U = I

Key property: preserves norm (Born rule still valid).

### Measurement Postulate

Measurement of observable O with eigenstates {|n⟩}:
```
P(n) = |⟨n|ψ⟩|²
```

After measurement, state collapses to |n⟩.

### No-cloning Theorem

Cannot copy arbitrary quantum states:
```
No unitary U such that U|ψ⟩|0⟩ = |ψ⟩|ψ⟩
```

Statistical implication: limited replication of quantum distributions.

## References

1. **Born, M.** (1926). "Quantenmechanik der Stoßvorgänge"
   - Original formulation of Born rule

2. **Quantum probability for statisticians** (arxiv:2503.02658)
   - Statistical applications of Born rule

3. **Khrennikov, A.** (2010). "Quantum-like brain"
   - Born rule in cognitive modeling

## Notes

- Born rule is experimentally verified in physics
- Statistical applications are theoretical/simulation-based
- No quantum hardware needed for mathematical framework
- Key: amplitude-phase structure enables interference