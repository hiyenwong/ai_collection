---
name: hybrid-quantum-time-series-forecasting
description: "Hybrid quantum-classical neural architecture methodology for time-series forecasting. Combines Quantum Leaky-Integrate-and-Fire (QLIF) spiking neurons with hybrid quantum-classical recurrent architectures for superior prediction accuracy."
---

# Hybrid Quantum Time-Series Forecasting

Methodology for building hybrid quantum-classical neural networks for time-series forecasting, combining quantum spiking neurons (QLIF) with classical recurrent architectures.

## Source Papers

- **QLIF-CAST**: arXiv:2605.18333 (2026-05-18) - Quantum Leaky-Integrate-and-Fire for Time-Series Weather Forecasting
- **Hybrid QNN NAS**: arXiv:2605.18345 (2026-05-18) - Hybrid Quantum-Classical Neural Architecture Search

## Core Architecture

### QLIF Neuron Model

The Quantum Leaky-Integrate-and-Fire (QLIF) neuron encodes membrane potential as single-qubit quantum states:

1. **State Encoding**: Neuron excitation state → qubit |ψ⟩ = cos(θ/2)|0⟩ + sin(θ/2)|1⟩
2. **Quantum Dynamics**: 
   - Rx rotation gates drive excitation from input spikes
   - T1 relaxation decay implements leak mechanism
3. **Firing**: Measurement collapses state; threshold crossing produces output spike
4. **Advantage**: Quantum superposition enables richer temporal dynamics than classical LIF

### Hybrid Quantum-Classical Recurrent Architecture

```
Input → Classical Preprocessing → QLIF Layer → Classical Post-processing → Output
              ↑                                    ↓
              └────────── Feedback Loop ──────────┘
```

Key design patterns:
- **Data Encoding**: Classical time-series → quantum state via amplitude/angle encoding
- **Circuit Structure**: Parameterized quantum circuits (PQC) with hardware-efficient ansatz
- **Measurement**: Expectation values of Pauli observables → classical signals
- **Coupling**: Classical layers for feature extraction, quantum layers for complex temporal modeling

## Implementation Steps

### Step 1: QLIF Neuron Implementation

```python
import pennylane as qml
import numpy as np

class QLIFNeuron:
    """Quantum Leaky-Integrate-and-Fire neuron."""
    
    def __init__(self, n_qubits=1, t1_decay=0.1):
        self.n_qubits = n_qubits
        self.t1_decay = t1_decay
        self.theta = 0.0  # membrane potential (qubit rotation angle)
    
    def integrate(self, input_spike):
        """Integrate input via Rx rotation gate."""
        self.theta += input_spike
        # Apply T1 relaxation (leak)
        self.theta *= np.exp(-self.t1_decay)
        # Clamp to [0, pi]
        self.theta = np.clip(self.theta, 0, np.pi)
    
    def fire(self, threshold=np.pi/2):
        """Check if neuron fires (measurement)."""
        if self.theta > threshold:
            self.theta = 0.0  # reset after firing
            return 1
        return 0
    
    def quantum_state(self):
        """Get current qubit state."""
        return np.array([np.cos(self.theta/2), np.sin(self.theta/2)])
```

### Step 2: QLIF-CAST Model Architecture

