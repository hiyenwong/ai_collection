---
name: quantum-viterbi-algorithm
description: "Quantum Viterbi decoding for hidden quantum Markov models (HQMMs). Strict quantum advantage over classical Viterbi via coherent superposition in hidden memory."
category: quantum-algorithms
---

# Quantum Viterbi Algorithm

**arXiv**: 2605.18912 (quant-ph, math-ph, math.PR)
**Authors**: Luigi Accardi, Abdessatar Souissi, El Gheteb Soueidi, Farrukh Mukhamedov, Mohamed Rhaima

## Core Methodology

Quantum analogue of the classical Viterbi algorithm for **hidden quantum Markov models (HQMMs)**. Given a sequence of measurement outcomes, identifies hidden quantum trajectories that maximize a joint decoding functional.

### Key Differences from Classical Viterbi

- **Classical**: Optimizes over finite discrete state space
- **Quantum**: Optimizes over continuous manifold of pure quantum effects
- Exploits **coherent superpositions** in the hidden memory

### Proven Quantum Advantage

Coherent hidden trajectories achieve decoding scores that **strictly exceed** any classical strategy constrained to diagonal (commuting) effects, even when both models share the same observed statistics.

### Mathematical Framework

- Optimization over continuous manifold of pure quantum effects
- Joint decoding functional maximization
- Proof of strict advantage via coherence exploitation

## Implementation Patterns

- Use quantum trajectories instead of discrete state paths
- Optimize over quantum effect manifolds (not just diagonal states)
- Exploit superposition in hidden memory for superior decoding scores

## Applications

- Quantum memories and quantum communication with memory
- Near-term quantum machine learning on NISQ devices
- Sequential decision-making with quantum state estimation
- Quantum error correction decoding

## Activation

quantum viterbi, hidden quantum markov, quantum decoding, sequential decision making, quantum communication with memory, HQMM, quantum trajectory decoding
