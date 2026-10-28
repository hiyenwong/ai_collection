---
description: Use when adding quantum Born priors to JEPA world models.
name: quantum-jepa-born-prior-world-models
category: ai_collection
version: 1.0
author: cs-cron-2026-10-27
license: MIT
metadata:
  hermes:
    tags: [jepa, world-models, quantum-born-machine, qcbm, latent-actions, energy-score, parameter-shift, proper-scoring-rule, multimodal-prediction, multi-agent-coordination, quantum-generative-model, stochastic-world-model]
    source: arXiv:2610.27921
    related_skills: [fc-qbm-quantum-attention-lm, dreaming-world-action-models, hallucination-prediction-world-models, agentic-phase-diagram-mapping, mcts-quantum-encoding]
---

# Quantum-JEPA: Conditional Quantum Born Priors for Latent-Action JEPA World Models

Methodology from arXiv:2610.27921 — "Quantum-JEPA: Quantum Born Priors for Latent-Action JEPA World Models" (Z. Liu, S. Liu, H. Wu; Qinous Technology + Tsinghua + Notre Dame; cs.AI, 20 Oct 2026).

## One-Line Summary

A stochastic JEPA world model whose "unobserved action" distribution is a conditional quantum circuit Born machine: circuit measurements sample binary latent actions z, one shared predictor maps each z to an alternative future representation, and the prior is trained ONLY through the quality+diversity of those predictions via a sampled energy objective — avoiding both the 2^n categorical output layer and statevector differentiation (finite-shot parameter-shift works, including readout noise; trained priors run on a real QPU).

## When to Use / Activation

- Modeling multimodal futures (several plausible continuations per observation) in representation space (JEPA-style), especially with a generative prior.
- Replacing categorical/mixture/AR priors over binary latent codes with a parameter-efficient correlated sampler.
- Coordinating multi-agent futures where the JOINT distribution of per-agent latent bits matters (entanglement as the correlation carrier).
- Training quantum circuits through downstream predictive cost instead of differentiating quantum states (measurement-based, hardware-compatible).
- Auditing whether a stochastic model's coordination is real: re-pair agents' predictions and compare joint vs marginal validity.

## Core Mechanism (equation-level)

1. **Setup (Eq. 1-2):** shared encoder f_ξ gives h = f_ξ(x), t = f_ξ(y); prior `p_θ(z|h)` samples z ∈ {0,1}^n; shared predictor `bt = P_ψ(h, z)` yields the random future representation `bT | x ~ Q_ξψθ(·|x)`.
2. **Conditional Born prior (Eqs. 3-4):** conditioner g_η (2-layer SiLU MLP, zero-init output) maps h → per-layer RY angles: `α_ℓj(h) = g_η(h)_ℓj + ϑ_ℓj + (π/2)·1[ℓ=1]`; ansatz `U = [∏_j RY(φ_j)] ∏_ℓ [E_ℓ ∏_j RY(α_ℓj)]` (E_ℓ = CNOT matching or identity for the product circuit); `p_θ(z|h) = |⟨z|U|0^n⟩|²`. The π/2 first-layer offset gives near-uniform initial support (Hadamard-like); terminal RY(φ_j) are trainable local readout bases shared across observations.
3. **Shared predictor (Eqs. 5-6):** bit embedding u(z) = MLP(2z−1), context c(h) = W_h h + b, then RESIDUAL transition with multiplicative interaction: `P_ψ(h,z) = N(h + W₂σ(W₁[c(h); u(z); c(h)⊙u(z)] + b₁) + b₂)`. Input width grows linearly in n — parameters shared across all 2^n joint codes.
4. **Sampled predictive objective (Eq. 7):** with K ≥ 2 prior samples and ρ(u,v) = ‖u−v‖₂/√d,
   `L_pred = (1/K) Σ_k ρ(bt_k, t) − (1/(2K(K−1))) Σ_{k≠l} ρ(bt_k, bt_l)`
   — the Gneiting-Raftery **energy score**: fit-to-target minus ½·diversity. Excluding self-pairs makes it unbiased; when several realized futures share one observation, AVERAGE the fit term over those targets (or the optimum collapses to a point mass on the single target).
5. **Encoder anti-collapse (Eqs. 8-9):** VISReg on both views (decoupled centre/scale/shape regularizers) — the encoder could otherwise cheat the predictive score by making features uninformative.
6. **Prior updates (Sec. 3.4):**
   - Classical prior: leave-one-out cost `C_k^LOO = ρ(bt_k,t) − (1/(K−1)) Σ_{l≠k} ρ(bt_k, bt_l)`; surrogate `L = (1/K) Σ_k log p_θ(z_k|sg(h))·sg(C_k^LOO)` (REINFORCE-style, gradient confined to prior).
   - Quantum measurement-based (Eq. 14): per angle a_j, `∂L/∂a_j = ½[ E_{z∼p_{a+π/2 e_j}} C(P_ψ(h,z); t, Q) − E_{z∼p_{a−π/2 e_j}} C(·) ]` with first-variation cost `C(u; t, Q) = ρ(u,t) − E_{V∼Q} ρ(u,V)` (Eq. 11); **Q = reference distribution from independent UNSHIFTED predictions, held fixed during the shift**; angle derivatives backprop through the classical conditioner (sg(h)) — no statevector differentiation. Valid under parameter-independent readout-error channels.
