---
name: mamba-spike-forecaster-bci
description: "Implicit Behavioral Decoding from Next-Step Spike Forecasts at Population Scale — using a single Mamba state-space model trained only on next-step spike counts (Neuropixels scale) to simultaneously forecast neural population activity and decode behavioral state via lightweight linear readout. arXiv: 2605.12999"
tags: [bci, mamba, state-space-model, neural-decoding, spike-forecasting, neuropixels, behavioral-decoding, closed-loop]
arxiv_id: "2605.12999"
date: "2026-05-13"
---

# Mamba Spike Forecaster for BCI Decoding

## Paper Reference

**Title:** Implicit Behavioral Decoding from Next-Step Spike Forecasts at Population Scale
**Authors:** John R. Minnick, Jesus Gonzalez-Ferrer, Kamran Hussain, Jinghui Geng, Ash Robbins, Mohammed A. Mostajo-Radji, David Haussler, Jason Eshraghian, Mircea Teodorescu
**arXiv:** 2605.12999 (May 13, 2026)
**Categories:** q-bio.NC, cs.LG
**Submitted to:** NeurIPS 2026 Neuroscience & Cognitive Science Track

## Abstract Summary

A single **Mamba state-space model** forecaster, trained only on next-step spike counts at Neuropixels scale, can simultaneously:
1. **Forecast** upcoming neural population activity
2. **Decode** behavioral state (mouse choice, stimulus side)

A lightweight per-session linear head reading the model's predicted rates outperforms the same linear classifier reading raw spike counts.

## Key Results

### Benchmark Performance (Steinmetz Visual Discrimination)

| Metric | Mamba Forecast | Raw Spikes (Linear) | Chance |
|--------|---------------|---------------------|--------|
| Choice decoding (trial vote) | **75.7±0.2%** | ~70% | 33% |
| Stimulus side (trial vote) | **66.1±0.6%** | ~61% | 33% |
| Calibration speed | **100-150 trials** to asymptote | More data needed | — |

### Performance vs Baseline

- **4-6 pp** improvement over matched 500ms-context linear decoder on raw spikes
- Pipeline fits inside **50 ms bin budget** on workstation GPUs
- 39 sessions, ~27,000 neurons, 1,994 held-out trials

## Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────┐
│                   Mamba Forecaster                       │
│                                                           │
│  Input: Spike Counts (t-N ... t-1)                       │
│  ┌─────────────────────────────────────────────────┐     │
│  │  ┌───┐  ┌───┐  ┌───┐      ┌───┐               │     │
│  │  │t-N│→ │t-N│→ │t-N│→ ...→│t-1│               │     │
│  │  └───┘  └───┘  └───┘      └───┘               │     │
│  │       Mamba SSM Block (×L layers)               │     │
│  │  ┌─────────────────────────────────────────┐    │     │
│  │  │  State Space Model                       │    │     │
│  │  │  h_t = A·h_{t-1} + B·x_t                │    │     │
│  │  │  y_t = C·h_t + D·x_t                     │    │     │
│  │  │  + Selective scan (data-dependent A,B,C) │    │     │
│  │  └─────────────────────────────────────────┘    │     │
│  └─────────────────────────────────────────────────┘     │
│         │                                                 │
│         ▼                                                 │
│  ┌─────────────────────────────────────────────────┐     │
│  │  Output: Forecast spike rates (next time step)  │     │
│  └─────────────────────────────────────────────────┘     │
│         │                                                 │
│         ▼                                                 │
│  ┌─────────────────────────────────────────────────┐     │
│  │  Lightweight Linear Readout Head                │     │
│  │  (per-session, minimal parameters)              │     │
│  │  ┌───────────────────────────────────────┐      │     │
│  │  │  behav_pred = W · forecast_rates + b   │      │     │
│  │  └───────────────────────────────────────┘      │     │
│  └─────────────────────────────────────────────────┘     │
│         │                                                 │
│         ▼                                                 │
│  Output: Choice (left/right) + Stimulus Side              │
└─────────────────────────────────────────────────────────┘
```

### Key Components

#### 1. Mamba SSM (State Space Model)

The Mamba architecture uses:
- **Data-dependent state transitions**: A, B, C matrices vary per input token
- **Selective scan algorithm**: Efficient parallel computation
- **Linear complexity**: O(N) instead of O(N²) like transformers

```python
class MambaBlock(nn.Module):
    def __init__(self, d_model, d_state, d_conv):
        super().__init__()
        self.d_model = d_model
        self.d_state = d_state
        self.conv1d = nn.Conv1d(d_model, d_model, d_conv, groups=d_model)
        self.x_proj = nn.Linear(d_model, d_state * 2 + d_model + d_model)
        self.dt_proj = nn.Linear(d_model, d_model)
        self.A_log = nn.Parameter(log_tensor(d_state, d_model))
        self.D = nn.Parameter(ones(d_model))
        
    def forward(self, x):
        # x: (batch, seq_len, d_model)
        # Selective scan: data-dependent A, B, C
        # ... (standard Mamba implementation)
        return y
```

#### 2. Spike Forecasting Objective

```python
def forecast_loss(predicted_rates, actual_spikes):
    """Training objective: predict next-step spike counts."""
    # Poisson negative log-likelihood
    loss = -sum(actual_spikes * log(predicted_rates) - predicted_rates)
    return loss
