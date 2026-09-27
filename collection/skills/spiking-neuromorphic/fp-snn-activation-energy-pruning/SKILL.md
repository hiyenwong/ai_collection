---
name: fp-snn-activation-energy-pruning
description: "Use to prune SNNs: spike-count activation energy criterion."
category: ai_collection
trigger_words: [SNN pruning, activation energy pruning, spike-count saliency, unsupervised personalization, neuromorphic deployment, lottery ticket SNN, BatchNorm recalibration spiking, surrogate gradient failure, LIF threshold sensitivity, one-shot pruning no labels]
---

# FP-SNN: Activation-Energy Pruning for Spiking Neural Networks

**Source**: arXiv:2609.26167 — Joseph Bingham (Technion). Code: github.com/JosephBingham/snn_fp

## Core Insight

In conventional ANNs, activation energy E[w] = |w|·(cumulative activation) is an empirical saliency proxy. In SNNs it becomes a **literal physical quantity**: E[w_ij] = |w_ij| · Σ_{t,x} s_i(x,t) counts actual synaptic AC operations (0.9 pJ each, 45nm CMOS) — the true metabolic cost of the synapse on the target workload. Pruning by it = direct measurement, not heuristic.

Mirrors biological selective stabilisation (Changeux/Katz-Shatz): |w| = structural importance × spike count = utilisation; product = joint survival rule for synapses.

## Algorithm (one-shot, no labels, no gradients)

```
for x in unlabeled target stream U:
    forward pass f_θ(x)
    for each prunable layer: E[w_ij] += |w_ij| · Σ_t s_i(x,t)   # pre-hook buffer per layer
threshold: τ = (1−σ)-quantile of E[w]  (global) or per-layer quantile
mask m_ij = 1[E[w_ij] ≥ τ];  use topk not quantile (tie handling; dead layers give all-zero E)
optional BN recalibration: reset BN stats, one forward pass over U, eval mode
```

## Three Findings (5 seeds each, Wilcoxon+Bonferroni)

### 1. Gradient-based pruning FAILS on SNNs (major negative result)
SNIP, GraSP, magnitude pruning collapse to near-chance by σ=0.2–0.4 across VGG-SNN and ResNet-19 SNN:
- CIFAR-100 20-class target: Magnitude+BN 4.7% at σ=0.1 (chance 5%); SNIP/GraSP 0.0% by σ=0.2. FP-SNN keeps 65.0% (source 65.0±0.9%)
- Root causes: (a) magnitude — weight decay makes deep-layer weights small → global magnitude thresholding decapitates classifier-adjacent layers first (retention diag: σ=0.1 removes nearly all deepest-layer weights); (b) SNIP — surrogate gradient (fast-sigmoid, slope 25) only accurate near threshold; neurons firing <5% of target samples get ~zero saliency regardless of true importance; (c) GraSP — second-order differences amplify surrogate noise → effectively random saliency
- Skip connections delay the cliff (ResNet-19 holds to σ=0.3–0.4) but do not prevent it → tied to spike-train representation, not one architecture
- Authors frame as empirical characterisation, not impossibility proof — alternative surrogates might partially mitigate

