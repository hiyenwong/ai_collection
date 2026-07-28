---
name: eeg-fm-stress-testing-clinical-decoding
title: EEG Foundation Model Stress Testing for Clinical Decoding
description: Comprehensive benchmarking framework for stress-testing EEG foundation models with dataset identity analysis and targeted negative controls to evaluate clinical decoding robustness.
trigger_words: [eeg foundation models, stress testing, clinical decoding, dataset identity, negative controls, frozen linear probes]
---

# EEG Foundation Model Stress Testing for Clinical Decoding

## Overview
This methodology provides a **comprehensive stress-testing framework** for evaluating pretrained EEG foundation models in clinical decoding tasks. The approach benchmarks multiple models across diverse clinical tasks and datasets using rigorous evaluation protocols including **dataset identity analysis** and **targeted negative controls** to reveal hidden biases and limitations.

## Core Contributions
- **Multi-model Benchmark**: Evaluation of six EEG foundation models (LaBraM, EEGMamba, CBraMod, REVE, BENDR, BIOT)
- **Clinical Task Diversity**: Five clinical tasks across four datasets including dementia, Alzheimer's, and ictal detection
- **Evaluation Unit Analysis**: Comparison of leave-one-subject-out, subject-grouped, and recording-level splits
- **Targeted Negative Controls**: Random initialization, random features, label permutation, scrambled-label fine-tuning, projection sensitivity
- **Dataset Identity Detection**: Quantification of dataset-specific biases in frozen embeddings

## Key Findings
1. **Performance Variability**: Frozen REVE achieves 0.568 AUROC on Korean dementia vs 0.769 for classical features
2. **Dataset Identity Bias**: Frozen embeddings decode dataset identity with AUROC 1.000 at PCA-50 (0.9998 after preprocessing)
3. **Random Initialization Superiority**: Randomly initialized encoder outperforms pretrained REVE on Korean diagnosis (0.659 vs 0.570)
4. **Classical Features Advantage**: Classical features nominally exceed REVE on Alzheimer's disease at subject level
5. **Controlled Positive Result**: Cross-subject ictal detection shows clear benefit (REVE: 0.793 AUROC, +9.2% over random)

## Implementation Guidelines

### Benchmark Setup
```python
# Stress-testing framework for EEG foundation models
class EEGStressTest:
    def __init__(self, models, datasets, clinical_tasks):
        self.models = models  # List of foundation models
        self.datasets = datasets  # Multiple clinical datasets
        self.tasks = clinical_tasks  # Clinical decoding tasks
        
    def run_comprehensive_benchmark(self):
        results = {}
        for model_name in self.models:
            model = load_pretrained_model(model_name)
            for dataset_name, dataset in self.datasets.items():
                for task in self.tasks[dataset_name]:
                    # Test different evaluation units
                    results[f"{model_name}_{dataset_name}_{task}"] = {
                        'subject_level': self.evaluate_subject_level(model, dataset, task),
                        'recording_level': self.evaluate_recording_level(model, dataset, task),
                        'negative_controls': self.run_negative_controls(model, dataset, task)
                    }
        return results
```

### Evaluation Protocols
1. **Frozen Linear Probes**: Use pretrained encoders with frozen weights
2. **Multiple Split Strategies**: 
   - Leave-one-subject-out (LOSO)
   - Subject-grouped splits
   - Explicitly identified recording-level splits
3. **Negative Control Suite**:
   - Random initialization baseline
   - Random features comparison
   - Label permutation test
   - Scrambled-label fine-tuning
   - Projection sensitivity analysis

### Dataset Identity Analysis
```python
# Detect dataset identity bias in embeddings
def analyze_dataset_identity(embeddings, dataset_labels, preprocessing=True):
    if preprocessing:
        # Apply band restriction and per-epoch z-scoring
        embeddings = apply_band_restriction(embeddings)
        embeddings = per_epoch_z_score(embeddings)
    
    # PCA dimensionality reduction
    pca_50 = PCA(n_components=50).fit_transform(embeddings)
    
    # Train classifier to detect dataset identity
    clf = LogisticRegression()
    scores = cross_val_score(clf, pca_50, dataset_labels, cv=5, scoring='roc_auc')
    return np.mean(scores)
```

## Use Cases
- **Model Validation**: Rigorous evaluation of EEG foundation models before clinical deployment
- **Bias Detection**: Identifying dataset-specific biases that could lead to false conclusions
- **Comparative Analysis**: Fair comparison between foundation models and classical features
- **Clinical Translation**: Understanding real-world performance limitations for medical applications
- **Research Reproducibility**: Standardized stress-testing protocol for future studies

## Pitfalls & Considerations
- **Evaluation Unit Dependency**: Results vary significantly based on split strategy (subject vs recording level)
- **Dataset Shift Sensitivity**: Performance degrades substantially under distribution shift
- **Comparator Strength**: Choice of baseline significantly affects conclusions
- **Hidden Biases**: Dataset identity can be decoded even from heavily preprocessed embeddings
- **Task Specificity**: Benefits may only appear in specific clinical tasks (e.g., ictal detection)

## Best Practices
1. **Always Include Negative Controls**: Test against random initialization and random features
2. **Use Multiple Evaluation Units**: Report results for both subject-level and recording-level splits
3. **Analyze Dataset Identity**: Quantify dataset-specific biases in embeddings
4. **Compare to Classical Features**: Benchmark against established classical feature pipelines
5. **Report Full Results**: Include both positive and negative findings transparently

## Activation Keywords
eeg foundation models, stress testing, clinical decoding, dataset identity, negative controls, frozen linear probes, leave-one-subject-out, recording-level splits, random initialization, classical features, ictal detection, dementia classification, alzheimer's disease

## References
- Zare, M. (2026). Stress-Testing EEG Foundation Models for Clinical Decoding: Dataset Identity and Targeted Negative Controls. arXiv:2607.24519 [cs.LG]