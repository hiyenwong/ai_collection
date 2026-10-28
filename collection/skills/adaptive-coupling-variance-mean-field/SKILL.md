---
name: adaptive-coupling-variance-mean-field
description: Weight-variance mean-field for adaptive oscillator networks.
trigger: adaptive coupling weight variance, second-order moment closure, adaptive Kuramoto mean field, coupling heterogeneity emergence, STDP symmetry, Ott-Antonsen adaptive networks, structured connectivity formation, phase-oscillator plasticity
category: ai_collection
---

# Coupling-Weight Variance Mean-Field Theory for Adaptive Oscillator Networks

**Source**: arXiv:2609.22597v1 (2026-09-22) — Gast, Takasu, Kurths, Kennedy (Scripps Research / PIK / HU Berlin).

## Problem

Mean-field reductions (Ott–Antonsen, OA) of adaptive networks track only the **average coupling weight** Ā. They cannot tell when coupling stays effectively homogeneous (global-coupling-like) vs. when **structured connectivity emerges** (assemblies, cores, antisymmetric couplings, chaos). This skill derives and applies a **second-order moment closure** giving closed mean-field equations for the coupling-weight variance V_A.

## Model

Network of non-identical Kuramoto oscillators (Lorentzian intrinsic-frequency spread Δ):

- Phases: `θ̇ᵢ = ωᵢ + (K/N) Σⱼ Aᵢⱼ(t) sin(θⱼ − θᵢ)`
- Adaptive weights: `Ȧᵢⱼ = μ G(θⱼ − θᵢ) + γ(1 − Aᵢⱼ)`  — drive G + decay to 1
- Two canonical rules: symmetric `G_s(φ)=cos(φ)` (Hebbian-like) vs. antisymmetric `G_a(φ)=sin(φ)` (spike-timing/anti-Hebbian-like)
- Adiabatic regime: γ, μ ≪ 1 (weights slow vs. phases).

## First-Order Mean Field (weight average)

- Symmetric: `Ā˙ = μ R² + γ(1 − Ā)` — coherence R feeds back into mean weight ⇒ **bistability**: fold at `Δ* = K(μ+γ)²/(8μγ)`; fixed points `Ã₁,₂ = ½ ± ½√(1+4μ²/(4γ²) − μ(4Δ−K)/(2γK))` (Eq. 15).
- Antisymmetric: `Ā˙ = γ(1 − Ā)` — average weight frozen at 1; macroscopic dynamics indistinguishable from global coupling **at first order**.
- Phase coherence on OA manifold: `Ṙ = −ΔR + (K Ā/2) R(1 − R²)`, bifurcation at `KĀ = 2Δ`.

## Second-Order Closure (the contribution)

Decompose pair drive into static + fluctuating parts: `Gᵢⱼ(t) = Γᵢⱼ + gᵢⱼ(t)`, with time-averaged single-oscillator moments `c(ω) = ⟨e^{iθ(ω,t)}⟩ₜ = p(ω)+iq(ω)`, order parameter `S ≡ |c|² = P+Q`, `R² = P−Q`, `⟨pq⟩=0`.

1. **Weight variance**: `V̇_A = 2μ C_A − 2γ V_A`
2. **Covariance split** `C_A = C_Γ + C_g` with linear ODE pair:
   - `Ċ_Γ = −γ C_Γ + μ σ_Γ²` (static, quenched spread)
   - `Ċ_g = −(γ + 2Δ) C_g + μ σ_g²` (fluctuating, damped by frequency spread 2Δ)
3. **Variances** (identical for both rules!):
   - `σ_Γ² = ½(S² − R⁴)` — static spread of pairwise drives
   - `σ_g² = ½(1 − S²)` — temporal fluctuations
4. **Locked/drifting split** for S: locked band |ω| ≤ b = KĀR, `S = S_L + S_D`, `S_L = arctan(b/Δ)·(2Δ/π)(1 + 2Δ²/b²) − 4Δ²/(πb) − R²` (Eq. 34).

**Steady-state variance** (Δ ≫ γ, valid for both rules):

```
V_A ≈ μ²(S² − R⁴) / (2γ²)                      (symmetric w/ Ā=1)
V_A/Ā² = μ²(S² − R⁴) / [2(γ + μR²)²]           (symmetric, self-consistent)
```

