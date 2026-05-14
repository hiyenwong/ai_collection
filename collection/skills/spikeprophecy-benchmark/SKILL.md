---
name: spikeprophecy-benchmark
description: >
  SpikeProphecy methodology for evaluating autoregressive neural population
  forecasting models. Addresses the critical benchmarking gap in large-scale
  neural dynamics prediction. Use when: evaluating neural forecasting models,
  designing neural population benchmarks, comparing Mamba/RNN/Transformer
  architectures for spike prediction, benchmarking brain-computer interface
  (BCI) components, building neural dynamics prediction pipelines, or
  analyzing next-step spike count forecasting at Neuropixels scale.
  Activation: spikeprophecy, neural forecasting benchmark, spike count prediction,
  neural population forecasting, autoregressive neural dynamics, BCI forecasting.
---

# SpikeProphecy Benchmark Methodology

Large-scale benchmark for autoregressive neural population forecasting,
addressing the critical gap in standardized evaluation of neural dynamics
prediction models.

## Paper Reference

- **Title**: SpikeProphecy: A Large-Scale Benchmark for Autoregressive Neural Population Forecasting
- **Authors**: John R. Minnick, Jinghui Geng, Kamran Hussain, Jesus Gonzalez-Ferrer, Ash Robbins, Mohammed A. Mostajo-Radji, David Haussler, Jason K. Eshraghian, Mircea Teodorescu
- **arXiv**: 2605.12992
- **Date**: 2026-05-13
- **Categories**: q-bio.NC, cs.LG

## Core Problem

Closed-loop BCI requires forecasting upcoming neural population activity, but no standardized benchmark exists to evaluate different forecasting architectures (RNN, Transformer, Mamba, state-space models) at Neuropixels scale (~27,000 neurons).

## Benchmark Design

### Data Characteristics
- **Scale**: ~27,000 neurons across 39 sessions (Steinmetz visual-discrimination)
- **Resolution**: 50 ms binning (standard for Neuropixels)
- **Trials**: 1,994 held-out trials across sessions
- **Task**: Visual discrimination (mouse choice + stimulus side)

### Evaluation Protocol
- **Task**: Next-step spike count forecasting
- **Input**: Historical spike counts at population scale
- **Output**: Predicted spike counts for next time bin
- **Metrics**: 
  - Forecast accuracy (correlation, MSE)
  - Downstream behavior decoding quality
  - Computational efficiency (fit within 50 ms GPU budget)

## Key Findings

### Mamba Forecaster Performance
- A single Mamba forecaster trained on next-step spike counts delivers both
  forecasting AND behavioral readout in one forward pass
- **Mouse choice decoding**: 75.7±0.2% trial vote (~2.3x chance)
- **Stimulus side decoding**: 66.1±0.6% trial vote (~2x chance)
- **Beats linear decoder on raw spikes** by 4-6 percentage points

### Calibration Efficiency
- Session-start calibration: ~100-150 trials to reach within 1-2 pp of asymptote
- Full pipeline fits within 50 ms bin budget on workstation GPUs
- Compatible with tethered chronic Neuropixels recording setups

## Architecture Comparison Framework

When evaluating neural forecasting models, compare across:

| Dimension | Metrics |
|-----------|---------|
| Accuracy | Correlation with true spikes, MSE, log-likelihood |
| Downstream utility | Behavior decoding accuracy from predicted rates |
| Calibration speed | Trials needed to reach asymptotic performance |
| Latency | Inference time per 50 ms bin |
| Scalability | Performance vs. neuron count |

## Implementation Patterns

### Linear Readout from Forecast
```python
# Train lightweight per-session linear head on predicted rates
# rather than raw spike counts
from sklearn.linear_model import LogisticRegression

# Mamba produces predicted rates (smoothed forecasts)
predicted_rates = mamba_forecaster.predict(historical_spikes)

# Linear head decodes behavior from predicted rates
decoder = LogisticRegression()
decoder.fit(predicted_rates, behavioral_labels)

# Compare against baseline: same decoder on raw spikes
baseline_decoder = LogisticRegression()
baseline_decoder.fit(raw_spikes, behavioral_labels)
```

### Calibration Protocol
1. Collect ~100-150 trials from session start
2. Train linear readout head on forecasted rates
3. Evaluate on held-out trials
4. Performance reaches within 1-2 pp of full-session asymptote

## Related Work

- Implicit Behavioral Decoding from Next-Step Spike Forecasts (2605.12999):
  Companion paper showing behavioral decoding from spike forecasts
- Predictive Coding Light+ (2605.12732): Sequence prediction via STDP + delays
- Mamba state-space models for neural dynamics forecasting

## When to Use This Skill

- Designing benchmarks for neural population forecasting models
- Comparing RNN/Transformer/Mamba architectures for spike prediction
- Building BCI systems requiring neural activity forecasting
- Evaluating whether forecasting improves downstream decoding
- Setting up standardized evaluation for neural dynamics research
