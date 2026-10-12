---
name: lora-nca-regulatory-handles
description: Use for low-rank (LoRA) control of NCA morphogenesis. Maps D'Arcy Thompson transformations to reusable regulatory weight-space hyper-directions.
category: ai_collection
version: 1.0.0
tags:
  - neural-cellular-automata
  - lora
  - morphogenesis
  - evo-devo
  - phenotypic-variation
  - low-rank-adaptation
  - morphospace
trigger_words:
  - neural cellular automata LoRA
  - morphogenesis control
  - phenotypic variation regulatory
  - D'Arcy Thompson transformation
  - weight-space hyper-directions
  - morphospace navigation
author: Benedikt Hartl, Milton L. Montero, Marcello Barylli, Sebastian Risi, Michael Levin
arxiv_id: "2609.29755"
date_added: "2026-09-27"
---

# LoRA-NCA: Reusable Regulatory Handles Control Phenotypic Variation

Methodology from arXiv:2609.29755 — "On Growth and Form, and Function: Reusable Regulatory Handles Control Phenotypic Variation" (Hartl, Montero, Barylli, Risi, Levin; Tufts Allen Discovery Center + ITU Copenhagen + Sakana AI, Sep 2026). Use when controlling morphology/phenotype transformations of self-organizing systems via low-rank weight modulations, or when searching for compact control handles in developmental/regulatory dynamics.

## Core Question (D'Arcy Thompson's Inverse Problem)

D'Arcy Thompson (1917) showed related species' anatomies are connected by simple grid transformations (e.g., porcupinefish → sunfish). But he left a century-old inverse problem: **if two anatomies are related by a grid transformation, what is the corresponding modulation of the developmental dynamics that physically generate them?**

Answer: In Neural Cellular Automata (NCAs) used as "minimal cybernetic tissue", Thompson's transformations are **low-dimensional directions (hyper-directions) in the regulatory weight space** — compact, reusable, composable interventions that redirect development without micromanaging cellular trajectories.

## Architecture: NCA as Regulatory Substrate

- **Growing NCA**: M×M grid (67×67) of cells, each with state vector x_i ∈ R^32 (RGBA + hidden channels), updated by a **shared 2-layer ANN** (H1=96, output=C=32; ≈12,416 parameters θ0).
- **Perception**: 3×3 Moore neighborhood filtered by identity + Sobel(Sx) + Sobel(Sy) kernels → p_i ∈ R^96.
- **Residual update**: `x_i^(t+1) = x_i^t + f_θ(X_i^t)`, with stochastic binary update mask (asynchrony → robustness).
- **Training objective**: `θ_Y = argmin_θ E_{T~U{TD±ΔD}, m} ||X̃^T − Y||²_F` — grows target Y from single seed cell, evaluated at random developmental time T.
- **Biological mapping**: cell state ≈ physiological state; shared ANN ≈ gene-regulatory network (GRN) coordinating local decisions toward a collective morphology.

## Method 1: Transformation-Conditional LoRA Mapping

Map a parametric phenotypic transformation T(s) to weight modulations of the frozen scaffold W0:

```
W_T(s) = W0 + ΔW_T(s),   ΔW_T(s) = Σ_k β(s_k) A_k B_k
```

- Train adapters {A_k, B_k} (rank r per layer) for each transformation Tk; linear coefficients β encode intervention strength.
- **Symmetric scaling parametrization**: `β(s_k) = β0·log(s_k/s0)` — reciprocal scaling is symmetric (d_k^±1 → ±β0·log d_k), and s_k=s0 → β=0 leaves the NCA unchanged.
- **Result**: rank-one adapters Δ_x, Δ_y (320 params = 2.6% of total) implement x/y scaling for 25 scaling combinations (25–49 px), **generalize to out-of-distribution scales s'∈[15,57]**, and compose with phenotype-specific adapters.

## Method 2: Shared-Scaffold Multi-Target Training (the reference frame)

Independently trained NCAs have incompatible weights (gauge symmetries). Fix: jointly train **one shared scaffold θ0 + Nϕ target-specific LoRAs**:

```
W(k') = W0 + ΔW_{k'} ,  ΔW_{k'} = A_{k'} B_{k'}   (one-hot/Kronecker-δ activation)
E_T = (1/Nϕ) Σ_{k'} ||X̃^T(k') − Y^{k'}||²  (jointly optimize θ0 AND all adapters)
```

