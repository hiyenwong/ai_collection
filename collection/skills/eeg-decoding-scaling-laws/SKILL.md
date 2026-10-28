---
name: eeg-decoding-scaling-laws
description: Power-law data scaling for EEG decoding across architectures. Use when planning EEG datasets or extrapolating model performance.
category: ai_collection
version: "1.0.0"
source: arXiv:2609.35056
source_title: "Scaling Laws for EEG Decoding: How Much Data Is Enough?"
authors: "José Maurício Nunes de Oliveira, Bruna J. Lopes, Léo Burgund, Raphael Y. Camargo, Bruno Aristimunha"
published: 2026-09-28
categories: "q-bio.NC"
trigger_words:
  - EEG scaling law
  - data requirements EEG
  - subject count trial count
  - cross-subject EEG benchmark
  - data-efficient experiment design
---

# Scaling Laws for EEG Decoding

## Overview
Methodology from arXiv:2609.35056 (de Oliveira, Lopes, Burgund, Camargo, Aristimunha; submitted 2026-09-28, q-bio.NC). First systematic characterization of **power-law data scaling** for EEG deep learning decoding: 5 models × 4 datasets, varying subject count and trial volume independently under cross-subject validation, then fitting $perf \propto D^{-\alpha}$-style power laws.

## Core Findings
1. **Trial vs subject scaling converge**: as total data volume grows, the distinction between adding trials vs adding subjects becomes largely irrelevant — what matters is total data volume (scan time × subjects).
2. **Power laws are model- and dataset-specific**: no universal exponent; each architecture-dataset pair needs its own fit.
3. **Robust descriptive framework**: power-law fits extrapolate well to larger subject pools — RMSE < 0.1 in most cases when extrapolating beyond observed subject counts.
4. **Data-efficient experimental design**: fitted scaling curves let researchers estimate the marginal value of recruiting more subjects vs collecting more trials per subject BEFORE running the study.

## Method Recipe
1. Fix architecture + dataset; run cross-subject validation with subject count $N_s \in \{...\}$ and trials-per-subject $N_t \in \{...\}$ grid.
2. Fit power law $\text{perf}(N_s, N_t) = A \cdot (N_s \cdot N_t)^{-\alpha}$ (or separate exponents for $N_s$, $N_t$ at small scale).
3. At large total volume the separate exponents collapse → single-volume exponent.
4. Extrapolate to target $N$ with confidence interval; check RMSE against held-out actual runs.
5. Use the curve to allocate budget: recruit subjects until marginal gain/subject < marginal gain/trial.

## Pitfalls
- Exponents do NOT transfer across architectures or datasets — refit for your pipeline.
- Cross-subject validation is the correct regime for these laws (within-subject scaling differs).
- Small-$N_s$ regime (< ~10 subjects) still shows trial/subject distinction; the collapse only holds at scale.
- Power law is descriptive, not mechanistic — it does not explain WHY a model saturates.

## Practical Significance
- EEG foundation-model era needs data-planning tools; this provides the first empirically grounded one.
- Answers the recurring question "how many subjects do I need?" with dataset-specific extrapolation instead of folklore.
- Baseline for judging whether a new EEG architecture is data-efficient or merely data-hungry: compare its scaling curve against these 5 reference models.

## Related Papers
- EEG foundation model literature (BIOT, EEGPT, LaBraM-style pretraining) — scaling behavior underexplored until now
- Standard neural scaling laws (Kaplan et al.; Hoffmann/Chinchilla) — vision/NLP analogue
