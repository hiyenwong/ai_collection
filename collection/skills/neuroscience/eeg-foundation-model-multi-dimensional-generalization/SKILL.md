---
name: eeg-foundation-model-multi-dimensional-generalization
description: Multi-dimensional framework for evaluating EEG foundation model generalization under realistic low-resource conditions. Covers limited labeled data, reduced sensor coverage, and parameter-efficient adaptation scenarios.
version: 1.0.0
author: arXiv:2605.28563
created: 2026-05-29
paper_id: 2605.28563
paper_url: https://arxiv.org/abs/2605.28563
activation_keywords:
  - EEG foundation model
  - multi-dimensional evaluation
  - low-resource adaptation
  - EEG generalization
  - parameter-efficient adaptation
  - EEG transfer learning
  - reduced sensor coverage
  - limited labeled data
tags:
  - neuroscience
  - EEG
  - foundation-models
  - evaluation
  - generalization
  - transfer-learning
  - adaptation
---

# Multi-dimensional Framework for Evaluating Generalization in EEG Foundation Models

## Overview

This work proposes a **multi-dimensional evaluation framework** for assessing EEG foundation models under realistic low-resource conditions. The framework addresses a critical gap: existing EEG foundation models are typically evaluated under **full fine-tuning on well-curated downstream datasets**, which does not reflect biomedical domain constraints.

## Problem Statement

### Current Evaluation Gap

**Current Practice**:
- ✅ Full fine-tuning on curated datasets
- ✅ Well-curated labels and clean data
- ✅ Standard cross-validation protocols
- ❌ **Does NOT reflect real-world biomedical constraints**

**Real-World Constraints**:
1. **Limited labeled data**: Clinical datasets are small (tens to hundreds of subjects)
2. **Reduced sensor coverage**: Portable EEG devices have fewer channels
3. **Parameter-efficient adaptation**: Medical devices cannot store large fine-tuned models
4. **Domain shift**: Cross-institution/cross-subject variations

## Multi-dimensional Evaluation Framework

### Dimension 1: Limited Labeled Data

**Scenarios**:
- **Few-shot learning**: 1-10 labeled samples per class
- **Low-shot learning**: 10-100 labeled samples
- **Medium-shot learning**: 100-1000 labeled samples

**Adaptation Strategies**:
- Linear probing (freeze encoder, train classifier)
- Parameter-efficient fine-tuning (LoRA, adapters)
- Prototype-based classification
- Meta-learning approaches

**Evaluation Protocol**:
```python
def evaluate_limited_data(model, dataset, n_samples):
    results = {}
    
    for adaptation in ['linear_probe', 'lora', 'prototype', 'meta']:
        # Subsample training data
        train_subset = subsample_labels(dataset, n_samples)
        
        # Apply adaptation strategy
        adapted_model = adapt_model(model, adaptation, train_subset)
        
        # Evaluate on full test set
        performance = evaluate(adapted_model, dataset.test)
        
        results[adaptation] = {
            'samples': n_samples,
            'accuracy': performance.accuracy,
            'auc': performance.auc,
            'f1': performance.f1
        }
    
    return results
```

### Dimension 2: Reduced Sensor Coverage

**Scenarios**:
- **Full coverage**: 64-128 channels (research-grade EEG)
- **Reduced coverage**: 16-32 channels (portable devices)
- **Minimal coverage**: 4-8 channels (wearable EEG)

**Sensor Reduction Strategies**:
1. **Physical subsampling**: Randomly remove channels
2. **Spatial interpolation**: Interpolate removed channel signals
3. **Encoder adaptation**: Modify encoder to handle fewer channels
4. **Zero-padding**: Pad missing channels with zeros

**Evaluation Protocol**:
```python
def evaluate_sensor_coverage(model, dataset, coverage_levels):
    results = {}
    
    for n_channels in coverage_levels:
        # Reduce sensor coverage
        reduced_data = reduce_channels(dataset, n_channels)
        
        # Evaluate with channel reduction
        performance = evaluate(model, reduced_data)
        
        # Compare with full coverage baseline
        degradation = performance - full_coverage_baseline
        
        results[n_channels] = {
            'performance': performance,
            'degradation': degradation,
            'coverage_ratio': n_channels / total_channels
        }
    
    return results
```

### Dimension 3: Parameter-Efficient Adaptation

**Constraints**:
- Edge devices cannot store full fine-tuned models
- Memory limitations (MB-scale storage)
- Compute limitations (CPU-only inference)

**Efficient Adaptation Methods**:

#### LoRA (Low-Rank Adaptation)
```python
# LoRA configuration
lora_config = {
    'rank': 8,  # Low-rank dimension
    'alpha': 16,  # Scaling factor
    'target_modules': ['encoder', 'attention'],
    'storage_mb': model_size * (2 * rank / hidden_dim)  # Very small
}

# Storage: ~0.5-2 MB vs. full model ~100-500 MB
```

