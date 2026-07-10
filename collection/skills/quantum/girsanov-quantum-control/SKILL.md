---
name: girsanov-quantum-control
description: Girsanov's theorem path-space regularization methodology for robust open quantum control. Bridges stochastic calculus (Girsanov theorem) with quantum optimal control, penalizing observable consequences of control on decoherence channels rather than control amplitude. Applicable to quantum control, stochastic control, RL.
category: quantum
trigger_words: ["girsanov quantum control", "path-space regularization", "open quantum control", "decoherence robust control", "KL divergence quantum trajectories", "quantum control stochastic calculus"]
---

# Girsanov's Theorem Path-Space Regularization for Open Quantum Control

## Core Idea

Use **Girsanov's theorem** from stochastic calculus to construct **closed-form, differentiable estimators of KL divergence between quantum trajectory distributions**, then use these as regularizers for robust quantum control under decoherence.

## Key Insight

Open quantum systems under continuous monitoring generate classical measurement records whose **drift depends on the noise experienced by the system**. The records of two evolutions sharing the same decoherence channels differ **only in this drift**, so Girsanov's theorem yields a closed-form KL divergence estimator between their trajectory distributions.

## Methodology

### Step 1: Define Reference Measures
- **Wiener KL (KL_W)**: More effective under certain noise model conditions
- **Drift-Variance Regularizer (R_DV)**: Works for all noise models

### Step 2: Apply as Control Regularizer
- Both regularizers drive the system toward states where **decoherence effects are minimal**
- They penalize the **observable consequences** of control on decoherence channels (not control amplitude itself)
- Qualitatively distinct from existing penalties on control fluence or smoothness

### Step 3: Optimize
- Use gradient-based optimization with the Girsanov-based regularizers
- Outperform unregularized gradient-based and RL baselines

## Results

- Reduce infidelity by up to **50%**
- Robustness to noise model mismatch: gains grow from **+17 pp at training noise to +27 pp under 2.5x noise mismatch**
- ~16% gains on calibrated IBM Kingston multi-qubit chain

## Trigger Conditions

- Designing quantum control protocols in presence of decoherence
- Need for robust quantum control under uncertain/noisy environments
- Open quantum systems with continuous monitoring
- Applying stochastic calculus techniques to quantum control problems
- RL or gradient-based quantum control optimization

## Pitfalls

- Wiener KL regularizer may not work optimally for all noise models — use R_DV as fallback
- Requires accurate characterization of decoherence channels
- Reference measure must be physically motivated for best results

## Verification

- Compare regularized vs unregularized control fidelity
- Test robustness under mismatched noise models (increase noise by 2-2.5x)
- Verify system does not occupy forbidden states during control

## References

- arXiv:2606.19947 - QMaxCal: Path-Space Regularization for Open Quantum Control via Girsanov's Theorem
- Authors: Merijn Moody, Zier Mensch, Miranda C. N. Cheng, Peter G. Bolhuis, Max Welling
