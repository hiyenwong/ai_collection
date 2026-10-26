---
name: colored-noise-rnn-chaos-soliton
description: "Colored-noise random RNN chaos thresholds and soliton map"
category: neuroscience
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [neuroscience, neural-dynamics, computational-neuroscience, random-networks, chaos]
    related_skills: [krylov-mean-field-chaos-rnn, ei-network-chaos-synchrony-theory, predictable-mean-field-chaos-rnn, memory-uncertainty-relation-recurrent-networks]
trigger: random recurrent neural network dynamics, dynamical mean field theory, colored noise, Ornstein-Uhlenbeck input, sublinear activation function, edge of chaos, largest Lyapunov exponent, local instability vs chaos, Schrödinger Lyapunov method, Pöschl-Teller potential, soliton two-point function, correlation time divergence cutoff, critical exponent nu=1/2, participation dimension, four-point function, replica calculation, DMFT, Sompolinsky model, type I excitability, Pade activation, unstable but non-chaotic regime, weak disorder expansion, Mehler expansion, Price theorem
---

# Random RNN Dynamics under Colored Noise and Sublinear Activations: Threshold Separation, Soliton Map, and Participation Dimension

**Source**: "Dynamics of random recurrent neural networks: colored noise and sublinear activations" — Germán Mato, Facundo Rigatuso, Gonzalo Torroba (Instituto Balseiro / Centro Atómico Bariloche, CONICET), arXiv:2610.31575 (q-bio.NC, cond-mat.dis-nn, nlin.CD, 22 Oct 2026).

## When to Use

Use when analyzing, simulating, or theorizing about **random/chaotic recurrent networks with temporally structured input noise or non-saturating (sublinear, power-law, type-I) activation functions**; when deciding whether observed population dynamics are chaotic vs merely locally unstable; when computing Lyapunov exponents or participation/dimensionality metrics from mean-field correlators; when a claimed "edge of chaos" needs the two-threshold test; when designing DMFT closures for colored-noise driven disordered systems.

## Core Contribution

Extends Sompolinsky–Crisanti–Sommers dynamical mean-field theory of random rate networks to **arbitrary internally colored (temporally correlated) noise** and a **smooth sublinear activation family**. Three deliverables:
1. A single self-consistent correlator equation interpolating white ↔ quenched noise, with matched short-/long-time solution that reproduces simulations **without measured input**.
2. Proof + numerics that **local linear instability (λc,1) and chaos onset (λc,2) are distinct thresholds**; the intermediate regime is locally unstable but Lyapunov-stable under a common noise history. Noise color and activation exponent jointly control the gap; universal cutoff τcorr,max ∝ D0^(−1/2) of the correlation-time divergence for ANY finite noise correlation time.
3. A replica four-point calculation giving **DPR(0)/N = (τ/τcorr)⁴** — zero-frequency participation dimension is slaved to the intrinsic correlation time, so chaos-threshold memory maximum appears as a participation minimum.

## The Model

```
τ dφi/dt = −φi + Σj Wij f(φj) + ξi(t)
⟨Wij Wkl⟩ = (λ²/N) δik δjl          (quenched Gaussian couplings)
dξi/dt = −ξi/τn + σn ηi(t)          (OU colored noise, per-neuron independent)
Gξ(t) = Dξ e^{−|t|/τn},  D0 ≡ Dξ·τn  (integrated noise strength — THE control parameter)
f(φ) = φ / (1 + β²φ²)^{(1−p)/2}     (odd, C∞, Padé family)
     ≈ φ            (|φ| ≪ 1/β)
     ≈ β^{p−1} sgn(φ)|φ|^p   (|φ| ≫ 1/β)
```
- p=0 saturating (tanh-like) → p=1 linear; p=1/2 = **type-I excitability** firing-rate regime.
- Limits recovered: τn→0 at fixed D0 = white noise; τn→∞ at fixed Dξ = quenched static input.

## Self-Consistent Equation (the central tool)

MSR/De Dominicis–Janssen path integral → single-site closure:

```
(−τ² ∂t² + 1) Cφ(t) − λ² Cf(t) = Gξ(t),   Ċφ(0)=0, Cφ(∞)=0
Cf(t) = ⟨f(φ(t))f(φ(0))⟩ under 2D Gaussian with covariances Cφ(t), Cφ(0)=q
```

