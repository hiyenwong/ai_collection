---
name: fit-structure-dissociation-latent-dynamics
description: Use when evaluating personalized dynamical models where similar predictive fit may hide different learned structure.
category: ai_collection
trigger_words: personalized latent dynamics, mLTD, transition-dependency graph, fit-structure dissociation, patient world model, EEG foundation model, epilepsy, TUEP, latent-state trajectory, group-lasso, next-state prediction, clinical AI evaluation
version: "1.0.0"
source: arXiv
source_title: "Similar Predictive Fit but Different Latent Dynamics: Characterizing Learned Dynamical Structure in Personalized Models of Brain Disorders"
authors: Rita Huan-Ting Peng, Nhat Bui
metadata:
  arxiv_id: "2610.10850"
  published: "2026-10-07"
  categories: "cs.LG; q-bio.NC"
---

# Fit–Structure Dissociation in Personalized Latent Dynamics (mLTD on TUEP)

**Core claim**: Two clinical groups can be *equally predictable* under their personalized dynamical models while the models learn *substantially different internal dependency structure*. Predictive validity and learned dynamical structure are two independent evaluation axes; checking only the first can hide clinically associated differences. Demonstrated on epilepsy vs non-epilepsy EEG (n=198): identical held-out likelihood, ~2× denser learned dependency graphs in epilepsy.

