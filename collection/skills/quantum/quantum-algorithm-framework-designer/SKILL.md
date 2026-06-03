---
name: quantum-algorithm-framework-designer
description: "Design and implement quantum algorithm frameworks for specific problem domains. Structure quantum circuits, define hybrid classical-quantum pipelines, and create reusable quantum algorithm templates. Use when: (1) Designing new quantum algorithms for optimization or simulation, (2) Creating framework scaffolding for QAOA/VQE/QMC applications, (3) Structuring hybrid quantum-classical pipelines, (4) Implementing quantum subroutines for specific problem types."
---

# Quantum Algorithm Framework Designer

Design and implement quantum algorithm frameworks for specific problem domains.

## Activation Keywords

- quantum algorithm framework
- quantum circuit design
- QAOA framework
- VQE framework
- quantum algorithm implementation
- hybrid quantum pipeline
- quantum subroutine design
- 量子算法框架
- 量子电路设计

## Tools Used

- `exec`: Run Qiskit/PennyLane quantum circuit scripts
- `read`: Load problem specifications and quantum library docs
- `write`: Generate quantum algorithm framework code and documentation

## Core Framework Patterns

### Pattern 1: QAOA Framework

```python
def qaoa_framework(problem_hamiltonian, n_layers=3):
    """
    QAOA framework structure:
    1. Problem encoding: H_problem = QUBO/Ising
    2. Mixer Hamiltonian: H_mixer = Σ X_i
    3. Circuit: alternating problem/mixer unitaries
    4. Optimization: minimize <ψ|H_problem|ψ>
    """
    circuit = QuantumCircuit(n_qubits)
    # Initial state: equal superposition
    circuit.h(range(n_qubits))
    # QAOA layers
    for _ in range(n_layers):
        apply_problem_unitary(circuit, gamma)
        apply_mixer_unitary(circuit, beta)
    return circuit
```

### Pattern 2: VQE Framework

```python
def vqe_framework(hamiltonian, ansatz_type="hardware_efficient"):
    """
    VQE framework structure:
    1. Ansatz: parameterized quantum circuit
    2. Measurement: expectation value of H
    3. Classical optimization: minimize energy
    """
    ansatz = create_ansatz(ansatz_type, n_qubits, n_layers)
    optimizer = SPSA(maxiter=300)
    vqe = VQE(ansatz, optimizer, quantum_instance)
    return vqe.compute_minimum_eigenvalue(hamiltonian)
```

### Pattern 3: Hybrid Classical-Quantum Pipeline

```
Input Data → Classical Preprocessing → Quantum Encoding
→ Quantum Circuit Execution → Measurement → Classical Postprocessing → Output
```

## Instructions for Agents

### Step 1: Identify Problem Type
Classify the target problem: combinatorial optimization (→ QAOA), eigenvalue problem (→ VQE), sampling (→ QMC), or simulation.

### Step 2: Select Algorithm Framework
Choose appropriate framework and determine: qubit requirements, circuit depth, classical optimizer, error mitigation needs.

### Step 3: Design Circuit Architecture
Define: encoding layer, variational/problem layers, measurement operators, and entanglement structure.

### Step 4: Implement Framework
Generate Python code using Qiskit/PennyLane; include parameter initialization, circuit construction, and optimization loop.

### Step 5: Validate Framework
Test on small instances with known solutions; benchmark vs classical baselines; report resource requirements.

## Examples

### Example 1: QAOA for Graph Coloring

```
User: "Design a QAOA framework for graph 3-coloring"

Agent:
1. Encode 3-coloring as QUBO: penalty for same-color adjacent nodes
2. Define QAOA circuit: problem unitary from QUBO, mixer from X gates
3. Implement 3-layer QAOA with COBYLA optimizer
4. Test on 5-node graph; report approximation ratio
```

### Example 2: VQE Molecular Simulation

```
User: "Create a VQE framework for H2 molecule ground state energy"

Agent:
1. Map H2 Hamiltonian to Pauli operators (Jordan-Wigner)
2. Design hardware-efficient ansatz (4 qubits, 2 layers)
3. Set up SPSA optimizer with 300 iterations
4. Run VQE and report ground state energy vs FCI reference
```

## Resources

- `references/`: Quantum algorithm implementation guides
- Related: `quantum-portfolio-optimizer`, `quantum-neural-hybrid`
