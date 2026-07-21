---
name: quantum-rl-dynamic-portfolio
description: "Quantum Reinforcement Learning (QRL) for dynamic portfolio optimization using Variational Quantum Circuits (VQC). Provides quantum analogues of Deep Deterministic Policy Gradient (DDPG) and Deep Q-Network (DQN) for sequential portfolio allocation. Achieves competitive performance vs classical deep RL with fewer trainable parameters. Use when: (1) implementing quantum RL for finance, (2) designing VQC-based trading agents, (3) comparing quantum vs classical RL for portfolio optimization, (4) building parameter-efficient quantum agents, (5) dynamic asset allocation with quantum circuits."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2601.18811"
  published: "2026-01-20"
  authors: "Vincent Gurgul, Ying Chen, Stefan Lessmann"
  tags: [quantum-finance, reinforcement-learning, portfolio-optimization, VQC, QDDPG, QDQN]
---

# Quantum RL for Dynamic Portfolio Optimization

## Core Concept

Quantum Reinforcement Learning (QRL) approach to dynamic portfolio optimization using Variational Quantum Circuits (VQC) as function approximators. Implements quantum analogues of DDPG (QDDPG) and DQN (QDQN) where the policy/value networks are replaced by parameterized quantum circuits.

## Key Methodology

### QDDPG — Quantum Deep Deterministic Policy Gradient

- **Actor network**: VQC outputs continuous portfolio weights
- **Critic network**: VQC evaluates state-action value Q(s,a)
- **State encoding**: Financial features encoded via angle/amplitude encoding into qubit states
- **Action**: Portfolio weight allocation (continuous, normalized via softmax or constrained layer)
- **Key advantage**: Fewer trainable parameters than classical neural nets of equivalent expressive power

### QDQN — Quantum Deep Q-Network

- **Discrete action space**: Discretized portfolio allocation decisions
- **VQC as Q-function approximator**: Outputs Q-values for each discrete action
- **Experience replay + target network**: Standard DQN stabilization techniques adapted for quantum circuits

### VQC Architecture Pattern

```
State Encoding → Parameterized Quantum Circuit → Measurement → Classical Post-processing
     ↓                        ↓                          ↓                    ↓
  Angle/Amplitude        Rotation gates +            Observable              Portfolio
  encoding of             entangling layers           expectation             weights
  market features         (RZ, RY, CNOT, CZ)          values
```

## Implementation Considerations

### Parameter Efficiency
- QRL agents achieve competitive Sharpe ratios with **fewer trainable parameters** than classical DDPG/DQN
- Quantum circuits exploit high-dimensional Hilbert space for compact representations
- Critical for NISQ-era deployment where circuit depth is constrained

### State Encoding Strategies
- **Angle encoding**: Map features to rotation angles — shallow circuits, O(n) gates
- **Amplitude encoding**: Logarithmic qubits O(log n) — deeper state preparation
- **Basis encoding**: Binary representation — requires more qubits

### Training Stability
- Parameter shift rule for gradient computation
- Natural gradient or Adam optimizer for VQC parameters
- Target network updates (soft: τθ' ← τθ + (1-τ)θ') to stabilize Q-learning
- Gradient clipping to handle quantum circuit gradient variance

### NISQ Constraints
- Circuit depth limited by coherence time
- Measurement shot noise requires multiple shots per expectation value
- Barren plateau risk — initialize parameters near identity or use layerwise training

## Applications

- Dynamic portfolio rebalancing under transaction costs
- Multi-asset allocation with risk constraints
- Quantum advantage research in sequential decision-making
- Parameter-efficient trading agent design

## Comparison Baselines

When evaluating QRL for portfolio optimization, compare against:
1. Classical DDPG / DQN with equivalent parameter counts
2. Mean-variance optimization (Markowitz)
3. Equal-weight and buy-and-hold baselines
4. Risk parity portfolios

## Activation Keywords

- quantum reinforcement learning
- QRL portfolio
- VQC trading agent
- quantum DDPG
- quantum DQN
- QDDPG
- QDQN
- variational quantum circuit finance
- quantum portfolio optimization
- parameter-efficient quantum agent
- dynamic asset allocation quantum
- quantum RL finance
