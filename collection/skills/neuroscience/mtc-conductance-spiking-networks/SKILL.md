---
name: mtc-conductance-spiking-networks
description: Multi-Timescale Conductance Spiking Networks (MTC-SNN) — gradient-trainable spiking neural networks where neural dynamics emerge from shaping the I-V curve via fast, slow, and ultra-slow conductances. Enables tonic, phasic, and bursting firing regimes within a single model, trainable via exact BPTT without surrogate gradients. arXiv: 2605.11835 (May 2026).
---

# Multi-Timescale Conductance Spiking Networks (MTC-SNN)

MTC-SNN is a **gradient-trainable spiking neural network framework** where rich firing dynamics emerge from shaping the current-voltage (I-V) curve through tunable conductances operating at multiple timescales. Unlike LIF-based models that use surrogate gradients, MTC neurons are **directly differentiable** and trainable via standard Backpropagation Through Time (BPTT).

**Paper**: Fulleda-Garcia, Soldado-Magraner, Margarit-Taulé, "Multi-Timescale Conductance Spiking Networks: A Sparse, Gradient-Trainable Framework with Rich Firing Dynamics for Enhanced Temporal Processing", arXiv:2605.11835 (May 2026)

## Core Problem

Existing SNN neuron models face a trilemma:
- **LIF models**: Computationally efficient but sacrifice biophysical realism, limited firing regimes, surrogate gradient mismatch
- **Adaptive LIF (AdLIF)**: Adds one slow state variable, but still captures narrow subset of biological diversity
- **Biologically detailed models**: Rich dynamics but not gradient-trainable, computationally expensive

The gap between **biological plausibility** and **machine learning trainability** remains significant, especially for continuous-valued temporal regression.

## MTC Neuron Model

### Circuit-Theoretic Foundation

Based on Ribar & Sepulchre's conductance-based framework: neuron excitability is controlled by shaping the I-V curve through parallel interconnection of positive and negative conductance elements at different timescales.

**Base membrane equation** (RC circuit):
```
τ_m · dU_m/dt = −(U_m − U_rest) + R·I_in − R·Σ I_x±
```

### Conductance Elements

Each conductance element follows:
```
τ_x · dU_x/dt = −U_x + U_m          (filtering)
I_x± = ±α_x± · tanh(U_x − δ_x±)    (nonlinear current)
```

Three timescales relative to τ_m:

| Element | Sign | Timescale | Role |
|---------|------|-----------|------|
| I_f− | Negative | Fast (τ_f → 1) | Creates negative differential resistance → drives action potential upstroke |
| I_s+ | Positive | Slow (τ_s ≫ τ_m) | Restorative → recovers membrane potential, enforces refractory period |
| I_s− | Negative | Slow | Second negative conductance → enables bursting |
| I_us+ | Positive | Ultra-slow (τ_us ≫ τ_s) | Balances slow negative → enables mode transitions |

### Firing Regimes

By modulating conductance parameters, the model smoothly transitions between:
- **Tonic spiking**: Constant firing in response to sustained input
- **Tonic bursting**: Clusters of spikes during sustained input
- **Phasic spiking**: Transient response to input onset only
- **Phasic bursting**: Transient burst at input onset

### Discrete-Time Formulation (Differentiable)

```python
# Explicit Euler-Forward discretization
U_x[t+1] = U_x[t] + (dt/τ_x) * (−U_x[t] + U_m[t])
U_m[t+1] = U_m[t] + (dt/τ_m) * (−U_m[t] + U_rest + I_in[t] − Σ I_x±[t])
```

### Synaptic Transduction (Signal Conditioning)

Transforms continuous membrane potential into standardized transmission signal:
```
s(t) = min(ReLU(U_m(t) − U_th) / (U_sat − U_th), 1)
```

Key properties:
- **Signal standardization**: Normalizes events to [0, 1] regardless of varying internal dynamics
- **Semi-digital communication**: Suppresses sub-threshold activity (s(t)=0 below U_th) while retaining continuous slope during rising phase
- **Noise gate**: Forces sparsity by requiring minimum depolarization for transmission
- **Differentiable**: Continuous slope enables exact gradient computation (no surrogate needed)

