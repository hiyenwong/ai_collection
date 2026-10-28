---
name: eeg-video-subject-scaling-law
description: Use when scaling EEG decoding cohorts or pretraining foundation models. Subject-count scaling law with S≈50 onset.
category: ai_collection
trigger_words: EEG foundation model, subject scaling, cross-modal contrastive, movie decoding, scaling law onset, REVE, V-JEPA-2, naturalistic stimuli, pretraining initialisation
metadata:
  arxiv_id: "2610.09287"
  published: "2026-10-07"
  authors: "Dung Truong, Kuntal Kokate, Arnaud Delorme"
  tags: [eeg-foundation-model, scaling-laws, cross-modal-alignment, naturalistic-decoding, subject-cohort, clip, v-jepa]
---

# EEG Video Subject Scaling Law (arXiv 2610.09287)

Truong, Kokate, Delorme (UCSD/CNRS). The largest subject-scaling study for naturalistic EEG video decoding: a cross-modal EEG–video contrastive encoder trained on cohorts from 10 to 1863 subjects (HBN dataset, two animated films), finding subject count is a productive scaling axis — but only above S ≈ 50.

## Core Findings

1. **Log-linear subject scaling law with an onset at S≈50.** Above the onset: +0.0244 probe r and +0.0093 retrieval top-1 per cohort doubling (R²=0.94/0.90), no saturation at S=1863. Below it — the ENTIRE range prior work occupies (max cohort 48) — no arm reaches even 1.4× an untrained encoder on the probe or 2× on retrieval. The disagreement with prior "scaling subjects doesn't help" conclusions (Banville et al. 2025) is a range restriction, not a contradiction: at their n, the curve moves too little for their design to resolve.
2. **Initialisation moves the exponent more than capacity.** An encoder initialised from a pretrained EEG foundation model (REVE) scales 1.5–1.7× faster per cohort doubling than randomly initialised encoders at two depths, is the ONLY arm still converting subjects into retrieval accuracy past S=701 (pretrained +0.022 top-1 vs deep-random +0.003 over the ladder top; shallow-random peaks early and turns down), and reaches a better optimum on ≥2.4× less compute (26.6 vs 63.3 PFLOPs). Depth shifts slopes less, and its effect on the LEVEL flips sign between within-task (shallower wins +0.008 r, 9/9 draw pairs) and cross-task (shallower loses −0.005 r).
3. **The untrained-encoder floor is high and must be reported.** A frozen random encoder already reaches r=0.105 on the within-task probe — about a third of the best cell — so absolute scores are uninterpretable without the floor. Every panel carries it.
4. **Negative control behaves as it should**: cross-task ZERO-SHOT retrieval never leaves chance in any arm at any S (within 0.005 of floor), while the cross-task PROBE does scale (2.93× chance at top). What fails to transfer across films is the EEG projection head, not the encoder representation.
5. **Optimum location is itself a cost.** Random-init optima travel the ladder (median epoch 125 at S=10 → 775 at S=1863, pinning against budget at the top — apparent saturation belongs to the PROTOCOL, not the subject axis); the pretrained optimum barely moves (325 of 375 at top). Deployable early stopping with patience finds the best checkpoint in 12/15 high-S cells for the pretrained arm vs 8/15 for random-init; random-init failures quit at epoch 200 when the best lay at 620–680.

## Methodology

### Cohort ladder design
- HBN EEG 129ch @200Hz, releases R1–R5 pool (2156 recordings) subsampled at S ∈ {10, 20, 50, 100, 200, 400, 701, 1000, 1400, 1863}, 3 nested draws per rung; R6 (108 subjects, zero overlap) reserved as untouched test release. All arms draw cohorts with the SAME seeds → identical subjects at every rung (paired comparisons).
- Training stimuli: "The Present"; cross-task transfer: "Despicable Me". 2s aligned windows, per-channel z-scored.
- Targets: 12 continuous frame features (low: luminance/contrast/entropy; mid: motion energy/depth/faces; high: scene naturalness/narrative events) + shot/scene segmentation (TransNet V2), setting retrieval pools at 101 timepoints / 49 shots / 35 scenes → chance is explicit.

