---
name: quantum-hierarchical-rl
description: "Quantum Hierarchical Reinforcement Learning using variational quantum circuits within option-critic architecture. Replaces classical components (feature extractors, option-value functions, termination functions, intra-option policies) with quantum circuits for parameter-efficient hierarchical decision-making. Use when: quantum reinforcement learning, hierarchical RL, option-critic quantum, variational quantum RL, parameter-efficient RL, quantum decision-making, quantum option-critic."
---

# Quantum Hierarchical Reinforcement Learning

## Description

Hybrid hierarchical RL agent using variational quantum circuits (VQCs) within the option-critic architecture. Substitutes classical components with quantum circuits for feature extraction, option-value estimation, termination functions, and intra-option policies. Achieves up to 66% parameter savings while outperforming classical baselines.

## Activation Keywords

- quantum reinforcement learning
- quantum hierarchical RL
- option-critic quantum
- variational quantum RL
- parameter-efficient RL
- quantum decision-making
- quantum option-critic
- quantum HRL

## Core Architecture

### Option-Critic Framework with Quantum Components

The option-critic architecture has four components; quantum replacement strategy:

| Component | Classical | Quantum Replacement | Effect |
|-----------|-----------|-------------------|--------|
| Feature Extractor | CNN/MLP | VQC | ✅ Best performer - saves 66% params |
| Option-Value Function | Linear layer | VQC | ⚠️ Bottleneck - degrades performance |
| Termination Function | Sigmoid | VQC | ⚠️ Mixed results |
| Intra-Option Policy | Softmax | VQC | ⚠️ Mixed results |

### Implementation Pattern

```python
# Quantum Feature Extractor (best performer)
class QuantumFeatureExtractor:
    def __init__(self, n_qubits, n_layers):
        self.n_qubits = n_qubits
        self.n_layers = n_layers
        self.params = nn.Parameter(torch.randn(n_layers, n_qubits, 3))
    
    def forward(self, state):
        # 1. Encode state into quantum amplitudes
        q_state = amplitude_encode(state)
        # 2. Apply variational layers
        for layer in range(self.n_layers):
            q_state = variational_layer(q_state, self.params[layer])
        # 3. Measure in computational basis
        return measure(q_state)

# Hybrid Option-Critic Agent
class QuantumOptionCritic:
    def __init__(self, n_qubits=4):
        self.feature_extractor = QuantumFeatureExtractor(n_qubits, n_layers=2)
        self.option_values = nn.Linear(n_qubits, n_options)  # Keep classical
        self.termination = nn.Linear(n_qubits, n_options)     # Keep classical
        self.intra_option_policy = nn.Linear(n_qubits, n_actions)  # Keep classical
```

### Key Findings from arXiv:2605.03434

1. **Quantum feature extractors outperform classical** with 66% fewer trainable parameters
2. **Quantum option-value estimation is a bottleneck** - degrades performance vs classical
3. **Circuit architecture matters**: depth, entanglement pattern, and encoding strategy affect results
4. **Hybrid approach wins**: quantum feature extractor + classical decision components is optimal
5. **Parameter efficiency is the key advantage**, not raw performance improvement

### Design Principles

- Use quantum circuits for feature extraction only (best results)
- Keep option-value functions classical (quantum version is bottleneck)
- Start with 4-8 qubits for feature encoding
- Use amplitude or angle encoding for state representation
- Monitor the noise-expressivity tradeoff as qubit count increases
- Evaluate on standard Gym environments before scaling

## Error Handling

- **Quantum option-value bottleneck**: If performance degrades, switch option-value to classical
- **Encoding mismatch**: Ensure state dimensions match qubit count (pad or PCA if needed)
- **Circuit depth**: Keep layers ≤ 3 for NISQ devices; deeper circuits accumulate too much noise

## Resources

- arXiv: https://arxiv.org/abs/2605.03434v1
- Option-critic architecture (Bacon et al., 2017)
- PennyLane or Qiskit for VQC implementation
