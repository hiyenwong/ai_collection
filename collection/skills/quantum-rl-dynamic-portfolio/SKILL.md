---
name: quantum-rl-dynamic-portfolio
category: quantum-finance
description: Quantum Reinforcement Learning (QRL) methodology for dynamic portfolio optimization using Variational Quantum Circuits (VQC). Implements quantum analogues of DDPG and DQN for sequential portfolio decisions with fewer parameters than classical deep RL.
tags:
  - quantum-reinforcement-learning
  - portfolio-optimization
  - variational-quantum-circuits
  - dynamic-trading
  - qrl
  - ddpg
  - dqn
---

# Quantum RL for Dynamic Portfolio Optimization

Quantum Reinforcement Learning (QRL) methodology for dynamic portfolio optimization using Variational Quantum Circuits (VQC). Based on arXiv:2601.18811.

## Description

This skill implements quantum analogues of Deep Deterministic Policy Gradient (DDPG) and Deep Q-Network (DQN) algorithms for dynamic portfolio optimization. The QRL agents use parameterized quantum circuits as function approximators, achieving competitive performance with classical deep RL baselines while using significantly fewer trainable parameters.

## Activation Keywords

- quantum reinforcement learning portfolio
- QRL dynamic portfolio
- variational quantum circuit trading
- quantum DDPG DQN
- quantum policy gradient
- quantum value function approximation

## Core Methodology

### 1. Quantum Policy Network Architecture

```
State → Classical Feature Encoding → Quantum Circuit → Measurement → Action
```

- **Input**: Portfolio state (asset prices, holdings, market indicators)
- **Quantum Layer**: Parameterized quantum circuit (PQC) with entangling gates
- **Output**: Action probabilities (buy/sell/hold) or continuous weights

### 2. QRL-DDPG (Continuous Action Space)

```python
# Actor Network: VQC-based policy
def quantum_actor(state, params):
    # Encode state into quantum state
    encoded = state_encoding(state)
    # Apply parameterized quantum circuit
    quantum_state = apply_pqc(encoded, params)
    # Measure to get action
    action = measure_expectation(quantum_state)
    return action

# Critic Network: Classical or hybrid
def hybrid_critic(state, action, params):
    # Combine state and action
    combined = concatenate(state, action)
    # Quantum-enhanced value estimation
    value = quantum_value_estimation(combined, params)
    return value
```

### 3. QRL-DQN (Discrete Action Space)

```python
# Q-Network with VQC
def quantum_q_network(state, params):
    # Encode market state
    encoded = amplitude_encoding(state)
    # Apply variational circuit
    qc_state = variational_circuit(encoded, params)
    # Measure Q-values for each action
    q_values = measure_all_actions(qc_state)
    return q_values
```

## Key Advantages

1. **Parameter Efficiency**: VQC-based agents use 10-100x fewer parameters than classical deep networks
2. **Quantum Advantage**: Potential for better exploration through quantum superposition
3. **Hardware Compatibility**: Shallow circuits suitable for NISQ devices
4. **Expressivity**: Quantum circuits can represent complex value functions with fewer parameters

## Implementation Guidelines

### State Encoding
- **Amplitude Encoding**: Map portfolio state vector to quantum amplitudes
- **Angle Encoding**: Use market features as rotation angles
- **Basis Encoding**: Binary representation of trading signals

### Circuit Design
- **Depth**: Keep circuits shallow (2-4 layers) for NISQ compatibility
- **Entanglement**: Use CZ or CNOT gates for feature interaction
- **Parameterization**: Ry, Rz rotations with trainable angles

### Training Protocol
1. Initialize quantum circuit parameters randomly
2. Collect experience using epsilon-greedy policy
3. Update parameters using quantum gradient estimation
4. Apply target network soft updates (DDPG) or Q-learning updates (DQN)

## Portfolio Environment

```python
class PortfolioEnv:
    def __init__(self, assets, initial_capital):
        self.assets = assets
        self.capital = initial_capital
        self.holdings = {asset: 0 for asset in assets}
    
    def step(self, action):
        # Execute trade
        # Calculate reward (Sharpe ratio, returns, etc.)
        # Update state
        return next_state, reward, done, info
```

## Performance Benchmarks

- **QRL-DDPG**: Achieves comparable Sharpe ratio to classical DDPG with 50x fewer parameters
- **QRL-DQN**: Matches DQN performance on discrete trading actions with reduced circuit depth
- **Training Stability**: Quantum gradient noise requires careful learning rate scheduling

## Pitfalls

1. **Gradient Estimation**: Quantum gradients require multiple circuit executions (parameter shift rule)
2. **Barren Plateaus**: Deep quantum circuits suffer from vanishing gradients
3. **State Preparation**: Amplitude encoding is exponentially expensive for large state spaces
4. **Measurement Noise**: NISQ device noise affects policy evaluation

## Related Patterns

- **quantum-finance-portfolio**: QAOA-based portfolio optimization
- **quantum-portfolio-optimizer**: Static portfolio selection via QAOA
- **quantum-ml-patterns**: General quantum ML patterns

## References

- arXiv:2601.18811 - "Quantum Reinforcement Learning for Dynamic Portfolio Optimization"
- Gurgul, Chen, Lessmann (2026) - VQC-based QRL for portfolio management
- arXiv:2603.16904 - Hybrid classical-quantum framework for portfolio construction
