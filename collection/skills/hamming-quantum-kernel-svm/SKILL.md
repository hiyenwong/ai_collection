---
name: hamming-quantum-kernel-svm
description: "Hamming quantum kernel for SVMs that avoids exponential concentration problem of fidelity quantum kernel. Uses full measurement statistics rather than single fidelity value. Outperforms fidelity kernel at 15+ qubits and classical Gaussian kernel on synthetic quantum data. Scales to 27 qubits without additional quantum resources. Activation: hamming quantum kernel, quantum SVM, exponential concentration, quantum kernel scalability, fidelity kernel alternative, scalable quantum kernel"
metadata:
  arxiv_id: "2605.31449"
  published: "2026-05-29"
  authors: "Anant Agnihotri, Michael Krebsbach, Florentin Reiter, Thomas Wellens"
  tags: [quantum, svm, kernel-methods, scalability, qml, classification]
---

## Core Problem: Exponential Concentration in Fidelity Quantum Kernels

The fidelity quantum kernel $K(x, x') = |\langle \psi(x) | \psi(x') \rangle|^2$ suffers from **exponential concentration** as system size increases:
- Kernel values concentrate to a constant as $n_q$ grows
- Prevents efficient scaling beyond few-qubit systems
- Makes quantum SVM useless for large-scale problems

## Hamming Quantum Kernel Solution

Instead of using a single fidelity value, the Hamming quantum kernel uses the **full measurement statistics**:

$$K_H(x, x') = \text{Hamming similarity of measurement outcome distributions}$$

Key properties:
- **Classical post-processing only**: No additional quantum resources needed
- **Same measurement outcomes**: Uses data already collected for fidelity kernel
- **Avoids exponential concentration**: Full statistics preserve information that single fidelity value loses
- **Scalable**: Demonstrated up to 27 qubits in simulation

## Performance Results

| Metric | Fidelity Kernel | Hamming Kernel | Classical Gaussian |
|--------|----------------|----------------|-------------------|
| ≤14 qubits | Competitive | Competitive | Competitive |
| ≥15 qubits | Degrades | **Outperforms** | Varies |
| Synthetic quantum data | Poor | **Outperforms** | Outperformed |
| MNIST | Competitive | Competitive | Competitive |

## Implementation Pattern

```python
# Pseudocode for Hamming quantum kernel
def hamming_quantum_kernel(measurements_x, measurements_x_prime):
    """
    Compute Hamming kernel from measurement bitstrings.
    
    measurements_x: array of bitstrings from circuit with input x
    measurements_x_prime: array of bitstrings from circuit with input x'
    """
    # Count matching bitstrings across measurement distributions
    matching = count_hamming_similar(measurements_x, measurements_x_prime)
    total = len(measurements_x) * len(measurements_x_prime)
    return matching / total

# Use with sklearn SVM
from sklearn.svm import SVC
K_train = compute_hamming_kernel_all_pairs(train_measurements)
svm = SVC(kernel='precomputed')
svm.fit(K_train, train_labels)
```

## When to Use

- Quantum SVM problems with ≥15 qubits where fidelity kernel fails
- Classical post-processing is acceptable (no quantum overhead)
- Synthetic quantum data classification
- Scaling quantum kernel methods beyond NISQ limitations

## Key Advantage

**Zero additional quantum cost**: The Hamming kernel uses the same measurement data as the fidelity kernel. The improvement comes entirely from better classical processing of existing quantum data.

## Pitfalls

- Requires sufficient measurement shots for reliable statistics
- Classical computation cost grows with number of shots (not qubits)
- Still needs quantum circuit execution for data encoding
