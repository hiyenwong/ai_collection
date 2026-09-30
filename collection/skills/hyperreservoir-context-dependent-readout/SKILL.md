---
name: hyperreservoir-context-dependent-readout
description: Context reservoir bilinearly modulates shared reservoir readout.
category: ai_collection
---

# HyperReservoir — Context-Dependent Time-Series Prediction via Readout-Level Modulation

Source: arXiv:2609.34847 (Tsuchiyama, Mihana, Horisaki, Röhm — University of Tokyo, 28 Sep 2026, cs.LG/nlin.AO).

Use when: time-series prediction spans multiple dynamical regimes (changing bifurcation parameters, multiple systems, or same attractor at different speeds); deciding WHERE context should enter a reservoir (input vs state vs readout); Conceptor or parameter-aware ESN underperforms because regimes share state-space geometry; physical reservoirs where only linear-regression training is affordable.

## Core idea

Context should not necessarily change the recurrent representation — often it should change **how a shared representation is decoded**. HyperReservoir = main reservoir (observed dynamics) + smaller context reservoir (contextual signal), coupled only through a **bilinear readout**: the context state parameterizes the effective output matrix applied to main-reservoir features. All training remains a single ridge regression; no backprop, both recurrent subsystems fixed after init.

## Architecture (Eqs. 8–11)

- Main reservoir h^R_t ∈ R^N driven by observed state u_t: standard leaky ESN, fixed J^R, W^R_in.
- Context reservoir h^H_t ∈ R^M (M ≪ N) driven ONLY by context c_t: fixed J^H, W^H_in.
- Augmented readout features: ψ_t = [h^R_t; h^H_t; h^H_t ⊗ h^R_t] (Kronecker).
- Prediction: ŷ_t = W^R h^R_t + W^H h^H_t + W^RH (h^H_t ⊗ h^R_t) + b — all coefficients by ridge regression (λ=1e-4).

## Central interpretation (Eq. 14)

Partition W^RH into M blocks B_m ∈ R^(Dout×N). Then the effective readout is affine in the context state:
**W_eff(h^H_t) = W^R + Σ_m h^H_t,m · B_m**
W^R = context-independent baseline; the bilinear term = context-dependent correction. This is a hypernetwork restricted to the readout: shared predictive structure stays in W^R, only the regime-dependent part of the mapping changes.

## The three context-injection points (the paper's taxonomy)

| Architecture | Where context acts | Assumption | Failure mode |
|---|---|---|---|
| Context-input ESN | external input u_t | shared state + shared readout decode all regimes | context barely separates trajectories when regimes are similar |
| Full-matrix Conceptor | state space: x_{t+1} = C_k x̃_{t+1}, C_k = R_k(R_k+γ⁻²I)^(−1) from context-k state correlations | regimes induce distinguishable state distributions | fails when attractor geometry is SHARED (slow vs fast same orbit) |
| HyperReservoir | readout only | representation can stay shared; the mapping to output changes | — |

Key diagnostic: for temporal scaling ṡ = ν_c·f(s), changing ν_c leaves continuous-time orbit geometry unchanged — the ONLY contextual distinction is traversal rate, invisible to Conceptor's state-correlation operator (slow/fast Conceptors stay aligned, Frobenius cosine S_C = 0.813±0.023) but decodable from a shared representation.

## Experimental protocol (reusable)

Three settings, escalating shared-ness of geometry:
1. **Geometrically distinct**: Lorenz vs Rössler (one-hot 2-dim context).
2. **Related regimes**: Rössler c_R ∈ {3.5, 5.7}.
3. **Shared attractor, different speeds**: same Rössler, vector field scaled by ν ∈ {0.5 slow, 1.5 fast}.

Controls: total recurrent states fixed at N+M=120 for all architectures; M swept over {2,5,10,20,40} (validation-selected: (N,M)=(110,10) Lorenz–Rössler, (115,5) for the other two); RK4 integration step 0.005, sampling 0.05; 256/64/64 train/val/test trajectories; 3 reservoir seeds; one-step-ahead prediction H=1 (observed state fed each step, no autonomous rollout); shared normalization statistics across regimes (preprocessing must not leak regime identity); 20-sample washout; metric = component-normalized MSE (cNMSE).

## Results

- HyperReservoir lowest mean test cNMSE in ALL three settings; advantage grows as geometry becomes more shared (weakest on Lorenz–Rössler where ESN≈Conceptor; largest on same-attractor-different-speed where Conceptor ≈ 1 order of magnitude WORSE than plain ESN).
- **Readout ablation** (same reservoirs, different features): Concat [h^R; h^H] and Strict [h^H⊗h^R] alone both lose to Augmented — need additive + bilinear together. Strict has comparable fitted-coefficient count, so it's not a dimension story.
- **Context dependence** R_ctx = (E11+E22)/(E12+E21): HyperReservoir shows the SMALLEST ratio — its accuracy collapses most when context is swapped on a fixed trajectory, i.e. it functionally uses context, not just trajectory shape.
- **M non-monotonic**: beyond validation-selected M, accuracy drops even as fitted coefficients grow — reallocating states from main to context reservoir is a genuine trade-off (bilinear features N·M = M(120−M) grow while representational capacity of main reservoir shrinks).

## Pitfalls & guidance

- Conceptor needs regimes with distinguishable state distributions — if your contexts share attractor geometry (temporal scaling, amplitude changes), switch to readout modulation.
- Don't feed predicted states back during evaluation here — this is short-horizon prediction, not autonomous attractor generation; report which.
- Context must be explicitly supplied and constant within trial; unknown/switching context inference is NOT addressed.
- Small context reservoir suffices (M=5–10 of 120); resist enlarging it.
- Ridge λ=1e-4 fixed works across all three settings; Conceptor aperture γ needs validation sweep (4/1/1 here).
- The bilinear block is O(N·M·Dout) coefficients — for physical reservoirs with large N, keep M tiny.

## Extensions

- Continuous context (regression instead of one-hot) falls out naturally since h^H_t is a smooth function of c_t — potential interpolation to unseen regime values (untested).
- Complementary to multifunctional reservoirs: multifunctionality without requiring multiple attractors — different computations = different temporal evolutions on common state-space structure.
- Pair with hardware reservoirs (photonic/NEMS/spin-torque): the main substrate stays untouched; only the trained readout differs per regime.

## Related skills

- `nems-multimode-reservoir-drive-diversity`, `dynamical-diversity-reservoir-computing` (nanomechanical multi-mode reservoirs — natural HyperReservoir substrates)
- `parametric-oscillator-reservoir-computing`, `memristor-reservoir-computing-image`
- `early-reservoir-evolutionary-learning`, `context-modulated-emrnn-memory` (context modulation at RNN level)
