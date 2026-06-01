---
name: q-spirl-quantum-spiking-rl
description: >
  Quantum Spiking Reinforcement Learning (Q-SpiRL) methodology for adaptive robot navigation
  and decision-making. Combines quantum circuit-enhanced state representation with spiking neural
  networks (SNNs) in a reinforcement learning framework. Use when: designing quantum-enhanced
  SNN agents, implementing QSNN/QMLP architectures for RL tasks, comparing quantum vs classical
  SNN performance, building neuromorphic quantum hybrid systems for robotics/navigation, or
  exploring quantum advantage in spiking network RL. Covers five agent families: tabular Q-learning,
  classical MLP, classical SNN, quantum-enhanced MLP (QMLP), and quantum-enhanced SNN (QSNN).
  Triggers: quantum spiking RL, Q-SpiRL, quantum SNN reinforcement learning, neuromorphic quantum,
  quantum robot navigation, QSNN, QMLP, quantum-enhanced spiking network.
---

# Q-SpiRL: Quantum Spiking Reinforcement Learning

## Core Framework

Q-SpiRL integrates quantum circuits into spiking neural networks for reinforcement learning,
evaluating five agent families under a unified framework:

1. **Tabular Q-learning** - baseline
2. **Classical MLP** - standard feedforward
3. **Classical SNN** - leaky integrate-and-fire (LIF) neurons
4. **Quantum-enhanced MLP (QMLP)** - quantum variational circuit + classical MLP
5. **Quantum-enhanced SNN (QSNN)** - quantum variational circuit + spiking neurons

## Architecture Pattern

```
State → [Quantum Feature Map] → [Quantum Variational Circuit] → [Measurement] → [Classical/SNN Policy] → Action
```

### Quantum Circuit Integration

- Encode state observations into qubit rotation angles
- Apply parameterized gates (RY, RZ, CNOT entanglement layers)
- Measure in computational basis to get enhanced features
- Feed measurements into policy network (MLP or SNN)

### SNN Policy Layer

For QSNN: quantum features drive LIF neuron membrane potentials
- Spike trains encode action probabilities
- Surrogate gradient descent for training through spiking nonlinearity
- Temporal coding preserves quantum feature richness over time steps

## Key Design Decisions

### Quantum Encoding Strategy
- **Amplitude encoding**: compact but requires state normalization
- **Angle encoding**: robust, maps each feature to qubit rotation
- **Basis encoding**: binary feature representation, N qubits for N binary features

### Entanglement Patterns
- Linear nearest-neighbor CNOT chains: shallow circuits, NISQ-friendly
- All-to-all entanglement: maximal expressivity, higher decoherence risk
- Circular entanglement: balanced connectivity with boundary wrap

### Training Protocol
1. Pre-train quantum circuit on state representation task (optional)
2. Train policy network with PPO/DQN using surrogate gradients
3. Joint fine-tuning of quantum circuit parameters + policy weights

## Performance Considerations

- QSNN typically outperforms classical SNN on complex navigation tasks with obstacles
- Quantum enhancement most pronounced in high-dimensional state spaces
- Circuit depth should match coherence time of target hardware
- Surrogate gradient choice critically affects SNN training stability

## Implementation Checklist

- [ ] Define quantum feature map matching state space dimensionality
- [ ] Choose variational ansatz (hardware-efficient or problem-inspired)
- [ ] Select SNN neuron model (LIF, Izhikevich, etc.)
- [ ] Implement surrogate gradient for backprop through spikes
- [ ] Design reward function for RL task
- [ ] Compare all five agent families under identical conditions
- [ ] Benchmark sample efficiency, final performance, inference latency

## Pitfalls

- **Barren plateaus**: deep quantum circuits cause vanishing gradients; use shallow ansatz
- **Spike saturation**: SNN neurons firing at max rate; adjust threshold or input scaling
- **Quantum-classical mismatch**: features from quantum circuit may not align with SNN dynamics; add normalization layer
- **Simulation overhead**: SNN + quantum simulation is slow; use event-driven SNN simulators
