---
name: limited-memory-quantum-testing
description: Stabilizer state testing and learning under quantum memory constraints. Proves testing complexity is Θ(n-k) with k-qubit memory, learning is Θ(n²/k), and exponential lower bound for purity testing. Identifies coherent quantum memory as the resource enabling testing-vs-learning separation.
category: quantum
trigger_words: stabilizer testing, quantum memory constraint, hidden shift problem, stochastic orthogonal group, purity testing, quantum state learning, memory-bounded quantum algorithms, likelihood ratio bounds
arxiv_id: 2607.02444
created: 2026-07-05
---

# Optimal Stabilizer Testing and Learning with Limited Quantum Memory

## Core Methodology

### 1. Problem Setting
- Algorithm receives copies of unknown n-qubit state sequentially
- May keep only **k qubits** of coherent quantum memory between measurements
- Classical setting (Gross, Nezami, Walter): testing uses 6 copies (dimension-independent), learning uses Θ(n)

### 2. Main Results

**Testing Complexity:** Θ(n-k)
- Upper bound via novel connection to **hidden shift problem**
- Lower bound via average-case bounds on likelihood ratios using **combinatorics of stochastic orthogonal group**

**Learning Complexity:** Θ(n²/k) (non-adaptive framework)

### 3. Key Insight
- Coherent quantum memory is the **resource** enabling separation between testing and learning
- Even with k=0.99n qubits memory, no constant-copy stabilizer tester exists
- For k=cn (0<c<1), testing is as hard as learning: both require Θ(n) copies

### 4. Purity Testing
- Proves **exponential lower bound** for purity testing
- Holds even when memory may be left coherent throughout protocol

## Implementation Steps

1. Formulate stabilizer testing problem with k-qubit memory constraint
2. Map to hidden shift problem for upper bound construction
3. Use stochastic orthogonal group combinatorics for lower bound
4. Analyze purity testing as application of techniques

## Applications

- Quantum state verification protocols
- Memory-constrained quantum algorithm design
- Quantum property testing complexity theory
- Quantum learning theory foundations

## Pitfalls

- The separation between testing (6 copies) and learning (Θ(n)) is **lost** under memory constraints
- k must be o(n) for meaningful results — near-full memory trivializes
- Non-adaptive learning framework — adaptive case may differ
- Purity testing lower bound is exponential — fundamental hardness
