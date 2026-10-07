---
name: supermartingale-label-transition-qnn
description: "Use when QNNs train on small noisy-label medical datasets."
version: 1.0
author: hermes-cron
license: MIT
metadata:
  hermes:
    tags: [noisy-labels, quantum-neural-network, supermartingale, loss-correction]
    related_skills: [qml-colorectal-cancer-classification, hqnn-design-space-exploration]
---

# SLT: Supermartingale-based Label Transition for Robust QNN Medical Classification

## When to Use

- Training QNNs or hybrid quantum-classical models on small medical datasets (MedMNIST-scale) with possibly corrupted annotations
- Refining a noise-transition matrix without anchor points, when confidence-threshold updates oscillate
- Any setting where an auxiliary estimate is updated from model outputs and needs a stability gate

## Source

arXiv:2607.16293 (Jul 2026) — "SLT: Robust Quantum Neural Networks for Noisy-Label Medical Image Classification via Supermartingale-based Label Transition" (Zhuang, Hasan, Shi, Guan)

**Trigger keywords**: noisy-label QNN, label noise correction, supermartingale, anchor-free transition matrix, medical image classification noise, small-data quantum, F1 robustness, MedMNIST, loss correction convergence, entropy reduction stabilization

## Core Problem

Small medical datasets (MedMNIST-scale) amplify annotation errors. QNNs are attractive compact models for small-data regimes but their intrinsic "natural smoothness" (rooted in the Born rule) keeps predictive distributions smooth — obscuring the high-confidence samples needed for classic noise-transition estimation. Updating the transition matrix whenever the model looks locally confident causes noise-driven oscillation.

## Methodology

### Key insight: QNN smoothness as stabilizing bias
Classical DNNs sharpen predictions quickly (good for finding anchor samples, bad for stability). QNNs stay smooth longer. SLT inverts the framing: instead of fighting smoothness, use it to DELAY unreliable transition updates until entropy reduction is provably monotone.

### Supermartingale formulation

- Model the entropy-reduction process of predictive probabilities as a supermartingale: predictive entropy H(p_θ(x)) decreases as training converges; define the process so its conditional expectation is non-increasing (supermartingale property)
- Use the supermartingale's monotone behavior as a **stability criterion**: only refine the noise-transition matrix T at steps where the entropy process exhibits stable (monotone) descent
- This filters out noise-driven oscillations — dynamic transition updates happen only on stable refinement steps

### Anchor-free transition refinement pipeline

1. Train QNN (VQC-wrapped classical layers) on noisy labels with cross-entropy
2. Track predictive entropy across epochs; construct the entropy-reduction supermartingale
3. At stable refinement steps (monotone entropy descent), update transition matrix T using current high-confidence predictions
4. Apply forward loss correction with refined T: L = CE(T·p_θ(x), ỹ) — no anchor points required
5. Iterate; convergence to steady state is proven

### Convergence guarantee

The supermartingale-based transition-refinement process converges to a steady state — a stability-aware foundation distinguishing SLT from heuristic confidence-threshold schedulers.

## Results

- 5 MedMNIST datasets (Breast, Pneumonia, Retina, Derma, Blood), 3 noise types (uniform, cyclic-flipping, custom-mapping), ratios 10/30/50%
- Beats CE, Forward correction, and 6 anchor-free baselines (T-Revision, Dual-T, VolMinNet, TVR, BLTM, CCR) on most settings
- Severe noise (50%): Breast 52.24%, Pneumonia 83.90% F1 while CE/Forward degrade substantially
- Ablation: temperature scaling on classical NNs partially mimics QNN smoothness — confirming smoothness is the operative stabilizer, not quantum-specific computation

## Reusable Patterns

### Pattern 1: Stability-gated hyperparameter updates
When a training-time auxiliary estimate (noise transition, class prior, loss weights) is refined from model outputs, gate each refinement on a provable monotonicity condition (supermartingale descent of predictive entropy) rather than raw confidence thresholds. Confidence thresholds fire during noise oscillations; monotonicity gates wait for genuine stabilization.

### Pattern 2: Turn a model's weakness into a scheduling signal
QNN over-smoothness (Born-rule-induced) is usually a limitation for anchor-point selection. Repurpose it as a natural delay mechanism preventing premature overconfidence in weak-anchor selection. Generalize: identify which model property makes a standard technique fail, then use that property itself as the timing control for a safer variant.

### Pattern 3: Anchor-free noise estimation for low-data regimes
Anchor points (classes with near-100% predicted probability) rarely exist in small medical datasets. Estimate the transition matrix from aggregate high-confidence predictions at stability-gated steps instead of per-class anchors.

## Related Skills

- qml-colorectal-cancer-classification (clinical QNN)
- hqnn-design-space-exploration (HQNN architecture)
- self-supervised-confidence-efficiency (confidence-based training)
