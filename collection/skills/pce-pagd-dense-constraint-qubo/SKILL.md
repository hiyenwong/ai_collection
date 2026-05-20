---
name: pce-pagd-dense-constraint-qubo
description: >
  Pauli Correlation Encoding with Problem-Aware Guided Decoding (PCE+PAGD) for
  dense-constraint QUBO problems in biomedical applications. Extends PCE
  methodology with PAGD decoder that scores candidates by combining marginal QUBO
  energy reduction with trained expectation-value priors and constraint-aware
  feasibility pruning. Achieves 75-100% near-optimal recovery on mRNA secondary
  structure prediction (50-240 variables, 7-14 qubits). Demonstrated on IBM Heron
  at biologically relevant scale (694-745 variables, 23 qubits, 480 two-qubit
  gates). Use when: (1) solving dense-constraint QUBO problems with quantum
  encoding, (2) biomedical structure prediction on quantum hardware, (3)
  scaling QUBO beyond qubit limits with correlation encoding, (4) decoding
  continuous expectation values into feasible binary solutions.
---

# PCE+PAGD: Dense-Constraint QUBO Encoding and Decoding

## Core Idea

Pauli Correlation Encoding (PCE) compresses m binary variables onto n=O(m^{1/k})
qubits by mapping them to commuting Pauli correlators. However, its continuous
expectation values must be decoded into feasible binary solutions - a critical
challenge for dense-constraint problems.

The Problem-Aware Guided Decoder (PAGD) solves this by scoring candidate variable
commitments through three signals:
1. **Marginal QUBO energy reduction** - how much each assignment improves energy
2. **Trained expectation-value prior** - learned distribution over good assignments
3. **Constraint-aware feasibility pruning** - eliminate assignments violating hard constraints

This combination achieves 75-100% near-optimal recovery (gap < 1%) on mRNA
secondary-structure prediction benchmarks, compared to 0-30% for sign-rounding
plus local-search baselines.

## Algorithm Steps

### Step 1: Formulate QUBO Problem

For mRNA secondary structure prediction:

```python
import numpy as np

# mRNA sequence of length L, base-pairing rules
# Variables x_{i,j} = 1 if bases i,j form a pair (0 otherwise)
# Constraints:
#   - Each base pairs with at most one other base
#   - Minimum loop size (typically 3 bases)
#   - No pseudoknots (for simpler models)

def build_mrna_qubo(sequence, energy_params):
    """Build QUBO for RNA secondary structure prediction."""
    L = len(sequence)
    # Valid pairs: Watson-Crick + wobble
    valid_pairs = []
    for i in range(L):
        for j in range(i + 4, L):  # min loop size 3
            if is_valid_pair(sequence[i], sequence[j]):
                valid_pairs.append((i, j))

    n_vars = len(valid_pairs)

    # Q: QUBO matrix where Q[i,j] is the energy of pairing i,j
    Q = np.zeros((n_vars, n_vars))
    for idx, (i, j) in enumerate(valid_pairs):
        Q[idx, idx] = energy_params.get_pair_energy(sequence[i], sequence[j])

    # Penalty for constraint violations (each base pairs at most once)
    penalty = 100.0  # Large enough to enforce constraints
    for idx1, (i1, j1) in enumerate(valid_pairs):
        for idx2, (i2, j2) in enumerate(valid_pairs):
            if idx1 != idx2 and (i1 == i2 or i1 == j2 or j1 == i2 or j1 == j2):
                Q[idx1, idx2] += penalty
                Q[idx2, idx1] += penalty

    return Q, valid_pairs
```

### Step 2: Pauli Correlation Encoding

Map n_vars binary variables onto n_qubits qubits:

```python
from qiskit.quantum_info import SparsePauliOp

def pce_encode(Q, n_qubits, k=2):
    """
    Encode QUBO matrix Q using Pauli Correlation Encoding.
    Maps m variables to n qubits via commuting Pauli correlators.

    n = O(m^(1/k)) qubits encode m variables

    Each variable x_i is mapped to a Pauli string:
    x_i -> (I - P_i) / 2  where P_i is a product of Z operators
    """
    n_vars = Q.shape[0]

    # Generate Pauli strings for each variable
    # Use k-local Pauli operators (products of up to k Z operators)
    pauli_assignments = generate_pauli_assignments(n_vars, n_qubits, k)

    # Build Hamiltonian: H = sum_i sum_j Q[i,j] * x_i * x_j
    # where x_i = (I - P_i) / 2
    terms = []
    coeffs = []

    for i in range(n_vars):
        for j in range(i, n_vars):
            if Q[i, j] != 0:
                # x_i * x_j -> (I - P_i)(I - P_j) / 4
                pauli_product = pauli_assignments[i] * pauli_assignments[j]
                terms.append(str(pauli_product))
                coeffs.append(Q[i, j] / 4)

    hamiltonian = SparsePauliOp.from_list(list(zip(terms, coeffs)))
    return hamiltonian, pauli_assignments
```

