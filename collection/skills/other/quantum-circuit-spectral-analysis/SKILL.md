---
name: quantum-circuit-spectral-analysis
description: "Spectral analysis of quantum circuits using Circuit Harmonic Matrices. Predict quantum machine learning model performance from circuit architecture without training. Analyze circuit expressivity, trainability, and generalization capacity via frequency-domain methods. Activation: quantum circuit spectral, circuit harmonic matrix, quantum circuit analysis, QML spectral, quantum model expressivity, circuit eigenvalue, quantum neural network spectrum."
---

# Quantum Circuit Spectral Analysis

Predict quantum machine learning performance from circuit architecture using spectral methods.

## Core Concept: Circuit Harmonic Matrices

Convert quantum circuits to harmonic matrices for spectral analysis. Circuit frequency spectrum reveals:
- **Expressivity**: How many functions can the circuit represent?
- **Trainability**: Will gradients vanish/explode?
- **Generalization**: Can the model generalize beyond training data?

**Key insight**: Circuit frequency spectrum correlates with QML performance.

## Method Overview

### Step 1: Construct Harmonic Matrix

From parametrized quantum circuit, build harmonic matrix H:
```python
# Circuit → harmonic matrix
H = construct_harmonic_matrix(circuit, parameters)
```

The matrix encodes circuit's frequency response across parameter space.

### Step 2: Compute Spectrum

Find eigenvalues and eigenvectors of H:
```python
eigenvalues, eigenvectors = np.linalg.eig(H)
```

Spectrum properties determine QML characteristics.

### Step 3: Interpret Spectrum

| Spectrum Property | QML Implication |
|-------------------|-----------------|
| Eigenvalue spread | Expressivity range |
| Eigenvalue density | Trainability (gradient landscape) |
| Low-frequency dominance | Good generalization |
| High-frequency dominance | Risk of overfitting |

## Key Findings from arXiv:2604.04292

**Circuit Harmonic Matrices: A Spectral Framework for Quantum Machine Learning**

Main results:
1. Low-frequency circuits generalize better
2. Too many frequencies → barren plateaus
3. Spectrum predicts optimal circuit depth
4. Encoding strategy affects frequency distribution

## Workflow for QML Model Selection

### 1. Analyze Circuit Candidates

Before training, compare circuit architectures:
```python
circuits = [
    "hardware-efficient ansatz",
    "QAOA-style",
    "tensor-network",
    "variational quantum eigensolver"
]

for circuit in circuits:
    spectrum = compute_spectrum(circuit)
    expressivity = measure_eigenvalue_spread(spectrum)
    trainability = check_barren_plateau_risk(spectrum)
    generalization = assess_frequency_distribution(spectrum)
    
    # Choose best candidate
```

### 2. Tune Circuit Parameters

Use spectrum to guide design:
- **Reduce depth** if spectrum shows too many frequencies
- **Change encoding** if low-frequency modes insufficient
- **Add structure** if spectrum lacks diversity

### 3. Validate Spectral Predictions

After training, verify predictions:
- Did low-frequency circuits generalize?
- Did high-frequency diversity increase expressivity?
- Did spectral warnings prevent barren plateaus?

## Spectral Metrics

### Expressivity Measure

Eigenvalue variance → expressivity:
```python
expressivity = np.var(eigenvalues)
# High variance → many representable functions
```

### Trainability Measure

Check gradient concentration:
```python
# Barren plateau risk: spectrum too flat
trainability = 1.0 / (np.std(eigenvalues) + epsilon)
# Low std → gradient vanishing risk
```

### Generalization Measure

Frequency concentration:
```python
low_freq_power = np.sum(eigenvalues[:k]**2) / np.sum(eigenvalues**2)
# High low-frequency power → good generalization
```

## Application Examples

### Example 1: VQE Circuit Selection

For molecular energy estimation:
1. Generate circuit candidates (different depths, encodings)
2. Compute spectra for all candidates
3. Select circuit with:
   - Enough expressivity (variance > threshold)
   - Good trainability (no barren plateau signature)
   - Low-frequency dominance (generalization)
4. Train selected circuit

### Example 2: Quantum Classifier

For binary classification:
1. Build encoding + variational circuit
2. Analyze spectrum
3. Adjust encoding if spectrum too high-frequency
4. Predict classification accuracy from spectrum

### Example 3: Quantum GAN Generator

For quantum generative model:
1. Construct generator circuit
2. Check spectrum for expressivity (need variance)
3. Ensure trainability (no flat spectrum)
4. Compare spectral predictions with actual generation quality

## Best Practices

1. **Before training**: Always analyze spectrum first (saves computation)
2. **Compare architectures**: Spectrum reveals best circuit design
3. **Tune encoding**: Encoding strategy strongly affects spectrum
4. **Depth vs spectrum**: More depth ≠ better spectrum
5. **Domain-specific**: Different tasks need different spectral signatures

## Common Pitfalls

- **Too many frequencies**: Overfitting risk, barren plateaus
- **Too few frequencies**: Limited expressivity, can't represent target
- **Wrong encoding**: Encoding dominates spectrum, not variational part
- **Ignoring structure**: Unstructured circuits have bad spectra

## Key Papers

- arXiv:2604.04292 - Circuit Harmonic Matrices (foundation)
- McClean et al. (2018) - Barren plateaus in QML
- Holmes et al. (2022) - Circuit expressibility measures
- Sim et al. (2021) - Expressibility vs entangling capability

## Tools

### Python Libraries

- **Qiskit**: Circuit construction and simulation
- **PennyLane**: Quantum machine learning framework
- **Cirq**: Google's quantum library
- **NumPy/SciPy**: Spectral analysis

### Analysis Scripts

- `scripts/spectrum_analyzer.py`: Compute circuit spectrum
- `scripts/expressivity_measure.py`: Quantify expressivity
- `scripts/barren_plateau_check.py`: Detect training risk

## Activation Triggers

Use this skill when:
- Choosing quantum circuit architecture for QML
- Predicting quantum model performance before training
- Analyzing why quantum model fails to train
- Optimizing quantum circuit depth and encoding
- User mentions "circuit spectrum", "harmonic matrix", "QML spectral"

## Example Usage

**User**: "My quantum classifier is not training well. How can I analyze the circuit?"

**Agent**:
1. Explain spectral analysis approach
2. Show how to compute circuit harmonic matrix
3. Interpret spectrum for expressivity/trainability
4. Diagnose issue from spectrum (e.g., barren plateau)
5. Recommend circuit modifications based on spectrum

## Related Skills

- **quantum-machine-learning**: General QML methods
- **physics-guided-neural-networks**: Physics-constrained learning
- **variational-quantum-algorithms**: VQE, QAOA specifics