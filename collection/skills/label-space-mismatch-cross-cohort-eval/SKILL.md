---
name: label-space-mismatch-cross-cohort-eval
description: Use when comparing classifier performance across cohorts.
trigger: cross-cohort evaluation, label-space restriction, label-space mismatch, annotation standard mismatch, METABRIC PAM50, claudin-low, EM prior correction, mask_only renormalise, cross-site accuracy comparison, cohort documentation compliance, portable endpoint, internal validation overstatement, multimodal fusion transfer failure, external validation genomics, subtype classifier transfer, McNemar paired test, label space reconciliation, class prior correction, target label set not recoverable, evaluation-rule change, macro F1 accuracy tradeoff
author: engineering-lion5
category: ai_collection
version: 1.0
license: MIT
related_skills: leakbench-clinical-agent-leakage-audit, same-brain-different-prediction, eeg-biomarker-robustness-cross-population, availability-contract-earnings-nlp, llm-rater-multiplicity-audit
---

# Label-Space Mismatch Distorts Cross-Cohort Evaluation

**Source**: arXiv 2610.24962 (Liu, Min, Zheng, Wang — 20 Oct 2026). Breast cancer molecular subtyping case study: METABRIC (n=1,369, six classes incl. claudin-low) → TCGA-BRCA (n=987) and GSE21653 (n=266), both annotated with five-class PAM50 (no claudin-low). A claudin-low prediction **cannot be correct** under a five-class standard. Decomposes the three evaluation operations routinely conflated in cross-site comparisons and shows the dominant correction is an evaluation-rule change, not a modeling gain.

## When to Use

- Transferring any classifier between cohorts/biobanks/hospitals whose **annotation standards differ** (different label ontologies, class counts, or category definitions).
- Reading or writing cross-cohort accuracy claims where source-classifier label space ⊃ target standard (missing or extra classes on either side).
- Deciding whether an external-accuracy jump after transfer came from better prediction or from an evaluation-rule change.
- Reviewing multimodal-fusion claims (genomics + clinical + methylation) whose internal gains might not transport.

## The Three Conflated Operations (separate them!)

1. **Label-space restriction (mask_only)** — restrict output to the target's allowed label set and renormalize. This is an **evaluation-rule change, not a retraining gain**. Dominant correction: TCGA-BRCA 73.76%→79.74%, GSE21653 63.16%→68.42%; macro F1 0.585→0.757 (unambiguously beneficial). On TCGA the six-class model sent 75 samples (7.6%) to the absent claudin-low column — incl. 22.1% of basal-like and 44.4% of Normal-like predictions.
2. **EM prior correction on the reconciled space (em_pam50)** — optional calibration step. Accuracy/Brier improve further (TCGA→80.65%, GSE→74.06%; Brier 0.376→0.291→0.275), but **macro F1 drops** (0.757→0.737) as mass shifts to the dominant class. A tradeoff a deployment can reasonably decline — report both metrics; the choice is about which error matters clinically.
3. **Target-label-space recovery** — **impossible from unlabelled predictions**: EM retains prior 0.0751 on the absent class; calibrated detectors fail. Compliance must come from **cohort documentation**, never inferred from model outputs.

## Protocol (before any cross-cohort performance claim)

1. **Report the cohort's allowed label set** as part of the eval spec (both directions: source classes absent in target, target classes absent in source).
2. Apply **label-space compliance**: mask predictions to the target's label set, renormalize, THEN score. Report masked and unmasked numbers side by side.
3. Only then consider prior correction — as a separately reported calibration step with its macro-F1 cost.
4. Never treat accuracy deltas across label-space boundaries as model-skill differences.

## Negative Results Worth Keeping

- **Multimodal fusion gains do not transfer**: no configuration (mRNA+clinical, mRNA+methylation, tri-modal) beats mRNA-only externally (n=694; McNemar p=0.13–1.00). Additional modalities/architecture raise internal CV while leaving or worsening external accuracy — report as a negative result about modality fusion, not a pipeline failure.
- **Internal validation overstates cross-cohort value**: the best internal model (713-dim flagship, 75.92% CV) is precisely the one that cannot transport — 59 METABRIC-only clinical dimensions (NPI, GRADE, INTCLUST, THREEGENE, cohort indicator) have no external counterpart. The harmonized model's higher TCGA accuracy reflects label-space restriction, not better prediction.
- **Genomic panel adds ~nothing** to pathological-complete-response prediction over clinical variables (ΔAUC = +0.0045).
- **Endpoint portability**: subtype accuracy is a weaker portable endpoint than survival discrimination (external C-index 0.577–0.584). Boundary errors map to distinct treatment decisions (Luminal A/B and claudin-low boundaries).

## Checklist for Cross-Cohort Studies

- [ ] Both cohorts' label ontologies documented with exact class lists
- [ ] Label-space reconciliation applied before scoring (mask+renormalize)
- [ ] EM/prior correction reported separately with macro F1 shown
- [ ] No claim that target label space was "recovered" from predictions
- [ ] Internal-only feature blocks identified (dimensions that cannot transport)
- [ ] McNemar/bootstrap CIs for paired config comparisons, per cohort
- [ ] A portable endpoint (e.g., survival discrimination) reported alongside subtype accuracy

## Pitfalls

- Treating label-space restriction gains as retraining/improvement gains (the central mistake this paper corrects).
- Applying EM correction on the *unreconciled* space, or reporting accuracy without the macro-F1 cost.
- Claiming a fusion advantage from internal CV alone — check external McNemar first.
- Ignoring that the mismatch direction can be reversed (target has classes the source lacks) — symmetric protocol required.
