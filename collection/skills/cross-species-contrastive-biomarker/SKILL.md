---
name: cross-species-contrastive-biomarker
description: Dual-rule contrastive learning aligning mouse and human neural dynamics to discover cross-species biomarkers and retrospectively track clinical drug efficacy. Use when translating preclinical electrophysiology to human disease, building cross-domain neural latent spaces, or evaluating drug rescue in a human-anchored geometry.
category: ai_collection
created: 2026-10-09
source_paper: "Cross-species representation learning aligns mouse and human neural dynamics and tracks clinical drug efficacy (arXiv:2610.11222)"
authors: "Tvrdic et al., Exin Therapeutics"
---

# Cross-Species Contrastive Biomarker — Dual-Rule Neural Representation Learning

## Core Idea

Learn a shared latent space from mouse + human electrophysiology **organized by biological state rather than species**, then evaluate drug effects in mice as displacement within that frozen, human-anchored geometry. Result: preclinical neural dynamics **retrospectively rank clinical drug efficacy** (Spearman ρ = 0.87, p = 0.0039 across 10 model-drug combinations) with zero drug-response data in training.

## The Dual-Rule Objective

Two complementary supervised-contrastive constraints on a shared encoder fed by species-specific input modules:

1. **Alignment rule**: same biological state → pull together ACROSS species (healthy mouse ↔ healthy human), upweighted positives `w_ip = 1 + β·1(s_i ≠ s_p)`.
2. **Separation rule**: different biological states → push apart IRRESPECTIVE of species (healthy ↔ disease).

```
L_i = -log [ Σ_{p∈P(i)} w_ip exp(sim(z_i, z_p)/τ) ] / [ Σ_{a≠i} exp(sim(z_i, z_a)/τ) ]
```

Plus a **gradient-reversal species classifier** suppressing species identity (but NOT forcing full domain invariance — that would erase phenotype-relevant signal). Do not collapse all disease into one cluster: use a **hierarchy** — healthy states co-aligned, disease states on a shared manifold, individual mouse models allowed to stay partially separated; a weak model-preference term lets each human patient sit near one model, several, or a generic disease region. Private latent space absorbs acquisition-specific variance; anti-collapse regularization (latent variance + covariance + participation ratio).

## Pipeline Pattern

1. **Common spectral frontend**: all recordings resampled 250 Hz, 0.5–70 Hz bandpass (4th-order zero-phase Butterworth), robust per-channel normalization (median + IQR), 8-s windows. No manual artifact rejection.
2. **Frozen representation**: train ONLY on untreated data (subject-level CV folds fixed once; seeds vary init/order, never partitions). Checkpoints chosen on validation subjects only — drug metrics never touch model selection.
3. **Drug response = out-of-sample projection**: embed treated recordings into the frozen space. Rescue metric M₂ = fraction of the disease→healthy route travelled (anchor = animal's own pre-dose state moved onto the target manifold; local route r built from softmax-weighted nearest healthy exemplars). Orthogonal displacement (outside the Fisher + top-eigen-difference discriminative subspace B) tracks off-target/sedation burden (exploratory ρ = 0.54).
4. **Clinical benchmark frozen a priori**: ordinal human efficacy score per model-drug combo (−1 documented aggravation … 4 first-line RCT-backed), assigned from published evidence BEFORE computing any latent metric. Standardize rescue scores within experimental family, then pooled Spearman + exact blocked permutation (14,400 relabelings) + bootstrap CI.

## Key Results

- **Sensory proof-of-concept** (human scalp EEG n=9 vs mouse intracranial EEG n=12, ASSR/chirp/oddball/optic-flow/gratings/checkerboards): 5/6 paradigms give cross-species response axes with cosine similarity 0.83–1.00 (oddball honestly fails — the framework does not impose alignment where none exists). Pooled auditory-vs-visual axis: cos = 1.00 (4°). Cross-species decoding above chance in held-out subjects.
- **Epilepsy** (TUEP/TUSZ human EEG; PTZ / AY9944 / 4-AP mouse models): PTZ & AY9944 align with human absence seizures; 4-AP with tonic-clonic/tonic — models capture complementary slices of human heterogeneity. 96 patients each show distinct affinity profiles (ternary assignment), and PTZ affinity correlates with antiseizure-medication burden / benzodiazepine exposure.
- **Drug efficacy tracking**: valproate & ganaxolone rescue 4-AP (p<0.03); failed drugs (JNJ-40411813, soticlestat, padsevonil) don't. **Tiagabine moves AY9944 (absence-like) AWAY from rescue — matching its clinically known absence-seizure aggravation — while rescuing PTZ.** Neural rescue vs frozen clinical efficacy: ρ = 0.87 overall AND within each family. Mouse-only biomarkers from the same latent space FAIL — cross-species alignment is what carries the translational signal. Conventional readouts (seizure count, high-amplitude time) underperform and don't improve with n.
- **Cross-aetiology generalization**: Fmr1-KO mouse in-vivo electrophysiology ↔ human 16p11.2 CNV scalp EEG (different genes, different modalities): shared hyperexcitability direction recovered; controls −0.43, deletions +0.07, duplications +0.30 (KW p = 0.025), continuous individual variation rather than binary diagnosis.

## Design Lessons

- **Alignment target = biological state, not domain invariance**: full species-invariance removes phenotype signal. Impose invariant structure selectively (which states align, which separate).
- **Evaluate interventions as geometry, not classification**: efficacy = displacement toward human-anchored healthy centroid along the conserved disease axis; orthogonal displacement may encode secondary effects (sedation) — a multidimensional pharmacological readout.
- **Freeze before perturbation**: treated data projected into a frozen representation is the cleanest way to claim the metric isn't circular. Pre-register the clinical benchmark before computing latent metrics.
- **Heterogeneity is structure, not noise**: letting multiple disease models and patients occupy a graded manifold turns model selection into an empirical mapping problem ("which patients does this model represent?") instead of face-valid mimicry.
- **Mouse-only features can obscure clinical relevance** — the same contrastive machinery trained per-species loses the translational axis entirely.
- **Modest in-domain AUROC is acceptable** (human epilepsy-vs-control AUROC 0.62) when the objective preserves within-disease structure for translation rather than optimizing binary classification.

## Limitations (authors' own)

- 10 model-drug combos, retrospective efficacy estimates; benchmark mixes syndromes/endpoints.
- Alignment cannot recover biology poorly represented in source datasets (AY9944 weakly separated, AUROC 0.55, because human atypical-absence examples are scarce).
- Assumes therapy should move activity toward the AVERAGE healthy state — compensatory rescue states would be missed; needs richer healthy/disease manifolds than a single restorative axis.
- Next step: prospective, individual-patient treatment prediction (match patient affinity → model where a drug rescues → zero-shot efficacy prediction; also clinical-trial enrichment).

## Datasets

- Human: TUEP/TUSZ (Temple University, NEDC), Simons Searchlight 16p11.2 EEG (SFARI Base)
- Mouse: PTZ, AY9944, 4-AP epilepsy models; Fmr1-KO; matched audiovisual sensory battery (custom, 250 Hz)
- Code & rodent data promised on publication (corresponding author: gabriel@exintherapeutics.com)