Static contribution decays at γ, fluctuating at γ+2Δ ⇒ **frequency heterogeneity quenches fluctuation-driven structure**; structure is quenched (static) in nature.

## Key Findings

1. **Non-monotonic Δ-dependence**: relative variance V_A/Ā² vs. heterogeneity Δ is nonlinear, non-monotonic, mediated by coherence R. Peaks near the fold bifurcation (symmetric) or chaotic regimes (antisymmetric).
2. **Symmetric vs. antisymmetric divergence** (the punchline):
   - Symmetric (cos): deviation from global coupling starts with oscillators in the **tails** (desynchronized, barely adapt) → synchronized strongly-coupled **core** emerges; bistable regime appears that is absent without adaptation.
   - Antisymmetric (sin): deviation starts at the **center** (synchronized at non-zero phase lag) → weights evolve in opposite, sign-dependent directions → core destabilizes, can yield chaos. Stronger departure from OA dynamics.
3. **Regime delineation**: the equations separate parameter space where adaptive networks behave like globally coupled systems from where complex coupling patterns form.

## Reuse Recipes

### When to apply
- Adaptive/plastic Kuramoto, theta-neuron, or phase-reduced SNN populations where weight structure matters.
- Deciding whether an OA/next-generation neural-mass reduction is valid for a plastic network (check V_A/Ā² via Eq. 47–49).
- Interpreting STDP-symmetry effects: Hebbian-like (symmetric, cos) plasticity homogenizes and stabilizes cores; timing/antisymmetric (sin) plasticity antisymmetrizes and destabilizes.

### Minimal mean-field integrator (5 ODEs)
```python
# integrate: R, Ā, C_Gamma, C_g  (+ optional V_A via algebra)
# dR   = -Delta*R + K*A/2 * R*(1-R**2)
# dA   = mu*R**2 + gamma*(1-A)          # symmetric rule
# dCg  = -gamma*Cg + mu*0.5*(S**2 - R**4)
# dCf  = -(gamma+2*Delta)*Cf + mu*0.5*(1-S**2)
# V_A  = Cg + Cf   (steady: mu^2*sig_G^2/gamma^2 + mu^2*sig_g^2/(gamma*(gamma+2*Delta)))
# S from Eq. 34 with b = K*A*R
```
Microscopic validation: N=500 oscillators, PyRates or hand-rolled; compare V_A/Ā² and hysteresis around fold.

### Validation checklist
- Hysteresis near Δ* in microscopic sim vs. mean-field fold (Fig. 2).
- Antisymmetric mismatch for μ>γ at low Δ (2Δ<K, R>0) — mean-field underestimates variance there.
- Weight matrix structure: symmetric → homogeneous core; antisymmetric → sign-split core couplings.

## Neuroscience Significance

- Synapses undergo activity/timing-dependent adaptation with heterogeneous functional forms across cell types. This gives the first closed-form macroscopic statistics for plastic weight **distributions**, not just means.
- Predicts: intermediate heterogeneity maximizes structured connectivity; timing-based (antisymmetric) rules drive stronger departures from homogeneous dynamics than rate-based (symmetric) rules.
- Connects to homeostatic plasticity and multistability of neuronal assemblies; framework extends to spiking mean fields (next-generation neural masses, Luke/Barreto, Montbrió, Gast 2023).

## Limitations / Open Problems

- One-way coupling: equations capture how R shapes weights, not how weight **variance** feeds back into phase dynamics (needs integro-differential treatment à la Gkogkas/Kuehn/Xu).
- Weak-coupling assumption in covariance derivation (θᵢ ≈ ωᵢt + θᵢ₀) for drifting oscillators.
- Antisymmetric low-Δ regime (μ>γ) underpredicted — exact closure open.

## Key References

- Ott & Antonsen 2008 (OA manifold); Kuehn 2016 (moment closure review)
- Gast et al. 2023 PRE 107, 024306 (heterogeneous spiking thresholds); Pietras/Clusella/Montbrió PRE 111, 014422 (2025) — low-dim adaptive spiking nets
- Gkogkas, Kuehn & Xu 2022 — continuum limits of adaptive networks
- PyRates (Gast) for microscopic simulation.
