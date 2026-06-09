---
name: q-spirl-quantum-spiking-rl
description: "Q-SpiRL: Quantum Spiking Reinforcement Learning framework combining spike-based temporal processing with variational quantum feature transformation for adaptive robot navigation and control. Use when: quantum reinforcement learning, spiking neural network RL, quantum spiking systems, robot navigation policies, quantum-enhanced SNN."
---

# Q-SpiRL: Quantum Spiking Reinforcement Learning

**arXiv**: 2605.20801 (2026-05-20)
**Authors**: Mohamed Khair Altrabulsi, Nouhaila Innan, Alberto Marchisio, Muhammad Kashif, Muhammad Shafique
**Categories**: cs.RO, quant-ph

## Core Idea

Q-SpiRL combines **spike-based temporal processing** (SNNs) with **variational quantum feature transformation** (VQC) in a reinforcement learning framework for adaptive robot navigation. The central QSNN (Quantum Spiking Neural Network) architecture achieves up to **99% success rate** in obstacle-aware navigation while maintaining high path efficiency.

## Architecture

### Five Agent Families Evaluated

1. **Tabular Q-Learning** - baseline classical approach
2. **Classical MLP** - multi-layer perceptron policy
3. **Classical SNN** - spiking neural network policy
4. **Quantum-enhanced MLP (QMLP)** - quantum features + MLP
5. **Quantum Spiking Neural Network (QSNN)** - quantum features + SNN (central contribution)

### QSNN Architecture Flow

```
Environment State → LIF Spiking Neurons → Spike Trains → Variational Quantum Circuit (VQC)
       → Quantum Feature Space → Measurement → Action Selection (Q-learning update)
```

The key insight: **spikes encode temporal dynamics naturally**, and the **quantum layer provides high-dimensional feature transformation** that captures complex obstacle-avoidance patterns classical networks miss.

## Implementation Pattern

```python
import pennylane as qml
import torch
import torch.nn as nn

class QSNNLayer(nn.Module):
    """Quantum Spiking Neural Network layer combining LIF neurons with VQC."""
    
    def __init__(self, n_spikes, n_qubits, n_actions):
        super().__init__()
        self.n_spikes = n_spikes
        self.n_qubits = n_qubits
        self.n_actions = n_actions
        
        # Spike encoding: temporal spike trains → phase encoding
        self.phase_encoder = nn.Linear(n_spikes, n_qubits)
        
        # Variational quantum circuit
        self.q_weights = nn.Parameter(torch.randn(3, n_qubits))
        
        # Measurement to action logits
        self.measurement = nn.Linear(n_qubits, n_actions)
        
    def forward(self, spike_trains):
        # Encode spikes as rotation angles
        phases = self.phase_encoder(spike_trains)
        
        # Apply parameterized quantum circuit
        # Each qubit gets a rotation based on spike timing
        # Ansatz: hardware-efficient with entangling layers
        circuit_output = self._quantum_circuit(phases)
        
        # Measure in computational basis → classical logits
        logits = self.measurement(circuit_output)
        return logits
    
    def _quantum_circuit(self, phases):
        """Hardware-efficient variational ansatz."""
        # Rotation encoding + entangling layers
        # Returns measurement expectations
        pass
```

## Training Pipeline

### Unified Evaluation Framework

All agent families trained under **identical conditions**:
- **Environments**: Grid-worlds (20×20, 30×30, 40×40) with static + dynamic obstacles
- **Metrics**: Success rate, success-weighted path length (SPL), path length, turn rate
- **Inference**: Deterministic (no exploration noise)

### Key Results

| Environment | QSNN Success Rate | Path Efficiency |
|-------------|-------------------|-----------------|
| 20×20       | ~99%              | High            |
| 30×30       | ~98%              | High            |
| 40×40       | ~97%              | High            |

### Hardware Deployment

- Executed on **IBM quantum hardware** (real-device conditions)
- Demonstrates **practical feasibility** of hybrid quantum-spiking policies
- Circuit depth optimized for NISQ-era constraints

## Key Insights

1. **QSNN > QMLP > Classical SNN > Classical MLP** in overall trade-off
2. **Spike-based temporal encoding** captures dynamic obstacle patterns better than static inputs
3. **Quantum feature space** provides non-linear transformations classical networks struggle with
4. **Deterministic inference** shows robust learned policies (not relying on exploration)

## When to Use

- **Robot navigation** in dynamic/unknown environments
- **Reinforcement learning** with temporal/spike-based state representations  
- **Quantum machine learning** applications requiring hardware deployment
- **Hybrid quantum-classical** systems needing efficient feature transformation
- **Control systems** where trajectory smoothness and success rate are critical

## Activation

quantum reinforcement learning, quantum spiking, QSNN, spike-based RL, quantum robot navigation, quantum SNN policy, variational quantum RL, quantum-enhanced control, IBM quantum deployment
