---
name: parametrically-driven-oscillator-neuromorphic
description: "Reservoir computing using parametrically-driven oscillators and frequency combs (arXiv:2604.21861). Demonstrates neuromorphic computation via two-mode parametric oscillator with 2:1 resonance across sub-threshold, parametric resonance, and frequency-comb regimes. Covers drive amplitude input encoding, temporal/spectral response sampling, chaotic time-series prediction (Mackey-Glass, Rossler, Lorenz), and design principles for tuning physical oscillator-based reservoir computers."
version: '1.0'
date: '2026-04-23'
authors: [Mahadev Sunil Kumar, Adarsh Ganesan]
arxiv_id: '2604.21861v1'
categories: [cs.NE, nlin.PS]
tags: [neuromorphic-computing, reservoir-computing, parametric-oscillator, frequency-comb, parametric-resonance, nonlinear-dynamics, chaotic-prediction, physical-reservoir-computing]
---

# Neuromorphic Computing Based on Parametrically-Driven Oscillators and Frequency Combs

**arXiv:** [2604.21861](https://arxiv.org/abs/2604.21861)
**Date:** April 23, 2026
**Authors:** Mahadev Sunil Kumar, Adarsh Ganesan
**Categories:** cs.NE, nlin.PS

## Summary

This paper investigates a two-mode parametrically driven oscillator system as a physical platform for reservoir computing. The system exhibits 2:1 parametric resonance and operates across three dynamical regimes — sub-threshold (linear), parametric resonance (nonlinear but coherent), and frequency-comb (high spectral dimensionality). Input signals are encoded as modulations of the parametric drive amplitude, and the oscillator's temporal and spectral responses serve as reservoir states. The approach is benchmarked on one step-ahead prediction of chaotic systems (Mackey-Glass, Rössler, Lorenz).

**Key finding:** Optimal computational performance is achieved at the parametric resonance boundary, where nonlinear interactions are activated while temporal coherence is preserved. Frequency-comb states offer increased spectral dimensionality but suffer from inconsistent performance, especially in the chaotic comb regime where phase coherence is lost. This establishes parametric resonance as a robust operating regime for oscillator-based neuromorphic computing.

## Key Contributions

1. **Three-regime characterization for reservoir computing:** Systematic mapping of computational performance across sub-threshold, parametric resonance, and frequency-comb dynamical regimes of a two-mode parametric oscillator.

2. **Parametric resonance as optimal operating point:** Identification that the boundary of the parametric resonance region provides the best trade-off between nonlinear transformation capability and temporal coherence.

3. **Input encoding via drive amplitude modulation:** Demonstrating that encoding input data into the parametric pump amplitude is an effective and physically realizable input method for oscillator-based reservoirs.

4. **Bifurcation-structure correspondence:** Direct mapping between prediction error landscapes and the underlying bifurcation structure, with low-error regions aligned to parametric resonance boundaries.

5. **Design principles for physical reservoirs:** Systematic analysis of how input modulation depth, detuning from frequency matching, damping ratio, and input data rate control accessible dynamical regimes and computational performance.

6. **Chaotic time-series prediction benchmarks:** Demonstrating reservoir performance on Mackey-Glass, Rössler, and Lorenz chaotic systems, validating the approach across multiple dynamical complexities.

## Methodology

### Step 1: Define the Two-Mode Parametric Oscillator System

Set up a system of two coupled oscillators exhibiting 2:1 parametric resonance, where a pump mode at frequency ω_p drives a signal mode at frequency ω_s ≈ ω_p/2:

- The pump mode is directly driven by an external force with amplitude that encodes the input signal
- The signal mode responds through nonlinear parametric coupling
- Key parameters: pump frequency ω_p, signal frequency ω_s, detuning δ = ω_s - ω_p/2, damping coefficients γ₁, γ₂, and nonlinear coupling strength

### Step 2: Encode Input Signals as Drive Amplitude Modulation

- Scale the input time series (e.g., Mackey-Glass, Rössler, Lorenz) to a suitable amplitude range
- Modulate the parametric drive amplitude with the scaled input: F(t) = F₀ + ε·u(t), where F₀ is the base drive amplitude, ε is the input scaling, and u(t) is the input signal
- The input scaling ε controls the depth of modulation and thus the dynamical regime accessible to the reservoir

### Step 3: Simulate/Simulate the Oscillator Response

- Numerically integrate the coupled oscillator equations using appropriate ODE solvers
- Allow a washout period at initialization to let transients decay
- For each input sample, record the oscillator's temporal state variables (amplitudes, phases of both modes) over a sampling window
- Optionally compute the Fourier transform to obtain spectral responses

### Step 4: Construct the Reservoir State Vector

- Collect temporal samples: sample the oscillator state at multiple time points within each input step to form a temporal feature vector
- Collect spectral samples: compute the frequency spectrum and sample at predefined frequency bins to form a spectral feature vector
- The combined temporal and spectral responses provide the high-dimensional reservoir state

### Step 5: Train the Readout Layer

- Use ridge regression (or similar linear regression with regularization) to map reservoir states to target outputs
- Training target: one step-ahead value of the chaotic time series
- Split data into training and testing sets; optimize the ridge regularization parameter

### Step 6: Evaluate Prediction Performance

- Compute normalized mean squared error (NMSE) or similar metric on test predictions
- Map prediction error across parameter space (drive amplitude, detuning, damping) to identify optimal operating regions
- Compare performance across the three dynamical regimes

### Step 7: Analyze Bifurcation Correspondence

- Compute bifurcation diagrams of the oscillator system as parameters vary
- Overlay prediction error maps with bifurcation boundaries
- Identify the relationship between dynamical regime transitions and computational capability

## Mathematical Framework

### Two-Mode Parametric Oscillator Equations

The system consists of two coupled modes with 2:1 parametric resonance:

```
ẍ₁ + 2γ₁ẋ₁ + ω₁²x₁ = F(t)·cos(ω_p·t) + α·x₂²

ẍ₂ + 2γ₂ẋ₂ + ω₂²x₂ = β·x₁·x₂
```

where:
- x₁, x₂ are the pump and signal mode displacements
- γ₁, γ₂ are damping coefficients for each mode
- ω₁, ω₂ are natural frequencies (ω₂ ≈ ω₁/2 for 2:1 resonance)
- F(t) = F₀ + ε·u(t) is the input-modulated drive amplitude
- α, β are nonlinear coupling coefficients
- ω_p is the external pump frequency

### Parametric Resonance Condition

2:1 parametric resonance occurs when:
```
ω_p ≈ 2·ω₂  (pump frequency is approximately twice the signal frequency)
```

The instability tongue (Arnold tongue) in the (F₀, δ) parameter plane defines the parametric resonance region, where δ = ω₂ - ω_p/2 is the detuning.

### Frequency-Comb Generation

When the drive amplitude exceeds the parametric resonance threshold, the nonlinear interactions generate a cascade of equidistant spectral lines (frequency comb) centered around the signal mode frequency. The comb spacing is determined by the detuning and the nonlinear coupling strength.

### Reservoir State Construction

For input sample u(t_n) at discrete time step n:
```
S_n = [x₁(t_n), ẋ₁(t_n), x₂(t_n), ẋ₂(t_n), |X₁(f₁)|, |X₁(f₂)|, ..., |X₂(f₁)|, |X₂(f₂)|, ...]
```

where X₁(f), X₂(f) are the Fourier transforms of the temporal windows for each mode.

### Readout Training

The readout weights W are trained via ridge regression:
```
W = S_trainᵀ · Y_train · (S_train · S_trainᵀ + λ·I)⁻¹
```

where S_train is the matrix of reservoir states, Y_train is the target output, and λ is the regularization parameter.

## Results

### Performance Across Dynamical Regimes

| Regime | Nonlinearity | Coherence | Prediction Quality |
|--------|-------------|-----------|-------------------|
| Sub-threshold | Low (linear) | High | Moderate (limited transformation) |
| Parametric resonance | Moderate (activated) | High (preserved) | **Best** (optimal trade-off) |
| Frequency comb (periodic) | High | Moderate | Variable across existence band |
| Frequency comb (chaotic) | High | Lost (no phase coherence) | Degraded |

### Key Observations

1. **Parametric resonance boundary is the sweet spot:** The transition region between sub-threshold and parametric resonance provides the richest nonlinear transformation while maintaining temporal coherence necessary for accurate prediction.

2. **Frequency combs are not universally better:** Despite increased spectral dimensionality, frequency-comb states show inconsistent performance across their existence band and degrade significantly in the chaotic comb regime.

3. **Design parameter sensitivity:**
   - **Input modulation depth (ε):** Controls the dynamical regime; too small keeps the system linear, too large pushes into chaotic comb
   - **Detuning (δ):** Affects the width and position of the parametric resonance tongue; small detuning broadens the optimal region
   - **Damping ratio (γ₂/γ₁):** Higher damping narrows the parametric resonance region but improves stability
   - **Input data rate:** Must be matched to the oscillator's intrinsic timescales for effective information transfer

4. **Bifurcation-error correspondence:** NMSE maps directly mirror the bifurcation structure — the lowest error regions trace the parametric resonance boundaries in parameter space.

### Benchmark Results

The system achieves competitive one step-ahead prediction on:
- **Mackey-Glass** (τ=17): Captures the delayed feedback dynamics through the oscillator's memory
- **Rössler system:** Captures the oscillatory and chaotic components
- **Lorenz system:** Captures the butterfly dynamics through multi-scale spectral features

## Implementation Notes

### Simulation Setup

```python
import numpy as np
from scipy.integrate import solve_ivp

def parametric_oscillator(t, state, F0, epsilon, u_func, gamma1, gamma2,
                          omega1, omega2, omega_p, alpha, beta):
    """Two-mode parametric oscillator with input-modulated drive."""
    x1, v1, x2, v2 = state

    # Input-modulated drive amplitude
    F_t = F0 + epsilon * u_func(t)

    # Pump mode (driven by external force + nonlinear coupling)
    dx1 = v1
    dv1 = (-2*gamma1*v1 - omega1**2*x1
            + F_t * np.cos(omega_p*t)
            + alpha * x2**2)

    # Signal mode (parametrically driven through coupling)
    dx2 = v2
    dv2 = (-2*gamma2*v2 - omega2**2*x2
            + beta * x1 * x2)

    return [dx1, dv1, dx2, dv2]
```

### Reservoir State Extraction

```python
def extract_reservoir_state(t_response, x1_response, x2_response,
                            v1_response, v2_response, spectral_bins=32):
    """Extract temporal and spectral features from oscillator response."""
    # Temporal features: uniformly sampled states
    temporal = np.concatenate([x1_response, x2_response,
                                v1_response, v2_response])

    # Spectral features: FFT magnitudes at selected bins
    X1_fft = np.abs(np.fft.rfft(x1_response))[:spectral_bins]
    X2_fft = np.abs(np.fft.rfft(x2_response))[:spectral_bins]

    spectral = np.concatenate([X1_fft, X2_fft])
    return np.concatenate([temporal, spectral])
```

### Readout Training with Ridge Regression

```python
from sklearn.linear_model import Ridge

def train_readout(states, targets, alpha=1e-3):
    """Train linear readout via ridge regression."""
    model = Ridge(alpha=alpha)
    model.fit(states, targets)
    return model
```

### Parameter Sweep for Regime Mapping

```python
def sweep_parameters(F0_range, delta_range, input_data, target_data):
    """Map prediction error across (F0, detuning) parameter space."""
    results = np.zeros((len(F0_range), len(delta_range)))

    for i, F0 in enumerate(F0_range):
        for j, delta in enumerate(delta_range):
            # Set detuning by adjusting omega_p or omega2
            omega_p = 2 * (omega2_base + delta)

            # Run reservoir, collect states
            states = run_reservoir(F0, delta, input_data)

            # Train and evaluate
            model = train_readout(states[:train_len], targets[:train_len])
            predictions = model.predict(states[train_len:])
            results[i, j] = np.mean((predictions - targets[train_len:])**2)

    return results
```

### Practical Implementation Tips

1. **Washout period:** Allow 100-500 oscillator periods for transient decay before collecting reservoir states
2. **Input scaling:** Normalize input data to [0, 1] or [-1, 1] before modulating the drive; typical ε values are 0.01-0.1 of F₀
3. **Sampling rate:** Sample the oscillator state at 10-50 points per input step to build rich temporal features
4. **ODE solver:** Use adaptive-step solvers (RK45 or DOP853) with tight tolerances (rtol=1e-8, atol=1e-10) near bifurcation boundaries
5. **Regularization:** Ridge parameter λ typically ranges from 1e-6 to 1e-2; use cross-validation to select
6. **Spectral binning:** 16-64 frequency bins per mode provide sufficient spectral features without overfitting

## Pitfalls

1. **Operating too deep in the frequency-comb regime:** The chaotic comb regime destroys phase coherence, leading to unpredictable reservoir states and poor prediction. Stay near the parametric resonance boundary.

2. **Mismatched timescales:** If the input data rate is much faster or slower than the oscillator's natural timescale, information transfer degrades. Match the oscillator's relaxation time to the input sampling interval.

3. **Excessive input modulation:** If ε·u(t) overwhelms F₀, the system can be driven into chaotic regimes unpredictably. Keep ε small relative to F₀.

4. **Ignoring washout:** Collecting states before transients decay contaminates the reservoir state with initial condition artifacts. Always discard an adequate washout period.

5. **Over-reliance on spectral features alone:** Temporal features near the parametric resonance boundary may be more informative than spectral ones. Use both temporal and spectral sampling.

6. **Single operating point optimization:** The optimal parameters are regime-dependent. Sweeping across (F₀, δ) space is essential to find the true optimum.

7. **Neglecting damping effects:** Higher damping can stabilize the system but narrows the parametric resonance region, potentially removing the optimal operating point. Balance damping against the desired regime width.

8. **Chaotic benchmark sensitivity:** Mackey-Glass with different τ values has varying predictability; ensure consistent benchmark parameters when comparing across studies.

## References

- Mahadev Sunil Kumar and Adarsh Ganesan, "Neuromorphic Computing Based on Parametrically-Driven Oscillators and Frequency Combs," arXiv:2604.21861v1, April 2026. [https://arxiv.org/abs/2604.21861](https://arxiv.org/abs/2604.21861)

- Related work on physical reservoir computing:
  - Tanaka et al., "Recent advances in physical reservoir computing: A review," Neural Networks, 2019.
  - Nakane et al., "Reservoir computing with spin waves in a garnet film," 2023.

- Related work on parametric oscillators for computing:
  - Dykman et al., "Fluctuating nonlinear oscillators: From nanomechanics to quantum superconducting circuits," 2012.
  - Kenig et al., "Parametric excitation of a micromechanical oscillator," 2012.

- Benchmark systems:
  - Mackey-Glass: Mackey and Glass, "Oscillation and chaos in physiological control systems," Science, 1977.
  - Lorenz system: Lorenz, "Deterministic nonperiodic flow," J. Atmos. Sci., 1963.
  - Rössler system: Rössler, "An equation for continuous chaos," Physics Letters A, 1976.
