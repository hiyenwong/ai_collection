---
name: same-brain-different-prediction
description: "EEG decoding reliability methodology addressing preprocessing-induced prediction instability. Formalizes preprocessing choices as a counterfactual intervention space and demonstrates that preprocessing decisions significantly undermine model reliability across BCI paradigms. Use when: (1) designing EEG/MEG decoding studies, (2) evaluating model reliability, (3) comparing preprocessing pipelines, (4) building robust BCI systems, (5) writing methods sections for neuroimaging papers, (6) conducting reproducibility audits, (7) assessing prediction stability across data transformations. Activation keywords: EEG preprocessing reliability, prediction stability, counterfactual preprocessing, EEG pipeline comparison, BCI robustness, preprocessing sensitivity, neural decoding reproducibility, EEG methodological rigor, preprocessing intervention."
arxiv: "2605.07212"
authors: "Dengzhe Hou, Zihao Wu, Lingyu Jiang et al."
category: methodology
---

# Same Brain, Different Prediction: How Preprocessing Choices Undermine EEG Decoding Reliability

**arXiv:2605.07212** | Hou, Wu, Jiang et al. (2026)

## Overview

EEG is a cornerstone of brain-computer interfaces (BCIs) and clinical neuroscience. Deep learning models for neural decoding are typically trained and evaluated under a **single, unreported preprocessing pipeline**. This paper reveals that this common practice masks a fundamental source of instability: preprocessing choices themselves act as a hidden confounder that can dramatically alter model predictions from the same neural data.

## Core Finding

**Up to 42% of trial-level predictions flip** when only the preprocessing pipeline changes — with the underlying brain data held identical. Standard uncertainty quantification methods (cross-validation, test-retest) fail to capture this because they condition on a fixed preprocessing pipeline.

## The Preprocessing Intervention Framework

### Counterfactual Formalization

The authors formalize preprocessing as a **counterfactual intervention space**:

$$P(y|x, \pi)$$

Where $y$ is the model prediction, $x$ is the raw EEG signal, and $\pi$ is the preprocessing pipeline. The critical question: how much does $P(y|x, \pi)$ vary as $\pi$ changes, holding $x$ constant?

### Preprocessing Dimensions

| Dimension | Common Choices | Reliability Impact |
|-----------|---------------|-------------------|
| **Filtering** | High-pass cutoff (0.1–1 Hz), low-pass cutoff, notch | Major — reshapes temporal features |
| **Referencing** | Average reference, mastoid, CAR, REST | Major — reshapes spatial features |
| **Artifact removal** | ICA, ASR, regression, none | Major — alters signal-to-noise |
| **Epoching** | Window length, baseline correction | Medium — affects temporal alignment |
| **Downsampling** | Target rate (128–512 Hz) | Minor–medium — information loss |

### Key Insight

Preprocessing is **not a neutral data preparation step** — it is a set of methodological choices that fundamentally determines what information is available to the model. Different "reasonable" pipelines expose different aspects of the same neural signal, leading to different predictions.

## Impact on EEG Decoding Reliability

### What This Means for Research

- **Single-pipeline evaluation overestimates reliability**: A model that achieves 85% accuracy under one pipeline may drop significantly under another
- **Results are pipeline-dependent, not just data-dependent**: Two labs studying the same phenomenon with different preprocessing can reach contradictory conclusions
- **Standard validation is insufficient**: Cross-validation measures variance within a pipeline, not across pipelines
- **Reproducibility crisis in neural decoding**: Unreported preprocessing choices make it impossible to replicate or compare studies

### Comparison with Standard Reliability Methods

| Method | Captures | Misses |
|--------|----------|--------|
| Cross-validation | Model variance (fixed pipeline) | Preprocessing variance |
| Test-retest reliability | Biological variance | Pipeline variance |
| Confidence intervals | Prediction uncertainty (fixed pipeline) | Pipeline-induced uncertainty |
| **Preprocessing intervention** | **Pipeline-induced instability** | Biological variance |

## Best Practices for Preprocessing Reporting

### Minimum Reporting Standards

When publishing EEG decoding results, report:

1. **Complete pipeline specification**
   - Filter types, cutoff frequencies, filter order
   - Referencing method and rationale
   - Artifact detection and removal approach
   - Epoching parameters (window, baseline)
   - Downsampling rate and anti-aliasing

2. **Pipeline selection rationale**
   - Why this high-pass cutoff? Why this reference?
   - Was this choice data-driven or convention-driven?

3. **Sensitivity analysis**
   - Results under at least 2–3 alternative reasonable pipelines
   - Report prediction stability (agreement rate) across pipelines
   - Flag trials with inconsistent predictions

4. **Code and configuration**
   - Share complete preprocessing scripts
   - Version all preprocessing libraries (MNE, EEGLAB, etc.)

### Preprocessing Sensitivity Checklist

