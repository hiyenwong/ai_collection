---
name: dfe-survival-probability-fidelity
description: "Fidelity estimation via DFE + L2-optimized survival moments."
category: ai_collection
---

# Practical Fidelity Estimation: DFE + Survival-Probability Protocols (arXiv 2610.21606)

**Paper**: Aman, Chatterjee, Javanmard, Pandit (IISER Mohali + DTU + Leibniz Hannover + VTT), quant-ph, 15 Oct 2026.

**Use when**: benchmarking noisy quantum devices without full tomography, choosing between state-structured (DFE) vs dynamics-structured (survival-probability) fidelity estimators, correcting readout attenuation in Pauli measurements, or reconstructing fidelity proxies from return-probability moments under strong noise.

## Two Complementary Protocols

### Protocol 1: Direct Fidelity Estimation (DFE) — state-structured

Estimates F(ρ,σ) = Tr(ρσ) for known pure target ρ via importance sampling over Pauli observables.

1. **Characteristic functions**: X_ρ(k) = Tr(ρW_k)/√d, X_σ(k) = Tr(σW_k)/√d; then F = Σ_k X_ρ(k)X_σ(k).
2. **Sampling distribution**: p(k) = X_ρ(k)² (valid for pure ρ since Σ_k X_ρ(k)² = 1 — verified numerically).
3. **Estimator**: X = X_σ(k)/X_ρ(k) for k ~ p(k); E[X] = Tr(ρσ) exactly (unbiased; MC check err ~1.6e-4 at 200k samples).
4. **Sample counts**: ℓ = ⌈(ε²δ)⁻¹⌉ Pauli indices; shots per index m_i = ln(2/δ²)/([X_ρ(k_i)]² d_ℓ ε²). Accuracy 2ε at confidence 1−2δ; expected preparations scale ≤ linearly in Hilbert dimension.

**Readout-noise correction**: independent bit flips with probability α attenuate a weight-w(k) Pauli string by β_k = (1−2α)^{w(k)} (verified by MC). Divide measured expectations by calibrated β_k (or per-qubit nonuniform coefficients). Works up to ~5% flip rate; amplifies statistical noise when |β_k| small.

**Depolarizing closed form** (useful as test anchor): for pure ρ in dim d, F = 1 − p(1 − 1/d), independent of the specific state (verified to machine precision).

### Protocol 2: Survival-Probability Reconstruction — dynamics-structured

Reconstructs the **adjoint-cycle fidelity proxy** F_Q from return probabilities, avoiding Pauli reconstruction entirely.

1. **Liouville space**: noisy evolution K = U·E (interaction-picture error map E = exp(Σ Ω_i)).
2. **Positive adjoint cycle**: Q = K†K (Hermitian PSD; eigenvalues = squared singular values of K). F_Q = ⟨⟨ρ₀|Q|ρ₀⟩⟩. **Critical honesty point**: F_Q ≠ F_phys unless E is PSD (E†E = E); for depolarizing p=0.2 on 2 qubits F_phys = 0.85 but F_Q = 0.73 — the proxy captures accumulated noise, not exact state fidelity.
3. **Moments via cycles**: R_m = ⟨⟨ρ₀|(K_I K)^m|ρ₀⟩⟩ — apply m forward–inverse cycles, measure return probability. Moments of Q only when the implemented inverse satisfies K_I = K† (a condition on the map, NOT a generic physical guarantee — pulse inverses reverse control Hamiltonian but not the dissipator, giving C ≃ e^{2Ω₁} only when commutator corrections vanish).
4. **Polynomial reconstruction**: F_Q ≈ Σ_{m=0}^{M} c_m R_m, coefficients approximating √λ on spectral interval λ ∈ [g, 1].

## L2-Optimized Coefficients (key contribution)

Instead of naive Taylor expansion of √λ at λ=1 (locally optimal, fails badly at strong noise), minimize the L2 error on the whole spectral interval [g,1]:

```
ϵ_M^{L2}(a) = [ Σ_m a_m² ∫_g^1 λ^{2m} dλ − 2 Σ_m a_m ∫_g^1 λ^{m+1/2} dλ + ∫_g^1 λ dλ ]^{1/2}
```

