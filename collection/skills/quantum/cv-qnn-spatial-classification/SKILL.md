---
name: cv-qnn-spatial-classification
description: Controlled comparison methodology showing continuous-variable (CV) QNNs outperform discrete-variable (DV) QNNs on spatial pattern recognition tasks like wafer-map defect classification.
category: quantum-ml
trigger_words: ["CV versus DV", "continuous variable QNN", "discrete variable QNN", "wafer map classification", "quantum spatial encoding", "CV advantage", "Fock cutoff"]
---

# CV versus DV Quantum Neural Networks: Spatial Classification

**Paper**: arXiv:2607.00961v1
**Authors**: Yeonhong Kim, Jonghyeok Im, Monu Nath Baitha, Kyoungsik Kim

## Core Insight

Under controlled conditions, **CV-QNNs consistently outperform DV-QNNs** on spatial pattern recognition tasks. At 4 qumodes/qubits, CV reaches 79.7% accuracy vs DV's 61.6% — an 18-point gap.

## Key Results

1. **CV Advantage**: Sharpest on spatially localized classes (Edge-Loc recall 0.66 vs DV ≤0.05)
2. **Representational Ceiling**: DV limitation is capacity-bound, not optimization failure
3. **Structured Encoding**: CV's continuous phase-space encoding captures fine spatial distinctions
4. **Hardware Validation**: DV accuracy holds at shallow depth, degrades at deepest circuits

## Methodology

### Controlled Architecture
- Shared convolutional backbone (~4.3M params)
- Interchangeable heads: classical dense, CV-QNN, DV-QNN
- Scaled over 3 sizes (3, 4, 8 qumodes/qubits)

### Encoding Strategy
- CV: structured neural-network-analogue layer + continuous phase-space
- DV: Hilbert space dimensionality with Fock cutoff d=2

## Applications

- **Industrial QA**: Wafer-level defect screening for semiconductor yield
- **Pattern Recognition**: Tasks requiring fine spatial distinction
- **Quantum Advantage Search**: Identifying where structured quantum heads help
