---
name: psychosis-scaling-critical-regime
description: "Phenomenological renormalization group (PRG) framework reveals early psychosis preserves critical regime but shows systematic scaling exponent shifts. Reorganization rather than loss of criticality — PRG + PSD + DFA combined analysis methodology."
---

## Context

Large-scale brain activity exhibits scale-invariant dynamics consistent with near-critical operation. Early psychosis shows systematic scaling exponent deviations across observables, but NOT a loss of criticality — rather a **reorganization of collective dynamics within a preserved scaling regime**.

**Key Finding**: Combining coarse-graining (PRG) with temporal scaling (PSD + DFA) provides principled framework for studying psychiatric disorders at the collective dynamics level.

**arXiv**: 2606.06290v1 (2026-06-04)
**Categories**: q-bio.NC, cond-mat.stat-mech

## Core Methodology

1. **Phenomenological Renormalization Group (PRG)**:
   - Coarse-graining approach to characterize collective dynamics across scales
   - Identify scaling exponents by analyzing how observables transform under scale reduction
   - Preserve scale-invariant organization → reveal exponent shifts rather than regime transitions

2. **Power Spectral Density (PSD) Analysis**:
   - Compute frequency-domain scaling: P(f) ~ f^(-β)
   - β exponent characterizes long-range temporal correlations
   - Healthy controls: non-trivial β consistent with critical-like dynamics
   - Early psychosis: systematic β shifts (increase or decrease depending on observable)

3. **Detrended Fluctuation Analysis (DFA)**:
   - Time-domain scaling: F(n) ~ n^α
   - α exponent measures self-similarity and persistence
   - Compare healthy vs. psychosis α values across brain regions

4. **Combined Framework**:
   - PRG: coarse-graining → identify collective dynamics regime
   - PSD: frequency scaling → long-range correlations
   - DFA: time scaling → self-similarity
   - **Synergy**: Different observables capture complementary aspects of same underlying reorganization

5. **Observable-Level Analysis**:
   - Systematic exponent shifts across multiple observables (not just one)
   - Same phenomenology (scale-invariant organization preserved)
   - Different quantitative values (exponents altered)
   - **Conclusion**: reorganization, not collapse

## Implementation Steps

### Step 1: Load Resting-State fMRI Data
```python
# Early psychosis patients + healthy controls
fmri_data = load_resting_state_fmri(subject_ids)
groups = {'healthy': healthy_ids, 'psychosis': psychosis_ids}
```

### Step 2: Phenomenological Renormalization Group
```python
def prg_coarse_graining(signal, scale_factors):
    """
    Apply PRG coarse-graining at multiple scales.
    
    Args:
        signal: fMRI time series
        scale_factors: List of coarse-graining scales
    
    Returns:
        coarse_grained: Signal at different scales
        scaling_exponents: Derived from observable transformations
    """
    coarse_grained = []
    for scale in scale_factors:
        averaged = moving_average(signal, window=scale)
        coarse_grained.append(averaged)
    
    # Compute scaling exponents from observable transformations
    exponents = compute_prg_exponents(coarse_grained)
    return coarse_grained, exponents
```

### Step 3: Power Spectral Density
```python
def compute_psd_scaling(fmri_signal):
    """
    Compute PSD scaling exponent β.
    
    Args:
        fmri_signal: BOLD time series
    
    Returns:
        beta: Scaling exponent P(f) ~ f^(-β)
    """
    freqs, psd = scipy.signal.welch(fmri_signal, fs=TR)
    
    # Fit power law in log-log space
    log_freq = np.log(freqs[1:])  # Skip DC
    log_psd = np.log(psd[1:])
    
    beta, _ = np.polyfit(log_freq, log_psd, deg=1)
    return -beta  # PSD ~ f^(-β), so exponent is -slope
```

### Step 4: Detrended Fluctuation Analysis
```python
def compute_dfa_scaling(fmri_signal, window_sizes):
    """
    Compute DFA scaling exponent α.
    
    Args:
        fmri_signal: BOLD time series
        window_sizes: List of fluctuation window sizes
    
    Returns:
        alpha: Scaling exponent F(n) ~ n^α
    """
    # Cumulative sum with detrending
    integrated = np.cumsum(fmri_signal - np.mean(fmri_signal))
    
    fluctuations = []
    for n in window_sizes:
        # Split into windows of size n
        segments = split_into_segments(integrated, n)
        
        # Detrend each segment
        detrended = [detrend_linear(seg) for seg in segments]
        
        # Compute RMS fluctuation
        f_n = np.sqrt(np.mean([np.var(d) for d in detrended]))
        fluctuations.append(f_n)
    
    # Fit power law: F(n) ~ n^α
    log_n = np.log(window_sizes)
    log_f = np.log(fluctuations)
    alpha, _ = np.polyfit(log_n, log_f, deg=1)
    
    return alpha
```

### Step 5: Group Comparison and Statistical Analysis
```python
def compare_scaling_exponents(healthy_data, psychosis_data):
    """
    Compare scaling exponents between groups.
    
    Args:
        healthy_data: Exponents from healthy controls
        psychosis_data: Exponents from early psychosis
    
    Returns:
        shifts: Systematic exponent differences
        statistics: Statistical test results
    """
    # Per-region comparison
    shifts = {}
    for roi in ROIS:
        healthy_exp = healthy_data[roi]
        psychosis_exp = psychosis_data[roi]
        
        # Statistical test
        statistic, p_value = mannwhitneyu(healthy_exp, psychosis_exp)
        shifts[roi] = {
            'mean_shift': np.mean(psychosis_exp) - np.mean(healthy_exp),
            'p_value': p_value,
            'effect_size': cohens_d(healthy_exp, psychosis_exp)
        }
    
    return shifts
```

## Key Results

- **Preserved Scale-Invariant Organization**: Both groups show non-trivial scaling (critical-like phenomenology intact)
- **Systematic Exponent Shifts**: Multiple observables show consistent direction of change
- **Reorganization Hypothesis**: Critical regime NOT lost, but collective dynamics reorganized
- **Complementary Observables**: PRG, PSD, DFA capture different aspects of same underlying shift

## Pitfalls

1. **Observable Fragmentation**: Previous studies reported altered measures but across different observables/modalities → unclear if capturing common alteration. **Fix**: Use combined PRG+PSD+DFA framework for unified characterization.

2. **Single-Observable Interpretation**: Finding exponent shift in one observable ≠ regime transition. Must check: (a) other observables, (b) overall phenomenology preserved? → **Conclusion**: reorganization, not collapse.

3. **Scale Range Sensitivity**: Exponents may vary across different scale ranges (high vs. low frequencies). Report exponents with explicit scale range specification.

4. **Subject Heterogeneity**: Early psychosis is heterogeneous condition. Stratify by symptom severity or clinical stage for finer-grained analysis.

5. **Temporal Resolution Limits**: fMRI TR ~ 1-2s limits maximum frequency observable. Cannot probe ultra-fast dynamics (gamma band) with fMRI alone.

## Verification

- PRG coarse-graining curves (observable vs. scale)
- PSD power-law fits in log-log space
- DFA fluctuation curves F(n) vs. n
- Group comparison: exponent shifts with effect sizes and p-values
- Preserved phenomenology check: both groups show scale-invariant organization

## Activation

psychosis, scaling behavior, critical regime, renormalization group, PRG, PSD, DFA, fMRI, resting-state, critical dynamics, scaling exponents, collective dynamics, psychiatric disorders, phenomenological coarse-graining, exponent shifts, scale-invariant organization, brain dynamics reorganization