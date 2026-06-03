---
name: qmarl-entanglement-coordination
description: "Quantum Multi-Agent Reinforcement Learning (QMARL) with entanglement-based coordination. Demonstrates provable quantum advantage via CHSH game (Tsirelson limit 0.854 vs classical ceiling 0.75). Hybrid quantum actor + classical critic outperforms both fully classical and fully quantum."
---

# QMARL Entanglement Coordination

## Description

Quantum Multi-Agent Reinforcement Learning (QMARL) methodology using shared entangled states for provable agent coordination advantage. Demonstrates that entanglement — not quantum circuits alone — is the active coordination mechanism in multi-agent systems.

Based on: "Quantum Advantage in Multi Agent Reinforcement Learning" (arXiv: 2605.14235) by Dahia & Szabo, May 2026.

## Activation Keywords

- quantum multi-agent RL
- QMARL entanglement
- quantum advantage MARL
- Tsirelson limit coordination
- CHSH game RL
- entangled agent coordination
- hybrid quantum critic
- quantum actor classical critic
- 量子多智能体强化学习
- 量子纠缠协调

## Core Findings

### 1. Provable Quantum Advantage via CHSH Game
- Classical ceiling: 0.75 win rate (mathematically proven)
- Entangled QMARL agents approach Tsirelson limit: 0.854
- Unentangled quantum circuits match classical baseline (0.75)
- **Key insight**: Entanglement, not quantum circuits, is the active coordination mechanism

### 2. Bell State Structure Matters
- Not all entangled states improve coordination equally
- Some Bell states enable coordination gains
- Others actively harm performance
- Entanglement structure selection is critical

### 3. Hybrid Architecture Wins
- QMARL without entanglement: ~2x improvement over classical MAA2C (~0.85 vs ~0.40)
- **Best**: Quantum actor + classical centralized critic
- Outperforms both fully classical and fully quantum solutions

## Implementation Patterns

### Pattern 1: Decentralized QMARL with Shared Entanglement

```python
# VQC actors with shared entangled states
# Each agent has a variational quantum circuit actor
# Entanglement is injected via shared Bell states

import pennylane as qml
import numpy as np

def create_entangled_actor(n_qubits, entanglement_type='bell'):
    """Create a VQC actor with shared entanglement."""
    dev = qml.device('default.qubit', wires=n_qubits)
    
    @qml.qnode(dev)
    def circuit(params, input_state):
        # Encode input
        for i in range(n_qubits):
            qml.RY(input_state[i], wires=i)
        
        # Apply entanglement layer (shared across agents)
        if entanglement_type == 'bell':
            qml.CNOT(wires=[0, 1])
            qml.Hadamard(wires=0)
        
        # Variational layers
        for layer in range(len(params)):
            for i in range(n_qubits):
                qml.Rot(*params[layer][i], wires=i)
            # Entangling gates within agent
            for i in range(n_qubits - 1):
                qml.CNOT(wires=[i, i+1])
        
        return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]
    
    return circuit
```

### Pattern 2: Hybrid Quantum Actor + Classical Critic

```python
class HybridQMARLAgent:
    """Hybrid QMARL: quantum actor + classical centralized critic."""
    
    def __init__(self, n_qubits, n_actions, critic_hidden=[64, 64]):
        # Quantum actor (variational circuit)
        self.actor_circuit = create_entangled_actor(n_qubits)
        self.actor_params = np.random.randn(3, n_qubits, 2)
        
        # Classical centralized critic
        self.critic = nn.Sequential(
            nn.Linear(n_agents * n_actions + state_dim, critic_hidden[0]),
            nn.ReLU(),
            nn.Linear(critic_hidden[0], critic_hidden[1]),
            nn.ReLU(),
            nn.Linear(critic_hidden[1], 1)
        )
    
    def select_action(self, observation, agent_id):
        # Run quantum circuit to get action probabilities
        q_output = self.actor_circuit(self.actor_params, observation)
        # Convert quantum expectation values to action probs
        action_probs = softmax(np.array(q_output))
        return np.random.choice(len(action_probs), p=action_probs)
    
    def update(self, observations, actions, rewards, next_observations):
        # Classical critic computes TD error
        td_error = self.compute_td_error(observations, actions, rewards, next_observations)
        # Update quantum actor parameters via gradient
        self.update_actor_params(td_error)
        # Update classical critic
        self.update_critic(td_error)
```

## Key Research Insights

| Configuration | Performance | Notes |
|--------------|-------------|-------|
| Classical MAA2C | ~0.40 (CoopNav) | Baseline |
| Unentangled QMARL | ~0.85 (CoopNav) | 2x improvement, no quantum advantage |
| Entangled QMARL | ~0.854 (CHSH) | Approaches Tsirelson limit |
| **Hybrid (Q actor + C critic)** | **Best overall** | Outperforms all others |

## Pitfalls

1. **Unentangled QMARL is NOT quantum advantage**: If your quantum circuits don't share entanglement, you're just using a different parameterization — performance gains may come from expressivity, not quantum effects
2. **Bell state selection matters**: Not all entangled states improve coordination; test multiple Bell state configurations
3. **CHSH game is the gold standard**: Use CHSH game (classical ceiling 0.75) to prove quantum advantage; other environments may not have provable classical bounds
4. **Hybrid > Pure quantum**: The best results come from quantum actors paired with classical centralized critics, not fully quantum systems

## Applications

- Multi-agent coordination tasks with communication constraints
- Distributed control systems requiring provable coordination guarantees
- Game-theoretic scenarios where classical coordination has known bounds
- Quantum-enhanced swarm intelligence

## Related Skills

- `quantum-ai-patterns` - General quantum AI research patterns
- `quantum-ml-patterns` - QML research methodology
- `rl-qec-control` - RL for quantum error correction

## Resources

- Paper: https://arxiv.org/abs/2605.14235
- CHSH Game: Classic Bell inequality test with proven classical bound
- Tsirelson Bound: Maximum quantum violation of CHSH inequality (≈0.854)
