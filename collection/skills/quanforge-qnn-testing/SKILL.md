---
name: quanforge-qnn-testing
description: "Mutation testing framework for Quantum Neural Networks (QNNs) based on the QuanForge methodology (arXiv:2604.20706). Use this skill when testing QNN robustness, analyzing quantum circuit vulnerabilities, performing mutation testing on quantum ML models, localizing weak regions in quantum circuits, or comparing QNN test suites. Also triggered by keywords: quantum testing, QNN testing, mutation testing, 量子测试, 量子神经网络测试."
---

# QuanForge: Mutation Testing for Quantum Neural Networks

A comprehensive skill for testing Quantum Neural Networks (QNNs) using mutation testing methodology, based on the QuanForge framework (arXiv:2604.20706).

## When to Use

Activate this skill when the user needs to:

- **Test QNN robustness** — evaluate how well a trained quantum neural network resists circuit-level faults
- **Perform mutation testing on quantum circuits** — systematically inject faults and measure detection rates
- **Compare QNN test suites** — determine which test data better exposes circuit vulnerabilities
- **Localize vulnerable circuit regions** — identify which layers or gates are most prone to failure
- **Assess QNN structural quality** — guide data enhancement and circuit redesign decisions
- **Evaluate noise resilience** — assess mutation killing under simulated noisy quantum conditions

**Activation keywords:** quantum testing, QNN testing, mutation testing, 量子测试, 量子神经网络测试

## Core Concepts

### Mutation Testing for QNNs

Mutation testing is a fault-based testing technique where small, deliberate changes (mutations) are introduced into a program to evaluate test quality. For QNNs, mutations are applied to the quantum circuit after training to simulate potential errors. A mutant is "killed" if the test suite detects a statistically significant behavioral change.

### Statistical Mutation Killing

Unlike classical mutation testing with deterministic outcomes, QNN measurements are inherently probabilistic. QuanForge uses **statistical hypothesis testing** to determine if a mutant is killed:

1. Run both the original QNN and the mutated QNN on the same test input
2. Collect measurement outcome distributions from both
3. Apply a statistical test (e.g., chi-squared, Kolmogorov-Smirnov, or Wasserstein distance) to compare distributions
4. If the distributions differ significantly (p-value < significance level α, typically 0.05), the mutant is **killed**
5. Otherwise, the mutant **survives**

This approach accounts for quantum measurement stochasticity and provides a reliable, repeatable killing criterion.

**Key formula:** The Mutation Score (MS) is calculated as:

```
MS = (Number of killed mutants) / (Total number of mutants) × 100%
```

A higher mutation score indicates a more effective test suite and a more thoroughly validated QNN.

## The 9 Mutation Operators

QuanForge defines nine post-training mutation operators at two levels. These operators simulate realistic errors that may occur during quantum circuit execution.

### Gate-Level Operators (5 operators)

| # | Operator | Description | Effect |
|---|----------|-------------|--------|
| G1 | **Gate Omission** | Remove a randomly selected gate from the circuit | Simulates gate execution failure |
| G2 | **Gate Insertion** | Insert a random gate at a random position | Simulates spurious gate operations |
| G3 | **Gate Replacement** | Replace one gate type with another (e.g., H → I, CNOT → CZ) | Simulates gate misconfiguration |
| G4 | **Gate Duplication** | Duplicate an existing gate (e.g., two consecutive H gates) | Simulates redundant operations |
| G5 | **Gate Reordering** | Swap the positions of two adjacent gates | Simulates timing/ordering errors |

### Parameter-Level Operators (3 operators)

| # | Operator | Description | Effect |
|---|----------|-------------|--------|
| P1 | **Parameter Perturbation** | Add random noise to rotation angles (θ → θ + δ) | Simulates calibration errors |
| P2 | **Parameter Dropout** | Set a parameter to zero or a fixed value | Simulates parameter freeze/failure |
| P3 | **Parameter Scaling** | Multiply a parameter by a random factor | Simulates systematic scaling errors |

### Measurement-Level Operator (1 operator)

| # | Operator | Description | Effect |
|---|----------|-------------|--------|
| M1 | **Measurement Alteration** | Change measurement basis or insert additional measurements | Simulates measurement errors |

## Mutant Generation Algorithm

QuanForge uses a systematic algorithm to generate effective mutants:

