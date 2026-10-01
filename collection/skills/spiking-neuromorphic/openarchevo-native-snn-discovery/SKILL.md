---
name: openarchevo-native-snn-discovery
description: Use when evolving native SNN architectures with LLM search
category: ai_collection
trigger: LLM-guided architecture search, spiking sequence model design, evolutionary NAS open program space, three-view novelty, surrogate-assisted evolution, spike-native architecture
source: arXiv:2609.40258 (Zhao, Wu, Zhu, Lu — City University of Hong Kong, 30 Sep 2026)
---

# OpenArchEvo — LLM-Guided Evolutionary Discovery of Native SNN Architectures

## Core Insight

ANN→SNN transfers underuse spiking computation: ANN and SNN implementations of the same 97 paired architectures agree only **partially in rank** on WikiText-2. Instead of searching a predefined configuration space (which limits discovery to expressible mechanisms), let an **LLM evolve executable architecture code in an open program space** under executable constraints, and use a **surrogate + novelty dual objective** to decide which candidates deserve expensive training.

## Problem Setup

- **Search space A**: admissible SNN block architectures, each as executable code within a fixed outer model wrapper.
- **Constraints (hard, checked before evaluation)**:
  1. Interface constraints (block input/output signatures)
  2. Causality constraints (no future-token leakage)
  3. **Spiking-projection constraint**: binary spikes must feed the parameter-dominant feature projections (this preserves sparse synaptic accumulation; weight sums evaluated by accumulating weights of active spikes only).
- **Bi-objective**: maximize `y(a, w*(a))` (task fitness) and `N(a; R)` (novelty vs reference set R).
- Fitness: `y(a) = ½φ_WT2(PPL_WT2(a)) + ½φ_ListOps(Acc_ListOps(a))`, anchored so SpikingDeltaNet = 0.500. Two complementary tasks because cross-task rank agreement is weak.
- Neuron model fixed (LIF, hard reset): `ṽ_τ = λv_{τ−1} + I_τ`, `s_τ = 𝕀[ṽ_τ ≥ θ]`, `v_τ = (1−s_τ)ṽ_τ`.

## Three-View Architecture Representation (the reusable pattern)

Code differences do NOT imply architectural novelty. Compare candidates across three complementary views:

| View | Content | Similarity metric |
|------|---------|-------------------|
| (a) Code | implemented operations + dataflow | CodeBLEU (averaged both directions) |
| (b) Design rationale | LLM-stated intent (EoH idea–code pairing) | text-embedding cosine (e.g. text-embedding-v4) |
| (c) Behavioral fingerprint | 21-D numerical vector | cosine after fixed affine scaling |

**Behavioral fingerprint construction (21-D)**:
- 7 initialization-time probes (fixed inputs, fixed init, fixed seed):
  - **SWSP** — sample-wise spiking patterns: adapt SWAP's sample-wise pattern count to binary spikes; each neuron–position response forms a pattern across probe samples; count distinct patterns
  - **FireRate** — mean spike activity per spiking layer
  - 5 classical zero-cost proxies (activation- and gradient-based: synflow/grad-norm style, Abdelfattah et al. 2021, Mellor et al. 2021)
- 4 module statistics (component counts, parameter count)
- 10 structural statistics (dimension flow, computational organization, resource allocation, subgraph)

**Dissimilarity & novelty** (novelty-search style, fixed untuned equal weights):
```
d(a1,a2) = 1 − ⅓[s_code + s_rat + s_fp]
N(a; R) = mean_{a'∈R\{a}} d(a, a')
```

## Surrogate-Assisted Two-Loop Evolution

**Inner loop (cheap, many candidates)**:
1. Seed island populations from evaluated archive D_{t−1} via NSGA-II nondominated sorting + crowding-distance truncation on (measured fitness, novelty).
2. LLM revises/recombines parent code + design rationales (within or across islands).
3. Feasibility check → fingerprint → **near-duplicate screening** vs archive.
4. Surrogate (TabPFN-2.5, using archive records as labeled context) predicts task metrics → predicted fitness ŷ.
5. Predicted fitness guides parent selection and survival.

