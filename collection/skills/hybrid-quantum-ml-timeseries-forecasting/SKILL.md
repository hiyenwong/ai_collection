---
name: hybrid-quantum-ml-timeseries-forecasting
description: "Hybrid quantum-classical machine learning methodology for multi-output time-series forecasting at utility scale on NISQ devices. Combines Kernelized Quantum Reservoir Computing with Repeated Measurement (KQRC-RM) and Projected Quantum Kernel Gaussian Process (QGP) for real-world energy forecasting. Demonstrated at 100+ qubit scale on ibm_marrakesh. Activation: quantum time-series, hybrid QML forecasting, quantum reservoir computing, quantum kernel GP, utility scale quantum ML."
---

# Hybrid Quantum-ML Time-Series Forecasting at Utility Scale

Methodology for hybrid quantum-classical machine learning applied to multi-output time-series forecasting, demonstrated at 100+ qubit scale on NISQ hardware.

## Source Paper

- **arXiv: 2605.24252** — "Hybrid Quantum-Classical Machine Learning Algorithms for Multi-Output Time-Series Forecasting at Utility Scale"
- **Authors**: Mackenson Polché, Varun Puram, Aditi Lal, Weronika Golletz, Joan Étude Arrow, Vardaan Sahgal, Kumar Ghosh, Giorgio Cortiana, Corey O'Meara
- **Published**: 2026-05-22
- **Categories**: quant-ph

## Core Problem

Multi-output time-series forecasting in energy systems is challenged by:
- Nonlinear dynamics
- Multi-scale seasonality
- Strong cross-series dependencies
- Limited qubit counts on NISQ devices

## Two Hybrid Frameworks

### 1. KQRC-RM (Kernelized Quantum Reservoir Computing with Repeated Measurement)

- **Architecture**: Coupled quantum reservoirs + ancilla-assisted repeated measurement + kernelized readouts
- **Purpose**: Jointly model temporal dynamics and cross-stream correlations
- **Results (3-stream, 114 qubits)**:
  - MPS simulator: MAE = 0.0811 (36.92% improvement over classical analog)
  - Hardware (ibm_marrakesh): MAE = 0.1524 (performance degradation on real hardware)

### 2. QGP (Projected Quantum Kernel Gaussian Process)

- **Architecture**: Replaces fidelity-based kernels with projected kernels from local reduced-state statistics
- **Purpose**: Multi-output prediction using topology-aware quantum kernels
- **Results (100-qubit, 100 outputs)**:
  - 49% of outputs achieve high-accuracy (MAE < 0.15)
  - Average MAE for low-error group: 0.082
  - Medium-error regime (MAE 0.15–0.35): avg MAE 0.229
  - High-error regime: avg MAE 0.664
  - **Overall**: 62.01% MAE reduction on simulator, 40.37% on hardware vs classical GP baseline

## Key Techniques

### Projected Quantum Kernels
- Construct kernels from local reduced-state statistics instead of full state fidelity
- More robust to noise than fidelity-based approaches
- Topology-aware: accounts for device connectivity constraints

### Kernelized Readouts
- Classical kernel methods applied to quantum reservoir outputs
- Bridges quantum feature extraction with classical regression

### Ancilla-Assisted Repeated Measurement
- Improves signal-to-noise ratio through repeated measurement cycles
- Critical for extracting useful information from noisy intermediate-scale devices

## Implementation Steps

1. **Data Preparation**: Collect multi-stream time-series data with known correlations
2. **Quantum Reservoir Design**: Map input streams to coupled quantum reservoirs
3. **Repeated Measurement**: Use ancilla qubits for improved readout fidelity
4. **Kernel Construction**: Build quantum kernels from reduced-state statistics
5. **Classical Readout**: Apply kernelized regression for final predictions
6. **Topology Mapping**: Optimize circuit layout for target hardware connectivity

## Hardware Considerations

- **Qubit Budget**: 100+ qubits needed for utility-scale problems
- **Circuit Depth**: Must respect coherence time constraints
- **Connectivity**: Topology-aware compilation essential
- **Noise Mitigation**: Repeated measurement + projected kernels reduce noise sensitivity

## Performance Expectations

| Metric | Simulator | Hardware |
|--------|-----------|----------|
| MAE improvement vs classical | 36–62% | 40% |
| Qubit requirement | 100–114 | 100–114 |
| High-accuracy outputs | ~70% | ~49% |

## Pitfalls

- **Hardware degradation**: Real device performance significantly below simulation
- **Scaling limits**: Performance varies across output streams — not all achieve high accuracy
- **Classical baseline**: Must compare against strong classical baselines (GP, not simple models)
- **Qubit overhead**: Multi-output problems require many qubits; single-output may be more practical on current hardware

## When to Use

- Multi-output time-series with strong cross-correlations
- Energy/utility-scale forecasting problems
- When classical models struggle with nonlinear multi-scale patterns
- When 100+ qubit quantum hardware is available
