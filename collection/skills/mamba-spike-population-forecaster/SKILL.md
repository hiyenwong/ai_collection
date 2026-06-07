---
name: mamba-spike-forecaster-bci
description: Mamba-based spike forecaster methodology for closed-loop BCI. A single Mamba model trained on next-step spike counts at Neuropixels scale simultaneously predicts neural activity and decodes behavioral state, outperforming linear decoders on raw spikes. arXiv: 2605.12999 (May 2026).
---

# Mamba Spike Forecaster for Closed-Loop BCI

This skill captures the methodology for using a **Mamba state-space model** as a next-step spike forecaster that simultaneously enables implicit behavioral decoding for closed-loop brain-computer interfaces.

**Paper**: John R. Minnick et al., "Implicit Behavioral Decoding from Next-Step Spike Forecasts at Population Scale", arXiv:2605.12999 (May 2026)

## Core Problem

Closed-loop BCIs typically require two separate components:
1. **Neural forecast**: Predict upcoming neural population activity
2. **Behavioral readout**: Decode the animal's behavioral state (choice, stimulus, etc.)

This work shows that **a single Mamba forecaster**, trained only on next-step spike prediction, implicitly learns behavioral representations that outperform direct decoding from raw spikes.

## Key Architecture

### Mamba Spike Forecaster

```python
import torch
import torch.nn as nn
from mamba_ssm import Mamba

class MambaSpikeForecaster(nn.Module):
    """Mamba model for next-step spike count forecasting at Neuropixels scale."""
    
    def __init__(
        self,
        n_neurons: int,        # Number of neurons (~700-1000 per session)
        d_model: int = 256,     # Mamba hidden dimension
        n_layers: int = 4,      # Number of Mamba layers
        dt: float = 0.05,       # Time bin (50ms)
        context_length: int = 10,  # Temporal context window
    ):
        super().__init__()
        self.n_neurons = n_neurons
        self.d_model = d_model
        self.context_length = context_length
        
        # Input projection: spike counts → Mamba embedding
        self.input_proj = nn.Linear(n_neurons, d_model)
        
        # Mamba layers (state-space model)
        self.mamba_layers = nn.ModuleList([
            Mamba(d_model=d_model, d_state=16, d_conv=4, expand=2)
            for _ in range(n_layers)
        ])
        
        # Output projection: hidden state → predicted spike rates
        self.output_proj = nn.Linear(d_model, n_neurons)
        
        # Optional: behavioral readout head (for analysis, not training)
        self.behavior_head = nn.Linear(d_model, n_classes)
    
    def forward(self, spike_history: torch.Tensor) -> torch.Tensor:
        """
        Predict next-step spike rates from history.
        
        Args:
            spike_history: (B, T, N) - spike counts in each time bin
                          B=batch, T=context_length, N=neurons
        
        Returns:
            predicted_rates: (B, N) - predicted spike rates for next bin
        """
        # Project to Mamba space
        x = self.input_proj(spike_history)  # (B, T, d_model)
        
        # Mamba forward pass (autoregressive state-space)
        for layer in self.mamba_layers:
            x = layer(x)  # (B, T, d_model)
        
        # Use last timestep's hidden state
        h_T = x[:, -1, :]  # (B, d_model)
        
        # Predict next-step rates
        predicted_rates = self.output_proj(h_T)  # (B, N)
        return predicted_rates
    
    def get_behavior_embedding(self, spike_history: torch.Tensor) -> torch.Tensor:
        """Extract the internal representation for behavioral decoding."""
        x = self.input_proj(spike_history)
        for layer in self.mamba_layers:
            x = layer(x)
        return x[:, -1, :]  # (B, d_model)
```

### Training Objective

```python
def train_spike_forecaster(model, spike_data, n_epochs, lr=1e-3):
    """Train Mamba to predict next-step spike counts."""
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
    
    for epoch in range(n_epochs):
        for batch in spike_data:
            # spike_history: (B, T, N) - past T timesteps
            # spike_next: (B, N) - next timestep's spike counts
            spike_history, spike_next = batch
            
            # Forward: predict next-step rates
            predicted_rates = model(spike_history)
            
            # Loss: Poisson-like loss for spike counts
            # Negative log-likelihood of Poisson with predicted rate
            loss = -torch.sum(
                spike_next * torch.log(predicted_rates + 1e-8) 
                - predicted_rates
            )
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
```

