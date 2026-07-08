---
name: cv-photonic-qnn-edge-ai
description: Parameter-efficient continuous-variable photonic quantum neural networks for edge AI — simplified Φ∘D∘U₁ architecture that cuts trainable parameters 40-45% while matching or exceeding full layer performance.
category: quantum-ml
trigger_words: ["photonic QNN", "continuous variable edge AI", "parameter efficient quantum", "oral cancer detection", "Kerr gates", "barren plateau mitigation", "simplified CV layer"]
---

# Parameter-Efficient CV Photonic QNN for Edge AI

**Paper**: arXiv:2606.28252v1
**Authors**: Akshay Bhagwan Sonawane, Sophie Choe, Lakshman Tamil

## Core Insight

A **simplified Φ∘D∘U₁ CV-QNN architecture** cuts trainable parameters 40-45% relative to standard Killoran et al. layers while matching or exceeding performance, enabling room-temperature quantum ML for edge deployment.

## Key Results

1. **18-Parameter Model**: 4-qumode simplified CV-QNN achieves highest validation AUC
2. **67% Fewer Params**: Outperforms 55-parameter classical baseline
3. **100% Test Accuracy**: Calibrated test accuracy across all seeds
4. **Barren Plateau Mitigation**: Dimensionality reduction + encoding restriction raise gradient variance by ~58 orders of magnitude

## Architecture

### Simplified Layer
```
Φ ∘ D ∘ U₁
```
- Φ: Nonlinearity (Kerr gates)
- D: Displacement gates
- U₁: Single-mode interferometric operations

### Pipeline
1. MobileNetV1 feature extraction
2. PCA to 16 dimensions
3. CV-QNN with displacement, interferometric, Kerr gates
4. Photonic backend (room temperature)

## Performance Trade-offs
- **2 qumodes**: Full layer has small but significant edge
- **4 qumodes**: Simplified layer significantly better with 44% fewer params

## Applications

- **Edge Medical AI**: Smartphone-based cancer screening
- **Parameter-Efficient Learning**: Quantum models for resource-constrained deployment
- **Room-Temperature Quantum Computing**: Photonic alternatives to cryogenic systems
