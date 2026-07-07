---
name: dendricl-icl-single-layer-snn
description: "DendriCL: Single-layer compartmental SNN achieving in-context learning via apical dendrite online-LMS dynamics. First SNN to solve Garg-2022 ICL benchmark at super-dimensional task spaces where Transformers fail. (arXiv:2607.02283)"
tags: [spiking-neural-network, in-context-learning, dendritic-computation, neuromorphic, biological-plausibility, online-learning, compartmental-model]
---

# DendriCL: Dendritic In-Context Learning in Single-Layer SNN

## Paper Reference
- **Title**: Dendritic In-Context Learning in a Single-Layer Spiking Neural Network
- **Authors**: Juwei Shen, Yujie Wu, Changwen Chen (Hong Kong Polytechnic University)
- **arXiv**: 2607.02283 (July 2026)
- **Key Contribution**: First single-layer SNN achieving general-purpose ICL on Garg-2022 benchmark

## Core Innovation

### The Problem
In-context learning (ICL) — solving new tasks from labeled examples in the prompt without parameter updates — had not been demonstrated in SNNs on the Garg-2022 benchmark. Existing SNNs (Spikformer, Pure LIF, LSNN, Spiking SSMs) collapse at task dimension d ≥ 20.

### Root Cause Analysis
Prior SNN designs route adaptation through **inference-time synaptic plasticity**, treating dendrites as passive conduits for error/teacher signals. This is structurally unnecessary.

### The Solution: DendriCL
A single-layer compartmental spiking architecture where:
- **Apical dendrite** = active online estimator (not passive conduit)
- **Subthreshold dynamics** implement leaky online Widrow-Hoff LMS
- **All synaptic weights frozen at inference** — adaptation is purely dynamical

## Architecture Details

### Three-Compartment Design (Biologically Grounded)
Based on cortical layer-5 pyramidal neurons:

```
Apical Dendrite (uA ∈ ℝ³⁸⁴)
  ↓ Online LMS: uA(t+1) = α·uA(t) + γ·et·WA·xt
  ↓ where et = (1-flagt)·(yt - ŷt)
  
Soma (LIF integration)
  ↓ vsoma = gB·uB + gA·WA,out·uA
  ↓ Spike if vsoma > θ, soft reset
  
Basal Dendrite (uB)
  ↓ Feedforward: uB = WB·xt
```

### Key Equations
1. **Basal projection**: uB(t) = WB·xt
2. **Prediction**: ŷt = uA(t)ᵀ·WA·xt
3. **Gated error**: et = (1 - flagt)·(yt - ŷt)
4. **Apical online-LMS**: uA(t+1) = α·uA(t) + γ·et·WA·xt
5. **Somatic integration**: vsoma(t) = gB·uB(t) + gA·WA,out·uA(t)
6. **LIF spike**: s(t) = ⊮[vsoma(t) > θ], vsoma ← vsoma - θ·s(t)

### Critical Design Choices
- **Apical state NOT reset by spikes** — evolves continuously across full context
- **Error gated at query position** — no learning signal during query
- **All parameters trained by BPTT** — no inference-time updates
- **dmodel = dapical = 384**, ~0.75M total parameters

## Theoretical Foundation

### Apical ≡ Leaky Online LMS (Proposition 1)
Setting WA = I, the apical update reduces to classical leaky Widrow-Hoff LMS:
```
ŵt+1 = α·ŵt + γ·(yt - ŵtᵀ·xt)·xt
```

Under i.i.d. inputs xt ~ N(0, Id) and targets yt = wᵀxt + εt:
- Convergence: E‖uA(k) - w‖² = O(d/k)
- This is the classical LMS convergence theorem
- **Contribution**: The update is embedded in compartmental architecture; BPTT tunes (α, γ, WA) to make the built-in rule optimal

### Mechanistic Verification
Linear probe recovers reference online-LMS trajectory from apical membrane:
- **R² = 0.93** — algorithm is structurally embedded in dynamics, not implicitly discovered

## Experimental Results

### Garg-2022 ICL Benchmark Performance

#### At d = 10 (low dimension):
- DendriCL: R² = 0.807 ± 0.005
- Transformer: R² = 0.996
- Spikformer: R² = 0.977
- Pure LIF: R² = 0.801
- **All architectures perform well at low d**

#### At d = 20 (critical threshold):
- **DendriCL: R² = 0.820 ± 0.005** (best SNN)
- Transformer: R² = 0.989
- Spikformer: R² = 0.724 ± 0.059
- Pure LIF: R² = 0.086 (collapsed)
- Active Dendrites: R² = 0.061 ± 0.018 (collapsed)
- LSNN: R² = 0.008 ± 0.002 (collapsed)
- **Clean bifurcation**: ICL-capable (≥0.72) vs collapsed (≤0.09)

#### Super-dimensional regime (d = 25-50):
**DendriCL is uniquely seed-stable:**

| d | DendriCL (50k) | Transformer (50k) | Spikformer (50k) |
|---|----------------|-------------------|------------------|
| 25 | 0.809 ± 0.010 | 0.991 ± 0.002 | 0.641 ± 0.028 |
| 30 | 0.807 ± 0.005 | 0.386 ± 0.479† | 0.637 ± 0.015 |
| 40 | 0.787 ± 0.005 | 0.009 ± 0.001 | 0.412 ± 0.031 |
| 50 | 0.649 ± 0.036 | 0.008 ± 0.001 | 0.239 ± 0.042 |

†Transformer bimodal at d=30: 3/6 seeds at R² ≤ 0.012, 2 at R² ≈ 0.98

**Key Finding**: Transformer collapses to chance from d=30 onward (architectural limit, not budget-induced). DendriCL maintains σ ≤ 0.036 across entire super-d range.