```
Algorithm: QuanForge Mutant Generation
Input:  Trained QNN circuit C, operator set O, mutation count N
Output: Set of mutants M

1. M ← ∅
2. For each operator op in O:
3.     For i = 1 to N_per_operator:
4.         C_mutant ← Apply(C, op, parameters)
5.         If C_mutant ≠ C:  # Ensure non-equivalent mutant
6.             M ← M ∪ {C_mutant}
7.         Else:
8.             Retry with different parameters
9. Return M
```

**Guidelines for effective mutant generation:**

- Generate mutants for each operator independently (single-mutant strategy)
- Ensure mutants are **non-equivalent** — the mutation must change circuit behavior
- Use stratified sampling across circuit layers and qubits
- Adjust perturbation magnitude based on the circuit's parameter ranges
- Generate sufficient mutants per operator (typically 10-50) for statistical reliability

## Workflow: QNN Mutation Testing

### Step 1: Prepare the Trained QNN

Ensure the QNN is fully trained and its parameters are fixed. The mutation testing framework operates on the **post-training** circuit.

```python
# Example: Load a trained QNN (PennyLane / Qiskit style)
import pennylane as qml
from pennylane import numpy as np

# Load trained parameters
params = np.load("trained_params.npy")
n_qubits = params.shape[1]
n_layers = params.shape[0]
```

### Step 2: Select Mutation Operators

Choose which operators to apply based on the analysis goals:

- **Comprehensive analysis**: Apply all 9 operators
- **Gate-level focus**: Use G1-G5 to assess circuit topology robustness
- **Parameter-level focus**: Use P1-P3 to assess parameter sensitivity
- **Hardware-aware**: Prioritize operators that map to realistic hardware errors

### Step 3: Generate Mutants

Apply each operator to produce mutants. Track which operator generated each mutant for later analysis.

```python
def apply_gate_omission(circuit, gate_index):
    """G1: Remove gate at specified index."""
    mutated = circuit.copy()
    mutated.remove_gate(gate_index)
    return mutated

def apply_parameter_perturbation(params, param_index, delta):
    """P1: Add noise to a parameter."""
    perturbed = params.copy()
    perturbed[param_index] += delta
    return perturbed

def apply_gate_replacement(circuit, gate_index, new_gate):
    """G3: Replace gate type (e.g., Hadamard → Identity)."""
    mutated = circuit.copy()
    mutated.replace_gate(gate_index, new_gate)
    return mutated
```

### Step 4: Execute Tests on Original and Mutants

Run both the original QNN and each mutant on the test suite, collecting output distributions.

```python
def run_qnn_test(circuit, params, test_data, n_shots=1024):
    """Run QNN on test data and collect measurement distributions."""
    results = []
    for sample in test_data:
        # Execute circuit with n_shots
        outcome = execute_circuit(circuit, params, sample, shots=n_shots)
        results.append(outcome)
    return results

# Test original
original_results = run_qnn_test(original_circuit, original_params, test_data)

# Test each mutant
for mutant in mutants:
    mutant_results = run_qnn_test(mutant.circuit, mutant.params, test_data)
```

### Step 5: Statistical Mutation Killing

Apply statistical tests to determine if each mutant is killed.

```python
from scipy import stats

def is_mutant_killed(original_dist, mutant_dist, alpha=0.05):
    """Determine if mutant is killed using statistical test.
    
    Uses chi-squared test for categorical distributions.
    Returns (killed: bool, p_value: float, test_statistic: float)
    """
    # Ensure distributions have same bins
    stat, p_value = stats.chisquare(mutant_dist, f_exp=original_dist)
    killed = p_value < alpha
    return killed, p_value, stat

# Evaluate all mutants
killed_count = 0
results_by_operator = {}

for mutant in mutants:
    killed, p_val, stat = is_mutant_killed(
        original_results, mutant_results[mutant.id]
    )
    if killed:
        killed_count += 1
    
    op_type = mutant.operator_type
    if op_type not in results_by_operator:
        results_by_operator[op_type] = {"killed": 0, "total": 0}
    results_by_operator[op_type]["total"] += 1
    if killed:
        results_by_operator[op_type]["killed"] += 1
```

### Step 6: Analyze Results

Calculate mutation scores and analyze operator-level performance.

