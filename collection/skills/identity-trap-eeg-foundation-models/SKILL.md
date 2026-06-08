---
name: identity-trap-eeg-foundation-models
description: Diagnostic audit methodology for detecting subject-identity shortcut learning in EEG foundation models. Use when evaluating EEG FM reliability, subject-disjoint cross-validation issues, or assessing whether high accuracy reflects genuine biomarkers vs identity features.
license: MIT
---

# The Identity Trap in EEG Foundation Models

Diagnostic framework for detecting subject-identity shortcut learning in frozen EEG foundation model representations.

## Problem Statement

EEG foundation models achieve high accuracy under subject-disjoint cross-validation, but this success can reflect either:
- **Genuine clinical biomarkers** (desired)
- **Subject-identity features correlating with labels** (shortcut learning)

This ambiguity is the **Identity Trap**.

## FMScope Diagnostic Protocol

Five-component frozen-representation diagnostic applied BEFORE fine-tuning:

### 1. Variance Decomposition
Quantify frozen subject-variance dominance:
- Subject-variance: **13-89x random null** in 12/12 dataset pairs
- Fine-tuning amplifies: **+10 to +63 pp increase**
- Significance: Universal Identity Trap across all EEG FMs

### 2. Subject-Axis Erasure
Linear removal of subject-identity axis:
- Improves decoding when label varies within subject: **+6 to +12 pp (primary), +4 to +27 pp (external)**
- Proves subject-variance is **removable linear axis**
- Validates physical shortcut nature

### 3. Aperiodic 1/f Ablation
Physiological carrier test:
- Remove aperiodic component → subject probe drops **9-19 pp** (LaBraM, CBraMod)
- REVE: saturates identity **without measurable aperiodic dependence**
- Significance: 1/f slope is one measurable subject carrier

### 4. Layer-wise Label Probing
Fine-tuning effect characterization:
- Fine-tuning amplifies label-variance **ONLY in cells with literature-established cross-subject markers**
- Distinguishes biological gains from identity gains

### 5. Within-Subject Direction Consistency
Validates whether learned representations reflect consistent biological patterns vs noise.

## Tested Foundation Models

- **LaBraM**: Strong aperiodic dependence (19 pp drop on ablation)
- **CBraMod**: Moderate aperiodic dependence (9 pp drop)
- **REVE**: Identity saturation without aperiodic correlation

## Dataset Matrix (2x2 Layout)

Four dataset types testing label-subject relations:
- **Subject relation of label**: Does label vary within subject?
- **Presence of consensus cross-subject EEG marker**: Literature-established biomarker exists?

## Key Findings

1. **Identity Trap is universal** - all FMs show dominant frozen subject-variance
2. **Physically grounded shortcut** - measurable physiological component (aperiodic 1/f)
3. **Subject-disjoint splitting insufficient** - cannot rule out identity shortcuts alone
4. **Erasure improves true signal** - removing subject-axis enhances within-subject label decoding

## Implementation Guidance

### When to Use FMScope

**Trigger conditions:**
- Evaluating EEG FM claims of "cross-subject generalization"
- Subject-disjoint splitting shows unexpectedly high accuracy
- Need to distinguish biomarker learning from shortcut learning
- Comparing frozen vs fine-tuned representations

### Diagnostic Workflow

1. **Compute frozen subject-variance** - quantify dominance ratio
2. **Apply subject-axis erasure** - test removable linear axis hypothesis
3. **Ablate aperiodic 1/f** - check physiological carrier (LaBraM/CBraMod)
4. **Layer-wise probing** - identify where fine-tuning affects representations
5. **Cross-cohort validation** - test erasure improvement on external datasets

### Code Availability

Implementation available at: https://github.com/junyoulin/fmscope

## Paper Reference

**arXiv:2606.06647** (cross-list: cs.LG, q-bio.NC)
- Authors: Jun-You Lin, Ying Choon Wu, Tzyy-Ping Jung
- 28 pages, 6 figures, 8 tables
- Submitted: 2026-06-04

## Significance for Neuroscience AI

This work reveals a fundamental reliability challenge in EEG foundation models - the apparent success may reflect **physically measurable shortcuts** (subject identity via aperiodic features) rather than learned biomarkers. FMScope provides the first diagnostic toolkit to separate these cases.

---

**Activation**: EEG foundation model, subject-disjoint, cross-validation, shortcut learning, identity trap, aperiodic 1/f, frozen representation, diagnostic audit, LaBraM, CBraMod, REVE, FMScope