```
□ Multiple high-pass cutoffs tested (e.g., 0.1 Hz, 0.5 Hz, 1 Hz)
□ Alternative referencing schemes compared
□ Artifact removal approaches documented
□ Prediction agreement rate across pipelines reported
□ Pipeline-dependent results flagged in discussion
□ Full preprocessing code shared
```

## Practical Guidance

### For Researchers Designing EEG Studies

1. **Pre-register preprocessing choices** before seeing results
2. **Run multi-pipeline analysis** as standard practice, not as an afterthought
3. **Report worst-case performance** alongside best-pipeline accuracy
4. **Use preprocessing-agnostic features** when possible
5. **Treat preprocessing as a hyperparameter** with its own sensitivity analysis

### For BCI System Development

1. **Pipeline robustness testing** should be part of system validation
2. **Ensemble across pipelines** for more stable predictions in deployment
3. **Monitor prediction consistency** in real-time as a reliability proxy
4. **Adaptive preprocessing** — adjust pipeline based on signal quality metrics
5. **Document pipeline versioning** for longitudinal BCI applications

### For Clinical Neuroscience

1. **Diagnostic decisions should be preprocessing-aware** — different pipelines may yield different clinical interpretations
2. **Multi-pipeline consensus** for critical clinical decisions
3. **Standardized preprocessing protocols** for clinical BCI applications
4. **Report preprocessing variance** alongside clinical outcome metrics

## Implementation

### Measuring Prediction Agreement Across Pipelines

```python
import numpy as np

def prediction_agreement_rate(predictions_dict):
    """Fraction of trials where all pipelines agree on prediction."""
    n_trials = len(list(predictions_dict.values())[0])
    agreements = np.zeros(n_trials, dtype=bool)
    for i in range(n_trials):
        preds = [predictions_dict[pi][i] for pi in predictions_dict]
        agreements[i] = len(set(preds)) == 1
    return np.mean(agreements)

def counterfactual_flip_rate(predictions_dict):
    """Fraction of trials where prediction flips across at least one pipeline pair."""
    return 1 - prediction_agreement_rate(predictions_dict)

def pairwise_agreement_matrix(predictions_dict):
    """Pairwise agreement rates between all pipeline combinations."""
    pipeline_names = list(predictions_dict.keys())
    n = len(pipeline_names)
    matrix = np.eye(n)
    for i in range(n):
        for j in range(i+1, n):
            p1 = predictions_dict[pipeline_names[i]]
            p2 = predictions_dict[pipeline_names[j]]
            agreement = np.mean(np.array(p1) == np.array(p2))
            matrix[i,j] = matrix[j,i] = agreement
    return matrix, pipeline_names
```

### Multi-Pipeline Evaluation Pattern

```python
# Define alternative reasonable pipelines
pipelines = {
    "hp0.1_avg_ref": lambda x: preprocess(x, hp=0.1, ref='average'),
    "hp0.5_mastoid": lambda x: preprocess(x, hp=0.5, ref='mastoid'),
    "hp1.0_CAR":     lambda x: preprocess(x, hp=1.0, ref='CAR'),
}

# Train and evaluate under each pipeline
results = {}
for name, pipeline in pipelines.items():
    processed = pipeline(raw_eeg)
    model = train_and_evaluate(processed, labels)
    results[name] = model.predict(processed)

# Report sensitivity
flip_rate = counterfactual_flip_rate(results)
print(f"Counterfactual flip rate: {flip_rate:.1%}")
```

## When to Apply These Insights

### Apply This Skill When:

- Designing or reviewing EEG/MEG decoding experiments
- Writing or reviewing methods sections for neural decoding papers
- Building or evaluating BCI systems for research or clinical use
- Conducting reproducibility audits of published neural decoding results
- Comparing results across studies with different preprocessing
- Teaching neural decoding methodology
- Pre-registering neuroimaging studies

### Do NOT Apply When:

- Working with non-neural time series data (different artifact profiles)
- The preprocessing pipeline is fully standardized and validated (e.g., FDA-approved clinical pipeline)
- Only interested in within-pipeline model comparisons

## Key Takeaway

> **Preprocessing is not a neutral preprocessing step — it is a set of methodological choices that fundamentally determines what your model learns and predicts.**
>
> Always report, test, and account for preprocessing sensitivity in neural decoding research. The same brain can yield different predictions under different preprocessing pipelines.

## Resources

- **Paper**: arXiv:2605.07212 — "Same Brain, Different Prediction: How Preprocessing Choices Undermine EEG Decoding Reliability"
- **Related frameworks**: MNE-Python preprocessing pipelines, BIDS-EEG standardization

## Related Skills

- eeg-brain-connectivity-bci: EEG connectivity analysis for BCI
- eccentricity-confound-eeg-visual-attention-decoding: Confound control in EEG decoding
- saliency-aware-eeg-decoding: Interpretable EEG decoding methods
