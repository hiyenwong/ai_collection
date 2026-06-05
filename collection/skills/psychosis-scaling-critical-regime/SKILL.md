---
name: psychosis-scaling-critical-regime
description: "Renormalization group framework for early psychosis brain dynamics analysis. Phenomenological renormalization group (PRG) + PSD + DFA characterize collective dynamics across scales. Systematic scaling exponent shifts indicate reorganization within preserved critical regime. Activation: psychosis, criticality, renormalization group, scaling, brain dynamics, collective organization, early psychosis, statistical mechanics."
metadata:
  arxiv_id: "2606.06290"
  published: "2026-06-04"
  authors: "Irem Topal, Paola Moreno Ancalmo, Guillermo Montana Valverde, Philipp Homan, Wolfram Hinzen"
  tags: [psychosis, criticality, renormalization-group, scaling, brain-dynamics, fMRI, statistical-mechanics, collective-dynamics]
license: Complete terms in LICENSE.txt
---

# Early Psychosis Scaling Behaviour Within Critical Regime

## Context

Large-scale brain activity exhibits scale-invariant dynamics consistent with near-critical operation. This paper investigates scaling properties in early psychosis using phenomenological renormalization group (PRG) framework combined with power spectral density (PSD) and detrended fluctuation analysis (DFA).

## Core Methodology

### 1. Phenomenological Renormalization Group (PRG) Framework

**Principle**: Coarse-grain brain activity across scales to extract scaling exponents.

**Implementation**:
```python
def phenomenological_renormalization(fmri_signal, scales):
    """
    Apply PRG coarse-graining to extract scaling exponents.
    
    Args:
        fmri_signal: Resting-state fMRI time series
        scales: List of coarse-graining scales (e.g., [2, 4, 8, 16])
    
    Returns:
        Scaling exponents for collective dynamics
    """
    coarse_signals = []
    for scale in scales:
        # Block averaging coarse-graining
        coarse = block_average(fmri_signal, scale)
        coarse_signals.append(coarse)
    
    # Extract scaling exponents via linear fit
    exponents = fit_scaling_exponents(coarse_signals, scales)
    return exponents
```

### 2. Multi-Observable Analysis

**Three complementary approaches**:

1. **Power Spectral Density (PSD)**: Frequency-domain scaling
   - $S(f) \sim f^{-\beta}$ where $\beta$ characterizes temporal correlations
   
2. **Detrended Fluctuation Analysis (DFA)**: Time-domain scaling
   - $F(n) \sim n^{\alpha}$ where $\alpha$ measures self-similarity
   
3. **PRG coarse-graining**: Scale-space organization
   - $A(\ell) \sim \ell^{-\gamma}$ where $\gamma$ captures collective dynamics

### 3. Scaling Exponent Comparison

**Key finding**: Early psychosis shows **systematic shifts** in scaling exponents, not loss of critical dynamics.

| Observable | Healthy Controls | Early Psychosis | Interpretation |
|------------|-----------------|-----------------|----------------|
| PSD $\beta$ | Critical-like | Shifted | Temporal correlation change |
| DFA $\alpha$ | Near-critical | Deviated | Self-similarity alteration |
| PRG $\gamma$ | Scale-invariant | Modified | Collective reorganization |

## Implementation Steps

### Step 1: Preprocess fMRI Data

- Resting-state fMRI preprocessing (motion correction, spatial normalization)
- Extract regional time series (e.g., ROI-based, whole-brain)
- Detrending and normalization

### Step 2: Apply PRG Coarse-Graining

```python
def block_average(signal, scale):
    """Coarse-grain signal by block averaging."""
    n_blocks = len(signal) // scale
    coarse = np.zeros(n_blocks)
    for i in range(n_blocks):
        coarse[i] = np.mean(signal[i*scale:(i+1)*scale])
    return coarse
```

### Step 3: Compute PSD Scaling

```python
def power_spectral_scaling(signal, freq_range):
    """Extract PSD scaling exponent."""
    freqs, psd = welch(signal, fs=1.0)
    valid_freqs = freqs[freq_range[0] < freqs < freq_range[1]]
    valid_psd = psd[freq_range[0] < freqs < freq_range[1]]
    log_freq = np.log(valid_freqs)
    log_psd = np.log(valid_psd)
    beta = -np.polyfit(log_freq, log_psd, 1)[0]
    return beta
```

### Step 4: Compute DFA Scaling

```python
def detrended_fluctuation_analysis(signal, window_sizes):
    """Compute DFA scaling exponent."""
    fluctuations = []
    for n in window_sizes:
        # Divide signal into windows of size n
        windows = [signal[i:i+n] for i in range(0, len(signal), n)]
        # Detrend each window
        detrended = [detrend(w) for w in windows]
        # Compute fluctuation
        f = np.sqrt(np.mean([np.var(d) for d in detrended]))
        fluctuations.append(f)
    # Fit scaling exponent
    log_n = np.log(window_sizes)
    log_f = np.log(fluctuations)
    alpha = np.polyfit(log_n, log_f, 1)[0]
    return alpha
```

### Step 5: Compare Scaling Exponents

- Compute scaling exponents for healthy controls and psychosis groups
- Statistical comparison (t-tests, effect sizes)
- Interpret shifts within critical framework

## Key Results

**Main finding**: Early psychosis is characterized by **reorganization of collective dynamics within a preserved scaling regime**, not simple loss of criticality.

**Evidence**:
1. Both groups show scale-invariant organization
2. Systematic shifts in all three observables (PSD, DFA, PRG)
3. Consistent phenomenology but altered scaling exponents

**Implications**:
- Critical-like dynamics are preserved in early psychosis
- Scaling regime is reorganized rather than destroyed
- PRG + temporal scaling provides principled framework

## Pitfalls

- **Fragmented measures**: Previous findings across isolated observables are inconsistent. Use multi-observable PRG framework.
- **False criticality loss**: Simple deviation ≠ loss of critical dynamics. Check for preserved scaling regime.
- **Scale selection**: PRG scales must cover relevant dynamical range. Test multiple scales.
- **Group heterogeneity**: Early psychosis may have subgroups. Consider stratification.
- **Cross-modal comparison**: Different observables may capture different aspects. Combine PRG + PSD + DFA.

## Verification

**Validation steps**:
1. Confirm scale-invariant organization in both groups
2. Extract scaling exponents from all three observables
3. Statistical comparison with appropriate tests
4. Interpret shifts as reorganization, not loss

**Metrics**:
- Scaling exponent consistency across observables
- Statistical significance of shifts
- Effect sizes (Cohen's d)

## Activation Keywords

- psychosis scaling
- critical regime
- renormalization group
- phenomenological renormalization
- brain dynamics
- collective organization
- early psychosis
- statistical mechanics
- PSD scaling
- DFA
- scale-invariant
- 精神病临界性
- 重整化群

## References

- arXiv:2606.06290 - Original paper
- Critical brain dynamics literature
- Renormalization group in neuroscience
- Statistical mechanics of brain activity