```python
import torch
import torch.nn as nn
import pennylane as qml

class QLIFLayer(nn.Module):
    """Quantum LIF layer using PennyLane."""
    
    def __init__(self, n_qubits, n_layers=2):
        super().__init__()
        self.n_qubits = n_qubits
        self.n_layers = n_layers
        self.weights = nn.Parameter(torch.randn(n_layers, n_qubits, 3))
        
        dev = qml.device("default.qubit", wires=n_qubits)
        
        @qml.qnode(dev)
        def circuit(inputs, weights):
            # Encoding
            for i in range(n_qubits):
                qml.RY(inputs[i], wires=i)
            
            # Variational layers
            for layer in range(n_layers):
                for i in range(n_qubits):
                    qml.Rot(*weights[layer, i], wires=i)
                for i in range(n_qubits - 1):
                    qml.CNOT(wires=[i, i + 1])
            
            return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]
        
        self.circuit = circuit
    
    def forward(self, x):
        # x: (batch, n_qubits)
        batch_size = x.shape[0]
        outputs = []
        for i in range(batch_size):
            out = self.circuit(x[i].detach().numpy(), self.weights.detach().numpy())
            outputs.append(out)
        return torch.tensor(outputs, dtype=torch.float32)

class QLIFCastModel(nn.Module):
    """QLIF-CAST hybrid quantum-classical recurrent model."""
    
    def __init__(self, input_dim, hidden_dim, n_qubits, output_dim, seq_len):
        super().__init__()
        self.seq_len = seq_len
        
        # Classical preprocessing
        self.input_proj = nn.Linear(input_dim, hidden_dim)
        
        # Quantum recurrent layer
        self.qlif = QLIFLayer(n_qubits)
        self.hidden_proj = nn.Linear(hidden_dim, n_qubits)
        
        # Classical post-processing
        self.output_proj = nn.Linear(n_qubits, output_dim)
        self.rnn = nn.GRU(hidden_dim, hidden_dim, batch_first=True)
    
    def forward(self, x):
        # x: (batch, seq_len, input_dim)
        batch_size = x.shape[0]
        
        # Classical feature extraction
        h = self.input_proj(x)
        h_rnn, _ = self.rnn(h)
        
        # Quantum processing
        q_input = self.hidden_proj(h_rnn)
        q_output = self.qlif(q_input.view(-1, q_input.shape[-1]))
        q_output = q_output.view(batch_size, self.seq_len, -1)
        
        # Output
        return self.output_proj(q_output)
```

### Step 3: Time-Series Data Encoding

```python
def encode_timeseries(data, n_qubits):
    """Encode multivariate time-series into quantum states."""
    # Normalize to [0, pi]
    normalized = (data - data.min()) / (data.max() - data.min()) * np.pi
    
    # Pad or truncate to n_qubits
    if len(normalized) < n_qubits:
        normalized = np.pad(normalized, (0, n_qubits - len(normalized)))
    else:
        normalized = normalized[:n_qubits]
    
    return normalized
```

## Key Results

| Metric | Classical LIF | QLIF-CAST | Improvement |
|--------|---------------|-----------|-------------|
| MSE | baseline | -15.4% | ↓ 15.4% |
| MAE | baseline | -4.4% | ↓ 4.4% |

## Hardware-Aware Design (FLOPs-Aware NAS)

For NISQ-era deployment:
1. **FLOPs as proxy**: Use classical FLOPs to estimate quantum circuit complexity
2. **Resource constraints**: Limit qubit count, circuit depth, measurement shots
3. **Architecture search**: Auto-tune encoding depth, variational layers, measurement strategy
4. **Noise resilience**: Design circuits robust to T1/T2 decoherence

## Activation Keywords

- quantum time series forecasting
- QLIF
- quantum spiking neural network
- hybrid quantum-classical neural network
- quantum recurrent architecture
- quantum machine learning forecasting

## Applicable Domains

- Weather/climate forecasting
- Financial time series prediction
- Sensor data anomaly detection
- Medical signal processing (EEG, ECG)
- Energy demand forecasting

## Pitfalls

1. **Barren plateaus**: Deep quantum circuits suffer from vanishing gradients
   - Solution: Use shallow circuits (< 10 layers), layer-wise training
2. **Statevector simulation limits**: Classical simulation scales as 2^n
   - Solution: Use tensor network simulators for > 20 qubits
3. **Shot noise**: Finite measurement shots add variance
   - Solution: Use 1000+ shots, or analytic gradients when available
4. **Data encoding bottleneck**: Loading classical data into quantum states is O(n)
   - Solution: Use amplitude encoding for exponential compression

## Verification Steps

1. Test QLIF neuron against classical LIF on same dataset
2. Verify quantum advantage scales with problem complexity
3. Check parameter-matched baseline fairness (same parameter count)
4. Validate on held-out test set with appropriate time-series split

## References

- arXiv:2605.18333 - QLIF-CAST: Quantum Leaky-Integrate-and-Fire for Time-Series Weather Forecasting
- arXiv:2605.18345 - Hybrid Quantum-Classical Neural Architecture Search
- arXiv:2505.01735 - Brain-Inspired Quantum Neural Architectures (QSNN + QLSTM)
- arXiv:2408.15462 - CTRQNets & LQNets: Continuous Time Recurrent and Liquid Quantum Neural Networks
