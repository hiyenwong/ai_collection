---
name: adaptive-fractional-state-cortical-dynamics
description: "分析皮层异常扩散/层级动力学时用。AF态双分数均场理论。"
metadata:
  arxiv_id: "2609.37355"
  published: "2026-09-29"
  authors: "Brendan Harris, Pulin Gong"
  source: "arXiv q-bio.NC, cond-mat.dis-nn, physics.bio-ph"
  tags: [computational-neuroscience, fractional-calculus, anomalous-diffusion, neural-dynamics, visual-hierarchy, mean-field-theory, neuropixels]
---

# Adaptive Fractional State: Cortical Dynamics Across the Visual Hierarchy

**arXiv 2609.37355** (2026-09-29) — Harris & Gong (University of Sydney). Combines Neuropixels recordings from six mouse visual areas (69 sessions, 41 mice), biophysical spiking circuit modeling, and a generalized mean-field theory to identify a unified cortical working regime.

**Activation keywords**: neuroscience, brain network, neural dynamics, computational neuroscience, anomalous diffusion, fractional dynamics, cortical hierarchy, Neuropixels, LFP analysis, superdiffusion, long-range memory, E:I balance

## Core Innovation

1. **AF state definition**: heavy-tailed **superdiffusive** fluctuations, **long-range temporal memory**, and **oscillations** coexist in the same cortical regime — previously studied only in isolation (Gaussian mean-field / Lévy-driven / colored-noise / oscillatory models each capture one piece).
2. **Bi-fractional mean field (bFNS)**: extends fractional neural sampling with *simultaneous* fractional spatial derivative (α → heavy tails, non-Gaussian jumps) and fractional temporal derivative (β → power-law memory) plus momentum coupling (γ → oscillations). One compact model unifies 5 established stochastic descriptions as limiting cases.
3. **Hierarchy of dynamical regimes**: the classical "hierarchy of timescales" is incomplete — areas move along a *joint axis* in the (a,b) plane: higher visual areas have weaker superdiffusion (a: 0.62→0.51) but stronger temporal memory (b: -1.75→-1.57), anticorrelated (Kendall τ_a=-0.40, τ_b=+0.60 in L2/3).
4. **Circuit mechanism**: the hierarchical shift is reproduced by progressively weakening effective inhibition (synaptic I:E ratio δ) in a spiking circuit near the localization–delocalization transition.

## Key Measurable Exponents

| Exponent | Definition | Method | L2/3 VISp value |
|---|---|---|---|
| Diffusion a | MAD(τ) ∝ τ^a | Mean absolute deviation of LFP increments (MAD robust to heavy tails; use 0.8–8 ms lag window) | 0.62 (superdiffusive; Brownian=0.5) |
| Spectral b | PSD ∝ f^b | Aperiodic fit after removing θ (7Hz) & γ (55Hz) peaks | -1.75 (shallow; Brownian=-2) |
| Variability c | Fano F(τ) ∝ τ^c | Spike-count power-law growth at windows >0.01s | 0.19 (super-Poissonian) |

**Critical inference pattern**: superdiffusion (a>0.5) + shallow spectrum (b>-2) is *contradictory for a Gaussian process* (Gaussian superdiffusion requires b≤-2). The resolution: heavy-tailed increments (excess kurtosis κ=0.35 vs. Fourier-surrogate 0, p<1e-20) generate superdiffusion *without* positive increment correlations, while long-range memory produces the shallow spectrum. Non-Gaussianity and non-Markovianity must both be present.

## bFNS Equations

On position x and auxiliary momentum p:

```
ᶜD_t^β x = -η∇Ṽ_α + γp + η^(1/α) ξ_{α,β}
dp/dt = -γ∇Ṽ_α
```

- α ∈ (1,2]: spatial fractional order — lowering α increases heavy-tailed jumps → superdiffusion
- β ∈ (0,1]: Caputo temporal fractional order — lowering β strengthens power-law memory → subdiffusive competition, shallower spectrum
- γ: momentum coupling → oscillations
- Ṽ_α: effective potential built so the process samples target distribution π(x)
- ξ_{α,β}: linear fractional stable drive

Limiting cases (the unification):
- α=2, β=1, γ=0 → Gaussian–Markovian diffusion (classical mean field)
- α=2, β=1, γ>0 → oscillatory Gaussian dynamics
- α<2, β=1, γ=0 → Lévy-driven superdiffusion
- α=2, β<1, γ=0 → fractional Langevin power-law memory
- α<2, β<1, γ>0 → full AF regime

