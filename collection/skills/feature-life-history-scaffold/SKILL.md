---
name: feature-life-history-scaffold
description: >
  Feature life history methodology for LLM training dynamics. Identifies the
  carrier scaffold — ~50 sparse features with stable life histories that organize
  the model's representational structure. Training follows two phases: selection
  (first 1%, features emerge/die 40x faster) and calibration (remaining 99%).
  Use when: analyzing LLM training dynamics, studying feature emergence,
  identifying core representational structure, sparse feature analysis,
  cross-layer ablation studies, interpretability. Triggered by: feature life
  history, carrier scaffold, representational backbone, two-phase training,
  sparse features, cross-layer ablation, scaffold hierarchy, Stecher 2026.
---

# Feature Life History & Carrier Scaffold

Methodology from arXiv:2605.18789 (Stecher, Radovanović, Sikimić & Kahle, 2026)
— features in language models have **life history**: they emerge, persist, and
die during training. A persistent representational backbone — the **carrier
scaffold** — of ~50 sparse features organizes the model's structure.

## Core Discovery

Training follows a **two-phase account**:
1. **Selection phase** (first 1% of training): features emerge, die, reorganize
   40× faster; scaffold is largely fixed
2. **Calibration phase** (remaining 99%): geometry calibrates around scaffold

## Four Properties of the Carrier Scaffold

### (i) It Assembles Early
- Features emerge, die, and reorganize **~40× faster** in first 1% of training
- Scaffold is **largely fixed** by that point

### (ii) It Is Load-Bearing
- **Joint cross-layer ablation** identifies carriers as far more load-bearing
  than any count-matched non-scaffold population
- Gap is **invisible to per-firing single-feature methods** — must use joint
  ablation across layers

### (iii) Function Precedes Direction
- Which features will become carriers is **predictable from training-onset
  firing patterns alone**
- Correctly distinguishes future carriers from non-carriers in **4 of 5 cases**
- Prediction works **before the geometry has settled**

### (iv) It Seeds Subsequent Development
- By end of training, scaffold carriers have recruited **64% of all active
  features** into the scaffold hierarchy

## Methodology

### Life History Tracking
```python
def track_feature_life(model, checkpoints, threshold=0.01):
    """Track when features emerge, persist, and die during training."""
    feature_histories = {}
    for i, ckpt in enumerate(checkpoints):
        features = extract_sparse_features(ckpt)
        for feat_id, activation in features.items():
            if feat_id not in feature_histories:
                feature_histories[feat_id] = []
            feature_histories[feat_id].append({
                'step': i,
                'active': activation.mean() > threshold,
                'strength': activation.mean()
            })
    return feature_histories
```

### Carrier Scaffold Identification
```python
def identify_carrier_scaffold(feature_histories, n_carriers=50):
    """Identify the ~50 features that form the stable carrier scaffold."""
    candidates = []
    for feat_id, history in feature_histories.items():
        active_steps = sum(1 for h in history if h['active'])
        stability = active_steps / len(history)
        candidates.append((feat_id, stability, history))
    candidates.sort(key=lambda x: x[1], reverse=True)
    return candidates[:n_carriers]
```

### Joint Cross-Layer Ablation
```python
def joint_cross_layer_ablation(model, feature_ids, test_data):
    """Ablate features jointly across layers to measure load-bearing."""
    baseline = model.evaluate(test_data)
    ablated_model = clone_model(model)
    for layer in ablated_model.layers:
        for feat_id in feature_ids:
            ablate_feature(layer, feat_id)
    ablated_score = ablated_model.evaluate(test_data)
    return baseline - ablated_score  # higher = more load-bearing
```

### Two-Phase Training Analysis
```python
def analyze_training_phases(feature_histories, phase_boundary=0.01):
    """Quantify the two-phase account of training."""
    phase_1_rates, phase_2_rates = [], []
    for feat_id, history in feature_histories.items():
        phase_1 = [h for h in history if h['step'] < phase_boundary * len(history)]
        phase_2 = [h for h in history if h['step'] >= phase_boundary * len(history)]
        phase_1_rates.append(count_state_changes(phase_1) / (phase_boundary * len(history)))
        phase_2_rates.append(count_state_changes(phase_2) / ((1 - phase_boundary) * len(history)))
    return np.mean(phase_1_rates) / np.mean(phase_2_rates)  # expected: ~40x
```

## Key Concepts

- **Feature life history**: trajectory through training (emerge → persist → die)
- **Carrier scaffold**: ~50 sparse features forming the representational backbone
- **Load-bearing**: features whose joint ablation causes significant performance drop
- **Scaffold hierarchy**: structure where carriers recruit other features (64%)
- **Two-phase training**: selection (1%) → calibration (99%)
- **Function precedes direction**: carrier identity predictable from onset firing

## Comparison with Single-Feature Methods

| Method | Detects Load-Bearing | Detects Carriers |
|--------|---------------------|-----------------|
| Per-firing single-feature | No | No |
| Joint cross-layer ablation | Yes | Yes |
| Life history tracking | No | Yes (identity) |

## Practical Applications

- **Efficient fine-tuning**: target the scaffold for minimal intervention
- **Model surgery**: preserve carrier features during model merging
- **Interpretability**: focus on 50 carriers vs. thousands of features
- **Training monitoring**: track scaffold formation as health metric
- **Feature pruning**: safely prune non-scaffold features

## Pitfalls

- **Per-firing methods miss the scaffold**: must use joint cross-layer ablation
- **Requires dense checkpoints**: need many intermediate model saves
- **Model-specific**: scaffold size may vary across architectures
- **Pythia-specific**: validated on Pythia-160M and -410M

## Citation

```bibtex
@article{stecher2026features,
  title={Features have life history. And we should care},
  author={Stecher, Philipp and Radovanović, Sandro and Sikimić, Vlasta and Kahle, Reinhard},
  journal={arXiv preprint arXiv:2605.18789},
  year={2026}
}
```