---
name: eeg-faar-artifact-rejection
description: >
  Fast Automatic Artifact Rejection (FAAR) methodology for EEG motor imagery BCIs.
  Lightweight automated artifact rejection that computes artifact-sensitive features,
  derives epoch-level Signal Quality Index, adaptively selects rejection thresholds,
  and automatically rejects contaminated epochs. Reduces inter-subject variability
  and addresses BCI illiteracy. arXiv: 2605.12408 (eess.SP). Hajhassani, Aristimunha,
  Graignic, Mellot, Kusch, Delorme, Semah, Caillet.
---

# Fast Automatic Artifact Rejection (FAAR) for EEG MI-BCIs

Lightweight, fully automated artifact rejection methodology for motor imagery (MI) based
brain-computer interfaces. Addresses the gap between decoder-focused research and data
curation quality, showing that artifact rejection significantly impacts downstream decoding
performance, especially in low-SNR conditions.

**Source**: arXiv 2605.12408 (2026-05-12), eess.SP

## Core Problem

Motor imagery BCIs are highly sensitive to EEG artifacts (eye blinks, muscle activity,
cardiac signals, line noise), yet most research focuses on decoder design rather than
data curation quality. The practical impact of automated artifact rejection on downstream
MI decoding performance remained unclear prior to this work.

## FAAR Methodology

### 1. Artifact-Sensitive Feature Computation

Computes a compact set of features sensitive to different artifact types:
- **Amplitude-based**: Peak-to-peak amplitude, variance, kurtosis
- **Frequency-based**: Power spectral density in artifact-prone bands
- **Temporal**: Signal derivatives, zero-crossing rates
- **Spatial**: Cross-channel correlations, reference channel deviations

### 2. Signal Quality Index (SQI)

Derives an epoch-level Signal Quality Index from the computed features:
```
SQI = f(artifact_features) → [0, 1]
```
Higher SQI indicates cleaner signal. The SQI is computed per epoch, enabling
fine-grained rejection decisions.

### 3. Adaptive Threshold Selection

Unlike fixed-threshold approaches, FAAR adaptively selects rejection thresholds
based on the data distribution:
- No manual threshold tuning required
- No prior knowledge of artifact types needed
- Thresholds adapt to subject-specific signal characteristics

### 4. Automatic Epoch Rejection

Contaminated epochs are automatically rejected based on the adaptive thresholds:
- Preserves sufficient data for training (not overly aggressive)
- Supports real-time BCI constraints (low computational overhead)
- Consistent behavior across offline curation, training, and online filtering

## Key Results

### Evaluation Protocol
- **13 publicly available MI datasets** evaluated
- Compared against: no-rejection baseline, AutoReject, Isolation Forest

### Main Findings

1. **Subject- and regime-dependent effects**: Rejection benefits vary significantly
   across subjects and recording conditions
2. **Largest gains in low-SNR conditions**: FAAR provides the most improvement
   when baseline signal quality is poor
3. **Reduces inter-subject variability**: Important property for MI-BCI reliability
   and addressing BCI illiteracy
4. **No aggressive data removal**: Maintains sufficient data for robust training
5. **Real-time compatible**: Lightweight computation supports online BCI use

### Comparison with Alternatives

| Method | Automation | Real-time | Subject Adaptivity | Data Preservation |
|--------|------------|-----------|-------------------|-------------------|
| FAAR | ✓ Full | ✓ Yes | ✓ Adaptive | ✓ Conservative |
| AutoReject | ✓ Full | ✗ No | ✓ Adaptive | Variable |
| Isolation Forest | ✓ Full | △ Limited | ✗ Fixed | Often aggressive |
| Manual | ✗ No | ✗ No | ✓ Expert | ✓ Selective |

## Implementation Pattern

