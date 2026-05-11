---
name: same-brain-different-prediction
description: "EEG decoding reliability assessment methodology addressing preprocessing-induced prediction instability. Demonstrates that up to 42% of trial-level predictions flip when only preprocessing changes, formalizing preprocessing as counterfactual intervention space. Use when: (1) evaluating EEG model reliability, (2) comparing preprocessing pipelines, (3) assessing prediction stability, (4) building robust BCI systems, (5) analyzing preprocessing sensitivity. Activation: EEG preprocessing reliability, prediction stability, counterfactual preprocessing, EEG pipeline comparison, BCI robustness, preprocessing sensitivity."
---

# Same Brain, Different Prediction

EEG decoding reliability methodology showing predictions are unstable across preprocessing pipelines. arXiv:2605.07212 (Hou et al., 2026).

## Core Finding

Across 6 datasets spanning 4 paradigms, **up to 42% of trial-level predictions flip** when only the preprocessing pipeline changes. Standard uncertainty methods don't capture this because they condition on a fixed preprocessing pipeline.

## Framework: Counterfactual Preprocessing Space

Formalize preprocessing choices as an intervention space:

$$P(y|x, \pi)$$

Where $\pi$ is the preprocessing pipeline. The question: how much does $P(y|x, \pi)$ vary as $\pi$ changes?

### Preprocessing Dimensions

| Dimension | Options | Impact |
|-----------|---------|--------|
| Filtering | High-pass cutoff (0.1-1Hz), low-pass cutoff | Major for temporal features |
| Referencing | Average, mastoid, CAR, REST | Major for spatial features |
| Artifact removal | ICA, ASR, regression, none | Major for noisy data |
| Epoching | Window length, baseline correction | Medium |
| Downsampling | Target rate (128-512Hz) | Minor-medium |

## Reliability Metrics

### Prediction Agreement Rate

```python
def prediction_agreement(models, data, pipelines):
    """Measure prediction consistency across preprocessing pipelines."""
    all_predictions = {}
    
    for pi_name, pi_func in pipelines.items():
        processed = pi_func(data)
        preds = models[pi_name].predict(processed)
        all_predictions[pi_name] = preds
    
    # Pairwise agreement
    pipeline_names = list(pipelines.keys())
    agreements = {}
    
    for i in range(len(pipeline_names)):
        for j in range(i+1, len(pipeline_names)):
            p1 = all_predictions[pipeline_names[i]]
            p2 = all_predictions[pipeline_names[j]]
            agreements[f"{pipeline_names[i]} vs {pipeline_names[j]}"] = np.mean(p1 == p2)
    
    return agreements
```

### Counterfual Flip Rate

```python
def counterfactual_flip_rate(predictions_dict):
    """Fraction of trials where prediction changes across pipelines."""
    n_trials = len(list(predictions_dict.values())[0])
    n_pipelines = len(predictions_dict)
    
    # For each trial, check if all pipelines agree
    all_agree = np.zeros(n_trials, dtype=bool)
    for trial_idx in range(n_trials):
        preds = [predictions_dict[pi][trial_idx] for pi in predictions_dict]
        all_agree[trial_idx] = len(set(preds)) == 1
    
    flip_rate = 1 - np.mean(all_agree)
    return flip_rate
```

## Practical Guidelines

### For Researchers

1. **Report preprocessing details** - Pipeline choices dramatically affect results
2. **Run sensitivity analysis** - Test multiple reasonable pipelines
3. **Use ensemble predictions** - Average across pipelines for stability
4. **Document pipeline selection rationale** - Why this cutoff? Why this reference?

### For BCI Systems

1. **Pipeline-agnostic features** - Prefer features stable across preprocessing
2. **Online monitoring** - Track prediction confidence as reliability proxy
3. **Adaptive pipelines** - Adjust preprocessing based on signal quality
4. **Report worst-case** - Not just best-pipeline accuracy

## Comparison with Standard Approaches

| Method | Captures | Misses |
|--------|----------|--------|
| Cross-validation | Model variance | Preprocessing variance |
| Test-retest | Biological variance | Pipeline variance |
| This framework | Preprocessing-induced instability | Biological variance |

## Key Takeaway

Preprocessing is not a neutral choice - it's a hyperparameter that fundamentally shapes what your model learns. Always report and test preprocessing sensitivity.