7. **Resource scaling:** at fixed depth L, QCBM params/gates grow LINEARLY in n with no 2^n output layer; correlated bits come from ONE circuit execution per draw (D3IL: 4,792 prior params vs Softmax-Categorical 15,792 — 69.7% reduction; AR-GRU 10,641; Mixture-4 5,012).

## Empirical Calibration (paper tables)

- **MovingMNIST** (product-representable targets): Entangled-QCBM validity 96.5 ± 1.1, close to best classical (Uniform-Bernoulli 96.5, Softmax-Categorical 95.8); entanglement NOT required when the target factorizes — Product-QCBM matches.
- **HEP18** (4-agent intersection, 18 coordinated futures, per-agent predictors isolated to their own action bits): **Entangled-QCBM coverage 99.73% / validity 93.38% under 0.5% readout flips + finite-shot parameter-shift; Product-QCBM coverage only 38.77%** — entanglement is the coordination carrier. Re-pairing agents: joint validity 93.38% → 12.71% while 96.61% stay individually valid — coordination lives in the prior's correlations, not marginals.
- **D3IL Avoiding** (96 human demos, 24 routes, direction-free recursive prediction from one shared point): QCBMs 18.01 routes / 75.06% coverage / TV 0.419 ≈ Softmax-Categorical (75.33%) and AR-GRU (73.54%); shared nonlinear predictor + recursive re-encoding can map product-distributed codes into correlated routes when one global predictor mediates — the D3IL setting does NOT establish a stable entanglement advantage (honest negative).
- **Real-QPU inference:** hardware noise shifts the action distribution; qubit/connection selection (no retraining, no circuit change) lifted HEP18 12-qubit joint validity 76.88% → 86.69% (ideal 98.41%); D3IL recursive rollouts within GPU-sampling ranges.
- **Honest limits:** quantum priors do not consistently beat strong classical methods on all metrics; circuits are shallow; measurement costs substantial at scale.

## Validation Replay (5/5 passed, numpy-only statevector, this workspace)

- T1 conditional prior: p(z|h) Born-normalized; different h → different distribution (L1=1.106); zero-init conditioner + π/2 offsets → exact uniform initial support (dev 0.0000) ✓
- T2 energy-score estimator: Eq. 7 (denominator **2K(K−1)**, self-pairs excluded) is unbiased (bias −0.00097 ± 0.0031); naive 1/K² divisor biased UP by ey/(2K) = +0.0442, observed +0.0429 ✓
- T3 parameter-shift (Eq. 14, fixed Q reference): matches finite-diff gradient to 1e-6 — ps=[−0.406917, −0.073304] = fd ✓
- T4 coordination: target = correlated bits {00,11}; parameter-shift-trained Entangled-QCBM TV = 0.009 vs Product-QCBM TV = 0.490 (product cannot represent the correlation; optimal product = uniform) ✓
- T5 re-pairing audit: trained entangled prior joint validity 0.990 → 0.503 after permuting agent-2 bits across scenes, per-bit marginals preserved exactly — coordination is genuinely in the joint distribution ✓

## Pitfalls (learned from replay)

- **Eq. 7 denominator is 2K(K−1)** — the ½ of the standard energy score. Dropping it (or dividing by K(K−1) without the 2) changes the fit-diversity balance; including self-pairs with a 1/K² divisor biases the estimate UP by ey/(2K).
- **Single-target collapse:** with ONE realized future per observation, the energy-score optimum is a point mass on that target (diversity term alone can't create the mixture). Multi-future observations MUST average the fit term over their realized futures; multi-mode marginals arise from conditioning across different observations, not from one observation.
- **Q reference must be FIXED during the shift:** if Q_ref is recomputed at the shifted angles, parameter-shift no longer matches the analytic gradient (observed: ps=[−0.24, +0.02] vs fd=[−0.57, −0.17] until fixed). Use independent unshifted predictions, exactly as the paper specifies.
- **RY gate application on non-trivial states:** must mix both amplitudes (new[r] = c·ψ[r] − s·ψ[r1]; new[r1] = s·ψ[r] + c·ψ[r1]) — single-branch writes silently break normalization on the second layer.
- **Where entanglement pays:** only when (a) targets are genuinely correlated AND (b) the predictor architecture cannot itself create the correlation (HEP18 isolated per-agent predictors). With one shared nonlinear predictor + recursive re-encoding, product bits suffice (D3IL) — report this asymmetry honestly.
- **Coordinate-vs-marginal audit:** re-pairing preserves marginals by construction — compare per-BIT marginals, not the 4-bin joint, when verifying the permutation.

## Relation to Prior Art

- vs Variational JEPA / Branch-JEPA / FlowWM: replaces variational/flow machinery with a sampled discrete prior trained by a proper scoring rule; improves validity + distributional fidelity over variational baselines on controlled tasks.
- vs classical discrete priors (Softmax-Categorical, Mixture, AR-GRU): linear-in-n parameters, one-execution correlated sampling; slight frequency-matching deficit vs the best categorical priors (TV) is the price.
- vs QCBM generative literature (Liu & Wang 2018, Rudolph et al. 2024): first to train the Born prior through downstream JEPA predictive energy rather than matching a data distribution directly, plus readout-noise-robust finite-shot training and real-QPU deployment of the trained prior.