```

#### 3. Linear Behavioral Readout

```python
class BehavioralReadout(nn.Module):
    def __init__(self, n_neurons, n_classes):
        super().__init__()
        # Per-session linear head
        self.W = nn.Linear(n_neurons, n_classes)
    
    def forward(self, forecast_rates):
        # forecast_rates: (batch, n_neurons)
        logits = self.W(forecast_rates)
        return logits  # Cross-entropy loss for decoding
```

## Training & Deployment Pipeline

### Step 1: Data Preparation

```python
def prepare_spike_data(spike_times, bin_width=50, n_bins_context=10):
    """
    Convert spike times to binned counts.
    bin_width=50ms (matching Neuropixels recording budget)
    """
    bins = np.arange(0, max(spike_times), bin_width)
    spike_counts, _ = np.histogram(spike_times, bins)
    # Context window: last n_bins_context bins
    context = spike_counts[-n_bins_context:]
    target = spike_counts[0]  # Next bin
    return context, target
```

### Step 2: Mamba Forecaster Training

```python
def train_mamba_forecaster(sessions_data, d_model=256, d_state=64, 
                            n_layers=4, learning_rate=1e-4):
    model = MambaForecaster(d_model, d_state, n_layers)
    optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)
    
    for epoch in range(num_epochs):
        for session in sessions_data:
            spike_counts = session['spike_counts']
            # Slide window prediction
            for t in range(context_len, len(spike_counts)):
                context = spike_counts[t-context_len:t]
                target = spike_counts[t]
                pred = model(context)
                loss = forecast_loss(pred, target)
                loss.backward()
                optimizer.step()
    return model
```

### Step 3: Adaptive Calibration (Per-Session)

```python
def calibrate_readout(model, session_start_data, n_calib_trials=150):
    """
    Calibrate linear readout with minimal trials.
    """
    # Freeze Mamba forecaster weights
    for param in model.mamba.parameters():
        param.requires_grad = False
    
    # Train only the linear readout head
    readout = BehavioralReadout(model.d_model, n_classes=2)
    optimizer = torch.optim.Adam(readout.parameters(), lr=1e-3)
    
    for trial in range(n_calib_trials):
        spike_context = session_start_data[trial]
        with torch.no_grad():
            forecast = model.mamba(spike_context)
        pred = readout(forecast)
        # Cross-entropy loss
        loss = F.cross_entropy(pred, session_start_data[trial]['label'])
        loss.backward()
        optimizer.step()
    
    return readout  # Within 1-2 pp of asymptote
```

## Why This Works

### Intuition

The Mamba forecaster learns the **statistical structure** of neural population dynamics. The predicted rates represent a **denoised, temporally smoothed** version of the neural activity that emphasizes behaviorally-relevant signal while suppressing noise.

```
Raw spikes:     | ▁▂▃▁▄▅▆▇▅▄▃▂▁ | ← Noisy
                |
Mamba forecast: | ▁▂▃▃▄▅▆▆▅▄▃▂▁ | ← Smooth + Denoised
                |   ↑ behavior    ↑
                |   relevant signal preserved
```

### Benefits over Raw Spikes

| Aspect | Raw Spikes | Mamba Forecast |
|--------|------------|----------------|
| Noise level | High (Poisson) | Low (denoised) |
| Temporal context | Fixed window | Learnable SSM |
| Signal-to-noise | Variable | Improved |
| Decoding performance | Baseline | +4-6 pp |

## Experimental Setup (Steinmetz Dataset)

- **Task**: Visual discrimination (left/right grating orientation)
- **Recording**: Neuropixels probes, multiple brain regions
- **Animals**: Mice (39 sessions)
- **Neurons**: ~27,000 total across sessions
- **Trials**: 1,994 held-out test trials
- **Bin width**: 50 ms
- **Context**: 500 ms (10 bins)

## Applications

1. **Closed-loop BCI**: Real-time decoding with minimal calibration
2. **Neural population forecasting**: Predict upcoming activity patterns
3. **Behavioral state monitoring**: Continuous readout from neural data
4. **Low-latency decoding**: Suitable for real-time neuroprosthetics

## Pitfalls & Considerations

- **Per-session calibration**: Still needs 100-150 trials per session
- **GPU requirement**: Workstation-class GPU needed for 50 ms budget
- **Cross-session generalization**: Linear readout is per-session
- **Dataset specificity**: Validated on visual discrimination; other behaviors may differ

## Related Work

- **Mamba** (Gu & Dao, 2023): Original state space model architecture
- **Steinmetz et al.** (2019): Visual discrimination dataset
- **Neuropixels**: Large-scale neural recording technology

## Activation Keywords

- Mamba neural decoding
- spike forecasting BCI
- implicit behavioral decoding
- Neuropixels Mamba
- state space model neuroscience
- Steinmetz benchmark
- closed-loop BCI Mamba
- neural population forecasting
- arXiv:2605.12999

## References

- arXiv:2605.12999 — "Implicit Behavioral Decoding from Next-Step Spike Forecasts at Population Scale" (Minnick et al., 2026)
- Gu & Dao, "Mamba: Linear-Time Sequence Modeling with Selective State Spaces" (2023)
- Steinmetz et al., "Distributed coding of choice, action and engagement across the mouse brain" (Nature, 2019)
