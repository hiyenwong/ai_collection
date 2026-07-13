---
name: quantum-cognitive-tunnelling-oscillators
description: "Quantum-tunnelling oscillator models for cognitive modelling and neural computation. Models optical illusion perception and group decision making using quantum-mechanical agents with context-dependent transitions. Use when: quantum cognition, cognitive modelling, decision making models, optical illusion perception, group decision making, quantum neural systems, quantum-tunnelling oscillators."
---

# Quantum Cognitive Tunnelling Oscillators

Quantum-tunnelling oscillator model as universal dynamical engine for quantum cognition problems.

## Core Concept

Treat cognitive agents as quantum-mechanical systems where choices shift through context-dependent transitions (tunnelling) rather than simple probabilities.

## Two Paradigmatic Applications

### 1. Optical Illusion Perception

Model ambiguous visual stimuli as quantum superposition states:
- Perceptual states as basis states in Hilbert space
- Perception switching as quantum tunnelling between minima
- Context acts as measurement collapsing the state

### 2. Group Decision Making

- Individuals as quantum-mechanical agents
- Network of coupled quantum-tunnelling oscillators
- Collective phenomena emerge from quantum-like entanglement

## Mathematical Framework

```python
import numpy as np
from scipy.integrate import solve_ivp

class QuantumCognitiveOscillator:
    def __init__(self, n_states, coupling=0.0):
        self.n = n_states
        self.coupling = coupling
        
    def tunnelling_hamiltonian(self, context_bias):
        """Hamiltonian with context-dependent potential."""
        H = np.zeros((self.n, self.n), dtype=complex)
        # Diagonal: energy levels (cognitive states)
        np.fill_diagonal(H, context_bias)
        # Off-diagonal: tunnelling amplitudes
        for i in range(self.n - 1):
            H[i, i+1] = H[i+1, i] = 0.1
        return H
    
    def evolve(self, state0, dt=0.1):
        """Time evolution of cognitive state."""
        H = self.tunnelling_hamiltonian(np.zeros(self.n))
        U = scipy.linalg.expm(-1j * H * dt)
        return U @ state0
```

## Key Principles

1. **Context-dependence**: Transitions depend on environmental context
2. **Network effects**: Coupled oscillators reproduce collective phenomena
3. **Non-classical probability**: Interference and superposition in decisions
4. **Machine-vision realisation**: Can be implemented with standard neural network tools

## When to Use

- Modeling ambiguous perception (illusions, bistable stimuli)
- Group decision dynamics with context effects
- Any cognitive task showing order effects or conjunction fallacy
- Neural computation where classical probability fails
