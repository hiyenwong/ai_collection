---
name: moviestage-scene-transition-global-fmri
description: Use when classifying movie-fMRI with event-aligned scene/transition representations. Hypergraph scene encoding + adjacent-scene FC reconfiguration + whole-movie FC fusion.
category: neuroscience
---

# MovieSTAGE: Scene, Transition, and Global Encoding for Movie-fMRI Classification

**Source**: Kim, Chung, Jang. "MovieSTAGE: Scene, Transition, and Global Encoding for Movie-fMRI ADHD Classification." arXiv:2610.09306 (Oct 2026). Hanyang University + HUFS.

## Core Insight

Naturalistic movie-fMRI predictive models usually collapse the run into whole-run FC, discarding narrative event structure. MovieSTAGE shows that event-aligned multiscale representations — within-scene hypergraph organization + adjacent-scene unsigned FC reconfiguration + whole-movie FC — carry incrementally complementary predictive signal beyond any single representation. On the CMI-HBN Despicable Me pediatric cohort (260 subjects), the fusion achieves AUROC 0.69/0.73/0.75 (case-control / subtype / 3-class) with the strongest BACC among baselines. Crucially, controlled comparisons show the human-annotated narrative partition beats both duration-matched random partitions AND fixed-count GSBS neural-state segments — narrative alignment itself carries information.

## Architecture (three branches)

### Branch 1: Scene-wise hypergraph (h_scn)

Per subject, per scene s:
1. FC estimation from limited temporal samples → **Ledoit–Wolf shrinkage covariance** → correlation → Fisher-z, diagonal zeroed. (Shrinkage is essential: scene blocks are short.)
2. ROI r's **FC profile** = row r of the scene FC matrix (x_i,s,r = FC[r, :]).
3. Cosine similarity between FC profiles → for each anchor ROI r, one hyperedge connecting r to its top-K most similar ROIs (K=6). E = R hyperedges per scene.
4. Hyperedge attribute = mean cosine similarity of anchor to its members.
5. HGNN layer with learnable hyperedge weights (Softplus on MLP([z̄_e, a_e]) ensures positivity):

```
Z^(l+1) = σ( (D_v)^(−1/2) · H · W_e · (D_e)^(−1) · H^T · (D_v)^(−1/2) · Z^(l) · W )
```

6. ROI embeddings → mean/max/std pooling → scene embedding → attention pooling across scenes → h_scn.

### Branch 2: Adjacent-scene transition (h_trn)

For each boundary q (S_q → S_q+1):
```
∆FC_i,q = | FC_i,q+1 − FC_i,q |   (elementwise absolute value)
```
**Unsigned by design**: no assumption of consistent signed direction across subjects or ROI pairs — only reconfiguration MAGNITUDE. Each ROI-level ∆FC row → shared 2-layer MLP → mean/max/std pooling → attention pooling over transitions → h_trn.

### Branch 3: Global context (h_glb)

Whole-movie LW-shrinkage FC → Fisher-z → vectorize upper triangle → linear projection with dropout. The strongest single branch in ablation — global FC provides broad subject-level context.

**Fusion**: h_cat = [h_glb, h_scn, h_trn] → MLP classifier, class-weighted cross-entropy.

## Key Results (CMI-HBN, 260 children 6–11y, SC-100 parcellation)

| Task | AUROC | BACC |
|---|---|---|
| NoDx vs ADHD | 0.69 ± 0.04 | 67.6% |
| ADHD-I vs ADHD-C | 0.73 ± 0.04 | 69.8% |
| 3-class | 0.75 ± 0.03 | 58.3% |

- **Branch ablation (3-class)**: Global alone 0.68; full fusion 0.75. Full model beats ALL two-branch variants after Holm correction (all pH ≤ 0.041) — conditional, partially complementary contributions, not three redundant views.
- **Encoder control**: HGNN scene encoder > MLP / GAT / BNT under matched settings (scene-only 0.65 vs 0.60–0.63; full-fusion 0.75 vs 0.69–0.71) — the hypergraph inductive bias specifically helps within-scene FC-profile organization.
- **Segmentation control**: Human-annotated 8 scenes > random duration-matched partition (+0.05 AUROC) AND > fixed-count GSBS segments (+0.04) — event alignment matters beyond segment count/duration.
- **Post-hoc finding**: strongest group differences at T5 (children leaving → Gru missing them): ADHD shows greater FPN–DMN and DMN–DMN reconfiguration magnitude (BH-FDR q<0.05) — consistent with ADHD literature on reduced task-positive/task-negative segregation.

## Evaluation Protocol (the methodological gold)

- 10 repetitions × stratified 5-fold CV; **complete out-of-fold (OOF) predictions** concatenated per repetition
- Standardization + class weights fit WITHIN each outer-training fold only
- Inner 20% stratified split for 12-config hyperparameter search + early stopping (patience 10, checkpoint by val AUROC)
- **Paired subject-cluster bootstrap CIs + two-sided permutation tests (10,000 iters)**: each subject's repeated predictions = one cluster/joint unit — avoids pseudo-replication across CV repetitions
- Holm correction applied per comparison family (baselines, drop-one-branch, encoders, segmentations)

## Implementation Notes

- Training: AdamW, lr 1.5e-4, wd 2e-5, batch 16, ≤80 epochs, 2 hypergraph layers, dropout 0.1, K=6 top-K hyperedge members, RTX A6000.
- Scene boundaries: published adult-rater annotations, shifted 4s (5 TRs) for hemodynamic delay, mapped to nearest TR.
- QC gate: median FD ≤ 0.2mm, registration NCC ≥ 0.8; FD did not differ across groups (Kruskal-Wallis p=0.092).
- Hypergraphs built from subject-specific FC profiles only — no diagnostic labels leak into graph construction.

## Pitfalls

- **Single-cohort limitation**: evaluated only on CMI-HBN pediatric Despicable Me; external validation on independent movie-fMRI cohorts pending.
- **Unequal temporal support**: predefined scenes vary in duration → unequal FC estimation support across scenes.
- **∆FC interpretation**: unsigned differences = reconfiguration magnitude, NOT signed connectivity change — never report as "increased/decreased connectivity".
- **Hyperedge projections ≠ physiological connectivity**: model-derived consensus hypergraphs are representations, not measured pathways.
- **Point-estimate superiority**: gains over baselines are ~0.03 AUROC — real but modest; the value is the controlled decomposition, not SOTA.

## Applications & Extensions

- Template for ANY naturalistic-stimulus neuroimaging classification: replace "whole-run FC" with scene/transition/global multiscale fusion.
- Unsigned ∆FC transition encoding is domain-portable — applicable to any regime where the reconfiguration magnitude (not direction) is the signal: sleep stage transitions, task-switch fMRI, seizure onset boundaries.
- Event-aligned modeling generalizes beyond ADHD: event segmentation (Baldassano-style) + hypergraph organization per event is a reusable decomposition.
- Related skills: [[hypergraph-flow-matching-connectome-generation]] (hypergraph connectome generation), [[eiu-compositional-mea-state-transitions]] (state transition analysis), [[eeg-video-subject-scaling-law]] (same CMI-HBN cohort, subject scaling).

## arXiv Metadata

- **ID**: 2610.09306
- **Date**: 2026-10-07
- **Categories**: cs.LG (cross-listed q-bio.NC)
- **Authors**: Boseong Kim, Haejun Chung, Ikbeom Jang
