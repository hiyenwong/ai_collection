---
name: fpqc-sac-quantum-financial-rl
description: FPQC-SAC methodology — Parameterized Quantum Circuit (PQC) integrated with Soft Actor-Critic (SAC) for financial reinforcement learning under low signal-to-noise ratio (SNR) conditions. Places PQC before actor/critic networks to constrain features, using quantum entanglement for cross-asset interactions.
---

# FPQC-SAC: Quantum Financial RL

## Description

FPQC-SAC (Frontier PQC Soft Actor-Critic) methodology integrating Parameterized Quantum Circuits (PQC) with Soft Actor-Critic (SAC) for financial reinforcement learning in low-SNR environments. The PQC layer is placed **before** the actor/critic networks to constrain and entangle feature representations, capturing cross-asset correlations that classical networks miss. Demonstrated 66.89% return gain over classical SAC on financial trading tasks.

## Activation Keywords
- fpqc-sac
- quantum financial rl
- quantum SAC
- PQC reinforcement learning
- quantum trading agent
- parameterized quantum circuit finance
- low SNR financial RL
- 量子金融强化学习
- quantum portfolio SAC
- entangled asset trading

## Tools Used
- terminal: Run quantum simulation (PennyLane, Qiskit) and RL training
- python: Implement FPQC-SAC pipeline
- write: Save training scripts and model checkpoints

## Methodology

### Core Architecture

```
Market State → Feature Engineering → PQC Layer → Entangled Features
    → Actor Network (SAC) → Action (Buy/Hold/Sell)
    → Critic Network (SAC) → Q-Value
    → Entropy Bonus → Policy Update
```

### Key Components

#### 1. Feature Engineering Pipeline
- Extract technical indicators from market data (returns, volume, volatility)
- Normalize features to [-1, 1] range for quantum encoding
- Feature vector dimension matches qubit count (or use angle encoding for fewer qubits)

#### 2. Parameterized Quantum Circuit (PQC)
- **Encoding**: Angle encoding maps normalized features to qubit rotation angles
- **Ansatz**: Hardware-efficient layers with entangling gates (CNOT/CZ chains)
- **Depth**: 2-4 layers for NISQ compatibility
- **Trainable Parameters**: Rotation angles optimized during RL training

#### 3. SAC Integration
- **PQC Output**: Measurement expectations become input to classical actor/critic
- **Actor Network**: Maps entangled features to action distribution (Gaussian policy)
- **Critic Networks**: Two Q-networks for clipped double Q-learning
- **Temperature (α)**: Auto-tuned for entropy regularization
- **Replay Buffer**: Standard SAC experience replay

### Training Protocol

```python
# Pseudo-code for FPQC-SAC training loop
for episode in range(num_episodes):
    state = env.reset()
    for step in range(max_steps):
        # 1. Encode state into quantum circuit
        quantum_features = pqc_forward(state)  # Measurement expectations
        
        # 2. Classical actor/critic on quantum features
        action, log_prob = actor(quantum_features)
        q1, q2 = critic1(quantum_features, action), critic2(quantum_features, action)
        
        # 3. Execute action in environment
        next_state, reward, done = env.step(action)
        
        # 4. SAC updates (standard)
        target_q = reward + gamma * (min_q_target - alpha * next_log_prob)
        critic_loss = MSE(q, target_q)
        actor_loss = alpha * log_prob - min_q
        alpha_loss = -alpha * (log_prob + target_entropy)
        
        # 5. Update all networks (including PQC parameters)
        update_all(critic_loss, actor_loss, alpha_loss)
        
        state = next_state
```

### Quantum Feature Encoding

| Encoding | Qubits | Description |
|----------|--------|-------------|
| Angle | N features | Each feature → rotation angle on single qubit |
| Amplitude | log2(N) | Encode all features in state amplitudes |
| IQP | N features | Instantaneous Quantum Polynomial-time encoding |

### PQC Ansatz Design

```
Layer 1: Rx(θ₁) ⊗ Ry(θ₂) ⊗ ... ⊗ Rn(θₙ)  # Data encoding
         CZ₁₂ ⊗ CZ₂₃ ⊗ ... ⊗ CZₙ₋₁,ₙ      # Entangling gates
         Rx(φ₁) ⊗ Ry(φ₂) ⊗ ... ⊗ Rn(φₙ)   # Trainable rotations

Layer 2: Repeat with different parameters
```

### Key Advantages

1. **Cross-Asset Entanglement**: Quantum entanglement captures non-linear correlations between assets that classical neural networks struggle with
2. **Low-SNR Robustness**: PQC acts as a feature filter, amplifying signal in noisy financial data
3. **Parameter Efficiency**: Quantum circuits can represent complex functions with fewer parameters
4. **Hardware-Aware**: Circuit depth designed for NISQ-era devices (2-4 layers)

### Hyperparameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| Learning Rate | 3e-4 | Adam optimizer for all networks |
| Batch Size | 256 | Mini-batch for SAC updates |
| Gamma | 0.99 | Discount factor |
| Target Entropy | -dim(action) | Automatic temperature tuning |
| PQC Layers | 2-4 | Circuit depth |
| Replay Buffer | 1e6 | Experience replay size |

## Error Handling

### Low-Qubit Limitation
- If asset dimension > available qubits, use dimensionality reduction (PCA) before encoding
- Or use amplitude encoding which requires log2(N) qubits

### Gradient Vanishing (Barren Plateaus)
- Use local cost functions instead of global
- Initialize parameters close to identity
- Use layer-wise training for deep circuits

### Classical Baseline Comparison
- Always compare against pure classical SAC
- Track: total return, Sharpe ratio, max drawdown
- Statistical significance testing required

## Implementation Notes

### PennyLane Implementation
```python
import pennylane as qml
import torch

n_qubits = 4
dev = qml.device("default.qubit", wires=n_qubits)

@qml.qnode(dev)
def quantum_circuit(inputs, weights):
    # Encoding
    for i in range(n_qubits):
        qml.RY(inputs[i], wires=i)
    
    # Entangling + trainable layers
    for layer in range(len(weights)):
        for i in range(n_qubits):
            qml.Rot(*weights[layer][i], wires=i)
        for i in range(n_qubits - 1):
            qml.CNOT(wires=[i, i + 1])
    
    return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]
```

### Integration with Stable Baselines3
- Use custom feature extractor in SAC policy
- Replace first layer with quantum circuit output
- Maintain all SAC training logic

## References
- arXiv:2606.10448 — FPQC-SAC: Quantum Financial RL (primary source)
- arXiv:2606.07727 — CVaR Portfolio Quantum Benchmarking
- arXiv:2512.22001 — VQE for Real-World Finance
- arXiv:2601.18811 — VQC-Based RL for Dynamic Portfolio

## Related Skills
- qrl-dynamic-portfolio
- qaoa-portfolio-optimization
- quantum-ml-healthcare
