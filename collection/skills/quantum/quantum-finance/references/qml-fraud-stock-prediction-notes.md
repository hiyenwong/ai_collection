# Quantum ML for Financial Fraud Detection & Stock Prediction — Session Notes (2026-05-23)

## 1. Contextual QNN for Multi-Asset Stock Prediction (arXiv: 2503.01884)

**Core innovation**: Share-and-specify ansatz enables simultaneous training of multiple assets on the SAME quantum circuit via quantum labels controlling task-specific operators.

**Key metrics**:
- Logarithmic qubit overhead: O(log N) for N assets vs O(N) for independent circuits
- Quantum Batch Gradient Update (QBGU) accelerates standard quantum SGD
- Tested on S&P 500: Apple, Google, Microsoft, Amazon stocks
- Outperforms Quantum Single-Task Learning (QSTL) baselines
- Captures inter-asset correlations naturally through shared quantum representation

**Architecture**:
- Shared layers: common quantum feature extraction across all assets
- Specify layers: asset-specific operators controlled by quantum labels
- Context encoding: recent trends (not entire history) as quantum context labels

**When to use**: Multi-asset prediction tasks where capturing cross-asset correlations matters and qubit budget is constrained.

## 2. FiD-QAE: Fidelity-Driven Quantum Autoencoder for Fraud Detection (arXiv: 2512.12689)

**Core innovation**: Uses quantum state fidelity (via SWAP test) as the anomaly detection criterion rather than classical reconstruction error.

**Key metrics**:
- F1-score competitive with classical methods under noise
- Validated on real IBM Quantum hardware with results consistent with simulation
- Maintains consistent performance across different class imbalance levels
- Robust under 5 quantum noise types (depolarizing, amplitude damping, phase damping, bit flip, phase flip)

**How it works**:
1. Transactions encoded into quantum states
2. Variational quantum circuit compresses to latent representation
3. SWAP test estimates fidelity between original and reconstructed states
4. Fidelity < threshold → fraud; Fidelity ≥ threshold → legitimate
5. Threshold calibrated on validation set

**When to use**: Financial anomaly detection where data dimensionality is high and classical autoencoders struggle. Quantum exponential encoding handles curse of dimensionality.

## 3. QML Architecture Comparison for Fraud Detection (arXiv: 2412.19441)

**Systematic comparison of 3 QML classifiers on non-normalized financial fraud datasets**:

| Architecture | F1-Score | Data Sensitivity | Noise Robustness |
|-------------|----------|-----------------|------------------|
| VQC | 0.88 | Low (robust) | High |
| SQNN | ~0.80-0.85 | Moderate | Moderate |
| EQNN | < 0.70 | High (struggles with non-standardized data) | Low |

**Key findings**:
- VQC consistently demonstrates strong classification results across configurations
- EQNN struggles significantly with non-standardized financial data — data preprocessing is critical
- Feature map and ansatz configuration choices DOMINATE architecture selection
- ANOVA confirms statistical significance of observed performance differences
- Best-performing models maintain competitive performance under 5 noise types

**Methodology**: Systematic evaluation across feature maps (angle, amplitude, IQP, ZZ) × ansatz configurations × layer depths (2-4 layers), with ANOVA validation and noise robustness testing.

**When to use**: When selecting QML architecture for financial classification tasks — start with VQC, systematically evaluate feature map/ansatz combinations, validate with ANOVA.

## Cross-Pattern Insights

1. **Data normalization is critical across all QML finance applications**: Non-normalized data causes poor convergence (EQNN) or encoding failures
2. **Configuration matters more than architecture**: Feature map and ansatz choices dominate performance differences
3. **Noise robustness is achievable**: Well-configured QML models maintain competitive performance under realistic noise conditions
4. **Logarithmic scaling is the key advantage**: QMTL achieves O(log N) qubit overhead for N assets — this is where quantum advantage emerges
5. **VQC is the safest starting point**: For classification tasks, VQC consistently outperforms alternatives with lower data sensitivity
