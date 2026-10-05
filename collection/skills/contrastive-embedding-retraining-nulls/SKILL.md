---
name: contrastive-embedding-retraining-nulls
description: Use retraining nulls on grouped contrastive embeddings.
category: ai_collection
trigger: contrastive embedding permutation test, grouped neural data null model, CEBRA dyad decoding identity confound, hyperscanning label inference, retrain-per-permutation control
---

# Retraining-Based Nulls for Grouped-Data Contrastive Neural Embeddings

Source: Huang, McCleod, Ames & Malaia, "Contrastive Neural Embeddings Reveal Individual Traits Beyond Conversational Role", arXiv:2610.03410 (NeurIPS 2026 Workshop on Symmetry and Geometry in Neural Representations).

## The Failure Mode

Decoding accuracy computed on a contrastive embedding (CEBRA, simCLR-style, etc.) is **not a test of the label** when the label is constant within a recording group (dyad, session, subject). Such a label is a *coarse-graining of group identity*: an encoder that merely learned "which dyad/session is this segment from" decodes the label above chance without representing anything about the trait.

The standard frozen-embedding permutation control **cannot detect this**: permuting labels over the fixed embedding asks only whether the learned geometry happens to contain the label partition — which it will whenever identity was learned.

## Empirical Anchor (the two-control table)

Dyadic EEG, CEBRA on S², dyad-level |ΔAQ| (autism-quotient difference) label:

| Control | Real 5-NN | Null (mean ± sd) | p |
|---|---|---|---|
| Frozen embedding, labels permuted (B=1000) | 0.7588 | 0.4821 ± 0.0340 | **0.001** |
| **Encoder retrained per permutation (B=5)** | 0.7657 | 0.7575 ± 0.0104 | **0.500** |

Same data, same labels — p-values differ by orders of magnitude because only the retraining null tests the *label* rather than the *geometry*. Null realizations from retrained encoders reach ~0.76 accuracy, i.e. arbitrary regroupings reproduce the "significant" decoding entirely from identity structure.

## Procedure (default protocol for grouped contrastive embeddings)

1. **Detect identity-confounded labels**: if the label is constant across all samples of a recording group, treat it as a proxy for group identity — expect inflated frozen-control significance.
2. **Retraining null**: permute *complete group-level label signatures* (preserving class counts), retrain the full encoder from scratch per permutation — identical preprocessing, architecture, config, seed policy, and training duration as the real run. Empirical p = (1 + #{null ≥ real}) / (1 + B).
3. **Use grouped cross-validation**: hold out both role mappings / all segments of a group together (leave-one-dyad-out), never segments.
4. **Prefer labels that vary within groups**: participant-level traits (which vary within a dyad) can survive identity-aware nulls; dyad-level traits cannot be separated from identity in a between-group design.
5. **Report both nulls** when space allows — their divergence is itself the diagnostic.

## When a Within-Group Label Survives

Participant-level AQ (varies within dyad, 40 participants / 80 recordings / 6.08M samples):

- Real decoding 0.2470 vs retraining-null 0.1157 ± 0.0197 over 100 permutations, **p = 0.0099** (dyad-level holdout).
- Exact-AQ 10-class 0.2437 vs 0.2007 majority baseline; binary AQ 0.6474 vs 0.5740.
- AQ silhouette is −0.167: the trait **grades the manifold without partitioning it** — expect continuous modulation, not clusters.

## Geometry Diagnostics (what to measure besides accuracy)

- **Spherical mixture structure & per-class dispersion**: if they track identity rather than the trait, decoding significance is identity-driven.
- **Spherical Kolmogorov–Smirnov statistics** (latitude/longitude/radius on S²): role KS = 0.013/0.019/0.021 (negligible) vs binary-AQ KS = 0.171/0.224/0.240 (graded structure).
- **Cross-condition cosine similarity**: within-participant speaker↔listener 0.9568 ± 0.0564 vs across-participant 0.1776 ± 0.6488 — the manifold is organized by **individual**, near-invariant to conversational role (speaker/listener 5-NN = 0.4736 vs 0.5006 majority = chance).
- **Frequency-band / non-oscillatory ablations**: controls that leave results unchanged indicate the effect is not band-specific.

## Design Consequences

- For dyadic/social neuroscience: adopt designs where the label of interest varies **within** a recording group (within-dyad manipulations, repeated pairings across partners).
- Treat strong decoding accuracy on grouped neural embeddings as a biomarker-candidate only after the retraining null passes.
- Related audit skill: `identity-trap-eeg-foundation-models` (same identity-vs-trait confound diagnosed for EEG foundation models); `snr-sample-size-representational-alignment` (data-quantity dependence of alignment).
