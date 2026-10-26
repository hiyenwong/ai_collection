---
name: longitudinal-fmri-network-reconfiguration-aging
description: Use for longitudinal fMRI connectivity aging analyses.
category: ai_collection
---

# Longitudinal Multi-Network fMRI Reconfiguration in Adult Aging

**Source**: T. Liu, W. Dong, H. Zheng, D. Liang, Z. Hu, G. Cheng, N. Zhang (SIAT CAS / Peking Univ Shenzhen Hospital), arXiv:2610.24433 (q-bio.NC, Oct 2026). Cohort: AABC Release 2, 852 adults (baseline 36-89y), 2,220 sessions, 8,727 session-state rows, median follow-up 5.5y, 4 states (REST, CARIT Go/NoGo inhibitory control, FaceName associative memory, visual-motor). Code: github.com/tingshanL/four-state-fmri-aging.

## When to use

- Longitudinal (within-person) functional-connectivity analysis over multi-year follow-up, especially multi-state (rest + task) designs.
- Aging/lifespan FC studies where covariance decline could be a BOLD-amplitude artifact rather than a coupling change.
- Choosing an amplitude normalization for connectivity (correlation vs signal-normalized vs total-amplitude) and needing to know which conclusions depend on that choice.
- Testing whether a network-level effect recurs across brain states or is state-specific.

## Core representations (methodological core)

1. **Log-scale covariance per network**: L_k = log C_k, where C_k = mean full-covariance over distinct parcel pairs within network k (10 networks from HCP-MMP1.0 360 parcels via Ji et al. 2019 assignment).
2. **Common level + relative profile (compositional split)**: G = (1/10)Σ_k L_k; R_k = L_k − G. R is a centered log-ratio (Aitchison): removes any multiplicative scale shared across networks while keeping relative balance; Σ_k R_k = 0 per observation. Fit R in 9 orthonormal Helmert coordinates (isometric log-ratio basis) with unrestricted residual covariance, then transform back to network contrasts.
3. **Signal normalization**: C_k^STD = C_k / P_k, with P_k = mean product of released (noise-removed) signal amplitudes a_p over distinct parcel pairs — a network-level amplitude-standardized covariance, NOT a mean Pearson correlation.
4. **Candidate total normalization**: t_p = sqrt(a_p² + n_p²) (signal + estimated noise, additive, uncorrelated); P_k^TOT from t_p t_q products. Diagnostics: parcel-pair ratios C_pq/(a_p a_q) fall outside [−1,1] but C_pq/(t_p t_q) all fall inside, and adding diag(n_p²) restores positive semidefiniteness — evidence the released covariance diagonal excludes unstructured noise variance.
5. **Attenuation identity**: L_k^TOT = L_k^STD + H_k with H_k = log(P_k / P_k^TOT) ≤ 0; it carries through G, R, and the FP contrast, so under shared GLS weights the difference between representations equals the H coefficients exactly.

## Longitudinal model

- Baseline age and elapsed follow-up enter as SEPARATE fixed effects (cross-sectional age differences ≠ within-person change); both in 5-year units, age centered at cohort mean.
- Joint 4-state design: state + baseline-age×state + elapsed-time×state (sum-coded); state-specific slopes are linear combinations, equal-state slope is their mean.
- GLS with Gaussian working covariance V_i = I + τ_P 11^T + τ_PS Z_i Z_i^T (participant + participant×state); sandwich uncertainty clustered at PEDIGREE level (related participants = one cluster).
- Wald χ² joint tests; Bonferroni simultaneous 95% intervals across the 4 states; 4,999 Gaussian pedigree-cluster multiplier draws for max-Wald / max-|t| familywise control across comparator networks; Holm within pre-declared families.
- Robustness battery: per-site slopes and leave-one-site-out, single-scanner subset (822/852), partial vs full covariance, cortical-thickness adjustment with between/within-person split, omit-one-reference-network re-computation, baseline-age moderation.

## Key results

- Native common covariance declined 7-11% per 5y in ALL four states (χ²₄=47.69, p=1.1e-9); slopes −0.105/−0.068/−0.085/−0.116 log-units/5y (REST/CARIT/FaceName/visuomotor).
- Signal pair amplitude −9.4%/5y equal-state (simultaneous CI 1.9-16.4%); noise pair amplitude flat (−0.7%, CI −5.0..+3.8%); paired contrast: signal declines MORE than noise (−0.092 log-units/5y, CI −0.177..−0.008).
- Common-level trajectory is normalization-dependent: near zero under signal normalization (χ²₄=4.59, Holm p=.332) but −4 to −7%/5y under candidate-total normalization (χ²₄=39.26, Holm p=1.8e-7); the two differ (p=.015). A correlation-type denominator (retains noise) can show a common decline that signal-normalization does not.
- Network-relative reconfiguration: time×network χ²₉=43.90 (p=1.5e-6); state-dependent time×network×state χ²₂₇=112.00 (p=2.6e-12). FP most positive (+0.058 log/5y), Language +0.037; Auditory −0.045, Visual1 −0.042. Profile contracts: across-network SD ratio 0.926 after 5y (0.896-0.960) — networks starting low rise, high fall (partial convergence, related to but distinct from dedifferentiation).
- **FP-relative shift (FP minus mean of other nine networks) positive in EVERY state**: +0.081/+0.063/+0.045/+0.070 log-units/5y ≈ +5-8%/5y (χ²₄=37.08, p=1.7e-7); magnitude differs across states (p=.0052); FP's own uncentered level also rises (+0.070, CI +0.005..+0.134) — the shift is not merely relative decline of comparators. Robust under both normalizations, at every site (+0.056..+0.077), leave-site-out, single-scanner, thickness-adjusted (slope-vector norm +2.1%, difference ns), and partial covariance (smaller but positive).
- **Cognition**: NO within-person FP↔FluidIQ coupling (χ²₄=5.63, p=.228) although between-person association exists (χ²₄=36.58, p=2.2e-7) — the trajectory is established, its FUNCTION (compensation/scaffolding) is not; testing compensation needs repeated task-relevant cognitive measures.
- FP cortical thickness declines less than other networks (FP-relative +0.0156 mm/5y, p=2.9e-9); thickness adjustment does not explain the functional trajectory.

## Pitfalls encoded

- Covariance-based FC conflates coupling and amplitude; correlation removes amplitude but keeps noise in the denominator — either choice can manufacture or mask "aging decline". Report the choice and test both.
- Cross-sectional age slopes are not longitudinal slopes; model baseline age and elapsed time separately.
- Task-state covariance may include shared task-evoked responses (the AABC release does not regress them before covariance estimation) — interpret state differences with care.
- A relative (compositional) FP rise can coexist with declining FP segregation: segregation contrasts within- vs between-network connectivity, the profile compares within-network covariance ACROSS networks.
- FP was characterized after the profile results in the same cohort; its prominence should be confirmed in an independent sample.

## Activation

longitudinal fMRI, functional connectivity, aging, BOLD amplitude, frontoparietal network, compositional data analysis, centered log-ratio, network reconfiguration, within-person change, pedigree-clustered inference, amplitude normalization
