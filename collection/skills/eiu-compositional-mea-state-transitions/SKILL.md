---
name: eiu-compositional-mea-state-transitions
description: EIU compositional analysis of MEA neuronal network state transitions over time.
category: ai_collection
trigger_words: MEA, electrophysiology, network state, EIU, compositional analysis, firing rate, ISI, in-vitro, 4-AP, optogenetic, drug response
---

# EIU Compositional Analysis of Neuronal Network State Transitions

**Source**: Auslender, Heydari, Malkoç, Zaccaria, Bozzi & Pavesi (University of Trento), "A Time-Resolved Framework for Quantifying Neuronal Network State Transitions", arXiv:2610.08392 (Oct 2026, q-bio.NC, v1 draft).

## Core Insight

Conventional electrophysiology metrics (mean firing rate, burst indices) compress temporally rich network responses into static aggregates, masking transient dynamics. The EIU (Excited–Inhibited–Unchanged) framework instead classifies **each electrode × each short time segment** against a data-driven control null, then tracks the culture's trajectory through a compositional simplex. This amplifies subtle intervention effects (Cohen's d increases, largest for MFR) while preserving direction and temporal evolution that pure divergence measures (D_KL) lack.

## The EIU Pipeline (step by step)

### 1. Data structuring
- Spike trains S_{i,n} per channel i (MEA: 60 electrodes typical, 10–20 kHz).
- Baseline window T_b before intervention; post-intervention divided into N windows T_j; **each window further split into K segments τ** (must contain enough spikes for ISI density estimation).
- Exclude electrodes with firing rate < 0.1 s⁻¹; exclude recordings with < 10 active electrodes.

### 2. Discriminators ξ (any measurable activity statistic)
| Discriminator | Interpretation | Sensitivity profile |
|---|---|---|
| MFR | mean spikes/channel/time | directional, low sensitivity |
| Mean ISI µ (log-domain) | characteristic firing timescale | directional, moderate |
| Peak ISI p (mode of log-ISI PDF) | dominant firing regime | more sensitive than MFR |
| D_KL (ISI PDF divergence) | full distributional change | highest raw discrimination, no direction |

ISI PDFs estimated per channel in log domain X = log₁₀(ISI), bin width δX = 0.1, KDE with Epanechnikov kernel.

### 3. Normalized change metric (symmetric contrast)
```
Δξ = (ξ^(j) − ξ^(b)) / (ξ^(j) + ξ^(b))
```
Scale-free, symmetric, ∈ [−1, 1] for non-negative ξ, stable when baseline ξ^(b) is small (unlike relative change).

### 4. Data-driven thresholds from vehicle control
- Pool Δξ values across **vehicle/control cultures** → empirical null distribution of intrinsic network variability.
- Thresholds: 95th percentile → Δth↑, 5th percentile → Δth↓. Recompute per time window if vehicle itself drifts (e.g., recording fatigue).

### 5. Electrode-segment classification
```
state = E  if Δξ > Δth↑   (excited)
       I  if Δξ < Δth↓   (inhibited)
       U  otherwise        (unchanged)
```

### 6. Compositional state vector per electrode, per window
```
s^(i,j)_γ = Σ_k 1[Δξ^(i,j,k) ∈ γ] / K,   γ ∈ {E, I, U},   Σ_γ s_γ = 1
```
Culture-level: s̄_j = mean over electrodes → point on 2-simplex. Barycentric 2D projection:
```
X = E + U/2,   Y = (√3/2)·U
```

### 7. Scalar summary metrics
- **Responsiveness**: R = E + I ∈ [0,1] — overall prevalence of change regardless of direction.
- **E-I balance**: η = log(E/I) — direction of change (faster- vs slower-spiking dominance).

### 8. Time-resolved trajectories
Recompute EIU at successive windows → trajectory of each experimental group through the simplex; static (whole-period) composition is the endpoint summary.

## Key Experimental Findings

1. **4-AP (K⁺ channel blocker, expected excitatory)**: 10/100 µM produced activity *reduction* — initial modest change then progressive MFR decline (desensitization-like/homeostatic suppression), reversible 24 h after washout. Aggregate MFR alone would miss this nonmonotonic temporal profile.
2. **Optogenetic ArchT inhibition**: post-illumination trajectory toward *excited* state (faster spiking) — compatible with rebound firing; R increases over 30 min.
3. **Bicuculline benchmark (independent lab, mESC DT/VT cultures)**: all four compositions (pure DT, pure VT, 80:20, 50:50) respond strongly but **converge to different response plateaus** — cell-type composition shapes the resulting network state, not just response presence.
4. **Effect-size analysis**: EIU transformation raises Cohen's d for µ (mean ISI) and MFR substantially; D_KL already strong → no further gain (bounded R saturates near 1 for strongly separated conditions).

## When EIU helps vs. doesn't

- ✅ Small-to-moderate, temporally persistent responses; heterogeneous electrode populations; dose-response discrimination; transient rebounds.
- ⚠️ Strongly separated conditions: gain saturates; value shifts to characterizing *direction and trajectory* rather than boosting d.
- The framework is metric-agnostic: it amplifies even conventional MFR — the improvement comes from *representation*, not from a special feature.

## Pitfalls

- **Threshold provenance matters**: thresholds must come from a genuine vehicle/control condition; reusing the intervention group's own variability inflates false U.
- **R saturation**: R = E+I is bounded; do not interpret flat R at high values as absence of further change.
- **D_KL direction-blindness**: always pair divergence with η or µ/p shifts for physiological interpretation.
- **Segment length τ**: too short → unreliable ISI PDF; too long → smears transients. Rule: enough spikes per channel-segment for stable KDE.
- **Log-domain ISI**: bimodal burst/intra-burst structure means arithmetic-mean ISI is misleading; all statistics in log₁₀ domain.

## Reuse Templates

### MEA/drug-screening assay
Baseline → dose ladder → per-window EIU trajectory → R(t), η(t) curves. Distinguish desensitization (R decays while η persists) from washout recovery (retest 24 h).

### Cross-lab/standardized benchmark validation
Same perturbation across culture compositions: compare **plateau positions** in simplex, not just significance.

### Extension to other modalities
The recipe (baseline window, control-derived thresholds, per-channel per-segment 3-way classification, simplex trajectory) transfers to calcium imaging (event rate as discriminator), EEG channel-level drug response, and any before/after multi-sensor perturbation experiment.

## Math Summary

- Contrast: Δξ = (ξ_j − ξ_b)/(ξ_j + ξ_b)
- State fractions: s_γ^(i,j) = (1/K)·Σ_k 1[Δξ^(i,j,k) ∈ γ]
- Culture vector: s̄_j = (1/N_ch)·Σ_i s^(i,j), s̄ ∈ Δ² (2-simplex)
- Responsiveness R = E + I; E-I balance η = log(E/I)

## References

- arXiv:2610.08392 — full pipeline with 4-AP, ArchT optogenetic, bicuculline benchmark datasets
- Maccione et al. PTSD spike detection (Precise Timing–Spike Detection) for MEA preprocessing
- Crocco et al. mESC DT/VT culture benchmark dataset (independent-lab validation)
- Related compositional-data visualization: barycentric simplex projection (Aitchison geometry)
