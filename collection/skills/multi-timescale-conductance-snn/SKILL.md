---
name: multi-timescale-conductance-snn
description: "Multi-Timescale Conductance Spiking Networks (MTCSN) methodology — a gradient-trainable SNN framework using fast, slow, and ultra-slow conductance shaping of I-V curves to produce rich firing regimes (tonic, phasic, bursting) with high sparsity. Enabling backpropagation through time without surrogate gradients. Use when designing conductance-based SNNs, implementing neuromorphic hardware with conductance synapses, or building sparse temporal processing models with differentiable spiking dynamics. Keywords: conductance SNN, multi-timescale spiking, gradient-trainable SNN, MTCSN, conductance-based neuron, surrogate-free SNN, I-V curve shaping, spiking regression, Mackey-Glass, AdLIF."
---

# Multi-Timescale Conductance Spiking Networks (MTCSN)

## Paper Source

- **Title**: Multi-Timescale Conductance Spiking Networks: A Sparse, Gradient-Trainable Framework with Rich Firing Dynamics for Enhanced Temporal Processing
- **Authors**: Alex Fulleda-Garcia, Saray Soldado-Magraner, Josep Maria Margarit-Taulé
- **arXiv**: [2605.11835](https://arxiv.org/abs/2605.11835) (2026-05-12)
- **Categories**: cs.NE, cs.AI, cs.LG

## Core Methodology

### Conductance-Based I-V Curve Shaping

Instead of phenomenological LIF models, MTCSN uses biophysically-inspired conductance dynamics:

$$\tau_m \frac{dV}{dt} = -(V - E_L) - \sum_k g_k(t) \cdot (V - E_k) + I_{ext}(t)$$

where conductances $g_k$ operate at multiple timescales:
- **Fast conductance** ($\tau_f \approx 1$ms): Captures rapid AMPA-like synaptic currents
- **Slow conductance** ($\tau_s \approx 10-100$ms): NMDA/GABA_B-like dynamics
- **Ultra-slow conductance** ($\tau_{us} \approx 100-1000$ms): Adaptation/homeostatic processes

### Key Design Principles

1. **I-V curve parameterization**: Tuning conductances shapes the neuron's I-V curve, directly controlling excitability type and firing regime
2. **Emergent firing patterns**: Single neuron model produces tonic, phasic, and bursting responses without explicit mode switching
3. **Gradient-trainable**: Discrete-time formulation enables backpropagation through time (BPTT) without surrogate gradient approximations
4. **Hardware-compatible**: Conductance parameters map directly to analog circuit implementations
5. **High sparsity**: Activity sparsity from both communication and computational perspectives

### Discrete-Time Formulation

For BPTT, the continuous dynamics are discretized:

$$V[t+1] = V[t] + \frac{\Delta t}{\tau_m} \left[-(V[t] - E_L) - \sum_k g_k[t](V[t] - E_k) + I[t]\right]$$

$$g_k[t+1] = g_k[t] \cdot e^{-\Delta t/\tau_k} + \Delta g_k[t]$$

Spike generation: $s[t] = \mathbb{1}(V[t] > V_{th})$, with reset $V \leftarrow V_{reset}$

### Trainability Advantages

- **No surrogate gradients**: Exact gradients flow through differentiable membrane dynamics
- **Rich temporal credit assignment**: Multi-timescale conductances provide natural temporal memory
- **Sparse activity**: Conductance shaping naturally suppresses unnecessary firing

## Comparison to Baselines

| Property | LIF | AdLIF | MTCSN (this work) |
|----------|-----|-------|-------------------|
| Gradient method | Surrogate | Surrogate | Direct BPTT |
| Firing regimes | Single | Limited | Tonic, phasic, bursting |
| Sparsity | Moderate | Moderate | High |
| Hardware mapping | Simple | Moderate | Direct to analog |
| Trainability | Good | Good | Superior |

### Performance (Mackey-Glass Regression)

- Outperforms LIF and AdLIF at the predictability limit
- Exhibits substantially sparser activity from both communication and computational perspectives
- Better noise robustness for continuous-valued outputs

## Implementation Pattern

```python
class MTCSNeuron(nn.Module):
    def __init__(self, n_fast=1, n_slow=1, n_ultra_slow=1):
        super().__init__()
        # Conductance parameters (learnable)
        self.g_fast = nn.Parameter(torch.randn(n_fast))
        self.g_slow = nn.Parameter(torch.randn(n_slow))
        self.g_ultra_slow = nn.Parameter(torch.randn(n_ultra_slow))
        
        # Timescales (can be fixed or learnable)
        self.tau_fast = 1.0   # ms
        self.tau_slow = 50.0  # ms
        self.tau_ultra_slow = 500.0  # ms
        
        # Reversal potentials
        self.E_exc = 0.0   # mV
        self.E_inh = -75.0  # mV
        self.E_L = -65.0    # mV
        
        self.V_th = -50.0
        self.V_reset = -65.0
        self.tau_m = 20.0   # ms
    
    def forward(self, I_ext, dt=1.0):
        """BPTT-compatible forward pass."""
        V = torch.full_like(I_ext, self.E_L)
        g = torch.zeros_like(I_ext)
        spikes = torch.zeros_like(I_ext)
        
        for t in range(I_ext.shape[0]):
            # Update conductances
            g = g * torch.exp(-dt / self.tau_k) + delta_g(t)
            
            # Update membrane potential
            dV = (-(V - self.E_L) - g * (V - self.E_k) + I_ext[t]) * dt / self.tau_m
            V = V + dV
            
            # Spike generation
            spikes[t] = (V > self.V_th).float()
            V = V * (1 - spikes[t]) + self.V_reset * spikes[t]
        
        return spikes
```

## Use Cases

1. **Temporal sequence processing**: Where standard LIF/AdLIF struggle with regression tasks
2. **Neuromorphic hardware deployment**: Conductance parameters directly map to analog circuits
3. **Low-power edge inference**: High sparsity reduces communication and computation
4. **Temporal credit assignment**: Multi-timescale dynamics provide natural memory without RNN overhead
5. **Biophysically realistic modeling**: Bridging computational neuroscience with deep learning

## Activation Keywords

- conductance SNN
- multi-timescale spiking
- gradient-trainable SNN
- MTCSN
- conductance-based neuron
- surrogate-free SNN
- I-V curve shaping
- spiking regression
- Mackey-Glass prediction
- AdLIF alternative