**Outer loop (expensive, few evaluations)**:
1. Shortlist: prioritize predicted performance, supplement with high mean-dissimilarity candidates (diversity).
2. Screen shortlist vs evaluated archive for near-duplicates.
3. NSGA-II selection on (predicted fitness, novelty vs filtered pool) → batch ≤ K, budget B total.
4. Train under fixed protocol (30 epochs WT2 + 25 epochs ⅓ ListOps), add to archive with measured outcomes.

**Screening funnel (measured)**: 18% compilation failures, 3% causal-check failures, 30% near-duplicate screening removed → 49% of raw proposals accepted.

## Key Results

| Model | WT103 PPL ↓ | Energy reduction vs dense Transformer |
|-------|------------|----------------------------------------|
| ANN DeltaNet | 27.5 | 1× (baseline) |
| **NeuroGate** (discovered) | **26.4** | 33.1× |
| HomeoResSSM (discovered) | 28.1 | 24.7× |
| LoopMem (discovered) | 27.8 | **50.6×** |
| SpikingDeltaNet (baseline SNN) | 34.5 | 14.8× |

- Total search cost: ~132 V100 GPU-days.
- Discovered native mechanisms: **spike-activity-dependent control of recurrent state updates and output gating** (NeuroGate), homeostatic residual SSM (HomeoResSSM), **state-norm feedback** (LoopMem).
- Surrogate study: probes-only Kendall τ ≈ 0.46–0.50; +SWSP/FireRate improves; full 21-D fingerprint strongest; TabPFN-2.5 best regressor vs XGB/RNN/RF/SVM/KNN. Warm-start stage matters: without it, best fitness after 6 iterations = 0.56 vs 0.68.
- Full multi-island evolution beats single-island, sampling+surrogate, and sampling-only on Top-1/Top-5 PPL AND novelty (Table 4).

## When to Use This Pattern

1. **Native architecture discovery for non-standard compute substrates** (spiking, analog, in-memory) where ANN intuition transfers poorly.
2. **Any expensive-evaluation evolutionary search**: the fingerprint → near-duplicate screening → surrogate prediction → bi-objective (performance, novelty) allocation loop is domain-agnostic.
3. **Open program space via LLM + executable constraints** instead of enumerating config spaces: specify *constraints* (interface/causality/substrate), not *mechanisms*.
4. Cumulative archive design: every trained candidate becomes labeled context for the surrogate and parent material — search outputs are a reusable record of evaluated designs.

## Pitfalls / Caveats

- Novelty is population-relative — depends on reference set R; fingerprints only *approximate* redundancy.
- Energy reductions are **arithmetic-operation estimates**, not measured hardware savings (memory access and execution costs excluded).
- Neuron model was fixed — jointly evolving neuron dynamics + architecture is open.
- Early-iteration surrogate has little labeled context; a warm-start expert archive substantially improves trajectory.
- ASI-Arch comparison used unequal budgets — interpret cross-paper claims cautiously.

## Implementation Checklist

- [ ] Define executable constraint checker (interface, causality, substrate projection) — reject before any compute
- [ ] Fix probe protocol (inputs, init, seed) BEFORE any comparisons
- [ ] Build fingerprint: substrate-specific pattern statistic (SWSP analog) + activity stats + classical proxies + structural stats
- [ ] Choose in-context surrogate (TabPFN) over trained regressors when archive is small
- [ ] Multi-island + NSGA-II selection on (predicted fitness, novelty)
- [ ] Budget-split: inner loop thousands of cheap evaluations, outer loop tens of trainings

## References
- arXiv:2609.40258 — OpenArchEvo (this paper)
- EoH (Liu et al. 2024) — idea–code pairing; LLMatic (Nasir et al. 2024) — quality-diversity NAS; ShinkaEvolve (Lange et al. 2026) — code-embedding novelty screening; SWAP (Peng et al. 2024) — sample-wise pattern count; TabPFN-2.5 (Hollmann et al. 2025)