## Comparison with Baselines

| Feature | LIF | AdLIF | MTC |
|---------|-----|-------|-----|
| Timescales | 1 (τ_m) | 2 (τ_m, τ_w) | 4 (τ_m, τ_f, τ_s, τ_us) |
| Firing regimes | Tonic only | Limited adaptation | Tonic, phasic, bursting |
| Training | Surrogate gradient | Surrogate gradient | Exact BPTT |
| Gradient fidelity | Mismatch | Mismatch | Exact |
| Sparsity control | Indirect | Indirect | Intrinsic (conductance-shaped) |

## Experimental Results

### Mackey-Glass Chaotic Time Series Forecasting

Benchmark: predict MG series (τ=17, chaotic regime) at prediction horizon of ~1 Lyapunov time (the limit of deterministic predictability).

**Architecture**: Feedforward SNN (no recurrent connections), single hidden layer of N independent spiking neurons + linear readout + 4th-order low-pass filter.

**Results**:
- MTC outperforms LIF and AdLIF in accuracy (lower MSE at predictability horizon)
- MTC exhibits **substantially sparser activity** in both:
  - **Rate sparsity**: Fewer spikes per neuron per timestep
  - **Duty-cycle sparsity**: Neurons active for smaller fraction of time
- Exact gradients (no surrogate) → better convergence for regression losses

## Implementation Patterns

### MTC Neuron Implementation

```python
import torch
import torch.nn as nn

class MTCNeuron(nn.Module):
    """Multi-Timescale Conductance neuron."""
    def __init__(self, n_neurons, dt=0.2, tau_m=1.0, U_rest=0.0,
                 U_th=0.5, U_sat=1.0):
        super().__init__()
        self.dt = dt
        self.tau_m = tau_m
        self.U_rest = U_rest
        self.U_th = U_th
        self.U_sat = U_sat
        self.n = n_neurons
        
        # Conductance parameters (learnable)
        # Fast negative conductance
        self.alpha_f = nn.Parameter(torch.randn(n_neurons) * 0.1)
        self.delta_f = nn.Parameter(torch.zeros(n_neurons))
        self.tau_f = nn.Parameter(torch.ones(n_neurons) * 0.1)
        
        # Slow positive conductance (restorative)
        self.alpha_s_pos = nn.Parameter(torch.randn(n_neurons) * 0.1)
        self.delta_s_pos = nn.Parameter(torch.zeros(n_neurons))
        self.tau_s = nn.Parameter(torch.ones(n_neurons) * 5.0)
        
        # Slow negative conductance (bursting)
        self.alpha_s_neg = nn.Parameter(torch.randn(n_neurons) * 0.05)
        self.delta_s_neg = nn.Parameter(torch.zeros(n_neurons))
        
        # Ultra-slow positive conductance
        self.alpha_us_pos = nn.Parameter(torch.randn(n_neurons) * 0.05)
        self.delta_us_pos = nn.Parameter(torch.zeros(n_neurons))
        self.tau_us = nn.Parameter(torch.ones(n_neurons) * 20.0)
    
    def conductance_current(self, U_x, alpha, delta, sign=1):
        """I_x = ±α · tanh(U_x − δ)"""
        return sign * alpha * torch.tanh(U_x - delta)
    
    def forward(self, I_in, n_steps):
        """Forward pass with BPTT-compatible dynamics."""
        B = I_in.shape[0]
        
        # Initialize state variables
        U_m = torch.full((B, self.n), self.U_rest, device=I_in.device)
        U_f = torch.zeros((B, self.n), device=I_in.device)
        U_s = torch.zeros((B, self.n), device=I_in.device)
        U_us = torch.zeros((B, self.n), device=I_in.device)
        
        outputs = []
        
        for t in range(n_steps):
            i_in = I_in[:, t] if I_in.ndim > 1 else I_in
            
            # Filter dynamics (Euler-Forward)
            U_f = U_f + (self.dt / self.tau_f) * (−U_f + U_m)
            U_s = U_s + (self.dt / self.tau_s) * (−U_s + U_m)
            U_us = U_us + (self.dt / self.tau_us) * (−U_us + U_m)
            
            # Conductance currents
            I_f = self.conductance_current(U_f, self.alpha_f, self.delta_f, sign=-1)
            I_s_pos = self.conductance_current(U_s, self.alpha_s_pos, self.delta_s_pos, sign=+1)
            I_s_neg = self.conductance_current(U_s, self.alpha_s_neg, self.delta_s_neg, sign=-1)
            I_us_pos = self.conductance_current(U_us, self.alpha_us_pos, self.delta_us_pos, sign=+1)
            
            I_total = I_f + I_s_pos + I_s_neg + I_us_pos
            
            # Membrane dynamics
            U_m = U_m + (self.dt / self.tau_m) * (
                −(U_m - self.U_rest) + i_in - I_total
            )
            
            # Synaptic transduction (semi-digital signal)
            s = torch.clamp(
                torch.relu(U_m - self.U_th) / (self.U_sat - self.U_th),
                0, 1
            )
            outputs.append(s)
        
        return torch.stack(outputs, dim=1)  # (B, T, N)
```

