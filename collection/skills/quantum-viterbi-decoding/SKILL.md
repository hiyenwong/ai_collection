---
name: quantum-viterbi-decoding
description: "Quantum Viterbi decoding methodology for hidden quantum Markov models (HQMMs). Extends classical Viterbi algorithm to quantum sequential decision-making with proven advantage over classical diagonal strategies."
version: 1.0.0
author: Hermes Agent (Cron Job)
license: MIT
source: arXiv:2605.18912
metadata:
  hermes:
    tags: [Quantum, Viterbi, Hidden-Markov-Model, Sequential-Decision, NISQ]
    related_skills: [quantum-neural-dynamics, hidden-markov-models, quantum-algorithms]
---

# Quantum Viterbi Decoding for HQMMs

## Overview

Extends the classical Viterbi algorithm to hidden quantum Markov models (HQMMs), enabling quantum sequential decision-making that provably outperforms any classical diagonal (commuting) strategy.

**Paper**: "Quantum Viterbi Algorithm" — Accardi, Souissi, Soueidi, Mukhamedov, Rhaima (arXiv:2605.18912, May 2026)

## Core Methodology

### 1. Hidden Quantum Markov Models (HQMMs)
- Classical HMMs: discrete hidden states, probabilistic transitions
- HQMMs: hidden states are pure quantum effects on a continuous manifold
- Observed statistics may be identical, but hidden trajectories differ fundamentally

### 2. Quantum Viterbi Score
- Classical: max over finite discrete state space
- Quantum: optimization over continuous manifold of pure quantum effects
- Exploits coherent superpositions in hidden memory

### 3. Strict Quantum Advantage
- Theorem: coherent hidden trajectories achieve strictly higher decoding scores than any classical strategy constrained to diagonal (commuting) effects
- Holds even when both models share the same observed statistics
- Advantage stems from non-commutativity of quantum effects

### 4. Algorithm Steps
```
Input: sequence of measurement outcomes O = (o_1, ..., o_T)
       quantum transition operators {E_o}
       initial quantum state |ψ_0⟩

For t = 1 to T:
  For each quantum effect φ:
    δ_t(φ) = max_{φ'} [δ_{t-1}(φ') · ⟨φ|E_{o_t}|φ'⟩²]
    ψ_t(φ) = argmax_{φ'} [·]

Backtrack: find trajectory maximizing joint decoding functional
```

## Applications
- **Quantum memories**: optimal readout of stored quantum information
- **Quantum communication with memory**: decoding channels with temporal correlations
- **NISQ quantum ML**: sequential classification, time-series analysis
- **Quantum error correction**: syndrome-based trajectory decoding

## Implementation Patterns

### Pattern 1: Parameterized Quantum Viterbi
```python
# Use parameterized quantum circuits (PQCs) to approximate
# the continuous effect manifold optimization
# Ansatz: U(θ)|0⟩ → measurement → update δ
```

### Pattern 2: Hybrid Classical-Quantum
```
Classical: maintain δ table, backtracking
Quantum: evaluate ⟨φ|E_o|φ'⟩² via circuit execution
Loop: iterate over discretized effect manifold
```

### Pattern 3: NISQ-Friendly Approximation
- Discretize continuous manifold into finite grid
- Use SWAP test for fidelity estimation
- Apply amplitude amplification for max-finding

## Key Insights
1. **Non-commutativity as resource**: the quantum advantage comes from effects not sharing eigenbasis
2. **Continuous vs discrete**: quantum Viterbi optimizes over continuous manifold, not discrete set
3. **Same observations, different inference**: identical observed statistics but different hidden trajectory inference
4. **Scalability bottleneck**: continuous optimization is harder than discrete; requires PQC approximation

## When to Use
- Sequential decision-making under quantum uncertainty
- Quantum systems with memory/temporal correlations
- NISQ-era quantum machine learning tasks
- Any scenario where classical Viterbi is applied to quantum data

## Pitfalls
- Continuous manifold optimization is exponentially harder than discrete
- Requires careful discretization for NISQ implementation
- Advantage only manifests when quantum effects are genuinely non-commuting
- Classical baselines with commuting effects may appear competitive on small instances

**Activation**: quantum viterbi, hidden quantum markov model, HQMM, sequential quantum decoding, quantum advantage decoding, quantum state estimation