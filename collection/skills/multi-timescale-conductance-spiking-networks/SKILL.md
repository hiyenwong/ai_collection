---
name: multi-timescale-conductance-spiking-networks
description: "Multi-Timescale Conductance (MTC) Spiking Networks methodology — sparse, gradient-trainable framework with rich firing dynamics. Derives differentiable conductance-based neurons with fast/slow/ultra-slow timescales, enabling direct BPTT without surrogate gradients. Benchmark: Mackey-Glass chaotic time series forecasting. Activation: MTC-SNN, conductance spiking, BPTT spiking, multi-timescale neuron, Mackey-Glass forecasting, I-V curve shaping, 多时间尺度电导脉冲网络."
---

# Multi-Timescale Conductance Spiking Networks (MTC-SNN)

Gradient-trainable SNN framework where neural dynamics emerge from shaping the current-voltage (I-V) curve via tunable fast, slow, and ultra-slow conductance elements. Enables direct backpropagation through time (BPTT) without surrogate-gradient approximations.

## Paper Reference

- **Title:** Multi-Timescale Conductance Spiking Networks: A Sparse, Gradient-Trainable Framework with Rich Firing Dynamics for Enhanced Temporal Processing
- **Authors:** Alex Fulleda-Garcia, Saray Soldado-Magraner, Josep Maria Margarit-Taulé
- **arXiv:** 2605.11835v1 (cs.NE, cs.AI, cs.LG)
- **Date:** 2026-05-12
- **PDF:** https://arxiv.org/pdf/2605.11835.pdf

## Core Problem

SNNs face a fundamental tradeoff:
1. **LIF neurons** are simple but strip away rich temporal dynamics — limited control over excitability, restricted firing repertoire
2. **Surrogate gradients** introduce forward-backward mismatch — limits faithful learning of complex temporal dynamics for regression
3. **Sparsity** managed indirectly via threshold/loss regularization rather than emerging from interpretable neuron mechanisms

## Key Innovation: Conductance-Shaped I-V Curves

### Circuit-Theoretic Foundation

Builds on Ribar & Sepulchre's reduced conductance-based framework where neuron behavior is controlled by shaping its I-V curve via parallel interconnection of positive and negative conductance elements at different timescales.

### Three-Timescale Architecture

| Timescale | Element | Function | Biological Analogy |
|-----------|---------|----------|-------------------|
| **Fast** (τf → 1) | If⁻ (negative conductance) | Creates negative differential resistance region; drives rapid depolarization (upstroke) | Na⁺ channel activation |
| **Slow** (τs ≫ τm) | Is⁺ (positive conductance) | Provides damping force; recovers membrane potential after spike; enforces refractory period | K⁺ channel activation |
| **Ultra-slow** (τus ≫ τs) | Is⁻ (slow negative) + Ius⁺ (ultra-slow positive) | Creates second negative conductance region on slow timescale; enables higher-order temporal processing | Slow adaptation currents |

### Governing Equations

**Voltage-gated conductance dynamics:**
```
τx · dUx/dt = -Ux + Vm
Ix± = αx± · tanh((Vm - Ux) / δx±)
```

**Membrane potential:**
```
τm · dVm/dt = -Vm + Σ Ix± + Iinput
```

Where:
- τx: time constant for state variable Ux relative to Vm
- αx±: maximal conductance (gain) of the channel
- δx±: voltage range where element is active

### Firing Regimes

Single model smoothly transitions between:
- **Tonic spiking:** constant firing rate under sustained input
- **Phasic spiking:** burst at stimulus onset then silence
- **Bursting:** clusters of spikes separated by quiescent periods
- **Spike frequency adaptation:** decreasing rate under constant input

## Discrete-Time Differentiable Formulation

### Key Breakthrough: No Surrogate Gradients

Unlike LIF/AdLIF models that require surrogate gradient approximations (ArcTan, SLAYER), the MTC model is **fully differentiable** because:
- Continuous voltage trajectory Um(t) is inherently smooth
- Spike generation emerges from continuous nonlinear dynamics
- State variables (Ux) evolve differentiably
- Standard BPTT applies directly

### Discretization

Explicit Euler-Forward discretization:
```
Um[t+1] = Um[t] + dt/τm · (-Vm[t] + Σ Ix±[t] + Iinput[t])
Ux[t+1] = Ux[t] + dt/τx · (-Ux[t] + Vm[t])
```

### Synaptic Transduction Model

Raw action potentials normalized to [0,1] via semi-digital communication function:
- Suppresses sub-threshold activity (s(t) = 0 for Vm < Vth)
- Maintains differentiability at spike onset for gradient computation
- Approximates nonlinear relationship between pre-synaptic voltage and neurotransmitter release

## Experimental Results: Mackey-Glass Forecasting

### Setup
- **Task:** Chaotic Mackey-Glass time series regression (γ=0.1, β=0.2, n=10, τ=17)
- **Prediction horizon:** d = 675 timesteps (~5× Lyapunov time)
- **Architecture:** Feedforward spiking network (no recurrence); temporal memory from intrinsic neuron dynamics
- **Training:** Adam optimizer, 10,000 epochs, batch size 128, Cosine Annealing LR
- **Readout:** Linear decode + 4th-order low-pass filter for continuous signal reconstruction

