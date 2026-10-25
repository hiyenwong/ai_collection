---
description: Use when choosing among quantum f-divergence extensions.
name: retrodictive-quantum-f-divergences
category: ai_collection
version: 1.0
author: info-cron-2026-10-25
license: MIT
metadata:
  hermes:
    tags: [quantum-information, f-divergence, petz-transpose, retrodiction]
    related_skills: [oneshot-entanglement-petz-hypothesis-testing, fvqkd-rocq-qkd-formal-verification]
---

# Retrodictive Tests Unify Quantum f-Divergences (Buscemi, arXiv:2610.29696)

**One-line**: All standard extensions of a classical f-divergence to quantum states (standard/Petz, maximal/Matsumoto, geodesic) are the SAME variational minimum — min classical D_f between forward and reverse stochastic processes over all "quantum-inside" implementations — differing only in the reference state γ used for Petz-transpose retrodiction. Changing γ changes the comparison, not the task.

## When to use
- Deciding which quantum f-divergence (standard vs maximal vs geodesic) fits a problem
- Giving an operational/classical-replay interpretation to Petz transpose or a relative entropy
- Variational bounds: any D_f(R‖F) computed by hand lower-bounds the family; spectral choices are certifiably optimal
- Quantum entropy production of a channel with faithful Choi operator
- Proving convexity/log-mixture inequalities operationally (mix optimal implementations)

## The construction (recipe)
1. Fix faithful ρ, σ (the prescribed average preparations) and a reference state γ on the same finite-dim system.
2. Form the relative density operators **A = γ^(-1/2) ρ γ^(-1/2)**, **B = γ^(-1/2) σ γ^(-1/2)**.
3. An *admissible implementation* = two weighted POVM resolutions Σᵢ λᵢEᵢ = A, Σⱼ μⱼHⱼ = B (arbitrary finite POVMs, noncommuting allowed, zero weights allowed). All ensemble/probability freedom is equivalent to this pair.
4. The reference coupling J_ij = Tr[√γ Eᵢ √γ Hⱼ] ties preparation to measurement by Petz transposition relative to γ: preparing τᵢ then measuring {Hⱼ} is the Bayesian-inverse pair of preparing υⱼ then measuring {Eᵢ} at prior γ.
5. Record laws: **F_ij = λᵢ J_ij** (forward: prepare for ρ, measure), **R_ij = μⱼ J_ij** (reverse: prepare for σ). Likelihood ratio on positive records is simply R_ij/F_ij = μⱼ/λᵢ.
6. Optimize: **V_f(ρ,σ;γ) = min over implementations of D_f(R‖F)**.

## The theorem (simultaneous spectral optimality)
The spectral decompositions A = Σₖ αₖPₖ, B = Σₗ βₗQₗ attain the minimum

**V_f(ρ,σ;γ) = Σ_{k,l} αₖ f(βₗ/αₖ) · Tr[√γ Pₖ √γ Qₗ]**  (= Petz quasi-entropy S_f^{√γ}(B‖A))

simultaneously for EVERY operator-convex f with f(1)=0. The optimizer depends on (ρ,σ,γ) but not on f.

Proof pattern (reusable): apply operator Jensen twice — first trace against γ-weighted effects to replace B's resolution by its spectral one, then use the conjugate generator f̃(u)=u f(1/u) to do the same for A; zero weights handled by λᵢ→λᵢ+ε limit. Spectral choices give equality by functional calculus.

## Reference menu (the whole zoo from one dial)
| Reference γ | Divergence recovered | KL specialization f(u)=u log u |
|---|---|---|
| γ = I/d (flat) | standard quantum f-div (Petz); Nussbaum–Szkoła record laws | Umegaki D(σ‖ρ) |
| γ ∈ {ρ, σ} (endpoints) | maximal quantum f-div = Matsumoto reverse-test optimization | Belavkin–Staszewski |
| γ_t = σ^t/Tr[σ^t], t∈[0,1] (power) | geodesic quantum f-div (Capel–Costa Rico) | D_t interpolating Umegaki→BS |

