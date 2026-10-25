---
name: central-spin-time-reversal-metrology
description: Use when designing SATIN/butterfly echo quantum metrology.
category: quantum
trigger: time-reversal echo metrology, central spin model squeezing, SATIN protocol, butterfly echo, axis-agnostic quantum sensing, cavity QED metrology, NMR quantum processor, Heisenberg scaling with collective readout
arxiv_id: "2610.30686"
---

# Time-Reversal-Based Quantum Metrology in a Central-Spin Architecture (SATIN → Butterfly Echo)

Methodology from "Time-reversal-based quantum metrology in a central-spin architecture: from SATIN to butterfly echo" (arXiv:2610.30686, Kumar & Choudhury, Oct 2026). Implements both time-reversal echo metrology protocols on ONE hardware primitive — a star-graph central-spin Hamiltonian — turning an over-squeezed (non-Gaussian, readout-hostile) entangled state into a macroscopic population difference measurable with coarse-grained collective detection.

## When to Use
- Designing quantum sensors with collective (not single-particle) readout that must beat the SQL at Heisenberg exponent.
- The encoding axis is known (use SATIN) or unknown (use butterfly echo).
- Platforms where entanglement is mediated by a central element: cavity QED, NMR quantum processors, ancilla-mediated spin chains.
- Extracting QFI from over-squeezed states whose fine structure defeats conventional readout.

## The hardware primitive: central-spin XX model

```
H = Ω S_z^(c) + (g̃/2)(S_+^(c) I_−^(b) + S_−^(c) I_+^(b))
```

- Single ancilla spin of magnitude S_cen (energy gap/detuning Ω) coupled uniformly to N bath spin-½ sensors via XX exchange — only N physical bonds, no bath-bath coupling. g̃ held N-independent (fixed microscopic coupling).
- Homogeneous coupling conserves total bath spin ⇒ dynamics confined to the symmetric Dicke subspace: **effective dimension (2S_cen+1)(N+1) instead of 2^N** — exact diagonalization to N=1000.
- **Dispersive regime** (Ω ≫ g̃√N): second-order Schrieffer–Wolff gives effective bath OAT `H_eff = χ (J_z)²` with `χ = g̃² S_cen / (2Ω)`. χ ∝ S_cen: **enlarging the ancilla accelerates squeezing without changing the metrological ceiling** — a speed knob, not a gain knob.

## Exact time reversal (the echo's engine)

Reverse evolution is implemented PHYSICALLY, not numerically: `R = e^{−iπS_y^(c)} · e^{−iπJ_x}` (π pulse on ancilla about y + collective π on bath about x) gives `R H R† = −H`, hence `U† = e^{+iHτ}`.
- Requires the longitudinal coupling A_z = 0 (an A_z S_z σ_z term is invariant under both flips and would survive).
- The reversal is of the FULL Hamiltonian, so the echo closes **exactly at all orders** of the Schrieffer–Wolff expansion — no dispersive approximation needed for cancellation at zero signal. This exactness is what makes the butterfly plateau a genuine physical result even outside the dispersive regime.

## SATIN echo (known axis)

1. Entangle: bath CSS |+x⟩^⊗N, ancilla in lowest state; evolve under full H for time t.
2. Encode: apply unknown rotation e^{−iφJ_y}.
3. Reverse: apply e^{+iHt} via the π-pulse construction; measure ⟨J_y⟩. At φ=0 forward and reverse cancel exactly (back to CSS).

Analytic (dispersive/OAT) signal slope, with x = 2S_cen·t/Ω and χ_eff = 2S_cen/Ω at g̃=2:

```
S(t) = (N/2)(N−1) · sin(x) · cos^{N−2}(x)
Δφ = √(N/4) / S(t),   gain G = 10 log10(1/(N Δφ²)) dB
t_opt = Ω/(2 S_cen √N)   [exact argmax: t* = Ω·arctan(1/√(N−2))/(2S_cen), verified numerically within 0.7% at N=100]
Ceiling: F_Q = N²/e   →   HL − 4.34 dB for the collective ⟨J_y⟩ readout
```

Numerically verified: F_Q/N² → 1/e (ratio 0.995 @ N=100 → 0.9999 @ N=4000). The 4.34 dB deficit = 1.34 dB intrinsic collective-⟨J_y⟩ readout penalty (vs parity-readout squeezed benchmark HL−3dB) + 3 dB Heisenberg gap. Gain profile is **bell-shaped**: past t_opt the squeezed quadrature rotates away from the measurement axis. Peak-gain scaling measured 7.2–9.2 dB/decade (Ω=300→2000), approaching the Heisenberg 10 dB/decade; t_opt power law N^−0.46 matches prediction.

