---
name: tii-hierarchical-brain-dynamics-mindfulness
description: Sliding-window TII decomposes intervention brain effects.
created: 2026-10-17
source_paper: "arXiv:2610.20854 - Two dissociable axes of brain hierarchical dynamics track universal and population-specific effects of mindfulness"
---

# TII Hierarchical Brain Dynamics & Mindfulness (arXiv:2610.20854)

**Use when**: analyzing time-varying brain network dynamics from EEG/MEG beyond time-averaged connectivity, quantifying temporal irreversibility / non-equilibrium dynamics, evaluating intervention (meditation, training, therapy) effects on brain dynamics, or building hierarchical-dynamics trajectories with interpretable scalar descriptors.

## Core Method: Sliding-Window Temporal Irreversibility Index (TII)

For each pair of ROI time series (x, y), bivariate TII at maximum lag M (following Hindriks et al.):

ξ(x,y,M) = 1/(M·(1−r₀²)) · Σₘ [rₘ(x,y) − r₋ₘ(x,y)]

where rₘ = cross-correlation at lag m, r₀ = zero-lag correlation. TII > 0 signals time-directed (non-equilibrium) coupling.

**Pipeline**:
1. EEG → source reconstruction (minimum-norm estimates) → Schaefer-100 parcellation, 7-network (Yeo) ordering; regional time series downsampled to 250 Hz.
2. TII matrices (100×100 ROIs) in sliding windows of duration **5M samples, step M/2 (90% overlap)**.
3. Aggregate to **28 inter-network couplings** (7 Yeo networks) → n_windows × 28 trajectory per participant × condition.
4. Six maximum lags: M ∈ {40, 72, 152, 252, 352, 600} ms, spanning N1 sensory (39–72 ms) → slow cognitive transitions (600 ms).
5. Node-level variant: row-sums of the 100×100 matrix → n_windows × 100 regional trajectories.

## Three Orthogonal Trajectory Descriptors

From each TII trajectory (per channel, averaged over 28 network pairs):
- **Temporal mean (mean_t)** = hierarchical depth — average TII magnitude.
- **Temporal variance (var_t)** = exploratory breadth — breadth of state-space exploration.
- **Lag-1 autocorrelation (autocorr)** = temporal persistence.

Demean time series per segment before var_t/autocorr to prevent baseline-drift contamination when concatenating segments.

## Main Findings (n=141, three cohorts)

Cohorts: cross-sectional Isha Yoga (n=96: ADV median 4,850 h / NOV 1,450 h / CNT 0 h); longitudinal 8-week MBSR healthy (n=28); longitudinal 8-week CoMET trauma-exposed PTSS (n=17).

**Three-part decomposition**:
1. **Hierarchical depth = invariant setpoint**: no differences across expertise (q>0.29), unchanged by either intervention (q>0.15). Triple null → selective sensitivity of the other two axes.
2. **Exploratory breadth = universal trait-stabilization axis**: monotonic expertise gradient (ADV < NOV ≤ CNT) at 4/6 lags after FDR (152/252/352 ms q=0.018; 600 ms q=0.022); pan-cerebral (all 28 network pairs at 152 ms); **dose-dependent** with log₁₀(1+hours) (ρ≈−0.25 to −0.33, 4 lags, up to 15,000+ h).
3. **Temporal persistence = bidirectional attractor axis, population-specific**: decreased in healthy MBSR (all 6 lags, peak 72 ms q=0.002) but INCREASED in trauma-exposed CoMET (40/252/352 ms q≈0.02) — convergence toward a balanced dynamical regime. Unobservable in cross-sectional experts (already stabilized at equilibrium).

Spatial signature: healthy = pan-cerebral flexibilization (26/28 pairs); trauma = focal — dorsal-attention/sensorimotor/executive/default-mode + intra-limbic renormalization of hypervigilance circuits. Same MBI protocol engages qualitatively distinct mechanisms by clinical baseline.

## Joint 5-State HMM: Mechanistic Dissociation

Joint HMM (K=5 by free-energy + Hamming-distance consistency across inits; n=141, 186 subject×condition segments) on TII trajectories at M=152 ms:
- States are highly persistent (self-transition 0.67–0.84), sparse inter-state transitions.
- **Exploratory breadth is a state-occupancy phenomenon**: FO of transient integrative State 3 correlates ρ≈+0.60 with breadth; persistent anchor States 2/4 correlate ρ≈−0.60 (all P<0.001, 152–600 ms).
- **Depth & persistence are NOT captured by static fractional occupancy** — they live in within-state dwell-time distributions, transition rhythms, phase relationships.
- Intervention effects concentrate ONLY on low-occupancy States 1↔2, in OPPOSITE directions: MBSR ↓State1/↑State2 (q<0.05); CoMET ↑State1/↓State2 (uncorrected P<0.05). State 3 (trait breadth substrate) unmodulated by 8-week interventions → trait effect reflects long-term consolidation, not acute practice.
- Evaluate FO-descriptor associations only in the cross-sectional cohort (one observation/subject) to avoid paired pre/post non-independence; FDR across 90 tests (5 states × 6 lags × 3 descriptors).

## Behavioral Anchor

Longitudinal Δ in BOTH axes selectively track the **Acting-with-Awareness facet** of FFMQ (breadth 600 ms ρ=+0.47; persistence 352 ms ρ=+0.48), no other facet survives; healthy and clinical participants lie on a SINGLE regression slope — the behavioral anchor is invariant to clinical status.

## Statistics Protocol

- BH-FDR everywhere; correction unit stated per analysis; BH valid because dependent tests across lags/pairs are positively correlated (BY unnecessarily conservative).
- Cross-sectional contrasts: Welch's t-test + Cohen's d; primary contrast ADV vs CNT (NOV as visual intermediate reference to avoid multiplicity inflation).
- Longitudinal contrasts: paired sign-flip permutation (robust for small n=17, no normality assumption).
- Robustness: autocorr effect verified against sliding-window overlap variation.

## Pitfalls
- Single template-reference geometry across subjects to prevent channel-reconstruction bias between sessions.
- Demean per segment before pooling, else second-order descriptors inherit drift.
- Don't attribute HMM state FO to paired longitudinal samples without independence handling.
- Cross-sectional expertise designs cannot see intervention-attractor effects already at equilibrium (persistence axis) — need longitudinal design.

## References
- arXiv:2610.20854; Hindriks et al. (TII definition); Yeo 7 networks / Schaefer-100; FFMQ five-facet mindfulness questionnaire
- Related skills: hierarchical-brain-criticality, nonequilibrium-brain-dynamics-physics, metastable-neural-states-event-segmentation, brain-oscillation-synchronization-framework