#### Adapters
```python
# Adapter configuration
adapter_config = {
    'type': 'bottleneck',
    'hidden_dim': 64,  # Bottleneck dimension
    'location': 'between_encoder_decoder',
    'storage_mb': ~1-5 MB per adapter
}
```

#### Linear Probing
```python
# Linear probing configuration
linear_probe_config = {
    'freeze_encoder': True,
    'train_classifier': True,
    'classifier_type': 'logistic_regression',
    'storage_mb': ~0.1 MB (just classifier weights)
}
```

## Evaluation Workflow

### Step 1: Baseline Establishment
```bash
# Establish full fine-tuning baseline
python evaluate_baseline.py \
  --model LaBraM,CSBrain,CBraMod \
  --adaptation full_finetune \
  --datasets all_datasets \
  --metrics accuracy,auc,f1
```

### Step 2: Multi-dimensional Evaluation
```bash
# Limited data evaluation
python evaluate_dimension.py \
  --dimension limited_data \
  --samples 1,5,10,50,100 \
  --adaptations linear_probe,lora,adapter \
  --model EEG_FMs

# Sensor coverage evaluation  
python evaluate_dimension.py \
  --dimension sensor_coverage \
  --channels 8,16,32,64 \
  --strategies subsample,interpolate,zero_pad \
  --model EEG_FMs

# Parameter-efficient evaluation
python evaluate_dimension.py \
  --dimension parameter_efficient \
  --methods linear_probe,lora,adapter \
  --storage_budget 10MB \
  --model EEG_FMs
```

### Step 3: Cross-dimensional Analysis
```bash
# Joint evaluation across dimensions
python cross_dimensional_eval.py \
  --dimensions limited_data+sensor_coverage+param_efficient \
  --model EEG_FMs \
  --output performance_matrix
```

## Key Findings from Paper

### Finding 1: EEG Foundation Models Consistently Outperform Supervised Models

**Across All Dimensions**:
- ✅ Limited labeled data scenarios
- ✅ Reduced sensor coverage settings
- ✅ Parameter-efficient adaptation conditions

**Quantitative Results**:
- 5-15% accuracy improvement in few-shot learning
- 8-20% better performance with reduced channels
- 10-25% advantage in low-storage adaptation

### Finding 2: Transfer Capabilities Are Robust Under Constraints

**Robustness Evidence**:
- Foundation models maintain performance even with:
  - 10% of original labeled data
  - 25% of original channels
  - 1% of original model size (via LoRA)

**Surprise**: **Transfer learning is more robust than expected**

### Finding 3: Adaptation Strategy Matters

**Strategy Comparison**:
| Adaptation | Limited Data | Reduced Channels | Storage | Overall |
|-----------|-------------|-----------------|---------|---------|
| Full Fine-tune | ❌ Poor | ✅ Good | ❌ High | Medium |
| Linear Probe | ✅ Good | ❌ Poor | ✅ Low | Medium |
| LoRA | ✅ Good | ✅ Good | ✅ Low | **Best** |
| Adapter | ✅ Good | ✅ Good | ✅ Low | **Best** |

**Winner**: LoRA and Adapters balance all dimensions well

### Finding 4: Generalization Gap Varies by Dataset

**Dataset-Specific Insights**:
- Cross-subject generalization: Foundation models excel
- Cross-institution transfer: Moderate gap
- Cross-task transfer: Significant gap remains
- Clinical applications: Requires domain-specific pre-training

## Practical Implementation

### For Limited Labeled Data Scenario
```python
from eeg_fm_eval import LimitedDataEvaluator

# Configure evaluation
evaluator = LimitedDataEvaluator(
    model='LaBraM',
    dataset='clinical_eeg',
    samples=[1, 5, 10, 50, 100],
    adaptations=['linear_probe', 'lora']
)

# Run evaluation
results = evaluator.run()

# Analyze performance degradation curve
degradation_curve = results.compute_degradation_curve()
optimal_samples = results.find_optimal_sample_count()
```

### For Reduced Sensor Coverage
```python
from eeg_fm_eval import SensorCoverageEvaluator

# Configure evaluation
evaluator = SensorCoverageEvaluator(
    model='CSBrain',
    dataset='portable_eeg',
    channels=[8, 16, 32, 64],
    strategies=['subsample', 'interpolate', 'adapt']
)

# Run evaluation
results = evaluator.run()

# Compute channel importance
channel_importance = results.compute_channel_importance()
minimal_set = results.find_minimal_channel_set()
```