**arXiv**: [2610.10850](https://arxiv.org/abs/2610.10850) (7 Oct 2026, UIUC / Carle Foundation Hospital)

## 1. The Question

> If personalized models achieve similar predictive performance, does this mean they learned similar temporal dynamics?

Clinical AI evaluation fixates on predictive accuracy. But for *patient world models* (models of how an individual's state evolves, eventually under intervention), what the model learned internally matters beyond accuracy. Epilepsy is a *dynamical* disorder — state transitions, not static patterns — making it the right testbed for whether latent *transition structure* carries clinical signal that predictive metrics miss.

## 2. Pipeline (frozen encoder → shared states → personalized dynamics)

```
TUEP EEG (30-s segments)
  → frozen CNN–Transformer EEG foundation model (1.46M params, pretrained on
    TUEG ≈18,800 h / 2,259,998 segments, self-supervised reconstruction)
  → 128-d segment representations
  → GLOBAL k-means (k=4 primary; k=6 robustness)  ← states shared across subjects
  → per-subject discrete state trajectory s^(n) = s_1..s_Tn
  → per-subject mLTD fit  ← temporal model personalized
  → W_n ∈ R^{k×k} sparse directed transition-dependency graph
```

Key design decisions:
- **Shared state space, personalized dynamics**: one global k-means for all subjects (states comparable across people); the *transition model* is fit independently per subject. Clinical labels never touch representation extraction, clustering, or fitting — only post-estimation group analysis.
- k=4 motivated by an elbow in TUEP representation clustering (Appendix A); k=6 shows robustness. Resolutions are NOT assumed state-correspondent.
- Preprocessing: 0.3–75 Hz bandpass, 60 Hz notch, 19-channel 10–20 montage, 200 Hz, ±100 µV → [−1,1].

## 3. mLTD: Multinomial Logistic Transition Distributions

For subject n, model the categorical state time series:

`P_n(s_t = j | s_{t−1}, …, s_{t−L})`,  j ∈ {1..k}

- **Group-lasso regularization across temporal lags** selects which directed state→state dependencies matter for next-state prediction. L ∈ {1..10} lags = 30 s..5 min of state history.
- Output `W_n[i,j]` = retained predictive dependency from state i to future state j, aggregated over lags. Nonzero ⇔ dependency retained.
- `W_n` is **NOT a Markov transition-probability matrix**: entries are learned predictive dependency strengths (Granger-style, no sum-to-1 constraint). Diagonal = self-dependency. Observational — dependencies are *predictive temporal relationships*, NOT causal physiological interactions.
- **Per-subject model selection**: (L*, λ*) = argmax mean held-out 5-fold time-series CV log-likelihood; λ ∈ {1e-6, 1e-4, 1e-2, 1}. Over-regularized subjects with all-zero W_n are "null models" (retained in primary analysis, examined separately).

## 4. Two Evaluation Axes

| Axis | Metric | Question answered |
|---|---|---|
| **Predictive validity** | held-out CV log-likelihood; within-subject next-state AUROC | can the model predict *this* subject's unseen transitions? |
| **Learned dynamical structure** | nonzero dependency count E_n; density D_n = E_n/k²; mean diagonal; null-model rate; scalar/graph/full-matrix features | how does the model organize temporal dependencies for this subject? does that organization carry clinical signal? |

## 5. Central Result: Fit–Structure Dissociation

| Metric (k=4) | Non-epilepsy | Epilepsy | p (Mann–Whitney) |
|---|---|---|---|
| Held-out CV log-likelihood | −0.991 | −0.992 | 0.95 |
| Next-state AUROC | 0.861 | 0.855 | 0.54 |
| **Nonzero dependencies E_n** | **5.67** | **10.01** | **1.1×10⁻⁷** |
| **Normalized density D_n** | **0.354** | **0.626** | – |
| Mean diagonal self-dependency | 0.152 | 0.219 | 1.7×10⁻⁴ |

Robust at k=6: E_n 13.46 vs 19.90 (p=5.2×10⁻⁵; densities 0.374 vs 0.553). Lag-wise: predictive fit matched at EVERY lag (p ≥ 0.37) — the structural difference is not an artifact of one group selecting different lags.

**Reading**: epilepsy models retain ~62.6% of all possible state-to-state dependencies vs 35.4% — a denser learned dependency organization — while both groups are equally predictable. Similar predictive fit does NOT imply similar learned dynamics.

## 6. Clinical Signal in Structure (secondary)

Group discrimination from W_n features alone (L2-regularized class-balanced logistic regression, stratified 5-fold subject-wise CV):

| Feature set | k=4 AUROC | k=6 AUROC |
|---|---|---|
| Scalar summaries (E_n, D_n, diagonal) | 0.697 | 0.677 |
| Graph-derived features | 0.679 | 0.645 |
| Full vectorized W_n | 0.615 | 0.654 |

Moderate — not a classifier paper. The point: clinically associated information IS present in the *organization* of learned latent dynamics even when predictive fit is statistically indistinguishable.

Null-model sensitivity: at k=4, all-zero W_n in 29/99 non-epilepsy vs 8/99 epilepsy — part of the density gap traces to null models, but excluding nulls keeps AUROC 0.665 (k=4) / 0.722 (k=6) above chance.

## 7. Why This Matters (Patient World Models)

- A patient world model must ultimately predict `P(x_{t+1} | x_{t:t−L+1}, u_t)` under intervention u_t. Before that step, you must know whether your personalized models learned *equivalent* dynamics across patients/groups. Predictive equivalence alone cannot establish this.
- Proposed extension: condition dynamics on measured interventions, characterize structural change `ΔW_n = W_n^post − W_n^pre` (requires longitudinal/intervention data + causal assumptions; this paper is the observational precursor).
- Methodological maxim: **evaluate predictive validity and learned dynamical structure separately** before assigning physiological meaning to latent states or deploying intervention-aware models.

## 8. Encoder-Dependence Caveat (from Appendix A)

Cross-encoder check with an independently pretrained encoder (LUNA-Base): **absolute state-occupancy patterns are strongly encoder-dependent** (r ≈ −0.06/0.03 across encoders!) — a warning for any latent-state interpretation. After Hungarian alignment on group occupancy signatures, epilepsy-associated occupancy *changes* show descriptive concordance (r_Δ = 0.96, exploratory). Lesson: occupancy/dynamics descriptors inherit encoder idiosyncrasies; validate what is invariant.

## 9. Responsible Use

- W_n descriptors are research descriptors of model-learned dynamics — NOT diagnostic biomarkers, causal brain graphs, or physiological connectivity maps. No autonomous diagnosis/treatment selection without prospective validation.
- k-means states are unsupervised, no established clinical semantics.
- Observational case–control: differences in W_n ≠ causal disease mechanisms.

## 10. Reuse Pattern (extract this, not the epilepsy specifics)

```
For ANY personalized dynamical model evaluation:
1. Fit per-subject sparse transition models (mLTD/group-lasso or equivalent) on shared latent states
2. Report BOTH held-out predictive fit AND structural descriptors (density, self-dependency,
   graph features) — never conflate them
3. Test group differences separately on each axis (fit-matched ≠ structure-matched)
4. Check robustness: multiple k, per-lag fit curves, null-model exclusion
5. Only then ask whether structure carries group/clinical information (AUROC from
   structural features, subject-wise CV)
```

The dissociation test itself — "compare groups on fit vs structure independently" — is the transferable contribution, applicable to patient models in any disorder where dynamics (not static patterns) carry the pathology.

## 标签
#patient-world-model #mLTD #latent-dynamics #fit-structure-dissociation #EEG-foundation-model #epilepsy #personalized-medicine #model-interpretability
