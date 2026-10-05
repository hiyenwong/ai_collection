---
name: heterogeneity-sr-liquid-computing
description: Quenched disorder structure (not magnitude) controls SR and LSM performance in FHN reservoirs. Use for heterogeneous reservoir design.
category: ai_collection
---

# Heterogeneity-Enhanced Stochastic Resonance in Liquid-State Computing

Source: Nath & Yamakou, "Heterogeneity-enhanced stochastic resonance improves
liquid-state computing in delayed spiking neural networks" (arXiv:2609.27896,
nlin.AO, Sept 2026). FAU Erlangen / TU Graz.

## Core Thesis

Noise intensity D and quenched structural heterogeneity are **coupled control
parameters** of reservoir dynamics. The computational benefit of heterogeneity
is determined by the **distributional structure** of the disorder (how it
redistributes effective activation/propagation scales), NOT by its magnitude
alone. Well-chosen quenched disorder lets a liquid reach its most informative
state with **weaker stochastic forcing**.

## Model Setup (reusable spec)

- N=50 FitzHugh–Nagumo neurons, ε=0.03, a0=1.0, Watts–Strogatz small-world
  topology, no autapses.
- Synaptic input: diffusive delayed coupling
  `Isyn,i(t) = Σ_j Wij·gij·[vj(t−τij) − vi(t)]`
- Heterogeneity injected **per-edge**, separately for coupling strength gij
  and time delay τij, drawn from three families (all projected to admissible
  intervals g∈[0.005,0.05], τ∈[0,2.5]):
  1. Gaussian: (µg, σg) — symmetric, mean-preserving
  2. Bimodal: two Gaussians at µ±σ/2 — two-scale organization
  3. Shifted-exponential: (µg, λg⁻¹) — one-sided, NON-mean-preserving
- Subthreshold regime first: isolated-neuron forcing threshold Ath≈0.016;
  use A=0.015. ALSO verify the homogeneous (g,τ) network is silent without
  noise (map mean ISI first) — recurrent coupling alone can destabilize rest.
- Reference cuts: τ=0.3 for coupling sweeps; g=0.0025 for delay sweeps.
- LSM: fixed reservoir + ridge-regularized linear readout, 5-step-ahead
  forecasting of weak aperiodic input; noise-optimized error
  RMSEmin(σg) = min_D RMSE(σg, D).

## Key Findings

1. **SR ↔ LSM performance link**: normalized zero-lag input–output coherence
   Q̄ inversely tracks readout RMSE across noise amplitude. The useful noise
   regime is where responses stay correlated with input temporal structure,
   not merely where threshold crossings are frequent.
   (Example: D=0.022 → RMSE 0.00721 vs D=0.006 → 0.00800, D=0.042 → 0.00820.)
2. **Gaussian coupling disorder**: broadens the strong-SR region in (µg, σg)
   space; under aperiodic drive it shifts optimal noise window toward weaker D
   and slightly reduces RMSEmin. Dominant effect under periodic forcing is
   amplitude amplification.
3. **Bimodal coupling disorder**: LARGEST RMSEmin reduction; shifts resonance
   ridge toward weaker noise. Interpretation: coexistence of weak-coupling
   sectors (retain local sensitivity) + strong-coupling pathways (recruitment/
   redistribution) — a two-scale susceptibility organization.
4. **Shifted-exponential disorder**: non-monotonic — slight benefit at
   intermediate scale, marked degradation at large scales. Root cause: it is
   one-sided and non-mean-preserving, so increasing σg also shifts mean
   coupling toward less responsive regions. Lesson: a "heterogeneity"
   parameter can secretly be a location parameter.
5. **Delay heterogeneity**: neither intrinsically constructive nor destructive.
   Homogeneous delay-response landscape is strongly structured (alternating
   max/min); στ smooths it. Enhancement occurs when mean delay sits in a
   low-response band; suppression when it sits in a high-response band.
6. Under aperiodic forcing, delay variation pushes much of (g,τ) space into
   deterministic spiking — for LSM experiments they fixed τ=0.3 and varied
   only coupling heterogeneity.

## Design Principles for Heterogeneous Reservoirs

- Prefer **symmetric, mean-preserving** disorder (Gaussian/bimodal) over
  one-sided distributions when broadening coupling scales.
- **Bimodal (two-scale) coupling** is the strongest enhancer in this regime —
  cheap recipe: sample half the edges weak, half strong.
- Tune noise D and heterogeneity σ **jointly**: heterogeneity moves the
  optimal noise level; the pair (D, σ) should be optimized as a 2D landscape,
  not sequentially.
- Map the homogeneous (mean-coupling, mean-delay) response landscape FIRST;
  heterogeneity acts by distribution-weighted averaging over that landscape.
- Always check whether the heterogeneity parameter preserves the mean —
  otherwise observed effects conflate disorder strength with location shift.

## Measurement Protocol

- PSR probe: spectral response Q at forcing frequency ω (periodic subthreshold
  drive) → resolves resonance landscape.
- ASR probe: normalized zero-lag coherence Q̄ under weak aperiodic drive →
  correlates with readout quality.
- Report RMSEmin = min over D for each heterogeneity scale (lower envelope),
  plus the argmin D to track the optimal-noise shift.

## Related Skills

- `noisy-snn-learning` — noise as computational resource (training-side)
- `heterogeneous-synaptic-dynamics` — synaptic heterogeneity modeling
- `parametric-oscillator-reservoir-computing` — oscillator reservoirs
- `stochastic-resonance-tinnitus-review` — SR in neuroscience context

## Pitfalls

- Effects are distribution- and regime-dependent; do NOT claim "heterogeneity
  helps" generically — the paper's central negative result.
- PSR and ASR optima need not coincide (different signals/observables); match
  the probe to the use case.
- Projection to admissible intervals creates boundary mass; realized moments
  deviate from nominal ones when 3σ crosses a boundary.
