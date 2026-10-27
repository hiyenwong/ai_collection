---
description: Use when noisy thermalization or Choi noise spectroscopy
name: deep-thermalization-choi-ensemble
category: ai_collection
version: 1.0
author: quantum-cron-2026-10-26-run2
license: MIT
metadata:
  hermes:
    tags: [deep-thermalization, projected-ensemble, choi-state, mixed-state, quantum-channels, noise-spectroscopy, wishart-ensemble, scrambling, measurement-conditioned-states, nisq-benchmarking]
    related_skills: [size-independent-mlsi-quantum-gibbs, magic-distillation-code-limits, qfi-stabilizer-framework, classical-shadow-estimation]
---

# Mixed-State Deep Thermalization: The Channel-Induced Ensemble

Methodology from arXiv:2610.31580 — "Mixed State Deep Thermalization under Generic Quantum Errors" (Xie-Hang Yu, Caltech + Pavel Kos, Univ. Ljubljana; quant-ph, 22 Oct 2026).

## One-Line Summary

Dilute local quantum errors do not destroy deep thermalization — they **select** it: after sufficient scrambling, the mixed-state projected ensemble (MSPE) converges universally to the **channel-induced ensemble (CIE)**, a Born-weighted normalized correlated Wishart ensemble ρ̃(X) = XMX† built from a Ginibre matrix X and the **normalized Choi state M of the error process**; the limit depends only on the Choi spectrum, not on the microscopic unitary dynamics, initial state, or error space-time location.

## When to Use / Activation

- Benchmarking emergent randomness on NISQ hardware via measurement-conditioned states (the pure-state Haar reference is wrong under noise; use the CIE).
- Inferring a noise channel's **Choi spectrum** from measured conditional-state distributions without knowing when/where errors acted (noise spectroscopy complement to bit-string-based noise learning).
- Predicting late-time fluctuation/eigenvalue statistics of conditional states in noisy chaotic circuits (beyond the reduced density matrix).
- Constructing universal random mixed-state ensembles with a prescribed correlation structure (Choi spectrum as the dial).
- Analyzing deep thermalization experiments (qudits, cold atoms, superconducting qubits) where readout of the complement B is complete but errors intervene.

## Core Construction (the reusable machinery)

**Setup.** Qudit chain, local dimension d. Retained region A (dim D_A = d^{N_A}), fully measured complement B (dim D_B), every outcome retained. Dilute local CPTP errors {N_i} interspersed in unitary evolution. Conditional (unnormalized) state: ρ̃_A(α) = ⟨α|ρ(t)|α⟩_B, Born weight P_α = Tr ρ̃_A(α). MSPE = {P_α, ρ_A(α)}; k-th moment ρ^(k) = Σ_α P_α ρ(α)^⊗k = Σ_α P_α^{1−k} ρ̃(α)^⊗k. First moment = reduced density matrix; higher moments resolve outcome fluctuations.

**Choi data.** Normalized Choi state M_N = (id ⊗ N)(|φ₀⟩⟨φ₀|) with |φ₀⟩ = d^{−1/2} Σ_i |ii⟩; CPTP ⇒ M ≥ 0, Tr M = 1. For well-separated dilute errors the effective object is the **joint Choi state M = ⊗_i M_{N_i}** (permutation weights factorize across scrambling regions).

**The CIE.** Draw X ∈ C^{D_A × D_C} from scaled complex Ginibre (i.i.d. centered circular complex Gaussian, E[X†X] = I; D_C = d^{2n} for n channels). Then

- ρ̃_M(X) = X M X†,  P_M(X) = Tr(XMX†),  ρ_M = ρ̃_M/P_M
- ensemble E_M = {P_M(X) dµ_G(X), ρ_M(X)} — a **Born-weighted normalized correlated Wishart ensemble**
- k-th moment: ρ_M^(k) = ∫ dµ_G(X) P_M^{1−k} (XMX†)^⊗k

**Main result (informal).** After sufficient scrambling, the late-time MSPE → E_M for any chaotic dynamics; the limit depends on M **only through its spectrum** (unitary invariance X → XV for M = VΛV† makes XMX† ≅ XΛX† in distribution).

**Known limits (sanity anchors).**
- Unitary error: M pure (rank 1) → pure-state Haar ensemble (standard deep thermalization).
- Complete depolarization N(ρ) = Tr ρ/d · I: M = I/d² → induced random density matrix = generalized Hilbert-Schmidt ensemble.
- Partial depolarization interpolates; arbitrary CPTP maps select their own Choi spectra. Equal Choi spectra ⇒ same limit, but transients retain the input–output structure of M.

## Where It Is Established (proof venues you can imitate)