```python
import numpy as np
from scipy import signal

class FAAR:
    def __init__(self):
        self.sqi_threshold = None
        
    def compute_features(self, epoch, fs):
        """Compute artifact-sensitive features for an epoch."""
        features = {}
        # Amplitude features
        features['ptp'] = np.ptp(epoch, axis=1)  # peak-to-peak
        features['var'] = np.var(epoch, axis=1)
        features['kurtosis'] = self._kurtosis(epoch, axis=1)
        
        # Frequency features
        freqs, psd = signal.welch(epoch, fs, nperseg=fs)
        features['delta_power'] = np.mean(psd[:, freqs < 4], axis=1)
        features['muscle_power'] = np.mean(psd[:, freqs > 30], axis=1)
        
        # Temporal features
        features['deriv_var'] = np.var(np.diff(epoch, axis=1), axis=1)
        
        return features
    
    def compute_sqi(self, features):
        """Derive Signal Quality Index from features."""
        # Normalize and combine features into single SQI score
        normalized = self._normalize_features(features)
        sqi = np.mean(normalized, axis=0)  # Average across features
        return sqi
    
    def adaptive_threshold(self, sqi_values):
        """Adaptively select rejection threshold."""
        # Use data-driven approach (e.g., percentile-based)
        threshold = np.percentile(sqi_values, self.rejection_percentile)
        return threshold
    
    def reject_epochs(self, eeg_data, fs, rejection_percentile=10):
        """Full FAAR pipeline: features → SQI → threshold → reject."""
        self.rejection_percentile = rejection_percentile
        
        features_list = []
        for epoch in eeg_data:
            features = self.compute_features(epoch, fs)
            sqi = self.compute_sqi(features)
            features_list.append(sqi)
        
        sqi_values = np.array(features_list)
        threshold = self.adaptive_threshold(sqi_values)
        
        # Reject epochs below threshold
        clean_mask = sqi_values >= threshold
        return clean_mask, sqi_values
```

## Use Cases

1. **MI-BCI pipeline preprocessing**: Essential first step before decoder training
2. **BCI illiteracy mitigation**: Reduces inter-subject variability in BCI performance
3. **Online BCI systems**: Lightweight enough for real-time artifact filtering
4. **Multi-subject studies**: Ensures consistent data quality across subjects
5. **Low-SNR recordings**: Provides largest gains when signal quality is poor

## Integration with Existing Workflows

### With MNE-Python
```python
import mne
from faar import FAAR

# Load raw EEG
raw = mne.io.read_raw_edf('subject01.edf')
epochs = mne.Epochs(raw, events, event_id, tmin, tmax)

# Apply FAAR
faar = FAAR()
clean_mask, sqi = faar.reject_epochs(epochs.get_data(), epochs.info['sfreq'])
epochs_clean = epochs[clean_mask]
```

### With PyTorch BCI pipelines
```python
# FAAR as preprocessing before neural network training
clean_data = eeg_data[clean_mask]
# Train decoder on clean data only
```

## Pitfalls & Notes

- **Adaptive is key**: Fixed thresholds perform poorly across subjects; FAAR's
  adaptive approach is essential for generalization
- **Don't be too aggressive**: Over-rejection reduces training data and can harm
  decoder performance; FAAR's conservative approach preserves data
- **Subject-dependent effects**: Benefits vary by subject; some subjects show
  minimal improvement while others show significant gains
- **Low-SNR priority**: Prioritize FAAR for recordings with known artifact issues
  or low baseline signal quality
- **Real-time constraints**: FAAR is designed for online use; ensure feature
  computation fits within your system's latency budget
- **Complement, don't replace**: FAAR handles epoch-level rejection; consider
  combining with channel-level rejection for comprehensive cleaning

## Related Skills
- `eeg-preprocessing-reliability` — EEG decoding reliability and preprocessing
- `eeg-cross-subject-decoding-survey` — Cross-subject EEG decoding methods
- `pa-tcnet-cross-subject-eeg` — Pathology-aware cross-subject EEG classification
- `mind2drive-eeg-driver-intention` — EEG-based driver intention decoding
- `eeg-foundation-model-adapters` — EEG foundation models with domain adaptation

## Activation Keywords
- FAAR artifact rejection, EEG cleaning, motor imagery BCI
- signal quality index, automated artifact rejection
- BCI illiteracy, inter-subject variability
- EEG preprocessing, epoch rejection
- low-SNR EEG, real-time BCI filtering