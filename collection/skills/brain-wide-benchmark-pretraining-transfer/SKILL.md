---
name: brain-wide-benchmark-pretraining-transfer
description: BrainWideBench three-suite protocol for across-animal transfer on multi-region neural recordings. Use when benchmarking neural foundation models.
category: ai_collection
metadata:
  arxiv_id: "2609.22064"
  published: "2026-09-18"
  authors: "Alexandre Andre, Shivashriganesh P. Mahato, Vinam Arora, et al. (IBL, UPenn, Mila, Columbia)"
  tags: [neural-foundation-model, benchmark, cross-animal-transfer, neuropixels, pretraining]
---

# BrainWideBench: Three-Suite Benchmark for Large-Scale Pretraining and Across-Animal Transfer

## Overview

BrainWideBench (arXiv:2609.22064) is the first benchmark for **across-animal transfer** on multi-region neural recordings, built on the IBL Brainwide Map dataset (276 brain regions, 139 mice, 688 Neuropixels insertions, 800k+ neuron hours). Its core contribution is a **three-suite evaluation protocol** that tests whether a single pretrained representation simultaneously generalizes across **behavior, dynamics, and anatomy** — three axes that no current method jointly masters.

**Key finding**: Pretraining reliably beats matched single-session baselines (which require expensive per-task hyperparameter tuning), but gains are heterogeneous — they depend strongly on the alignment between the pretraining objective and the downstream task. No single method performs uniformly well across all three suites.

## The Three-Suite Protocol

### TS1: Behavior Decoding (8 tasks)
- **5 frame-level regression** (50 Hz, seq2seq): licking rate (D² under Poisson), whisker motion energy, wheel speed, left/right paw speed (R²)
- **3 sequence-level classification** (balanced accuracy): stimulus contrast, choice, reward
- Windows: 1s around trial events (stimulus onset, movement onset, feedback)
- **Split**: temporal within-session 40% train / 20% val / 40% test — kills autocorrelation leakage AND models realistic calibration-then-deploy use

### TS2: Neural Activity Prediction (2 tasks)
- **Co-smoothing**: mask random neurons in context, reconstruct from observed rest
- **Forecasting**: predict last 200ms of each window from past
- **Split**: interleaved 5-minute temporal blocks (NOT causal trial splits — nonstationarity makes indexed-neuron identity unreliable across long spans, so causal splits compress model differences)
- **Metrics**: D² (deviance fraction explained, Poisson) + bits-per-spike (bps)

### TS3: Neuron Identity / Brain Region (10-class)
- Predict CCF Cosmos-level region (Isocortex, Hippocampus, Cerebellum, ...) from unit activity
- **Transductive zero-shot**: adapt on held-out animals with external supervision (e.g., behavioral labels), then probe region labels
- **Inductive zero-shot**: no adaptation at all — strictest test of invariant identity features
- **Single-unit vs multi-unit** settings (neighbors on probe help); macro-F1

### The animal-level split (the load-bearing design choice)
Pretrain: 126 mice / 423 sessions / 274 regions. Evaluate: 13 disjoint mice / 29 sessions / 124 regions. Models must generalize to unseen individuals, not unseen sessions of seen animals.

## TSS vs TSU Taxonomy

- **TSS (task-suite-supervised)**: pretrain directly on a suite's tasks (POYO+, multi-task POSSM, MtM for TS2)
- **TSU (task-suite-unsupervised)**: pretraining objective disjoint from evaluation (NDT-Stitch, MtM when evaluated on TS1)
- Cross-task transfer is the surprise: TSS-trained representations often win even on tasks they weren't optimized for, when the objective family aligns.

## Results Matrix (what to cite)

