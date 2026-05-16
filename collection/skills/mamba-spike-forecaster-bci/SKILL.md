---
name: mamba-spike-forecaster-bci
description: >
  Mamba-based spike forecaster for closed-loop BCI. A single Mamba forecaster
  trained on next-step spike counts at Neuropixels scale delivers both neural
  population forecasting AND behavioral decoding in one forward pass.
  Predicted rates decode mouse choice at 75.7% (3-class, 2.3x chance) and
  stimulus side at 66.1% (2x chance), beating matched-context linear decoders
  by 4-6 percentage points. A calibration block of ~100-150 trials brings
  readout within 1-2pp of asymptote. Fits inside 50ms bin budget on workstation GPUs.
  Activation: spike forecasting, BCI decoding, neural population dynamics,
  Mamba neural forecaster, Neuropixels spike analysis, closed-loop BCI,
  behavioral decoding from spikes, spike count prediction,
  neural dynamics forecasting, Poisson rate prediction
---

# Mamba Spike Forecaster for Closed-Loop BCI

## Overview

A single Mamba forecaster trained only on next-step spike counts simultaneously:
1. **Forecasts** upcoming neural population activity (50ms ahead)
2. **Decodes** behavioral state (choice, stimulus) via lightweight linear readout

arXiv: 2605.12999 (May 2026)

## Key Insight

A forecaster's predicted firing rates serve as a **behaviorally informative compression** of recent population state. Reading behavior off the forecaster's predicted rates outperforms reading directly from raw spike counts under matched temporal context.

## Architecture

```
Spike-counts (M neurons, H=10 bins, 500ms context)
    → Mamba selective state-space model
    → Predicted next-bin firing rates λ̂(t+1) ∈ R^M
        → (1) Population forecast (direct output)
        → (2) Behavioral decoding via linear head: softmax(Wλ̂ + b)
```

- **Input**: Sliding window of population spike-count vectors X_t ∈ Z^M≥0, H=10 bins (500ms), Δt=50ms
- **Model**: Mamba (selective state-space model) — causal recurrence with content-aware gating
- **Loss**: Poisson negative log-likelihood (NLL) on predicted rates
- **Multi-session**: Pads to M_max=1998 neurons with per-sample channel mask

## Behavioral Decoding Results

| Target | Mamba Decoding | Matched-Context Linear | Gain |
|--------|---------------|----------------------|------|
| Mouse Choice (3-class) | 75.7±0.2% | ~70% | +4-6 pp |
| Stimulus Side (3-class) | 66.1±0.6% | ~60% | +4-6 pp |

- **Chance levels**: 33.3% (3-class)
- **Calibration**: ~100-150 trials brings readout within 1-2pp of asymptote
- **Multi-seed**: Results consistent across 3 training seeds
- **Architecture controls**: Transformer, LRU, NDT2 bidirectional all within ~1-3pp

## Why It Works

1. **Training objective forces integration**: Next-step Poisson rate prediction requires integrating population activity over history window
2. **Continuous-valued compression**: Predicted rates carry more behavioral info than raw single-bin spike counts
3. **No behavioral labels needed for forecaster**: Behavior decodes implicitly from spike forecasts
4. **Single model replaces two**: One forecaster replaces separate forecasting + decoding networks

## Implementation Guide

### Data Format

```python
# Per-bin spike counts: M neurons × H history bins
X_t = spikes[t-H+1:t+1]  # shape: (M, H), dtype: int, Δt=50ms
```

### Training Loop

```python
# Predict next-step rates
rates = model(X_t)  # shape: (M,), softplus activated

# Poisson NLL loss
loss = poisson_nll(rates, spikes[t+1])  # only on unmasked channels

# Multi-session: pad to M_max, use channel mask
```

### Behavioral Readout (Post-hoc)

```python
# Linear head on predicted rates (per-session)
W, b = fit_multinomial_logistic(rates, behavior_labels)
predictions = softmax(W @ rates + b)
```

### Closed-Loop Deployment

```python
# 1. Session-start calibration: ~100-150 trials
# 2. Fit linear readout on calibration data
# 3. Online inference: Mamba forward pass + linear head
# 4. Both forecast AND decode in one pass (< 50ms on workstation GPU)
```

## Comparison to Alternatives

| Method | Forecasting | Decoding | Inference Cost |
|--------|-----------|----------|---------------|
| Linear decoder on raw spikes | ✗ | Baseline | Low |
| LFADS (VAE) | Smoothed rates | Requires separate decoder | High |
| NDT/NDT2 | Masked attention | Yes | Medium-High |
| CEBRA | Embedding | Yes (contrastive) | Medium |
| **Mamba forecaster** | **Next-step** | **Implicit** | **Medium** |

## Applicability

- Closed-loop BCI systems requiring both forecasting and decoding
- Neuropixels-scale recordings (>1000 simultaneous neurons)
- Any task where behavior can be decoded from neural population activity
- Real-time systems with <50ms latency budget
- Generalizes to Transformer/LRU architectures (tested)

## Limitations

- GPU-bound inference (not suitable for implanted devices)
- Multi-session training requires channel padding/masking
- Per-session linear readout needs calibration data
- Tested on visual-discrimination task; generalization to other tasks TBD

## Activation Keywords

- spike forecasting, BCI decoding, neural population dynamics
- Mamba neural forecaster, Neuropixels spike analysis
- closed-loop BCI, behavioral decoding from spikes
- spike count prediction, neural dynamics forecasting
- Poisson rate prediction, state-space model neuroscience