Stationarity δϵ/δa_m = 0 gives the linear system **G a = b** with:
- G_{mn} = (1 − g^{m+n+1})/(m+n+1)
- b_m = (1 − g^{m+3/2})/(m+3/2)
- c_m = a_m (solved coefficients are the expansion coefficients)

**Verified performance** (g=0.05): M=2: RMS 1.0e-2; M=3: 3.9e-3; M=4: 1.7e-3 — vs Taylor RMS ~0.55 at all M. In the high-noise subinterval [g, 0.3] at M=3: L2 6.2e-3 vs Taylor 0.68. L2 optimization wins by ~2 orders of magnitude in exactly the regime where the paper claims it.

## Spectral Validity Conditions (Appendix A)

- **Lower bound**: λ_min(Q) = s²_min(K) ≥ e^{−2η}, where η = ∫₀ᵀ ‖L(t)‖dt (Gronwall + submultiplicativity). So choose g ≤ e^{−2η}.
- **Upper bound**: λ_max(Q) ≤ 1 requires HS-contractivity — NOT automatic for every channel; verify or enforce by spectral rescaling.
- **Weak-noise regime**: η ≪ 1 and ‖Ω₂+Ω₃+…‖ ≪ ‖Ω₁‖ (first-order Magnus validity). Adjoint-cycle spectrum near 1 means e^{2η}−1 ≪ 1.
- **Pulse-inverse cycle**: C = K_I K ≃ e^{Ω₁}e^{Ω₁^{(I)}} — reduces to e^{2Ω₁} only if Ω₁^{(I)} ≃ Ω₁ and commutators negligible. Coherent errors in the inverse add generators and break the cancellation. Purity losses: ΔP_C = 2ΔP_K.

## Worked Spectral Example (for tests)

Depolarizing channel on n qubits: superoperator eigenvalues are 1 (identity component, overlap² = 1/d for pure state) and (1−p) (traceless, norm² = 1−1/d).
- R_m = (1/d)·1^m + (1−1/d)(1−p)^{2m}
- F_Q = 1/d + (1−1/d)(1−p)² — matches direct ⟨⟨ρ₀|K†K|ρ₀⟩⟩ to machine precision.

## Protocol Selection Guide

| Situation | Use |
|---|---|
| Known classically-simulable target, sparse/structured Pauli representation | DFE |
| Many distinct measurement bases impractical; repeated return experiments accessible | Survival-probability |
| Readout noise dominant | DFE + attenuation correction; or survival (SPAM-insensitive but unquantified) |
| Strong noise (spectrum far from 1) | Survival + L2-optimized coefficients (never Taylor) |
| Target state has high magic (stabilizer Rényi entropy M₂) | Costly — DFE sampling grows ~exponentially with M₂; classical characterization cost becomes part of the benchmarking problem |

## Honest Limitations (paper's own caveats — do not overstate)
- Survival-probability simulations use **exact moments** — no finite-shot or explicit SPAM fluctuations; experimental robustness is NOT established yet.
- SPAM robustness of return probabilities "depends on the implementation and is not quantified" by these simulations.
- A generic physical approximate inverse yields moments of C, not of Q — reconstruction of F_Q requires separately justified cycle-matching.
- DFE needs efficient classical computation of target Pauli coefficients (magic scaling is an open question).

## Related Skills
- [[stableshots-quantum-shot-optimization]] — shot-budget stopping rules
- [[qem-statistical-benchmarking]] — statistical methodology for QEM evaluation
- [[fidelity-estimation-hamiltonian-parameter-estimation]] — MLE-Hamiltonian approaches

## Key References
- Flammia & Liu, PRL 106, 230501 (2011) — original DFE
- Green, Pandit, et al., arXiv:2212.10771 — periodic-driving recurrence diagnostics
- Pandit et al., Quantum 6, 682 (2022) — recurrence witnesses
- Santos, Henao, Uzdin, arXiv:2305.19359 — pulse-inverse constructions
