---
name: quantum-spectral-anomaly-detection
category: quantum-machine-learning
description: QSPADE methodology for computing PCA-like anomaly scores from quantum state spectra using temperature-controlled thresholds.
trigger_words: ["QSPADE", "quantum anomaly detection", "spectral anomaly", "quantum PCA", "temperature-controlled threshold", "anomaly score", "quantum kernel"]
---

# Quantum Spectral Anomaly Detection (QSPADE)

Methodology from arXiv:2607.05307 (Yuan et al., Jul 2026).

## Problem

Classical PCA computes anomaly scores by evaluating test samples relative to the subspace spanned by leading eigenvectors. For quantum data, explicitly recovering principal eigenvectors, constructing full Gram matrices, or loading QRAM-style data can be more costly than estimating the anomaly score itself.

## Solution: QSPADE

Computes PCA-like anomaly scores directly from the spectrum of the average state of the normal dataset, avoiding explicit eigenvector recovery.

### Core Innovation

- **Temperature-Controlled Spectral Threshold**: Replaces hard PCA rank selection with smooth, temperature-controlled spectral threshold
- Near-threshold spectral components contribute partially to the anomaly score
- Score varies continuously (no jumps at cutoff boundaries)
- Less sensitive to noise or arbitrary hard cutoffs
- Zero-temperature limit recovers hard-projector PCA score

### Key Properties

- Measurement-based quantum detector
- Sample complexity independent of data dimension
- Behaves like kernel-PCA on encoded classical data
- Detects phase transitions (e.g., transverse-field Ising) without predefined order parameters

### Application

Use when:
- Performing anomaly detection on quantum-native systems
- Monitoring quantum systems where diagnostic observables are unknown
- Implementing quantum-kernel anomaly detection on encoded classical data
- Avoiding expensive eigenvector recovery or QRAM data loading

### Implementation Pattern

```
Normal Dataset → Average State ρ → Spectral Decomposition →
  Temperature-Controlled Threshold →
  Smooth Anomaly Score (continuous, no hard cutoffs)
```

### Comparison with Classical PCA

| Feature | Classical PCA | QSPADE |
|---------|--------------|--------|
| Eigenvector recovery | Required | Not needed |
| Gram matrix | Full construction | Avoided |
| Threshold | Hard cutoff | Temperature-smoothed |
| Sample complexity | O(d) | O(1) independent of d |
| Continuity | Discontinuous at cutoff | Continuous |
