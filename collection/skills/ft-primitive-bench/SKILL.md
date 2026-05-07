---
name: ft-primitive-bench
description: >
  Fault-tolerant quantum benchmarking methodology using FTPrimitiveBench framework.
  Systematic benchmarking of quantum error-correcting codes under hardware-motivated
  noise models (Pauli bias, measurement bias, spatial/temporal non-uniformity).
  Supports logical primitives: memory, lattice surgery, transversal Hadamard, phase gate.
  Enables hardware-aware co-design of fault-tolerant quantum architectures.
  Activation: fault-tolerant benchmark, quantum benchmarking, FTPrimitiveBench,
  hardware-motivated noise, logical primitive benchmark, QEC benchmark,
  noise model specification, surface code primitives, quantum error correction testing,
  容错量子基准测试, 量子误差纠正基准
---

# FTPrimitiveBench: Fault-Tolerant Quantum Benchmarking

Systematic methodology for benchmarking quantum error-correcting codes under
hardware-motivated noise models, enabling reproducible comparative studies of
QEC protocols and hardware-aware co-design.

## Core Concepts

### Noise Model Taxonomy

| Noise Family | Description | Hardware Origin |
|-------------|-------------|-----------------|
| **Pauli Bias** | Asymmetric X/Y/Z error rates | Physical gate implementations |
| **Measurement Bias** | Different error rates for different measurement outcomes | Readout hardware |
| **Spatial Non-uniformity** | Position-dependent error rates | Device fabrication variations |
| **Spatio-temporal** | Time-varying spatial correlations | Environmental fluctuations |

### Logical Primitives

| Primitive | Operation | Significance |
|-----------|-----------|--------------|
| **Logical Memory** | Store logical qubit over time | Baseline coherence test |
| **Lattice Surgery** | Merge/split logical qubits | Two-qubit operations |
| **Transversal Hadamard** | Logical H gate | Clifford gate set |
| **Logical Phase Gate** | S gate via lattice surgery | Non-Clifford extension |

## Benchmarking Workflow

### Step 1: Noise Model Specification

Define structured noise that reflects target hardware:

```python
# Example: Pauli-biased noise model
noise_spec = {
    "type": "pauli_bias",
    "bias_ratio": {"X": 0.01, "Y": 0.001, "Z": 0.1},  # Z-biased
    "correlation_length": 0,  # Independent errors
}

# Example: Spatial non-uniformity
noise_spec = {
    "type": "spatial",
    "base_rate": 0.001,
    "variation": 0.5,  # 50% variation across device
    "correlation_length": 3,  # Errors correlated within 3 qubits
}
```

### Step 2: Primitive Construction

Build the circuit for each logical primitive at target code distance:

```python
# Parameters
code_distance = 5
num_rounds = 10
primitive = "logical_memory"  # or "lattice_surgery", "transversal_hadamard", "phase_gate"

# Construct stabilizer circuit for the primitive
circuit = build_primitive_circuit(
    code_type="surface_code",
    distance=code_distance,
    primitive=primitive,
    rounds=num_rounds
)
```

### Step 3: Noisy Simulation

Run HPC-scale stabilizer simulation with specified noise:

```python
# Monte Carlo simulation
results = simulate_noisy(
    circuit=circuit,
    noise_model=noise_spec,
    num_shots=10000,
    decoder="mwpm"  # Minimum Weight Perfect Matching
)

# Extract logical error rate
logical_error_rate = results["logical_error_rate"]
confidence_interval = results["confidence_interval"]
```

### Step 4: Analysis

Compare results across noise models and primitives:

```python
# Key analysis: structured noise affects primitives differently
analysis = {
    "noise_primitive_interaction": compare_across_primitives(results),
    "decoder_sensitivity": compare_decoders(results),
    "hardware_co_design": identify_optimal_code_distance(results),
}
```

## Key Findings from Research

1. **Structured noise affects primitives qualitatively differently** - memory benchmarks
   alone cannot predict performance of active logical computation
2. **Noise-primitive-decoder interplay matters** - the optimal decoder depends on
   both the noise structure and which primitive is being executed
3. **Hardware-aware co-design is essential** - uniform depolarizing noise models
   miss opportunities for joint code-hardware optimization
4. **Benchmarks must extend beyond memory** - lattice surgery and gate operations
   reveal failure modes invisible to memory-only testing

## Integration with Existing Skills

- **quantum-error-correction-methods**: QEC code selection and analysis
- **quantum-fault-tolerance-benchmark**: Hardware-modeled fault tolerance evaluation
- **quantum-ml-patterns**: ML-assisted decoder design
- **systems-engineering**: Systematic methodology and reproducibility

## Usage Examples

### Basic Benchmark Run
```
使用 FTPrimitiveBench 在表面码上测试逻辑内存和晶格手术的基准性能
```

### Hardware Co-design
```
基于 Pauli 偏置噪声模型，设计最优的表面码距离和解码器组合
```

### Noise Model Comparison
```
比较均匀去极化噪声和结构化噪声对量子逻辑门的影响
```

## Pitfalls

- **Uniform depolarizing is insufficient** - it misses structured error correlations
  present in real hardware
- **Memory-only benchmarks are incomplete** - they don't capture gate operation failures
- **Decoder choice matters** - different decoders perform differently under structured noise
- **Simulation scale is critical** - HPC-scale simulation needed for realistic distances

## Resources

- GitHub: https://github.com/ShuwenKan/FTPrimitiveBench
- arXiv: 2605.04049 - "FTPrimitiveBench: A Benchmark Suite For Logical Computation
  Under Hardware-Motivated and Biased Noise Models"
