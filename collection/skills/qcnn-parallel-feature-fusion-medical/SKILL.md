---
name: qcnn-parallel-feature-fusion-medical
description: "Parallel multi-circuit quantum feature fusion methodology for medical image classification. Use when: (1) building hybrid quantum-classical CNN architectures for biomedical image classification, (2) comparing quantum vs classical models with statistical rigor (Wilcoxon signed-rank test, Cohen's d effect size), (3) designing parallel quantum encoding circuits (amplitude + angle encoding simultaneously), (4) parameter-matched fairness evaluation for QML vs classical baselines. Covers QCNN architecture pattern, dual-encoding VQC fusion, and NISQ-era validation framework."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2512.02066"
  published: "2025-11-29"
  authors: "Ece Yurtseven"
  tags: [quantum, medical, qcnn, feature-fusion, statistical-validation, breast-cancer, breastmnist]
---

# Parallel Multi-Circuit Quantum Feature Fusion for Medical Imaging

## Core Methodology

Hybrid QCNN architecture that runs **two distinct quantum circuits in parallel**:
- **Amplitude-encoding VQC** — encodes classical features as quantum state amplitudes
- **Angle-encoding VQC with circular entanglement** — encodes features as rotation angles with ring topology entanglement

Both operate on 4 qubits. Their quantum feature embeddings are fused with classical convolutional features into a joint feature space, then processed by a fully connected classifier.

## Key Innovation: Statistical Validation Framework

Establishes rigorous statistical comparison between hybrid quantum and classical models:

1. **Parameter matching** — quantum and classical models have matched parameter counts to isolate quantum contribution
2. **Multiple independent runs** — 5 independent training runs for statistical significance
3. **Wilcoxon signed-rank test** — non-parametric test (p = 0.03125) confirms significance
4. **Cohen's d effect size** — large effect (d = 2.14) confirms practical significance, not just statistical

## Architecture Pattern

```
Input Image → Classical Conv Layers → Feature Maps
                                         ↓
                    ┌────────────────────┼────────────────────┐
                    ↓                    ↓                    ↓
          Amplitude-Enc VQC      Angle-Enc VQC          Classical Features
          (4 qubits, 4 qubits)   (circular entang.)     (conv outputs)
                    ↓                    ↓                    ↓
              Quantum Emb 1        Quantum Emb 2         Classical Vectors
                    └────────────────────┼────────────────────┘
                                         ↓
                              Joint Feature Space
                                         ↓
                              Fully Connected Classifier
                                         ↓
                              Binary Classification
```

## When to Use This Skill

- Medical image classification tasks with limited data (BreastMNIST, ChestX-ray, etc.)
- NISQ-era experiments with 4-8 qubits
- Need statistically validated quantum advantage claims
- Comparing QML models against classical baselines with fair parameter budgets
- Building hybrid architectures that fuse multiple encoding strategies

## Implementation Steps

### Step 1: Classical Feature Extraction
```python
# Standard CNN backbone (parameter-matched to baseline)
class ConvBackbone(nn.Module):
    def __init__(self, base_params=50000):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 16, 3, padding=1)
        self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
        self.pool = nn.AdaptiveAvgPool2d((4, 4))
        # Parameter count must match classical baseline
```

### Step 2: Parallel Quantum Circuits
```python
# Amplitude encoding VQC
def amplitude_encoding_vqc(features, n_qubits=4):
    # Encode classical features as quantum amplitudes
    # Apply variational layers
    return quantum_state_measurements

# Angle encoding VQC with circular entanglement
def angle_encoding_vqc(features, n_qubits=4):
    # Encode features as rotation angles (RY gates)
    # Apply circular (ring) entanglement pattern
    # Apply variational layers
    return quantum_state_measurements
```

### Step 3: Feature Fusion & Classification
```python
def forward(x):
    classical_features = conv_backbone(x)
    quantum_amp = amplitude_encoding_vqc(classical_features)
    quantum_angle = angle_encoding_vqc(classical_features)
    
    # Fuse all embeddings
    joint = torch.cat([classical_features.flatten(), 
                       quantum_amp, quantum_angle], dim=1)
    return classifier(joint)
```

### Step 4: Statistical Validation
```python
from scipy import stats
import numpy as np

# After 5+ independent runs with same seed splits
quantum_accs = [acc1, acc2, acc3, acc4, acc5]
classical_accs = [acc1, acc2, acc3, acc4, acc5]

# Wilcoxon signed-rank test (paired, one-sided)
stat, p_value = stats.wilcoxon(quantum_accs, classical_accs, 
                                alternative='greater')

# Cohen's d effect size
d = (np.mean(quantum_accs) - np.mean(classical_accs)) / pooled_std

# Report: p < 0.05 and d > 0.8 (large) = statistically and practically significant
```

## Error Handling

### Quantum Advantage Not Significant
- Check parameter matching — quantum model must not have more trainable parameters
- Increase number of independent runs (5 minimum, 10 recommended)
- Try different encoding strategies (this paper shows angle+amplitude fusion works)
- Consider dataset size — small datasets may not show advantage

### NISQ Hardware Limitations
- 4-qubit circuits are NISQ-friendly; scale cautiously
- Use noise mitigation if deploying on real hardware
- Simulation first, then validate on hardware

### Parameter Matching Pitfall
- Count ALL trainable parameters including quantum gate angles
- Classical baseline should have same total parameter budget
- Document the matching methodology for reproducibility

## Verified Results
- Dataset: BreastMNIST (binary benign/malignant classification)
- Hybrid QCNN: Statistically significant improvement over parameter-matched CNN
- p = 0.03125 (Wilcoxon, one-sided)
- Cohen's d = 2.14 (large effect size)
- Published: QCNC 2026

## Activation Keywords
- qcnn parallel feature fusion
- quantum feature fusion medical
- statistical validation quantum ml
- wilcoxon quantum advantage
- cohen d quantum classification
- amplitude angle encoding fusion
- breastmnist quantum classification
- parameter matched quantum baseline
- parallel vqc medical imaging
