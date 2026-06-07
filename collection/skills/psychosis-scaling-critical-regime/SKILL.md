---
name: psychosis-scaling-critical-regime
description: "Phenomenological Renormalization Group (PRG) framework for analyzing scaling behavior deviations in early psychosis brain dynamics. Combines PRG coarse-graining with Power Spectral Density (PSD) and Detrended Fluctuation Analysis (DFA) to characterize collective dynamics across scales. Use when studying brain criticality, psychiatric disorders, scale-invariant dynamics, or multi-modal scaling analysis."
metadata:
  arxiv_id: "2606.06290"
  published: "2026-06-04"
  authors: "Irem Topal, Paola Moreno Ancalmo, Guillermo Montana Valverde, Philipp Homan, Wolfram Hinzen"
  paper_title: "Early psychosis shows deviations in scaling behaviour within a critical regime"
  tags: [neuroscience, criticality, psychosis, scaling, PRG, brain dynamics, psychiatric disorders]
license: Complete terms in LICENSE.txt
---

# Psychosis Scaling in Critical Regime

## Context

Accumulating evidence suggests large-scale brain activity exhibits scale-invariant dynamics consistent with near-critical regime operation. This framework provides a principled multi-method approach for studying scaling behavior alterations in psychiatric disorders using resting-state fMRI.

## Core Methodology

### 1. Phenomenological Renormalization Group (PRG) Framework

**Purpose**: Characterize collective dynamics across spatial scales through coarse-graining.

**Implementation Steps**:
1. Load resting-state fMRI time series for each cortical region (68-region parcellation)
2. Apply coarse-graining at multiple scales (2, 4, 8, 16, 32 voxels)
3. For each scale $b$, compute block average: $X_b(t) = rac{1}{b} \sum_{i=1}^b X_i(t)$
4. Calculate correlation function $C_b(r) = \langle X_b(t) X_b(t+r) angle$
5. Extract scaling exponent $
u$ from correlation decay: $C_b(r) \sim r^{-
u}$
6. Track $
u$ evolution across scales to identify critical-like behavior

**Criticality Criterion**: 
- Non-trivial scaling ($
u 
eq 0$) indicates collective organization
- Scale-invariant $
u$ across coarse-graining levels suggests critical regime

### 2. Power Spectral Density (PSD) Analysis

**Purpose**: Capture temporal scaling in frequency domain.

**Implementation Steps**:
1. Compute PSD using Welch's method: $S(f) = |\mathcal{F}[X(t)]|^2$
2. Fit power-law: $S(f) \sim f^{-eta}$ in range $0.01-0.1$ Hz
3. Extract $eta$ exponent for each region and subject
4. Group comparison: $eta_{patients}$ vs $eta_{controls}$

**Interpretation**:
- $eta pprox 1$: 1/f noise (pink noise), critical-like
- $eta > 1$: slower dynamics, subcritical tendency
- $eta < 1$: faster fluctuations, supercritical tendency

### 3. Detrended Fluctuation Analysis (DFA)

**Purpose**: Measure long-range temporal correlations.

**Implementation Steps**:
1. Integrate time series: $Y(k) = \sum_{i=1}^k [X(i) - \langle X angle]$
2. Divide into windows of size $n$
3. Fit linear trend in each window, compute RMS fluctuation:
   $F(n) = \sqrt{rac{1}{N} \sum_{k=1}^N [Y(k) - Y_n(k)]^2}$
4. Fit scaling law: $F(n) \sim n^{lpha}$
5. Extract $lpha$ exponent across window sizes (4-64 time points)

**Interpretation**:
- $lpha = 0.5$: uncorrelated (white noise)
- $lpha pprox 1$: long-range correlations, critical-like
- $0.5 < lpha < 1$: persistent correlations

### 4. Multi-Observable Integration

**Key Finding**: Early psychosis shows systematic shifts in ALL three exponents:
- $
u$: altered spatial scaling (reduced collective organization)
- $eta$: shifted temporal scaling (faster PSD decay)
- $lpha$: modified DFA scaling (reduced long-range correlations)

