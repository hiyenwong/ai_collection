---
name: fc-guided-band-selection-bci
description: Functional Connectivity-guided spectral band selection for Motor Imagery Brain-Computer Interfaces (MI-BCIs). Ranks frequency bands using phase-based connectivity (wPLI, PLV, PLI) across sensorimotor channels to identify subject-specific discriminative bands, reducing CSP pipeline dimensionality while maintaining classification accuracy.
author: Hermes Agent
version: 1.0.0
license: MIT
dependencies:
  - numpy>=1.21.0
  - scipy>=1.7.0
  - scikit-learn>=1.0.0
  - mne>=1.0.0
  - pyriemann>=0.5.0
  - matplotlib>=3.5.0
  - pandas>=1.3.0
triggers:
  - FC-guided band selection
  - functional connectivity BCI
  - MI-BCI spectral selection
  - wPLI PLV band selection
  - filter bank CSP band selection
  - phase connectivity motor imagery
  - subject-specific frequency bands
  - hemispheric coupling BCI
keywords:
  - brain-computer interface
  - motor imagery
  - functional connectivity
  - common spatial pattern
  - filter bank CSP
  - wPLI
  - PLV
  - PLI
  - band selection
  - phase locking
  - sensorimotor rhythms
  - spectral selection
  - BCI Competition IV-2a
  - OpenBMI
---

# FC-Guided Band Selection for Motor Imagery BCI

## Overview

This skill implements **Functional Connectivity (FC)-guided spectral band selection** for Motor Imagery Brain-Computer Interfaces (MI-BCIs), based on the methodology described in *"Functional Connectivity-Guided Band Selection for Motor Imagery Brain-Computer Interfaces"* (arXiv: 2605.00746, Araújo do Carmo & Nagarajan, 2026).

The core insight: rather than using predefined frequency sub-bands in Filter Bank CSP (FBCSP), this method identifies the most discriminative spectral bands by calculating **phase-based functional connectivity** across sensorimotor channels, ranking bands by the effect size of their hemispheric coupling differences, and pruning to the top-K bands for feature extraction and classification.

## Problem Statement

### CSP Performance Dependency on Spectral Range

The Common Spatial Pattern (CSP) algorithm is the cornerstone of MI-BCI decoding, but its performance depends critically on the spectral range of the input EEG data:

- **Individual variability**: User-specific neural rhythms (μ and β bands) vary significantly across individuals in both center frequency and bandwidth
- **Heuristic limitations**: Standard FBCSP uses predefined, evenly-spaced frequency sub-bands (e.g., 4-8, 8-12, 12-16 Hz) that are not selected using subject-specific physiological criteria
- **Dimensionality waste**: Using all bands in a filter bank increases computational cost and may include non-discriminative frequency ranges, introducing noise and overfitting
- **Volume conduction artifacts**: Traditional coherence measures are contaminated by zero-lag volume conduction, obscuring true neural connectivity

### Key Questions Addressed

1. Which frequency bands carry the most discriminative information for a given subject?
2. What is the minimum number of bands (K*) required to maintain performance within a 2% equivalence zone of the full filter bank baseline?
3. Which phase-based connectivity metric (wPLI, PLV, or PLI) provides the best trade-off between dimensionality reduction and inter-session robustness?

## Methodology

### 1. Filter Bank Design

The EEG signal is decomposed into a filter bank of **9 contiguous sub-bands spanning 4–40 Hz**:

| Band Index | Frequency Range (Hz) | Physiological Interpretation     |
|------------|----------------------|----------------------------------|
| 1          | 4–8                  | Theta                            |
| 2          | 8–12                 | μ (mu) — sensorimotor rhythm     |
| 3          | 12–16                | Low β (beta)                     |
| 4          | 16–20                | Low-mid β                        |
| 5          | 20–24                | Mid β                            |
| 6          | 24–28                | Mid-high β                       |
| 7          | 28–32                | High β                           |
| 8          | 32–36                | High β / low γ                   |
| 9          | 36–40                | Low γ                            |

