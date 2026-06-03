---
name: rl-quantum-eigensolver
description: "Reinforcement Learning Contracted Quantum Eigensolver (RL-CQE) methodology for computing electronic excited states and real-time quantum dynamics. Use when: designing quantum algorithms for many-fermion systems, excited state computation, variational quantum eigensolver variants, RL-assisted quantum simulation, contracted quantum eigensolver, quantum dynamics simulation, near-term quantum computing applications."
category: quantum
---

# RL-Quantum Eigensolver (RL-CQE)

Reinforcement learning-assisted contracted quantum eigensolver for excited states and real-time dynamics of many-body systems. Based on arXiv:2605.18569.

## Core Concept

A deep Q-network agent adaptively selects two-body operators at each iteration of the contracted quantum eigensolver (CQE), yielding more compact ansätze and improved convergence for:
- Electronic excited state computation
- Real-time quantum dynamics simulation
- Many-fermion system ground states (original application)

## Key Methodology

### 1. RL-CQE Framework

1. State: Current wavefunction parameters and residual energy
2. Action: Select next two-body operator from pool
3. Reward: Energy reduction / convergence improvement
4. Policy: Deep Q-network learns optimal operator selection strategy

### 2. Excited State Extension

- Orthogonality constraints enforced via penalty terms
- Sequential targeting: find n-th excited state orthogonal to lower states
- Modified reward: E_n - λ·Σ|⟨ψ_n|ψ_k⟩|² for k < n

### 3. Real-Time Dynamics

- Time-evolution via McLachlan variational principle
- RL agent selects operators minimizing time-step error
- Adaptive time-stepping based on convergence rate

## Implementation Pattern

```python
# Pseudocode for RL-CQE
class RLCQE:
    def __init__(self, hamiltonian, n_qubits):
        self.H = hamiltonian
        self.dqn = DeepQNetwork(state_dim, action_dim)
        self.operator_pool = generate_two_body_operators(n_qubits)
    
    def solve_excited_state(self, k, ortho_states=None):
        psi = initialize_state()
        for step in range(max_steps):
            state = encode_state(psi, self.H)
            action = self.dqn.select_action(state)
            op = self.operator_pool[action]
            psi_new = apply_operator(psi, op)
            reward = compute_energy_reduction(psi, psi_new, self.H)
            if ortho_states:
                reward -= penalty * orthogonality_violation(psi_new, ortho_states)
            self.dqn.update(state, action, reward, psi_new)
            psi = psi_new
        return psi
```

## When to Use

- Near-term quantum hardware (NISQ-era)
- Problems requiring excited state spectra
- Real-time evolution of quantum systems
- Chemistry/materials science applications

## Pitfalls

- Operator pool size grows combinatorially — use screening/selection
- DQN training requires many episodes — consider transfer learning
- Excited state orthogonality can be numerically unstable

## Activation
RL quantum eigensolver, contracted quantum eigensolver, excited state quantum, quantum dynamics RL, many-body quantum simulation, quantum chemistry neural