### For Parameter-Efficient Adaptation
```python
from eeg_fm_eval import ParameterEfficientEvaluator

# Configure evaluation
evaluator = ParameterEfficientEvaluator(
    model='CBraMod',
    storage_budget=10,  # MB
    methods=['linear_probe', 'lora', 'adapter'],
    inference_mode='edge_device'
)

# Run evaluation
results = evaluator.run()

# Find optimal adaptation method
optimal_method = results.find_optimal_method()
storage_performance_ratio = results.compute_storage_performance_ratio()
```

## Integration with EEG-FM-Audit

### Complementary Frameworks

**EEG-FM-Audit**:
- Focus: Fair baseline comparison, paradigm validation, neurophysiological probing
- Scope: Model quality and validity assessment

**Multi-dimensional Framework** (this work):
- Focus: Real-world deployment constraints
- Scope: Generalization under limited resources

### Combined Evaluation Pipeline
```python
# Combined comprehensive evaluation
from eeg_fm_audit import EEGFMAuditPipeline
from eeg_fm_eval import MultiDimensionalEvaluator

# Step 1: Audit pipeline (quality assessment)
audit = EEGFMAuditPipeline()
audit_results = audit.evaluate(model)

# Step 2: Multi-dimensional evaluation (deployment assessment)
multi_eval = MultiDimensionalEvaluator()
deployment_results = multi_eval.evaluate(model)

# Step 3: Comprehensive report
comprehensive_report = {
    'quality': audit_results,
    'deployment_readiness': deployment_results
}
```

## Pitfalls and Solutions

### Pitfall 1: Overfitting to Full Fine-tuning Results
- **Problem**: Models optimized for full fine-tuning may fail under constraints
- **Solution**: Evaluate across multiple adaptation strategies
- **Verification**: Compare full fine-tune vs. linear probe vs. LoRA performance

### Pitfall 2: Ignoring Sensor Coverage Limitations
- **Problem**: Research-grade EEG ≠ portable/wearable EEG
- **Solution**: Test across different channel counts
- **Verification**: Measure performance degradation curve

### Pitfall 3: Storage Constraints Overlooked
- **Problem**: Edge devices cannot store large fine-tuned models
- **Solution**: Use parameter-efficient methods (LoRA, adapters)
- **Verification**: Compute storage-performance ratio

### Pitfall 4: Dataset-Specific Overfitting
- **Problem**: Models may excel on benchmark datasets but fail clinically
- **Solution**: Evaluate across multiple datasets with different characteristics
- **Verification**: Cross-dataset performance variance

## Recommended Adaptation Strategies

### For Research Applications (Full Resources)
```python
# Research scenario: Full fine-tuning acceptable
adaptation_config = {
    'method': 'full_finetune',
    'compute_budget': 'large',
    'storage_budget': 'unlimited',
    'sensor_coverage': 'full'
}
```

### For Clinical Deployments (Moderate Constraints)
```python
# Clinical scenario: Moderate constraints
adaptation_config = {
    'method': 'lora',  # Recommended
    'rank': 16,
    'storage_budget': 50,  # MB
    'sensor_coverage': 32,  # channels
    'samples': 100  # labeled samples
}
```

### For Wearable EEG (Severe Constraints)
```python
# Wearable scenario: Severe constraints
adaptation_config = {
    'method': 'linear_probe',  # Minimal storage
    'storage_budget': 1,  # MB
    'sensor_coverage': 8,  # channels
    'samples': 50  # labeled samples
}
```

## Future Extensions

### Extension 1: Temporal Dimension
- Evaluate under varying temporal durations
- Real-time vs. batch processing constraints
- Online learning scenarios

### Extension 2: Compute Budget
- CPU-only inference performance
- GPU memory limitations
- Latency requirements

### Extension 3: Domain Shift
- Cross-institution transfer
- Cross-subject variability
- Cross-population generalization

### Extension 4: Clinical Validation
- Neurological disorder detection
- Mental health monitoring
- Cognitive state tracking

## Related Skills

- `eeg-fm-audit-systematic-evaluation`: EEG-FM systematic audit pipeline
- `eeg-foundation-model-adapters`: Domain adaptation for EEG FMs
- `eeg-foundation-sae-interpretability`: SAE-based FM interpretability
- `tta-eeg-foundation-models`: Test-time adaptation for EEG FMs
- `eeg-preprocessing-reliability`: EEG preprocessing reliability assessment

## References

- Paper: arXiv:2605.28563
- Title: "A Multi-dimensional Framework for Evaluating Generalization in EEG Foundation Models"
- Categories: cs.LG, cs.AI
- Created: 2026-05-27

## Metadata

**arXiv**: 2605.28563  
**DOI**: https://doi.org/10.48550/arXiv.2605.28563  
**Category**: cs.LG, cs.AI  
**Submitted**: 2026-05-27  
**Updated**: 2026-05-29 (Cron Job)