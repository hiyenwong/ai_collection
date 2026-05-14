---
name: spikeprophecy-benchmark
description: "SpikeProphecy methodology for autoregressive neural population forecasting. Introduces a large-scale benchmark for causal, autoregressive spike-count forecasting on real electrophysiology recordings. Core contribution: population metric decomposition separating aggregate performance into temporal fidelity, spatial pattern accuracy, and magnitude-invariant alignment. Evaluated on 105 Neuropixels sessions (~89,800 neurons) with 7 architecture baselines spanning SSMs, RNNs, transformers, and other families. Activation: SpikeProphecy, neural population forecasting, spike count forecasting, Neuropixels benchmark, autoregressive spike prediction, neural dynamics prediction, population metric decomposition, temporal fidelity, spatial pattern accuracy, Steinmetz dataset, neural population models."
---

# SpikeProphecy Benchmark Methodology

## Overview

SpikeProphecy (arXiv: 2605.12992) introduces the **first large-scale benchmark for causal, autoregressive spike-count forecasting** on real electrophysiology recordings. It challenges the field's reliance on a single aggregate Pearson correlation metric, which masks critical structural aspects of neural population predictions.

## Core Problem

Neural population models predict joint firing of many simultaneously recorded neurons forward in time, but are typically evaluated by a single aggregate Pearson correlation $r$ between predicted and actual spike counts. This scalar collapses together distinct aspects of prediction quality — temporal fidelity, spatial pattern accuracy, and magnitude alignment — making it impossible to distinguish what a model actually captures.

## Key Contributions

### 1. Population Metric Decomposition

Decomposes aggregate forecasting performance into three orthogonal components:

- **Temporal Fidelity**: How well the model captures the timing dynamics of neural activity
- **Spatial Pattern Accuracy**: How well the model captures the spatial correlations across neurons
- **Magnitude-Invariant Alignment**: How well the model captures relative firing rate patterns independent of absolute magnitude

This decomposition surfaces aspects of the underlying data that an aggregate scalar obscures.

### 2. Large-Scale Benchmark Protocol

- **Dataset**: 105 Neuropixels sessions (Steinmetz 2019 + IBL Repeated Site)
- **Scale**: ~89,800 neurons across sessions
- **Task**: Causal, autoregressive spike-count forecasting
- **Baselines**: 7 architectures spanning 4 structural families:
  - 4 State Space Models (3 diagonal + 1 non-diagonal)
  - RNN-based models
  - Transformer-based models
  - Other baseline families

### 3. Implicit Behavioral Decoding

Companion work (arXiv: 2605.12999) demonstrates that a single Mamba forecaster trained on next-step spike counts can simultaneously:
- Forecast neural population activity
- Decode behavioral state from predicted rates
- Achieve 75.7±0.2% trial vote accuracy on mouse choice (~2.3× chance)
- Achieve 66.1±0.6% on stimulus side (~2× chance)
- Outperform matched linear decoders by 4-6 percentage points

## Application to Skill Development

### When to Apply This Methodology

- Evaluating neural population forecasting models
- Designing benchmark protocols for neural dynamics prediction
- Comparing SSM, RNN, and transformer architectures for spike prediction
- Analyzing multi-dimensional prediction quality beyond aggregate correlation

### Metric Decomposition Implementation

```python
# Conceptual framework for the three-way decomposition
def decompose_population_metrics(predictions, ground_truth):
    """
    Decompose aggregate forecasting metrics into:
    1. Temporal fidelity (time-domain accuracy per neuron)
    2. Spatial pattern accuracy (cross-neuron correlation structure)
    3. Magnitude-invariant alignment (rate pattern without scale)
    """
    # Temporal: per-neuron temporal correlation
    temporal = compute_temporal_fidelity(predictions, ground_truth)
    
    # Spatial: cross-neuron pattern at each timestep
    spatial = compute_spatial_accuracy(predictions, ground_truth)
    
    # Magnitude-invariant: normalized rate patterns
    magnitude_invariant = compute_magnitude_invariant(predictions, ground_truth)
    
    return {
        'temporal_fidelity': temporal,
        'spatial_pattern': spatial,
        'magnitude_invariant': magnitude_invariant
    }
```

### Architecture Selection Guidance

| Architecture | Strengths | Best For |
|-------------|-----------|----------|
| SSM (diagonal) | Efficient, long context | High-throughput sessions |
| SSM (non-diagonal) | Captures cross-neuron interactions | Dense connectivity patterns |
| RNN | Proven on sequential data | Moderate-scale sessions |
| Transformer | Global attention | Complex temporal dependencies |

## Research Implications

1. **Evaluation matters**: How we evaluate spike forecasting matters as much as what we build
2. **Decomposition reveals structure**: Population metric decomposition surfaces critical aspects collapsed by aggregate scalars
3. **Unified forecasting+decoding**: A single forecaster can serve both prediction and behavioral readout
4. **Scale enables discovery**: 105-session, ~89,800-neuron benchmark provides statistical power for nuanced comparisons

## Related Skills

- `mamba-spike-forecasting-behavioral-decoding` - Mamba forecaster for behavioral decoding
- `autoregressive-flow-matching-neural-dynamics` - Flow matching for neural dynamics
- `neural-population-dynamics` - Neural population analysis methods

## References

- SpikeProphecy: arXiv:2605.12992
- Implicit Behavioral Decoding: arXiv:2605.12999
- Steinmetz Dataset: Nature 2019
- IBL Repeated Site: International Brain Laboratory
