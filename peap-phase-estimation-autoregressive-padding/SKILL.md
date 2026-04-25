---
name: peap-phase-estimation-autoregressive-padding
description: "Phase Estimation with Autoregressive Padding (PEAP) for EEG oscillatory phase analysis — uses AR model to pad edge segments, improving phase estimation accuracy by 3.2-9.2% over Hilbert transform. Activation triggers: EEG phase, phase estimation, autoregressive, Hilbert transform, oscillation, brain rhythm, time-frequency."
---

# PEAP: Phase Estimation with Autoregressive Padding

> Autoregressive model-based edge padding for EEG oscillatory phase estimation, achieving 3.2–9.2% accuracy improvement over standard Hilbert transform by reducing edge artifacts in band-pass filtered signals.

## Metadata
- **Source**: arXiv:2604.02212
- **Authors**: Miriam Kirchhoff, Johanna Rösch, Maria Ermolova, Oskari Ahola, Sarah Harders, Juliana Hougland, Ulf Ziemann
- **Published**: 2026-04-02
- **Categories**: q-bio.NC

## Core Methodology

### Key Innovation
Applies autoregressive (AR) modeling to predict and pad EEG signal segments at both edges before band-pass filtering and Hilbert transform phase extraction. This eliminates the edge artifacts that degrade phase estimation at trial boundaries.

### Technical Framework

1. **Problem**: Band-pass filtering creates edge artifacts at trial boundaries → phase estimates unreliable near edges (affects ~1 cycle at each end)
2. **Solution — AR Padding**:
   - Fit AR model to the observed signal segment
   - Forward-predict beyond the end of the segment
   - Backward-predict before the start of the segment
   - Concatenate predicted padding with observed signal
   - Apply band-pass filter to the padded signal
   - Extract phase via Hilbert transform on padded signal
   - Discard padding portions, keep only original segment phase estimates
3. **Result**: +3.2% to +9.2% phase estimation accuracy across frequency bands

### Algorithm Steps
1. Fit AR(p) model to input signal x(t) using Yule-Walker or Burg method
2. Generate forward extension: x(N+1), x(N+2), ... via AR prediction
3. Generate backward extension: ..., x(-2), x(-1), x(0) via time-reversed AR
4. Concatenate: [backward_pad | x(t) | forward_pad]
5. Band-pass filter the padded signal
6. Apply Hilbert transform → analytic signal → instantaneous phase
7. Extract phase only for original segment indices

## Implementation Guide

### Prerequisites
- Python 3.x with NumPy, SciPy
- `scipy.signal` for filtering and AR modeling

### Step-by-Step
1. Load EEG data as trial segments
2. Determine AR model order (e.g., via AIC or BIC)
3. Fit AR model and generate bidirectional padding
4. Apply band-pass filter to padded signal
5. Compute instantaneous phase via Hilbert transform
6. Extract phase estimates for original time points

### Code Example
```python
import numpy as np
from scipy.signal import hilbert, butter, filtfilt, lfilter
from numpy.linalg import solve

def fit_ar_model(signal, order=20):
    """Fit AR model using Yule-Walker equations."""
    N = len(signal)
    # Autocorrelation
    r = np.correlate(signal, signal, mode='full')[N-1:N+order]
    # Yule-Walker
    R = np.array([[r[abs(i-j)] for j in range(order)] for i in range(order)])
    rhs = -r[1:order+1]
    coeffs = solve(R, rhs)
    return coeffs

def ar_predict(signal, coeffs, n_forward):
    """Forward-predict n_forward samples using AR model."""
    p = len(coeffs)
    extended = np.concatenate([signal, np.zeros(n_forward)])
    for i in range(len(signal), len(signal) + n_forward):
        extended[i] = -np.sum(coeffs[::-1] * extended[i-p:i])
    return extended

def peap_phase(eeg_trial, freq_band, ar_order=20, pad_factor=3):
    """PEAP: Phase Estimation with Autoregressive Padding."""
    fs = eeg_trial.shape[0]  # assume first dim is time
    n_samples = len(eeg_trial)
    
    # Fit AR and generate padding
    coeffs = fit_ar_model(eeg_trial, order=ar_order)
    n_pad = int(pad_factor * fs / freq_band[0])  # ~3 cycles of padding
    
    # Forward and backward padding
    forward = ar_predict(eeg_trial, coeffs, n_pad)[n_samples:]
    backward = ar_predict(eeg_trial[::-1], coeffs, n_pad)[n_samples:][::-1]
    
    # Padded signal
    padded = np.concatenate([backward, eeg_trial, forward])
    
    # Band-pass filter
    b, a = butter(4, [freq_band[0]/(fs/2), freq_band[1]/(fs/2)], btype='band')
    filtered = filtfilt(b, a, padded)
    
    # Hilbert transform phase
    analytic = hilbert(filtered)
    phase = np.angle(analytic)
    
    # Extract original segment
    return phase[n_pad:n_pad+n_samples]
```

## Applications
- **EEG phase analysis**: More accurate trial-level phase estimation for ERP/ERD studies
- **Brain-state-dependent stimulation**: Closed-loop TMS/tES triggered on oscillatory phase
- **Brain-computer interfaces**: Phase-based features for motor imagery decoding
- **Sleep research**: Accurate slow-wave phase detection for memory consolidation studies
- **Neurofeedback**: Real-time phase-based neurofeedback training

## Key Findings
1. AR padding eliminates edge artifacts in band-pass filtered EEG
2. Phase accuracy improves 3.2–9.2% depending on frequency band
3. Improvement is most pronounced for low-frequency oscillations (theta, alpha)
4. Method is computationally lightweight and suitable for real-time applications
5. Compatible with any downstream phase analysis (PLV, PAC, phase-triggered averaging)

## Pitfalls
- AR model order selection affects prediction quality — too low causes poor extrapolation
- Very noisy signals may produce unstable AR predictions
- Padding length should be at least 2-3 cycles of the target frequency
- Not a replacement for proper experimental design (still better to have longer trials)

## Related Skills
- brain-state-transition-network-control
- rl-closed-loop-eeg-tms
- eeg-foundation-models-review
- deep-learning-closed-loop-tms-bci
