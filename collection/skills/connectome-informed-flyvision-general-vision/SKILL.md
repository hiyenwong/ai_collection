---
name: connectome-informed-flyvision-general-vision
category: ai_collection
description: "果蝇视觉连接组作为CV归纳偏置: FlyVision用ON/OFF对偶stem+三阶段循环图混合, 3.7M参数逼近ResNet18."
tags: [connectomics, computer-vision, inductive-bias, drosophila, brain-inspired-architecture, neuromorphic]
---

# Connectome-Inspired FlyVision: From Drosophila Visual Connectome to General-Purpose Computer Vision

**Paper**: From the Drosophila Visual Connectome to General-Purpose Computer Vision (arXiv: 2610.08418, 6 Oct 2026)
**Authors**: Zongyu Li, Akito Yamauchi, Huaizhi Liu, Vishwanatha Rao, Jia Guo (Columbia / UPenn)
**Code**: ConnectomeX project (checkpoint-compatible PyTorch implementations)

## Core Thesis

Biological connectomes encode structured solutions to visual computation. ConnectomeX tests whether **abstractions of Drosophila optic-lobe circuit organization** (FlyWire: 139,255 neurons / 54.5M synapses; optic lobe: ~38,500 intrinsic neurons / 227 cell types) can serve as **reusable inductive biases for artificial vision** — outside the biological tasks and stimulus distributions they were measured for. Result: a conserved motif (parallel ON/OFF pathways + recurrent computation + population-level graph interaction) **scales from MNIST to ImageNet to medical imaging** with 3–4× fewer parameters than ResNet18.

## Architecture: The Conserved Connectome Motif

The backbone separates a **reusable connectome-informed computation core** from task-dependent input/output interfaces:

1. **Dual ON/OFF stem** (retina → lamina abstraction):
   - Surround `s` = per-channel spatial mean over the full image (global) or reflect-padded 7×7 local mean (local-k7)
   - ON response = `ReLU(x − s)`; OFF response = `ReLU(s − x)` — parallel contrast channels like fly ON/OFF pathways
   - "+ LF" variant: zero-initialized learnable 5×5 stride-2 conv of the surround map added to stem output (low-frequency pathway) — improved ImageNet top-1 from 66.25% → 66.53%
2. **Three recurrent graph-mixing stages** (medulla → lobula abstraction), each stage:
   - Feed-forward 3×3 conv + 3×3 **recurrent conv** (1–2 updates per stage; gated by learnable scalar gates) + **four-population graph mixer** (population-level interaction, from cell-type-structured connectivity)
   - GroupNorm + SiLU activation
   - Stage strides 1/2/2 (ImageNet) or 2/2/2 (radiography); recurrent-step config 1/2/2
3. **Adaptive global pooling → embedding → task head**
   - Compact: 16/32/64 channels → 64-d embedding; Base: 64/128/256 → 512-d; Large: 96/192/384 → 768-d
   - Checkpoint compatibility: the same 54-tensor state schema loads across tasks; only the classifier head is replaced

**Key design principle**: stride and recurrent-update count are **execution hyperparameters, not state tensors** — the same checkpoint can execute different forward schedules (how they run one backbone on both 224×224 ImageNet and radiography).

## Performance Map (parameter efficiency is the headline)

| Task | FlyVision | ResNet18 | Parameter ratio |
|------|-----------|----------|-----------------|
| MNIST | 99.34% @ 80,608 params | 99.22% @ 11.18M | **139×** fewer |
| CIFAR-10 | 78.03% @ 81,408 | 83.44% @ 11.18M | 138× fewer |
| ImageNet-1K top-1 | 66.53% (Large local-k7+LF, 3.7M) | 69.25% (11.7M) | ~3× fewer |
| ImageNet top-5 | 86.31% | — | |
| Skin disease (22-class) | 63.78% acc / 95.28% AUROC @ 2.99M | 66.19% / 95.96% @ 11.19M | ~3.7× fewer |
| Chest X-ray (4-class) | 92.76% @ 2.97M | 91.56% @ 11.18M | **exceeds ResNet18** with 3.8× fewer |
| BrainAGE (T1w MRI) | MAE 5.98 yrs, R²=0.868 | — | volumetric extension |

## BrainAGE Extension: 2D Encoder → Volumetric MRI

The ImageNet-pretrained 2D FlyVision Large encoder is reused for 3D T1w MRI without architectural change:
- Each volume → 24 slices (8 sagittal + 8 coronal + 8 axial)
- Each slice embedded independently by the shared encoder
- Slice-level age predictions fused **within and across anatomical views** by confidence-modulated Gaussian voting
- Held-out 433 scans: three-axis fusion MAE 5.98 years, R² = 0.868 — a multi-view route from a 2D pretrained encoder to scan-level regression

## Methodological Lessons (Why This Pattern Generalizes)

1. **Circuit-organization abstraction > biofidelic replication**: the model keeps parallel channels / recurrent loops / population interaction — the **computational motif** — not neuron-level wiring. Motifs proved portable across stimulus domains the fly never saw (radiographs, MRI).
2. **Capacity scaling within a fixed motif**: widen channels (16→384) while the three-stage recurrent-graph structure stays frozen; the motif is capacity-independent.
3. **Transfer is architecture-dependent** (honest negative results):
   - MNIST→CIFAR: FlyVision −0.41 pts (P=0.664, n.s.); ResNet18 −0.97 pts (P=0.034); LeNet +1.84 (P<0.001) — same source init helps one architecture and hurts another
   - Direct ImageNet init on ResNet18: +2.40 pts. Transfer direction/magnitude **varies per source-target-architecture combination**; never assume a pretrained backbone transfers.
4. **Biomedical edge**: on chest radiography FlyVision *exceeded* ResNet18 with 3.8× fewer parameters; hierarchical analysis localized residual error to normal-vs-disease routing (the clinically hard boundary), not within-disease confusion.
5. **Audit-first benchmarking**: skin-disease split was SHA-256 content-audited — 306 duplicate-content groups, 37 contradictory-label groups, 63 train/test leaks quarantined before evaluation. Reusable protocol for any Kaggle-derived medical benchmark.

## Implementation Recipe

```
# Conserved motif (PyTorch-like pseudocode)
x = input
s = surround(x, mode='global' | 'local_k7')
on  = relu(x - s);  off = relu(s - x)
h = stem([on, off])                      # dual branch
for stage in [S1, S2, S3]:                # widths e.g. 96/192/384
    for r in range(n_recur[stage]):       # 1-2 gated updates
        h = h + gate_r * conv3x3_recurrent(h)
    h = graph_mixer(h, populations=4)    # population-level interaction
    h = silu(groupnorm(h))
    h = downsample(h, stride[stage])
emb = adaptive_pool(h) -> head
```
Training: AdamW lr=1e-3, cosine decay, label smoothing 0.1, RandAugment, BF16, grad-clip 5 (FlyVision only), 90 epochs ImageNet.

## Reuse Triggers

- Designing compact vision backbones under parameter/memory budget (edge, medical screening)
- Testing whether a biological circuit motif (connectome, cortical column) is computationally useful — use this "motif abstraction + capacity scaling + cross-domain ladder" protocol
- Extending 2D pretrained encoders to volumetric medical imaging via multi-view slice fusion
- Needing honest transfer analysis: paired per-image predictions + exact McNemar + Holm adjustment, never aggregate accuracy alone

## Related Skills

- [[boundary-preserving-null-connectome]] — connectome null models
- [[brain-alignment-causal-dissociation-attention-heads]] — brain-guided architecture evaluation
- [[gnn-transformer-fusion]] — graph+Euclidean fusion architectures