### 2. Pruning can IMPROVE accuracy (personalization)
N-MNIST 3-class target: FP-SNN global at σ=0.8 → 98.4±0.4% vs source 97.2±0.7% (+1.2pp, p<0.05, Cohen's d≈2.1) while removing 80% of weights. Mechanism: cross-class interference removal — spike-train representation shared across 10 classes; weights for the 7 non-target classes inject noise; pruning recovers a target-specialised lottery ticket that **exceeds** the source. On CIFAR-100 (harder target), FP-SNN matches source to σ=0.5 (63.6 vs 65.0, −1.4pp @ 50% sparsity, flat plateau σ=0.1–0.5).

### 3. BN recalibration has a sparsity-dependent crossover (σ*≈0.4)
- Harmful at σ≤0.3 (−15pp): estimation noise from small unlabeled stream (N≈2000) dominates
- Essential at σ≥0.5 (+11 to +27pp): pruning-induced activation shift dominates; fixed LIF threshold θ=0.5 lets whole layers go silent/saturated
- No analogue in continuous-activation networks — specific to threshold-gated dynamics. Practical rule: recalibrate only when σ≥0.5. Crossover point depends on calibration size/architecture (not a universal constant).

## Scope Selection Rule
- **Global scope** for σ≤0.6: energy flows naturally, early layers (dense input) keep more, exploits genuine early-layer redundancy
- **Per-layer scope** for σ≥0.7: prevents decapitation of deep layers (at σ=0.6 global: deepest conv layers retain only 4.1%/13.8% vs 70–90% early)
- Empirical crossover σ≈0.65: at σ=0.8 per-layer+BN 16.9% vs global 0.1% (CIFAR-100)

## Criterion Ablation (why the product matters)
- Spike-count-only matches FP-SNN at σ≤0.3 (CIFAR-100) — pruning never-firing synapses is easy
- Diverges at σ=0.4: count-only 52.8% vs FP-SNN 64.7%; collapses at σ=0.5 (1.4%) — must discriminate among firing neurons by weight magnitude
- N-MNIST: spike patterns so discriminative that |w| matters only at σ=0.8 (+6.8pp). Dataset-dependent complementarity → always use the product
- All activity-based criteria share an identical cliff at σ=0.9 (6.7±13-15%) → capacity boundary, not signal failure

## Energy Accounting (secondary)
σ=0.5 → 72.8 nJ/sample vs 77.4 source (−6%): pruning removes rarely-firing synapses, so weight reduction ≫ energy reduction. Accuracy-preservation and energy-minimisation diverge at moderate sparsity — high-energy (frequent+strong) synapses are retained precisely because they matter. 44% energy cut only at σ=0.9 where accuracy collapses.

## Setup Details
- VGG-SNN widened w=2, 37.7M params, Conv→BN→LIF, T=4 timesteps, direct input encoding; N-MNIST SCNN 3×LIFConv(32/64/128)+2 FC-LIF(256), T=20, frame-binned DVS events
- Personalization: CIFAR-100 K'=20 classes ×100 unlabeled imgs; N-MNIST K'=3 ×200
- LIF: β=0.9, θ=0.5, fast-sigmoid surrogate; AdamW lr 5e-3, cosine, 200/100 epochs
- Baselines all one-shot with +BN: Random, Magnitude, SNIP (uses labels!), GraSP

## Reusable Patterns & Warnings

1. **Never trust surrogate-gradient saliency post-hoc on SNNs** — one-shot gradient pruning methods from the ANN literature (SNIP/GraSP/magnitude) are worse than random pruning on spike trains. Random+BN is the honest floor baseline for SNN pruning papers.
2. **Activity×magnitude joint criterion** E=|w|·spikes for any spiking/subnetwork-selection task: label-free, single forward pass, hardware-grounded.
3. **Fixed firing thresholds amplify BN drift** → recalibrate statistics after any drastic sparsification; crossover depends on (shift magnitude vs estimation noise).
4. **Decapitation diagnostic**: log per-layer weight retention after global thresholding; switch to per-layer scope when deep layers fall below ~20%.
5. **Improvement-under-pruning in personalization**: when source classes ⊃ target classes, pruning to target stats can exceed source accuracy — check before assuming pruning always hurts.
6. Report accuracy-at-sparsity as primary; energy only via SynOps×0.9pJ estimates, acknowledging post-pruning firing-rate changes.

## Limitations
One-shot only (no post-prune fine-tuning); σ* empirical; VGG/SCNN only (no recurrent/transformer SNNs, no DVS-Gesture/CIFAR10-DVS); Tiny-ImageNet sources undertrained (appendix-only); energy = CMOS estimate, not measurement.

## Related Local Skills
- nm-pruning-spiking-neural-networks, cqp-criticality-constrained-snn-pruning, quantized-snn-hardware-optimization, effective-plasticity
