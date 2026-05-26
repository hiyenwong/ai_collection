---
name: adaptive-hybrid-feature-fusion-medical
description: "Adaptive Hybrid Quantum-Classical Feature Fusion methodology for medical image classification. Learns optimal complementarity between quantum and classical features through adaptive weighting. Activation: adaptive hybrid feature fusion, quantum classical complementarity, medical image quantum fusion, HQNN feature fusion, quantum classical integration medical."
---

# Adaptive Hybrid Quantum-Classical Feature Fusion for Medical Classification

Methodology for integrating quantum machine learning with classical deep learning through adaptive feature fusion for medical image analysis.

## Core Concept

The integration of QML with classical deep learning offers promising avenues by mapping data into high-dimensional Hilbert spaces. However, effectively leveraging the complementarity of quantum and classical features requires adaptive fusion mechanisms.

## Architecture

### Dual Feature Extraction

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class DualFeatureExtractor(nn.Module):
    """Extract features from both classical and quantum pathways."""
    
    def __init__(self, classical_dim=256, quantum_dim=16):
        super().__init__()
        # Classical CNN pathway
        self.classical_extractor = nn.Sequential(
            nn.Conv2d(3, 64, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(64, 128, 3, padding=1),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d(1),
            nn.Flatten(),
            nn.Linear(128, classical_dim)
        )
        
        # Quantum feature extraction (simulated)
        self.quantum_dim = quantum_dim
        
    def forward(self, x):
        # Classical features
        classical_feat = self.classical_extractor(x)
        
        # Quantum features (placeholder for actual quantum circuit)
        # In practice: encode classical_feat into quantum circuit
        quantum_feat = self.quantum_encoding(classical_feat)
        
        return classical_feat, quantum_feat
```

### Adaptive Fusion Module

```python
class AdaptiveFeatureFusion(nn.Module):
    """Adaptively weight quantum and classical features."""
    
    def __init__(self, classical_dim, quantum_dim, hidden_dim=64):
        super().__init__()
        self.gate = nn.Sequential(
            nn.Linear(classical_dim + quantum_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 2),
            nn.Softmax(dim=1)
        )
        self.classical_proj = nn.Linear(classical_dim, hidden_dim)
        self.quantum_proj = nn.Linear(quantum_dim, hidden_dim)
        
    def forward(self, classical_feat, quantum_feat):
        # Compute adaptive weights
        combined = torch.cat([classical_feat, quantum_feat], dim=1)
        weights = self.gate(combined)  # [batch, 2]
        
        # Project features
        c_proj = self.classical_proj(classical_feat)
        q_proj = self.quantum_proj(quantum_feat)
        
        # Weighted fusion
        fused = weights[:, 0:1] * c_proj + weights[:, 1:2] * q_proj
        return fused, weights
```

### Full Model

```python
class HybridMedicalClassifier(nn.Module):
    def __init__(self, num_classes, classical_dim=256, quantum_dim=16):
        super().__init__()
        self.feature_extractor = DualFeatureExtractor(classical_dim, quantum_dim)
        self.fusion = AdaptiveFeatureFusion(classical_dim, quantum_dim)
        self.classifier = nn.Linear(64, num_classes)
        
    def forward(self, x):
        classical_feat, quantum_feat = self.feature_extractor(x)
        fused, weights = self.fusion(classical_feat, quantum_feat)
        logits = self.classifier(fused)
        return logits, weights
```

## Three Progressive Fusion Strategies

The paper introduces three strategies of increasing sophistication:

| Strategy | Approach | Training Mode | Performance on BreastMNIST |
|----------|----------|--------------|---------------------------|
| **SHF** (Static Hybrid Fusion) | Offline feature extraction | Two-stage training | Baseline |
| **DHF** (Dynamic Hybrid Fusion) | End-to-end co-adaptation | Joint training | Improved |
| **TSHF** (Temperature-Scaled Hybrid Fusion) | Learnable scalar τ balancing | Joint + adaptive | **Best: 87.82% acc, 91.77% F1, 89.08% AUC-ROC** |

### TSHF Core Mechanism
TSHF introduces a learnable scalar τ that dynamically balances quantum and classical branch contributions:
- Solves the optimization asymmetry where classical gradients overwhelm quantum gradients
- τ adapts during training to find optimal balance point
- ResNet backbone + trainable quantum circuit achieves peak performance

## Workflow

1. **Data Preparation**:
   - Collect medical images (e.g., thermographic, X-ray, MRI)
   - Split into train/val/test sets
   - Apply standard augmentations

2. **Feature Extraction**:
   - Train classical CNN backbone (ResNet-18 recommended)
   - Extract quantum features via 4-qubit variational circuit with strongly entangling layers
   - Use pre-trained encoders when available

3. **Fusion Strategy Selection**:
   - Start with SHF for baseline (offline extraction)
   - Move to DHF for end-to-end training
   - Use TSHF for best results (learnable τ balances branches)

4. **Adaptive Fusion Training**:
   - For TSHF: initialize τ and learn end-to-end
   - Monitor τ evolution — indicates which branch dominates
   - Track both branch gradient magnitudes for asymmetry detection

5. **Analysis**:
   - Analyze learned weights per sample/class
   - Identify when quantum features dominate
   - Identify when classical features dominate
   - Report TSHF τ final value as interpretability metric

## Parameters

- **Classical Dimension**: 128-512 (depends on CNN architecture)
- **Quantum Dimension**: 8-32 (number of qubits/encoding dimension)
- **Hidden Dimension**: 64-128 for fusion
- **Learning Rate**: 1e-3 with cosine decay
- **Batch Size**: 16-32 (medical images)

## Advantages

- **Adaptive**: Learns optimal feature weighting per sample
- **Complementarity**: Exploits strengths of both paradigms
- **Interpretable**: Fusion weights reveal feature importance
- **Robust**: Graceful degradation if one pathway fails

## Use Cases

- Breast cancer thermographic classification
- Medical image diagnosis
- Pathology image analysis
- Radiology image classification
- Multi-modal medical fusion

## Limitations

- Requires quantum simulator or access to quantum hardware
- Quantum feature extraction can be slow on simulators
- Fusion weights may need careful regularization

## References

- Sobrinho et al. (2026). "On the Complementarity of Quantum and Classical Features: Adaptive Hybrid Quantum-Classical Feature Fusion for Breast Cancer Classification" (arXiv:2604.22903)

## Related Skills

- hybrid-quantum-classical-architecture
- quantum-medical-imaging
- quantum-classical-hybrid-nn
