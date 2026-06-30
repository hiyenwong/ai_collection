---
name: qdp-quantum-differential-privacy
description: "Differential privacy analysis for quantum machine learning models — DP-SGD application to hybrid variational QML, gradient clipping bounds, and quantum noise vs calibrated noise analysis."
---

# QDP Quantum Differential Privacy

## Description
Methodology for applying differential privacy (DP) to quantum machine learning (QML) models. Analyzes the interplay between gradient clipping and calibrated noise addition in DP-SGD for hybrid variational quantum models with classical inputs and outputs. Demonstrates that quantum noise does NOT provide a satisfactory replacement for calibrated noise in DP-SGD, and shows how deterministic bounds on gradient norms for quantum models translate into explicit control of clipping bias.

## Activation Keywords
- quantum differential privacy
- quantum DP-SGD
- private quantum training
- differentially private QML
- quantum gradient clipping
- 量子差分隐私
- 私有量子训练
- DP-SGD quantum

## Core Concepts

### Key Finding: Quantum Noise ≠ DP Noise
Quantum hardware noise (decoherence, gate errors) does NOT provide formal differential privacy guarantees because:
1. Quantum noise is uncalibrated and data-independent
2. DP requires calibrated, data-dependent noise addition
3. Hardware noise cannot be tuned to match a specific privacy budget (ε, δ)

### DP-SGD for Hybrid QML
Standard DP-SGD pipeline applied to hybrid quantum-classical models:
1. **Gradient Clipping**: Clip per-sample gradients to bound sensitivity
2. **Noise Addition**: Add calibrated Gaussian noise to batch gradients
3. **Privacy Accounting**: Track cumulative privacy loss via composition theorems

### Gradient Norm Bounds for Quantum Models
For parameterized quantum circuits (PQCs) with bounded generator norms:
- Deterministic bounds on gradient norms exist for wide class of quantum models
- These bounds translate into **explicit control of clipping bias**
- When clipping threshold τ ≥ max gradient norm, clipping bias = 0 (no bias introduced)
- This is a key advantage over classical models where gradient norms are unbounded

### Privacy-Utility Tradeoff Protocol
Under fixed clipping threshold τ and privacy budget (ε, δ):
1. Train equivalent quantum and classical models
2. Quantum models retain higher accuracy in private-training regimes
3. The formal privacy guarantee is ensured by the classical DP-SGD mechanism, not by quantum noise

## Usage Patterns

### Pattern 1: DP-SGD Analysis for QML
When analyzing privacy of quantum machine learning models:
1. Identify the hybrid architecture (classical input → quantum circuit → classical output)
2. Determine gradient computation method (parameter-shift, finite difference, etc.)
3. Apply DP-SGD with appropriate clipping threshold
4. Account for privacy using advanced composition (Rényi DP or Gaussian DP)
5. Compare quantum vs classical model accuracy under same privacy budget

### Pattern 2: Gradient Norm Bounding
For parameterized quantum circuits:
1. Compute generator norms for each parameterized gate
2. Derive deterministic upper bound on gradient norm: ||∇L|| ≤ 2 Σ ||H_i||
3. Set clipping threshold τ ≥ bound to avoid clipping bias
4. If τ < bound, analyze clipping bias as function of τ

### Pattern 3: Privacy Budget Allocation
For multi-round QML training:
1. Define total privacy budget (ε, δ)
2. Allocate noise scale σ based on number of training steps T
3. Use moments accountant for tight privacy accounting
4. Monitor accuracy degradation as function of σ

## Instructions for Agents

### Step 1: Model Architecture Analysis
- Identify whether model is fully quantum, hybrid, or classical baseline
- Determine input/output modalities (classical vs quantum data)
- Note the number of trainable parameters and circuit depth

### Step 2: DP Mechanism Selection
- For hybrid models with classical I/O: DP-SGD is applicable
- For fully quantum models: consider quantum differential privacy (QDP) formalisms
- Always use classical DP mechanism for formal guarantees

### Step 3: Gradient Clipping Strategy
- Compute theoretical gradient norm bounds for the quantum circuit
- Set clipping threshold based on bounds (avoid over-clipping)
- Monitor actual gradient norms during training to validate bounds

### Step 4: Privacy Accounting
- Use standard DP accounting libraries (Opacus, TensorFlow Privacy)
- For hybrid models, account for classical DP-SGD mechanism
- Track both per-step and cumulative privacy loss

### Step 5: Empirical Evaluation
- Compare quantum vs classical model accuracy under same privacy budget
- Evaluate on both synthetic and real-world datasets
- Report accuracy gap as function of privacy budget ε

## Error Handling

### Clipping Bias Too High
- Symptom: Model accuracy degrades significantly with DP
- Fix: Increase clipping threshold τ or reduce model sensitivity
- Verify gradient norm bounds are correct

### Privacy Budget Exceeded
- Symptom: Training stops before convergence due to privacy budget
- Fix: Increase batch size (reduces noise scale), use advanced composition
- Consider privacy amplification via subsampling

### Quantum Hardware Noise Interference
- Symptom: Hardware noise obscures DP noise effects
- Fix: Use noiseless simulator for DP analysis; hardware noise is separate concern
- Do NOT conflate hardware noise with DP-calibrated noise

## Resources
- arXiv: 2606.29293 "Private training in quantum machine learning"
- DP-SGD original paper: Abadi et al. (2016)
- Quantum gradient bounds: Holmes et al. (2022)

## Related Skills
- `quantum-ml-certified-training` - Certified training for QML
- `quantum-ml-robustness` - QML robustness analysis
- `qml-framework-agnostic-design` - Framework-agnostic QML design