Trained with Nϕ = 120 (then 25,000) emoji targets sharing frozen scaffold W0 (rank-16 adapters).

**Zero-shot transfer**: the scale hyper-directions Δ_x, Δ_y learned on ONE phenotype (blue fish) apply zero-shot to **all** phenotypes with the same scaffold — different fish, lizard, fire extinguisher — preserving internal features while rescaling global shape (anisotropic scaling also produces effective shear).

**Closed-form composition**:
```
W^{xy}(k'; s_x, s_y) = W0 + Σ_k δ_{kk'} ΔW_k + β(s_x)Δ_x + β(s_y)Δ_y
```

## Method 3: Empirical Discovery of Semantic Hyper-Directions (PCA over 25k adapters)

From ≈25,000 phenotype-specific LoRA-NCAs (rank 16, shared scaffold), **PCA on full effective weight modulations ΔW_φ = A_φ B_φ** (concatenated & standardized — NOT raw LoRA factors, which yield limited structure):

- **PC0 ↔ horizontal extent**: r(PC0, x) = −0.71 (cross-correlation with y only 0.07)
- **PC1 ↔ vertical extent**: r(PC1, y) = −0.73
- Adding ±β·ΔW_PC0 to ANY phenotype's weights compresses/stretches x-extent parametrically (also affects brightness — features are entangled).
- **Style direction**: mean translation ΔW_open = ⟨ΔW⟩_OpenMoji − ⟨ΔW⟩_others transfers OpenMoji's black-outline style while preserving baseline features (cosine ≈0.1 to PC0/PC1 despite size effect).
- **Fission direction**: ΔW_F = ⟨ΔW⟩_split − ⟨ΔW⟩_non-split causes symmetric vertical splitting (β≳2), or fusion in −ΔW_F direction.

## Key Findings

1. **Rank-one suffices for scaling** (2.6% of parameters) — coherent macroscopic transformation needs only a minimal regulatory displacement.
2. **Universal hyper-directions of scale** transfer zero-shot across morphologies sharing the scaffold → adapters are compositional, not memorizing phenotype features.
3. **Degeneracy of morphogenetic control (poly-computing)**: learned Δ_x,y and PCA-derived PC0/PC1 both control extent but have only ≈0.1 cosine similarity — distinct directions in weight space produce the same macroscopic transformation. Multiple functional organizations coexist as overlapping control handles.
4. **Pattee's multiscale control handles realized**: macroscopic change without micromanaging microscopic degrees of freedom.
5. **Facilitated variation made computational**: conserved regulatory dynamics + compact reusable modulations = a small action space for evolution; handles are retained/reused/recombined (combinatorial evolvability advantage over point mutation).
6. **Negative result (honest)**: mapping regenerative capabilities from regenerative→non-regenerative NCAs did NOT yield a generalizable hyper-direction (Section A.5).

## Implementation Notes

- Loss: pixel MSE for training, LPIPS perceptual loss for evaluation (MSE mostly tracks size, not semantic accuracy).
- 16 stochastic rollouts per configuration for evaluation.
- PCA axes must be mapped from standardized coordinates back to original weight coordinates before intervention.
- LoRA on both hidden and output layers, same rank; perception block can also be LoRA'd (conv/attention kernels).
- Reference frame matters: hyper-directions only transfer within the same scaffold W0.

## Application Directions

1. **Bioengineering/regeneration**: identify GRN/bioelectric-network hyper-directions equivalent to morphallactic regenerative control; redirect developmental attractors (wound→limb regeneration, cancer as loss of system-level control, aging/rejuvenation).
2. **Anatomical compiler**: conditional generative AI producing tailored developmental programs from target-spec prompts (Thompson's inverse problem as text-to-morphology).
3. **Evolvability research**: stacked LoRA hyper-directions as a testbed for whether recombination of existing capabilities outpaces point-mutation search.
4. **Any self-organizing multi-agent system**: compact, transferable control handles for redirecting collective outcomes without micro-management.

## Related Work

- [[brain-inspired-nca]] — NCA morphogenesis basics
- [[low-rank-rnn-learning-dynamics]] — low-rank structure in recurrent dynamics
- [[heterogeneity-sr-liquid-computing]] — other NCA-adjacent dynamical substrates

## Source

arXiv:2609.29755 — https://arxiv.org/abs/2609.29755