### Efficiency Gains
- **~4× spike reduction** over Pure LIF
- **Projected ~10× Loihi-class energy advantage**
- Architectural simplicity and efficiency co-vary (not trade off)

## Biological Plausibility

### Anatomical Grounding
- **Layer-5 pyramidal neurons**: Apical tuft receives top-down feedback, basal dendrites receive bottom-up input
- **Persistent subthreshold voltage**: Calcium plateaus on 100+ ms timescales (Larkum et al., 1999, 2002; Gidon et al., 2020)
- **Predictive coding consistency**: Apical compartment as error-driven dynamics aligns with Rao & Ballard (1999), Bastos et al. (2012)

### Contrast with Prior Compartmental Models

| Model | Apical Role | Adaptation Mechanism |
|-------|-------------|---------------------|
| Urbanczik-Senn 2014 | Teacher signal | Plasticity-driven |
| Sacramento 2018 | Backprop error | Plasticity-driven |
| Iyer 2022 (Active Dendrites) | External context gate | Plasticity-driven |
| **DendriCL (Ours)** | **Online LMS estimator** | **Dynamics-driven, frozen weights** |

## Implementation Guide

### Training Setup
- **Optimizer**: AdamW, lr=10⁻³, weight decay 10⁻⁴, cosine schedule
- **Batch size**: 64
- **Steps**: 10k (baseline) or 50k (compute-matched)
- **Seeds**: 3 per config (5 seeds for d ∈ {20, 30})
- **Surrogate gradients**: Arctan approximation for LIF
- **No pre-training, no inference-time plasticity**

### Task Protocol (Garg-2022)
- Linear regression: d ∈ {5, 10, 15, 20, 25, 30, 40, 50}, k = 2d context pairs
- Binary classification: d = 10, k = 20
- 2-layer ReLU NN regression: d = 20, k = 40
- Each minibatch samples fresh task parameter w ~ N(0, Id), fresh context, fresh query
- Loss computed only at query position

### Key Hyperparameters
- α (apical decay): learned
- γ (learning rate): learned
- WA, WB (projections): learned
- gA, gB (somatic gains): learned
- θ (spike threshold): learned
- dmodel = dapical = 384

## Pitfalls and Limitations

### Rigor Caveat
- Theoretical analysis covers apical compartment (purely linear)
- LIF reset introduces nonlinearity not formally handled by theorem
- Empirical probe (R² = 0.93) establishes correspondence holds despite nonlinearity

### Scope Exclusions
- **Excludes inference-time plasticity SNNs**: e-prop, differentiable plasticity, IP²-RSNN, STDP-based methods, hardware-local-rule learning
- These solve complementary problem (cheap parameter updates at inference)
- DendriCL focuses on dynamics-only adaptation with frozen weights

### When to Use DendriCL
✅ **Use when**:
- Need biologically plausible ICL
- Targeting neuromorphic hardware (Loihi, SpiNNaker)
- Energy efficiency critical
- Task dimension d ≥ 20 (where other SNNs fail)
- Want seed-stable performance at super-d

❌ **Don't use when**:
- Maximum accuracy required (Transformer still better at low d)
- Need attention-based interpretability
- Task requires deep hierarchical processing

## Research Implications

### Theoretical
- ICL requires **neither attention, depth, nor inference-time plasticity**
- Single compartment with online-LMS dynamics is sufficient
- Extends "dynamics-as-algorithm" theorems to spiking substrate

### Practical
- First ICL setting where architectural simplicity and efficiency co-vary
- Enables energy-efficient neuromorphic ICL implementations
- Opens door to biologically plausible continual learning

### Biological Hypothesis
- Apical dendrites may implement online parameter estimation in vivo
- Testable prediction: cortical layer-5 neurons should exhibit LMS-like dynamics
- Falsifiable by future in vivo recordings

## Related Work Context

### Implicit-GD Lineage
- Akyürek et al. (2023): Transformers recover GD iterates
- von Oswald et al. (2023): Linear self-attention ≡ one GD step
- Ahn et al. (2024): Preconditioned GD
- Sushma et al. (2024): State-space models
- Park et al. (2024): Mamba
- Tong & Pehlevan (2025): MLPs
- **DendriCL**: Spiking substrate analog

### Compartmental Models
- Urbanczik & Senn (2014): Apical = teacher
- Sacramento et al. (2018): Apical = backprop error
- Miconi et al. (2018): Differentiable plasticity
- Bellec et al. (2018): LSNN (adaptive threshold)
- Iyer et al. (2022): Active Dendrites (context gates)
- **DendriCL**: Apical = online estimator (dynamics, not plasticity)

## Activation Triggers
Use this skill when working on:
- Spiking neural networks (SNNs)
- In-context learning (ICL) mechanisms
- Dendritic computation models
- Neuromorphic computing
- Biological plausibility in deep learning
- Compartmental neuron models
- Online learning algorithms
- Garg-2022 benchmark
- Energy-efficient AI
- Brain-inspired architectures

## Code and Resources
- **Paper**: https://arxiv.org/abs/2607.02283
- **PDF**: https://arxiv.org/pdf/2607.02283.pdf
- **Key Figures**: Architecture diagram (Fig 2), performance comparison (Table 1, 2), apical-LMS probe (Fig 4)
- **Parameter count**: ~0.75M (competitive with baselines)

## Citation
```bibtex
@article{shen2026dendricl,
  title={Dendritic In-Context Learning in a Single-Layer Spiking Neural Network},
  author={Shen, Juwei and Wu, Yujie and Chen, Changwen},
  journal={arXiv preprint arXiv:2607.02283},
  year={2026}
}
```