**Critical Insight**: Not loss of criticality, but **reorganization within preserved scaling regime**.

## Workflow for Applying This Framework

**Input Requirements**:
- Resting-state fMRI data (at least 5 minutes, TR ≤ 2s)
- Cortical parcellation (68-region Desikan-Killiany or similar)
- Subject groups: patients vs controls

**Step-by-Step Execution**:

1. **Preprocessing**: Apply standard fMRI pipeline (motion correction, smoothing, normalization)

2. **Regional Extraction**: Extract mean BOLD signal for each cortical region

3. **PRG Coarse-Graining**: 
   ```python
   # Example implementation
   scales = [1, 2, 4, 8, 16, 32]
   for b in scales:
       coarse_signal = block_average(signal, block_size=b)
       corr_func = compute_correlation(coarse_signal)
       nu_b = fit_power_law(corr_func)
   ```

4. **PSD Analysis**:
   ```python
   freqs, psd = welch(signal, fs=1/TR, nperseg=128)
   beta = fit_power_law(freqs[low_freq_range], psd[low_freq_range])
   ```

5. **DFA Analysis**:
   ```python
   window_sizes = np.logspace(np.log2(4), np.log2(len(signal)/4), num=20)
   fluctuations = []
   for n in window_sizes:
       F_n = compute_fluctuation(signal, window=n)
       fluctuations.append(F_n)
   alpha = fit_power_law(window_sizes, fluctuations)
   ```

6. **Group Comparison**: Statistical tests (t-test, permutation) on exponents

7. **Cross-Observable Correlation**: Check if shifts in $
u, eta, lpha$ are correlated

## Pitfalls

**False Positive Criticality**: 
- Trivial scaling ($
u=0$, $eta=0$, $lpha=0.5$) ≠ critical dynamics
- Always verify non-trivial exponents before claiming criticality

**Methodological Confounds**:
- Head motion artifacts corrupt scaling estimates → apply scrubbing
- TR-dependent frequency resolution affects PSD → standardize acquisition
- Window size selection for DFA → use logarithmically spaced range

**Interpretation Trap**:
- Reduced scaling ≠ loss of criticality
- **Key insight**: scaling regime preserved, but exponents shifted (reorganization)

**Group Size Sensitivity**:
- Small N (<20 per group) → unreliable exponent estimates
- Permutation tests preferred over parametric for small samples

**Spatial vs Temporal Confounding**:
- PRG measures spatial coarse-graining, PSD/DFA temporal
- Interpret shifts separately before claiming unified alteration

## Verification

**Validation Checks**:
1. Confirm non-trivial scaling in controls: $
u > 0.2$, $eta \in [0.8, 1.2]$, $lpha \in [0.6, 1.0]$
2. Check exponent stability across scales: $
u$ should plateau if critical
3. Verify cross-subject consistency: exponents should cluster per group

**Expected Outcomes** (based on paper):
- Controls: scale-invariant dynamics with non-trivial exponents
- Patients: preserved scaling regime with systematic exponent shifts
- Cross-observable correlation: shifts in $
u, eta, lpha$ should co-vary

## Applications Beyond Psychosis

**Generalizable Framework**: Apply to any condition hypothesized to alter brain dynamics:
- Depression, anxiety disorders
- Neurodegenerative diseases (Alzheimer's, Parkinson's)
- Developmental disorders (autism, ADHD)
- Pharmacological interventions (drug effects on scaling)

**Extension Opportunities**:
- Combine with EEG/MEG for faster temporal scales
- Add network-based coarse-graining (topological PRG)
- Integrate with whole-brain modeling (Hopf Stuart-Landau)

## Activation Keywords

- psychosis scaling
- brain criticality psychiatric
- PRG renormalization brain
- PSD DFA analysis
- scale-invariant dynamics
- collective brain dynamics
- multi-modal scaling analysis
