---
name: fc-guided-band-selection-mi-bci
description: "Functional connectivity-guided spectral band selection for motor imagery BCI. Uses phase-based connectivity (wPLI, PLV, PLI) to identify optimal EEG frequency bands for CSP-based decoding instead of heuristic filter banks. Activation: BCI band selection, motor imagery, functional connectivity CSP, FC-guided BCI, spectral band optimization, EEG feature selection."
---

# FC-Guided Band Selection for Motor Imagery BCI

> Uses static functional connectivity to select optimal spectral bands for MI-BCI decoding, replacing heuristic filter bank designs with a principled, physiologically-informed approach.

## Metadata
- **Source**: arXiv:2605.00746
- **Authors**: Natália Araújo do Carmo, Aarthy Nagarajan
- **Published**: 2026-05-01

## Core Methodology

### Problem
CSP (Common Spatial Pattern) performance in MI-BCI depends critically on the spectral range of input EEG. Filter Bank CSP (FBCSP) uses predefined frequency sub-bands rather than subject-specific physiological criteria.

### Solution: FC-Guided Band Selection

1. **Compute Phase-Based Connectivity**: Calculate connectivity across sensorimotor channels using:
   - **wPLI** (weighted Phase Lag Index): mitigates volume conduction artifacts
   - **PLV** (Phase Locking Value): most aggressive for dimensionality reduction
   - **PLI** (Phase Lag Index): basic phase consistency measure

2. **Define Filter Bank**: Create 9-band filter bank spanning 4-40 Hz

3. **Rank Bands by Effect Size**: Calculate hemispheric coupling differences per band, rank by effect size

4. **Prune to Top-K**: Select top K bands for CSP feature extraction

5. **Classify**: Use FBCSP pipeline + Support Vector Regressor

### Key Findings
- **PLV** enables most aggressive dimensionality reduction (prioritizes μ and low-β ranges)
- **wPLI** demonstrates superior inter-session robustness (mitigates volume conduction)
- FC-guided selection can reduce required CSP fits by 22.2% to 77.8% while maintaining accuracy within 2% equivalence zone
- Outperforms random band ablation consistently

## Implementation Guide

### Prerequisites
- EEG data with sensorimotor channels
- CSP/FBCSP implementation
- Phase connectivity computation (wPLI, PLV, PLI)

### Step-by-Step

1. **Preprocess EEG**: Band-pass filter to 4-40 Hz, extract sensorimotor channels (C3, C4, Cz, etc.)

2. **Compute Connectivity Matrix**: For each frequency band, compute pairwise phase connectivity between hemispheric channel pairs

3. **Calculate Effect Size**: For each band, compute Cohen's d of hemispheric coupling differences between motor imagery classes

4. **Rank and Select**: Sort bands by effect size, select top-K bands

5. **Apply CSP**: Run CSP on selected bands only

6. **Classify**: Train SVM on CSP features

### Pseudocode
```python
# For each band b in filter_bands (4-40 Hz, 9 bands):
#   1. Band-pass filter EEG to band b
#   2. Compute wPLI/PLV/PLI between sensorimotor channels
#   3. Calculate hemispheric coupling difference (left vs right)
#   4. Compute effect size (Cohen's d) per class
# Rank bands by effect size
# Select top-K bands
# Run FBCSP on selected bands only
# Classify with SVM
```

## Applications
- Motor imagery BCI decoding optimization
- Subject-specific EEG band selection
- Reducing CSP computational overhead
- Interpretable feature selection for BCI

## Pitfalls
- Requires sufficient trial data for reliable connectivity estimation
- Effect size thresholds may vary across datasets
- wPLI is more computationally expensive than PLV
- Proof-of-concept only (validated on BCI Competition IV-2a and OpenBMI)

## Related Skills
- eeg-brain-connectivity-bci
- bci-rehabilitation-protocols
- copilot-assisted-second-thought-bci
- eeg-ieeg-bridge-bci
- hermes-brain-connectivity