### Step 3: Quantum Circuit Execution

```python
from qiskit import transpile
from qiskit.circuit.library import TwoLocal, RealAmplitudes

def run_quantum_circuit(hamiltonian, n_qubits, backend, n_layers=3, n_shots=8192):
    """Execute quantum circuit and collect expectation values."""
    ansatz = RealAmplitudes(n_qubits, reps=n_layers)
    circuit = ansatz.bind_parameters(optimal_params)

    # Transpile for target backend
    transpiled = transpile(circuit, backend=backend)

    # Execute and measure
    from qiskit.primitives import Estimator
    estimator = Estimator()
    result = estimator.run(transpiled, hamiltonian, [optimal_params]).result()

    # Collect expectation values for all Pauli observables
    expectation_values = measure_all_paulis(transpiled, backend, n_shots)
    return expectation_values
```

### Step 4: Problem-Aware Guided Decoder (PAGD)

The key innovation - decoding continuous expectation values into feasible binary solutions:

```python
import torch
import torch.nn as nn

class PAGDDecoder:
    """
    Problem-Aware Guided Decoder for dense-constraint QUBO problems.

    Scores candidate variable commitments by combining:
    1. Marginal QUBO energy reduction
    2. Trained expectation-value prior
    3. Constraint-aware feasibility pruning
    """

    def __init__(self, Q, constraints, valid_pairs):
        self.Q = Q  # QUBO matrix
        self.constraints = constraints  # Hard constraints
        self.valid_pairs = valid_pairs
        self.n_vars = Q.shape[0]
        self.prior_network = self._build_prior_network()

    def _build_prior_network(self):
        """Trainable prior over expectation values."""
        return nn.Sequential(
            nn.Linear(self.n_vars, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, self.n_vars),
            nn.Sigmoid()  # Output probabilities in [0,1]
        )

    def train_prior(self, expectation_values, labels, epochs=100):
        """Train prior network on labeled QUBO solutions."""
        optimizer = torch.optim.Adam(self.prior_network.parameters(), lr=1e-3)
        criterion = nn.BCELoss()

        for epoch in range(epochs):
            optimizer.zero_grad()
            predictions = self.prior_network(expectation_values)
            loss = criterion(predictions, labels)
            loss.backward()
            optimizer.step()

    def decode(self, expectation_values, n_restarts=100):
        """
        Decode expectation values into feasible binary solution.

        Uses multiple restarts with guided selection:
        1. Score each variable by marginal energy reduction
        2. Apply trained prior for bias toward good assignments
        3. Prune assignments violating constraints
        """
        best_solution = None
        best_energy = float('inf')

        for restart in range(n_restarts):
            # Score: energy reduction + prior probability
            energy_scores = self._compute_marginal_energy(expectation_values)
            prior_scores = self.prior_network(expectation_values).detach().numpy()

            # Combined score
            combined = 0.6 * energy_scores + 0.4 * prior_scores

            # Greedy assignment with constraint checking
            solution = np.zeros(self.n_vars, dtype=int)
            available = set(range(self.n_vars))

            while available:
                # Pick highest-scored available variable
                idx = max(available, key=lambda i: combined[i])
                solution[idx] = 1
                available.remove(idx)

                # Prune: remove variables that conflict with this assignment
                to_remove = set()
                for j in available:
                    if self._conflicts(idx, j):
                        to_remove.add(j)
                available -= to_remove

            energy = solution @ self.Q @ solution
            if energy < best_energy:
                best_energy = energy
                best_solution = solution.copy()

        return best_solution, best_energy

    def _compute_marginal_energy(self, expectation_values):
        """Compute marginal energy reduction for each variable."""
        marginal = np.zeros(self.n_vars)
        for i in range(self.n_vars):
            # Energy if x_i = 1 minus energy if x_i = 0
            marginal[i] = self.Q[i, i] + 2 * np.dot(self.Q[i, :], expectation_values)
        return -marginal  # Negate because we want energy reduction

    def _conflicts(self, i, j):
        """Check if assigning both variables i and j violates constraints."""
        pair_i = self.valid_pairs[i]
        pair_j = self.valid_pairs[j]
        # Conflict if they share a base
        return len(set(pair_i) & set(pair_j)) > 0
```

### Step 5: Training with QUBO-Space Sigmoid Loss

