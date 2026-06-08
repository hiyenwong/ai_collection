---
name: identity-trap-eeg-foundation-models
description: "The Identity Trap in EEG Foundation Models: A Diagnostic Audit — FMScope protocol for detecting subject-identity shortcut learning in EEG FMs before fine-tuning. Five diagnostics: variance decomposition, subject-axis erasure, 1/f ablation, layer probing, direction consistency. Activation: identity trap, EEG foundation model, shortcut learning, subject identity, FMScope, LaBraM, CBraMod, REVE, diagnostic audit."
---

## Context

EEG foundation models report strong accuracy on clinical resting-state EEG. However, high accuracy under subject-disjoint cross-validation can reflect either genuine clinical biomarkers or subject-identity features correlating with the label. This paper introduces **FMScope** — a frozen-representation protocol diagnosing the Identity Trap at representation level.

**Key Finding**: Identity Trap is universal — frozen subject-variance is 13-89x random null in 12/12 dataset pairs, rising under fine-tuning.

**Paper**: arXiv:2606.06647 (Jun-You Lin et al., 2026-06-04)
**Category**: cs.LG + q-bio.NC (Machine Learning + Neurons and Cognition)
**Pages**: 28 pages, 6 figures, 8 tables

## Core Methodology

### 1. The Identity Trap Definition

**Problem**: Subject-disjoint splitting alone cannot rule out shortcut learning when:
- Subject-identity features correlate with clinical labels
- Cross-validation may not expose representation-level shortcuts
- High accuracy may reflect physiological identity rather than pathology

**Physical Basis**: Subject identity has measurable physiological component (aperiodic 1/f signal)

### 2. FMScope Protocol (Five Diagnostics)

#### Diagnostic 1: Variance Decomposition
```python
# Measure frozen subject-variance vs label-variance
subject_variance = variance_along_subject_axis(frozen_repr)
label_variance = variance_along_label_axis(frozen_repr)
null_variance = variance_random_null(frozen_repr)

# Identity Trap indicator
trap_ratio = subject_variance / null_variance  # 13-89x = trap detected
```

#### Diagnostic 2: Subject-Axis Erasure
```python
# Erase subject-identity linear axis from frozen representation
erased_repr = remove_subject_axis(frozen_repr)

# Check improvement in label decoding
delta_accuracy = label_decode(erased_repr) - label_decode(frozen_repr)
# +6 to +12 pp improvement = subject-axis was shortcut
```

#### Diagnostic 3: Aperiodic 1/f Ablation
```python
# Remove aperiodic component from EEG input
ablated_eeg = remove_aperiodic_1f(raw_eeg)

# Measure subject probe drop
delta_subject_probe = subject_probe(ablated_eeg) - subject_probe(raw_eeg)
# -9 to -19 pp on LaBraM/CBraMod = 1/f carries subject identity
# REVE: no change = saturates identity without 1/f dependence
```

#### Diagnostic 4: Layer-wise Label Probing
```python
# Probe each layer for label information
for layer in range(num_layers):
    probe_accuracy[layer] = linear_probe(
        frozen_repr[layer], 
        labels
    )

# Fine-tuning amplifies label-variance only where literature marker exists
```

#### Diagnostic 5: Within-Subject Direction Consistency
```python
# Check if label direction consistent within subject
consistency = within_subject_label_consistency(frozen_repr)

# High consistency = genuine marker
# Low consistency = subject-identity shortcut
```

### 3. 2x2 Experimental Layout

| Factor 1: Subject Relation of Label | Factor 2: Cross-Subject EEG Marker |
|-------------------------------------|-----------------------------------|
| **Within-Subject** | **No Marker** → Primary Trap Cells |
| **Between-Subject** | **Marker Exists** → Fine-tuning Amplifies |

**Primary Cells**: Label varies within subject + no consensus marker → Identity Trap most severe

### 4. Tested Models

- **LaBraM**: Subject probe drops 9-19 pp with 1/f ablation
- **CBraMod**: Similar 1/f dependence as LaBraM
- **REVE**: Saturates subject identity without measurable aperiodic dependence

