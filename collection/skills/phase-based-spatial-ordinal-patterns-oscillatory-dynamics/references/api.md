# Phase-Based Spatial Ordinal Patterns Reference

## Original Paper
- **Title**: Phase-based spatial ordinal patterns for characterizing oscillatory dynamics
- **Authors**: Robison J. Santos-Silva, Bruno R. R. Boaretto, Thiago L. Prado, Roberto C. Budzinski
- **arXiv**: [2608.17196](https://arxiv.org/abs/2608.17196)
- **Published**: 2026-08-17
- **Categories**: nlin.AO, q-bio.NC

## Key Equations and Algorithms

### Spatial Ordinal Pattern Construction
For a system with N oscillators and phase values φ_i(t):
1. For each oscillator i at time t
2. Compare φ_i(t) with neighboring phases φ_j(t) for j ∈ neighbors(i)
3. Encode the ordering relation as a symbolic pattern
4. Handle near-equal phases (|φ_i - φ_j| < ε) with special categories

### Spatial Permutation Entropy
H_spatial(t) = -Σ p(π_k, t) log p(π_k, t)
where π_k are the spatial ordinal patterns and p(π_k, t) is their probability at time t.

## Implementation Considerations

### Phase Extraction Methods
- Hilbert transform for narrowband signals
- Wavelet transform for multiband signals  
- Instantaneous frequency methods for non-stationary signals

### Parameter Selection
- Neighborhood size: typically 1-2 hops in network topology
- Near-equal phase tolerance ε: calibrate based on signal noise level
- Sliding window size for entropy calculation: balance temporal resolution vs stability

## Validation Examples from Paper

### Synthetic Networks
- Kuramoto oscillators with varying coupling strengths
- Random networks with different topologies
- Demonstrated ability to distinguish different synchronization regimes

### Human EEG Data
- Resting-state EEG from multiple subjects
- Showed subject-specific patterns within individuals
- Detected transient dynamics during resting state

## Related Methods

- Traditional permutation entropy (amplitude-based)
- Phase synchronization measures (PLV, PLI, WPLI)
- Symbolic dynamics for complex systems
- Ordinal pattern analysis in time series