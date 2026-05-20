---
name: large-scale-quantum-kernels-hyperspectral
description: "Large-scale fidelity quantum kernel SVM for hyperspectral classification using tensor network contraction and GPU acceleration. Overcomes exponential concentration via bandwidth optimization."
category: quantum-ml
---

# Large-Scale Quantum Kernels for Hyperspectral Data Classification

**arXiv**: 2605.17587 (quant-ph)
**Authors**: A. Delilbasic, A. Miroszewski, A. Wijata, J. Nalepa, J. Mielczarek, M. Riedel, G. Cavallaro

## Core Methodology

First large-scale study of **fidelity-quantum-kernel SVMs** for hyperspectral data classification **without** heavy prior feature selection or dimensionality reduction.

### Computational Breakthrough

- **Tensor network contraction** + **GPU acceleration** overcomes traditional bottlenecks
- Achieves **quadratic scaling O(n²)** in number of qubits
- Enables evaluation on data with **hundreds of spectral bands**

### Key Finding: Bandwidth Optimization

Kernel bandwidth optimization is **crucial** for mitigating exponential concentration effects and ensuring generalization. Without proper bandwidth tuning, quantum kernels collapse to trivial solutions.

### Results

| Dataset | Task | Quantum Kernel | Classical RBF |
|---------|------|---------------|---------------|
| Indian Pines (50-band) | Binary | 78.0±6.2% | 72.0±5.0% |
| Indian Pines (50-band) | 4-class | 83.3±3.1% | — |
| Methane Detection (75-band) | Binary | 58.5±5.0% | 55.1±2.5% |

## Implementation Patterns

- Simulate quantum kernels via tensor network contraction (not direct statevector)
- Use GPU acceleration for O(n²) kernel matrix computation
- Optimize kernel bandwidth to avoid exponential concentration
- Apply to high-dimensional data without preprocessing/dimensionality reduction
- Benchmark against multiple classical baselines under identical budgets

## Pitfalls

- **Exponential concentration**: Quantum kernels collapse if bandwidth is not optimized
- **No heavy feature selection needed**: Quantum kernels work directly on raw spectral bands
- **Tensor network simulation**: More scalable than direct quantum simulation

## Applications

- Hyperspectral remote sensing classification
- High-dimensional medical imaging
- Environmental monitoring (methane detection, etc.)
- Any domain with high-dimensional feature spaces

## Activation

quantum kernels, hyperspectral classification, tensor network contraction, fidelity kernel, exponential concentration, bandwidth optimization, quantum SVM