## Implementation Steps

### Step 1: Load Frozen EEG Foundation Model

```python
from transformers import AutoModel

# Load pretrained EEG FM (LaBraM, CBraMod, REVE)
model = AutoModel.from_pretrained("path/to/eeg_fm")
model.eval()  # Freeze for representation extraction
```

### Step 2: Extract Frozen Representations

```python
def extract_frozen_repr(model, eeg_batch):
    """Extract frozen representation before fine-tuning."""
    with torch.no_grad():
        repr = model.encoder(eeg_batch)  # Frozen encoder output
    return repr
```

### Step 3: Run FMScope Diagnostics

```python
def run_fmscope(model, dataset, labels, subjects):
    """Complete FMScope diagnostic audit."""
    frozen_repr = extract_frozen_repr(model, dataset)
    
    results = {
        'variance_decomposition': variance_decomp(frozen_repr, subjects),
        'subject_axis_erasure': subject_erasure_test(frozen_repr, labels),
        'aperiodic_ablation': aperiodic_test(model, dataset, subjects),
        'layer_probing': layer_probe_audit(frozen_repr, labels),
        'direction_consistency': consistency_check(frozen_repr, subjects, labels)
    }
    
    return results
```

### Step 4: Interpret Identity Trap Severity

```python
def interpret_trap(results):
    """
    Classify Identity Trap severity based on FMScope results.
    """
    severity = 'low'
    
    # Subject-variance dominance
    if results['variance_decomposition']['trap_ratio'] > 13:
        severity = 'moderate'
    
    # Subject-axis erasure improves label decoding
    if results['subject_axis_erasure']['delta'] > 6:
        severity = 'severe'
    
    # 1/f ablation drops subject probe
    if results['aperiodic_ablation']['delta'] > -9:
        severity = 'physiologically-grounded'
    
    return severity
```

## Key Results

### Main Finding 1: Universal Identity Trap
- Frozen subject-variance 13-89x random null in **12/12 dataset pairs**
- Fine-tuning amplifies subject dominance (+10 to +63 pp)
- Subject-axis is removable linear component

### Main Finding 2: 1/f as Subject Carrier
- Aperiodic 1/f signal carries subject identity for LaBraM/CBraMod
- Removing it drops subject probe by 9-19 pp
- REVE saturates identity without measurable 1/f dependence

### Main Finding 3: Fine-Tuning Selectivity
- Fine-tuning amplifies label-variance **only where cross-subject marker exists**
- No marker → fine-tuning amplifies shortcut
- Marker exists → fine-tuning amplifies genuine signal

## Pitfalls

- **Subject-Disposition Splitting Insufficient**: Cannot detect representation shortcuts alone
- **Frozen Protocol Limitation**: Diagnostics run before fine-tuning; post-tuning behavior may differ
- **1/f Removal Complexity**: Requires FOOOF or similar spectral parameterization
- **External Cohort Generalization**: Identity Trap severity varies across datasets
- **Physiological Grounding**: 1/f is biologically meaningful; complete removal may harm legitimate signal

## Verification

- Tested on 4 datasets in 2x2 layout
- 12/12 pairs show Identity Trap (subject-variance 13-89x null)
- Subject-axis erasure improves decoding in primary cells (+6 to +12 pp)
- External cohort transfer: +4 to +27 pp improvement after erasure
- Layer-wise probing confirms fine-tuning selectivity

## Clinical Implications

- **Diagnostic**: Use FMScope before deploying EEG FMs clinically
- **Mitigation**: Erase subject-axis for within-subject varying labels
- **Validation**: Check 1/f dependence to understand shortcut mechanism
- **Future Work**: Develop subject-invariant EEG FMs

## Activation

- identity trap
- EEG foundation model
- FMScope
- shortcut learning
- subject identity
- LaBraM
- CBraMod
- REVE
- diagnostic audit
- variance decomposition
- aperiodic 1/f
- frozen representation