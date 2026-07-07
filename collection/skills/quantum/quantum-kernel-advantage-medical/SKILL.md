---
name: quantum-kernel-advantage-medical
version: v1.0.0
last_updated: 2026-05-20
description: "Quantum kernel advantage methodology for medical imaging classification under class imbalance. Use when: (1) Evaluating QSVM vs classical SVM on medical datasets with severe class imbalance, (2) Comparing quantum and classical kernels using frozen foundation model embeddings, (3) Designing two-tier fair comparison frameworks for quantum ML, (4) Analyzing kernel eigenspectrum for effective rank, (5) Addressing classical kernel collapse on minority class prediction. Based on arXiv:2604.24597."
---

# Quantum Kernel Advantage for Medical Imaging

## Core Methodology

Demonstrate quantum kernel advantage using a two-tier fair comparison framework:
- **Input**: Frozen embeddings from medical foundation models (MedSigLIP, RAD-DINO, ViT)
- **Dimensionality reduction**: PCA to q features
- **Classifiers**: QSVM vs classical SVM on identical features

## Two-Tier Comparison Framework

### Tier 1: Untuned Comparison
- Untuned QSVM (C=1) vs untuned linear SVM (C=1)
- Both receive identical PCA-q features
- Evaluate minority-class F1 across multiple qubit counts
- Quantum advantage when classical linear kernel collapses to majority-class prediction

### Tier 2: Tuned Classical Baseline
- Untuned QSVM vs C-tuned RBF SVM
- Classical SVM gets hyperparameter tuning advantage
- Quantum advantage persists if QSVM still wins

## Key Findings

- Classical linear kernel collapses: 90-100% seeds predict majority class at every qubit count
- QSVM maintains non-trivial recall without tuning
- At q=11 with MedSigLIP-448: QSVM F1=0.343 vs classical F1=0.050 (gain +0.293, p<0.001)
- Quantum kernel effective rank far exceeds linear kernel rank at optimal qubit counts

## Kernel Eigenspectrum Analysis

```
effective_rank = exp(entropy(eigenvalues))
```

- Quantum kernel effective rank peaks at architecture-dependent qubit count
- Classical linear kernel rank remains C-invariant (collapsing)
- Eigenspectrum analysis predicts which qubit counts will show advantage

## Implementation

```python
from qiskit_machine_learning.kernels import QuantumKernel
from sklearn.decomposition import PCA
from sklearn.svm import SVC

# Step 1: Get frozen embeddings from medical foundation model
# embeddings shape: (n_samples, d)

# Step 2: PCA dimensionality reduction
pca = PCA(n_components=q)
X_pca = pca.fit_transform(embeddings)

# Step 3: QSVM with quantum kernel
qsvm = SVC(kernel='precomputed')
# Compute quantum kernel matrix using parameterized circuit
K_q = compute_quantum_kernel(X_pca_train, X_pca_train, n_qubits=q)
qsvm.fit(K_q, y_train)

# Step 4: Classical baseline
linear_svm = SVC(kernel='linear', C=1.0)
linear_svm.fit(X_pca_train, y_train)

# Step 5: Compare F1 on minority class
```

## When to Use

- Medical imaging classification with class imbalance
- Evaluating quantum advantage claims rigorously
- Feature selection via PCA + kernel comparison
- Foundation model embedding evaluation

## Activation Keywords
- quantum kernel advantage, QSVM medical, quantum SVM classification, quantum kernel medical imaging, quantum advantage medical, quantum SVM vs classical SVM, 量子核优势医学, quantum foundation model embeddings, classical kernel collapse, kernel eigenspectrum

## Paper Reference
- arXiv:2604.24597 — "Quantum Kernel Advantage over Classical Collapse in Medical Foundation Model Embeddings"
- Code: https://github.com/sebasmos/qml-medimage
