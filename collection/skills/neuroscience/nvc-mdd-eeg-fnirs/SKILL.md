---
name: nvc-mdd-eeg-fnirs
description: Use for resting-state EEG-fNIRS neurovascular coupling metrics in depression. GFP peak-locked HbT correlation analysis.
category: ai_collection
version: 1.0.0
tags:
  - neurovascular-coupling
  - major-depressive-disorder
  - eeg-fnirs
  - multimodal-neuroimaging
  - clinical-biomarker
  - resting-state
trigger_words:
  - neurovascular coupling depression
  - EEG fNIRS multimodal
  - NVC consistency coefficient
  - initial dip hemodynamic
  - MDD biomarker monitoring
  - GFP peak-locked analysis
author: Feng Yan, Xiaobin Wang, Yao Zhao, Shuyi Yang, Zhiren Wang
arxiv_id: "2506.11634"
date_added: "2026-09-27"
---

# Neurovascular Coupling Differences in MDD: Simultaneous Resting-State EEG-fNIRS

Methodology from arXiv:2506.11634 — "Differences in Neurovascular Coupling in Patients with Major Depressive Disorder: Evidence from Simultaneous Resting-State EEG-fNIRS" (Yan et al., Beijing Huilongguan Hospital/PKU + Tsinghua, 2025). Use when analyzing neurovascular coupling (NVC) from multimodal EEG+fNIRS, building depression biomarkers, or designing resting-state clinical neurophysiology studies.

## Core Idea

Neurovascular coupling (NVC) — neural activation → O2 consumption → vasodilation → CBF increase → HbO2 rise — is measurable **without task paradigms** by locking hemodynamic analysis to spontaneous EEG global field power (GFP) peaks. MDD disrupts the age-related maturation of NVC, and disruption scales with illness severity.

## Data & Cohort

- **206 recruited**: 134 MDD (DSM-5; acute/maintenance/stable phase) + 72 healthy controls (HC), stratified by age (HC split at 28y to match MDD age distribution).
- **After QC**: 74 retained (17 MDD HAMD>16 "MDD_1", 18 MDD HAMD≤16 "MDD_2", 22 young HC_1, 17 older HC_2) — **65% rejection rate**, mostly hair-coverage fNIRS signal loss (long hair/poor hygiene in severe MDD).
- **Paradigm**: 2-min eyes-open + 2-min eyes-closed resting state ×2; plug-and-play synchronized EEG-fNIRS, optodes concentrated on PFC (mPFC + frontoparietal junction + temporal).

## NVC Metric Pipeline (peak-locked correlation analysis)

1. **EEG preprocessing**: 0.5–40 Hz bandpass (EEGLAB pop_eegfiltnew), ICA artifact rejection, automated bad-channel detection (kurtosis).
2. **GFP peaks replace task-evoked P300** (oddball paradigms fail in severe MDD due to habituation/cognitive overload): GFP(t) = sqrt(Σ_i (V_i(t) − V̄(t))²), computed ONLY over channels under fNIRS coverage (Pz, P3, P4, P7, P8, PO3, PO4, Oz, O1, O2 excluded).
3. **Peak detection**: local maxima strictly greater than any GFP value in surrounding ±5 s; top 5 peaks per epoch.
4. **NVC consistency coefficient**: for each GFP peak, Spearman correlation between interpolated EEG activation and HbT (total hemoglobin) over the following 10 s → NVC_R(t); smooth (Savitzky-Golay).
   - **mNVC_R**: maximum correlation in window (must be a strict local max vs t±1); **mNVC_RT** its latency.
   - **Interpolation note**: interpolate EEG (not fNIRS) to optode positions — preserves fNIRS spatial detail.
5. **Initial dip** (oxygen-consumption phase, for subjects with mNVC_R>0): most negative correlation point BEFORE the NVC peak → **mID_R** (depth), **mID_RT** (timing). Reflects deoxygenation preceding vasodilation.
6. **Replenishment phase**: ΔmNVC_T = mNVC_RT − mID_RT (duration from dip to coupling peak); ΔmNVC_R = mNVC_R − mID_R (correlation gain).
7. **Statistics**: ANCOVA (Age, Gender covariates), estimated-marginal-means post-hoc with BH-FDR correction; partial correlations vs HAMD/HAMA controlling Age/Gender/Medication.

## Key Results

| Finding | Value | Condition |
|---|---|---|
| Age ↑ NVC consistency in HC (HC_2 > HC_1) | p_FDR=0.013, d=0.90 | Eyes-open |
| Age-NVC correlation present in HC, absent in MDD | r=0.253 (HC) vs r=−0.063 (MDD) | Eyes-open |
| Severity ↔ lower coupling consistency (partial r, ctrl age/gender/med) | −0.336, p=0.060 | Eyes-closed |
| Replenishment gain higher in older HC (HC_2 > HC_1) | p_FDR=0.004, d=1.07 | Eyes-open |
| MDD replenishment attenuated vs age-matched HC | p_uncorr≈0.05, d≈0.63 | Eyes-open |
| Initial dip: no significant group differences | p=0.24–0.96 | both |

- **Age-related NVC maturation is disrupted in MDD**: patients show intermediate values that don't differ from either HC group — the age-consistency slope flattens.
- **Deficit is at the neurovascular interface, not neural activity**: EEG topography differences alone (MDD_2) don't explain NVC changes.
- **Condition-specificity**: nearly all significant effects in **eyes-open** rest — arousal acts as a "stress test" revealing latent NVC impairment; eyes-closed rest is less sensitive.
- mID_R trended positively with HAMA (anxiety → deeper initial oxygen consumption, r=0.318, p=0.100).

## Clinical & Methodological Implications

1. **Biomarker**: wearable EEG-fNIRS NVC consistency is a candidate severity-monitoring biomarker and recovery-trajectory tracker (complements EEG microstate findings in drug-naïve MDD).
2. **Design rule**: resting-state + eyes-open challenge > passive eyes-closed rest or task paradigms for psychiatric NVC studies (obviates attention confounds in severe patients).
3. **Mechanism**: consistent with endothelial dysfunction and reduced vascular elasticity in depression (SSRI/SNRI vasodilation is a partial confound; partial correlations survived medication control but cross-sectional design can't fully separate disease from medication effects).
4. **Honest limitations**: 65% data rejection (hair → gender imbalance in retained MDD sample); small final N (74); most severity correlations are trend-level (p≈0.06–0.10); ANCOVA covariates don't fully deconfound medication (94%/83% medicated).

## Related Work

- [[eeg-brain-connectivity-bci]] — EEG connectivity metrics
- [[interpretable-eeg-biomarkers-parkinsons]] — other clinical EEG biomarkers
- [[eeg-tinnitus-biomarker-robustness]] — biomarker robustness methodology
- [[atoms-of-thought-eeg-microstates]] — microstates converge with GFP-peak NVC analysis

## Source

arXiv:2506.11634 — https://arxiv.org/abs/2506.11634
