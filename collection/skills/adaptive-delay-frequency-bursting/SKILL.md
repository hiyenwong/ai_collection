---
name: adaptive-delay-frequency-bursting
description: "Use when modeling adaptive delay-coupled oscillators. Quantized detuning frequency bursts."
category: ai_collection
tags: [neuroscience, nonlinear-dynamics, oscillator-networks, time-delay, bursting, slow-fast-systems, synchronization]
---

# Frequency Bursting in Adaptive Delay-Coupled Oscillators

Methodology from arXiv:2609.24671 (Wang, Sieber, Cao, Kurths, Yanchuk — 2026, nlin.AO).

**Core discovery**: Two phase oscillators with *slow adaptive coupling* + *delayed coupling* robustly self-organize into **frequency bursting (FB)**: long near-synchronized epochs punctuated by fast phase slips, where the mean-frequency detuning is **quantized** to integer multiples of the small adaptation frequency: Ω₁ − Ω₂ = n·ε (n = number of spikes per burst).

## Minimal Model (System 1–4)

Two phase rotators with adaptive, delayed coupling:

    dφ₁/dt = ω₁ + K₁(τ-delayed φ₂ − φ₁ terms, phase shift α)
    dφ₂/dt = ω₂ + K₂(τ-delayed φ₁ − φ₂ terms, phase shift α)
    dK₁/dt = ε · G₁(φ₂(t−τ) − φ₁(t))   (causal plasticity rule)
    dK₂/dt = ε · G₂(φ₁(t−τ) − φ₂(t))   (Hebbian-like rule)

Key structural features:
- **Fast variables**: phases φ — infinite-dimensional dynamics due to delay τ (functional state space)
- **Slow variables**: coupling strengths K₁, K₂ — ordinary ODE adaptation, timescale 1/ε
- **Two distinct adaptation rules**: causal (spike-timing-dependent-like) vs Hebbian — their interplay produces approximately *antiphase* modulation of the coupling weights
- Neuronal interpretation: K₁ adaptation ≈ STDP (spike-timing-dependent plasticity), K₂ ≈ Hebbian consolidation

## The Frequency Bursting Phenomenon

FB solutions are **relative periodic orbits** (phase-shift symmetry): φ(t) = Ωt + modulations, with modulation period T ∝ 1/ε.

1. **Slow drift**: relative phase ψ = φ₂ − φ₁ stays approximately locked for times ~1/ε
2. **Fast transition**: step-like phase jump of 2π·n during brief slips
3. **Quantized detuning**: mean frequency difference |Ω₁ − Ω₂| = n·ε — NOT rational locking; frequency ratio alone cannot classify the state
4. **Burst size = winding number**: the accumulated relative winding over one modulation period is an integer n; n equals the number of spikes in the frequency burst

**Diagnostic**: instantaneous relative frequency ẋ = (dψ/dt)/(2π-ish) shows n localized spikes per slow period; classify states by winding number, not frequency ratio.

## Fast-Slow Geometric Mechanism

The backbone is organized by **critical manifolds** of relative equilibria:

- Relative equilibria: φᵢ = Ωt + θᵢ, Kᵢ constant — phase-locked states
- For each slow pair (K₁, K₂), the fast subsystem admits a finite number M of distinct roots Ω^(m) → **M critical manifold sheets** S^(m), planar sheets parametrized by (K₁,K₂)
- **Sheets multiply with delay**: M grows as delay τ increases (large-delay spectral theory — Yanchuk-Perlikowski): more coexisting phase-locked states
- Stability of each sheet via quasipolynomial characteristic equation (infinitely many roots; neutral eigenvalue from symmetry)

**Bursting cycle** = slow crawl along a stable sheet → drift into fold boundary → fast jump to another sheet (phase slip) → repeat. Alternation of slow/fast transitions generates the quantization: each fast jump advances winding by integer amount.

## Key Properties (verbatim findings)

1. FB oscillations = periodic bursts of relative frequencies with n spikes
2. Mean frequency difference proportional to ε (inverse adaptation timescale)
3. Detuning quantized: Ω₁−Ω₂ = n·ε, n ∈ ℤ⁺ ("near-synchrony with quantized detuning")
4. Robust: FB states exist stably in finite parameter regions; many coexisting FB states from overlapping stable sheets
5. Parameter continuation (DDE-BifTool with phase-shift symmetry extension) confirms coexisting relative equilibria with distinct frequencies and instability indices

## When to Use

- Neuronal oscillator pairs/ensembles with both synaptic plasticity (slow adaptation) and axonal propagation delay — quantized detuning predicts discrete burst-size classes in spiking co-activity
- Semiconductor laser networks with optical feedback (Lang-Kobayashi class) — the same slow-fast delay mechanism
- Any adaptive network where coupling weights evolve on a much slower timescale than node dynamics AND signals propagate with delay: ecological interactions, social adaptation
- Diagnosing "not-quite-synchronized" states: if measured frequency ratios look irrational but close to 1, check for winding-number quantization before concluding desynchronization
- Bursting without intrinsic neuron dynamics: pure network mechanism — relevant to population-rate bursts observed in delayed plastic circuits

## Reusable Patterns

1. **Winding-number classification**: for near-synchronous delayed-adaptive systems, characterize solutions by accumulated relative winding per slow period (integer n), not by frequency ratio
2. **Critical-manifold bookkeeping**: treat slow coupling variables as parameters of the fast subsystem; enumerate stable sheets; bursting = itinerary over sheets crossing fold boundaries
3. **Quantized detuning as fingerprint**: detuning locked to integer multiples of adaptation frequency is a signature of delay+adaptation interplay — usable as an inverse diagnostic from spike-train data
4. **Large-delay sheet proliferation**: delay increases the number of coexisting stable phase-locked states → multistability; expect many coexisting burst states with different n in high-delay regimes
5. **Causal + Hebbian dual adaptation**: using two complementary plasticity rules (one timing-causal, one correlation-based) yields antiphase weight cycling — a minimal oscillation-generating motif for neuromorphic synapses

## Simulation Recipe

1. Choose ω₁=ω₂ (rescale to 0/1 by rotating frame — Appendix A normalization)
2. Set ε ≪ 1 (e.g. 0.01), delay τ moderate-to-large (sheet count grows with τ)
3. Integrate DDEs (e.g. Julia DifferentialEquations / Python JAX-DDE); discard transient ~10/ε
4. Compute instantaneous relative frequency; count spikes per slow period → n
5. Verify Ω₁−Ω₂ ≈ n·ε; sweep initial conditions to enumerate coexisting n-families
6. Continue branches in τ with DDE-BifTool (phase-shift-symmetry aware) to map stability regions

## Limitations

- Two-oscillator analysis; extension to networks open (though mechanism is pairwise-local)
- Chaotic bursting transition: stability loss of periodic FB states is an open question
- Phase-oscillator reduction assumes weak coupling — strong coupling may need amplitude models

## Source

- arXiv:2609.24671 — Wang, Sieber, Cao, Kurths, Yanchuk, "Frequency bursts in adaptive delay-coupled oscillators" (nlin.AO, 2026)
- Related: [[finite-size-fluctuation-response-kuramoto]], [[spectral-transfer-cascade-kuramoto]], [[network-attractors-delay-plasticity]], [[frequency-bursts-adaptive-delay-coupled]]
