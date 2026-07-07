---
name: closed-loop-quantum-probability
description: Closed-loop decomposition of quantum probabilities from unitarity — Bargmann invariants as phase-invariant loop quantities, Born rule as quadratic structure from forward/reverse amplitude products. Connects quantum probability to number theory (loop invariants, cyclic groups) and statistics (phase-invariant estimation). Trigger words: closed-loop quantum probability, Bargmann invariant, unitarity, Born rule derivation, quantum interference, phase-invariant, cyclic loop.
license: arXiv: 2606.02504
source: https://arxiv.org/abs/2606.02504
---

# Closed-Loop Quantum Probability Decomposition

## Overview

Reformulates quantum probability decomposition as a direct consequence of unitarity, where closed loops are fundamental quantum entities and interference arises from distinct loop classes weighted by Bargmann phases.

## Core Methodology

### Closed-Loop Framework
- Quantum probabilities decompose into sums over closed loops in state space
- Each loop class contributes weighted by its Bargmann phase
- Bargmann invariants emerge naturally as phase-invariant quantities (not independently postulated)

### Born Rule from Unitarity
- Born rule reflects quadratic structure from forward × reverse amplitude product
- This product defines the fundamental closed loop
- Cross-terms in interference reinterpreted as contributions from distinct loop classes

### Mathematical Structure
- Loop decomposition: P = Σ_L c_L · B_L where B_L = Tr(ρ₁ρ₂...ρₙ) is the Bargmann invariant
- Phase invariance: B_L is invariant under global phase transformations
- Connection to cyclic group structure: n-loop invariants form representation of Z_n

## Applications

1. **Statistical estimation**: Phase-invariant quantities enable robust estimation from noisy measurements
2. **Number theory connection**: Loop invariants map to characters of finite cyclic groups
3. **Quantum algorithms**: Loop-based decomposition provides alternative framework for quantum probability computation
4. **Interpretability**: Demystifies interference as loop-class contributions rather than mysterious cross-terms

## Implementation

1. **Identify loop structure**: Decompose probability amplitude into forward/reverse path pairs
2. **Compute Bargmann invariants**: B_L = ⟨ψ₁|ψ₂⟩⟨ψ₂|ψ₃⟩...⟨ψₙ|ψ₁⟩
3. **Weight by phase**: Each loop class weighted by exp(i·Arg(B_L))
4. **Sum contributions**: P = Σ_L |B_L| · exp(i·Arg(B_L))

## Key Insight

Unitarity ⟹ closed-loop decomposition ⟹ Bargmann invariants ⟹ Born rule. The chain is deductive, not axiomatic.

## Activation

closed-loop quantum probability, Bargmann invariant, unitarity, Born rule derivation, quantum interference, phase-invariant, cyclic loop, quantum foundations
