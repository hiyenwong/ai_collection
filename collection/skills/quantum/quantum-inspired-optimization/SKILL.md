---
name: quantum-inspired-optimization
description: >
  Quantum-inspired classical optimization algorithms derived from quantum computing
  concepts. Covers LogQ non-linear continuous relaxation, quantum-inspired evolutionary
  algorithms, and quantum-to-classical translation patterns. Use when exploring
  quantum-inspired methods, classical alternatives to quantum algorithms, or
  QUBO solvers without quantum hardware.
  Trigger: quantum-inspired, LogQ algorithm, quantum-inspired optimization,
  quantum classical translation, QUBO classical solver, quantum-inspired finance
---

# Quantum-Inspired Optimization

## Description

Methodology for designing and applying classical algorithms inspired by quantum
computing principles. Focuses on practical optimization methods that achieve
quantum-like benefits without requiring quantum hardware.

## Activation Keywords

- quantum-inspired optimization
- LogQ algorithm
- quantum classical translation
- QUBO classical solver
- quantum-inspired finance
- non-linear continuous relaxation
- 量子启发优化

## Core Algorithms

### 1. LogQ Algorithm (arXiv:2604.12925)

Non-linear continuous relaxation for QUBO problems:

```python
def logq_relaxation(Q, x0, max_iter=1000):
    """LogQ-inspired continuous relaxation for QUBO.

    Q: QUBO matrix (n x n)
    x0: Initial continuous point in [0,1]^n
    Returns: Binary solution
    """
    from scipy.optimize import minimize

    def objective(x):
        return x @ Q @ x

    # Continuous relaxation with box constraints
    bounds = [(0, 1)] * len(x0)
    result = minimize(objective, x0, bounds=bounds, method='L-BFGS-B')

    # Round to binary
    return (result.x > 0.5).astype(int)
```

**Advantages over quantum:**
- No Pauli decomposition needed
- No measurement overhead
- Gradient-inspired optimization
- Fewer computational resources

### 2. Quantum-Inspired Evolutionary Algorithms

Algorithms that use quantum concepts (superposition, interference) classically:

- Quantum-inspired particle swarm optimization
- Quantum-behaved differential evolution
- Quantum-inspired simulated annealing

### 3. Tensor Network Methods

Classical simulation of quantum systems using tensor networks:

- Matrix Product States (MPS) for optimization
- Tensor Train decomposition for high-dimensional problems
- DMRG-inspired optimization for QUBO

## Quantum-to-Classical Translation Pattern

When to translate quantum to classical:

1. **Resource constraint**: Limited qubits or circuit depth
2. **Noise sensitivity**: NISQ devices produce unreliable results
3. **Scalability need**: Classical method scales better for large problems
4. **Pragmatic choice**: Faster time-to-solution required

### Translation Steps

1. Identify quantum algorithm core mechanism
2. Map quantum operations to classical equivalents
3. Design continuous relaxation of discrete variables
4. Implement gradient-inspired optimization
5. Validate against quantum baseline

## QUBO Problem Formulation

Standard QUBO form: minimize x^T Q x, x in {0,1}^n

Common mappings:
- Portfolio selection: x_i = 1 if asset i selected
- Feature selection: x_i = 1 if feature i included
- Scheduling: x_{i,t} = 1 if task i at time t

## Performance Comparison

| Method | Scalability | Accuracy | Speed | Hardware |
|--------|-------------|----------|-------|----------|
| LogQ | High | Good | Fast | Classical |
| QAOA | Limited | Variable | Slow | Quantum |
| HQGA | Medium | Good | Medium | Hybrid |

## Resources

- See references/logq-implementation.md for detailed implementation
- See references/translation-patterns.md for quantum-to-classical mapping

## Related Skills

- quantum-portfolio-optimization: Portfolio-specific quantum methods
- quantum-ml-patterns: General quantum ML patterns
- quantum-optimization-qaoa: Pure QAOA methodology