### MTC-SNN for Time Series Regression

```python
class MTCSNN(nn.Module):
    """Feedforward MTC-SNN for temporal regression."""
    def __init__(self, input_dim, n_neurons, output_dim=1):
        super().__init__()
        self.input_proj = nn.Linear(input_dim, n_neurons)
        self.neuron = MTCNeuron(n_neurons)
        self.readout = nn.Linear(n_neurons, output_dim)
        # Low-pass filter for signal reconstruction
        self.lp_filter = nn.Sequential(
            nn.Conv1d(1, 1, kernel_size=5, padding=2),
            nn.Conv1d(1, 1, kernel_size=5, padding=2),
        )
    
    def forward(self, x, n_steps):
        # Project input to neuron space
        x_proj = self.input_proj(x)  # (B, T, N)
        
        # MTC dynamics
        spikes = self.neuron(x_proj, n_steps)  # (B, T, N)
        
        # Linear readout
        y = self.readout(spikes)  # (B, T, out)
        
        # Low-pass filtering for continuous reconstruction
        y = y.transpose(1, 2)  # (B, out, T)
        y = self.lp_filter(y)
        return y.transpose(1, 2)  # (B, T, out)
```

### Training Loop (Exact BPTT — No Surrogate)

```python
# MTC trains with standard BPTT — no surrogate gradient needed!
model = MTCSNN(input_dim=1, n_neurons=256)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=10000)

for epoch in range(10000):
    optimizer.zero_grad()
    predictions = model(inputs, n_steps=Tx)
    loss = nn.functional.mse_loss(predictions, targets)
    loss.backward()  # Exact gradients through conductance dynamics
    optimizer.step()
    scheduler.step()
```

## When to Use MTC-SNN

- **Temporal regression** with long-range dependencies (time series forecasting, signal prediction)
- **Energy-efficient temporal processing** where sparsity matters
- **Neuromorphic hardware implementation** (conductance parameters map to analog circuit elements)
- **Replacing LIF/AdLIF** when richer dynamics or exact gradients are needed
- **Closed-loop control systems** requiring continuous-valued outputs from spiking networks

## Related Skills

- `multi-timescale-conductance-spiking-networks` — existing skill (overlaps, this updates with latest findings)
- `multi-plasticity-snn-training` — SNN training patterns
- `snn-learning-survey` — SNN learning rules overview
- `globally-optimal-snn-parameter-reconstruction` — SNN optimization

## Key Insights

1. **Exact BPTT without surrogates**: Conductance-based dynamics are naturally differentiable → no forward-backward mismatch
2. **Four timescales enable rich dynamics**: Fast (depolarization), slow (recovery), slow-negative (bursting), ultra-slow (mode transitions)
3. **Sparsity emerges intrinsically**: Conductance-shaped excitability controls when/how neurons fire, not through external regularization
4. **Feedforward suffices for temporal tasks**: Internal neuron memory replaces need for recurrent network connections
5. **Analog circuit mapping**: Conductance parameters directly correspond to transconductance blocks in subthreshold MOS circuits
6. **I-V curve shaping as computation**: Excitability regimes determined by slopes and intersections of aggregate I-V curves
