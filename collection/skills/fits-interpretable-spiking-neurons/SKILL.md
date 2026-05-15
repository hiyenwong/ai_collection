---
name: fits-interpretable-spiking-neurons
description: >
  FiTS (Frequency Selectivity and Temporal Shaping) spiking neuron methodology.
  Factorizes temporal computation within each neuron into explicit Frequency
  Selectivity (FS) and Temporal Shaping (TS) modules. The FS module
  parameterizes each neuron's target frequency as the maximizer of its
  subthreshold magnitude response; the TS module reshapes when frequency
  components contribute to membrane voltage through group-delay modulation.
  Use when: designing interpretable SNN neurons, building auditory processing
  SNNs, parameterizing neuron-level frequency preferences, implementing
  temporal shaping within spiking neurons, or analyzing learned frequency
  and timing organization in SNNs.
  Activation: FiTS, frequency selective spiking neuron, temporal shaping SNN,
  interpretable spiking neurons, group-delay modulation, neuronal resonance,
  all-pass filter spiking, frequency selectivity neuron, SHD SSC benchmarks.
---

# FiTS: Interpretable Spiking Neurons via Frequency Selectivity and Temporal Shaping

Spiking neuron that makes temporal roles explicit by factorizing neuron-level
temporal computation into Frequency Selectivity (FS) and Temporal Shaping (TS).
Enables frequency-domain initialization, learning, and post-training
interpretation within the same coordinate.

## Paper Reference

- **Title**: FiTS: Interpretable Spiking Neurons via Frequency Selectivity and Temporal Shaping
- **Authors**: Jongmin Choi, Joon Son Chung
- **arXiv**: 2605.13071 [cs.NE]
- **Date**: 2026-05-14
- **Institution**: Korea Advanced Institute of Science and Technology (KAIST)
- **Categories**: cs.NE (Neural and Evolutionary Computing)

## Core Problem

Prior work improves SNN temporal modeling through richer neuron dynamics
(adaptive/resonant) and network-level mechanisms (recurrence, delays), but
leaves each neuron's frequency preference and response timing implicit in
learned coefficients. FiTS makes these roles explicit and interpretable.

## FS Module: Learnable Frequency Selectivity

### Continuous-Time Dynamics

Extends LIF with voltage-dependent adaptation current (resonant dynamics):

$$\dot{V}(t) = -\mu V(t) + I(t) - \eta a(t)$$
$$\dot{a}(t) = -\rho a(t) + \gamma V(t)$$

Where:
- $\mu = 1/\tau_m$ (membrane time constant)
- $\rho = 1/\tau_a$ (adaptation time constant)
- $\kappa = \eta\gamma$ (voltage-adaptation coupling)

### Subthreshold Frequency Response

$$H(j\Omega) = \frac{\rho + j\Omega}{(\mu\rho + \kappa - \Omega^2) + j(\mu+\rho)\Omega}$$

### Theorem 1: Exact Target Frequency Parameterization

The target frequency (magnitude response maximizer) has a closed form:

$$\Omega^\star = \sqrt{\sqrt{\kappa(2\rho^2 + 2\rho\mu + \kappa)} - \rho^2}$$

Conversely, for any desired $\Omega^\star > 0$:

$$\kappa^\star = \rho(\rho+\mu)\left[\sqrt{1 + \frac{(1 + (\Omega^\star/\rho)^2)^2}{(1 + \mu/\rho)^2}} - 1\right]$$

**Key innovation**: Instead of learning $\kappa$ directly (implicit frequency),
FiTS learns $\Omega^\star$ directly and computes $\kappa^\star$ via the
inverse mapping. This makes the target frequency the common quantity for
initialization, optimization, and post-training interpretation.

### Discrete-Time Implementation

Semi-implicit Euler discretization:

$$V_0[k+1] = (1-\mu\Delta t)V[k] - \eta\Delta t \cdot a[k] + I[k]$$
$$a[k+1] = (1-\rho\Delta t)a[k] + \gamma\Delta t \cdot V_0[k+1]$$

## TS Module: Learnable Temporal Shaping

Reshapes when frequency components contribute to pre-spike membrane voltage
accumulation through group-delay modulation.

### All-Pass Filter Cascade

M-stage cascade of first-order all-pass filters (preserve magnitude, modify phase):

$$A_m(z) = \frac{z^{-1} - \beta_m}{1 - \beta_m z^{-1}}, \quad A^{(M)}(z) = \prod_{m=1}^M A_m(z)$$

### Group-Delay Modulation via λ-Mixing

$$\tilde{V}_m[k+1] = (1-\lambda_m)\tilde{V}_{m-1}[k+1] + \lambda_m V_m[k+1]$$

Where $\lambda_m \in [0,1]$ controls contribution of each all-pass stage.

