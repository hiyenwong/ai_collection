---
name: cv-flags-bosonic-ancilla-errors
description: Use when protecting bosonic codes from ancilla decay. CV flags record continuous gate errors in phase space for feedback correction.
category: ai_collection
trigger_words: bosonic QEC, cat code, GKP code, ancilla decay, continuous-variable flag, heterodyne measurement, syndrome extraction, circuit QED, conditional rotation, conditional displacement
---

# Continuous-Variable Flags for Bosonic Codes (arXiv:2610.07139)

**Paper**: Décultot, Gautier, Mirrahimi (Alice & Bob / ENS Paris / RIKEN, quant-ph, Oct 2026)
**Task**: Ancilla decay during qubit-oscillator gates propagates to the storage oscillator as a **continuous error** whose magnitude depends on jump time — beyond any bosonic code's correction scope. Make it detectable and correctable instead of preventing it.

## Core Mechanism: CV Flag

1. **Flag oscillator** coupled to the same ancilla via dispersive interaction — its **phase-space position encodes the continuous error** (jump time τ ∈ [0, T]) corrupting the memory.
2. After the gate, **heterodyne measurement** of the flag estimates the error.
3. **Feedback** (conditional displacement/rotation) undoes the error **up to a bosonic code stabilizer** — the continuous channel is *discretized* into code-correctable errors.

Key insight: the flag needs **no new ingredients** — same dispersive coupling, displacements, and rotations that implement the protected gates drive the flag.

## Error Model (conditional rotation CR(θ))

Ancilla decay at time τ during CR(θ) leaves the memory rotated by:
```
θ_err = θ·(2τ/T − 1)   (continuous in τ)
```
The |e⟩ component relaxes to |g⟩ mid-gate, reversing its rotation trajectory — final memory position depends continuously on τ. Same structure for conditional displacement CD(β): error displacement interpolates continuously with τ.

## Protection Orders (explicit sequences)

| Gate | Flags | Protection |
|------|-------|-----------|
| CR(θ) | 1 flag | **All orders** in ancilla decay |
| CD(β) | 1 flag | First order |
| CD(β) | 2 flags (χ-matched) | **All orders** (second flag records post-echo decays; weight function F̃_ee concentrates at s=−2, 0) |

χ-matched protocols extend protection to ancilla **thermal excitations**.

## Benchmark Results (realistic circuit-QED parameters)

- **Four-component cat code parity measurement**: residual logical bit-flip p_X ≈ 5×10⁻⁷ at flag size |ζ|²=100 — **>3 orders of magnitude below unprotected**; decreases monotonically with |ζ|².
- **sBs-stabilized finite-energy GKP**: logical lifetime **4 ms → ≈450 ms** at |ζ|²=120 (within factor 1.5 of the noiseless-ancilla bound); with full realistic imperfections ≈170 ms at |ζ|²=200 (~40× improvement). Big conditional displacement dominates the error budget — protect it first.

## Robustness (all four idealizations relaxed)

| Imperfection | Effect | Fix |
|--------------|--------|-----|
| Detection efficiency η<1 | Gaussian broadens 1/η | Rescale flag displacements by 1/√η — photon overhead ×1/η (η=0.5 doubles budget) |
| Flag photon loss κ_f | Random phase-kicks → **pure ancilla dephasing** channel | Benign vs the logical errors prevented; deterministic decay ζ→ζe^(−κ_f t/2) absorbed in calibration |
| Flag self-Kerr | Deterministic recalibration | Re-tune flagging sequence |
| Finite control pulses | Deterministic recalibration | Re-tune |

None is a fundamental obstacle: first = resource overhead, rest = dephasing or recalibration.

## Implementation Notes

- Flag performance is governed by **flag size |ζ|²** — the phase-space separation between coherent states encoding distinct jump times.
- Per-round logical bit-flip from conserved quantities (four-photon stabilization): p_X = Tr[J₁ C(|0_L⟩⟨0_L|⊗|+⟩⟨+|)], C = N_R bare / M∘F flagged.
- Conditional bit-flip p_X|γ obtained by sweeping rotation angles µ after heterodyne outcome γ; restabilization follows.
- Optimal GKP cycle: run sBs cycles as fast as possible — remaining decoherence is memory loss during idle windows + intrinsic finite-energy pumping imperfection.

## Reusable Patterns

1. **Record-don't-prevent for continuous errors** — when a continuous error channel lies outside code scope, correlate an auxiliary degree of freedom with the error parameter and measure it, instead of engineering error-insensitive couplings (which stay first-order-limited).
2. **Continuous-to-discrete error discretization** — feedback correction "up to a stabilizer" converts uncorrectable continuous errors into correctable discrete ones.
3. **Phase-space metrology as error encoder** — a coherent-state ruler in phase space maps an unknown continuous parameter (jump time) to a measurable complex amplitude.
4. **Reuse-the-toolbox instrumentation** — protection hardware (the flag) is driven by the same primitives as the protected gates: zero marginal calibration complexity.
5. **Graded robustness analysis** — relax each idealization one-by-one and classify impact as overhead / benign channel / deterministic recalibration; only the first costs resources.

## Related

- GKP codes (Gottesman-Kitaev-Preskill); cat codes; binomial codes — bosonic encoding landscape
- sBs (small-Big-small) repetition stabilization — GKP flagship protocol
- kg concepts: bosonic error correction, continuous-variable flag, ancilla decay error channel, heterodyne jump-time estimation, GKP code stabilization
- Future: squeezed/non-Gaussian pointer states improve jump-time SNR at fixed photon number; jump-time-optimal readout beyond heterodyne