**Empirical diffusion law (unconfined)**: a ≈ 1 - α/2 + β/2. Spatial fraction raises a; temporal fraction lowers it. Hierarchy direction = lowering β (time-fractional axis dominates), not changing α.

## Workflow (replicable analysis pipeline)

1. **Measure exponents on recordings** (LFP + spikes per area/layer):
   - a: fit MAD(τ) power law at short lags (0.8–8 ms); MAD ≫ MSD for heavy tails (finite first moment, divergent variance breaks MSD)
   - b: decompose PSD into oscillatory peaks + aperiodic component; fit aperiodic slope
   - c: Fano factor F(τ) at long windows; power-law growth = long-range dependence
   - Heavy-tail check: pooled step-size excess kurtosis vs phase-randomized FT surrogates (sign test across sessions)
2. **Locate areas in the (a,b) plane**; correlate ranks with anatomical hierarchy score (per-session Kendall τ, report across-session median)
3. **Circuit model sweep**: spatially-embedded E/I spiking network with adaptation; sweep I:E ratio δ × adaptation Δg_K; recompute exponents of synaptic input currents. Transition regime (between localized wave packets and delocalized spiking) reproduces AF signatures without parameter tuning
4. **Mean-field neuron**: fit target stable distribution (tail index 1.5, scale 0.14, location 0.2 from circuit currents); drive single fluctuation-driven neuron with bFNS input; reproduce subthreshold distribution, ~8.8 Hz sparse firing with mean 12 mV below threshold, and Fano scaling

## Implementation Notes

- **MAD increment statistic** (Python sketch):
  ```python
  def mad_exponent(x, lags):
      # a>0.5 superdiffusive; robust for infinite-variance increments
      return np.array([np.mean(np.abs(x[lag:] - x[:-lag])) for lag in lags])
      # fit log(mad) vs log(lag) over 0.8–8 ms
  ```
- **Fano factor power law**: compute F(τ) over window grid 0.01–1 s; fit log-log slope at long windows
- **Caputo derivative** β<1: weights past increments via slowly decaying kernel; relaxation becomes power-law instead of exponential
- Causal dissociation of α vs β effects on exponents: α acts on jump statistics, β acts on relaxation/spectrum; they jointly determine a — measure both, don't collapse to one timescale

## Pitfalls

- Do NOT use MSD/DFA for heavy-tailed increments — variance diverges; use MAD (first-moment) scaling
- A single characteristic timescale per area misses the joint (a,b) displacement; the two exponents move in *opposite* directions up the hierarchy
- The L2/3 hierarchical axis does not survive to deep layers: spectral correlation vanishes by L6 (τ=-0.07) and diffusion correlation *reverses sign* (τ=+0.33) — layer specificity matters
- E:I ratio is one sufficient axis, not uniquely identified: synaptic kinetics, connectivity, adaptation can produce related displacements; anatomy (PV density, inhibitory interareal fraction) only constrains direction
- Circuit model Fano scaling is *tempered* by oscillations at long windows while experimental data show power law to 1 s — possible heterogeneity/intracellular dynamics not captured

## Applications & Extensions

- Reframe any cortical-hierarchy timescale analysis as a 2D (a,b) working-regime map (areas, layers, behavioral states, task demands on same axes)
- Testable prediction: intracellular recordings across hierarchy should show preserved heavy-tailed step statistics but strengthened temporal persistence toward higher areas, strongest in L2/3
- Exploration–exploitation interpretation: primary cortex = rapid reconfiguration via large excursions; higher areas = accumulation/maintenance via memory. Optimal balance should shift with behavioral state — testable with task/anaesthesia
- Anomalous-diffusion diagnostics generalize to EEG/MEG/Ca imaging: measure (a,b,c) triple instead of single timescale constants
- Connect to sampling-based computation: heavy-tailed motion supports multimodal landscape sampling; memory stabilizes trajectories and extends fading memory

## Related Skills
- `latency-driven-heterogeneity-visual-encoding` (hierarchical timescales)
- `nonequilibrium-brain-dynamics` (criticality frameworks)
- `predictable-mean-field-chaos-rnn` (mean-field reductions)

## Source
- arXiv: 2609.37355 — data/code availability stated in paper (public Neuropixels datasets: Allen Institute Visual Coding + independent set; bFNS implementation in Methods XI.5)
