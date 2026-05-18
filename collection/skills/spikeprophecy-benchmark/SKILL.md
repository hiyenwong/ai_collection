---
name: spikeprophecy-benchmark
description: "SpikeProphecy benchmark methodology for evaluating autoregressive neural population forecasting models. Introduces population metric decomposition that separates temporal fidelity, spatial pattern accuracy, and magnitude-invariant alignment."
tags: ["neuroscience", "benchmark", "spike-forecasting", "neural-population", "electrophysiology", "evaluation"]
---

# SpikeProphecy Benchmark

## Description

SpikeProphecy is the first large-scale benchmark for causal, autoregressive spike-count forecasting on real electrophysiology recordings. Its core contribution is a population metric decomposition that separates aggregate evaluation into three interpretable axes: temporal fidelity, spatial pattern accuracy, and magnitude-invariant alignment.

## Activation Keywords

- spike forecasting benchmark
- neural population forecasting
- population metric decomposition
- Neuropixels benchmark
- spike-count evaluation
- autoregressive neural model
- electrophysiology forecasting

## Key Findings

### Finding 1: Brain-Region Predictability Hierarchy
- Decomposition reveals a functional brain-region predictability ranking
- Reproducible across all seven architecture baselines (SSMs, Transformer, LSTM, spiking networks)
- Survives ANCOVA correction for firing-statistics constraints
- Region delta R-squared = 0.018 above firing-statistics covariates

### Finding 2: Sub-Poisson Evaluation Floor
- Rigorous metrics combined with genuine biophysical constraints on regular spike trains
- Creates an evaluation floor below Poisson randomness
- Two compounding causes: metric sensitivity + biophysical limits

### Finding 3: Negative Result on ANN-to-SNN Distillation
- KL-on-output-rates distillation for ANN to SNN transfer fails in Poisson count domain
- Important negative result for neural architecture transfer

## Benchmark Design

### Datasets
- **Steinmetz 2019**: 39 Neuropixels sessions
- **IBL Repeated Site**: 66 sessions
- **Total**: ~89,800 neurons across 105 sessions

### Architecture Baselines
Seven baselines spanning four structural families:
1. **SSMs** (State Space Models): 3 diagonal + 1 non-diagonal
2. **Transformer**: Attention-based sequence model
3. **LSTM**: Recurrent neural network
4. **Spiking Network**: Biologically-inspired architecture

### Population Metric Decomposition
Instead of aggregate Pearson r, decompose into:
1. **Temporal Fidelity**: How well does the model predict timing?
2. **Spatial Pattern Accuracy**: How well does it predict which neurons fire?
3. **Magnitude-Invariant Alignment**: Does it get relative firing rates right?

### Auditable Leakage Suite
- Prevents data leakage between train/test splits
- Ensures fair evaluation across architectures

## Evaluation Protocol

### Standard Metrics (Baseline)
- Aggregate per-neuron Pearson correlation r
- Mean squared error (MSE)
- Coefficient of determination (R-squared)

### Population Metric Decomposition (Contribution)
- Separates temporal, spatial, and magnitude components
- Reveals structure hidden by aggregate scalar
- Enables brain-region level analysis

## Applications

1. **Brain-Computer Interfaces**: 50-100ms look-ahead predictions for closed-loop BCIs
2. **Digital Twin Simulators**: In silico neural population simulators
3. **Architecture Selection**: Compare SSMs vs Transformers vs LSTMs vs Spiking Networks
4. **Cross-Dataset Generalization**: Test model transfer across recording sessions

## Error Handling

### Data Leakage
- Use auditable leakage suite to detect train/test contamination
- Ensure proper temporal splitting for autoregressive models

### Firing Statistics Confounds
- Apply ANCOVA correction for firing-rate differences
- Account for sub-Poisson evaluation floor

### Metric Limitations
- Aggregate Pearson r masks important structure
- Always use decomposition for detailed analysis

## References

- arXiv:2605.12992 - "SpikeProphecy: A Large-Scale Benchmark for Autoregressive Neural Population Forecasting" (May 2026)