**Key innovation**: λ-mixing can induce negative group-delay shift, impossible
under pure all-pass cascade composition. This enables richer temporal shaping
with only 2M additional neuron-wise parameters.

## Architecture

```
Input → FS Module (Ω* → κ* mapping) → TS Module (AP cascade + λ-mixing)
       ↓                                     ↓
    V₀[k+1] (pre-reset voltage)          Ṽ_M[k+1] (effective voltage)
                                               ↓
                                          Threshold check → Spike
```

## Key Properties

1. **Explicit frequency control**: Each neuron has a learnable target frequency Ω*
2. **Closed-form inverse**: Ω* ↔ κ* mapping enables frequency-domain initialization
3. **Group-delay shaping**: TS module controls timing without changing magnitude response
4. **Negative group-delay**: λ-mixing enables behavior beyond pure AP composition
5. **LIF recoverable**: Setting η=0 (κ=0) recovers standard LIF (Ω*=0)
6. **Interpretable**: Post-training, read Ω* and group-delay shifts to understand neuron roles

## Experimental Results

### Benchmarks
- SHD (Spiking Heidelberg Digits): 20-class speech
- SSC (Spiking Speech Commands): 35-class keyword spotting
- GSC (Google Speech Commands): non-spiking variant

### Performance
- FiTS consistently improves over plain LIF baseline in simple feedforward SNNs
- Competitive with strong temporal SNN baselines (no recurrence or network-level delays needed)
- Learned target frequencies and group-delay shifts provide interpretable neuron-level summaries

## Implementation Pattern

```python
import torch
import torch.nn as fi

class FiTSNeuron(nn.Module):
    """FiTS spiking neuron with FS and TS modules."""
    
    def __init__(self, ts_stages=2):
        super().__init__()
        # FS: learnable target frequency
        self.omega_star = nn.Parameter(torch.tensor(1.0))  # rad/s
        
        # TS: all-pass filter parameters
        self.M = ts_stages
        self.beta = nn.Parameter(torch.zeros(ts_stages))  # tanh constrained
        self.lam = nn.Parameter(torch.zeros(ts_stages))   # sigmoid constrained
        
        # Fixed: membrane & adaptation time constants
        self.mu = 1.0 / 0.02   # τ_m = 20ms
        self.rho = 1.0 / 0.05  # τ_a = 50ms
    
    def compute_kappa(self):
        """Inverse mapping: Ω* → κ* (Theorem 1)"""
        omega = torch.abs(self.omega_star)
        mu, rho = self.mu, self.rho
        term = (1 + (omega/rho)**2)**2 / (1 + mu/rho)**2
        kappa = rho * (rho + mu) * (torch.sqrt(1 + term) - 1)
        return kappa
    
    def forward(self, input_current, state):
        # FS module: compute κ* from Ω*, then discrete-time update
        kappa = self.compute_kappa()
        eta = kappa  # simplified (η·γ = κ)
        gamma = 1.0
        
        V0 = (1 - self.mu*dt) * state['V'] - eta*dt * state['a'] + input_current
        a_new = (1 - self.rho*dt) * state['a'] + gamma*dt * V0
        
        # TS module: all-pass cascade + λ-mixing
        V_ts = self.temporal_shaping(V0, state)
        
        # Spike generation
        spike = (V_ts > self.threshold).float()
        V_reset = V_ts * (1 - spike)  # reset on spike
        
        return spike, {'V': V_reset, 'a': a_new}
```

## When to Use This Skill

- Designing interpretable spiking neurons with explicit frequency preferences
- Building auditory processing SNNs (speech, keyword spotting, music)
- Parameterizing neuron-level temporal roles in SNNs
- Analyzing learned frequency and timing organization post-training
- Implementing frequency-domain initialization for SNNs
- Comparing with adaptive/resonant LIF variants (AdLIF, PLIF, etc.)
- Understanding group-delay modulation in neural dynamics

## Related Work

- Adaptive LIF neurons (AdLIF, GLIF, CLIF)
- Resonate-and-fire models (Izhikevich)
- Structured state-space spiking models
- Learnable synaptic/axonal delays (DelRec)
- FSTA-SNN (frequency-domain attention, feature-level not neuron-level)

## Pitfalls

1. **Continuous vs. discrete gap**: Ω* is continuous-time parameter; realized discrete-time target may differ slightly. Use small Δt for accuracy.
2. **Semi-implicit vs. explicit Euler**: Semi-implicit is used for stability; explicit Euler gives different discrete dynamics.
3. **λ-mixing constraint**: λ_m must be in [0,1]; use sigmoid parameterization.
4. **β constraint**: |β_m| < 1 for stability; use tanh parameterization.
5. **Not a replacement for recurrence**: FiTS enhances individual neurons; combine with recurrent architectures for maximum effect.
6. **Auditory domain focus**: Best results on frequency-structured inputs; may need adaptation for other modalities.
