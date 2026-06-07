---
name: psychosis-scaling-critical-regime
description: 精神病早期阶段脑动力学临界性scaling偏差研究方法论。结合重整化群(RG)框架与多种scaling分析方法，揭示精神病中的临界性重组而非丢失。
version: 1.0.0
author: Irem Topal et al.
arxiv_id: 2606.06290
date: 2026-06-04
categories: [neuroscience, criticality, psychiatry, brain-dynamics]
tags: [criticality, psychosis, renormalization-group, DFA, PSD, scaling-law, fMRI]
activation_keywords: [criticality, psychosis, renormalization, scaling, brain dynamics, psychiatric disorder, DFA, PSD, fMRI]
---

# Psychosis Scaling Deviations in Critical Regime

## Overview

Methodology for detecting early psychosis through deviations in scaling behaviour within a preserved critical regime. Combines phenomenological renormalization group (PRG) with power spectral density (PSD) and detrended fluctuation analysis (DFA).

**Paper**: arXiv:2606.06290 (2026-06-04)
**Authors**: Irem Topal, Paola Moreno Ancalmo, Guillermo Montana Valverde, Philipp Homan, Wolfram Hinzen

## Core Innovation

### Theoretical Framework
- **Critical brain hypothesis**: Large-scale brain activity operates near-critical regime
- **Scale-invariant dynamics**: Long-range correlations, efficient information processing
- **Psychiatric disorder perspective**: Not simple loss of criticality, but **reorganization within preserved scaling regime**

### Key Discovery
Previous findings were **fragmented across observables and modalities**. This paper provides **unified framework** showing:
- Different scaling measures capture **common alteration**
- Early psychosis shows **systematic shifts** in scaling exponents
- Preserves overall phenomenology of scale-invariant organization

## Methodology

### Step 1: Phenomenological Renormalization Group (PRG)

```
PRG Framework:
- Coarse-graining approach for collective dynamics
- Track observables across spatial scales
- Identify scale-invariant properties
- Detect scaling exponent shifts
```

**Implementation**:
1. Divide brain into progressively larger regions
2. Compute coarse-grained observables at each scale
3. Analyze scaling relationships
4. Compare scaling exponents between groups

### Step 2: Power Spectral Density (PSD) Analysis

```
PSD Scaling:
S(f) ~ f^(-β)

Parameters:
- β: PSD scaling exponent
- f: Frequency
- S(f): Power spectral density

Healthy: β ~ 1 (pink noise/critical)
Psychosis: Systematic shifts in β
```

### Step 3: Detrended Fluctuation Analysis (DFA)

```
DFA Scaling:
F(n) ~ n^α

Parameters:
- α: DFA scaling exponent
- n: Window size
- F(n): Fluctuation function

Critical: α ~ 1 (long-range correlations)
Psychosis: Shifts in α across observables
```

### Step 4: Combined Analysis Framework

```
Integration:
1. Apply PRG to fMRI data → coarse-grained dynamics
2. Calculate PSD scaling at each scale → β(s)
3. Calculate DFA scaling at each scale → α(s)
4. Compare scaling exponent trajectories:
   - Healthy controls: Consistent critical-like values
   - Psychosis: Systematic shifts across scales
```

## Key Results

### Healthy Controls
- **Non-trivial scaling behavior** consistent with critical-like organization
- **Scale-invariant phenomenology** preserved across observables
- **Consistent scaling exponents**: β ~ 1, α ~ 1

### Early Psychosis
- **Same overall phenomenology**: Scale-invariant organization preserved
- **Systematic exponent shifts**: Multiple observables show coordinated deviations
- **Reorganization, not loss**: Critical regime maintained but altered

### Methodological Advances
- **Unified framework**: Coarse-graining + temporal scaling = principled approach
- **Multi-observable consistency**: Different measures capture same alteration
- **Scale-specific deviations**: Exponent shifts vary across scales

## Implementation Details

### Dataset
- **Modality**: Resting-state fMRI
- **Population**: Early psychosis patients + healthy controls
- **Analysis**: Multi-scale coarse-graining

