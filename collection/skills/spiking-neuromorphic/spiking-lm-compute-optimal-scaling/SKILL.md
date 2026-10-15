---
description: Use when scaling spiking language models under budgets.
name: spiking-lm-compute-optimal-scaling
category: ai_collection
trigger_words: spiking language model scaling, IsoFLOP, compute-optimal, Chinchilla, SpikeGPT scaling, neuromorphic LM training
---

# Compute-Optimal Scaling Laws for Spiking Language Models

**Source**: arXiv:2610.15146 (Saunders, Ren, He — Luma AI / X School, 10 Oct 2026, AXIOM workshop)

## Core Finding

The first Chinchilla-style IsoFLOP scaling study of a spiking language model. SpikeGPT-family models (RWKV backbone + LIF spiking neurons with arctan surrogate gradients) swept width 384→1536 across compute budgets 3×10^17 to 10^19 FLOPs on FineWeb-EDU.

**Compute-optimal frontier**: N_opt ∝ C^0.556 (R²=0.996), D_opt ∝ C^0.444 — close to dense Transformers' 0.5, so spiking does NOT change how parameters and data should be traded off under a compute budget.

## Loss Decomposition (the key diagnostic)

Against matched non-spiking baselines, the loss gap splits into two additive components:
1. **Backbone cost**: ~0.16 nats (dense RWKV vs Transformer) — constant across all compute budgets
2. **Spiking cost**: 0.338 → 0.263 → 0.227 → 0.225 nats (falls with compute, levels off by 10^19 FLOPs)

This is the first quantification of the accuracy cost of binary/sparse activations at scale.

## Methodology Details

- **IsoFLOP profiles**: fit parabola to validation loss L vs log N at each compute budget; vertex = (N_opt, L_opt); D_opt = C/(6N_opt)
- **C ≈ 6ND** (Kaplan convention); RWKV has no attention term, so matmuls dominate FLOP accounting — cleanest possible IsoFLOP setting
- Training: AdamW (β1=0.9, β2=0.999), batch 16, context 1024, gpt-neox-20b tokenizer, single-epoch to token budget
- Learning rate per width from pilot power law: LR_opt(d) = k·d^(-p), cosine decay to 1/10

## The Parameter-Counting Artifact (critical pitfall)

The exponent α moves across the entire Kaplan–Chinchilla debate purely by convention:
- Strict non-embedding (13ld²): α = 0.75 (near Kaplan's 0.73)
- FLOP-matmul count (13ld² + vd): α = 0.62
- Total (13ld² + 2vd): α = 0.56 (near Chinchilla's 0.5)

With 50,257-token vocab the embedding is 11–50% of all parameters. **Always report the counting convention when comparing scaling exponents** (Pearce & Song 2024 confirmed for SNNs).

## Statistical Rigor

- Jackknife over tiers: α_total = 0.556, range [0.532, 0.615] — estimate robust to any single tier
- Seed variance ≤ 0.003 nats → exponent shift < 0.01: NOT seed-limited
- Sensitivity to tier count: 2/3/4 tiers → α = 0.454/0.537/0.556: **more tiers is the main way to tighten α**
- Independent Chinchilla Approach-3 parametric fit (L = E + A/N^a + B/D^b) reproduces exponents within 0.04; E ≈ 2.7 nats
- Out-of-sample: hero run at C=10^20 (N≈2.44B, width 2048/depth 41, D≈7.1B tokens) reached L=2.76 vs predicted 2.78 nats

## Spike Dynamics Facts

- Spike rates depend on training progress (tokens-per-parameter), NOT model size — rising toward ~0.36 firing fraction
- Spiking cost appears to plateau near 0.23 nats; whether it resumes falling at larger scale is untested (4 tiers, single-seed baselines)

## Practical Recipe (for SNN LM builders)

1. Given budget C: pick N_T = 1.82×10^-2 · C^0.556, then D = C/(6N) — near-equal N/D split, slightly N-tilted
2. Train single-epoch; scale LR with width via fitted power law
3. Expect a fixed ~0.16-nat RWKV-backbone tax plus a ~0.23-nat spiking tax vs a matched Transformer by 10^19 FLOPs
4. Report non-embedding vs total parameter counts explicitly — α shifts 0.75→0.56 between conventions
5. To improve the exponent estimate, add compute tiers, not seeds

## Limitations

- Four tiers (3×10^17–10^19) far below Chinchilla's 10^21–10^24
- FineWeb-EDU only; aspect ratio d/l drifts 38→53 across widths
- Baselines one seed per configuration; spiking-cost plateau untested beyond 10^19

## Relations

- Extends: Chinchilla (Hoffmann 2022) IsoFLOP methodology to SNNs; Pearce & Song 2024 parameter-counting reconciliation
- Contrasts: post-hoc spiking of pretrained LLMs (Xing 2024) — this is from-scratch training
- Companion neuro skill: bullet-trains-parallel-snn-training (exact-BPTT training efficiency)
