---
name: quantum-medical-diagnosis
description: "Framework for applying quantum machine learning to medical diagnosis tasks. Covers QNN architectures, encoding strategies, and evaluation methodologies for clinical data. Trigger: quantum medical diagnosis, QNN healthcare, quantum clinical prediction, medical quantum ML"
---

# Quantum Medical Diagnosis

Framework for applying quantum machine learning (QML) to medical diagnosis and clinical prediction tasks.

## Core Methodology

### 1. Problem Identification

- **Rare Event Prediction**: QNNs show advantage for low-prevalence conditions (e.g., 14% anastomotic leak rate, Fβ-optimized sensitivity 83.3%)
- **Complex Pattern Recognition**: Quantum feature spaces capture non-linear relationships in medical imaging (breast cancer, diabetic retinopathy)
- **Privacy-Sensitive Data**: Federated quantum learning (FQPDR) for distributed medical datasets without sharing patient data
- **Data Complexity Signature**: Predict when quantum outperforms classical — QPL approach on 60-qubit IBM Eagle/Heron hardware

### 2. Quantum Neural Network Architecture Selection

#### Hybrid QNN (Recommended for NISQ)
- Classical encoder + Quantum variational circuit + Classical classifier
- Best for: Image-based diagnosis (breast cancer, diabetic retinopathy, blood cells)
- **Adaptive Fusion**: Dual-branch quantum+classical with adaptive weighting based on data complexity (arXiv: 2604.22903)
- **Blood Cell Classification**: ResNet-50 backbone → latent bottleneck → VQC → classifier, 3.7% F1 improvement, IBM hardware-validated (arXiv: 2605.23324)

#### Three-Model Comparison Protocol (arXiv: 2605.23324)
To rigorously isolate quantum advantage in HQNN medical imaging, evaluate three architectures:
1. **HQNN**: Classical backbone → bottleneck → VQC → classifier
2. **Classical Matched**: Classical backbone → bottleneck → classical nonlinear layer (same capacity as VQC) → classifier
3. **Baseline**: Classical backbone → classifier (no intermediate transformation)
This controls for model capacity and ensures reported improvements are genuinely quantum-derived, not from added parameters.

#### Pure QNN
- End-to-end quantum circuit with ZZFeatureMap encoding
- Best for: Tabular clinical data (colorectal cancer risk, CKD prediction)
- Example: QNN for anastomotic leak classification with 83.3% sensitivity vs classical baselines

#### Energy-Based Training (Equilibrium Propagation)
- Backprop-free training via energy differences: ∂E/∂θ ≈ (E_nudged - E_free) / ε
- Compatible with quantum circuits where backprop is not natively supported
- Use when: blood cell analysis, leukemia detection, NISQ hardware constraints
- See: `qml-equilibrium-propagation-medical` skill for full methodology

#### Lightweight Hybrid (CNN + VQC Classifier Head)
- Classical CNN backbone + quantum circuit as classifier head (1-4 qubits)
- Reduces operator-dependency in medical image interpretation
- Use when: coronary angiography, cardiac imaging, lightweight QML enhancement
- See: `quantum-enhanced-coronary-classification` skill for full methodology

#### Federated QNN
- Privacy-preserving collaborative learning across institutions
- Best for: Multi-center medical image analysis (diabetic retinopathy)
- Architecture: Local QNN training + parameter aggregation without data sharing

### 3. Encoding Strategy

| Data Type | Encoding Method | Qubits Required | Paper Evidence |
|-----------|----------------|-----------------|----------------|
| Medical Images | Amplitude encoding | log2(image_features) | FQPDR, HQNN breast cancer |
| Tabular Clinical | ZZFeatureMap + RealAmplitudes | num_features | Colorectal cancer (83.3% sens) |
| Tabular Clinical | ZZFeatureMap + EfficientSU2 | num_features | CKD design space exploration |
| Time-series | Quantum Projective Learning | variable | Antibiotic resistance (60 qubit) |
| Multiomic | Quaternionic extensions | num_features * 4 | Neurodegenerative diseases |

### 4. Circuit Design Patterns