### Architecture & objective
- Three arms: pretrained REVE (depth 22, d_model 512, 8 heads, 200-sample patches with 20-sample overlap, released first-stage weights via braindecode); random-init depth 22; random-init depth 12 (non-overlapping 400-sample patches).
- Soft-target CLIP on mean-centred movie embeddings: frozen V-JEPA-2 supplies 1408-d vision targets → linear 512-d projection. The teacher's own window-to-window similarities define SOFT targets — the EEG encoder fits a graded distance, not binary match/mismatch. Beat hard-target CLIP and a scene-mask loss. Natural fit for continuous film where windows seconds apart are genuinely alike.
- Fixed gradient steps per epoch; total steps per run from a prior convergence study (4400 below S=701; random-init arms retrained at 8800 above, since the shorter budget proved limiting). Nothing stopped early; checkpoints written on a shared grid, read afterwards.

### Two independent readouts
- **Feature-encoding probe** (fitted): RidgeCV on mean-pooled 512-d vector, Pearson r with cluster bootstrap B=2000. Discards the EEG projection → isolates representation quality from decoder capacity.
- **Fit-free retrieval**: L2-normalised cosine similarity in the shared space, e→v top-{1,5,10} at all three granularities, nothing fitted at eval time. First retrieval result reported on continuous film.
- Every cell read at its OWN checkpoint optimum (argmax of held-out retrieval on the cohort complement — 293 subjects the draw didn't train on — over checkpoints every 25 epochs). Selecting on the probe instead moves the chosen epoch but not the outcome.

## Design Lessons (transferable)

1. **Range restriction masquerades as a null result.** Prior scaling work concluded "subjects don't help" from n≤48; the onset at S≈50 means their null and this paper's sub-onset measurements are the SAME measurement. When a scaling axis looks flat, ask whether the tested range sits below the onset.
2. **Report the untrained floor** alongside every scaling number — a random encoder's score is the zero of the scale, not zero.
3. **Initialisation is a scaling-hyperparameter**: pretrained init doesn't just lift the curve, it multiplies the EXPONENT (gap widens every rung) and stabilises the optimum location, which in turn makes model selection reliable. Random-init arms confound the subject axis with a moving convergence point.
4. **Paired-seed cohort draws** let you compare arms on identical subjects at every rung — arm differences cannot come from cohort composition.
5. **Include a readout expected NOT to scale** (cross-task zero-shot retrieval) as a pipeline control: it confirms the subject slope is not manufactured by the pipeline.
6. **Compute accounting**: depth-22 step costs 3.8× depth-12; the shallow random-init arm reaches its optimum on 15.6 PFLOPs (¼ of deep arm) while BEATING it on every within-task readout — at this data scale extra depth buys nothing. Pretrained-weights compute is already paid and reusable, excluded from comparison.

## Limitations (paper's own)

Single dataset/montage/protocol; one training film, one transfer target. Fit and test share the stimulus on the within-task probe (inflates absolute r; subjects disjoint and overlap constant across S so the SLOPE is unaffected — cross-task probe on an unseen film confirms). 3 draws/cell → smallest attainable per-step p = 0.10; inference rests on the ladder as a whole. Top rung barely replicates (each draw takes 86% of the pool). Capacity axis is two depths, no per-arm hyperparameter sweep. Says nothing about hours-per-subject law (3.4 min/subject).

## Outlook

Extension across datasets with heterogeneous montages but shared stimuli (REVE's montage-agnostic input supports this); EEGDash / NEMAR / HED standardisation make subject pooling cheap. Subject scaling on shared naturalistic stimuli is an effective, currently UNSATURATED frontier for EEG foundation models.

## Related Skills

- [[specbram-band-power-eeg-fm]] — EEG foundation model audit (band-power specificity)
- [[eeg-decoding-scaling-laws]] — power-law data scaling for EEG decoding
- [[matched-input-eeg-fm-audit]] — EEG FM auditing protocol
- [[laya-eeg-foundation]] / [[reve-eeg-foundation]] — REVE-family EEG foundation models