```python
def qubo_sigmoid_loss(solution, Q, temperature=1.0):
    """
    QUBO-space sigmoid loss that preserves the QUBO penalty structure.

    Unlike standard BCE loss, this loss directly optimizes the QUBO objective
    while maintaining differentiability for gradient-based training.
    """
    energy = solution @ Q @ solution
    # Sigmoid maps energy to [0,1], lower energy = higher probability
    return -torch.sigmoid(-energy / temperature).mean()
```

### Step 6: Hardware Deployment

```python
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler, Estimator

def deploy_to_heron(hamiltonian, pagd_decoder, n_qubits=23):
    """
    Deploy to IBM Heron processor.

    Key metrics from the paper:
    - 480 native two-qubit gates at depth 256
    - SWAP-free transpilation
    - PAGD decoded gaps on QPU match or beat simulator means
    - Exact CPLEX-optimum recovery achieved
    """
    service = QiskitRuntimeService()
    backend = service.backend('ibm_sherbrooke')  # Heron-class device

    # Transpile with SWAP-free mapping
    transpiled = transpile(hamiltonian.to_instruction(), backend=backend,
                          optimization_level=3)

    # Execute on QPU
    estimator = Estimator(backend=backend)
    result = estimator.run(transpiled, hamiltonian).result()

    # Decode QPU results with PAGD
    solution, energy = pagd_decoder.decode(result.values)
    return solution, energy
```

## Key Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| n_qubits | O(m^(1/k)) | Number of qubits for m variables |
| k | 2 | PCE compression factor |
| n_restarts | 100 | PAGD decoder restarts |
| n_layers | 3 | Ansatz circuit depth |
| penalty | 100.0 | Constraint violation penalty in QUBO |
| temperature | 1.0 | QUBO sigmoid loss temperature |
| n_shots | 8192 | Measurement shots per circuit |

## Performance Benchmarks

| Metric | PAGD | Sign-Rounding + LS |
|--------|------|-------------------|
| Near-optimal recovery (gap < 1%) | 75-100% | 0-30% |
| Variables tested | 50-240 | 50-240 |
| Qubits used | 7-14 | 7-14 |
| Hardware scale | 694-745 vars, 23 qubits | N/A |
| Two-qubit gates | 480 | N/A |
| Circuit depth | 256 | N/A |

## Scalability Analysis

- **Qubit compression**: O(m^(1/k)) qubits for m variables
- **mRNA sequences**: 30-60 nt → 50-240 variables → 7-14 qubits
- **Large scale**: 102-105 nt → 694-745 variables → 23 qubits
- **Gate count**: 480 two-qubit gates, depth 256 (SWAP-free)

## When to Use PCE+PAGD vs Alternatives

| Method | Max Variables | Hardware | Decoding Quality |
|--------|--------------|----------|-----------------|
| Direct encoding | ~n_qubits | Gate-based | Exact |
| **PCE+PAGD (this)** | **O(n_qubits^k)** | **Gate-based** | **75-100% near-optimal** |
| Quantum annealing | ~5000 | D-Wave | Problem-dependent |
| Classical (CPLEX) | Unlimited | CPU | Exact |
| Sign-rounding + LS | ~n_qubits | Gate-based | 0-30% near-optimal |

Use PCE+PAGD when:
- Dense-constraint QUBO problems with more variables than qubits
- Need high-quality decoding of quantum expectation values
- Biomedical/molecular structure prediction on quantum hardware
- Scaling beyond direct encoding limits on NISQ devices

## Activation Keywords

- pce pagd, pauli correlation decoding, dense constraint qubo, mRNA quantum
  prediction, problem-aware guided decoder, qubo decoding quantum, quantum
  rna structure, expectation value decoding, qubo sigmoid loss, ibm heron
  quantum bio, scalable qubit encoding, quantum structure prediction

## Related Skills

- `pauli-correlation-portfolio-optimization`: PCE for financial portfolio optimization
- `pauli-detecting-quantum-codes`: Pauli group variance for quantum error detection
- `distributed-quantum-error-correction`: Distributed QEC patterns
- `quantum-medical-diagnosis`: Quantum computing for medical diagnosis

## References

- Friedhoff, Metkar, Davis, Kumar, Galda. "Pauli Correlation Encoding for mRNA
  Secondary Structure Prediction: Problem-Aware Decoding for Dense-Constraint QUBOs"
  arXiv:2605.20163 (2026)

## Notes

- The PAGD decoder is the key differentiator from the original PCE portfolio skill
- Trained priors survive deployment to noisy superconducting hardware
- CPLEX-optimum recovery achieved on at least one sequence on real QPU
- The QUBO-space sigmoid loss preserves penalty structure unlike standard BCE
