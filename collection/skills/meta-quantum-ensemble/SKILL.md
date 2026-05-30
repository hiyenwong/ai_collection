---
name: meta-quantum-ensemble
description: "Hybrid quantum-classical ensemble methodology for network intrusion detection. Fuses QSVM and QNN outputs using Random Forest meta-learner to capture agreement/disagreement patterns between quantum branches."
tags: [quantum, machine-learning, security, intrusion-detection, ensemble]
---

# Meta-Quantum Ensemble (MQE)

## Description

Hybrid quantum-classical ensemble framework for robust network intrusion detection. Combines Quantum Support Vector Machines (QSVMs) and Quantum Neural Networks (QNNs) — which rely on different learning mechanisms and exhibit distinct prediction behaviors — using a Random Forest meta-learner that captures agreement and disagreement patterns between quantum branches to improve prediction stability and detection performance on imbalanced IoT/IDS datasets.

Based on: *Meta-Quantum Ensemble Framework for Robust Network Intrusion Detection* (arXiv: 2605.28879)

## Activation Keywords

- meta-quantum ensemble
- MQE intrusion detection
- quantum ensemble IDS
- QSVM QNN fusion
- hybrid quantum ensemble
- quantum intrusion detection
- quantum network security
- quantum ML ensemble

## Tools Used

- terminal: Run quantum circuit simulations (Qiskit/PennyLane)
- web_search: Find quantum ML datasets and benchmarks
- read_file: Load training data and model configurations
- write_file: Save trained ensemble models and evaluation results

## Installation

```bash
pip install qiskit qiskit-machine-learning scikit-learn numpy pandas
```

### Prerequisites

- Python 3.9+
- Qiskit runtime access (local simulator or IBM Quantum)
- scikit-learn for classical meta-learner

## Usage Patterns

### Pattern 1: Standalone QSVM Training

```python
from qiskit_machine_learning.kernels import FidelityQuantumKernel
from qiskit_machine_learning.algorithms import QSVC

# Train QSVM on network traffic features
qsvm = QSVC(quantum_kernel=FidelityQuantumKernel(feature_map=ZZFeatureMap))
qsvm.fit(X_train, y_train)
predictions_qsvm = qsvm.predict(X_test)
```

### Pattern 2: Standalone QNN Training

```python
from qiskit_machine_learning.neural_networks import SamplerQNN
from qiskit_machine_learning.algorithms import NeuralNetworkClassifier

# Train QNN on same features
qnn = SamplerQNN(feature_map=ZZFeatureMap, ansatz=RealAmplitudes)
qnn_classifier = NeuralNetworkClassifier(qnn)
qnn_classifier.fit(X_train, y_train)
predictions_qnn = qnn_classifier.predict(X_test)
```

### Pattern 3: MQE Meta-Ensemble Fusion

```python
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Step 1: Get predictions from both quantum models
pred_qsvm = qsvm.predict(X_test)
pred_qnn = qnn_classifier.predict(X_test)
prob_qsvm = qsvm.predict_proba(X_test)
prob_qnn = qnn_classifier.predict_proba(X_test)

# Step 2: Build meta-features capturing agreement/disagreement
meta_features = np.column_stack([
    prob_qsvm,           # QSVM probabilities
    prob_qnn,            # QNN probabilities
    pred_qsvm == pred_qnn,  # Agreement indicator (1=agree, 0=disagree)
    np.abs(prob_qsvm - prob_qnn).sum(axis=1)  # Prediction divergence
])

# Step 3: Train Random Forest meta-learner
meta_learner = RandomForestClassifier(n_estimators=100, random_state=42)
meta_learner.fit(meta_features, y_test)  # Use labels for supervised meta-learning

# Step 4: Ensemble predictions
ensemble_predictions = meta_learner.predict(meta_features)
```

## Instructions for Agents

### Step 1: Dataset Preparation

1. Load network intrusion detection dataset (TON IoT, CICIDS2017, or similar)
2. Handle class imbalance using SMOTE or class weighting
3. Normalize features to [0, 1] range for quantum encoding
4. Split into train/validation/test sets (e.g., 70/15/15)
5. Reduce feature dimensionality if needed (PCA, feature selection) for qubit compatibility

### Step 2: Train QSVM Branch

