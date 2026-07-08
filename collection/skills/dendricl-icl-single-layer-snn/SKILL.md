---
name: dendricl-icl-single-layer-snn
description: >
  DendriCL methodology for dendritic in-context learning in single-layer spiking neural networks.
  The apical compartment's subthreshold dynamics implement online Widrow-Hoff LMS, enabling
  general-purpose ICL without attention, depth, or inference-time plasticity. First SNN to
  solve Garg-2022 ICL benchmark at d≥30 where Transformers fail.
  Trigger: dendritic computation, in-context learning SNN, compartmental neuron, online LMS,
  biological ICL, neuromorphic ICL, apical dendrite, single-layer learning
arxiv_id: "2607.02283v1"
date: "2026-07-02"
authors: "Juwei Shen, Yujie Wu, Changwen Chen (HK PolyU)"
categories: ["cs.NE", "cs.LG"]
tags: ["spiking neural network", "in-context learning", "dendritic computation", "compartmental neuron", "online LMS", "neuromorphic"]
---

# DendriCL: Dendritic In-Context Learning in a Single-Layer Spiking Neural Network

## Core Insight

In-context learning (ICL) does NOT require attention, depth, or inference-time plasticity. A single dendritic compartment with online-LMS dynamics is sufficient.

The subthreshold dynamics of a single apical dendritic compartment implement a complete online learning algorithm (leaky Widrow-Hoff LMS). By treating the compartment as the computational substrate rather than a passive conduit, ICL emerges from dynamics alone with frozen synaptic weights at inference.

## Architecture

Single-layer compartmental spiking network with d_model = 384 parallel pyramidal-like units:

```
Per-unit recurrence at context position t:
  uB(t) = WB * xt                    (basal projection)
  ŷt = uA(t)^T * WA * xt            (scalar prediction)
  et = (1 - flagt) * (yt - ŷt)      (gated error)
  uA(t+1) = α * uA(t) + γ * et * WA * xt   (apical online-LMS)
  vsoma(t) = gB * uB(t) + gA * WA,out * uA(t)  (somatic integration)
  s(t) = ⊮[vsoma(t) > θ]            (LIF spike, soft reset)
```

Key design choices:
- Apical state uA is NOT reset by somatic spikes — evolves continuously across full context
- Error et is gated OFF at query position
- All synaptic weights frozen at inference time
- ~0.75M total parameters, single layer

## Structural Equivalence: Apical ≡ Leaky Online LMS

When WA = I, the apical update reduces to:
```
ŵ_{t+1} = α * ŵ_t + γ * (yt - ŵ_t^T * xt) * xt
```
This is classical leaky Widrow-Hoff LMS. Under i.i.d. inputs and linear targets, E||uA(k) - w||² = O(d/k) — the classical LMS convergence theorem.

Linear probe recovers reference online-LMS trajectory from apical membrane at R² = 0.93, confirming the algorithm is structurally embedded in the dynamics.

## Key Results

### Garg-2022 ICL Benchmark
- **d=10**: DendriCL R² = 0.807 (competitive with all architectures)
- **d=20**: DendriCL R² = 0.820 (best spike-based model, within 3pp of non-spiking ablation)
- **d=30**: DendriCL R² = 0.807 (ONLY architecture maintaining >0.5)
- **d=40**: DendriCL R² = 0.787 (Transformers collapse to chance)
- **d=50**: DendriCL R² = 0.649 (all others at chance floor)

### Seed Stability
- DendriCL: σ ≤ 0.036 across entire super-d range (uniquely stable)
- Transformer: bimodal at d=30, collapses at d≥40 (architectural failure, not budget)
- Spikformer: degrades gracefully but trails by 0.17 at d=30

### Efficiency
- ~4× spike reduction over Pure LIF
- Projected ~10× Loihi-class energy advantage
- Architectural simplicity and inference-time efficiency co-vary (not trade off)

## Biological Grounding

- Three-compartment layout (apical-basal-soma) matches cortical layer-5 pyramidal neurons
- Apical compartment carries persistent multi-dimensional subthreshold voltage with calcium plateaus on 100+ ms timescales
- Consistent with predictive coding framework (apical = error-driven dynamics)
- Falsifiable hypothesis: in vivo recordings should reveal LMS-like dynamics in apical tufts

## Contrast with Prior Work

| Model | Apical Role | Adaptation Mechanism |
|-------|-------------|---------------------|
| Urbanczik-Senn 2014 | Teacher signal | Plasticity-driven |
| Sacramento 2018 | Backprop error | Plasticity-driven |
| Iyer 2022 (Active Dendrites) | External context gate | Plasticity-driven |
| Miconi 2018 | Differentiable plasticity | Hebbian fast weights |
| **DendriCL (Ours)** | **Online LMS estimator** | **Dynamics-driven, frozen weights** |

## Practical Applications

1. **Neuromorphic ICL**: Deploy in-context learning on Loihi/SpiNNaker without inference-time weight updates
2. **Energy-efficient adaptation**: Single-layer architecture enables ~10× energy savings
3. **Brain-inspired AI**: Demonstrates that biological dendritic computation is computationally sufficient for ICL
4. **Robust high-dimensional learning**: Only architecture seed-stable at d≥30
5. **Hardware-software co-design**: Compartmental dynamics map naturally to analog neuromorphic circuits

## Training Details

- BPTT from scratch, AdamW, lr=1e-3, weight decay 1e-4, cosine schedule
- Batch size 64, 10k steps (baseline) or 50k steps (compute-matched)
- LIF surrogate gradients: arctan approximation
- 3 seeds per config (5 seeds for d∈{20,30})
- No pre-training, no plasticity at inference

## Implications

1. ICL is a generic property of trained sequence models — now extended to spiking substrate
2. The "depth hypothesis" for ICL is wrong: a single compartment suffices
3. Dendritic computation is not just biologically plausible — it's computationally optimal for ICL
4. Opens path to fully neuromorphic in-context learning systems
