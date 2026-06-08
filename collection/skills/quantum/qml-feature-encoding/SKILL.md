---
name: qml-feature-encoding
description: "Quantum Machine Learning feature encoding methodology — three-axis cost-expressivity-robustness taxonomy, depth-fidelity bounds under NISQ decoherence, unified trainability analysis, and five-regime decision framework for selecting encoding strategies on real hardware."
---

# QML Feature Encoding

## Description
Quantum Machine Learning feature encoding methodology based on systematic review of 66 primary works (2017-2026). Provides a three-axis taxonomy (cost-expressivity-robustness), closed-form depth-fidelity bounds under NISQ decoherence channels, unified trainability analysis linking Fourier expressivity/barren-plateau/kernel concentration, and a five-regime decision framework mapping (feature dimension, qubit budget, error rate, task type) to hardware-grounded encoding recommendations.

## Activation Keywords
- quantum feature encoding
- qml data encoding
- quantum data loading
- amplitude encoding
- angle encoding
- quantum machine learning encoding
- 量子特征编码
- 量子数据编码
- qml encoding strategy
- NISQ encoding

## Tools Used
- terminal: Run quantum circuit simulations
- web_search: Find encoding literature
- browser: Access quantum computing platforms

## Usage Patterns

### Pattern 1: Encoding Selection on NISQ Hardware
Given device parameters (D=feature dimension, n=qubits, p=error rate, τ=task type):
1. Check if p >= 10^-3 → use shallow angle-based encoding
2. If p < 10^-3 and n >= log2(D) → amplitude encoding viable
3. For classification tasks → IQP encoding
4. For regression → data re-uploading

### Pattern 2: Trainability Analysis
For a given encoding circuit:
1. Compute Fourier expressivity as function of encoding depth
2. Estimate barren-plateau onset via gradient variance scaling
3. Check quantum kernel concentration via spectral norm
4. If all three pass → encoding is trainable

### Pattern 3: Depth-Fidelity Bound
Given gate error rate p and circuit depth d:
- Critical threshold: p* ~ 10^-3
- If p >= p*: fidelity degrades exponentially with depth
- Recommendation: keep depth < O(1/p)

## Instructions for Agents

### Step 1: Characterize the Problem
Determine:
- Feature dimension D
- Available qubits n
- Hardware error rate p (from calibration data)
- Task type τ (classification, regression, clustering)

### Step 2: Apply Five-Regime Decision Framework
| Regime | Conditions | Recommended Encoding |
|--------|-----------|---------------------|
| 1 | p >= 10^-3, D small | Shangle encoding |
| 2 | p >= 10^-3, D large | Dense-angle encoding |
| 3 | p < 10^-3, n >= log2(D) | Amplitude encoding |
| 4 | p < 10^-3, n < log2(D) | Data re-uploading |
| 5 | Any p, structured data | IQP encoding |

### Step 3: Verify Trainability
Before committing to encoding:
1. Check Fourier spectrum coverage
2. Verify gradient doesn't vanish (barren plateau check)
3. Ensure kernel matrix isn't concentrated

### Step 4: Optimize Circuit Depth
Minimize depth while maintaining expressivity:
- Use basis encoding for binary features (depth=0)
- Use angle encoding for continuous (depth=D)
- Avoid deep amplitude encoding on NISQ

## Error Handling

### Amplitude Encoding on Noisy Hardware
If p >= 10^-3 and amplitude encoding chosen:
- Expect exponential fidelity decay
- Fall back to angle encoding with depth O(D)
- Trade qubit advantage for noise robustness

### Barren Plateau Detected
If gradients vanish exponentially:
- Reduce encoding depth
- Try local cost functions
- Use layerwise training

## Resources
- arXiv: 2606.05387 — "Feature Encoding in Quantum Machine Learning: A Survey and Practical Guidelines"
- PRISMA-adapted protocol for systematic QML encoding review
