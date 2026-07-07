---
name: ml-qem-variational-algorithms
description: "Machine Learning-based Quantum Error Mitigation (ML-QEM) for variational quantum algorithms. Uses near-Clifford circuit simulation for training data, transfers across Hamiltonians, outperforms ZNE in high-noise regimes. Applicable to NISQ processors. arXiv:2606.02697."
metadata:
  arxiv_id: "2606.02697"
  category: "quant-ph"
  authors: ["Nikita Korolev", "Kirill Lakhmanskiy", "Daniil Rabinovich"]
  published: "2026-06-01"
---

## Machine Learning-based Quantum Error Mitigation for Variational Algorithms

**arXiv: 2606.02697** (June 2026)

### Problem

Existing ML-QEM methods have restricted applicability to variational circuits and rely on inaccessible noiseless training data. This limits their practical use on NISQ processors where noiseless data is unavailable.

### Solution

**Clifford-based Training Protocol**:
1. Generate training data by simulating (near-)Clifford circuits — efficiently classically simulable
2. Use this data for model selection and training
3. Produce a mitigation model that corrects variational circuits with arbitrary parameters
4. Model transfers across different target Hamiltonians of similar structure

### Key Results

- **Benchmarked on**: VQE for Sherrington-Kirkpatrick Hamiltonian (up to n qubits)
- **Noise models**: Various tested (depolarizing, coherent, etc.)
- **Performance**: Consistent several-fold error suppression across all settings
- **vs ZNE**: Superior performance in high-noise regime
- **NISQ applicability**: Demonstrated suitability for present-day processors

### Reusable Patterns

#### Pattern 1: Clifford Surrogate Training
Use classically simulable Clifford circuits as training data surrogates for error mitigation models:
- Clifford circuits → efficient classical simulation → abundant noiseless training data
- Trained model → applies to arbitrary variational circuits (non-Clifford)
- Key insight: error structure learned from Clifford generalizes to non-Clifford

#### Pattern 2: Cross-Hamiltonian Transfer
Once trained, the mitigation model transfers across different Hamiltonians of similar structure:
- Train on Hamiltonian A → mitigate on Hamiltonian B
- Reduces per-problem training overhead
- Enables reuse of mitigation infrastructure across experiments

#### Pattern 3: NISQ-Ready QEM Protocol
Complete pipeline for practical error mitigation:
1. Identify target variational circuit family
2. Find structurally similar Clifford circuits
3. Simulate Clifford circuits (noiseless + noisy) for training pairs
4. Train ML model on (noisy → noiseless) mapping
5. Apply model to target variational circuits
6. Verify transfer across Hamiltonian variants

### Activation
quantum error mitigation, ML-QEM, variational algorithms, VQE, NISQ, Clifford simulation, error suppression, zero-noise extrapolation, machine learning quantum

### Related Skills
- `circuit-balancing-error-mitigation` - Circuit balancing for error mitigation
- `quantum-ml-patterns` - Reusable QML research patterns
- `qml-empirical-benchmarking` - Empirical QML benchmarking methodology
