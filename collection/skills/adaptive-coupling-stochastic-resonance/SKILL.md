---
name: adaptive-coupling-stochastic-resonance
description: "Adaptive coupling (incl. memristive) as a flexible control knob for stochastic resonance in oscillator networks. Use when tuning noise-induced dynamics regularity."
category: ai_collection
tags: [stochastic-resonance, adaptive-coupling, memristive-coupling, bistable-oscillators, noise-induced-dynamics, oscillator-networks]
---

# Adaptive Coupling as a Stochastic-Resonance Control Tool

**Paper**: Stochastic resonance in adaptive dynamical networks (arXiv: 2610.11367, Vladimir V. Semenov, Saratov State University, nlin.AO, 2026-10-08)

## Trigger / Activation

Use when: modeling or controlling stochastic resonance (SR) in coupled bistable/excitable oscillator ensembles; designing adaptive (state-dependent) coupling in neural-mass or oscillator networks; tuning optimal noise intensity without changing the noise itself; memristive synapse models interacting with noise; deciding coupling topology (local vs global) for noise-induced regularity; sensory systems where SR is functional (auditory detection, mechanoreception).

**Keywords**: stochastic resonance, adaptive coupling, memristive coupling, bistability, SNR curve, optimal noise intensity, coupling topology, noise-induced oscillations, adaptive networks, short-term plasticity mapping

## Core Problem

Stochastic resonance — noise-enhanced response to weak subthreshold periodic forcing — appears across systems (ice-age models, lasers, chemical reactions, mammalian auditory system). Applications need three operations: **enhance** SR (detectors, energy harvesting), **suppress** SR (machinery fault detection, precision fabrication), and **shift** the optimal noise intensity D_opt to an accessible range. Classic control levers (time-delayed feedback, noise correlation time/PDF shaping, additive+multiplicative noise mix, static coupling strength/topology) all require modifying noise or hard-wiring topology. Question: does **adaptive coupling** — coupling strength that itself evolves with the oscillators' states — serve as a flexible SR control tool?

## Model

N = 100 overdamped bistable oscillators, each with independent additive white noise, common weak periodic forcing:

dx_i/dt = m·x_i − x_i³ + A·sin(ω_e t) + √(2D)·n_i(t) + f_i(x⃗, σ⃗)

with m = 0.25 (bistable, x*_{1,2} = ±0.5), A = 0.04 (subthreshold), ω_e = 0.005 (low). Heun integration, Δt = 0.001, t_total = 10⁶. SR measured by ensemble-averaged SNR(D) from per-oscillator power spectra: SNR = (S_max − S_min)/S_min with S_max at ω_e and S_min averaged over [0.75ω_e, 0.85ω_e] ∪ [1.15ω_e, 1.25ω_e] sidebands.

### Three coupling families studied

**1. Phenomenological adaptive local coupling (2 configs)** — coupling element state σ_i obeys

dσ_i/dt = γΔ_i/(1+Δ_i) − α·σ_i,  Δ_i = |x_i − x_{i+1}|  (or |x_i − (x_{i−1}+x_{i+1})/2|)

coupling term f_i ∝ (σ + σ_s)(x_neighbor − x_i). γ = adaptivity rate, α = decay ("forgetting"), σ_s = optional static component. Coupling strengthens with neighbor mismatch — a homeostatic/suppressive rule (analogous to short-term depression-then-reinforcement, or error-driven plasticity).

**2. Global adaptive coupling** — same σ dynamics with Δ_i = |x_i − mean_j x_j| and all-to-all coupling term.

**3. Memristive coupling** — physically motivated realization: cubic memristor window M(σ) = 1 + b·σ², coupling f_i = s/2·{M(σ_{i−1})(x_{i−1}−x_i) + M(σ_i)(x_{i+1}−x_i)}, state dσ_i/dt = (x_i − x_{i+1}) − α·σ_i. Here b = memristivity, α = forgetting effect, s scales BOTH static and adaptive components simultaneously.

The decay term −α·σ_i is essential: without it, coupling strength grows unboundedly (since γΔ/(1+Δ) ≥ 0 always) and one gets extreme multistability with initial-condition-dependent characteristics — structurally unstable, nonstationary, unphysical. With decay, growth (during mismatch) and relaxation (during in-phase intervals) balance into a stationary process.

## Core Findings

### 1. Adaptive coupling = full SR control knob

Tuning γ (adaptivity) alone can:
- **Enhance** SR: SNR peak rises (local: max at γ ≈ 10⁻²; global: resonant enhancement at γ ≈ 0.2).
- **Suppress** SR: further γ increase kills regularity (local: gradual at high γ; global: sharp drop after peak).
- **Shift D_opt over ~2 orders of magnitude**: local coupling D_opt from 2×10⁻³ (γ=10⁻⁴) to 8×10⁻² (γ=1).

The enhancement-vs-suppression is **resonant in γ** — an optimal adaptivity exists, exactly like static coupling strength, but γ is a physically different knob (it controls the *dynamics* of coupling, not its magnitude).

### 2. Mechanism: ⟨σ⟩ acts as an emergent static component

The coupling state oscillates with nearly constant amplitude around a mean ⟨σ⟩ that increases monotonically with both D and γ. The network responds to γ as if static coupling were being raised: adaptive dynamics ≈ static coupling with strength ⟨σ⟩(γ, D). This explains why all adaptive-coupling SR curves reproduce the known static-coupling phenomenology (enhance → saturate → suppress, with horizontal D-shift). The structure is effectively frozen; the adaptivity mostly sets the operating point.