### Baselines
| Model | Gradient Method | Key Mechanism |
|-------|----------------|---------------|
| LIF | Surrogate (ArcTan) | Simple integrate-and-fire |
| AdLIF | SLAYER (α=5) | Spike frequency adaptation variable |
| **MTC** | **Direct BPTT** | **Multi-timescale conductances** |

### Results
- MTC **outperforms** LIF and AdLIF on Mackey-Glass forecasting
- Achieves higher sparsity naturally from conductance dynamics
- Rich firing patterns captured without recurrent network overhead
- Feedforward-only architecture with intrinsic temporal memory

## Why This Matters

### 1. Eliminates Surrogate Gradient Mismatch
The forward dynamics and backward gradients are consistent — no ad-hoc surrogate functions needed. This is critical for regression tasks where approximation error, noise, and spike discretization can severely degrade continuous-valued outputs.

### 2. Conductance-Shaped Excitability as Computation
The neuron's I-V curve is itself a computational mechanism — biological circuits exploit conductance modulation to attune to input statistics. MTC captures this explicitly.

### 3. Analog Circuit Compatibility
Localized conductance elements implementable with compact transconductance blocks (subthreshold MOS) — I-V characteristics need not be exact tanh functions, any approximately monotone nonlinearity suffices.

## Implementation Guide

### Step 1: Define Conductance Elements
```python
class MTCNeuron:
    def __init__(self):
        # Fast timescale (negative conductance)
        self.tau_f = 1.0  # → instantaneous
        self.alpha_f_minus = 1.0
        self.delta_f_minus = 0.1
        
        # Slow timescale (positive conductance)
        self.tau_s = 10.0
        self.alpha_s_plus = 0.5
        self.delta_s_plus = 0.2
        
        # Ultra-slow timescale
        self.tau_us = 100.0
        self.alpha_s_minus = 0.3
        self.alpha_us_plus = 0.2
```

### Step 2: Forward Pass (Differentiable)
```python
def forward(self, Vm, U_f, U_s, U_us, I_input, dt):
    # Update filtered voltages
    U_f = U_f + dt/self.tau_f * (-U_f + Vm)
    U_s = U_s + dt/self.tau_s * (-U_s + Vm)
    U_us = U_us + dt/self.tau_us * (-U_us + Vm)
    
    # Compute conductance currents
    I_f = self.alpha_f_minus * torch.tanh((Vm - U_f) / self.delta_f_minus)
    I_s = self.alpha_s_plus * torch.tanh((Vm - U_s) / self.delta_s_plus)
    I_s_minus = -self.alpha_s_minus * torch.tanh((Vm - U_s) / self.delta_s_minus)
    I_us = self.alpha_us_plus * torch.tanh((Vm - U_us) / self.delta_us_plus)
    
    # Update membrane potential
    Vm = Vm + dt/self.tau_m * (-Vm + I_f + I_s + I_s_minus + I_us + I_input)
    
    return Vm, U_f, U_s, U_us
```

### Step 3: Training with BPTT
```python
# Standard PyTorch training loop — no surrogate gradients needed
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
for epoch in range(10000):
    output = model(input_sequence)  # BPTT through conductance dynamics
    loss = mse_loss(filtered_output, target)
    loss.backward()  # Exact gradients through differentiable dynamics
    optimizer.step()
```

## Hyperparameter Tuning Strategy

1. **Phase-space analysis:** Analyze I-V curves and Vm traces of individual neurons under varying inputs to ensure rich temporal behavior
2. **Conductance time constants:** Grid search over τs, τus ratios relative to τm
3. **Gain parameters:** Balance αx± to avoid saturation or silence
4. **Voltage sensitivity:** Adjust δx± to control activation sharpness

## Applications

1. **Chaotic time series forecasting:** Mackey-Glass, Lorenz, financial time series
2. **Event-based sensor processing:** DVS cameras, neuromorphic audio
3. **Temporal pattern recognition:** Speech, gesture, EEG decoding
4. **Neuromorphic hardware deployment:** Analog circuit implementation
5. **Low-power edge inference:** Sparse event-driven computation

## Activation Keywords

- MTC-SNN
- multi-timescale conductance spiking
- conductance-based spiking neuron
- BPTT spiking neural network
- I-V curve shaping neuron
- surrogate-gradient-free SNN
- Mackey-Glass spiking forecasting
- 多时间尺度电导脉冲网络

## Related Skills

- `snn-learning-survey` — Comprehensive SNN learning rule survey
- `spiking-neural-network-analysis` — SNN paper analysis patterns
- `spikingjelly-framework` — SpikingJelly framework usage
- `ei-network-chaos-synchrony-theory` — E/I network dynamics theory

## Limitations & Open Questions

- Higher per-neuron computational cost than LIF
- More hyperparameters to tune (conductance gains, timescales)
- Validation needed on larger-scale tasks beyond Mackey-Glass
- Recurrent MTC networks not yet explored
- Hardware implementation details pending

## Future Directions

1. Recurrent MTC-SNN architectures
2. Self-supervised pre-training for conductance neurons
3. Cross-modal temporal processing
4. Real neuromorphic chip deployment (Loihi, SpiNNaker)
5. Integration with attention/spiking transformer architectures