Closure toolkit (reusable beyond this paper):
- **Price's theorem**: ∂_{Cφ} Cf = ⟨f′(t)f′(0)⟩ ≡ Cf′ — differentiate correlators w.r.t. covariance instead of expanding.
- **Mehler expansion**: Cf(t) = Σ_k ⟨f^(k)⟩²_q/k! · Cφ(t)^k (Hermite coefficients; odd f → odd k only). Long-time decay governed by first Hermite coefficient: κ² = (1 − λ²⟨f′⟩²_q)/τ², **τcorr = 1/κ**.
- **Matched solution**: short-time (oscillator kernel K(t)=sin/sinh(Ωt)/Ω with Ω²=(λ²⟨f′²⟩q−1)/τ²) matched to long-time Mehler tail at t* (continuity of C and Ċ) → predicts full correlator, no measured input needed.

## Two Distinct Thresholds and the Schrödinger Method

- **Local instability** λc,1: Ω²=0 ⇔ λ²⟨(f′)²⟩q = 1 (curvature of effective potential at C=q vanishes).
- **Chaos** λc,2: largest Lyapunov ΛL > 0. Two copies sharing W **and the same noise history**; perturbation correlator obeys a 1D **Schrödinger problem**
```
[−τ² ∂t² + W(t)] Ψ = E Ψ,  W(t) = 1 − λ² Cf′(t),  E = 1 − (1 + ΛLτ)²
```
Chaos ⟺ **negative-energy bound state** (E<0). Necessary condition: min_t W(t) = W(0) ≤ E < 0 — identical to λ>λc,1. NOT sufficient: full spectral analysis needed → λc,1 ≤ λc,2.
- **Intermediate regime** (λc,1 < λ < λc,2): locally unstable (instantaneous growth) yet asymptotically contracting under common noise — chaos suppression by shared noise is generic, not a white-noise artifact.
- Numerics (N=4000): p=0, τn=0.5 → λc,1≈2.5, λc,2≈4; p=0.8 → both <2, gap≈0.25. Increasing τn (fixed D0) lowers both and shrinks the gap; strictly quenched noise → **thresholds coincide** (λc,1=λc,2=λ*, single bifurcation, continuous).

## Weak-Disorder Scaling and the Universal Cutoff Exponent

Particle picture: self-consistent equation = particle in potential V(C,q) = −C²/2 + λ²C_F(C,q); energy conservation fixes q. Key results:
- Noiseless: q ≃ (λ²−1)/(λ²|f⁽³⁾(0)|), τcorr ~ τ/|λ−1| diverges at λ=1 (SCS recovered: λc,1=λc,2=1).
- White/colored noise at weak D0: q(λc,1) ≈ (12/5)^{1/4} D0^{1/2}/(τ^{1/2}|f⁽³⁾(0)|^{1/2}); λ²c,2 ≃ 1 + 12^{1/4}|f⁽³⁾(0)|^{1/2} D0^{1/2}/τ^{1/2}.
- **Main universal result**: τcorr,max = 3^{1/4} τ^{3/2}/(|f⁽³⁾(0)|^{1/2} D0^{1/2}) — exponent **νξ = 1/2 independent of noise color**, because near the transition τcorr ≫ τn and the network only sees the integrated strength D0. Slow noise matters only through crossover |f⁽³⁾(0)|·D0·τn² ~ τ³ (verified: data collapse of τcorr,max vs D0 fails exactly when τcorr,max ~ τn).
- Quenched noise instead: NO cutoff — τcorr ~ [(λ*²−1)λ*(λ−λ*)]^{−1/2} still diverges. Finite-τn vs τn→∞ is a non-commuting limit: fix τn, send D0→0 first.

