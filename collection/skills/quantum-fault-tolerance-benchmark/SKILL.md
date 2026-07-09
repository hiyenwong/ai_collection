---
name: quantum-fault-tolerance-benchmark
description: >
  Evaluate quantum error-correcting codes under hardware-motivated and biased noise models.
  Benchmark fault-tolerant quantum computing primitives via noisy stabilizer simulation.
  Use when: (1) evaluating QEC code performance, (2) designing fault-tolerant quantum circuits,
  (3) simulating quantum error correction under realistic noise, (4) comparing logical error rates
  across hardware platforms, (5) FTPrimitiveBench methodology.
---

# Quantum Fault Tolerance Benchmark

Evaluate fault-tolerant quantum computing primitives under realistic noise models.
Based on FTPrimitiveBench methodology (arXiv:2605.04049).

## Core Components

### 1. Noise Models

- **Biased noise**: Depolarizing, dephasing, amplitude damping with bias ratios
- **Hardware-motivated**: Derived from physical qubit characteristics (T1, T2, gate fidelities)
- **Correlated errors**: Spatial and temporal correlations matching hardware behavior

### 2. Error-Correcting Codes

- **Surface codes**: Planar, rotated, XZZX variants
- **Color codes**: 2D and 3D topological codes
- **LDPC codes**: Quantum low-density parity-check codes
- **Concatenated codes**: Recursive encoding schemes

### 3. Fault-Tolerant Primitives

- **Logical gates**: Transversal, lattice surgery, magic state distillation
- **State preparation**: Logical |0>, |+, magic states
- **Measurement**: Logical Pauli measurements
- **Memory**: Idle logical qubit preservation

## Workflow

### Step 1: Define Noise Model

```python
noise_model = {
    "gate_error_rate": 1e-3,
    "measurement_error_rate": 1e-3,
    "idle_error_rate": 1e-4,
    "bias_ratio": 100,  # Z errors >> X errors
    "correlation_length": 5  # Spatial correlation
}
```

### Step 2: Select QEC Code and Distance

Choose code type and code distance d. Logical error rate typically scales as:
p_L ≈ A * (p/p_th)^((d+1)/2)

### Step 3: Run Noisy Stabilizer Simulation

- Simulate circuit with noise injection at each operation
- Track syndrome measurements and apply decoder
- Count logical errors over many trials

### Step 4: Extract Metrics

- **Logical error rate**: Fraction of runs with uncorrectable errors
- **Threshold**: Physical error rate below which increasing d improves p_L
- **Overhead**: Physical qubits per logical qubit
- **Circuit depth**: Time to execute FT primitive

## Key References

- FTPrimitiveBench: arXiv:2605.04049
- Related: quantum-error-correction, quantum-systems-engineering

## Limitations

- Stabilizer simulation limited to Clifford circuits + magic states
- Computational cost scales with number of qubits and circuit depth
- Real hardware may have noise features not captured by models
