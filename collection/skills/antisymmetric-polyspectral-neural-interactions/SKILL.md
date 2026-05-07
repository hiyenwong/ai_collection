---
name: antisymmetric-polyspectral-neural-interactions
description: >
  Generalized framework of antisymmetric cross-polyspectral indices for identifying
  high-order neural interactions in EEG/MEG data. Addresses cross-frequency coupling (CFC)
  detection while being intrinsically robust to volume conduction/instantaneous mixing.
  Use when: analyzing higher-order neural interactions (beyond pairwise), cross-frequency
  coupling (CFC), polyspectral analysis of EEG/MEG/MEG, multi-site TMS protocol design,
  volume-conduction-robust connectivity, or harmonic dependency quantification.
  Activation: polyspectral, cross-polyspectrum, antisymmetric index, higher-order interaction,
  cross-frequency coupling, CFC, volume conduction robust, mTMS, cubic nonlinearity,
  neural harmonic, 多频交互, 高阶交互, 交叉频率耦合
---

# Antisymmetric Polyspectral Indices for High-Order Neural Interactions

Based on: Basti et al. (2026), arXiv:2605.04636

## Problem

Conventional EEG/MEG connectivity measures (PLV, ImCoh, wPLI) assume same-frequency
interactions, treating frequency bands in isolation. They cannot detect **cross-frequency
coupling (CFC)** — where a frequency f₀ arises from n-1 components such that
f₀ = f₁ + f₂ + ... + fₙ₋₁. Additionally, volume conduction creates spurious zero-lag
artifacts that corrupt connectivity estimates.

## Solution: Antisymmetric Cross-Polyspectral Indices

A general family of indices that quantify n-th order harmonic dependencies while being
**intrinsically robust to instantaneous mixing** (volume conduction).

### Key Mathematical Principle

For n time series x₁, ..., xₙ, the cross-polyspectrum is the n-dimensional Fourier
transform of their n-th order cumulant. The antisymmetric index exploits the fact that
for real signals, the polyspectrum satisfies conjugate symmetry. The **antisymmetric part**
cancels out contributions from instantaneous linear mixing while preserving genuine
nonlinear phase couplings.

### General Form

```
P_n(f₁, f₂, ..., fₙ₋₁) = E[X₁(f₁) · X₂(f₂) · ... · Xₙ₋₁(fₙ₋₁) · Xₙ*(f₀)]
```
where f₀ = f₁ + f₂ + ... + fₙ₋₁ and * denotes complex conjugate.

The antisymmetric index:
```
A_n = P_n - P_n*(-f₁, -f₂, ..., -fₙ₋₁)
```

This eliminates zero-lag (volume conduction) contributions because for purely
instantaneously mixed signals, P_n = P_n*, making A_n = 0.

## When to Use

| Situation | Conventional Metric | This Method |
|-----------|-------------------|-------------|
| Same-frequency, no volume conduction | PLV, wPLI | Not needed |
| Same-frequency, with volume conduction | ImCoh, wPLI | Not needed |
| Cross-frequency, no volume conduction | PAC, CFS | Consider this |
| Cross-frequency, with volume conduction | **No robust metric exists** | **This method** ✓ |
| Higher-order (n≥3) interactions | **No standard method** | **This method** ✓ |

## Validation

- **Simulations**: Validated with cubic nonlinearities (n=4 case: f₀ = f₁ + f₂ + f₃)
- **Empirical EEG**: Applied to resting-state EEG recordings
- **Results**: Revealed significant higher-order dependencies undetectable by standard
  connectivity approaches (PLV, ImCoh, PAC)

## Clinical Application: Multi-site TMS (mTMS)

The indices enable personalized mTMS protocols:
1. Identify target multi-frequency network interactions from patient EEG
2. Design stimulation patterns using coil arrays at distinct frequencies (f₁, f₂, ...)
3. The overlap region receives combined drive at f₀ = f₁ + f₂ + ...
4. Monitor coupling strength using antisymmetric indices in real-time

## Implementation Notes

### Computation Pipeline

```python
import numpy as np
from scipy.signal import welch, csd

def compute_cross_polyspectrum(signals, fs, nperseg=256):
    """Compute cross-polyspectrum for n signals (n≥3).
    For n=3 (bispectrum): f0 = f1 + f2
    For n=4 (trispectrum): f0 = f1 + f2 + f3
    """
    # 1. Compute Fourier transforms (Welch's method)
    # 2. Form polyspectral products at each frequency tuple
    # 3. Average over segments
    # 4. Extract antisymmetric part
    pass

def antisymmetric_index(polyspectrum, freqs):
    """Compute antisymmetric polyspectral index.
    A(f1, f2, ...) = P(f1, f2, ...) - P*(-f1, -f2, ...)
    """
    # Conjugate symmetry cancellation
    pass
```

### Key Parameters
- **Order n**: Determines interaction complexity (n=3: bispectrum, n=4: trispectrum)
- **Frequency resolution**: Trade-off between spectral resolution and variance
- **Segment length**: Longer segments → better frequency resolution but fewer averages

### Pitfalls
- **Data length**: Higher-order polyspectra require significantly more data for stable estimates
- **Non-stationarity**: Assumes quasi-stationary segments; use sliding windows for dynamics
- **Interpretation**: Non-zero index indicates genuine nonlinear coupling, but directionality
  requires additional analysis (e.g., time-reversed surrogates)

## References

- Basti et al. (2026). "A Generalized Framework of Antisymmetric Polyspectral Indices
  for Identifying High-Order Neural Interactions." arXiv:2605.04636 [q-bio.NC].
- Nolte et al. (2004). Imaginary part of coherency for identifying brain interactions.
- Canolty et al. (2006). Phase-amplitude coupling in human ECoG.
- Hipp & Siegel (2015). Cortical spike-field coupling and CFC.