1. Select feature map (ZZFeatureMap for non-linear separability)
2. Configure kernel (FidelityQuantumKernel or TrainableFidelityQuantumKernel)
3. Train QSVC on training data
4. Evaluate on validation set (precision, recall, F1, especially at low FPR)

### Step 3: Train QNN Branch

1. Select ansatz (RealAmplitudes, EfficientSU2, or custom)
2. Configure SamplerQNN with appropriate feature map
3. Train using NeuralNetworkClassifier or VQC
4. Evaluate on validation set

### Step 4: Build Meta-Ensemble

1. Extract predictions and probabilities from both quantum models
2. Construct meta-features:
   - Individual model probabilities (all class probabilities)
   - Agreement indicator (binary: same/different prediction)
   - Prediction divergence (L1 or L2 distance between probability vectors)
   - Per-model confidence scores
3. Train Random Forest meta-learner on meta-features + true labels
4. Evaluate ensemble on test set

### Step 5: Evaluation and Analysis

1. Compare ensemble vs. standalone quantum models across metrics:
   - Overall accuracy, precision, recall, F1
   - Low-FPR performance (critical for IDS)
   - Reliability metrics (calibration, stability)
   - Per-class performance (attack type detection rates)
2. Analyze agreement/disagreement patterns:
   - When do QSVM and QNN disagree?
   - Does the meta-learner correctly resolve disagreements?
   - Which quantum branch is more reliable for specific attack types?
3. Document results with dataset, metric, and fusion representation dependencies

## Error Handling

### Too Many Features for Quantum Circuit
```
If feature count > available qubits:
  1. Apply PCA to reduce to target dimensionality
  2. Use feature importance ranking to select top features
  3. Consider amplitude encoding for exponential compression
```

### QSVM/QNN Training Fails to Converge
```
If training loss plateaus or oscillates:
  1. Check for barren plateaus (gradient norm ~ 0)
  2. Reduce circuit depth or use layer-wise training
  3. Try different ansatz or feature map
  4. Increase shots for more accurate probability estimation
```

### Meta-Learn Overfits to Validation Set
```
If ensemble performance drops on test set:
  1. Use cross-validation for meta-feature construction
  2. Add regularization to Random Forest (max_depth, min_samples_leaf)
  3. Ensure meta-features are computed on held-out fold predictions
  4. Consider stacking with out-of-fold predictions
```

### Quantum Simulator Too Slow
```
If simulation time exceeds practical limits:
  1. Reduce number of shots (start with 1024, increase if needed)
  2. Use statevector simulator for small circuits
  3. Switch to Aer qasm_simulator with noise model
  4. Consider running on real IBM Quantum hardware for final evaluation
```

## Best Practices

1. **Always use different learning mechanisms**: QSVM (kernel-based) and QNN (gradient-based) provide complementary decision boundaries
2. **Meta-features should capture disagreement**: The value of ensembling comes from models that make different errors
3. **Evaluate at low FPR thresholds**: IDS requires very low false positive rates; optimize for this regime
4. **Use multiple fusion representations**: Try probability stacking, voting, and meta-learning to find the best fusion strategy
5. **Document dataset dependencies**: Results vary significantly between TON IoT and CICIDS2017; report per-dataset performance
6. **Include classical baselines**: Compare against standalone classical models (RF, SVM, NN) to demonstrate quantum advantage

## Limitations

- Requires sufficient qubits for feature encoding (limited on NISQ devices)
- Meta-learner is classical; full quantum meta-learning is an open research direction
- Performance gains are dataset-dependent; not guaranteed on all IDS datasets
- Circuit depth and shot count trade off accuracy vs. runtime
- Class imbalance in IDS datasets requires careful handling before quantum encoding

## Resources

- **Paper**: arXiv:2605.28879 - "Meta-Quantum Ensemble Framework for Robust Network Intrusion Detection"
- **Qiskit ML**: https://qiskit.org/ecosystem/machine-learning/
- **TON IoT Dataset**: https://ieee-dataport.org/open-access/toniot-datasets
- **CICIDS2017**: https://www.unb.ca/cic/datasets/ids-2017.html

## Related Skills

- quantum-ml-patterns: Reusable patterns for QML research
- quantum-neural-architecture: QNN architecture design
- post-quantum-cryptographic-protocol-analysis: Post-quantum security analysis
- quantum-ml-robustness: QML model testing and robustness