### Analysis Pipeline
```
Python/R Implementation:
1. Preprocess fMRI (standard pipeline)
2. Apply PRG coarse-graining:
   - Define spatial scales (s1, s2, ..., sn)
   - Aggregate voxels into regions
   - Compute mean activity per region
3. Calculate PSD at each scale:
   - FFT on coarse-grained time series
   - Estimate β via linear regression
4. Calculate DFA at each scale:
   - Detrend windows
   - Estimate α via regression
5. Compare exponent distributions:
   - Statistical tests (t-tests, permutation)
   - Effect size calculations
```

### Statistical Framework
```
Exponent Comparison:
- Distribution tests: KS test, Mann-Whitney U
- Effect sizes: Cohen's d
- Multiple scales: ANOVA or mixed models
- Corrections: Bonferroni/FDR
```

## Practical Applications

### Clinical Use Cases
1. **Early psychosis detection**: Scaling exponent shifts as biomarkers
2. **Disease progression monitoring**: Track exponent changes over time
3. **Treatment response**: Assess if scaling recovers toward healthy values
4. **Risk stratification**: Identify individuals with criticality deviations

### Research Applications
1. **Multi-modal validation**: Extend to EEG, MEG, iEEG
2. **Cross-disorder comparison**: Apply to depression, schizophrenia, ADHD
3. **Computational modeling**: Simulate criticality shifts
4. **Mechanistic studies**: Link to neurotransmitter systems

## Limitations & Future Work

### Current Limitations
- Requires resting-state fMRI (may not apply to task data)
- Small sample sizes in psychiatric studies
- Cross-site scanner variability
- Interpretation of exponent shifts unclear

### Future Directions
- **Task-based fMRI**: Extend to cognitive tasks
- **Other disorders**: Depression, anxiety, neurodevelopmental
- **Longitudinal studies**: Track scaling changes over time
- **Mechanistic links**: Connect to dopamine/glutamate systems
- **Clinical trials**: Test if treatment normalizes scaling

## Related Work

### Critical Brain Dynamics
- Scale-invariant brain activity
- Near-critical regime operation
- Long-range temporal correlations
- Efficient information processing

### Psychiatric Biomarkers
- fMRI-based disorder detection
- Dynamic functional connectivity
- Network topology alterations
- Temporal pattern analysis

## Theoretical Significance

### Criticality Theory
This paper advances criticality theory in neuroscience:
1. **Reorganization vs loss**: Psychiatric disorders alter, not destroy criticality
2. **Preserved phenomenology**: Overall structure maintained
3. **Exponent shifts**: Systematic, coordinated deviations
4. **Unified framework**: PRG + scaling = comprehensive approach

### Scaling Laws
- **Power-law behavior**: S(f) ~ f^(-β), F(n) ~ n^α
- **Critical exponents**: β ~ 1, α ~ 1
- **Shift patterns**: Psychosis alters exponents systematically
- **Multi-scale consistency**: Same shifts across observables

## Code & Resources

- **Paper**: https://arxiv.org/abs/2606.06290
- **Pages**: 26 pages, 10 figures
- **Categories**: q-bio.NC, cond-mat.stat-mech
- **Keywords**: criticality, psychosis, renormalization, scaling

## Citation

```bibtex
@article{topal2026psychosis,
  title={Early psychosis shows deviations in scaling behaviour within a critical regime},
  author={Topal, Irem and Ancalmo, Paola Moreno and Valverde, Guillermo Montana and Homan, Philipp and Hinzen, Wolfram},
  journal={arXiv preprint arXiv:2606.06290},
  year={2026}
}
```

## Key Takeaways

1. **Criticality reorganization**: Psychosis alters criticality, doesn't destroy it
2. **Unified framework**: PRG + PSD + DFA = comprehensive scaling analysis
3. **Systematic shifts**: Coordinated exponent deviations across observables
4. **Preserved phenomenology**: Overall scale-invariant structure maintained
5. **Clinical potential**: Scaling exponents as psychiatric biomarkers