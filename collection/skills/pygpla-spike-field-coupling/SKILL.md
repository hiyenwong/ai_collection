---
name: pygpla-spike-field-coupling
description: "Multivariate spike-LFP coupling via GPLA SVD and RMT testing"
category: neuroscience
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [neuroscience, electrophysiology, spike-field-coupling, phase-locking, LFP, random-matrix-theory, population-coding, high-density-recording]
    related_skills: [hermes-brain-connectivity, mle-toolbox-eeg-meg, vanillasort-spike-sorting, spike-forecast-behavioral]
trigger: spike-field coupling, spike-LFP, phase locking value, PLV, PPC, generalized phase locking, GPLA, gPLV, LFP phase, high-density electrophysiology, Neuropixels, multichannel coupling, population-level coupling, coupling matrix, low-rank coupling modes, Marchenko-Pastur, random matrix theory significance test, spike-triggered LFP, complex coupling matrix SVD, jitter surrogate, same-contact bias, channel whitening
---

# PyGPLA: Generalized Phase Locking Analysis for Multivariate Spike-Field Coupling

**Source**: "PyGPLA: A Python Package for Generalized Phase Locking Analysis" — Amir Khani, Christian Beste, Shervin Safavi (Donders Institute / TU Dresden / MPI Biological Cybernetics), arXiv:2610.26304 (q-bio.NC, 19 Oct 2026). Python implementation of GPLA (Safavi et al., eLife 2023); package on PyPI, docs on Read the Docs.

## When to Use

Use when analyzing **spike-LFP coupling in high-density recordings** (many channels × many units) where pairwise measures (PLV, pairwise phase consistency) explode combinatorially; when you need to know **whether a neural population is coupled to the field, which channels/units contribute, and how their phases are organized** — not just that one channel-unit pair couples; when you want a **dimension-aware significance test** where more channels/units improve statistical power instead of multiplying comparisons.

## Core Method

1. **Analytic LFP**: band-pass filter + Hilbert transform per channel → L_f(t) = a_f(t)·e^{iφ_f(t)}. (Upstream of the package — filter bandwidth trades phase meaning vs. temporal dynamics.)
2. **Complex coupling matrix**: Ĉ(f) ∈ C^{Nc×Nu}, each entry sums the analytic LFP **evaluated at every spike time** of that unit across trials. Normalizations: divide columns by total spike count N_m^tot (PLV-type) or by √N_m^tot (unit-variance scaling required by the analytical test).
3. **SVD**: C = UDV^H ≈ d1·u1·v1^H. Leading singular value **d1 = gPLV** (population coupling strength); **u1 = LFP vector** (per-channel contribution+phase), **v1 = spike vector** (per-unit contribution+phase).
4. **Phase convention**: SVD is invariant to global complex rotation → fix arg(mean(u1)) = 0, so mean spike-vector phase = overall spike-LFP phase lag. Optionally normalize gPLV by (Nc·Nu)^{-1/2} for cross-size comparability.

## Interpretation of the Spike Vector (why gPLV alone is not enough)

gPLV compresses the population to one scalar — it cannot distinguish coupling *organization*. The spike vector in the complex plane does:
- **Synchronous**: coefficients collapse to a common angle (shared preferred phase)
- **Sequential**: coefficients spread along an arc (progressive phase lag across units)
- **Clustered**: coefficients form a few subgroups (phase-locked subpopulations)
- **Uncoupled**: no stable phase pattern

Pooling spikes across units would destroy exactly this diversity.

## Statistical Testing (the key scaling insight)
- **Analytical RMT test**: with unit-variance (√N_m^tot) scaling + channel whitening, scaled squared singular values follow the **Marchenko-Pastur distribution** under the null; coupling is significant when singular values exceed the MP upper edge. **Dimensionality helps**: a larger matrix gives coherent low-rank signal more room to separate from the noise bulk — detection rate rises with units/channels while false positives stay ≤5%. This inverts the pairwise-testing regime where more comparisons only cost power.
- **Whitening (prerequisite for the analytic test)**: reduced-rank whitening — keep covariance eigenmodes explaining a fixed variance fraction (e.g. 99%), shared effective rank N_c^eff across trials (avoids over-amplifying small-eigenvalue noise); unwhiten u1 back to channel space for interpretation.
- **Surrogate tests**: multiple jittering schemes; also mitigates **same-contact bias** (spike and LFP on one electrode) by replacing suspect entries with jittered-spike estimates instead of discarding the unit/channel.
- Trial concatenation assumes approximate stationarity of coupling statistics; otherwise run GPLA per trial/condition or in sliding/event-locked windows.

## Package Layout

- `pygpla.api.gpla` — one-call high-level API (preparation → coupling → SVD → significance)
- `pygpla.preprocessing` (trial concat, temporal/unit selection, spike-count threshold, whitening), `pygpla.core` (coupling matrix, SVD, phase alignment, unwhitening), `pygpla.stats` (surrogates + RMT test), `pygpla.config` (dataclass parameter grouping)
- Core depends only on NumPy; SciPy optional; accepts plain NumPy arrays (no custom containers); ships Poisson/phase-locked spike-train simulators + reproducible figure scripts + tests.

## Workflow

1. Band-pass filter LFP at frequency f → Hilbert analytic signal (choose bandwidth for your science; not in package).
2. Select trials, time windows, units (spike-count threshold); select LFP channel subset if needed.
3. Optionally whiten (required for RMT test; keep unwhitening operator).
4. Build coupling matrix (choose 1/N vs 1/√N normalization deliberately).
5. SVD → gPLV, u1, v1; apply phase convention; unwhiten + rescale spike vector (reweight by spike counts).
6. Test significance (MP edge for analytic; jitter surrogates otherwise); interpret u1/v1 geometry, not just gPLV.

## Pitfalls
- Applying the analytic test without whitening + √N normalization invalidates the MP null.
- Same-electrode spike-LFP entries are biased by shared measurement/preprocessing — use the jitter-replacement mitigation.
- Narrowband phase is only meaningful if the band actually contains an oscillation; bandwidth choice is the main scientific degree of freedom.
- Don't compare raw gPLV across different matrix sizes — use the (Nc·Nu)^{-1/2}-normalized variant.
- gPLV high ≠ uniform coupling: check whether structure is sequential/clustered before aggregating units.

## References
- Khani, Beste, Safavi (2026). PyGPLA. arXiv:2610.26304.
- Safavi et al. (2023). GPLA: multivariate spike-field coupling. eLife (original MATLAB implementation + statistical theory, arXiv:2202.01309).
- Freund, Safavi et al. (2023). RMT significance testing for GPLA (analytical test).
- Vinck et al. (2010, 2012). Pairwise phase consistency / spike-field measures (the pairwise baseline GPLA generalizes).