## Chaos–Soliton Map (novel analytic handle)
Near the chaos transition keep first nonlinear Mehler term → φ⁴ field theory:
```
−C̈ + κ²C − λ3 C³ = Gξ/τ²,   λ3 = (λ²/3!)⟨f⁽³⁾⟩²_q/τ²
```
- Noiseless chaotic state = **sech soliton**: C(t) = √(2κ²/λ3)·sech(κt), self-consistency q = √2·κ/√λ3.
- Fluctuation spectrum = **Pöschl–Teller**: W(t) = τ²κ²(1 − 6sech²(κt)); bound state ψb = sech²(κt), E0 = −3τ²κ² ⇒ **ΛL ≈ (3/2)·τ/τ²corr near onset** — Lyapunov exponent is fixed by the correlation time alone.
- White noise: cusped shifted soliton sech(κ(|t|+t0)); perturbation theory in t0 gives ΛLτ ≈ (3/2)(κ²τ² − √(λ3/2)·D0).

## Participation Dimension from the Four-Point Function

DPR(ω) = [Tr Cf(ω)]²/Tr[Cf(ω)²] needs the disorder-averaged off-diagonal product Γf — a **four-point object** (each pair O(1/N), O(N²) pairs). Replica trick: two copies sharing W but **independent noise histories** (contrast: Lyapunov copies share noise!). Result:
```
DPR(ω)/N = (1 − λeff²/(1+τ²ω²))²,   λeff = λ⟨f′⟩q = √(1 − τ²/τ²corr)
⇒ DPR(0)/N = (τ/τcorr)⁴   — temporal and geometric observables slaved
DPR(0)/N|_{λc,2} = (f⁽³⁾(0))² D0² / 3τ²  (smooth minimum, scales as D0²)
```
- Crossover to full participation at ω ~ 1/τcorr; high frequencies stay near DPR/N≈1 in ALL regimes (stable, unstable-nonchaotic, chaotic).
- Low-dimensional output covariance appears **before** chaos (already in the unstable window), strongest for p=1/2 (type-I).

## Operational Lessons (when analyzing any random network)
1. **Three probes, three quantities — never conflate**: participation ← λ⟨f′⟩; local instability ← λ⟨f′²⟩^{1/2}; chaos ← temporal correlations of f′ (full Schrödinger spectrum). A dimensionality dip or instability need NOT coincide with chaos onset.
2. **Noise color enters only through D0 near criticality** — measure/report integrated noise, not spectrum shape, when close to a transition; the τcorr≫τn universality argument is reusable in any driven disordered system.
3. **Intermediate locally-unstable-nonchaotic windows are generic** under common-noise driving; check both thresholds before labeling dynamics "chaotic" from Jacobian spectra alone.
4. **Order of limits matters**: quenched (τn→∞) vs finite-τn-then-D0→0 give different phase diagrams; state which limit is taken.
5. Finite-size effects are appreciable near the linear end (p→1) — Appendix C of source; report N-scaling of geometry observables.

## Simulation Protocol (reproducing the theory checks)
- Euler–Maruyama, xi-first OU update; σn = √(2Dξ/τn); verify ⟨ξξ⟩ numerically.
- Nested averaging: W-seeds × noise replicas → decomposes variance into quenched (between-W) vs annealed (between-replica) components — numerical counterpart of self-averaging.
- Lyapunov: Benettin two-replica under SAME noise history, renormalize separation each step.
- Spectral DPR: M independent noise histories at fixed W, Hann-windowed segments, U-statistic estimators for Cf and Γf (r≠s removes self-pair bias; i≠j selects off-diagonal covariance).

## Relation to Prior Work
- SCS 1988: noiseless λc=1, τcorr divergence. Schuecker et al. / Engelken et al.: white-noise threshold separation. This paper: general Gξ(t) unified + universal exponent + soliton map + DPR bridge. Kadmon–Sompolinsky-type participation results (white noise) and the authors' quenched-noise work recovered as limits p→0/1 and τn→0/∞.

## Pitfalls
- Do not read long correlator tails as chaos evidence — long τcorr ≠ positive ΛL.
- ⟨f′⟩ vs ⟨f′²⟩ confusion flips instability conclusions (Cauchy–Schwarz: κ²≥0 with equality only for linear f).
- Lyapunov copies must share the noise; participation replicas must NOT — mixing them silently zeroes Γf.
- Report D0 = ∫Gξ/2, not Dξ or σn alone; τcorr,max collapse across τn is the actual test of the universality claim.