Closed forms (all numerically verified 2026-10-25, 24/24 checks, err ≤ 1e-13):
- General γ, KL: **V(ρ,σ;γ) = Tr[γ B log B] − Tr[σ log A] = D_BS(σ‖γ) − Tr[σ log A]** (Cor. 3.3)
- Flat: V = Tr[σ(log σ − log ρ)]
- Endpoint γ=ρ: V = Tr[ρ B log B]; BS also equals −Tr[σ log(σ^(-1/2) ρ σ^(-1/2))]
- Geodesic: **D_t(σ‖ρ) = (1−t)·Tr[σ log σ] − Tr[σ log(σ^(−t/2) ρ σ^(−t/2))]**; t=0 → Umegaki, t=1 → BS; superoperator form ⟨√ρ, f(Γ_t)(√ρ)⟩_HS with Γ_t(X)=σ^(1−t) X ρ^(−1/2) σ^t ρ^(−1/2) matches this closed form (verified via vec/kron eigendecomposition at t=0.25, 0.5).

## Channel extension
Insert any channel E between preparation and measurement (Petz transpose R_γE in the reverse process): min becomes Σ αₖ f(βₗ/αₖ) Tr[Qₗ E(√γ Pₖ √γ)], with A,B built from γ, η=E(γ). The f(u)=−log u orientation reproduces average entropy production (Bai–Buscemi–Scarani) for faithful-Choi channels.

## Convexity, operationally
At fixed γ: V_f(Σ pₖρₖ, σ; γ) ≤ Σ pₖ V_f(ρₖ, σ; γ) — combine per-k optimal implementations sharing the σ-side spectral resolution, keeping k in the record. KL case strengthens to the **log-mixture bound**: V(mix) ≤ −log Σ pₖ exp[−V(ρₖ,σ;γ)] ≤ Σ pₖ Vₖ (i.e. exp[−V] concave in ρ). Verified numerically.

## Pitfalls / sharp edges
1. **ρ = σ does NOT give V = 0 unless [ρ,γ] = 0** (verified: ρ=σ, non-commuting γ → V=1.34>0). Two identical states can be distinguished by their implementations — the pair of prescribed states does not determine the minimum.
2. Commuting (diagonal) ρ,σ,γ collapse to classical KL, **γ-independent** — any reference gives the same number; noncommutativity is where the reference matters.
3. The two *separate* reverse-test divergences D_f(F‖J)=D_f(a‖g), D_f(R‖J)=D_f(b‖h) do NOT determine the coupled D_f(R‖F) — the coupling J carries irreducible information.
4. BS relative entropy has several equivalent forms (Tr[ρB log B], −Tr[σ log A], Tr[σ log(σ^(1/2)ρ^(−1)σ^(1/2))]) — all agree only with the correct A,B; re-derive rather than mix conventions.
5. Endpoint references turn the retrodictive test into a single Matsumoto reverse test (one preparation device, two input laws p,q); minimal D(q‖p) also = least classical information gain (Bayesian update) explaining ρ→σ as learning about an unchanged source.

## Minimal verification snippet (numpy, ~30 lines)
Random faithful states (W W†/tr); Hermitian log via eigh; V via the Tr[γB log B]−Tr[σ log A] closed form; assert: flat γ → Umegaki; γ=ρ → all BS forms equal; commuting → classical KL; spectral double-sum == closed form; geodesic t via kron-superoperator eigendecomposition == closed form; log-mixture bound ≤ linear. All pass at 1e-13 in the 2026-10-25 run (script: ~/.hermes/cache/scratch/info1025_verify_qfd.py).

## Cross-links
- oneshot-entanglement-petz-hypothesis-testing (arXiv:2610.31501, same batch): Petz *recovery* fidelity via binary hypothesis testing — the same Petz map serving distinguishability from the channel-coding side.
- fvqkd-rocq-qkd-formal-verification (arXiv:2610.30645): security = chain of distinguishability bounds; retrodictive tests give the operational ground meaning of each link.
- kl-minimality-distribution-reconstruction: KL uniqueness among smooth f-divergences — here the quantum side keeps f free and moves the arbitrariness into γ instead.
