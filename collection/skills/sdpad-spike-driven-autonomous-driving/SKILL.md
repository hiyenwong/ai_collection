---
name: sdpad-spike-driven-autonomous-driving
description: "SDPAD fully spike-driven end-to-end autonomous driving planner: integer ANN2SNN conversion, Spike-3D-Lift with spike-driven-max replacing softmax depth distribution, Spike-QFormer query decoder, deformable spike-cross-attention. 69.9 mJ energy (<2% of ANN planners), 86.3 PDMS on NAVSIM. Use when building neuromorphic/edge planners, converting BEV lifting to spike arithmetic, or deploying SNN planning on embedded hardware."
---

# SDPAD: Fully Spike-Driven End-to-End Autonomous Driving

**Source**: arXiv:2610.11583 — "SDPAD: A Fully Spike-Driven Pipeline for End-to-End Autonomous Driving" (Zhang, Zhang, Yang, Sawan — Westlake University / CenBRAIN Neurotech, 2026-10-08)

## Core Thesis

First **fully spike-driven** perception-to-planning pipeline for autonomous driving, closing the SNN-vs-ANN planning-accuracy gap while consuming **<2% of ANN baseline energy**. Every operation is gated by integer spikes; inference is a **single feed-forward pass with zero temporal simulation loops** (the classic SNN latency killer is eliminated by parallelized conversion).

## Architectural Pipeline

```
6-cam images → E-Spikeformer backbone (integer ANN2SNN converted)
            → Spike-3D-Lift (spike-driven-max depth → BEV lifting)
            → Spiking BEV representation
            ├→ Spike-SegHead (semantic seg)   ┐ aux supervision
            ├→ Spike-AgentHead (3D det)       ┘
            └→ Spike-QFormer: ego/agent/map queries distilled from BEV
               → waypoint queries fuse via spiking cross-attention
               → 3-mode reference curve + Deformable Spike-Cross-Attention
               → Spike-MLP → ego trajectory
```

## Key Mechanisms

### 1. Integer ANN2SNN conversion (no temporal unrolling at inference)
- I-LIF neuron, soft reset: `U[t]=H[t−1]+X[t]`, `S[t]=θ(U[t]−V_th)`, `H[t]=U[t]−V_th·S[t]`.
- Rate coding over window T with quantized-clip activation: `a_l^T = (1/T)·⌊clip(U^l, 0, T)⌉` — the source ANN is trained with this quantized activation to minimize conversion gap.
- **Parallelization trick**: accumulated potential `U^l = H^l[0] + (W^l/T)·Σ_t S^{l−1}[t]` means all T spike decisions reduce to threshold comparisons `S^l[t] = θ(U^l − V_th·t)` — computable in one pass, so **T is a quantization hyperparameter, not a simulation loop**.

### 2. Spike-Driven-Max (SDM) — the softmax-free depth distribution
The LSS-style BEV lift normally needs a dense floating-point softmax depth distribution (hardware-hostile). SDM:
- Round+clip depth to discrete spike intensities: `D̂ = ⌊clip(D, D_min, D_max)⌉` (STE for gradients).
- Exponential mapping for non-linear depth significance: `M = D̂ · 2^(D̂−D_max)`.
- Learnable normalization: `N = D_max + softplus(α)`; final `S_D = max(M, ε)/N` — a *sparse discrete spike state*, not a probability vector.
- Frustum membrane potential `V_F = P(S_D) ⊗ P(I)` → matmul degenerates to **spike-gated accumulation** (accumulation replaces multiply on neuromorphic hardware).
- BEV sampling: radial/Cartesian projection + bilinear interpolation of `V_F` + I-LIF firing → Spiking BEV.
- Ablation vs alternatives: SDM cuts FLOPs 23.6% (45.96→35.13 MFLOPs) vs softmax while keeping mIoU 36.60%/mAP 13.94% and best planning L2; SparseMax and raw I-LIF are cheaper but destroy perception fidelity (I-LIF collapses to 17.48% mIoU, propagating into planning safety).

### 3. Spike-QFormer — query-based planning decoder, spiking
- Unified **spiking attention primitive** with NO softmax: `SA(X_q, X_kv) = SN(Q̃ K̃ᵀ Ṽ · 2v_scale) W_o`, where Q̃/K̃/Ṽ are integer spike tensors (SN applied before AND after each projection). Matmuls of spike tensors = spike-gated accumulation; exponentiation/division entirely removed.
- **Multi-source queries**: ego query (1), agent queries (N_a=30), map queries — learnable embeddings extracting from 10×10 downsampled BEV + status token (CAN-bus ⊕ one-hot command, `v_status = W_s[c_can; c_cmd]`) via 3 stacked spiking decoder layers (self-attn + cross-attn + spike MLP).
- **Waypoint queries** fuse the three groups via single-layer spiking cross-attention → command-conditioned trajectory candidates.
- **Deformable Spike-Cross-Attention (SCA)**: refinement anchored to predicted trajectory anchors — aggregates multi-scale BEV features at trajectory-relevant locations.

### 4. Training
- ANN perception stack pre-trained → converted; aux supervision: BEV segmentation + agent-state (contributes ~1% PDMS on NAVSIM). Losses: trajectory regression + segmentation + detection.

## Results

| Benchmark | Metric | SDPAD | Reference |
|---|---|---|---|
| nuScenes open-loop | avg L2 / collision | **0.40 m / 0.12%** | on par with strong ANN planners (SAD was the SNN baseline) |
| nuScenes energy | inference | **69.9 mJ** | <2% of recent ANN baselines |
| NAVSIM navtest closed-loop | PDMS | **86.3** | +4.3 over SNN planner SAD; matches mainstream ANN planners |

Ablations (decoder components, L2/collision @3s):
- Map-only baseline: 0.98 m / 0.44% → +Ego: 0.97 → +Agent: 0.70 → Ego+Agent w/o Map: 0.67 → full E+M+A: 0.66 m / 0.30% → +Deformable SCA: **0.64 m / 0.26%** (params 39M vs 35M).
- **Quantization steps T (2→8)**: L2 5.32→0.64 m, collision 6.12%→0.26%; energy *decreases* slightly 84.73→69.93 mJ because coarser quantization fires denser spikes — finer T = sparser firing. Important scaling insight: T trades accuracy for spike sparsity, not energy monotonically.

## Why This Matters / When to Use

- **Edge/embedded deployment blueprint**: single-pass integer-spike inference eliminates the temporal-loop latency objection to SNNs in real-time control.
- **Softmax replacement pattern**: SDM shows how to convert any probabilistic-attention lifting (depth distributions, BEV frustums) into spike-gated accumulation without collapsing fidelity — the pattern generalizes to other geometric lifting ops.
- **Query-based decoders transfer to spikes**: Q-Former-style heterogeneous aggregation (ego/agent/map) survives spiking attention with no softmax — multimodal scene interaction is no longer an SNN bottleneck.
- **Honest negative/limitation notes**: relies on ANN pre-training + conversion (not direct surrogate-gradient training); evaluated at 69.9 mJ estimate; authors flag on-chip neuromorphic deployment + direct training as future work.
- Related: Spikformer/Spike-driven Transformer (attention without softmax), SAD (prior SNN planner), UniAD/VAD (ANN planners), LSS (BEV lifting).

**Activation keywords**: spiking neural network, autonomous driving, end-to-end planning, BEV lifting, spike-driven attention, ANN-to-SNN conversion, quantized-clip activation, neuromorphic hardware, energy efficiency, NAVSIM, nuScenes, PDMS, deformable attention, query decoder, edge deployment, integer arithmetic, rate coding, single-pass inference
