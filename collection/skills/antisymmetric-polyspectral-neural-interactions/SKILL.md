---
name: antisymmetric-polyspectral-neural-interactions
description: >
  Generalized framework of antisymmetric cross-polyspectral indices for identifying
  high-order neural interactions. Quantifies harmonic dependencies among multiple
  frequency components (f_N = sum of f_i) while being intrinsically robust to
  instantaneous mixing and volume conduction. Enables personalized multi-site TMS
  protocols by monitoring multi-frequency network interactions. Activation:
  polyspectral analysis, cross-frequency coupling, high-order neural interactions,
  volume conduction robust, antispectral indices, EEG higher-order analysis,
  multi-frequency coupling, mTMS protocol design, bicoherence tricoherence.
---

# Antisymmetric Polyspectral Indices for High-Order Neural Interactions

**Paper**: arXiv:2605.04636 (2026-05-06)
**Authors**: Alessio Basti, Rikkert Hindriks, Ruggero Freddi, Gian Luca Romani, Vittorio Pizzella
**Categories**: q-bio.NC, stat.ME

## Core Contribution

Introduces a general family of antisymmetric cross-polyspectral indices that quantify
harmonic dependencies among N time series where frequency f_N arises from the
combination of N-1 components (f_N = Σ f_i), while being intrinsically robust to
instantaneous mixing (volume conduction).

## Problem Solved

Cross-frequency interactions are fundamental for integrating information across
temporal scales, but conventional metrics suffer from:
- Complex multi-frequency nonlinearities
- Spurious zero-lag artifacts from volume conduction
- Lack of robust framework for genuine N-way interactions

## Mathematical Framework

### Antisymmetric Cross-Polyspectral Index

For N time series with frequencies f_1, ..., f_{N-1} and f_N = Σ f_i:

- The index is antisymmetric under permutation of input frequencies
- This antisymmetry ensures robustness to instantaneous mixing
- Quantifies genuine non-linear coupling beyond pairwise interactions

### Key Properties

1. **Volume Conduction Robustness**: Antisymmetry intrinsically cancels
   zero-lag artifacts common in EEG/MEG
2. **N-Way Generalization**: Unified framework from bicoherence (N=3) to
   arbitrary-order polyspectra
3. **Theoretical Guarantees**: Derived theoretical properties validated
   through cubic nonlinearity simulations
4. **Empirical Validation**: Applied to real EEG recordings, revealing
   higher-order dependencies missed by standard methods

## Applications

1. **EEG Cross-Frequency Analysis**: Detect genuine phase-amplitude,
   phase-phase, and higher-order couplings
2. **MEG Source-Space Analysis**: Identify true neural interactions
   without source leakage artifacts
3. **Personalized mTMS**: Monitor and modulate specific multi-frequency
   network interactions for targeted stimulation
4. **Biomarker Discovery**: Higher-order interactions as disease biomarkers

## Computational Implementation

### Key Steps

1. Compute cross-polyspectrum for target frequency combinations
2. Apply antisymmetry operator to cancel instantaneous mixing
3. Normalize to obtain bounded index [-1, 1] or [0, 1]
4. Statistical significance testing against surrogate data

### Pseudocode

```python
def antisymmetric_polyspectral_index(signals, freq_bands):
    """
    signals: N time series (channels × time)
    freq_bands: list of frequency tuples (f1, f2, ..., fN) where fN = sum(fi)
    """
    # 1. Compute Fourier transforms
    spectra = fft(signals, axis=-1)
    
    # 2. Compute cross-polyspectrum for each frequency combination
    for freq_tuple in freq_bands:
        polyspectrum = compute_polyspectrum(spectra, freq_tuple)
        
    # 3. Apply antisymmetry: sum over permutations with alternating signs
    antisymmetric = apply_antisymmetry(polyspectrum)
    
    # 4. Normalize and return
    return normalize_index(antisymmetric)
```

## Comparison with Existing Methods

| Method | Order | Volume Conduction Robust | N-Way |
|--------|-------|-------------------------|-------|
| Coherence | 2 | No | No |
| Phase-Locking Value | 2 | No | No |
| Bicoherence | 3 | Partial | No |
| **Antisymmetric Index** | **N** | **Yes** | **Yes** |

## Testable Predictions

- Higher-order dependencies exist in resting-state EEG beyond pairwise coupling
- Antisymmetric indices reveal coupling patterns invisible to standard metrics
- Specific frequency triplets/quadruplets show task-dependent modulation
- mTMS protocols targeting identified couplings show enhanced efficacy

## Related Skills

- `hermes-brain-connectivity` - connectivity analysis tools
- `eeg-hopfield-emotion-energy` - EEG-based analysis
- `brain-stimulation-dynamics-state` - brain stimulation
- `swpc-directed-functional-connectivity` - directed connectivity
