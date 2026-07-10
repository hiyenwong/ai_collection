---
name: qlif-cast-quantum-spiking-forecasting
description: Quantum Leaky-Integrate-and-Fire (QLIF-CAST) methodology for time-series forecasting. Adapts QLIF spiking neural networks for multivariate regression, achieving 15.4% lower MSE than classical LIF and 94% faster convergence than QLSTM/QNN. Activated by: quantum spiking forecasting, QLIF, time-series quantum, quantum regression.
---

# QLIF-CAST: Quantum Leaky-Integrate-and-Fire for Time-Series Forecasting

## Description
QLIF-CAST methodology adapts the Quantum Leaky Integrate-and-Fire (QLIF) spiking neural network for time-series regression tasks, specifically multivariate weather and environmental forecasting. It encodes neuron excitation states as single-qubit quantum superpositions driven by Rx rotation gates and T1 relaxation decay, within a hybrid quantum-classical recurrent architecture.

Key results:
- **15.4% lower MSE** vs parameter-matched classical LIF baseline
- **4.4% lower MAE** vs classical LIF
- **94% less training time** vs QLSTM and QNN on air quality/wind speed benchmarks
- **1.2% average deviation** from simulation on IBM Marrakesh 156-qubit QPU
- Occupies distinct position in speed-error trade-off space

## Activation Keywords
- quantum spiking forecasting
- QLIF-CAST
- quantum leaky integrate and fire
- quantum time-series regression
- quantum weather forecasting
- quantum spiking neural network forecasting
- 量子脉冲预测
- QLIF

## Core Architecture

### QLIF Neuron Model
- **State encoding**: Single-qubit quantum superposition $|\psi\rangle = \cos(\theta/2)|0\rangle + e^{i\phi}\sin(\theta/2)|1\rangle$
- **Excitation dynamics**: Rx rotation gates drive state evolution based on input
- **Leak mechanism**: T1 relaxation decay provides natural forgetting
- **Firing threshold**: Measurement probability determines spike emission
- **Recurrent connectivity**: Hybrid quantum-classical feedback loop

### Hybrid Architecture
```
Input Time-Series → Quantum Encoding → QLIF Layer → Classical Readout → Output
                        ↑                                          |
                        └──────────── Recurrent Feedback ─────────┘
```

## Usage Patterns

### Pattern 1: Weather/Environmental Forecasting
Use QLIF-CAST for multivariate time-series forecasting where:
- Data has temporal dependencies and multiple correlated features
- Classical LIF/RNN models show convergence bottlenecks
- Quantum speedup in training is valuable
- Applications: weather, air quality, wind speed, climate

### Pattern 2: Resource-Constrained Training
Use QLIF-CAST when:
- Training time is a critical constraint
- Need favorable speed-accuracy trade-off
- Classical LSTM/GRU models are too slow for the dataset size

### Pattern 3: NISQ-Era Deployment
Use QLIF-CAST for:
- Hybrid quantum-classical pipeline on current hardware
- Shallow quantum circuits with classical pre/post-processing
- Hardware verification confirms <2% simulation-to-hardware gap

## Instructions for Agents

### Step 1: Problem Assessment
Determine if QLIF-CAST is appropriate:
- **Is it time-series regression?** QLIF-CAST extends QLIF beyond classification to continuous prediction
- **Is data multivariate?** The model handles multiple correlated input features
- **Is speed important?** QLIF-CAST shows significant training speed advantages

### Step 2: Data Encoding
- Encode time-series features as rotation angles for Rx gates
- Use amplitude encoding for normalized input values
- Map temporal sequences to sequential quantum circuit applications

### Step 3: Architecture Design
```python
# Conceptual architecture
class QLIF_CAST:
    def __init__(self, n_qubits, n_classical_features):
        # QLIF neurons as qubits
        self.quantum_neurons = n_qubits
        # Rx rotation for input excitation
        self.rotation_gate = 'Rx'
        # T1 relaxation for leak
        self.t1_decay = parameter
        # Hybrid readout
        self.classical_readout = Linear(n_qubits, output_dim)
    
    def forward(self, x_t, h_prev):
        # Quantum state update
        psi = Rx(x_t) @ T1_decay(h_prev)
        # Measurement → classical
        spike = measure(psi)
        # Classical readout
        output = self.classical_readout(spike)
        return output, psi  # For recurrence
```

### Step 4: Training Protocol
- Use hybrid quantum-classical gradient descent
- Quantum circuit evaluation for forward pass
- Classical backpropagation for readout layer
- Parameter-shift rule for quantum gate gradients

### Step 5: Hardware Deployment
- Verify on simulator first
- Deploy on IBM QPU or similar NISQ device
- Expect ~1.2% deviation from simulation (as reported)
- Use error mitigation for noise resilience

## Error Handling

### Barren Plateau Problem
- QLIF-CAST's shallow circuit depth mitigates this vs deep QNNs
- Use layer-wise training if needed

### Noise Sensitivity
- T1 relaxation is physically motivated but can accumulate errors
- Apply measurement error mitigation on hardware
- Use the 1.2% hardware deviation as tolerance bound

### Classical Baseline Comparison
- Always compare against parameter-matched classical LIF
- Use MSE and MAE as primary metrics
- Track training time as secondary advantage

## Related Skills
- `spiking-neural-network-analysis` - SNN analysis methodology
- `quantum-neural-architecture` - QNN design patterns
- `hybrid-quantum-classical-systems` - Hybrid system engineering
- `qlif-quantized-burst-neurons-v2` - Related QLIF neuron models

## Reference
- Paper: "QLIF-CAST: Quantum Leaky-Integrate-and-Fire for Time-Series Weather Forecasting"
- Authors: Alberto Marchisio, Aayan Ebrahim, Nouhaila Innan
- arXiv: 2605.18333
- Published: 2026-05-18