1. **Dual-unitary circuits** (exactly solvable): folded k-replica network; maximally-entangled-basis measurements on B; scrambling projects the spatial transfer matrix onto permutation sectors; the channel assigns each sector a Choi-dependent weight. Convergence **exponential in time**, with moment-dependent prefactors separating relaxation rate from time-to-accuracy (design times vs asymptotic rates).
2. **Global Haar dynamics** (U₁ → N → U₂): two-step argument — (i) Haar-average the moments (first U₁ makes the error-site input near-maximally mixed, so the post-channel state embeds the Choi state via Stinespring dilation; U₂ makes the embedding Haar-random → Ginibre X), (ii) **concentration of measure** lifts the average to typical instances. Key Lipschitz bound: ‖ρ^(k) − ρ′^(k)‖₁ ≤ (2k−1)‖ρ − ρ′‖₁. Averaged moment approaches CIE exponentially in N_B.
3. **Local Haar-random circuits at large local dimension**.
4. **Numerics** (beyond solvable points): random unitary / reset / random Kraus channels in random dual-unitary circuits, local Haar circuits, and kicked Ising — deviations decay as D_B^{−1/2} ∝ 2^{−N_B/2}.

**Replica continuation (technical lever).** Born weights P_α^{1−k} prevent direct k-copy contraction: contract r = k+q replicas with q traced (all copies share outcome α), forming trace-normalized raw moments; analytically continue q → 1−k to recover physical moments. Equality of raw moments at all positive integer orders ⇒ equality of Born-weighted moments.

## Protocols

### P1 — Benchmarking emergent randomness under noise
1. Run the noisy circuit; measure complement B completely each shot; record conditional states ρ_A(α) and Born weights P_α.
2. Estimate moments ρ^(k) for k = 1, 2, 3 (k=2: purity fluctuations; k=3: eigenvalue statistics).
3. Build the CIE reference from the *assumed or independently characterized* error channels: M = ⊗ M_{N_i}; sample X ~ Ginibre; compute ρ_M^(k) by Monte Carlo over X.
4. Deviation metric: normalized Schatten distance Δ^(k) = ‖ρ_NA^(k) − ρ_ref^(k)‖ / ‖ρ_ref^(k)‖; exponential decay in time/N_B confirms the theory; the plateau value diagnoses whether your channel model's Choi spectrum is right.

### P2 — Choi-spectrum noise spectroscopy (inverse use)
1. Collect the late-time MSPE (only the conditional-state distribution is needed — error times/locations may be unknown).
2. Fit the Choi spectrum {λ_1 ≥ λ_2 ≥ …} of M (trace-1 PSD constraint, D_C = d^{2n}) by matching observed moments ρ^(k) against CIE predictions.
3. Several well-separated errors ⇒ recovers the **joint** Choi spectrum without identifying individual channels.
4. Ground-truth test: engineer mid-circuit partial resets (known Choi spectrum) and check the predicted ensemble; finite-time corrections probe the input–output structure beyond spectrum.

### P3 — Generating correlated random mixed states
To sample "scrambled-and-noised" conditional states synthetically: pick desired Choi spectrum Λ, set M = VΛV† (any V), draw Ginibre X, output ρ_M(X). Captures the correct fluctuation statistics that iid Hilbert-Schmidt sampling misses.

## Assumptions / Pitfalls

- **Dilute errors only**: channels must be separated by long scrambling regions; finite error density is open — correlated effective Choi state is conjectured but unproven there.
- **Complete measurement of B with all outcomes retained**; mixedness must come entirely from the physical channel (not from discarded measurement data).
- **Replica-continuation assumption** is used in the dual-unitary derivation (standard in the design/design-time literature, but state it when porting).
- Universality is **spectrum-only for the limit**; transient (pre-asymptotic) corrections can distinguish channels with identical spectra — don't over-interpret early-time deviations.
- Moment-order dependence of convergence prefactors: high-k moments need longer times (design time ≠ asymptotic rate).
- Conserved quantities/symmetries alter the limiting ensemble (as in pure-state deep thermalization) — the CIE here assumes no nontrivial conservation laws.

## Connections

- Extends pure-state deep thermalization (projected ensembles → Haar) and the generalized Hilbert–Schmidt ensemble (complete depolarization) to a one-parameter family interpolating via Choi spectrum.
- Choi state as "macroscopic data surviving scrambling" parallels FOGI-coordinate noise models in randomized benchmarking (arXiv:2610.31500).
- NISQ benchmarking via emergent randomness: replace Haar reference with CIE.
- Gibbs-sampler/MLSI line (arXiv:2610.31571 skill: size-independent-mlsi-quantum-gibbs): both are "universal late-time law" results for noisy quantum dynamics; here the invariant is the Choi spectrum rather than a log-Sobolev constant.
