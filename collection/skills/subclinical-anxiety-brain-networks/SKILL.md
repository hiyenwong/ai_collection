---
name: subclinical-anxiety-brain-networks
description: "Mapping behavioral, physiological, and subjective components of subclinical anxiety to dissociable intrinsic brain networks using resting-state functional connectivity. Two-system framework with rsFC analysis. Trigger words: subclinical anxiety brain networks, rsFC anxiety, anxiety functional connectivity, ACC insula anxiety, hippocampus insula anxiety, threat anticipation anxiety, two-system anxiety framework."
---

# Intrinsic Brain Networks Underlying Subclinical Anxiety

## Overview

Maps the behavioral, physiological, and subjective dimensions of subclinical anxiety to partially dissociable but overlapping intrinsic brain networks using resting-state functional connectivity (rsFC).

## Two-System Framework

Anxiety comprises three components that do not always align:
1. Behavioral: Response patterns (e.g., reaction time under threat)
2. Physiological: Autonomic arousal (e.g., skin conductance)
3. Subjective: Self-reported anxiety severity

## Methodology

### Experimental Design
- Participants: Young adults spanning range of subclinical anxiety levels
- Task: Threat anticipation paradigm measuring:
  - Behavioral: Reaction time under temporally uncertain threat
  - Physiological: Skin conductance response
  - Subjective: NIH Fear-Affect self-report

### Analysis Pipeline
1. Resting-state fMRI acquisition
2. ROI-based rsFC computation
3. Correlation with anxiety measures
4. Sequential family-wise error correction

## Key Findings

### Three Dissociable Connectivity Patterns

| Anxiety Component | Brain Network | Direction |
|------------------|---------------|-----------|
| Behavioral (vigilance) | ACC to Insula | Increased connectivity with anxiety |
| Physiological (arousal) | ACC to OFC | Increased connectivity with arousal |
| Subjective (self-report) | Hippocampus to Insula | Increased connectivity with anxiety |

### Interpretation
- Higher subclinical anxiety: faster responses under uncertain threat (increased vigilance)
- No direct association with physiological arousal at behavioral level
- Each anxiety dimension maps onto a distinct but partially overlapping neural circuit

## Implementation Pattern

```python
def rsfc_anxiety_analysis(rsfc_matrix, roi_labels,
                          behavioral_scores,
                          physiological_scores,
                          subjective_scores):
    """Map anxiety components to rsFC patterns."""
    n_connections = rsfc_matrix.shape[1]
    results = {}
    for component_name, scores in [
        ("behavioral", behavioral_scores),
        ("physiological", physiological_scores),
        ("subjective", subjective_scores)
    ]:
        correlations = []
        p_values = []
        for conn_idx in range(n_connections):
            r, p = stats.pearsonr(rsfc_matrix[:, conn_idx], scores)
            correlations.append(r)
            p_values.append(p)
        corrected_p = multipletests(p_values, method='fdr_bh')[1]
        sig_mask = corrected_p < 0.05
        results[component_name] = {
            "correlations": np.array(correlations),
            "significant_connections": np.where(sig_mask)[0]
        }
    return results
```

## Key Brain Regions

- ACC (Anterior Cingulate Cortex): Conflict monitoring, threat processing
- Insula: Interoception, emotional awareness
- OFC (Orbitofrontal Cortex): Reward/punishment evaluation
- Hippocampus: Contextual memory, pattern separation

## Clinical Implications

- Dissociable neural circuits suggest potential for targeted interventions
- Resting-state connectivity can serve as early neural markers
- Extends task-based findings to resting-state paradigms
- Informs precision psychiatry approaches

## Paper Reference

- arXiv: 2605.00465v1 [q-bio.NC]
- Authors: Shruti Kinger, Mrinmoy Chakrabarty
- Date: 2026-05-01
- Categories: Quantitative Biology - Neuroscience (q-bio.NC)

## Related Skills

- brain-connectivity-analysis
- hermes-brain-connectivity
- time-varying-brain-connectivity
- eeg-tinnitus-biomarker-robustness
