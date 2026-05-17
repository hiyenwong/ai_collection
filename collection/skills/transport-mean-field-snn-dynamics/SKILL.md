---
name: transport-mean-field-snn-dynamics
description: >
  Transport mean field methodology for approximating macroscopic dynamics of spiking neural
  networks. Derives population firing rate evolution from initial voltage distributions through
  a Fokker-Planck system, based on transport solutions to the advection equation. Unlike
  traditional mean field approaches using asynchronous steady-state solutions, this method
  captures firing rate fluctuations emerging from dynamic interaction between time-varying
  inputs, initial densities, and coupling in neural populations. Applicable to integrate-and-fire
  networks with slow time-varying inputs in the excitation-driven regime.
  Use when: modeling neural population dynamics, mean field theory for SNNs, firing rate
  fluctuations, Fokker-Planck approaches to neural dynamics, transport equation in neuroscience,
  population-level neural modeling.
  Keywords: transport mean field, Fokker-Planck SNN, firing rate fluctuations, population
  dynamics, integrate-and-fire mean field, advection equation neuroscience, voltage distribution
  dynamics, neural population modeling.
---

# Transport Mean Field SNN Dynamics

arXiv: 2605.14319 | Nicola & Campbell (May 2026)

## Core Contribution

Analytically derives approximate macroscopic dynamics for populations of coupled
integrate-and-fire neurons by solving the transport equation for the advection dynamics,
predicting how firing rate fluctuations emerge from initial voltage distributions under
time-varying inputs.

## Problem Addressed

Firing rate fluctuations are observed experimentally at multiple time scales:
- **Single neurons**: Trial-to-trial variability
- **Across trials**: Stimulus-elicited response variability
- **Across populations**: Population-level rate oscillations and transients

Traditional mean field approaches assume asynchronous or constant flux steady states,
which fail to capture dynamic transients and initial-condition-dependent fluctuations.

## Key Methodology

### Transport-Based Mean Field

The population of neurons is described by a probability density function `ρ(v, t)` over
the voltage variable `v` at time `t`:

```
∂ρ/∂t + ∂/∂v [μ(v,t) · ρ] = D · ∂²ρ/∂v²
```

where:
- `μ(v,t)`: drift term (time-varying input + coupling effects)
- `D`: diffusion coefficient (noise/variance)
- `ρ(v,t)`: voltage distribution density

### Transport Solution (Advection Equation)

When diffusion is small and inputs are slow, the dominant dynamics come from the
transport (advection) term:

```
∂ρ/∂t + ∂/∂v [μ(v,t) · ρ] = 0
```

The solution follows characteristics of the ODE:

```
dv/dt = μ(v, t)
```

This gives a closed-form approximation for the evolution of the voltage distribution
and the resulting population firing rate.

### Flux Calculation

The instantaneous population firing rate (flux) at the threshold `v_th`:

```
r(t) = J(v_th, t) = μ(v_th, t) · ρ(v_th, t) - D · ∂ρ/∂v|_{v_th}
```

The transport approximation provides `ρ(v_th, t)` by tracking how the initial
distribution evolves along characteristics.

## Assumptions

1. **Slow inputs**: Time-varying inputs change slowly compared to neuronal timescales
2. **Excitation-driven regime**: Neurons operate in a regime dominated by excitatory drive
3. **Integrate-and-fire neurons**: LIF or similar models with reset mechanism
4. **Coupled network**: Recurrent connections modeled through mean field coupling

## When to Use This Approach

| Scenario | Recommended |
|----------|------------|
| Steady-state analysis | Traditional mean field (steady-state FP) |
| Dynamic transients | **Transport mean field** (this method) |
| Fast-varying inputs | Full Fokker-Planck simulation |
| Initial condition effects | **Transport mean field** (this method) |
| Large coupled networks | **Transport mean field** (this method) |

## Mathematical Framework

### Characteristic Equations

