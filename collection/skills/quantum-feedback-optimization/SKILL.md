---
name: quantum-feedback-optimization
description: "Feedback-based quantum optimization methodology for combinatorial optimization problems. Covers FALQON (Feedback-based ALgorithm for Quantum OptimizatioN) and its classical counterparts, quantum-classical correspondence of spin systems, and higher-order unconstrained binary optimization. Use when: designing feedback-based quantum optimization algorithms, comparing quantum vs classical optimization, or solving combinatorial optimization with feedback control."
---

# Quantum Feedback-Based Optimization

Feedback-based quantum optimization uses measurement-driven feedback to solve combinatorial optimization. FALQON (Feedback-based ALgorithm for Quantum OptimizatioN) adaptively controls quantum evolution based on instantaneous energy measurements.

## FALQON Algorithm

### Core Mechanism

```
|ψ(t)⟩ evolves under H(t) = H_P + β(t)H_M
β(t) = λ · ⟨ψ(t)|[H_M, H_P]|ψ(t)⟩
```

Where:
- H_P = problem Hamiltonian (encodes cost function)
- H_M = mixer Hamiltonian
- β(t) = feedback parameter (adaptive)
- λ = feedback gain

### Key Properties

1. **Energy monotonicity**: ⟨H_P⟩ decreases monotonically
2. **No classical optimization loop**: Unlike QAOA, no outer optimizer needed
3. **Continuous-time**: Natural analog quantum evolution
4. **Adaptive**: Parameters adjust based on quantum state

## Quantum vs Classical Counterpart

### Classical Correspondence

Using quantum-classical correspondence of spin systems, a classical counterpart exists:
```
dx/dt = -∇E(x) + feedback_term
```

### Comparison Results

| Aspect | Quantum | Classical |
|--------|---------|-----------|
| Solution quality | Can be advantageous | Generally lower quality |
| Convergence speed | Slower | Generally faster |
| Scalability (HOUBO) | Limited by qubits | One classical algorithm shows significant scalability |

## Design Patterns

### Pattern 1: FALQON for QUBO

For Quadratic Unconstrained Binary Optimization:
```
H_P = Σ Qᵢⱼ σᶻᵢ σᶻⱼ + Σ hᵢ σᶻᵢ
H_M = Σ σˣᵢ
β(t) = λ · ⟨[H_M, H_P]⟩
```

### Pattern 2: Higher-Order UBO

For Higher-Order Unconstrained Binary Optimization:
- Reduce to QUBO via auxiliary variables
- Or use higher-order feedback terms
- Classical algorithm shows significant scalability for large instances

### Pattern 3: Hybrid Quantum-Classical

Combine quantum feedback with classical preprocessing:
1. Classical: Problem decomposition, warm start
2. Quantum: FALQON evolution for fine optimization
3. Classical: Post-processing, verification

## Implementation Guide

### Step 1: Define Problem Hamiltonian
Map cost function C(x) to H_P:
```
xᵢ ∈ {0,1} → σᶻᵢ eigenvalues
C(x) → H_P = Σ cᵢ σᶻᵢ + Σ cᵢⱼ σᶻᵢ σᶻⱼ + ...
```

### Step 2: Choose Mixer
Standard: H_M = Σ σˣᵢ
Problem-specific: Use domain knowledge

### Step 3: Set Feedback Gain
λ controls convergence speed:
- Too small: Slow convergence
- Too large: Oscillations, instability
- Adaptive: λ(t) based on energy landscape

### Step 4: Evolve and Monitor
```
while not converged:
    β = λ · ⟨[H_M, H_P]⟩
    |ψ⟩ ← exp(-i(H_P + βH_M)Δt) |ψ⟩
    E = ⟨ψ|H_P|ψ⟩
    if E improved: continue
    else: adjust λ
```

## Benchmarking

When comparing quantum vs classical:
- Test on small instances (both)
- Test classical on large instances
- Track: solution quality, convergence speed, scalability
- Key finding: quantum can find better solutions, classical converges faster

## Common Pitfalls

1. **Feedback gain selection**: Critical for stability
2. **Higher-order problems**: May require problem-specific adaptations
3. **Qubit limitations**: Classical algorithms scale better for large instances
4. **Noise sensitivity**: Feedback amplifies hardware noise

## References

- **FALQON**: Feedback-based Algorithm for Quantum Optimization
- **Quantum-Classical Correspondence**: Spin system analysis
- **arXiv: 2605.13082** - Feedback-based quantum optimization and classical counterpart

## Activation

- quantum feedback optimization
- FALQON algorithm
- feedback-based quantum optimization
- quantum combinatorial optimization
- quantum classical optimization comparison
- higher-order binary optimization quantum
