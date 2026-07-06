---
name: mean-field-low-rank-adaptation-oscillations
version: 1.0.0
description: >
  Dynamical mean-field theory for low-rank recurrent networks with firing-rate adaptation.
  Identifies four oscillatory regimes and bifurcation mechanisms linking chaos, Hopf bifurcation,
  and noise-sustained oscillations to biological rhythms (Up-Down states, waxing-and-waning episodes).
trigger_phrases:
  - mean-field theory
  - low-rank recurrent network
  - firing-rate adaptation
  - oscillatory dynamics
  - chaos onset
  - Hopf bifurcation
  - Up-Down states
  - coherent state
  - noise-sustained oscillations
activation_keywords:
  - neural oscillations
  - working memory
  - sleep rhythms
  - anesthesia
  - criticality
  - dynamical systems
  - reduced-order model
  - bifurcation analysis
tags:
  - q-bio.NC
  - computational neuroscience
  - dynamical systems
  - mean-field theory
  - oscillations
  - adaptation
created: 2026-06-30
arxiv_id: "2606.30366"
arxiv_url: https://arxiv.org/abs/2606.30366
authors:
  - Bowen W. Zheng
  - Earl K. Miller
  - Ila R. Fiete
affiliations:
  - MIT (Earl K. Miller lab)
  - Stanford (Ila R. Fiete lab)
publication_date: 2026-06-29
---

# Mean-Field Theory of Rich Oscillatory Dynamics in Low-Rank Recurrent Networks with Activity-Dependent Adaptation

## Abstract
Dynamical mean-field theory for random recurrent networks with low-rank structure and firing-rate-driven adaptation. When random connectivity is strong enough to generate chaos, increasing adaptation strength drives the network through four regimes: static coherent state → noise-sustained oscillations (regular → irregular) → stochastic switching between symmetric wells → global limit cycle. The theory identifies two instability mechanisms (chaos onset from random connectivity + Hopf bifurcation of coherent mode) and shows how adaptation shapes both through frequency-dependent single-neuron transfer function. A reduced 3D model captures bifurcation structure. Above chaos threshold, coherent population-level oscillations coexist with heterogeneous firing rates and network-generated stochasticity at single-neuron level. Produces waxing-and-waning rhythmic episodes, persistent state switching, and slow Up-Down alternations — dynamics observed during wakefulness, sleep, and anesthesia.

## Core Insights

### 1. Four Dynamical Regimes
Adaptation strength creates a progression through qualitatively distinct regimes:
- **Regime I (Static Coherent State)**: Weak adaptation, stable fixed point
- **Regime II (Noise-Sustained Oscillations)**: Regular → irregular oscillations via noise amplification near bifurcation
- **Regime III (Stochastic Switching)**: Bistable regime with noise-driven transitions between symmetric attractor wells
- **Regime IV (Global Limit Cycle)**: Strong adaptation drives deterministic oscillations

### 2. Two Instability Mechanisms
- **Chaos onset**: Driven by random connectivity strength (classical mean-field instability)
- **Hopf bifurcation of coherent mode**: Adaptation creates oscillatory instability even in non-chaotic regime

These mechanisms interact: adaptation reshapes the frequency-dependent single-neuron transfer function, modifying both chaos threshold and oscillation frequency.

### 3. Reduced 3D Model
Full network dynamics captured by 3D ODE system tracking:
- Mean population activity (m)
- Adaptation variable (a)
- Variance of activity (Δ)

This reduction preserves bifurcation structure and enables analytical tractability.

### 4. Coexistence of Scales
Above chaos threshold:
- **Population level**: Coherent oscillations (macroscopic order)
- **Single-neuron level**: Heterogeneous firing rates + network-generated stochasticity (microscopic variability)

This explains how structured population dynamics emerge from seemingly irregular single-unit activity.

### 5. Biological Relevance
Theory accounts for empirically observed phenomena:
- **Waxing-and-waning rhythmic episodes**: Sleep spindles, alpha bursts
- **Persistent state switching**: Bistable perception, working memory switches
- **Slow Up-Down alternations**: Slow-wave sleep, anesthesia (isoflurane, propofol)

## Methodology

### Model Specification
- **Network**: N → ∞ neurons with random Gaussian connectivity (variance g²/N) + low-rank structure
- **Neuron model**: Rate-based with firing-rate adaptation (time constant τ_a)
- **Connectivity**: J_ij = g/√N * χ_ij + low-rank components (e.g., rank-1 for line attractor)
- **Adaptation**: a_i evolves as τ_a * da_i/dt = -a_i + r_i(t) (firing-rate feedback)

### Mean-Field Derivation
1. **Self-consistency equations**: Express order parameters (m, Δ) in terms of single-neuron statistics
2. **Frequency-dependent transfer function**: Adaptation modifies neuron gain as function of input frequency
3. **Linear stability analysis**: Compute eigenvalues of Jacobian around fixed point
4. **Bifurcation tracking**: Vary adaptation strength (β) and connectivity (g) to map phase diagram

### Reduced Model Construction
- **Moment closure**: Truncate hierarchy at second order (Gaussian assumption)
- **Slow-fast decomposition**: Separate fast (activity) and slow (adaptation) timescales
- **Center manifold reduction**: Project dynamics onto critical eigenspace near bifurcation

## Key Equations

### Mean-Field Equations (Schematic)
```
dm/dt = -m + F(m, a, Δ; g, β)
da/dt = (-a + m) / τ_a
dΔ/dt = G(m, a, Δ; g, β)
```
where F is nonlinear transfer function incorporating adaptation, G captures variance dynamics.