## Butterfly echo (unknown axis, axis-agnostic)

Axis-agnostic sensing: encoding is a rotation about an UNKNOWN axis n̂; single-shot non-adaptive channel is depolarizing `ρ_θ = (1/4π)∫dn̂ R_n̂(θ) ρ R_n̂†(θ)` with channel QFI

```
F(θ) = (4/3) Σ_{j∈{x,y,z}} Var(J_j)   → maximize all three variances simultaneously = anticoherent states
Haar-random Dicke probe: F_channel = N(N+2)/3 ≈ N²/3
Echo collective readout extracts 3/4 of channel QFI:  F_echo = (3/4)·F_channel ≈ N²/4
Gain: G = 10 log10(N/4)   → Heisenberg exponent, exactly 6 dB below HL
```

Protocol (star-graph implementation):
1. Initialize |↓⟩_c ⊗ |I, I⟩_b (fully polarized Dicke).
2. **Forward scrambling**: K random conjugated CSM steps `U_j(m̂_j) = (1⊗R_bath(m̂_j)) e^{−iHτ} (1⊗R†_bath(m̂_j))`, m̂_j uniform on S², α_j ∈ [0,2π) — random-axis OAT in the dispersive limit; **axes recorded classically**.
3. Encode unknown rotation e^{−iθJ_n̂}.
4. Apply inverse sequence U†_1···U†_K from the recorded axes; measure ⟨J_z⟩.

Signal: ⟨J_z⟩/I → sinc²(Iθ) (N→∞) — **quadratic** near θ=0 (fully polarized Dicke is an I_z eigenstate); sensitivity from curvature, extracted with a stated bias angle θ_b (paper convention 10⁻⁴), averaged over ~50 circuit realizations.

**K = 8 steps suffice** (≈ N-independent) to reach Haar-limit performance.

## Key results and design rules

- **Monotone plateau vs bell curve**: butterfly gain rises monotonically then saturates at a stable plateau (each pulse re-randomizes the OAT axis; once isotropic, extra evolution changes nothing) — within 0.3 dB of 10log10(N/4); σ-bands collapse at the plateau (self-averaging, std(F_Q)/F_Q ~ N^−1/2, converging to an approximate unitary 2-design). For N≥100 a SINGLE random circuit is reusable as a fixed sensing resource.
- **Robustness beyond dispersive**: even at Ω=100 (OAT mapping broken) butterfly stays within 0.5 dB of Haar — the ceiling is set by the Dicke subspace dimension, not OAT accuracy. SATIN's ceiling degrades with detuning instead.
- **Known axis ⇒ SATIN wins**: N²/e vs N²/4 (prefactor e vs 4); both scale F_Q ∝ N².
- **S_cen knob**: raising S_cen 0.5→1.0→1.5 leaves plateau height and K≈8 depth unchanged while cutting τ_opt by 2–3×. Butterfly τ_opt ∝ Ω/(2S_cen g̃² N^α), α≈0.80 (each step must wrap the coherent state fully around the Bloch sphere before re-randomizing).
- Exchange-coupled XX forbids the product-probe N² shortcut available to longitudinal J_zσ_z ancilla probes — ceilings reported are specific to exchange coupling.

## Pitfalls
- SATIN's bell curve: mistiming past t_opt rapidly forfeits gain — schedule t at t_opt or track the squeezed quadrature.
- Butterfly's quadratic signal: sensitivity depends on the bias-angle convention; always state θ_b.
- Time-reversal construction breaks if a longitudinal A_z S_zσ_z term is present (flip-invariant, survives reversal) — keep the coupling purely transverse.
- λ-analog warning for platform transfer: Dicke-subspace confinement relies on homogeneous coupling; disorder in g̃ breaks the dimension reduction.

## Related topics
- satinin-style echo protocols: one-axis twisting skills (OAT squeezing), Wineland parameter benchmarks
- time-reversal / Hamiltonian-inversion skills (chaos-based metrology is a DIFFERENT lineage — butterfly echo ≠ butterfly metrology)
- cavity-QED collective-readout skills; anticoherent states in quantum rotosensing