Each band is extracted using a zero-phase bandpass filter (e.g., 4th-order Butterworth, forward-backward via `scipy.signal.filtfilt`) to avoid phase distortion.

### 2. Phase-Based Connectivity Metrics

Three complementary phase-based connectivity metrics are computed for each band:

#### Weighted Phase Lag Index (wPLI)

Measures the asymmetry of the imaginary component of the cross-spectrum, weighted by magnitude:

```
wPLI = |E[|Im{X}| · sgn(Im{X})]| / E[|Im{X}|]
```

- **Advantage**: Robust to volume conduction and common source artifacts
- **Interpretation**: Non-zero wPLI indicates consistent, non-zero-lag phase coupling
- **Best use case**: Inter-session robustness; when data spans multiple recording sessions with varying electrode impedances

#### Phase Locking Value (PLV)

Measures the consistency of phase differences across trials:

```
PLV = |(1/N) Σ exp(j · Δφ(t))|
```

- **Range**: 0 (random phase) to 1 (perfect phase locking)
- **Advantage**: Sensitive to both zero-lag and non-zero-lag coupling
- **Best use case**: Aggressive dimensionality reduction; prioritizes μ and low-β ranges

#### Phase Lag Index (PLI)

Measures the asymmetry of the phase difference distribution:

```
PLI = |E[sgn(Im{X})]|
```

- **Advantage**: Insensitive to volume conduction (ignores zero-lag coupling)
- **Disadvantage**: Discontinuous; discards amplitude information
- **Best use case**: Quick screening; binary assessment of consistent lagged coupling

### 3. Sensorimotor Channel Selection

Functional connectivity is computed across **four key sensorimotor channels**:

- **Left hemisphere**: C3, CP3 (or equivalent positions in the 10-20 system)
- **Right hemisphere**: C4, CP4 (or equivalent positions)

These channels are selected because:
- Motor imagery of left/right limbs produces contralateral ERD/ERS patterns
- The four channels capture hemispheric asymmetry central to MI classification
- Minimal channel count reduces computational overhead and overfitting risk

### 4. Hemispheric Coupling Difference Ranking

For each frequency band and connectivity metric:

1. **Compute intra-hemispheric connectivity**:
   - Left: connectivity(C3, CP3)
   - Right: connectivity(C4, CP4)

2. **Compute inter-hemispheric connectivity**:
   - Cross: connectivity(C3, C4), connectivity(CP3, CP4)

3. **Calculate hemispheric coupling difference** (HCD):
   ```
   HCD_band = |left_connectivity - right_connectivity|
   ```