For the advection equation `∂ρ/∂t + ∂(μρ)/∂v = 0`:

```python
# Characteristic curve: tracks voltage evolution
def characteristic(t, v0, mu_fn):
    """Solve dv/dt = mu(v, t) with initial condition v(0) = v0."""
    # Numerical integration along characteristics
    from scipy.integrate import solve_ivp
    sol = solve_ivp(
        lambda t, v: mu_fn(v, t),
        [0, t],
        [v0],
        method='RK45',
        dense_output=True
    )
    return sol.sol(t)[0]

# Density evolution along characteristics
def density_along_characteristic(v0, t, rho_0, mu_fn):
    """Compute density at time t for a characteristic starting at v0."""
    v_t = characteristic(t, v0, mu_fn)
    # Jacobian of characteristic map
    # ρ(v,t) = ρ₀(v₀) / |∂v(t)/∂v₀|
    jacobian = compute_jacobian(v0, t, mu_fn)
    return rho_0(v0) / abs(jacobian)
```

### Firing Rate Prediction

```python
def predict_firing_rate(rho_0, mu_fn, v_reset, v_threshold, t_eval):
    """Predict population firing rate from initial voltage distribution."""
    rates = []
    for t in t_eval:
        # Find which initial conditions reach threshold at time t
        v_at_t = [characteristic(t, v0, mu_fn) for v0 in v_grid]
        # Count crossings and compute flux
        flux = compute_flux_at_threshold(
            rho_0, v_grid, v_at_t, mu_fn, v_threshold, t
        )
        rates.append(flux)
    return np.array(rates)
```

## Key Insights

1. **Initial conditions matter**: The initial voltage distribution significantly affects
   transient firing rate dynamics — a feature absent from steady-state mean field theory

2. **Dynamic interaction**: Fluctuations emerge from the interplay of:
   - Time-varying external inputs
   - Initial voltage density shape
   - Recurrent coupling strength

3. **Transport vs. diffusion**: In the excitation-driven regime with slow inputs,
   the transport (deterministic drift) dominates over diffusion, making the advection
   equation a good approximation

4. **Computational efficiency**: Transport solution is much faster than full
   Fokker-Planck simulation while capturing essential transient dynamics

## Comparison with Other Mean Field Approaches

| Method | Captures Transients | Computational Cost | Accuracy |
|--------|-------------------|-------------------|----------|
| Steady-state FP | ❌ | Low | Good for steady state |
| Full FP simulation | ✅ | High | Very good |
| **Transport MF** | ✅ | **Medium** | **Good for slow inputs** |
| QIF mean field | Partial | Medium | Limited model class |

## Applications

- **Neural population modeling**: Predicting population-level firing dynamics
- **Stimulus response analysis**: Understanding trial-to-trial variability
- **Network state transitions**: Analyzing how networks transition between states
- **Theoretical neuroscience**: Bridging microscopic neuron models to macroscopic dynamics
- **SNN macroscopic analysis**: Understanding population-level behavior of spiking networks

## Activation

- transport mean field SNN, Fokker-Planck neural dynamics
- firing rate fluctuations, population dynamics
- integrate-and-fire mean field, advection equation neuroscience
- voltage distribution dynamics, neural population modeling
- 传输平均场, 脉冲神经网络动力学, 群体神经动力学

## Limitations

- Requires slow input assumption — not valid for rapidly changing stimuli
- Excitation-driven regime only — may not apply to inhibition-dominated networks
- Approximation quality degrades when diffusion becomes significant
- Single-population mean field — extensions needed for multi-population networks

## Related Work

- Brunel & Hakim (1999): Fast global oscillations in sparsely connected networks
- Fourcaud & Brunel (2002): Dynamics of population activity in networks of integrate-and-fire neurons
- Montbrió et al. (2015): Macroscopic description for networks of QIF neurons
- Deco et al. (2008): The dynamic brain: from spiking neurons to neural masses
