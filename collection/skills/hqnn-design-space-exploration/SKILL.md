---
name: hqnn-design-space-exploration
description: "Systematic design space exploration methodology for Hybrid Quantum Neural Networks. Covers encoding methods, ansatz selection, measurement strategies, and shot optimization for medical ML applications. Trigger: HQNN design, quantum neural network architecture search, QNN encoding selection, quantum circuit design medical"
---

# HQNN Design Space Exploration

Systematic methodology for exploring and optimizing Hybrid Quantum Neural Network (HQNN) architectures for near-term quantum machine learning applications.

## Motivation

HQNN performance depends critically on design choices:
- Classical-to-quantum data encoding method
- Quantum circuit architecture (ansatz)
- Measurement strategy
- Number of shots

Poor choices lead to suboptimal performance even on the same task. This methodology provides a systematic exploration framework.

## Design Space Dimensions

### 1. Encoding Methods

| Method | Description | Qubit Cost | Best For |
|--------|-------------|-----------|----------|
| **Amplitude** | Encode data as quantum state amplitudes | log2(n) | High-dimensional data, images |
| **Angle** | Encode features as rotation angles | n | Low-dimensional tabular data |
| **IQP** | Instantaneous Quantum Polynomial encoding | n | Complex feature interactions |
| **ZZFeatureMap** | Entangling feature map with ZZ interactions | n | Tabular clinical data (proven for colorectal cancer) |

### 2. Ansatz Architectures

| Ansatz | Expressibility | Trainability | Hardware Efficiency | Best Use |
|--------|---------------|-------------|-------------------|----------|
| **RealAmplitudes** | Medium | High | Medium | Clinical tabular data (83.3% sensitivity achieved) |
| **EfficientSU2** | High | Medium | High | Noisy NISQ devices |
| **TwoLocal** | High | Medium | Medium | Balanced expressibility-trainability |
| **HardwareEfficient** | Medium | High | Very High | Specific quantum hardware |

### 3. Measurement Strategies

- **Expectation Values**: Standard for classification tasks
- **Probability Distributions**: For multi-class problems
- **Fβ-Optimized**: Weight toward recall for imbalanced medical datasets
- **Multi-Objective**: Simultaneous optimization of sensitivity + specificity

### 4. Shot Count Optimization

- **1000+ shots**: Stable gradients for training
- **100-500 shots**: Faster iteration, noisier gradients
- **Adaptive shots**: Increase shots as training converges
- **Shot noise analysis**: Evaluate performance vs shot count tradeoff

## Exploration Protocol

### Phase 1: Encoding Screening
1. Test all viable encoding methods on target dataset
2. Measure: training stability, convergence speed, final accuracy
3. Select top 2 encodings for Phase 2

### Phase 2: Ansatz Optimization
1. For each selected encoding, test all ansatz architectures
2. Vary circuit depth: [1, 2, 3, 5] layers
3. Measure: expressibility, trainability, noise robustness
4. Select top 2 (encoding, ansatz) combinations

### Phase 3: Measurement Tuning
1. Test different measurement strategies
2. Optimize Fβ for target recall/sensitivity
3. Validate on held-out test set

### Phase 4: Shot Analysis
1. Train with varying shot counts: [100, 500, 1000, 5000]
2. Plot performance vs computational cost
3. Select minimum shots achieving target performance

### Phase 5: Noise Robustness
1. Simulate hardware noise at different levels
2. Test selected configuration under noise
3. Apply error mitigation if needed
4. Compare with classical baseline under same conditions

## Evaluation Metrics

| Metric | Formula | Medical Target |
|--------|---------|---------------|
| **Sensitivity** | TP/(TP+FN) | >80% for rare events |
| **Specificity** | TN/(TN+FP) | >85% |
| **Fβ-Score** | (1+β²)·P·R/(β²·P+R) | β=2 for recall emphasis |
| **AUC-ROC** | Area under ROC curve | >0.85 |
| **Noise Robustness** | Performance degradation | <10% under hardware noise |

## Implementation Checklist

- [ ] Define problem type (binary/multi-class classification, regression)
- [ ] Characterize dataset (size, features, class balance)
- [ ] Determine qubit budget (hardware constraints)
- [ ] Phase 1: Encoding screening
- [ ] Phase 2: Ansatz optimization with depth sweep
- [ ] Phase 3: Measurement strategy selection
- [ ] Phase 4: Shot count optimization
- [ ] Phase 5: Noise robustness testing
- [ ] Compare with classical baselines
- [ ] External validation on independent dataset

## Key Findings from Literature

1. **ZZFeatureMap + RealAmplitudes**: Best for clinical tabular data (colorectal cancer: 83.3% sensitivity)
2. **ZZFeatureMap + EfficientSU2**: Better for noisy devices
3. **Fβ-optimization**: Critical for imbalanced medical datasets (14% leak prevalence)
4. **Design space matters**: Poor choices can negate quantum advantage
5. **Noise simulation**: Essential before hardware deployment

## Pitfalls

1. **Exhaustive search infeasible**: Use systematic screening, not grid search
2. **Overfitting to noise**: Test generalization across noise levels
3. **Ignoring classical baselines**: Always compare against best classical method
4. **Hardware constraints**: Design choices limited by available qubits and connectivity
5. **Small datasets**: Medical data often limited — use cross-validation carefully

## Related Skills

- `quantum-medical-diagnosis`: Broader quantum ML for medical applications
- `quantum-neural-architecture`: General QNN design principles
- `quantum-ml-patterns`: Reusable QML research patterns

## Activation Keywords

- HQNN design
- quantum neural network architecture search
- QNN encoding selection
- quantum circuit design medical
- hybrid quantum architecture
- quantum ansatz selection
- QNN shot optimization
- quantum feature map medical