| Suite | Winner | Key numbers |
|-------|--------|-------------|
| TS1 behavior | POYO+ (TSS) | Licks D²=0.678, Choice 0.689, Reward 0.898; avg rank 2.53 vs POYO single-session 4.80 |
| TS1 cross-task (TSU) | NDT-Stitch/MtM | Licks 0.525/0.469 from masked-prediction pretraining alone |
| TS2 forecasting | NDT-Stitch | D²=0.157/bps=0.369 — despite NON-CAUSAL pretraining |
| TS2 co-smoothing | MtM | D²=0.191/bps=0.459 — spatial masking aligns with co-smoothing |
| TS3 inductive | NuCLR | multi-unit linear probe F1=0.654; NEMO 0.605; ISI baseline 0.355 |
| TS3 transductive | NDT-Stitch/MtM | 0.155-0.159 vs POYO+/POSSM ~0.10 — masked prediction preserves region structure; behavior decoding does not |

## Load-Bearing Insights

1. **Objective-alignment law**: forecasting ← temporal masked prediction (NDT-Stitch); co-smoothing ← spatial masking (MtM); region identity ← explicit unit-embedding objectives (NuCLR/NEMO). Transfer follows objective family, not architecture.
2. **Anatomy does not come free**: representations optimized for behavior or dynamics do not organize around anatomical structure (POYO+ region F1 ≈ 0.10 vs NuCLR 0.65). Preserving stable unit identity across animals requires designing for it.
3. **Pretraining amortizes engineering**: single-session baselines needed extensive per-task tuning; pretrained models used a standardized finetune recipe and still matched or beat them. Compute accounting shows single-session tuning costs more.
4. **Honest-hedging discipline**: rankings reliable in aggregate (broad model groups stable across resampled splits), NOT pointwise — 13 held-out animals cannot distinguish within-group rankings. Categorical labels (TSS/TSU, transductive/inductive) are organizational, not causal claims.

## Implementation Recipe (using the benchmark)

```python
# Data: IBL Brainwide Map via ONE API, standardized into torch_brain format
# 1. Load pretrain corpus (126 mice) with session/probe/unit QC metadata
# 2. Pretrain your model with any objective (keep behavior spikes + anatomy labels available)
# 3. TS1: finetune on 40% of each held-out session, validate on 20%, test on last 40%
#    - report R2 (regression), D2 (Licks), balanced accuracy (classification)
# 4. TS2: co-smooth masked units + forecast last 200ms on 5-min interleaved blocks
#    - report D2 + bps
# 5. TS3: zero-shot region classification, single-unit + multi-unit, linear AND MLP probes
#    - report macro-F1
# 6. Average over 5 finetuning seeds; rank models with significance-aware ranking
```

## Pitfalls

- **Do not use causal trial splits for TS2** — nonstationary neuron identity makes them ill-defined and compresses differences between models.
- **Do not read pointwise rankings** from 13 animals; only group-level conclusions replicate.
- **Don't assume behavior-aligned pretraining helps TS3** — it does not (POYO+ ≈ 0.10 F1).
- **Multi-unit context is a free lunch** for TS3 (+0.03-0.09 F1 across methods) — report both settings.
- **Licking is an event stream**: use Poisson D², not R².

## Applications & Extensions

- Diagnose where a new neural foundation model generalizes before investing in scaling
- Study scaling laws for neural data (pretraining corpus supports it: QC metadata at session/probe/unit level)
- Test zero-shot calibration: current SOTA still needs target-session stitchers/embeddings — minimal-calibration transfer is the open frontier this benchmark measures
- Cross-modality/cross-species extension (current limits: mouse only, Neuropixels only, visual decision task only)

## Related Skills

- [[brain-of-omnifunctional-foundation-model]] — omnifunctional brain foundation model (fMRI)
- [[mv-brain-network-foundation-model]] — multiview brain FM
- [[tribe-v2-foundation-model]] — tri-modal in-situ brain FM

## Source

arXiv:2609.22064 — Andre, Mahato, Arora, et al. + International Brain Laboratory, "BrainWideBench: Benchmarking large-scale pretraining and across-animal transfer in multi-region neural recordings" (2026). Data: IBL Brainwide Map via ONE API; benchmark format: torch_brain.
