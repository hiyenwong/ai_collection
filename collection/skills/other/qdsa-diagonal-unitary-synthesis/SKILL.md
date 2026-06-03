---
name: qdsa-diagonal-unitary-synthesis
category: quantum
description: Qubitized Diagonal Synthesis Algorithm (QDSA) for efficient diagonal unitary compilation. Uses quantum signal processing (QSP) and qubitization techniques to synthesize diagonal unitaries with logarithmic depth in precision. Achieves optimal gate complexity for quantum simulation of diagonal Hamiltonians and phase oracles.
---

# QDSA: Qubitized Diagonal Unitary Synthesis

## Overview

Diagonal unitaries are ubiquitous in quantum algorithms: phase estimation, Hamiltonian simulation, quantum machine learning, and oracles for Grover search. The challenge is to compile an arbitrary diagonal unitary $D = \text{diag}(e^{i\phi_0}, e^{i\phi_1}, \dots, e^{i\phi_{2^n-1}})$ using a minimal number of quantum gates.

**QDSA** uses qubitization and quantum signal processing to achieve:
- **Gate complexity**: $\mathcal{O}(n + \log(1/\epsilon))$ for $n$-qubit diagonal with precision $\epsilon$
- **Ancilla qubits**: $\mathcal{O}(1)$ — constant overhead
- **Circuit depth**: logarithmic in precision, linear in qubit count

## When to Use

- Compiling phase oracles for Grover's algorithm / amplitude amplification
- Hamiltonian simulation of diagonal terms $e^{-iD t}$
- Quantum machine learning feature maps (diagonal encoding)
- Quantum Fourier transform variants with diagonal pre/post-processing
- Variational quantum algorithms with diagonal ansatz layers

## Key Concepts

### The Diagonal Synthesis Problem

Given a function $f: \{0,1\}^n \to \mathbb{R}$, implement:
$$U_f |x\rangle = e^{if(x)} |x\rangle$$

Naive approach: $2^n$ controlled-phase gates — exponential cost.

### Qubitization Framework

Qubitization embeds the target operation into a larger unitary:

1. **Block encoding**: $U = \begin{pmatrix} H & \cdot \\ \cdot & \cdot \end{pmatrix}$
2. **Signal processing**: Apply polynomial transformation $P(H)$ via QSP
3. **Projection**: Extract desired operation from the block

For diagonal unitaries, the key insight is that $D$ can be block-encoded using a **state preparation** circuit.

### QSP for Diagonal Synthesis

Quantum Signal Processing applies a polynomial $P(x)$ to a Hermitian operator:

$$P(H) = \sum_k c_k T_k(H)$$

where $T_k$ are Chebyshev polynomials. For diagonal $D$:

1. Encode phases as polynomial coefficients
2. Use QSP sequence: $e^{i\phi_0 Z} W e^{i\phi_1 Z} W^\dagger \cdots e^{i\phi_d Z}$
3. Each $W$ is the block encoding; $Z$-rotations are single-qubit

### Complexity Bounds

| Method | Gate Count | Ancilla | Precision |
|--------|-----------|---------|-----------|
| Naive decomposition | $\mathcal{O}(2^n)$ | 0 | Exact |
| Multiplexed rotation | $\mathcal{O}(2^n)$ | 0 | Exact |
| **QDSA (this method)** | $\mathcal{O}(n \cdot \log(1/\epsilon))$ | $\mathcal{O}(1)$ | $\epsilon$ |

## Implementation Steps

### Step 1: Function Encoding

Represent the phase function $f(x)$ as a Fourier series or polynomial:

```python
def encode_phases(f, n_qubits, degree):
    """
    Encode phase function f(x) as polynomial coefficients for QSP.
    
    Args:
        f: function {0,1}^n -> R
        n_qubits: number of qubits
        degree: polynomial degree (controls precision)
    
    Returns:
        QSP phase angles [phi_0, phi_1, ..., phi_d]
    """
    # Sample f on computational basis
    values = [f(x) for x in range(2**n_qubits)]
    
    # Fit Chebyshev polynomial
    coeffs = chebyshev_fit(values, degree)
    
    # Convert to QSP angles
    angles = qsp_angle_synthesis(coeffs)
    
    return angles
```

### Step 2: Block Encoding Construction

```python
def diagonal_block_encoding(f, n_qubits):
    """
    Construct block encoding of diagonal unitary.
    Uses SELECT-ORACLE structure.
    
    Circuit:
    ancilla ──H──●──H──
                 |
    data ────────U_f──
    """
    # SELECT oracle: |0⟩⟨0| ⊗ D + |1⟩⟨1| ⊗ D†
    # This is efficiently implementable for diagonal D
    pass
```

### Step 3: QSP Circuit

```python
def qsp_circuit(angles, block_encoding):
    """
    Construct QSP circuit from phase angles.
    
    Circuit structure:
    ──Rz(phi_0)──W──Rz(phi_1)──W†──Rz(phi_2)──W──...──Rz(phi_d)──
    
    where W is the block encoding and d = len(angles) - 1
    """
    circuit = QuantumCircuit()
    
    for i, phi in enumerate(angles):
        circuit.rz(phi, ancilla_qubit)
        if i < len(angles) - 1:
            if i % 2 == 0:
                circuit.append(block_encoding, all_qubits)
            else:
                circuit.append(block_encoding.inverse(), all_qubits)
    
    return circuit
```

### Step 4: Full QDSA Pipeline

```python
def qdsa_compile(f, n_qubits, epsilon=1e-3):
    """
    Compile diagonal unitary e^{if(x)} using QDSA.
    
    Returns: (quantum_circuit, gate_count, ancilla_count)
    """
    # 1. Determine polynomial degree for target precision
    degree = compute_qsp_degree(epsilon, lipschitz_bound(f))
    
    # 2. Encode phases as QSP angles
    angles = encode_phases(f, n_qubits, degree)
    
    # 3. Construct block encoding
    W = diagonal_block_encoding(f, n_qubits)
    
    # 4. Build QSP circuit
    circuit = qsp_circuit(angles, W)
    
    # 5. Optimize: merge consecutive rotations, cancel inverses
    circuit = optimize_circuit(circuit)
    
    return circuit, circuit.count_ops(), circuit.num_ancillas
```

## Pitfalls

- **Polynomial degree vs. precision**: Degree $d = \mathcal{O}(\log(1/\epsilon))$ — high precision requires more QSP steps
- **Function smoothness**: Non-smooth phase functions require higher polynomial degree; consider smoothing
- **Ancilla measurement**: Some QSP variants require post-selection on ancilla — check success probability
- **Gate decomposition**: Each controlled-$W$ gate may itself require decomposition into native gates
- **Error accumulation**: QSP errors compound multiplicatively across layers; use robust angle synthesis

## Verification

- Check unitary fidelity: $|\langle \psi | U_{\text{target}}^\dagger U_{\text{QDSA}} | \psi \rangle| \geq 1 - \epsilon$
- Verify gate count scales as $\mathcal{O}(n \log(1/\epsilon))$
- Test on simple cases: $f(x) = \alpha x$ (linear phase) should compile exactly with low degree

## References

- Paper ID 625 in kg.db (QDSA diagonal unitary synthesis)
- Quantum Signal Processing (Low, Yoder, Chuang 2016)
- Qubitization (Low, Chuang 2019)
- Diagonal unitary compilation techniques
