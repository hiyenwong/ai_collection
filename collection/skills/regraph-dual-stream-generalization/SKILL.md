---
name: regraph-dual-stream-generalization
description: "ReGraph methodology: recurrent dual-stream graph model showing relational generalization and grid-like representations emerge along the dorsal visual stream via biological inductive biases. Use when studying how 'what'/'where' stream segregation gives rise to context-invariant codes, how grid-cell-like hexagonal patterns emerge in attention matrices, or designing brain-inspired dual-stream architectures with dorsal-to-ventral modulation."
---

# ReGraph: Dual Visual Stream Emergent Generalization

Source: arXiv:2610.07962v1 (Kang, Lee, Lee, Hong — 2026-10-08)

## Core Claim

Relational structure underlying generalization (MEC grid codes, context-invariant representations) does NOT arise de novo in the hippocampal-entorhinal system. It crystallizes progressively along the extended dorsal visual stream, driven by three biological inductive biases rooted in the retinal M/P (magnocellular/parvocellular) dichotomy.

## Architecture (Three Inductive Biases)

1. **Stream-specialized asymmetric encoding** (primary stage): dorsal stream receives fast temporal sampling / low spatial resolution tokens (M-cell trait); ventral receives high spatial resolution / RGB (P-cell trait). Ablation: trait-symmetric variant drops to 69.78 vs full-asymmetric ReGraph 74.57 (SSV2 33-class top-1). Asymmetry itself — not mere dual-stream existence — drives the gain.

2. **Input-driven dynamic lateral connectivity** (extended stage): each cortical area modeled as graph nodes; lateral connectivity = MHSA interpreted as a dynamic adjacency matrix A(X) = softmax(QK^T/√d) — dense over all node pairs, recomputed every forward pass. This replaces GCN's static A. Multi-head = multi-channel parallel processing (different "connection types" per head).

3. **Dorsal-to-ventral top-down modulation**: learnable gate g_l injects dorsal context-invariant features into ventral stream (Magnocellular Advantage hypothesis). Gated fusion unit per layer.

## Key Results

- **Grid-like emergence**: HOSVD on pre-softmax attention matrices → top-5% singular-value bases; hexagonal spatial autocorrelograms (gridness score > shuffled null) appear ONLY in ReGraph's extended dorsal stream, monotonically increasing across layers L1→L4 (0.0→15.3%); absent in Unmodulated, Dorsal-Only variants and ALL standard baselines (VideoMAE, TimeSformer, SlowFast).
- **Functional relevance of grid-like bases**: bases-ablation (remove grid bases from attention) causes OOD accuracy drop concentrated at L3–L4 (+7.0 to +14.0 pp); connectivity-reconstruction error surges at same layers (+.082/+.094). Grid bases act as reusable routing templates.
- **Context-invariance transfer mechanism**: dorsal stream natively context-invariant (small OOD drops); ventral stream acquires invariance ONLY at later layers as gate g opens (near-init → 0.4+ at L3–L4). Cross-stream modulation, not independent computation.
- Single-stream references: Dorsal-Only 71.69, Ventral-Only 60.38 → stream coupling essential.

## Analysis Pipeline (RPA — Relational Primitives Analysis)

1. Extract per-class, per-head, per-layer pre-softmax attention matrices (30 correctly-classified training samples per class, above-median-accuracy classes).
2. HOSVD per class–head–layer; retain top 5% singular-value bases (robustness: 3%/7%).
3. Reshape spatial bases → 2D autocorrelogram → gridness score vs shuffled null.
4. Layer-wise OOD linear probing for context-invariance; bases-ablation and connectivity-reconstruction for functional relevance.

## Design Rules for Brain-Inspired Dual-Stream Models

- Make streams asymmetric on temporal/spatial resolution, not just input content.
- Use attention-as-dynamic-adjacency for intra-areal lateral connectivity (never static graphs).
- Add explicit cross-stream gated modulation; monitor gate opening trajectory as mechanism evidence.
- Fixed token budget across variants for fair ablation.
- Pretrained primary stage fine-tuned at 100x smaller LR than extended-stage layers trained from scratch.

## Limitations Noted by Authors

- Unidirectional D→V modulation only (real cortex is reciprocal).
- Tested on spatiotemporal visual stimuli only (SSV2); non-visual abstract relational reasoning untested.

## References

- Code: https://anonymous.4open.science/r/regraph-351D/README.md
- Weights: https://doi.org/10.5281/zenodo.19917046
- Prior grid-cell emergent work: Dordek et al. 2016, Stachenfeld et al. 2017, Sorscher et al. 2023 (treat grid codes as local MEC computation — this paper relocates origin upstream).