### 3. Topology trade-off

Global coupling reaches **higher peak SNR** than local, but suppression after the peak is more abrupt. Local coupling degrades gracefully; global coupling is high-gain/high-risk.

### 4. Static + adaptive additivity

With σ_s = 0.2 fixed, increasing γ shifts D_opt up and suppresses SR — identical to further increasing σ_s at γ = 0. The two knobs act in the same direction (confirmed hypothesis of similar character). Practical use: SR already enhanced by static coupling can be suppressed by turning up adaptivity.

### 5. Memristive coupling: b's effect flips with total strength

- Low total coupling s = 0.01: increasing b (memristivity) **enhances** SR.
- High s = 0.1: increasing b **suppresses** SR.
- Both shift D_opt upward.
Reason: s scales static AND adaptive components together — enhancement needs weak static base, suppression dominates when the static base is already strong. Memristive hardware thus inherits the full SR control phenomenology.

## Reusable Recipes

### Recipe A — SR control matrix (what to tune for which goal)

| Goal | Local adaptive | Global adaptive | Memristive |
|------|---------------|-----------------|------------|
| Enhance SNR peak | γ ≈ 10⁻², moderate α | γ ≈ 0.2 | small s, increase b |
| Suppress SR | large γ (graceful) | γ past 0.2 (sharp) | large s, increase b |
| Shift D_opt up | increase γ (2 decades) | increase γ | increase b |
| Shift D_opt down | decrease γ / increase α | decrease γ | decrease b |

### Recipe B — simulation skeleton (Heun, ensemble SR)

```python
# N bistable oscillators, ring topology, adaptive coupling Eqs.(2)
for step in range(n_steps):
    # local mismatch
    Delta = np.abs(x - np.roll(x, -1))
    dsigma = gamma * Delta / (1 + Delta) - alpha * sigma
    # coupling force (static component sigma_s optional)
    f = 0.5 * ((np.roll(sigma, 1) + sigma_s) * (np.roll(x, 1) - x)
             + (sigma + sigma_s) * (np.roll(x, -1) - x))
    dxdt = m*x - x**3 + A*np.sin(omega_e*t) + noise_sqrt2D + f
    # Heun predictor-corrector (evaluate slopes at midpoint too)
    ...
# SNR: per-oscillator periodogram -> S_max at omega_e,
# S_min = mean of sidebands [0.75,0.85]w_e & [1.15,1.25]w_e; ensemble-average
```

### Recipe C — diagnostic before interpreting γ-effects

Always record σ_i(t) traces: (a) time-average ⟨σ⟩ vs γ and vs D — if ⟨σ⟩ drifts, effects are just "static coupling drift" and the adaptive model reduces to its mean-field static counterpart; (b) oscillation amplitude of σ(t) — small amplitude + large mean = quasi-static structure (paper's regime); large amplitude = genuinely dynamical coupling where new effects may appear beyond the static phenomenology.

### Recipe D — mapping to neuroscience coupling rules

The suppressive adaptive rule dσ/dt ∝ γΔ/(1+Δ) − ασ is the same mathematical family as: short-term synaptic depression/recovery (Tsodyks-Markram: state variable gating effective strength by usage/mismatch), error-correction plasticity in spiking networks, and neuromodulatory homeostasis. When studying noise-induced switching/rhythmogenesis in such networks, expect: γ ↔ plasticity rate shifts optimal noise floor; α ↔ recovery rate buffers the effect (higher α needs higher γ for equal SR change); topology decides whether mis-tuning causes graceful or catastrophic regularity loss.

## Connections

- **Neuroscience SR**: mammalian auditory system SR (forced detection near threshold); cortical up/down-state switching as bistability + noise; adaptive coupling here = short-term plasticity modulating the SR operating point — a candidate mechanism for how attention/neuromodulation shifts the optimal noise level without changing intrinsic noise.
- **Adaptive-network theory**: complements enhancement results in small-world bistable networks; extends known adaptive-coupling effects (explosive sync, frequency clusters, chimeras) with the SR dimension.
- **Memristive/neuromorphic hardware**: cubic-memristor couplers are real devices; this paper is the demonstration that memristive synapses control SR — relevant for noise-harvesting sensors and analog neuromorphic front-ends where noise is unavoidable and must be exploited, not suppressed.
- **Noise-induced switching in excitable pairs** (Bačić et al.): same interaction of adaptivity and noise at 2-oscillator scale.

## Pitfalls

- **Do not omit the decay term (−ασ)**: without it σ grows unboundedly (input γΔ/(1+Δ) ≥ 0), producing extreme multistability, initial-condition-dependent characteristics, and nonstationary statistics — structurally unstable, not a model of any real process.
- SNR sideband definition matters: the paper uses fixed relative sidebands around ω_e ([0.75,0.85] and [1.15,1.25]); changing these windows changes reported SNR values (use one definition throughout a study).
- Forcing must be subthreshold (A = 0.04 < transition threshold) for clean SR; above threshold, resonance is trivially driven (though SR can still be observed).
- Ring local coupling results transfer across the two local configurations (per-node vs per-edge σ) — the phenomenology is robust to how adaptivity is wired locally, but the D_opt values differ quantitatively.
- The "quasi-static structure" interpretation (⟨σ⟩ dominant, amplitude small) held across all studied regimes; genuinely dynamical coupling (large σ oscillations) may behave differently — verify Recipe C before extrapolating.
- Higher decay α does NOT change the qualitative picture but shifts the γ needed for a given effect upward (quantitative compensation only).
