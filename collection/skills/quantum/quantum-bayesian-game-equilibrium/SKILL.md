---
name: quantum-bayesian-game-equilibrium
description: Parameterized quantum circuit methodology for computing correlated equilibrium in Bayesian games. Addresses exponential growth in joint type-action space with quantum advantage.
created: 2026-06-06
category: quantum-economics
source: arxiv:2606.03109
tags:
  - quantum game theory
  - Bayesian games
  - correlated equilibrium
  - parameterized quantum circuits
  - multi-agent economics
---

# Quantum Bayesian Game Equilibrium

## Overview

Computing correlated equilibrium in Bayesian games is challenging due to exponential growth in joint type-action space with number of players. Parameterized Quantum Circuits (PQCs) provide a compact representation that can encode correlations inaccessible to classical methods, enabling efficient equilibrium computation for multi-agent economic scenarios.

## Core Methodology

### 1. Quantum Game Representation
- Encode player types as quantum states
- Map action spaces to measurement bases
- Use entangled states to represent correlated strategies
- Leverage quantum superposition for type uncertainty

### 2. Parameterized Circuit Design
- Design ansatz circuit with player-specific subcircuits
- Include entangling layers between player qubits
- Parameterize rotation angles as strategy variables
- Use hardware-efficient ansatz for NISQ compatibility

### 3. Equilibrium Finding
- Define payoff expectation as quantum observable
- Optimize circuit parameters to maximize expected payoff
- Use gradient-based or gradient-free optimization
- Verify equilibrium conditions (no unilateral deviation improves payoff)

### 4. Correlation Encoding
- Use Bell states or GHZ states for shared randomness
- Encode correlated strategy recommendations in entanglement
- Measure in appropriate basis to extract actions
- Verify correlation structure matches game requirements

## Implementation Steps

1. **Formulate game**: Define players, types, actions, payoffs
2. **Design quantum circuit**: Create PQC with player subcircuits and entangling layers
3. **Encode types**: Map type distributions to initial quantum states
4. **Optimize parameters**: Find parameters that satisfy equilibrium conditions
5. **Extract strategies**: Measure circuit to obtain correlated strategy recommendations
6. **Verify equilibrium**: Check no player benefits from unilateral deviation

## Key Parameters

- Qubits per player: ceil(log2(|action space|))
- Entangling layers: 2-4 between player subcircuits
- Optimization method: SPSA, COBYLA, or gradient-based
- Shots per evaluation: 1000-10000
- Convergence tolerance: 1e-4 on payoff gradient

## Advantages

- Compact representation of correlated strategies
- Quantum entanglement enables novel correlations
- Polynomial qubit scaling vs exponential classical
- NISQ-compatible for small-to-medium games
- General framework for any Bayesian game

## Use Cases

- Auction mechanism design
- Market equilibrium computation
- Contract negotiation with incomplete information
- Multi-firm competition analysis
- Mechanism design with private information

## Pitfalls

- Barren plateaus in deep circuits
- Requires careful ansatz design
- Classical simulation limited to ~20 qubits
- Noise affects equilibrium precision
- Verification requires many circuit evaluations

## Verification

1. Test on known game solutions (Prisoner's Dilemma, Battle of Sexes)
2. Compare with classical correlated equilibrium algorithms
3. Verify no profitable unilateral deviations
4. Check convergence stability across random initializations
5. Validate on larger games with classical benchmarks