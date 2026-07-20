---
name: limited-memory-stabilizer-testing
category: ai_collection
description: Sample complexity analysis for stabilizer state testing and learning under k-qubit coherent memory constraints. Establishes fundamental memory-information tradeoffs in quantum information processing.
trigger_words: stabilizer testing, quantum memory, sample complexity, hidden shift, coherent memory, stabilizer learning, purity testing, memory constraints
arxiv_id: "2607.02444"
source_paper: "Optimal Stabilizer Testing and Learning with Limited Quantum Memory"
---

# Limited Memory Stabilizer Testing Framework

## Core Results

When an algorithm receives copies of an unknown n-qubit state but may keep only **k qubits of coherent quantum memory** between measurements:

### Testing Complexity
- Sample complexity of testing stabilizer states: **Θ(n - k)**
- With full memory: constant (6 copies) — dimension independent
- With k=0 memory: Θ(n) — as hard as learning

### Learning Complexity  
- Sample complexity of learning (non-adaptive): **Θ(n²/k)**
- With full memory: Θ(n)
- With k=0 memory: impossible (unbounded)

### Fundamental Separation Loss
- **Key insight**: The famous testing-vs-learning separation (constant vs linear) is LOST under memory constraints
- Even with k=0.99n qubits memory, NO constant-copy stabilizer tester exists
- For k=cn qubits (0 < c < 1), testing is AS HARD as learning: both require Θ(n) copies

### Purity Testing
- **Exponential lower bound** for purity testing even when memory may be left coherent throughout protocol

## Theoretical Techniques

1. **Hidden Shift Connection**: Upper bounds via novel connection to the hidden shift problem
2. **Combinatorial Lower Bounds**: Average case bounds on likelihood ratios via combinatorics of stochastic orthogonal group
3. **Memory as Enabling Resource**: Coherent quantum memory is THE resource enabling separation between testing and learning

## Memory Regimes

### Regime 1: Full Memory (k = n)
- Testing: O(1) copies — Gross-Nezami-Walter result
- Learning: Θ(n) copies
- Separation: YES (constant vs linear)

### Regime 2: Sublinear Memory (k = cn, 0 < c < 1)
- Testing: Θ(n) copies
- Learning: Θ(n) copies  
- Separation: LOST (same complexity)

### Regime 3: Near-Full Memory (k = 0.99n)
- Testing: Θ(n) copies
- No constant-copy tester exists
- Separation: LOST (despite 99% memory)

### Regime 4: Zero Memory (k = 0)
- Testing: Θ(n) copies — non-adaptive measurement only
- Learning: impossible without memory

## Applications

1. **Quantum resource theory**: Coherent memory as a quantifiable resource
2. **Quantum benchmarking**: Memory-constrained state verification protocols
3. **Quantum cryptography**: Security analysis under memory-bounded adversaries
4. **NISQ algorithms**: Designing memory-efficient quantum verification routines

## Verification Steps

1. Identify memory constraint k relative to system size n
2. Determine if testing-learning separation is preserved (only when k=n)
3. For k < n: expect Θ(n-k) testing samples, Θ(n²/k) learning samples
4. For purity testing: expect exponential sample requirements

## Pitfalls

- **Do not assume testing is easier than learning** under memory constraints — they become equally hard
- Even 99% memory (k=0.99n) is NOT sufficient for constant-copy testing
- Non-adaptive learning with zero memory is fundamentally impossible
- The hidden shift connection is key to upper bound proofs — don't overlook it
- Stochastic orthogonal group combinatorics are essential for lower bounds
