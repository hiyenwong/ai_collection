# On-Hardware QNN Training via Butterfly Circuits (arXiv:2606.03517)

## Paper
"Scalable On-Hardware Training of Quantum Neural Networks and Application to Clinical Data Imputation" — Mathur et al., 2026-06-02

## Problem
Training QNNs on quantum hardware bottlenecked by gradient estimation: standard parameter-shift requires O(n²) circuit evaluations with trainable parameters.

## Solution: Three Co-Designed Ingredients

### 1. Butterfly Circuit Architecture
- Structured, subspace-preserving ansatz with O(n log n) parameters
- Logarithmic circuit depth
- Commuting structure within each layer enables parallel gradient extraction

### 2. Layer-Wise Training Strategy
- Confine on-hardware optimization to one small layer at a time
- Freeze trained layers before adding next layer
- Avoids simultaneous optimization of all parameters

### 3. Parallelized Parameter-Shift Rule
- Exploits commuting structure within each Butterfly layer
- Extracts all gradients in constant number of circuit executions per layer
- Reduces evaluations from O(n²) to O(log n) per optimization step

## Validation
- IonQ Forte Enterprise trapped-ion hardware at 16 qubits
- Tensor-network simulation at 32 qubits
- 32-qubit inference executed on hardware
- No performance degradation relative to ideal or noisy simulation
- Clinical benchmark: MIMIC-III EHR data, patient survival prediction

## Key Results
- Hybrid classical-quantum models match or exceed classical neural baselines
- Reduced variance across training runs
- Practical, scalable QNN training under realistic hardware constraints

## Relationship to quantum-ml-patterns
This extends Pattern 1 (VQC Design) with a specific hardware-scalable architecture. The Butterfly circuit + layer-wise training + parallelized parameter-shift combination is a concrete instantiation that solves the O(n²) gradient bottleneck identified in the VQC pattern.

## When to Use
- QNN training on NISQ hardware with 16+ qubits
- Clinical/medical data with optimization instability sensitivity
- Any scenario where standard parameter-shift gradient estimation is the bottleneck
- Trapped-ion hardware preferred (but applicable to other platforms)

## Pitfalls
- Butterfly architecture restricts expressivity — verify task compatibility
- Layer-wise training may get stuck in local optima — add fine-tuning phase
- Hardware noise still affects results — combine with error mitigation
- Commuting parameter identification requires careful circuit analysis
