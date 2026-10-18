---
name: sam-guided-epr-snn-continual
description: Spike-saliency patch replay for SNN continual learning.
category: ai_collection
---

# Saliency-Guided Experience Packing Replay for Continual Learning in Deep SNNs

**Paper**: Saliency-Guided Replay for Continual Learning in Deep Spiking Neural Networks
**arXiv**: 2610.17998 (Panetta, Di Valerio — Sapienza Rome; Proietti — Goethe Frankfurt; 13 Oct 2026)
**Categories**: cs.LG, cs.AI, cs.CV, cs.NE
**Claim to novelty**: first use of explainable AI (XAI) to guide replay-based continual learning in spiking neural networks — prior SNN replay work (Proietti et al. 2023 experience replay; Dequino et al. 2024 compressed latent replay) stored full samples or latents without saliency selection.

## When to Use

- Building continual-learning pipelines for deep SNNs (VGG9/ResNet-style, BNTT-stabilized) under memory budgets, e.g. neuromorphic edge devices
- Adapting ANN saliency-guided replay (EPR, Grad-CAM variants) to event-driven/spiking models where gradients are non-differentiable
- Designing forward-only explainability for SNNs (no backward passes) that doubles as a functional exemplar-selection signal
- Studying explanation drift across sequential tasks (what saliency maps forget/refine)
- Any replay-buffer design problem where full-sample storage is too expensive and patch packing is acceptable

## Core Method

### 1. Spike Activation Maps (SAM) — forward-only spatio-temporal saliency

Given spike tensor S ∈ {0,1}^{T×C×H×W} (T timesteps, C channels):

```
K(τ) = exp(−γτ)  for τ>0, else 0            # causal temporal kernel, decay γ=0.7
NCS_{c,h,w}(t) = Σ_{τ=1}^{t−1} K(τ)·S_{c,h,w}(t−τ)   # neuronal contribution score (ISI-weighted history)
H_t(h,w) = Σ_c NCS_{c,h,w}(t)·S_{c,h,w}(t)           # SAM heatmap: history × current spike
```

- Temporal aggregation for replay selection: **mean over all timesteps** (H = (1/T)ΣH_t) beats or ties last-timestep-only (H = H_T) across all benchmarks
- Layer choice: **deepest convolutional layer** (lower spatial res, richer semantics, more discriminative saliency — following Zeiler-Fergus); the paper uses layer 7
- No backward pass, no surrogate gradient needed for the explanation itself — SAM exploits inter-spike-interval dynamics directly

### 2. SAM-guided Experience Packing & Replay (EPR-SP)

1. Bilinearly upsample aggregated SAM H to input resolution (32×32 for CIFAR)
2. Sliding window P×P (P=24) computes patch saliency score s(top,left) = Σ H_full(h,w) over the window
3. argmax location → extract patch from original image; store (patch, top*, left*, label, SAM heatmap, optional SAM history)
4. Replay: place patch back onto zero canvas at stored coordinates → same supervised loss as current data
5. Storage admission: exemplar stored only if prediction correct OR ground-truth in top-3 predictions (model-validated selection)
6. Optional: reprocess stored exemplars with updated model to track explanation drift

Loss: L_total = L_CE(current) + λ_replay·L_CE(replay) — λ_replay=1.0 (CIFAR10 & tight-budget CIFAR100), λ_replay=0.3 (larger-budget CIFAR100); no explanation-matching loss (SAM is class-agnostic — explanations guide SELECTION only, not the objective).

### 3. Equal-cost accounting (the fair-comparison trick)

```
cost = 1.00 (full 32×32 image) vs 0.56 (24×24 patch: 3×24×24=1728 B vs 3×32×32=3072 B, 44% reduction)
Memory budget MB = M_t × cost
```
- EPR-SP at M_t=177 patches ≡ BASELINE at M_t=100 full images (both MB≈99)
- Compare at equal MB, not equal sample count — this is where the advantage lives

## Experimental Setup

- VGG9 SNN: conv layers of LIF neurons (threshold 1.0, soft reset), per-timestep BatchNorm (BNTT), Poisson input encoding, **T=25 timesteps (low latency)**
- Benchmarks: Split-CIFAR10 (5 tasks), Split-CIFAR100/10, Split-CIFAR100/20; TIL and CIL (CIL: concatenated frozen task heads + replay-only head updates after each epoch)
- SGD momentum 0.9, batch 128, wd 5e-4, grad-clip ℓ2≤1.0, η∈{0.1,0.3}, cosine annealing per task (reset at task boundary), early stopping on 20% task validation split
- Grid-searched on BASELINE first (λ_mem∈{0.95,0.99}, dropout on/off), then ablated selection strategy × temporal aggregation; 3 seeds

