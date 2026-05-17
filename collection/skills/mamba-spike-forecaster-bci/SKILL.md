---
name: mamba-spike-forecaster-bci
description: "Mamba forecaster for population-scale spike prediction and implicit behavioral decoding in closed-loop BCI. Use a single Mamba selective state-space model trained on next-step spike counts to simultaneously forecast neural population dynamics and decode behavioral states. Activation: mamba spike forecaster, spike prediction, behavioral decoding, BCI closed-loop, Neuropixels decoding, neural population forecasting, implicit decoding, state-space model spike."
---

# Mamba Spike Forecaster for BCI

A single Mamba selective state-space model trained only on next-step spike counts can simultaneously forecast neural population activity AND decode behavioral states — no separate decoder needed.

**Paper**: Minnick et al., "Implicit Behavioral Decoding from Next-Step Spike Forecasts at Population Scale" (arXiv:2605.12999, May 2026)

## Core Insight

The forecasting objective (next-step Poisson rate prediction) forces the model to integrate population activity over a history window. Its continuous-valued rate outputs serve as a **behaviorally informative compression** of the recent population state. Predicted rates carry more behavioral information than raw spike counts.

## Architecture

### Input Pipeline
- Spike-sorted Neuropixels recordings (M neurons, 50ms bins)
- Sliding window: H=10 bins (500ms context)
- History matrix X_t ∈ R^(M×H)

### Mamba Forecaster
```
h_t = Ā h_{t-1} + B̄ x_t
y_t = C h_t
```
- Selective state-space model with causal recurrence
- Content-aware gating matched to spike-count autoregression
- Output: predicted next-bin firing rates λ̂_{t+1} ∈ R^M_{>0} via softplus
- Trained with Poisson negative log-likelihood (NLL)
- ~1.95M parameters

### Behavioral Readout
- Per-session multinomial logistic regression: ŷ = softmax(Wλ̂ + b)
- Decodes: response (3-class), stimulus side (3-class), contrast (16-class)
- Behavioral labels NEVER enter forecaster training

## Key Results (Steinmetz visual-discrimination benchmark)

| Metric | Mamba | Matched Linear Baseline | Gain |
|--------|-------|------------------------|------|
| Mouse choice (trial vote) | 75.7% | ~70-71% | +4-6 pp |
| Stimulus side (trial vote) | 66.1% | ~60-62% | +4-6 pp |
| Chance level | 33.3% | — | — |

- 39 sessions, ~27,000 neurons, 1,994 held-out trials
- Per-neuron Pearson r = 0.176, population-rate r = 0.783
- Calibration: ~100-150 trials → within 1-2 pp of asymptote
- Fits inside 50ms bin budget on workstation GPUs

## Implementation Pipeline

### 1. Data Preparation
```python
# Cross-laboratory: Steinmetz 2019 + IBL Repeated Site
# 105 sessions, 89,768 channels across 42 Allen CCF regions
# Pad to M_max = 1,998 with per-sample channel mask
# 50ms bins, H=10 history (500ms context)
```

### 2. Training
- Loss: Poisson NLL on real (unmasked) channels
- Optimizer: AdamW + cosine LR warmup
- Epochs: 50
- Split: 70/15/15% temporal train/val/test per session
- Behavioral evaluation: separate 20% trial-level holdout

### 3. Behavioral Decoding (Post-hoc)
- Use predicted rates as features
- Per-session multinomial LR over behavioral targets
- Same protocol applied to raw-count baselines for fair comparison

## Architecture Controls

All sharing same input pipeline, Poisson NLL, training schedule:

| Architecture | Parameters | Decoding Performance |
|-------------|-----------|---------------------|
| Mamba (selective SSM) | 1.95M | Best (headline results) |
| Transformer (causal attention) | 2.22M | Within ~1-3 pp |
| LRU (linear recurrent unit) | 1.23M | Within ~1-3 pp |
| NDT2-style bidirectional masked | ~2.22M | Within ~1-3 pp |

## Deployment Considerations

### Closed-Loop BCI
- Session-start calibration: 100-150 trials
- Inference fits 50ms bin budget
- Single model replaces separate forecast + decode networks
- Reduces compute/memory by ~2x vs dual-model approach

### Multi-Session Training
- Pad to M_max neurons, mask per-sample
- Per-session specialization recovered by post-hoc linear readout
- Cross-laboratory generalization verified

## Comparison to Related Methods

| Method | Spike Prediction | Behavioral Decoding | Implicit Decoding |
|--------|-----------------|-------------------|-------------------|
| LFADS | Smoothed rates (non-causal) | No | No |
| NDT/NDT2 | Masked attention | Yes (supervised) | No |
| CEBRA | No (embeddings only) | Yes (supervised) | No |
| NEDS | Yes (Poisson) | Yes (supervised) | No |
| **This work** | **Yes (causal)** | **Yes (emergent)** | **Yes** |

## When to Use

- Closed-loop BCI requiring both forecasting and decoding
- Population-scale neural recordings (Neuropixels, multi-electrode arrays)
- When computational budget is constrained (single model for two tasks)
- Multi-session behavioral decoding with minimal per-session calibration
- Causal spike-rate forecasting for downstream control systems

## Pitfalls

- Per-neuron prediction is noisy at 50ms bins (single-neuron Poisson noise dominates)
- Population-level structure is reliably captured even when per-neuron predictions are weak
- Behavioral decoding is emergent — quality depends on task-relevant dynamics being captured by forecasting objective
- Calibration needed per session (~100-150 trials minimum)
- GPU-bound — not suitable for edge-only deployment without external compute
