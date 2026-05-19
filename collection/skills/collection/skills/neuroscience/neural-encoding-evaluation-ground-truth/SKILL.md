---
name: neural-encoding-evaluation-ground-truth
description: Evaluation framework for neural encoding models using MEEG ground-truth approximation via Canonical Prediction Alignment (CPA) and Participant Averaging (PA). Yields 250-1000% improvement over conventional metrics. Based on Di Liberto (2026) arXiv:2604.14694.
tags: [neural-encoding, evaluation-metrics, MEEG, CCA, TRF, ground-truth-approximation, signal-detectability]
date: 2026-04-18
source: "arXiv:2604.14694"
---

# Neural Encoding Model Evaluation via Ground-Truth Approximation

## Core Problem

Standard evaluation metrics (Pearson/Spearman correlation) between encoding model predictions and MEEG signals **severely underestimate** model performance because most MEEG variance is stimulus-unrelated noise.

## Solution: CPA-PA Framework

### Canonical Prediction Alignment (CPA)
- Uses Canonical Correlation Analysis (CCA) to align model predictions with MEEG recordings
- Suppresses stimulus-irrelevant signals by projecting MEEG onto prediction-aligned subspace
- Works at single-participant level
- **Gain: ~68% over best-channel correlation (R-MAX)**

### Participant Averaging (CPA-PA)
- Additional denoising when stimuli are shared across participants
- Averages CPA-aligned signals across participants
- **Gain: ~252% over R-MAX; up to 3241% at very low SNR**

## Metrics Comparison

| Metric | Description | Limitation |
|--------|-------------|------------|
| R-AVG | Average across channels | Diluted by noisy channels |
| R-MAX | Best single channel | Requires cross-validation; still noise-limited |
| R-CPA | CPA-aligned correlation | Single-participant denoising |
| R-CPA-PA | CPA + participant averaging | Requires shared stimuli across participants |

## Validation Results

- **Synthetic data**: 300-1000% improvement at SNR -30 to -50 dB
- **Real data**: 250% average improvement across 34 MEEG datasets (818 datapoints)
- **Signal detectability**: Match-vs-mismatch accuracy improved by 71% (CPA) and 210% (CPA-PA)
- **Single-participant recovery**: CPA retrieves neural signatures where conventional metrics fail

## Signal Detectability Framework

Match-vs-mismatch test:
1. Encode model predictions for stimulus segment
2. Compare to neural response for same segment ("match") vs random segment ("mismatch")
3. Classification accuracy measures whether encoding captures stimulus-relevant activity

## Key Insight

Linear Time-Invariant (TRF) encoding models may have been **systematically undervalued** in sensory neuroscience due to evaluation metric limitations. CPA-PA reveals they capture significantly more stimulus-relevant activity than previously recognized.

## Implementation Approach

```python
# CPA: CCA alignment between predictions and MEEG
from sklearn.cross_decomposition import CCA
cca = CCA(n_components=k)
X_aligned, Y_aligned = cca.fit_transform(predictions, meeg_data)

# PA: Average across participants with shared stimuli
aligned_avg = np.mean([aligned[p] for p in participants], axis=0)

# Correlation with ground-truth approximation
r_cpa_pa = np.corrcoef(predictions, aligned_avg)[0, 1]
```

## Open Data Resource

- 34 standardized MEEG datasets (31 EEG, 2 MEG, 1 fNIRS)
- Tasks: speech, music, video, sign language, auditory attention
- Populations: adults, children, infants
- Available at: https://osf.io/c76p8/

## Related Skills

- `neural-encoding-evaluation-meeg`: Related MEEG evaluation
- `hermes-brain-connectivity`: Brain connectivity analysis
- `eeg-hopfield-emotion-energy`: EEG analysis methods

## References

- Di Liberto, G.M. (2026). "Robust Evaluation of Neural Encoding Models via ground-truth approximation." arXiv:2604.14694.
- Crosse, M.J. et al. (2016). "The Multivariate Temporal Response Function." Frontiers in Human Neuroscience.
- Lalor, E.C. et al. (2006). "The temporal response function for speech envelope tracking." NeuroImage.