## Key Results

| Setting | Metric | EPR-SP vs BASELINE @ MB≈10 (tightest) |
|---|---|---|
| CIFAR100/10 TIL | AvgAcc | **+3.1 pts** |
| CIFAR100/20 TIL | AvgAcc | **+2.4 pts** |
| CIFAR100/10 CIL | AvgAcc | **+5.8 pts** |
| CIFAR100/20 CIL | AvgAcc | **+3.2 pts** |
| CIFAR100/10 CIL | AvgForg | **−17.8 pts** (less forgetting) |
| CIFAR100/20 CIL | AvgForg | **−13.7 pts** |

- **Buffer-saturation crossover**: at MB≈30 on CIFAR100, BASELINE recovers the TIL accuracy lead while EPR-SP keeps the forgetting advantage — low-resolution patches show diminishing returns vs full images as budget grows. Advantage is strongest in the tight-budget regime that matters for neuromorphic hardware.
- At equal SAMPLE count, BASELINE wins (patches lose info) — the win only appears at equal MEMORY cost. Report both.
- **Explanation drift analysis**: SAMs generated right after task learning vs after all 20 tasks — salient regions remain largely consistent; final SAMs for early tasks become MORE concentrated on target object, LESS on background → continual learning can refine, not just preserve, task-relevant representations.
- EPR-SP (SAM-selected) consistently ≥ BASE-EPR (uniform-random patches) across all benchmarks → model-validated saliency selection adds real signal over random packing.

## Method Notes & Pitfalls

1. SAM is class-agnostic (aggregate spike activity, not output-conditioned) — you cannot add explanation-matching regularization directly; the paper's own future work suggests output-conditioned scores or temporal attention to fix this
2. Fixed patch size P=24 is a limitation — no multi-scale packing
3. Small-scale benchmarks only (CIFAR); early-task SAM quality depends on how well the model was already trained (cold-start problem — pretrained backbones suggested as fix)
4. Admission rule (correct OR top-3) couples buffer content to current model quality — early weak models pack worse exemplars
5. CIL protocol detail: previous-task heads are frozen during current-task training; a separate replay phase per epoch unfreezes heads and replays — necessary for head calibration
6. The 0.56 cost factor assumes raw byte storage; latent-compression competitors (Dequino et al.) change the accounting again

## Transferable Patterns

1. **Forward-only saliency as selection signal**: any non-differentiable/gradient-hostile model class (SNN, Boolean nets, analog accelerators) can reuse causal-kernel saliency (exp-decay history × current activity) for exemplar/patch/memory selection without backprop
2. **Equal-cost budget accounting**: when comparing storage-efficient CL methods, always define cost-weighted budgets (samples × bytes) — headline gains often invert between equal-sample and equal-cost framings
3. **Explain-then-pack pipeline**: heatmap → upsample → sliding-window argmax → store patch + coordinates; replay reconstructs padded inputs so the supervised loss is unchanged (no special replay loss needed)
4. **Explanation drift as a CL diagnostic**: storing per-exemplar SAM history and re-plotting after later tasks is a cheap qualitative check that representations are not silently repurposed

## Related Skills

- `elitereplay-quality-diversity-replay-grpo` — replay buffer diversity for RL post-training (different objective, same buffer-quality concern)
- `importance-shrinkage-continual-learning` — regularizer-side CL (EWC/MAS) where this paper is replay-side
- `seal-kd-snn-knowledge-distillation` / `stars-snn-data-free-knowledge-distillation` — SNN distillation alternatives to replay
- `multi-plasticity-snn-training` — SNN plasticity co-design
- `snn-performance-analysis` — SNN benchmarking context

## Key Equations

```
K(τ) = exp(−γτ)·[τ>0]                       # causal kernel, γ=0.7
NCS(t) = Σ_τ K(τ)·S(t−τ)                    # ISI-weighted spike history
H_t = Σ_c NCS_c(t)·S_c(t)                   # SAM heatmap at t
H = (1/T)·Σ_t H_t  (mean aggregation)        # selection heatmap
s(top,left) = Σ_{h,w∈window} H_full        # patch score, P=24
(top*,left*) = argmax s                     # pack location
L = L_CE(B_i) + λ_r·L_CE(B_mem)             # λ_r=1.0 or 0.3
cost: 3·24·24/3·32·32 = 0.5625              # patch cost factor
```
