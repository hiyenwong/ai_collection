---
name: quantum-histopathologic-cancer-detection
category: ai_collection
description: |
  Quantum algorithms for histopathologic cancer detection using configurable dual-gradient
  CSWAP circuits (DG-CSWAP) and hardware-efficient destructive swap circuits (DG-DST).
  Covers NISQ-era quantum image classification with noise mitigation pipelines.
  From arXiv:2606.21752 (Goyal et al., 2026).
trigger_words:
  - quantum cancer detection
  - histopathologic quantum
  - DG-CSWAP
  - quantum histopathology
  - quantum image classification
  - quantum hardware medical
  - NISQ cancer detection
  - quantum edge detection
---

# Quantum Histopathologic Cancer Detection

## Paper
Configurable Algorithms for Histopathologic Cancer Detection on Quantum Hardware
arXiv: 2606.21752 (2026-06-19)
Authors: Nandika Goyal, Glen Uehara, Andreas Spanias

## Core Methodology

### 1. DG-CSWAP (Dual-Gradient Controlled-SWAP)
- Computes multi-directional edge responses in a single quantum circuit execution
- Uses per-pixel local Ry encoding to represent image features as qubit rotations
- Controlled-SWAP gates compare neighboring pixel quantum states to detect edges
- Single execution produces edge response in multiple directions simultaneously

### 2. DG-DST (Dual-Gradient Destructive Swap Test)
- Hardware-efficient alternative natively matched to QPU gate sets
- Algebraically equivalent to DG-CSWAP but with substantially lower circuit complexity
- Uses destructive swap test (no ancilla qubit needed) reducing qubit count
- Two-circuit validation strategy: run both DG-CSWAP and DG-DST on QPU and compare

### 3. NISQ Mitigation Pipeline (3-Stage)
- **Stage 1: Readout Error Correction** — Calibrate measurement errors via confusion matrix
- **Stage 2: Bias Subtraction** — Remove systematic hardware bias from results
- **Stage 3: Slope Regression** — Regress measured values against expected to correct scaling
- Combined effect: reduces single-pixel hardware MSE by ~8x

### 4. Validation Protocol
- Tested on 5 quantum processors via Amazon Braket
- Inter-platform Pearson r ~ 0.93-0.94 across simulator-hardware pairs
- 79.80% accuracy on PatchCamelyon dataset with single ResNet-50
- Compared to QFT baseline: uses fewer qubits, executes on real hardware

### 5. Lite Configuration
- Reduced preprocessing pipeline with 17x speedup
- Only 2.59% accuracy cost for significant time savings
- Trade-off between speed and accuracy configurable

## Implementation Patterns

### Pattern 1: Quantum Image Encoding
```
Image patch → ResNet-50 feature extraction → Per-pixel Ry encoding → Quantum state
```
- Classical CNN extracts features; quantum circuit processes local correlations
- Hybrid approach avoids full quantum state preparation overhead

### Pattern 2: Algebraic Equivalence Validation
```
DG-CSWAP(result1) == DG-DST(result2) [algebraically proven]
→ Run both on hardware → Compare → Validate hardware correctness
```
- Use proven algebraic equivalence as hardware validation tool
- If results diverge beyond noise, hardware has systematic issues

### Pattern 3: NISQ Mitigation Stack
```
Raw measurement → Readout correction → Bias subtraction → Slope regression → Clean result
```
- Layered mitigation: each stage addresses different error source
- Readout correction: measurement calibration
- Bias subtraction: systematic offset removal
- Slope regression: amplitude scaling correction

## Key Findings
- First quantum hardware implementation with noise mitigation for histopathologic classification
- 17x speedup possible with minimal accuracy loss (Lite config)
- Hardware-efficient destructive swap test matches CSWAP quality at lower complexity
- Multi-platform validation essential: different QPUs show consistent behavior (r > 0.93)

## Applicable To
- Medical image classification on NISQ hardware
- Quantum edge detection and feature extraction
- Hybrid quantum-classical medical diagnosis pipelines
- Benchmarking quantum image processing algorithms across platforms
- NISQ-era noise mitigation for medical applications

## Activation
quantum cancer, histopathologic quantum, DG-CSWAP, DG-DST, quantum medical image, quantum edge detection, NISQ medical, quantum histopathology, PatchCamelyon quantum, quantum hardware classification
