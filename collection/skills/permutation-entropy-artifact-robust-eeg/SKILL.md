---
name: permutation-entropy-artifact-robust-eeg
description: Use on raw EEG; ordinal entropy survives blink artifacts.
category: ai_collection
version: "1.0.0"
trigger_words:
  - permutation entropy
  - ordinal patterns
  - spatial permutation entropy
  - EEG artifact robustness
  - eyes open eyes closed
  - raw EEG without preprocessing
source: arXiv:2609.22265
source_title: Exploring the robustness of permutation entropy analysis to differentiate between closed-eyes and open-eyes resting states
authors: Juan Gancio, Natalia López López, Antonio J. Pons, Giulio Tirabassi, Cristina Masoller
published: 2026-09-22
categories: q-bio.NC, physics.data-an
---

# Permutation Entropy Artifact-Robust EEG State Analysis

## Core Finding

Temporal permutation entropy (PE) and horizontal spatial permutation entropy (SPE_H) distinguish eyes-open (EO) vs eyes-closed (EC) resting states **directly on raw EEG without artifact removal** (paired t-test p < 10⁻³ over 109 subjects). Robustness extends to: (a) recordings as short as **0.12 s** (19 samples → 17 ordinal patterns) for temporal PE; (b) a **single spatial snapshot** across 64 channels for SPE_H; (c) reduced electrode montages (31 or 17 channels) because the undersampling bias cancels in paired within-subject tests.

**Mechanism**: ordinal patterns encode *relative* order of data points, not absolute values. Blink artifacts act as monotonic temporal ramps which PE is provably robust to. Spatially, blink gradients run anterior–posterior across frontal channels, so **vertical** OPs (FP1→FPZ→FP2 chain, pattern 1-2-3 over-expressed) are corrupted while **horizontal** (lateral-medial) OPs stay perpendicular to the gradient and unaffected.

## Method

### 1. Temporal PE (per channel)
- Sliding window over each channel's time series; embed length L=3 (patterns from 3 consecutive samples, 160 Hz data).
- Each window [x_i, x_{i+1}, x_{i+2}] → permutation index π; symbol s_i ∈ {L! = 6 possible ordinal patterns}.
- Ties broken by order of occurrence (introduces fixed bias that cancels in EO−EC differences).
- PE_k = −Σ p_j ln p_j over pattern probabilities; average over channels → ⟨PE⟩_j per subject j.

### 2. Spatial PE (per time snapshot)
- At each time step, OPs defined over L=3 spatially adjacent channels in two orientations:
  - **Horizontal (SPE_H)**: lateral–medial chains (perpendicular to blink gradient → artifact-robust).
  - **Vertical (SPE_V)**: anterior–posterior chains (aligned with blink gradient → corrupted by artifacts; only discriminates on cleaned data).
- One snapshot of all 64 channels suffices for significant EO/EC separation with SPE_H.

### 3. Statistical protocol
- Paired t-test (scipy) on within-subject differences ⟨PE⟩_j,EO − ⟨PE⟩_j,EC; significance threshold p < 10⁻³.
- For time-budget analysis: split into 118 non-overlapping 0.5 s segments, plot median p-value vs analyzed interval; raw data reaches significance at 0.12 s.
- Dataset: PhysioNet EEGMMIDB, 109 subjects, 64 channels, 160 Hz, 59 s per condition.

## Key quantitative results
| Quantity | Result |
|---|---|
| PE raw-data EO vs EC | significant, p < 10⁻³, unaffected by ICA artifact removal |
| SPE_H raw data | significant, p < 10⁻³, artifact removal changes almost nothing |
| SPE_V raw data | NOT discriminative (blink gradient over-expresses pattern 1-2-3); discriminative only after cleaning |
| Minimum time for PE (raw) | 0.12 s (17 ordinal patterns) |
| Minimum data for SPE_H | single 64-channel snapshot |
| Electrode reduction 64→31→17 | differences stay significant; negative bias cancels in paired test |
| Raw vs cleaned pre-frontal OP sequence | only 40% identical, but probability distributions nearly equal → PE unchanged |

## Implementation recipe
```python
# 1. Load raw EEG (NO filtering, NO ICA)
# 2. For each channel: build L=3 ordinal patterns over sliding windows
#    (ties → order of occurrence)
# 3. PE_ch = -sum(p*np.log(p)) over 6 pattern probs
# 4. Spatial: at each sample, horizontal triplets (lateral-medial chains incl. FPZ)
#    vs vertical triplets (anterior-posterior)
# 5. Report ⟨PE⟩, ⟨SPE_H⟩, ⟨SPE_V⟩ per subject/condition
# 6. scipy.stats.ttest_rel(ec_vals, eo_vals) → paired test
```

## When to use
- Real-time or low-power EEG state detection where preprocessing is too costly (portable devices, BCI, medical monitors).
- Deciding whether artifact removal is needed before entropy analysis (often: it is not).
- Any EO/EC, vigilance, or resting-state classification pipeline.
- Choosing spatial OP orientation: prefer orientation perpendicular to known artifact gradient.

## Pitfalls
- **SPE_V on raw data is a trap**: vertical/anterior-posterior OPs align with blink gradients and fail without cleaning — use horizontal OPs or alpha-band filtering instead.
- Tie-breaking bias: order-of-occurrence ties bias pattern probabilities slightly; harmless for *differences* but not for absolute entropy comparisons across pipelines.
- Undersampled pattern distributions (17-31 channels) lower absolute SPE values; only the paired difference remains valid.
- Cleaning was applied to EO recordings only — asymmetry could itself aid discrimination; verify with an alternative removal method before claiming artifact-independence.
- L=3 only; larger L (4+) untested here and needs far more data per estimate.

## Extensions
- Weighted PE / amplitude-aware PE for comparison; OP variability; ordinal transitions.
- 2D spatial patterns or Hilbert-curve orderings of channels (underexplored).
- Combine temporal + spatial OPs; increase L.

## References
- Bandt & Pompe, Phys. Rev. Lett. 88, 174102 (2002) — original PE.
- Boaretto et al., Chaos Solitons Fractals 171, 113453 (2023) — spatial PE.
- Gancio et al., Chaos 34, 043130 (2024) — prior EO/EC PE comparison.
