---
name: pa-tcnet-cross-subject-eeg
description: "PA-TCNet methodology for cross-subject motor imagery EEG decoding in stroke patients. Combines pathology-aware temporal calibration (filtering lesion-induced slow-wave artifacts) with physiology-guided target refinement (entropy-based pseudo-label filtering) for robust domain adaptation. Use when: cross-subject EEG decoding, stroke rehabilitation BCI, motor imagery classification with pathological EEG, domain adaptation for EEG, lesion-aware neural decoding, or brain-computer interfaces for neurological patients."
version: 1.0.0
---

# PA-TCNet: Pathology-Aware Temporal Calibration

Cross-subject EEG decoding framework for stroke patient motor imagery BCI.

## Problem

Stroke lesions cause: (1) abnormal slow-wave temporal dynamics that mislead temporal filters, (2) pronounced inter-patient heterogeneity that breaks domain adaptation, (3) unstable pseudo-labels in target domain.

## Architecture

### Pathology-Aware Temporal Calibration
```python
# Filter pathological slow waves (<4 Hz) from temporal processing
def pathology_aware_temporal_calibration(eeg_signal, fs=250):
    from scipy.signal import butter, filtfilt
    # High-pass filter to remove slow-wave artifacts
    b, a = butter(4, 4.0, 'highpass', fs=fs)
    calibrated = filtfilt(b, a, eeg_signal, axis=-1)
    return calibrated
```

### Physiology-Guided Target Refinement
```python
def physiology_guided_refinement(predictions, confidence_threshold=0.7):
    """Entropy-based pseudo-label filtering."""
    entropy = -np.sum(predictions * np.log(predictions + 1e-8), axis=-1)
    reliable = entropy < -np.log(confidence_threshold)
    return reliable
```

### Multi-Source Domain Adaptation
- Multiple healthy source domains → stroke target domain
- Category-level multi-source alignment (not global alignment)
- Prevents negative transfer from mismatched source categories

## Training Pipeline

1. Calibrate temporal features (remove slow-wave contamination)
2. Align source domains at category level
3. Generate pseudo-labels with entropy filtering
4. Fine-tune with reliable target samples only

## Activation Keywords
- PA-TCNet
- cross-subject EEG decoding
- stroke BCI
- motor imagery classification
- pathology-aware EEG
- domain adaptation EEG
- lesion-aware decoding
- 跨受试者脑电解码

## References
- Wang et al., "PA-TCNet: Pathology-Aware Temporal Calibration for Cross-Subject Motor Imagery EEG Decoding in Stroke Patients", arXiv:2604.16554, 2026