4. **Rank bands** by the effect size (Cohen's d) of the HCD between MI classes (e.g., left hand vs. right hand imagery):
   ```
   d = (mean_HCD_class1 - mean_HCD_class2) / pooled_std
   ```

5. **Select top-K bands** with the largest effect sizes for downstream CSP feature extraction.

### 5. Top-K Band Pruning Strategy

The method evaluates K values from **1 to 8** (out of 9 total bands):

- **K=1**: Maximum compression; single most discriminative band
- **K=2–4**: Moderate compression; balance of performance and efficiency
- **K=5–8**: Minimal compression; near-complete filter bank

The **optimal K\*** is defined as the minimum K where classification accuracy remains within a **2% equivalence zone** of the full 9-band FBCSP baseline:

```
K* = min{K : accuracy(K) ≥ accuracy(9-band) - 0.02}
```

This ensures that band selection achieves meaningful dimensionality reduction without clinically significant performance degradation.

## Implementation Pipeline

### End-to-End Workflow

```
┌─────────────────────────────────────────────────────────────────────┐
│                    FC-GUIDED BAND SELECTION PIPELINE                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  1. EEG Preprocessing                                               │
│     ├── Bandpass filter (0.5–100 Hz) + notch filter (50/60 Hz)      │
│     ├── Artifact rejection / ICA cleaning                           │
│     └── Epoch extraction (cue onset to offset)                      │
│                                                                     │
│  2. Filter Bank Decomposition                                       │
│     ├── Apply 9 bandpass filters (4–40 Hz, 4 Hz width)              │
│     └── Extract 9 band-limited signal sets                          │
│                                                                     │
│  3. Phase Estimation                                                │
│     ├── Hilbert transform per band per channel                      │
│     └── Extract instantaneous phase angles                          │
│                                                                     │
│  4. Connectivity Computation                                        │
│     ├── wPLI / PLV / PLI for each band                              │
│     ├── Compute across 4 sensorimotor channel pairs                  │
│     └── Store connectivity matrices per band                        │
│                                                                     │
│  5. Band Ranking                                                    │
│     ├── Calculate HCD per band per MI class                         │
│     ├── Compute Cohen's d effect sizes                               │
│     └── Rank bands by discriminative power                          │
│                                                                     │
│  6. Top-K Selection                                                 │
│     ├── Select top-K bands for K = 1..8                             │
│     └── Identify K* (minimum K within 2% equivalence zone)          │
│                                                                     │
│  7. FBCSP Feature Extraction                                        │
│     ├── Run CSP on selected bands only                              │
│     └── Extract log-variance CSP features                           │
│                                                                     │
│  8. Classification                                                  │
│     ├── Support Vector Machine / SVR classifier                     │
│     ├── Cross-validation (subject-dependent or subject-independent)  │
│     └── Report accuracy, F1, Cohen's kappa                           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Core Python Implementation

```python
import numpy as np
from scipy.signal import butter, filtfilt, hilbert
from scipy.stats import ttest_ind
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.metrics import cohen_kappa_score
import mne
from mne.decoding import CSP


class FCGuidedBandSelector:
    """
    Functional Connectivity-guided band selection for MI-BCI.

    Parameters
    ----------
    sfreq : float
        Sampling frequency in Hz.
    band_edges : list of tuple
        List of (low, high) frequency pairs for the filter bank.
        Default: 9 bands from 4-40 Hz (4 Hz width each).
    metric : str
        Connectivity metric: 'wpli', 'plv', or 'pli'.
    """

    def __init__(self, sfreq=250, band_edges=None, metric='wpli'):
        self.sfreq = sfreq
        self.metric = metric.lower()
        self.band_edges = band_edges or [
            (4, 8), (8, 12), (12, 16), (16, 20),
            (20, 24), (24, 28), (28, 32), (32, 36), (36, 40)
        ]
        self.band_rankings_ = None
        self.selected_bands_ = None

    def _bandpass_filter(self, data, low, high):
        """Zero-phase bandpass filter using Butterworth design."""
        nyq = self.sfreq / 2.0
        low_norm = low / nyq
        high_norm = high / nyq
        b, a = butter(4, [low_norm, high_norm], btype='band')
        return filtfilt(b, a, data, axis=-1)

    def _compute_phase(self, signal):
        """Extract instantaneous phase via Hilbert transform."""
        analytic = hilbert(signal, axis=-1)
        return np.angle(analytic)

    def _compute_wpli(self, phase1, phase2):
        """
        Compute Weighted Phase Lag Index.

        Parameters
        ----------
        phase1, phase2 : array-like
            Instantaneous phase time series for two channels.
            Shape: (n_trials, n_timepoints)
        """
        # Compute cross-spectrum phase difference
        phase_diff = phase1 - phase2
        # Imaginary component of cross-spectrum
        im_cross = np.sin(phase_diff)
        # wPLI formula
        numerator = np.abs(np.mean(np.abs(im_cross) * np.sign(im_cross), axis=-1))
        denominator = np.mean(np.abs(im_cross), axis=-1)
        wpli = np.where(denominator > 0, numerator / denominator, 0)
        return np.mean(wpli, axis=0)  # Average across trials

    def _compute_plv(self, phase1, phase2):
        """
        Compute Phase Locking Value.

        Parameters
        ----------
        phase1, phase2 : array-like
            Instantaneous phase time series for two channels.
        """
        phase_diff = phase1 - phase2
        complex_plv = np.mean(np.exp(1j * phase_diff), axis=-1)
        return np.abs(complex_plv)

    def _compute_pli(self, phase1, phase2):
        """
        Compute Phase Lag Index.

        Parameters
        ----------
        phase1, phase2 : array-like
            Instantaneous phase time series for two channels.
        """
        phase_diff = phase1 - phase2
        im_cross = np.sin(phase_diff)
        pli = np.abs(np.mean(np.sign(im_cross), axis=-1))
        return pli

    def compute_connectivity(self, band_signals, channel_pairs):
        """
        Compute phase-based connectivity for all bands and channel pairs.

        Parameters
        ----------
        band_signals : list of ndarray
            Band-limited signals for each band.
            Each element: shape (n_trials, n_channels, n_timepoints)
        channel_pairs : list of tuple
            Pairs of channel indices for connectivity computation.
            e.g., [(0, 1), (2, 3), (0, 2), (1, 3)] for
            [left_intra, right_intra, cross1, cross2]

        Returns
        -------
        connectivity : ndarray
            Shape: (n_bands, n_channel_pairs)
        """
        n_bands = len(band_signals)
        connectivity = np.zeros((n_bands, len(channel_pairs)))

        for b_idx, signals in enumerate(band_signals):
            phases = self._compute_phase(signals)
            for p_idx, (ch1, ch2) in enumerate(channel_pairs):
                if self.metric == 'wpli':
                    connectivity[b_idx, p_idx] = self._compute_wpli(
                        phases[:, ch1, :], phases[:, ch2, :])
                elif self.metric == 'plv':
                    connectivity[b_idx, p_idx] = self._compute_plv(
                        phases[:, ch1, :], phases[:, ch2, :])
                elif self.metric == 'pli':
                    connectivity[b_idx, p_idx] = self._compute_pli(
                        phases[:, ch1, :], phases[:, ch2, :])

        return connectivity

    def rank_bands(self, connectivity_class1, connectivity_class2,
                   n_intra_pairs=2, n_cross_pairs=2):
        """
        Rank bands by hemispheric coupling difference effect size.

        Parameters
        ----------
        connectivity_class1, connectivity_class2 : ndarray
            Connectivity matrices for each MI class.
            Shape: (n_bands, n_channel_pairs)
        n_intra_pairs : int
            Number of intra-hemispheric channel pairs (left + right).
        n_cross_pairs : int
            Number of inter-hemispheric channel pairs.

        Returns
        -------
        ranked_indices : ndarray
            Band indices sorted by descending Cohen's d.
        effect_sizes : ndarray
            Cohen's d values for each band.
        """
        n_bands = connectivity_class1.shape[0]
        effect_sizes = np.zeros(n_bands)

        for b_idx in range(n_bands):
            # Intra-hemispheric coupling (first n_intra_pairs columns)
            intra1 = np.mean(connectivity_class1[b_idx, :n_intra_pairs])
            intra2 = np.mean(connectivity_class2[b_idx, :n_intra_pairs])

            # Hemispheric coupling difference
            hcd1 = np.abs(intra1)
            hcd2 = np.abs(intra2)

            # Cohen's d effect size
            pooled_std = np.sqrt(
                (np.var(intra1) + np.var(intra2)) / 2.0)
            if pooled_std > 0:
                effect_sizes[b_idx] = np.abs(hcd1 - hcd2) / pooled_std
            else:
                effect_sizes[b_idx] = 0

        ranked_indices = np.argsort(effect_sizes)[::-1]
        return ranked_indices, effect_sizes

    def select_top_k(self, ranked_indices, k):
        """Select top-K band indices."""
        return ranked_indices[:k]

    def find_optimal_k(self, ranked_indices, accuracies_k, baseline_accuracy,
                       tolerance=0.02):
        """
        Find optimal K* within the 2% equivalence zone.

        Parameters
        ----------
        ranked_indices : ndarray
            Band indices sorted by descending effect size.
        accuracies_k : dict
            Mapping of K value to classification accuracy.
        baseline_accuracy : float
            Accuracy of the full 9-band FBCSP pipeline.
        tolerance : float
            Equivalence zone tolerance (default: 0.02 = 2%).

        Returns
        -------
        k_star : int
            Minimum K maintaining accuracy within tolerance of baseline.
        """
        for k in range(1, len(ranked_indices) + 1):
            if k in accuracies_k:
                if accuracies_k[k] >= baseline_accuracy - tolerance:
                    return k
        return len(ranked_indices)  # Fallback: use all bands
```

### FBCSP Integration

```python
class FBCSPWithFCSelection:
    """
    Filter Bank CSP with FC-guided band selection.

    Integrates the FC-guided band selector with the standard FBCSP
    classification pipeline.
    """

    def __init__(self, sfreq=250, metric='wpli', n_csp_components=4):
        self.sfreq = sfreq
        self.selector = FCGuidedBandSelector(sfreq=sfreq, metric=metric)
        self.n_csp_components = n_csp_components
        self.csp = CSP(n_components=n_csp_components, reg=None)
        self.clf = SVC(kernel='linear', C=1.0)

    def fit(self, X, y, k=None):
        """
        Fit the pipeline with FC-guided band selection.

        Parameters
        ----------
        X : ndarray
            EEG data, shape (n_trials, n_channels, n_timepoints)
        y : ndarray
            Class labels
        k : int, optional
            Number of top bands to select. If None, uses all bands.
        """
        # Step 1: Filter bank decomposition
        band_signals = []
        for low, high in self.selector.band_edges:
            band_data = self.selector._bandpass_filter(X, low, high)
            band_signals.append(band_data)

        # Step 2: Compute connectivity and rank bands
        # (Assumes two-class MI: left hand vs right hand)
        class1_mask = y == y[0]  # Adjust based on actual labels
        class2_mask = ~class1_mask

        # Define sensorimotor channel pairs (indices for C3, CP3, C4, CP4)
        channel_pairs = [(0, 1), (2, 3), (0, 2), (1, 3)]

        conn_class1 = self.selector.compute_connectivity(
            [bs[class1_mask] for bs in band_signals], channel_pairs)
        conn_class2 = self.selector.compute_connectivity(
            [bs[class2_mask] for bs in band_signals], channel_pairs)

        ranked_indices, effect_sizes = self.selector.rank_bands(
            conn_class1, conn_class2)

        self.selector.band_rankings_ = ranked_indices
        self.selector.effect_sizes_ = effect_sizes

        # Step 3: Select top-K bands
        k = k or len(band_signals)
        selected = self.selector.select_top_k(ranked_indices, k)
        self.selector.selected_bands_ = selected

        # Step 4: FBCSP on selected bands
        csp_features = []
        for b_idx in selected:
            band_data = band_signals[b_idx]
            csp_feat = self.csp.fit_transform(band_data, y)
            csp_features.append(csp_feat)

        X_csp = np.hstack(csp_features)

        # Step 5: Classification
        self.clf.fit(X_csp, y)
        return self

    def predict(self, X):
        """Predict class labels for new data."""
        band_signals = []
        for low, high in self.selector.band_edges:
            band_data = self.selector._bandpass_filter(X, low, high)
            band_signals.append(band_data)

        selected = self.selector.selected_bands_
        csp_features = []
        for b_idx in selected:
            band_data = band_signals[b_idx]
            csp_feat = self.csp.transform(band_data)
            csp_features.append(csp_feat)

        X_csp = np.hstack(csp_features)
        return self.clf.predict(X_csp)
```

## Performance Benchmarks

### BCI Competition IV-2a Dataset

- **Subjects**: 9 (A01–A09)
- **Classes**: 4-class motor imagery (left hand, right hand, foot, tongue)
- **Channels**: 22 EEG electrodes
- **Sampling rate**: 250 Hz
- **Trials**: 288 per subject (72 per class), 2 sessions

**Key results**:
- FC-guided selection consistently outperforms random band ablation
- PLV achieves the most aggressive dimensionality reduction (lower K*)
- wPLI shows superior inter-session robustness (Session 1 → Session 2 transfer)
- Typical K* range: 3–6 bands depending on subject and metric

### OpenBMI Dataset

- **Subjects**: 54
- **Classes**: 2-class motor imagery (left hand, right hand)
- **Channels**: 62 EEG electrodes
- **Sampling rate**: 1,000 Hz
- **Sessions**: 2 sessions per subject

**Key results**:
- Larger subject pool confirms generalizability of FC-guided approach
- Dimensionality reduction savings: 22.2% to 77.8% fewer CSP fits
- Inter-subject variability in K* highlights the value of subject-specific selection

### Ablation: Random vs. FC-Guided Selection

| Metric            | Full 9-band FBCSP | FC-Guided (K*) | Random (K*) |
|-------------------|-------------------|-----------------|-------------|
| Accuracy          | Baseline          | ≥ baseline - 2% | Variable    |
| CSP fits reduced  | 0%                | 22–78%          | 22–78%      |
| Session transfer  | Baseline          | Superior (wPLI) | Degraded    |
| Interpretability  | Low               | High            | None        |

## PLV vs. wPLI Trade-offs

### PLV (Phase Locking Value)

**Strengths**:
- Most aggressive dimensionality reduction (lowest K*)
- Strongly prioritizes μ (8–12 Hz) and low-β (12–20 Hz) ranges
- Highest sensitivity to phase-locked oscillatory activity
- Best for single-session, within-subject decoding

**Weaknesses**:
- Susceptible to volume conduction artifacts
- Zero-lag coupling from common sources inflates connectivity estimates
- Lower inter-session robustness (Session 1 → Session 2 performance drops more)

### wPLI (Weighted Phase Lag Index)

**Strengths**:
- Superior inter-session robustness
- Mitigates volume conduction by weighting non-zero-lag components
- More stable across recording sessions with varying electrode setups
- Better generalization to unseen data

**Weaknesses**:
- May require more bands (higher K*) to reach equivalence zone
- Computationally slightly more expensive than PLV
- May miss genuine zero-lag functional connectivity

### Practical Recommendation

| Use Case                                    | Recommended Metric |
|---------------------------------------------|--------------------|
| Maximum compression, single-session         | PLV                |
| Cross-session / longitudinal studies        | wPLI               |
| Quick screening / resource-constrained      | PLI                |
| Clinical / real-world BCI deployment        | wPLI               |
| Research / maximum accuracy                 | Compare all three  |

## Usage Examples

### Basic Usage

```python
from your_module import FCGuidedBandSelector, FBCSPWithFCSelection

# Initialize with PLV for aggressive dimensionality reduction
pipeline = FBCSPWithFCSelection(sfreq=250, metric='plv', n_csp_components=4)

# Fit on training data (shape: n_trials x n_channels x n_timepoints)
pipeline.fit(X_train, y_train, k=4)  # Select top 4 bands

# Predict
predictions = pipeline.predict(X_test)

# Access selected bands
print(f"Selected bands: {pipeline.selector.selected_bands_}")
print(f"Band rankings:  {pipeline.selector.band_rankings_}")
```

### Finding Optimal K*

```python
# Evaluate all K values
selector = FCGuidedBandSelector(sfreq=250, metric='wpli')
# ... (compute connectivity and rank bands as above) ...

# Get accuracies for each K (requires cross-validation loop)
accuracies_k = {}
for k in range(1, 9):
    acc = cross_validate_with_k(X, y, k, ranked_indices)
    accuracies_k[k] = acc

# Find optimal K*
baseline_acc = cross_validate_with_k(X, y, 9, ranked_indices)
k_star = selector.find_optimal_k(ranked_indices, accuracies_k, baseline_acc)
print(f"Optimal K*: {k_star} (baseline accuracy: {baseline_acc:.3f})")
```

### Working with MNE-Python Datasets

```python
import mne
from mne.datasets import eegbci

# Load BCI Competition IV-2a data (via MNE)
# Note: Use the official dataset download for Competition IV-2a
raw = mne.io.read_raw_edf('A01T.edf', preload=True)
raw.filter(0.5, 100)
raw.notch_filter([50])

# Extract epochs
events = mne.find_events(raw, stim_channel='STI 014')
epochs = mne.Epochs(raw, events, event_id={
    'left_hand': 1, 'right_hand': 2,
    'foot': 3, 'tongue': 4
}, tmin=0, tmax=4, baseline=None, preload=True)

# Pick sensorimotor channels
epochs.pick_channels(['C3', 'CP3', 'C4', 'CP4'])

# Convert to numpy array
X = epochs.get_data()
y = epochs.events[:, 2]

# Run FC-guided band selection
pipeline = FBCSPWithFCSelection(sfreq=250, metric='wpli')
pipeline.fit(X, y, k=4)
```

## Configuration Parameters

| Parameter              | Type   | Default        | Description                                    |
|------------------------|--------|----------------|------------------------------------------------|
| `sfreq`                | float  | 250            | EEG sampling frequency (Hz)                    |
| `metric`               | str    | 'wpli'         | Connectivity metric: 'wpli', 'plv', 'pli'      |
| `band_edges`           | list   | 9 bands 4–40 Hz| Custom filter bank definitions                 |
| `n_csp_components`     | int    | 4              | Number of CSP spatial filters per band         |
| `k`                    | int    | None (use all) | Number of top bands to select                  |
| `equivalence_tolerance`| float  | 0.02           | 2% accuracy tolerance for K* selection         |
| `channel_pairs`        | list   | 4 pairs        | Sensorimotor channel indices for FC            |

## Limitations and Considerations

1. **Static vs. Adaptive**: This method uses **static** band selection (computed once per subject). For adaptive BCIs, consider re-ranking bands online as neural patterns shift.

2. **Channel Selection**: The 4-channel sensorimotor selection is optimal for hand MI. Foot and tongue imagery may require additional channel pairs (e.g., Cz, FCz).

3. **Filter Design**: The 4 Hz band width is a design choice. Narrower bands increase frequency resolution but may reduce signal-to-noise ratio.

4. **Effect Size Sensitivity**: Cohen's d assumes approximately normal distributions. For small trial counts, consider permutation-based effect size estimation.

5. **Multi-class Extension**: The current methodology is demonstrated on 2-class MI. For 4-class (Competition IV-2a), apply the ranking per class pair and aggregate via voting or mean effect size.

6. **Computational Cost**: Connectivity computation scales as O(n_bands × n_channel_pairs × n_trials × n_timepoints). For large datasets, consider subsampling trials or using parallel computation.

## Related Skills

- **`eeg-brain-connectivity-bci`**: General EEG-based brain connectivity analysis for BCI applications
- **`fc-guided-band-selection-mi-bci`**: Variant focusing on motor imagery-specific implementations
- **`hermes-brain-connectivity`**: Comprehensive brain connectivity toolkit with multiple modalities

## References

1. Araújo do Carmo, N., & Nagarajan, A. (2026). *Functional Connectivity-Guided Band Selection for Motor Imagery Brain-Computer Interfaces*. arXiv:2605.00746 [q-bio.NC, eess.SP].

2. Blankertz, B., et al. (2008). Optimizing spatial filters for robust EEG single-trial analysis. *IEEE Signal Processing Magazine*, 25(1), 41-56.

3. Vinck, M., et al. (2011). An improved index of phase-synchronization for electrophysiological data in the presence of volume-conduction, noise and sample-size bias. *NeuroImage*, 55(4), 1548-1565.

4. Lachaux, J.-P., et al. (1999). Measuring phase synchrony in brain signals. *Human Brain Mapping*, 8(4), 194-208.

5. Stam, C. J., et al. (2007). Phase lag index: Assessment of functional connectivity from multi channel EEG and MEG with diminished bias from common sources. *Human Brain Mapping*, 28(11), 1178-1193.

6. Ang, K. K., et al. (2008). Filter bank common spatial pattern (FBCSP) in brain-computer interface. *IJCNN*, 2390-2397.
