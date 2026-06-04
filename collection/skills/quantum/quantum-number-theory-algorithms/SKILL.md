---
name: quantum-number-theory-algorithms
description: Quantum algorithms for number theory problems. Use when exploring quantum approaches to: (1) primality testing, (2) factorization, (3) prime number theorem, (4) Goldbach conjecture, (5) quantum integer arithmetic, (6) Riemann zeta connections to quantum systems, or when implementing quantum probabilistic subroutines with Grover/Shor operators.
---

# Quantum Number Theory Algorithms

Quantum algorithms that solve classical number theory problems with polynomial time complexity.

## Core Algorithms

### Quantum Probabilistic Subroutines

**Pattern**: Grover search + Shor Fourier transform for counting

```python
# Quantum counting: estimate solutions count
def quantum_counting(grover_operator, shor_ft, precision):
    """
    Combines Grover's search with Fourier transform for counting.
    Fully unitary - can be embedded in larger quantum networks.
    """
    # 1. Initialize superposition
    # 2. Apply Grover iterations
    # 3. Extract periodicity via Fourier transform
    # 4. Estimate solution count
```

### Number Theory Problems

#### Primality Testing
- Quantum algorithm: O(poly(n)) time
- Uses quantum counting for prime detection
- Based on Rabin's probabilistic method

#### Prime Number Theorem
- Quantum estimation of π(N) (prime counting function)
- Polynomial time vs classical exponential

#### Goldbach Conjecture
- Quantum counting of representations N = p + p'
- Hardy-Littlewood asymptotic formula

### Quantum Integer Arithmetic

**Definition**: Quantum integer `[n]_q = 1 + q + ... + q^{n-1}`

**Operations**:
- Addition: `[m]_q ⊕_q [n]_q = [m+n]_q`
- Multiplication: `[m]_q ⊗_q [n]_q = [mn]_q`

**Ring structure**: Quantum integers form ring with quantum rational field.

## Activation Keywords

- quantum number theory
- quantum primality test
- quantum factorization
- quantum integer
- quantum counting
- quantum prime theorem
- quantum Goldbach
- quantum zeta function
- quantum probabilistic algorithm
- 量子数论
- 量子素性测试

## Tools Used

- `exec`: Run quantum simulation scripts (Qiskit, Cirq)
- `read`: Load algorithm implementations, reference papers
- `write`: Save quantum circuits, algorithm results
- `web_search`: Search arxiv for latest quantum number theory papers

## Implementation Patterns

### Pattern 1: Quantum Counting for Number Theory

```markdown
Steps:
1. Define oracle function f(x) for number property
2. Build Grover operator G = (2|ψ⟩⟨ψ| - I)O
3. Apply quantum Fourier transform
4. Extract periodicity → estimate solution count
```

### Pattern 2: Quantum Integer Computations

```markdown
Steps:
1. Encode number n as quantum integer polynomial
2. Apply addition/multiplication rules
3. Extract classical result from polynomial coefficients
```

### Pattern 3: Riemann Zeta in Quantum Systems

Connection: Quantum correlation functions → Riemann zeta values

Example: Heisenberg XXX antiferromagnet emptiness formation probability P(n)
- P(n) expressed via ζ(odd arguments), ln 2, rational coefficients

## Key References

**arxiv:9907020v2**: Quantum Probabilistic Subroutines and Problems in Number Theory (Carlini, Hosoya)
- Grover + Shor counting algorithm
- Primality testing in poly time
- Prime number theorem quantum version

**arxiv:0204006v1**: Additive Number Theory and Quantum Integers (Nathanson)
- Quantum integer ring construction
- Addition and multiplication rules

**arxiv:0202346v2**: Quantum Correlations and Number Theory (Boos et al.)
- Riemann zeta in quantum correlation functions
- Heisenberg XXX model connection

**arxiv:2410.13988v2**: Quantum Dynamics in Number-Theory Potentials (Cassettari et al.)
- Prime number spectrum traps
- Rabi oscillations in number-theory-inspired potentials

## Use Cases

1. **Fast primality testing**: Quantum polynomial vs classical exponential
2. **Prime counting**: Estimate π(N) efficiently
3. **Number theory experiments**: Design quantum systems testing conjectures
4. **Quantum integer arithmetic**: Novel computational framework
5. **Quantum-statistical mechanics**: Zeta function applications

## Instructions

When implementing quantum number theory algorithms:

1. **Check existing quantum simulators**: Qiskit, Cirq, PennyLane
2. **Define oracle carefully**: Oracle determines what you're counting
3. **Verify unitarity**: Ensure algorithm can be embedded in larger circuits
4. **Test on small numbers first**: N < 100 before scaling
5. **Compare with classical**: Quantum speedup should be significant

## Error Handling

- **Oracle design errors**: Verify oracle marks correct states
- **Counting precision**: Increase Fourier samples for better estimates
- **Decoherence**: Use error correction for large N
- **Complexity analysis**: Ensure polynomial time claim holds

## Resources

- **References**: See [references/papers.md](references/papers.md) for detailed paper analysis
- **Scripts**: [scripts/quantum_counter.py](scripts/quantum_counter.py) for quantum counting implementation
- **arxiv**: Search "quantum number theory" for latest research

## Related Skills

- `distributed-quantum-computing`: Distributed quantum algorithm execution
- `hybrid-quantum-classical-systems`: Hybrid quantum-classical algorithms
- `arxiv-search`: Paper discovery workflow