#### Ansatz Selection
- **RealAmplitudes**: General purpose, proven for clinical tabular data
- **EfficientSU2**: Hardware-efficient, better for noisy NISQ devices
- **TwoLocal**: Balanced expressibility and trainability

#### Design Space Exploration Checklist (from CKD study)
- [ ] Encoding method (amplitude, angle, IQP)
- [ ] Ansatz architecture (RealAmplitudes, EfficientSU2, TwoLocal)
- [ ] Circuit depth vs noise tradeoff
- [ ] Measurement strategy (expectation values, probabilities)
- [ ] Shot count (1000+ for stable gradients)
- [ ] Classical layer configuration

### 5. Evaluation Metrics for Medical QML

- **Sensitivity/Recall**: Critical for rare disease detection — quantum configs achieved 83.3% vs classical lower
- **Fβ-score**: Weight toward recall (β>1) for imbalanced medical datasets
- **AUC-ROC**: Overall discrimination ability
- **Clinical Utility**: Decision curve analysis for deployment readiness
- **Privacy Preservation**: Federated learning efficiency metrics

### 6. Noise Robustness

- Simulate hardware noise during training (tested under simulated noise in colorectal study)
- Use error mitigation techniques
- Test under varying noise levels to find robust configurations
- Compare with classical baselines under same noise conditions

### 7. Federated Quantum Learning (FQPDR Pattern)

1. **Local QNN Training**: Each institution trains QNN on local medical data
2. **Parameter Aggregation**: Server aggregates model parameters (not data)
3. **Cross-Evaluation**: Validate on held-out datasets from other institutions
4. **Lightweight Models**: Few learnable parameters for practical deployment
5. **Datasets**: E-ophtha, Retina MNIST, Kaggle DR datasets

## Workflow

1. **Data Preparation**: Normalize medical data, handle class imbalance (SMOTE, weighted loss)
2. **Feature Selection**: Reduce dimensionality for qubit constraints (PCA, feature importance)
3. **Encoding Choice**: Select based on data type and problem complexity
4. **Circuit Design**: Choose ansatz, depth, measurement strategy via design space exploration
5. **Training**: Hybrid optimization with noise simulation
6. **Evaluation**: Compare with classical baselines on clinical metrics
7. **Validation**: External dataset testing, cross-institution validation for federated

## Key Papers (2026)

- **FQPDR**: Federated QNN for Diabetic Retinopathy (arXiv: 2605.08324) — privacy-preserving early detection
- **Adaptive HQNN**: Quantum+Classical Feature Fusion for Breast Cancer (arXiv: 2604.22903) — dual-branch adaptive weighting
- **HQNN Design Space**: Hybrid QNN for Chronic Kidney Disease (arXiv: 2604.13608) — systematic encoding/ansatz evaluation
- **QML Colorectal**: Anastomotic Leak Classification (arXiv: 2604.13951) — 83.3% sensitivity with ZZFeatureMap
- **HQNN Blood Cells**: Blood Cell Classification with HQNN (arXiv: 2605.23324) — ResNet-50 + VQC, 3.7% F1 improvement, IBM hardware-validated
- **QPL Antibiotic**: Quantum Projective Learning for Resistance (arXiv: 2601.15483) — 60-qubit IBM Eagle/Heron experiments
- **Quantum Neuro**: Frequency-Domain Multiomic Analysis (arXiv: 2508.07948) — quaternionic extensions for AD/MS/PD/ALS

## Pitfalls

1. **Qubit Limitations**: Current NISQ devices limit problem size — use design space exploration to find optimal qubit count
2. **Noise Sensitivity**: Medical applications require high reliability — test under simulated hardware noise
3. **Data Scarcity**: Medical datasets are often small — federated learning addresses this
4. **Classical Baselines**: Must demonstrate quantum advantage over classical ML — use Fβ-optimized comparison
5. **Class Imbalance**: Rare medical events need special handling — Fβ optimization, weighted loss
6. **Regulatory Compliance**: Medical applications require FDA/CE considerations

## Activation Keywords

- quantum medical diagnosis
- QNN healthcare
- quantum clinical prediction
- medical quantum ML
- quantum cancer detection
- federated quantum learning medical
- quantum anastomotic leak
- quantum diabetic retinopathy
- quantum CKD prediction
- quantum antibiotic resistance