### Behavioral Readout (Post-hoc Analysis)

```python
def train_behavior_decoder(forecaster, spike_history, behavior_labels, n_trials=100):
    """
    Train a lightweight linear decoder on Mamba's predicted rates
    to decode behavioral state.
    """
    # Get Mamba's predicted rates (frozen forecaster)
    with torch.no_grad():
        predicted_rates = forecaster(spike_history)
    
    # Train linear classifier on predicted rates
    decoder = nn.Linear(forecaster.n_neurons, n_behavior_classes)
    optimizer = torch.optim.Adam(decoder.parameters(), lr=1e-2)
    
    for epoch in range(100):
        logits = decoder(predicted_rates)
        loss = nn.functional.cross_entropy(logits, behavior_labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
    return decoder
```

## Experimental Results

### Steinmetz Visual-Discrimination Benchmark

**Dataset**: 39 sessions, ~27,000 neurons, 1,994 held-out trials (Steinmetz et al.)

**Decoding Performance**:

| Metric | Mamba Predicted Rates | Linear on Raw Spikes | Chance |
|--------|----------------------|---------------------|--------|
| Mouse Choice | 75.7 ± 0.2% | 69-71% | 33% |
| Stimulus Side | 66.1 ± 0.6% | 60-62% | 33% |

- Mamba wins by **4-6 percentage points** on both response and stimulus side decoding
- Performance: **~2.3x chance level** for choice, **~2x chance level** for stimulus

### Calibration Efficiency

- **100-150 trials** of session-start calibration brings readout within **1-2 pp of asymptote**
- Fast adaptation: minimal calibration needed for deployment

### Computational Budget

- Full pipeline fits inside **50ms bin budget** on workstation-class GPUs
- Compatible with tethered chronic Neuropixels recording setups
- Real-time capable for closed-loop applications

## Key Insights

1. **Implicit behavioral representations**: Training only on spike prediction, Mamba learns representations that are better for behavioral decoding than raw spikes
2. **State-space efficiency**: Mamba's selective state mechanism efficiently compresses temporal context into behaviorally-relevant features
3. **Single-model dual-purpose**: One model serves both forecasting and decoding — no separate decoder needed
4. **Scalable to Neuropixels scale**: Handles ~700-1000 neurons per session, tested across 27,000 total neurons
5. **Minimal calibration**: ~100-150 trials sufficient for near-asymptotic performance
6. **Temporal context advantage**: Mamba's long-range temporal modeling outperforms matched 500ms-context linear decoders

## When to Use This Approach

- **Closed-loop BCI systems**: Real-time behavioral decoding from neural populations
- **Neuropixels-scale recordings**: Large-scale neural population analysis
- **Spike-based prediction tasks**: Next-step neural activity forecasting
- **Resource-constrained deployment**: Need for efficient real-time inference
- **Multi-task neural decoding**: Simultaneous prediction and decoding from single model

## Related Skills

- `mamba-spike-behavioral-decoding` — implicit behavioral decoding from spike forecasts
- `mamba-spike-forecasting-behavioral-decoding` — Mamba forecaster for implicit behavioral decoding
- `implicit-behavioral-decoding-spike-forecasts` — behavioral decoding from next-step spike forecasts
- `eeg-brain-connectivity-bci` — BCI methodology
- `neurotrain-local-learning-snn-benchmarking` — SNN benchmarking

## Implementation Checklist

- [ ] Install `mamba_ssm` package (`pip install mamba-ssm`)
- [ ] Preprocess spike data into 50ms bins
- [ ] Split into context windows (e.g., 10 timesteps = 500ms context)
- [ ] Train Mamba on next-step spike prediction (Poisson NLL loss)
- [ ] Extract internal representations for behavioral decoding
- [ ] Train lightweight linear decoder on predicted rates
- [ ] Validate on held-out trials
- [ ] Calibrate with 100-150 session-start trials
- [ ] Deploy for closed-loop operation
