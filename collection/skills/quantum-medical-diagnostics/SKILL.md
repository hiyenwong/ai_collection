---
name: quantum-medical-diagnostics
description: >
  Patterns and methodologies for applying quantum computing and quantum machine learning
  to medical diagnostics, healthcare, and clinical applications. Covers hybrid quantum-classical
  architectures (HQNNs, QNNs, QSVMs), quantum-enhanced medical imaging, federated quantum
  learning for privacy-aware diagnosis, and parameter-efficient quantum multi-task learning.
  Use when: (1) researching quantum ML for healthcare/medical diagnosis, (2) designing hybrid
  quantum-classical models for medical image classification, (3) implementing quantum circuits
  for clinical prediction tasks, (4) studying quantum advantage in medical data analysis,
  (5) building privacy-preserving quantum healthcare systems, (6) benchmarking QML on real
  quantum hardware with medical datasets (MedMNIST, etc.).
---

# Quantum Medical Diagnostics

Reusable patterns from research on quantum computing applied to medical diagnostics and healthcare.

## Core Architectural Patterns

### 1. Hybrid Quantum-Classical Feature Fusion

Map classical features into quantum Hilbert spaces for enrichment, then fuse back for classification.

**Pipeline:**
1. Classical feature extraction (CNN, ResNet, etc.)
2. Dimensionality reduction (PCA to ~8-16 features)
3. Quantum amplitude encoding (4-8 qubit circuit)
4. Feature fusion: concat classical + quantum features
5. Classical classifier (SVM, Random Forest, etc.)

**Fusion strategies** (from breast cancer classification research):
- **Static Hybrid Fusion (SHF)**: Fixed concatenation ratio
- **Dynamic Hybrid Fusion (DHF)**: Adaptive weighting per sample
- **Temperature-Scaled Hybrid Fusion (TSHF)**: Trainable temperature parameter controlling quantum/classical balance

**Key insight:** TSHF with ResNet + trainable quantum circuit achieves 87.82% accuracy, F1=91.77%, AUC-ROC=89.08% on BreastMNIST.

### 2. Quantum Neural Network (QNN) Classifiers for Healthcare

Use parameterized quantum circuits (PQCs) as trainable layers in neural networks.

**Architecture:**
```
Input → Data encoding (angle/amplitude) → PQC layers → Measurement → Classical post-processing → Output
```

**Healthcare applications:**
- Prostate cancer, heart failure, diabetes classification
- Thermographic breast cancer classification
- Brain tumor MRI classification (HQNN)

**Key findings:**
- QNNs achieve competitive accuracy with classical models on structured healthcare data
- Quantum attention mechanisms (QAttn-CNN) improve skin cancer classification
- Ablation studies show quantum layers improve generalization, reduce overfitting on small medical datasets

### 3. Tensor-Network Quantum Frontends for Federated Medical Diagnosis

Use tensor networks as classical frontends that compress medical data before quantum processing.

**Privacy benefits:**
- Tensor network compression reduces data exposure
- Compatible with federated learning across hospitals
- Quantum processing on compressed representations

### 4. Parameter-Efficient Quantum Multi-Task Learning

Share quantum circuit parameters across multiple diagnostic tasks.

**Benefits:**
- Reduced qubit requirements compared to per-task circuits
- Transfer learning between related medical conditions
- Efficient use of limited quantum hardware

## Medical Imaging Workflow

### Quantum-Enhanced Medical Image Analysis

```
Medical Image → Classical Preprocessing → Feature Extraction
    → Quantum Encoding → PQC Processing → Measurement
    → Classical Classification → Diagnosis
```

**Key techniques:**
- **PCA + Quantum Amplitude Encoding**: Reduce features to match available qubits (currently 4-8 practical)
- **Quantum Attention**: Replace classical attention with quantum circuit for feature weighting
- **Hybrid Convolutional**: Classical conv layers + quantum dense layers

**Benchmarks:**
- MedMNIST on 127-qubit IBM quantum hardware (first comprehensive QML study)
- X-ray fracture diagnosis: 99% accuracy, 82% faster feature extraction with hybrid pipeline
- Skin cancer: QAttn-CNN outperforms classical CNN on ISIC dataset

## Practical Considerations

### NISQ-Era Constraints

- Current hardware: 100-1000+ qubits but noisy (NISQ)
- Practical circuits: 4-16 qubits for medical tasks
- Shot noise limits measurement precision
- Classical simulation needed for circuit design validation

### Data Encoding Strategies

| Strategy | Qubits Needed | Best For |
|----------|--------------|----------|
| Amplitude encoding | log2(N) | Dense feature vectors |
| Angle encoding | N | Normalized features |
| Basis encoding | N | Binary/categorical data |

### Evaluation Metrics for QML Healthcare

- Accuracy, F1-score, AUC-ROC (standard)
- Parameter efficiency: accuracy per trainable parameter
- Feature extraction time reduction
- Generalization on small medical datasets

## Related Papers in Knowledge Graph

High PageRank papers (see kg.db):
- "Quantum computing and artificial intelligence: status and perspectives" (PR=0.015)
- "Quantum Circuit-Based Learning Models Bridging Quantum Computing and ML" (PR=0.013)
- "CTRQNets & LQNets: Continuous Time Recurrent and Liquid Quantum Neural Networks" (PR=0.006)

## References

- arxiv:2504.13910 — QML for Medical Image Classification survey
- arxiv:2505.20804 — QNN and QSVM evaluation on healthcare datasets
- arxiv:2604.22903 — Adaptive Hybrid Quantum-Classical Feature Fusion for Breast Cancer
- arxiv:2604.16953 — HQNNs for Breast Cancer Thermographic Classification
- arxiv:2604.01616 — Tensor-Network Frontends for Privacy-Aware Federated Medical Diagnosis
- arxiv:2604.13560 — Parameter-efficient Quantum Multi-task Learning
- Nature s41598-026-35605-3 — MedMNIST benchmarking on real quantum hardware
- arxiv:2409.10932 — Hybrid QML for Coronary Heart Disease Detection
- arxiv:2505.14716 — Hybrid Quantum Classical Pipeline for X-Ray Fracture Diagnosis
