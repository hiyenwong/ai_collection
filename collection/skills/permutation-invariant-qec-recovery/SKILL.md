---
name: permutation-invariant-qec-recovery
description: "Quantum Error Recovery (QER) methodology for permutation-invariant (PI) quantum codes under correlated noise. Uses channel-aware recovery maps with tunable PI code parameters to achieve fidelity beyond noise-independent QEC. Covers CAD code family construction, coherent recovery circuit compilation, and low-overhead implementation."
---

# Permutation-Invariant QEC Recovery

## Description
Quantum Error Recovery (QER) methodology using permutation-invariant (PI) codes with channel-aware recovery maps. Unlike stabilizer codes that require noise-parameter-independent correction, QER uses knowledge of the error channel to find optimal recovery maps, restoring the uncorrupted state with higher fidelity. PI codes offer tunable parameters to suit the noise model and benefit from simple recovery circuits with reduced addressability requirements.

## Activation Keywords
- permutation invariant quantum code
- PI code recovery
- correlated error correction
- amplitude damping recovery
- CAD code
- quantum error recovery
- coherent recovery map
- 置换不变量子码恢复
- 相关振幅阻尼恢复

## Core Concepts

### Quantum Error Recovery (QER) vs QEC
- **QEC**: Noise-parameter independent; applies fixed correction regardless of noise strength
- **QER**: Noise-parameter dependent; uses channel knowledge to find optimal recovery map, exceeding QEC fidelity

### Permutation-Invariant (PI) Codes
- Codes symmetric under any permutation of physical qubits
- Tunable parameters to match specific noise models
- Simple recovery circuits with reduced addressability vs stabilizer codes
- Effective for non-Pauli noise (e.g., correlated amplitude damping)

### CAD Codes (Correlated Amplitude-Damping)
- New PI code family for global symmetric amplitude-damping errors
- **CAD4**: 4-qubit code, perfectly corrects 1 global symmetric AD error, recovery circuit uses 10 system/ancilla gates
- **CAD9**: 9-qubit code, outperforms many existing codes by >1 order of magnitude

## Methodology

### Step 1: Noise Model Characterization
Identify the error channel:
- **Collective symmetric AD**: All qubits experience same amplitude-damping rate
- **Local symmetric correlated AD**: Per-qubit AD with symmetric correlations
- Model the channel using Kraus operators for the specific noise process

### Step 2: PI Code Selection/Design
Choose or design a PI code family:
- For amplitude damping: Use CAD code family
- For other correlated noise: Design PI code with parameters tuned to noise model
- Key parameters: code distance, number of physical qubits, symmetry group

### Step 3: Optimal Recovery Map Computation
Compute the coherent QER map:
1. Characterize the error channel mathematically
2. Solve for optimal recovery map maximizing average fidelity
3. Express recovery as a quantum circuit (system + ancillary qubits)

### Step 4: Circuit Compilation
Compile the recovery map to an implementable circuit:
- Use linear geometric phase gates for CAD4 (10 gates total)
- Minimize system-ancilla gate count
- Respect hardware connectivity constraints

### Step 5: Fidelity Evaluation
Compare QER fidelity vs standard QEC:
- Benchmark against noise-parameter independent correction
- Evaluate under varying noise strengths
- Measure improvement factor (CAD9 shows >10x improvement)

## Workflow

### Pattern 1: Correlated Amplitude-Damping Recovery
For systems experiencing correlated AD noise:
1. Model the AD channel with correlation parameter
2. Select CAD4 or CAD9 based on qubit budget
3. Compute optimal recovery map for the channel
4. Compile to circuit using geometric phase gates
5. Deploy with fidelity monitoring

### Pattern 2: General Correlated Noise QER
For arbitrary correlated noise models:
1. Obtain/process noise channel estimate
2. Design PI code symmetric under the noise symmetry group
3. Compute optimal recovery via convex optimization
4. Compile recovery circuit
5. Validate fidelity improvement over standard QEC

## Error Handling
### Non-Pauli Noise
Stabilizer codes often require additional overhead for non-Pauli noise. Use PI codes which naturally handle correlated non-Pauli noise with lower overhead.

### Recovery Map Complexity
For large codes, optimal recovery map computation can be expensive. Use approximate recovery or decompose into smaller sub-problems.

## Resources
- Paper: arXiv:2607.02346
- Related: `quantum-error-correction-methods` (umbrella), `loss-biased-qec` (bias-tailored QEC)