### Transfer Function with Adaptation
```
F(m, a, Δ) = ∫ Dξ φ(√Δ * ξ + m - a)
```
where φ is single-neuron activation function, Dξ is Gaussian measure.

Adaptation enters as effective subtraction from input: m_eff = m - a.

### Chaos Threshold
```
g_c(β) = 1 / max_ω |χ(ω)|
```
where χ(ω) is frequency-dependent susceptibility modified by adaptation.

## Applications & Extensions

### 1. Working Memory
Low-rank structure implements line attractor; adaptation enables switching between memory states. Predicts:
- Drift timescale controlled by adaptation strength
- Noise-induced switching rate follows Kramers escape formula

### 2. Sleep & Anesthesia
Regime III-IV transitions model:
- Slow oscillation (<1 Hz) during NREM sleep
- Burst-suppression patterns under deep anesthesia
- Predicts bifurcation markers for depth-of-anesthesia monitoring

### 3. Neural Variability
Theory predicts:
- Fano factor modulation across oscillation cycle
- Trial-to-trial variability peaks near bifurcation (criticality)
- Noise correlation structure depends on regime

### 4. Criticality
Hopf bifurcation provides mechanism for operating near critical point:
- Maximized dynamic range
- Optimal information transmission
- Power-law avalanches (when extended to spiking networks)

## Implementation Guide

### Minimal Simulation (Python/JAX)
```python
import jax.numpy as jnp
from jax import jit

@jit
def mean_field_step(m, a, Delta, g, beta, tau_a, dt):
    """One Euler step of 3D reduced model."""
    # Transfer function (tanh approximation)
    m_eff = m - beta * a
    F = jnp.tanh(jnp.sqrt(Delta) * m_eff)
    
    # Variance dynamics
    G = g**2 * (1 - F**2)**2 - Delta
    
    # Euler integration
    m_new = m + dt * (-m + F)
    a_new = a + dt * (-a + m) / tau_a
    Delta_new = Delta + dt * G
    
    return m_new, a_new, Delta_new
```

### Parameter Sweeps
To reproduce phase diagram:
- Vary `g` ∈ [0.5, 2.0] (connectivity strength)
- Vary `beta` ∈ [0.0, 1.0] (adaptation strength)
- For each (g, beta), simulate 10k steps, compute:
  - Power spectrum → detect oscillations
  - Autocorrelation → detect switching
  - Variance → detect bifurcations

### Bifurcation Detection
Use `PyDSTool` or `AUTO` for continuation:
```python
from PyDSTool import *

# Define ODE system
args = args(fast_weight=g, slow_weight=beta, tau_a=10.0)
DSargs = args
DSargs.varspecs = {
    'm': '-m + tanh(sqrt(Delta)*(m - beta*a))',
    'a': '(-a + m)/tau_a',
    'Delta': 'g**2 * (1 - tanh(sqrt(Delta)*(m - beta*a))**2)**2 - Delta'
}
DSargs.pars = {'g': 1.0, 'beta': 0.5, 'tau_a': 10.0}

ds = Generator.Dopri5(DSargs)
# Bifurcation continuation in beta
```

## Connections to Existing Work

### Classical Mean-Field Theory
- **Sompolinsky et al. (1988)**: Chaos in random networks (g_c = 1)
- **Cavanagh et al. (2017)**: Low-rank structure for working memory
- **Schuessler et al. (2020)**: Mixed selectivity in low-rank networks

### Adaptation in Neural Models
- **Miller & Wang (2006)**: Adaptation in attractor networks
- **Mongillo et al. (2008)**: Synaptic facilitation as working memory
- **Murray et al. (2017)**: Adaptation-induced oscillations

### Biological Oscillations
- **Sanchez-Vives & Mattia (2014)**: Slow oscillations in sleep
- **Haider et al. (2013)**: Up-Down states in vivo
- **Hudson et al. (2014)**: Noise-induced oscillations in V1

## Future Directions

### 1. Spiking Extension
Convert rate model to spiking (LIF or GLIF):
- Test if mean-field predictions hold at single-spike resolution
- Derive spike-count corrections to rate-based theory
- Compare with large-scale spiking network simulations

### 2. Multi-Population Extension
Include excitatory-inhibitory balance:
- Add inhibitory population with its own adaptation
- Study gamma-theta coupling mechanisms
- Model cross-frequency phase-amplitude coupling

### 3. Learning Rules
Incorporate synaptic plasticity:
- STDP + homeostatic plasticity → self-organized criticality?
- Meta-learning of adaptation time constants
- Task-driven optimization of low-rank structure

### 4. Experimental Validation
Test predictions with:
- **In vivo recordings**: Verify regime transitions during sleep-wake cycle
- **Optogenetics**: Perturb adaptation (e.g., modulate K+ channels)
- **MEG/EEG**: Detect bifurcation markers in human recordings

## References

1. Zheng, B.W., Miller, E.K., & Fiete, I.R. (2026). Mean-field theory of rich oscillatory dynamics in low-rank recurrent networks with activity-dependent adaptation. *arXiv:2606.30366*.
2. Sompolinsky, H., Crisanti, A., & Sommers, H.J. (1988). Chaos in random neural networks. *Physical Review Letters*, 61(23), 2596.
3. Cavanagh, S.E., Tower-Seyal, K., & Fiete, I.R. (2017). Flexible working memory in low-rank recurrent networks. *NeurIPS*.
4. Mongillo, G., Barak, O., & Tsodyks, M. (2008). Synaptic theory of working memory. *Science*, 319(5869), 1543-1546.
5. Murray, J.D., et al. (2017). Stable population coding for working memory coexists with heterogeneous neural dynamics. *PNAS*, 114(2), 394-399.
