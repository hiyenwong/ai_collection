---
name: tree-tensor-network-compilation
description: "Tree tensor network renormalisation methodology for compiling matrix product states (MPS) into log-depth quantum circuits. Use when: loading quantum states onto quantum hardware, building shallow circuits for MPS/MPO, verifying quantum circuits, circuit-level device calibration, reducing circuit depth for NISQ-era algorithms, quantum state preparation, and overlap estimation. arXiv: 2605.06579"
---

# Tree Tensor Network Compilation for Quantum State Preparation

Practical log-depth quantum state preparation and circuit verification via tree tensor network (TTN) compilation. Based on: arXiv:2605.06579 "Practical Log-Depth Quantum State Preparation and Circuit Verification via Tree Tensor Network Compilation" (Mingare & Coveney, 2026).

## Core Idea

Matrix product states (MPS) provide efficient classical descriptions of quantum states useful as reference states for quantum algorithms (QPE, QSCI). Loading MPS onto quantum computers requires shallow circuits for NISQ hardware viability. This methodology decomposes MPS into **log-depth quantum circuits** via tree tensor network renormalisation.

## Key Contributions

1. **Log-depth MPS compilation**: Decompose MPS to O(log n) depth quantum circuits via TTN renormalisation
2. **Fidelity-depth tradeoff**: Explicit parameter trades small fidelity loss for large circuit depth savings
3. **MPO extension**: Extend decomposition to matrix product operators for overlap circuits
4. **Verifier circuits**: Construct log-depth, ancilla-free circuits for estimating |<phi|U|psi>|^2 with device calibration applications

## Methodology

### Step 1: MPS to TTN Conversion

Convert the MPS into a tree tensor network structure:

1. Parse the MPS tensors A[i] with bond dimension chi
2. Group sites into a binary tree structure (bottom-up)
3. At each tree node, perform SVD to split and truncate:
   - Reshape the combined tensor into a matrix
   - SVD: M = U * S * V^dagger
   - Truncate by keeping top k singular values (controls fidelity-depth tradeoff)
   - U and V^dagger become child node tensors

### Step 2: Circuit Extraction from TTN

Extract quantum gates from each TTN tensor:

1. For each tensor T at a tree node:
   - Reshape T as a unitary matrix U_target
   - Decompose U_target into elementary gates (CNOT + single qubit rotations)
   - Use standard decomposition (e.g., KAK for 2-qubit, Cosine-Sine for larger)
2. Circuit depth per level = O(1) for fixed bond dimension
3. Total depth = O(log n) for n qubits

### Step 3: Fidelity-Depth Tradeoff

Control the truncation parameter k at each SVD step:

```
k = min(chi^2, target_bond_dim)
```

- Larger k -> higher fidelity, deeper circuits
- Smaller k -> lower fidelity, shallower circuits
- For NISQ: prioritize depth (k <= 4-8 typical)

### Step 4: MPO Overlap Circuits

For estimating |<phi|U|psi>|^2:

1. Prepare |psi> via TTN circuit (depth O(log n))
2. Apply unitary U
3. Apply inverse TTN circuit for |phi>
4. Measure in computational basis
5. Probability of |0...0> = |<phi|U|psi>|^2

## Implementation Workflow

### Input to Output

```
MPS tensors (classical) -> TTN decomposition -> Gate sequence -> Quantum circuit
```

### Parameters

| Parameter | Description | Typical Value |
|-----------|-------------|---------------|
| n | Number of qubits | 10-50 (NISQ) |
| chi | MPS bond dimension | 10-100 |
| k | Truncation bond dim | 4-16 |
| depth_target | Max circuit depth | 50-200 |

### Algorithm Pseudocode

```
function compile_mps_to_circuit(MPS_tensors, target_k):
    # Step 1: Build TTN from MPS
    ttn_tree = build_binary_tree(MPS_tensors)
    
    for level in tree_levels(ttn_tree):
        for node in level:
            # SVD truncation
            U, S, V = svd_truncate(node.tensor, k=target_k)
            node.left.tensor = U
            node.right.tensor = V
            node.gate = decompose_unitary(node.tensor)
    
    # Step 2: Extract circuit
    circuit = []
    for level in tree_levels(ttn_tree):
        for node in level:
            circuit.append(node.gate)
    
    return circuit

function verify_overlap(circuit_psi, U, circuit_phi):
    # Ancilla-free overlap verification
    full_circuit = circuit_psi + U + inverse(circuit_phi)
    result = execute(full_circuit, shots=10000)
    overlap = result.probability(all_zeros)
    return overlap
```

## Applications

1. **Quantum Phase Estimation**: Prepare ground state reference
2. **Quantum Chemistry (QSCI)**: Prepare molecular ground states
3. **Circuit Verification**: Calibrate device by comparing expected vs measured overlaps
4. **NISQ State Loading**: Load classically-computed states onto quantum hardware

## Limitations

- Best for states with low entanglement entropy (MPS-efficient)
- Truncation introduces approximation error
- SVD-based decomposition scales as O(chi^3) classically
- Not suitable for highly entangled states (volume-law)

## Activation Keywords

- tree tensor network
- ttn compilation
- mps to circuit
- quantum state preparation
- log-depth circuit
- circuit verification
- overlap estimation
- matrix product state loading
- shallow quantum circuit
- nisq state preparation
- 树张量网络编译
- 量子态制备

## Related Skills

- quantum-circuit-synthesis-gst: Gate set tomography circuit synthesis
- quantum-ml-data-loading: Alternative state loading via amplitude encoding
- fpga-quantum-error-decoder: Hardware error correction for prepared states
