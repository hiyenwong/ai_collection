---
name: gsap-gated-spike-axial-propagation
description: Use when building spike-native token interactions in SNNs.
---

# GSAP: Gated Spike Axial Propagation — Rethinking Pairwise Token Interaction in Spiking Transformers

**Paper**: arXiv:2609.26297 (Shen, Zhao, Li, Yu, Zhang, Xing, Zhang, Zhang — Inst. Automation CAS / CEBSIT / Zhongguancun Academy, 22 Sep 2026)

## Core Idea

Conventional Spiking Transformers (Spikformer's SSA, Spiking Attention) inherit the **pairwise query–key matching** paradigm from Transformers. But binary spike representations make Q·K matching produce highly sparse, input-dependent, coincidence-gated interaction patterns — long-range communication becomes hostage to the instantaneous availability of matching spike events.

**GSAP decouples information propagation from context selection**: propagate first, select second.

## Three Parallel Pathways

Input: spike representation `S ∈ {0,1}^{T×B×C×H×W}`

1. **Propagation pathway (global context)**
   - `F = SN_feat(P_feat(S))` — pointwise projection + spiking neuron
   - `H = SN_h(P_h(F) + F)` — horizontal spatial aggregation with spike re-encoding (preserves membrane temporal states)
   - `M = P_v(H)` — vertical spatial aggregation
   - Long-range reach via sequential axial aggregation, no explicit source–receiver affinities.

2. **Selection pathway (receiver-conditioned gate)**
   - `G = SN_sel(P_sel(S))` — binary gate from the *receiver-side* representation
   - `M̃ = G ⊙ M` — each token regulates how much propagated context it incorporates, according to its own state
   - Key contrast: attention couples communication and selection via affinity; GSAP separates them.

3. **Local pathway**
   - `L = D_3×3(S)` — depthwise 3×3 conv on spike representation
   - `Z = S + L + M̃`; `X_out = P_out(SN_fuse(Norm_fuse(Z)))` — fuse identity + local + selected global.

## Key Results (all with fewer parameters than baselines)

| Task | Baseline | Result |
|------|----------|--------|
| ImageNet-1K (Spikingformer-8-384/512/768) | 72.45 / 74.79 / 75.85% | **73.29 / 76.07 / 78.19%** |
| CIFAR-100 (Spikingformer) | 79.21% | **80.21%** (params 9.36M → 8.84M) |
| CIFAR-100 (QKFormer) | 81.15% | **81.64%** |
| ADE20K semantic segmentation | — | 66.84% single-stage / 66.65% hierarchical |
| PASCAL VOC (QKFormer) | 32.63 mIoU | **36.90 mIoU**; Spikingformer 31.64 → 33.82 |
| Event-based N-Caltech101 | 84.45% | **85.54%** |
| OTTT online learning (CIFAR-100, OTTT-A) | Spiking Attention | **>10 percentage points gain**; higher cross-step gradient cosine similarity |

## Mechanistic Insight (Why It Works)

- **Online learning (OTTT) stability**: In Spiking Attention, multiplicative sparse-spike terms suppress learning signals → gradient directions fluctuate across timesteps → poor gradient accumulation. GSAP's structured spatial propagation avoids pairwise spike matching → consistent cross-step gradients (higher cosine similarity between consecutive-step gradients).
- **Token-perturbation analysis**: long-range propagation coexists with spatially localised sensitivity — broad communication + selective utilisation, not diffuse mixing.

## Design Principles Extracted

1. Spike-native interaction should exploit **temporal membrane states + sparse events**, not mimic dense attention.
2. **Axial propagation + receiver gating** gives O(H+W) token reach without affinity matrices (vs O(HW) for pairwise attention).
3. Spiking neurons placed *between* aggregation stages re-encode context and inject temporal dynamics into global aggregation.
4. Decoupling propagation from selection parallels neuromodulatory information routing vs point-to-point synaptic QK matching.
5. For online/temporal-local learning rules (OTTT), choose interaction mechanisms with **stable gradient flow across timesteps** — this can matter more than raw offline accuracy.

## When to Use
- Designing Spiking Transformer token-mixing blocks (replacement for SSA/Spiking Attention).
- Event-based vision (DVS) models needing global context without quadratic spike-matching.
- Online-learning SNNs (OTTT-family) where gradient consistency matters.
- Energy/latency-constrained deployment: spike-driven computation, fewer params than attention baselines.

## Relationship to Existing Skills
- Extends `attention-mechanisms` family: axial propagation ≈ AxialAttention made spike-driven; receiver gating ≈ dynamic attention gating.
- Complements `wta-spiking-transformer-language` and `spiking-transformer-effective-dimension`: those keep pairwise interaction; GSAP replaces it.
- Contrast with `stdp-spiking-transformer-attention` (S²TDPT): STDP local learning vs GSAP architectural interaction change.

## Reproducibility
- Code included in supplementary material; GSAP integrates by replacing only the token interaction module, backbone unchanged.

## Limitations
- ImageNet gains concentrated in mid/large backbones; very small models less conclusive.
- Receiver-gate ablation shows gating sometimes *reduces* OTTT stability (ungated variant isolates propagation effect) — gating benefits offline representation, propagation benefits online learning; choose per setting.
