---
name: antisymmetric-polyspectral-neural-interactions
description: Generalized framework of antisymmetric cross-polyspectral indices for identifying high-order neural interactions in M/EEG and other neural data. Extends pairwise connectivity analysis to capture complex multi-node relationships. Use when analyzing higher-order brain connectivity, polyspectral analysis, cross-bispectrum, cross-trispectrum, neural phase coupling, or multi-node interactions beyond pairwise connections.
---

# Antisymmetric Polyspectral Indices for Neural Interactions

Based on: *Basti, Hindriks, Freddi, Romani, Pizzella, Nolte, Marzetti (2026)* — arXiv:2605.04636

## Overview

This paper introduces a **generalized framework of antisymmetric polyspectral indices** for detecting high-order (3-way, 4-way+) neural interactions that go beyond traditional pairwise connectivity measures.

## Core Theory

### Why Higher-Order Interactions Matter

Traditional connectivity analysis (coherence, phase-locking) only captures **pairwise** relationships. But brain function involves **multi-node coordination**:
- Three regions co-activating in a specific phase relationship
- Nonlinear interactions requiring 3+ nodes to describe
- Synergistic effects not decomposable into pairs

### Antisymmetric Cross-Polyspectral Framework

The framework generalizes spectral connectivity to higher orders:

```
B(f1, f2) = E[X(f1) · X(f2) · X*(f1+f2)]     # Cross-bispectrum (3-way)
T(f1,f2,f3) = E[X(f1)·X(f2)·X(f3)·X*(f1+f2+f3)]  # Cross-trispectrum (4-way)
```

Key innovation: **antisymmetric indices** that are robust to volume conduction and detect genuine multi-node coupling.

### Properties

| Property | Pairwise | Higher-Order |
|----------|----------|-------------|
| Detects nonlinear coupling | ✗ | ✓ |
| Volume conduction robust | Partially | ✓ (antisymmetric) |
| Captures synergy | ✗ | ✓ |
| Directionality info | Limited | Enhanced |

## Estimation Pipeline

### 1. Preprocessing
- Multivariate neural time series (EEG/MEG/LFP)
- Artifact removal, filtering
- Epoch segmentation if task-related

### 2. Spectral Estimation
```python
from scipy.signal import welch, csd

def estimate_cross_bispectrum(signals, fs, nperseg=256):
    """
    Estimate cross-bispectrum between neural signals.
    
    Args:
        signals: N x T array (N channels, T timepoints)
        fs: Sampling frequency
        nperseg: Segment length for Welch's method
    
    Returns:
        bispectrum: Complex cross-bispectrum estimates
    """
    # 1. Segment data with overlap
    # 2. Compute FFT for each segment
    # 3. B(f1,f2) = mean(X_i(f1) * X_i(f2) * conj(X_i(f1+f2)))
    # 4. Antisymmetric component extraction
    pass
```

### 3. Antisymmetric Index Computation
- Extract antisymmetric component of polyspectrum
- Normalize by power spectra for interpretability
- Statistical testing via surrogate data (phase randomization)

### 4. Network Construction
- Build hypergraph where hyperedges represent significant multi-node interactions
- Compare with pairwise graph to identify synergistic connections

## Statistical Validation

### Surrogate Testing
```python
def phase_randomize_surrogate(signals, n_surrogates=100):
    """Generate surrogates preserving power spectrum but destroying phase coupling."""
    fft_data = np.fft.fft(signals, axis=-1)
    phases = np.random.uniform(0, 2*np.pi, fft_data.shape)
    surrogate_fft = np.abs(fft_data) * np.exp(1j * phases)
    return np.fft.ifft(surrogate_fft, axis=-1).real
```

### Multiple Comparison Correction
- FDR correction across frequency bins and node combinations
- Cluster-based permutation testing for spatio-temporal data

## Applications

| Application | Index Used | What It Reveals |
|-------------|-----------|----------------|
| Cross-frequency coupling | Cross-bispectrum | Phase-amplitude coupling |
| Multi-region coordination | Cross-trispectrum | 4-node synergistic networks |
| Directional coupling | Asymmetric bicoherence | Information flow direction |
| Network synergies | Hypergraph analysis | Beyond-pairwise organization |

## Comparison with Existing Methods

| Method | Order | Nonlinear | Robust to Volume Conduction |
|--------|-------|-----------|---------------------------|
| Coherence | 2nd | ✗ | ✗ |
| Phase-Locking Value | 2nd | Partially | ✗ |
| Imaginary Coherence | 2nd | Partially | ✓ |
| **Antisymmetric Bispectrum** | **3rd** | **✓** | **✓** |
| **Antisymmetric Trispectrum** | **4th** | **✓** | **✓** |

## References

- [arXiv:2605.04636](https://arxiv.org/abs/2605.04636) — Full paper
- Related: `higher-order-brain-networks`, `brain-connectivity-analysis`

## Activation Keywords

`polyspectral`, `bispectrum`, `trispectrum`, `higher-order connectivity`, `cross-bispectrum`, `neural interactions`, `multi-node coupling`, `antisymmetric index`, `hypergraph brain`, `synergistic connectivity`
