---
name: "generalized-hamiltonian-quantum-feature-maps"
description: "Generalized two-qubit Hamiltonian methodology for Projective Quantum Feature Maps (PQFMs) — unified feature encoding through local Pauli fields and pairwise interactions with statistical benchmarking on NISQ hardware."
---

# Generalized Hamiltonian Quantum Feature Maps

## Description

Methodology for constructing generalized two-qubit Hamiltonian-based Projective Quantum Feature Maps (PQFMs) that provide a unified way to encode classical features through local Pauli fields and pairwise two-qubit Pauli interactions. This construction allows distinct classical variables to be embedded along different Pauli axes of the same qubit, increasing information density of shallow circuits while remaining compatible with hardware constraints. Includes nested cross-validation protocol with paired statistical tests for benchmarking quantum vs classical baselines.

**Source**: arXiv:2606.13641 - "Generalized two-qubit Hamiltonian for Projective Quantum Feature Maps" (2026-06-11)

## Activation Keywords
- generalized PQFM
- projective quantum feature map
- two-qubit Hamiltonian encoding
- quantum feature encoding
- Hamiltonian PQF
- 广义量子特征映射
- 量子特征编码
- pqfmlib
- Hamiltonian-based PQFM

## Tools Used
- terminal: Run quantum circuit simulation, benchmarking scripts
- browser: Access quantum hardware (IBM Quantum, Rigetti)
- file: Create and manage PQFM configuration files, benchmark results

## Core Concepts

### Generalized Two-Qubit Hamiltonian

The key innovation is a unified Hamiltonian that allows embedding different classical variables along different Pauli axes:

```
H(θ, x) = Σ_i f_i(x_i) · σ_i^α + Σ_{i<j} g_ij(x_i, x_j) · σ_i^α ⊗ σ_j^β
```

Where:
- `f_i(x_i)`: Local Pauli field functions for each qubit
- `g_ij(x_i, x_j)`: Pairwise two-qubit interaction functions
- `σ_i^α`: Pauli operators (X, Y, Z) on qubit i along axis α
- `α, β`: Different Pauli axes for different variables (enabling multi-axis encoding)

### Key Advantages over Standard PQFMs

1. **Multi-axis encoding**: Distinct classical variables embedded along different Pauli axes of the same qubit
2. **Increased information density**: More features encoded in shallow circuits
3. **Hardware compatibility**: Respects device topology and gate constraints
4. **Unified framework**: Encompasses Ising-glass and Heisenberg PQFMs as special cases

### Statistical Benchmarking Protocol

Proper evaluation requires:
1. **Nested cross-validation**: Outer loop for performance estimation, inner for hyperparameter tuning
2. **Paired statistical tests**: Wilcoxon signed-rank test or paired t-test across folds
3. **Classical baselines**: Matched classical models with equivalent capacity
4. **Hardware comparison**: Both simulator (statevector) and real quantum processor results

## Usage Patterns

### Pattern 1: Constructing a Generalized PQFM

1. **Define classical feature vector** `x = [x_1, ..., x_d]`
2. **Choose Pauli axis assignment**: Map each feature to a specific Pauli axis (X, Y, Z)
3. **Construct local terms**: `f_i(x_i) = θ_i · x_i · σ_i^{α_i}`
4. **Construct pairwise terms**: `g_ij(x_i, x_j) = θ_ij · x_i · x_j · σ_i^{α_i} ⊗ σ_j^{β_j}`
5. **Exponentiate to get circuit**: `U(x) = exp(-i · H(θ, x) · t)`
6. **Measure observables**: Expectation values of Pauli operators as features

### Pattern 2: Statistical Benchmarking

1. **Define classification/regression task** with dataset D
2. **Set up nested CV**: K outer folds, M inner folds
3. **For each outer fold**:
   a. Train inner hyperparameters
   b. Evaluate on held-out test fold
   c. Record quantum features and classical baseline predictions
4. **Aggregate results**: Mean, std, confidence intervals
5. **Statistical test**: Paired test across folds, report p-value
6. **Compare**: Quantum vs classical, different Hamiltonian families

### Pattern 3: Hardware-Aware PQFM Design

1. **Query device topology**: Get connectivity graph from quantum backend
2. **Design Hamiltonian terms**: Only include interactions between connected qubits
3. **Circuit compilation**: Use hardware-native gate set
4. **Noise mitigation**: Apply readout error mitigation, zero-noise extrapolation
5. **Validation**: Compare hardware results with statevector simulation

## Instructions for Agents

### Step 1: Identify Encoding Strategy
- Analyze the classical feature space (continuous, categorical, mixed)
- Determine optimal Pauli axis mapping for information density
- Consider hardware constraints (connectivity, coherence time)

### Step 2: Implement Hamiltonian PQFM
- Use a library like `pqfmlib` (Python library for Hamiltonian PQFMs)
- Construct the generalized Hamiltonian with local and pairwise terms
- Compile to quantum circuit respecting hardware topology

### Step 3: Generate Quantum Features
- Execute circuits on quantum processor or simulator
- Measure expectation values of chosen observables
- Construct feature matrix from measurement outcomes

### Step 4: Train and Evaluate
- Feed quantum features to classical ML model (SVM, Random Forest, etc.)
- Run nested cross-validation protocol
- Perform paired statistical tests against classical baselines
- Report both quantum and classical results with statistical significance

### Step 5: Analyze Results
- Identify which Hamiltonian terms contribute most to performance
- Analyze hardware noise impact vs simulator baseline
- Determine conditions where quantum features provide advantage

## Error Handling

### Hardware Noise Dominance
- If quantum results significantly worse than simulator: noise is dominant
- Apply error mitigation: readout correction, dynamical decoupling
- Consider shallower circuits or error-aware feature selection

### Barren Plateau in Parameterized Circuits
- If gradient vanishes: use layerwise training, parameter initialization strategies
- Monitor gradient norms during optimization
- Consider fixed-structure Hamiltonians (no parameterized gates)

### Statistical Significance Not Achieved
- Increase number of CV folds or dataset size
- Try different Hamiltonian families (Ising, Heisenberg, generalized)
- Adjust observable selection (single-qubit vs multi-qubit measurements)

## Examples

### Example: Biomedical Classification with Generalized PQFM

Given a biomedical dataset with d features and binary classification:
1. Map features to Pauli axes: continuous → Z-axis, categorical → X-axis
2. Construct Hamiltonian with local Z-fields and X-Z cross terms
3. Execute on 156-qubit IBM quantum processor
4. Generate quantum features from 2-qubit measurement correlations
5. Train SVM classifier with nested CV
6. Perform Wilcoxon signed-rank test vs classical kernel SVM
7. Report: accuracy, AUC, p-value, hardware vs simulation comparison

## Resources

- arXiv:2606.13641 - Original paper
- pqfmlib - Python library for Hamiltonian-based PQFMs (publicly available)
- IBM Quantum Experience - Hardware access for benchmarking
- Qiskit - Circuit compilation and execution

## Related Skills

- quantum-ml-patterns
- quantum-feature-encoding-selection
- quantum-ml-robustness
- quantum-ml-data-loading
