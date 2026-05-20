---
name: shallow-qft-alternative-hp-circuits
description: "O(n) alternative to Quantum Fourier Transform using Hadamard-controlled Phase (HP-L) circuits. Replaces O(n²) QFT depth in Shor's algorithm with neural network classical post-processing."
category: quantum-algorithms
---

# O(n) Alternative to Quantum Fourier Transform

**arXiv**: 2605.16998 (quant-ph, cs.LG)
**Authors**: Kaiming Bian, Zujin Wen, Oscar Dahlsten

## Core Methodology

Constructs a family of **shallow quantum circuits** (HP-L) using only Hadamards and controlled-Phase gates that can replace the O(n²) depth QFT in hidden subgroup problem algorithms like Shor's.

### Two Key Properties of QFT Exploited

1. **Shift invariance**: Allows removal of random overall shift in the phase
2. **Fisher information retention**: QFT retains information about hidden subgroup generator accessible in measurement outcomes

### HP-L Circuit Construction

- **HP-1 circuit**: O(n) depth, uses only Hadamards + controlled-Phase gates
- Preserves shift invariance (proven)
- Retains exponentially growing Fisher information (numerical analysis)
- Can replace QFT in Shor's algorithm numerically demonstrated

### Classical Post-Processing

Uses an **efficient neural network** to process measurement outcomes, compensating for the simpler quantum circuit structure.

## Implementation Patterns

- Replace QFT with HP-L circuits for depth reduction: O(n²) → O(n)
- Use Hadamard + controlled-Phase gate set only
- Preserve shift invariance in circuit design
- Quantify retained information via discrete Fisher information
- Neural network classical post-processing for measurement interpretation

## Advantages over QFT

- **Linear depth**: O(n) vs O(n²) — critical for near-term hardware
- **Simpler gate set**: Only Hadamard + controlled-Phase
- **Proven shift invariance**: Mathematical guarantee
- **Neural post-processing**: Compensates for simpler quantum structure

## Applications

- Shor's algorithm on near-term quantum hardware
- Hidden subgroup problem algorithms
- Quantum phase estimation with reduced circuit depth
- NISQ-era quantum algorithms requiring Fourier transforms

## Activation

shallow QFT, HP circuits, quantum Fourier transform alternative, linear depth quantum circuits, Shor's algorithm optimization, Fisher information quantum, hidden subgroup problem
