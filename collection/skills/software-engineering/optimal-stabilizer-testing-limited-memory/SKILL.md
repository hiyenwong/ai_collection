---
name: optimal-stabilizer-testing-limited-memory
description: Stabilizer state testing and learning under limited quantum memory constraints - sample complexity bounds for testing and learning with k-qubit memory.
category: ai_collection
trigger_words: stabilizer testing, limited quantum memory, stabilizer learning, quantum state testing, sample complexity quantum
arxiv_id: 2607.02444
---

# Optimal Stabilizer Testing and Learning with Limited Quantum Memory

## Background

Stabilizer states are fundamental in quantum computing (error correction, teleportation, measurement-based QC). Testing whether an unknown state is a stabilizer state, and learning which one, are fundamental computational problems.

**arXiv**: 2607.02444 (July 2026)
**Categories**: quant-ph, cs.CC, cs.DS, cs.IT, cs.LG

## Core Concept

The paper studies stabilizer state testing and learning under **limited coherent quantum memory** constraints:

- Algorithm receives copies of unknown n-qubit state sequentially
- Can only keep **k qubits** of coherent quantum memory between measurements
- This models realistic NISQ-era constraints where full quantum memory is expensive

## Key Results

### Sample Complexity Bounds

- **Testing** with k-qubit memory: **Θ(n - k)** copies required
- **Learning** with k-qubit memory: **Θ(n²/k)** copies required

### Critical Finding

The **testing-vs-learning separation** that exists with full memory is **lost under memory constraints**. With unlimited memory, testing is much easier than learning, but with limited memory both scale similarly.

## Algorithm Design

1. **Memory-constrained processing**: Process copies sequentially, keeping only k qubits
2. **Adaptive measurement strategy**: Choose measurements based on limited stored state
3. **Trade-off analysis**: More memory (larger k) reduces sample complexity linearly

## Implications

- Quantum memory is a critical resource for stabilizer protocols
- NISQ devices with limited memory face fundamentally harder learning tasks
- Testing-learning gap collapses under realistic memory constraints

## Pitfalls

- **Memory Assumption**: Bounds assume k < n; when k >= n the full-memory bounds apply
- **Coherent vs Classical Memory**: Only coherent quantum memory helps; classical memory between measurements doesn't improve bounds
- **Adaptive vs Non-adaptive**: Results may differ for non-adaptive measurement strategies

## Applications

- Quantum error correction verification
- Quantum state certification
- NISQ-era quantum protocol design
- Quantum machine learning with limited resources