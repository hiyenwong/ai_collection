# Clinical QML Patterns for Imbalanced Medical Data

## Core Pattern: Quantum Advantage for Minority Class Prediction

Across multiple studies (2026), QML shows consistent advantage in clinical settings where:
- Target prevalence is low (10-20%)
- Classical models sacrifice sensitivity for accuracy
- False negatives are clinically costly

## Validated Results

| Paper | Task | Classical Sensitivity | QNN Sensitivity | Method |
|-------|------|----------------------|-----------------|--------|
| 2604.13951 | Anastomotic leak (14%) | 66.7% | 83.3% | ZZFeatureMap + RealAmplitudes/EfficientSU2 |
| 2606.03517 | Clinical data imputation | N/A | Matches/exceeds baselines | Butterfly circuit + parallelized parameter-shift |
| 2604.22903 | Breast cancer classification | - | - | Adaptive hybrid quantum-classical feature fusion |
| 2604.22877 | MGMT methylation (glioblastoma) | - | - | IA-QCNN with ring-topology |
| 2602.14641 | Biomarker prediction | Comparable | Reduced variance | QRC with neutral atoms (hardware regularization) |

## Key Methodology

### Feature Encoding
- **ZZFeatureMap**: Entangling encoding for clinical feature interaction capture
- **Hybrid encoding**: Classical pre-processing + quantum feature space for best results

### Optimization
- **F_beta > accuracy**: Clinical tasks prioritize sensitivity; optimize for F_beta (beta > 1)
- **Noise-aware training**: Test under hardware noise models before deployment
- **Multiple optimizers**: COBYLA, SPSA, Adam converge differently under noise

### Hardware Progress
- 2606.03517: First demonstration of QNN training on real hardware (IonQ Forte, 16 qubits) with 32-qubit inference
- 2602.14641: Neutral-atom QRC shows beneficial regularization effect from hardware noise

## Pitfalls
- Accuracy is misleading for imbalanced clinical data — always report sensitivity/recall
- Small clinical datasets risk overfitting QNNs
- Hardware noise degrades performance; ansatz robustness testing is mandatory
- Optimizer choice significantly impacts convergence under noise