```python
# Overall mutation score
mutation_score = killed_count / len(mutants) * 100

# Per-operator analysis
for op, data in results_by_operator.items():
    op_score = data["killed"] / data["total"] * 100
    print(f"{op}: {op_score:.1f}% killing rate ({data['killed']}/{data['total']})")

# Layer-level vulnerability analysis
layer_vulnerability = {}
for mutant in mutants:
    if not mutant.killed:
        layer = mutant.target_layer
        layer_vulnerability[layer] = layer_vulnerability.get(layer, 0) + 1

print("Most vulnerable layers (most surviving mutants):")
for layer, count in sorted(layer_vulnerability.items(), key=lambda x: -x[1]):
    print(f"  Layer {layer}: {count} surviving mutants")
```

## Key Patterns and Techniques

### Pattern 1: Gate Replacement Strategies

When replacing gates, use semantically meaningful substitutions:

- **Hadamard → Identity** (H → I): Removes superposition capability
- **CNOT → CZ**: Changes entanglement mechanism
- **RX → RZ**: Changes rotation axis
- **Pauli-X → Pauli-Z**: Flips bit-flip to phase-flip
- **Toffoli → CNOT**: Reduces multi-qubit gate complexity

### Pattern 2: Parameter Perturbation Magnitudes

Choose perturbation δ based on the context:

- **Small perturbations** (δ ≈ 0.01-0.1): Simulate calibration noise
- **Medium perturbations** (δ ≈ 0.1-0.5): Simulate drift errors
- **Large perturbations** (δ ≈ 0.5-π): Simulate gross misconfiguration

### Pattern 3: Multi-Shot Strategy

Use sufficient shots (n_shots ≥ 1024) for reliable statistical killing:

- Fewer shots → higher variance → more false negatives (surviving mutants)
- More shots → better statistical power → more accurate killing
- Balance shots vs. computational cost based on available resources

### Pattern 4: Layer-by-Layer Vulnerability Mapping

To localize circuit weaknesses:

1. Group mutants by which layer they target
2. Calculate per-layer killing rates
3. Layers with low killing rates are more robust (or tests are insufficient)
4. Layers with high killing rates indicate structural vulnerability

### Pattern 5: Test Suite Comparison

To compare two test suites A and B:

1. Generate the same mutant set for both
2. Calculate MS_A and MS_B separately
3. Higher mutation score indicates a more effective test suite
4. Use per-operator breakdown to identify what each suite catches

## Interpreting Results

### Mutation Score Benchmarks

| Mutation Score | Interpretation |
|----------------|----------------|
| < 30% | Test suite is weak; many mutants survive undetected |
| 30-60% | Moderate test coverage; room for improvement |
| 60-80% | Good test coverage; most faults are detected |
| > 80% | Strong test coverage; consider harder mutants or tougher operators |

### Operator Effectiveness

- **High killing rate operators** simulate errors easily detected by current tests
- **Low killing rate operators** indicate blind spots in the test suite
- Operators with 0% killing rate may be equivalent mutants or indicate the test data lacks sensitivity to that error type

### Surviving Mutants Analysis

Surviving mutants reveal:
- **Redundant circuit regions** where errors don't affect outputs
- **Insufficient test data** that doesn't exercise certain circuit behaviors
- **Over-parameterized circuits** where parameter changes are absorbed

## Noisy Simulation Mode

To assess practical feasibility on real quantum hardware:

1. Add a noise model (depolarizing, amplitude damping, readout error)
2. Re-run mutation testing under noise
3. Compare mutation scores with and without noise
4. Noise typically reduces mutation scores by masking mutation effects
5. A large drop indicates the QNN is sensitive to hardware noise

## Common Pitfalls

1. **Equivalent mutants**: Some mutations produce functionally identical circuits. Always verify non-equivalence.
2. **Insufficient shots**: Too few measurement shots lead to unreliable statistical killing.
3. **Single-operator bias**: Relying on one operator type gives incomplete coverage. Use all 9.
4. **Ignoring circuit topology**: Mutations should cover all layers and qubits, not just one region.
5. **Over-interpreting low scores**: A low mutation score may indicate a robust circuit, not necessarily a bad test suite.

## References

- **Paper**: "QuanForge: A Mutation Testing Framework for Quantum Neural Networks" (arXiv:2604.20706)
- **Core techniques**: Statistical hypothesis testing, mutation analysis, quantum circuit simulation
- **Recommended frameworks**: PennyLane, Qiskit, Cirq for circuit manipulation and execution
