---
name: qlif-cast-weather-forecasting
description: "QLIF-CAST: Quantum Leaky-Integrate-and-Fire methodology for time-series regression (weather forecasting). Hybrid quantum-classical recurrent architecture using single-qubit superpositions for neuron states. Demonstrates 15.4% MSE reduction over classical LIF and 94% faster convergence vs QLSTM/QNN."
tags: ["quantum-spiking", "time-series-forecasting", "quantum-machine-learning", "weather-forecasting", "hybrid-quantum-classical"]
category: ai_collection
---

# QLIF-CAST: Quantum Leaky-Integrate-and-Fire for Time-Series Forecasting

**arXiv**: 2605.18333 (May 18, 2026)
**Authors**: Alberto Marchisio, Aayan Ebrahim, Nouhaila Innan, Muhammad Kashif, Muhammad Shafique
**Category**: Quantum Physics (quant-ph); Machine Learning (cs.LG)

## Overview

QLIF-CAST extends the Quantum Leaky-Integrate-and-Fire (QLIF) spiking neural network from classification to **time-series regression**, specifically short-term multivariate weather forecasting. It encodes neuron excitation states as **single-qubit quantum superpositions** within a hybrid quantum-classical recurrent architecture.

## Core Innovation

### Quantum Neuron Model

Each QLIF neuron encodes its excitation state as a single-qubit state:
```
|ψ⟩ = cos(θ/2)|0⟩ + sin(θ/2)|1⟩
```

- **Rx rotation gates**: Drive neuron excitation based on input current
- **T1 relaxation decay**: Models natural decay (leaky behavior)
- **Threshold firing**: Measurement-based spike generation

### Hybrid Architecture

```
Input → Classical Feature Encoder → QLIF Recurrent Layer → Classical Decoder → Output
         (multivariate features)     (quantum neuron states)  (readout layer)
```

The QLIF layer sits within a recurrent structure, processing temporal sequences with quantum-enhanced dynamics.

## Key Results

### Evaluation 1: Weather Forecasting (vs Classical LIF)

| Metric | Classical LIF | QLIF-CAST | Improvement |
|--------|--------------|-----------|-------------|
| MSE | Baseline | **15.4% lower** | ↓ 15.4% |
| MAE | Baseline | **4.4% lower** | ↓ 4.4% |

Demonstrates quantum neuronal dynamics reduce prediction error over classical equivalents with matched parameters.

### Evaluation 2: Cross-Domain Comparison (vs QLSTM, QNN)

| Model | Training Time | Error | Speed-Accuracy Tradeoff |
|-------|--------------|-------|------------------------|
| QLSTM | 100% (baseline) | Baseline | Standard |
| QNN | ~60% | Higher error | Fast but less accurate |
| **QLIF-CAST** | **6%** (94% reduction) | Competitive | **Optimal position** |

### Hardware Verification

- Executed on **IBM Marrakesh** (156-qubit QPU)
- Only **1.2% average deviation** from simulation
- Confirms reliable circuit execution on real quantum hardware

## Methodology

### QLIF Neuron Dynamics

1. **Input Encoding**: Multivariate features → rotation angles for Rx gates
2. **Excitation Update**: |ψ(t)⟩ = Rx(input)|ψ(t-1)⟩
3. **T1 Decay**: Natural relaxation toward ground state
4. **Spike Detection**: Measure qubit; spike if |1⟩ probability exceeds threshold
5. **State Reset**: Post-spike reset to ground state

### Training

- Hybrid quantum-classical optimization
- Classical parameters: encoder/decoder weights
- Quantum parameters: rotation angles, thresholds
- Loss: MSE for regression tasks

## Applications

- **Weather forecasting**: Short-term multivariate prediction
- **Air quality prediction**: Cross-domain validation
- **Wind speed forecasting**: Time-series regression
- **General time-series**: Any continuous-valued prediction task

## Implementation Considerations

```python
# Conceptual QLIF-CAST architecture
class QLIF_CAST:
    def __init__(self, n_qubits, n_features):
        self.encoder = ClassicalEncoder(n_features, n_qubits)
        self.qlif = QLIFRecurrentLayer(n_qubits)  # Quantum circuit
        self.decoder = ClassicalDecoder(n_qubits)
    
    def forward(self, x):
        encoded = self.encoder(x)
        quantum_states = self.qlif(encoded)
        return self.decoder(quantum_states)
```

### Hardware Requirements

- Quantum backend: IBM Q (156+ qubits recommended)
- Classical co-processor for encoding/decoding
- Hybrid optimization framework (PennyLane, Qiskit)

## Comparison with Related Approaches

| Approach | Task Type | Quantum Advantage | Hardware Verified |
|----------|----------|-------------------|-------------------|
| QLIF (prior) | Classification | Yes | No |
| QLIF-CAST (this work) | **Regression** | **Yes (15.4% MSE)** | **Yes (IBM Marrakesh)** |
| QLSTM | Regression | Moderate | Some |
| QNN | Regression | Limited | Some |

## Limitations

- **NISQ-era constraints**: Limited qubit count and coherence time
- **Simulation vs Hardware**: 1.2% deviation may grow with larger circuits
- **Domain scope**: Primarily validated on environmental forecasting
- **Scalability**: Quantum advantage may diminish with classical hardware improvements

## Activation Keywords

- qlif-cast
- quantum leaky integrate fire
- quantum spiking neural network
- quantum time series forecasting
- hybrid quantum classical recurrent
- single qubit neuron
- quantum weather forecasting
- T1 relaxation neuron
- quantum regression
- Rx rotation neuron

## Citation

```bibtex
@article{marchisio2026qlifcast,
  title={QLIF-CAST: Quantum Leaky-Integrate-and-Fire for Time-Series Weather Forecasting},
  author={Marchisio, Alberto and Ebrahim, Aayan and Innan, Nouhaila and Kashif, Muhammad and Shafique, Muhammad},
  journal={arXiv preprint arXiv:2605.18333},
  year={2026}
}
```
