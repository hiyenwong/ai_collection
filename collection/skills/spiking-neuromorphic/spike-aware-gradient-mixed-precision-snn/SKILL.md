---
name: spike-aware-gradient-mixed-precision-snn
description: Use when assigning mixed-precision bits to SNN layers.
category: ai_collection
version: 1.0
author: hermes-dl-cron
license: MIT
trigger: SNN quantization, mixed precision bit allocation, Fisher sensitivity, membrane threshold margin, HAWQ alternative, spiking neural network compression, neuromorphic deployment
arxiv: "2610.30339"
---

# Spike-Aware Gradient-Based Mixed-Precision Quantization of SNNs

arXiv 2610.30339.

## When to Use
Use when quantizing spiking neural networks to mixed precision under a global bit budget — especially when Hessian-based methods (HAWQ-V2) are too expensive due to temporal unrolling across timesteps.

## Problem
HAWQ-V2-style Hessian trace estimation requires Hessian-vector products unrolled over ALL SNN timesteps — huge memory and compute. Need first-order sensitivity matching Hessian accuracy at a fraction of the cost.

## Method

### 1. Fisher-weighted perturbation energy (first-order sensitivity)
Empirical diagonal Fisher: F_ii ≈ E[g_i²], g_i = ∂L/∂w_i — one backward pass on a calibration set.
Layer sensitivity = Fisher-weighted quantization perturbation energy:
Ω_l = Σ_i g_{l,i}²·(Δw_{l,i})², Δw = quantized − fp weight at the candidate bit-width.
Normalized (removes layer scale bias): S_l = Σ_i g²Δw² / (Σ_i g² + ε).
Theory anchor: ΔL ≈ ½ Σ H_ii(Δw_i)² with per-layer decomposition H_ii = α_l·F_ii + R_i — the Fisher term is the cheap proxy; α_l and residual R never need computing.

### 2. Spike-aware threshold margin
Per-neuron per-timestep membrane threshold margin, measured during the SAME calibration forward pass:
d_{j,t} = |V_th − V_{j,t}| / V_th.
Layer margin: m_l = (1/NT)·Σ_t Σ_j d_{j,t}, normalized to [0,1].
Small margin ⇒ membrane potential near the firing threshold ⇒ a small weight perturbation can FLIP spike generation ⇒ quantize conservatively.
Protection factor: P_l = 1 + β·(1 − m_l).

### 3. Greedy bit allocation
min Σ_l S_l(b_l) subject to Σ n_l·b_l ≤ B, b_l ∈ candidate set (e.g. {8,4}).
Initialize all layers at max precision; repeatedly reduce the layer minimizing sensitivity increase per bit saved:
l* = argmin_l [ΔS_l·P_l / (n_l·Δb)], ΔS_l = S_l(b_l−Δb) − S_l(b_l).
Loop until the target average bit-width B. All S_l computed ONCE from a single backward pass — the greedy loop is pure arithmetic.

## Results
- ResNet-34 / ImageNet (PASCAL-converted, T=8): 73.30% at 6.70 avg bits (HAWQ-V2: 73.14%) — 4.78× compression
- Bit-allocation cost: 13.38 s vs 22 min 23.5 s (≈100× faster); peak GPU memory 11.3 GB vs 26.1 GB (−56.9%)
- VGG/ResNet/ViT SNNs across QCFS and PASCAL (ANN→SNN) and TET (direct training), SpikeZip-TF ViTs; CIFAR-10/100, ImageNet, CIFAR10-DVS
- SpikeZip-TF ResNet-18 (T=64): 94.52% vs HAWQ-V2 93.60% (+0.92)
- Accuracy curves within 0.05% of HAWQ-V2 across the whole bit-width range on VGG-16/CIFAR-10

## Reusable patterns
1. First-order Fisher sensitivity as a Hessian proxy — Ω = Σ g²Δw² normalized by Σg²; applicable to ANY architecture where second-order costs dominate (RNNs, temporally unrolled nets).
2. Domain-specific vulnerability margin — SNNs use membrane-threshold distance; other domains can substitute their own distance-to-discontinuity statistic into the protection factor P = 1 + β(1−m).
3. Greedy cost-per-bit allocation — ΔS·P/(n·Δb) is a knapsack-style heuristic requiring sensitivities only at candidate bit-widths, computed once.

## Related
HAWQ-V2 (Hessian trace), SpikeZip-TF, QCFS, PASCAL, TET; distinct from spikeq-spike-guided-ptq-snn (PTQ level selection via flipped spikes) — this skill covers training-aware per-layer BIT-WIDTH allocation.
