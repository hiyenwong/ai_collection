---
name: quantum-clinical-benchmarking
description: "Rigorous clinical benchmarking methodology for quantum machine learning in healthcare. Covers statistically reliable QNN evaluation, hardware noise simulation, clinical metric optimization (sensitivity-specificity tradeoffs), and quantum kernel comparison on real medical datasets. Trigger: quantum clinical benchmark, QNN medical validation, quantum healthcare benchmarking, clinical quantum ML evaluation, quantum medical prediction."
---

# Quantum Clinical Benchmarking Methodology

Systematic benchmarking framework for evaluating quantum machine learning models on clinical medical datasets. Addresses the critical gap between quantum ML research and clinically deployable models through rigorous statistical evaluation, noise-aware testing, and medically relevant metric optimization.

## Core Methodology

### 1. Clinical Study Design Pattern

**Key Finding**: A priori medical constraints on patient data are essential — unlike toy ML benchmarks, clinical datasets have strict inclusion/exclusion criteria that fundamentally limit available samples (e.g., 200-patient colorectal surgery cohort).

**Design Checklist**:
- [ ] Define clinical endpoint (e.g., anastomotic leak, disease diagnosis)
- [ ] Apply a priori medical inclusion/exclusion criteria
- [ ] Determine minimum clinically required sensitivity (e.g., 83.3% for leak detection)
- [ ] Calculate specificity at fixed sensitivity threshold
- [ ] Ensure statistical reliability: average across 10+ independent optimization runs

### 2. QNN Architecture Benchmarking Protocol

**Tested Configurations** (from clinical anastomotic leak study):

| Configuration | Encoding | Ansatz | Optimizer | Key Metric |
|--------------|----------|--------|-----------|------------|
| EfficientSU2-BFGS | ZZFeatureMap | EfficientSU2 | BFGS | Highest mean AUC |
| RealAmplitudes-CMA | ZZFeatureMap | RealAmplitudes | CMA-ES | Highest Average Precision |

**Critical Finding**: At clinically required sensitivity of 83.3%, specific QNN configurations achieved significantly higher specificity and NPV than classical baselines (logistic regression, MLP, boosting algorithms).

### 3. Quantum Kernel Evaluation Framework

**From COVID-19 biomarker study** — systematic comparison of quantum kernels:

| Kernel Method | Encoding | Use Case |
|--------------|----------|----------|
| Amplitude Encoding | State amplitude | High-dimensional omics data |
| Angle Encoding | Rotation angles | Normalized biomarker values |
| ZZ Feature Map | Entanglement | Correlated multi-omics features |
| Projected Quantum Kernel | Subspace projection | Dimensionality-reduced biomarkers |

**Performance-based Feature Importance**: Ridge regression for biomarker ranking → higher/lower importance groups → compare classical SVM vs QSVM on each group.

### 4. Hardware Noise Simulation Protocol

- Simulate realistic hardware noise during QNN training
- Test multiple noise levels (calibration errors, decoherence)
- Report performance distribution (mean ± std) across noise conditions
- Compare with classical baselines under same noise constraints

### 5. Statistical Reliability Requirements

**From Nature Scientific Reports study**:
- Performance averaged across 10 independent optimization runs
- Report both AUC and Average Precision (handles class imbalance)
- Calculate Negative Predictive Value (NPV) at clinical sensitivity threshold
- Statistical significance testing against classical baselines

### 6. Clinical Metric Optimization Strategy

**Priority Order** (for rare event prediction):
1. **Sensitivity/Recall**: Fixed at clinically required minimum (e.g., 83.3%)
2. **Specificity**: Maximize at fixed sensitivity
3. **NPV**: Critical for ruling out disease
4. **AUC**: Overall discrimination ability
5. **Average Precision**: Better than AUC for imbalanced clinical data

### 7. Dataset Requirements

- Minimum 100-200 patients for meaningful QNN evaluation
- Class imbalance must be addressed (anastomotic leak ~14% prevalence)
- Multi-cohort validation when possible (Cleveland Clinic + Swedish Medical Center)
- External validation on held-out datasets

## Workflow

1. **Clinical Problem Definition**: Identify endpoint, constraints, minimum sensitivity
2. **Data Preparation**: Apply medical criteria, handle class imbalance
3. **Architecture Search**: Test ZZFeatureMap + multiple ansatze + optimizers
4. **Noise Simulation**: Test under realistic hardware noise conditions
5. **Statistical Evaluation**: 10+ runs, report distribution, significance testing
6. **Clinical Metric Analysis**: Optimize specificity at fixed sensitivity
7. **Classical Comparison**: Benchmark against hyperparameter-tuned classical models

## Key Papers (2026)

- **QNN Anastomotic Leak**: Nature Scientific Reports (DOI: 10.1038/s41598-026-44402-x) — clinical benchmarking of QNNs vs classical models on 200-patient dataset
- **QSVM COVID-19 Biomarker**: Computer Methods and Programs in Biomedicine (DOI: 10.1016/j.cmpb.2026.109343) — quantum SVM for biomarker analysis with performance-based feature importance

## Pitfalls

1. **A Priori Constraints**: Clinical data cannot be augmented arbitrarily — respect medical inclusion criteria
2. **Single-Run Results**: QNN training is non-convex; single-run results are meaningless
3. **Class Imbalance**: Medical datasets are imbalanced; use Average Precision, not AUC alone
4. **Hardware Noise**: Simulated results ≠ real quantum device — test under noise
5. **Clinical Threshold**: Accuracy is not clinically meaningful — optimize for sensitivity-specificity tradeoffs
6. **Baseline Rigor**: Compare against hyperparameter-tuned classical models, not default baselines
