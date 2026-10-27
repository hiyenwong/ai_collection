---
name: model-free-stealthy-attack-cps
description: Use when auditing model-free stealthy attacks on CPS.
category: ai_collection
---

# Model-Free Generative Stealthy Attacks on Safety-Critical CPS

Source: arXiv 2610.31864 — "Model-Free Generative Stealthy Attacks on Safety-Critical Vehicle Cyber-Physical Systems" (Mairaj ud din, Bhatti, Ahmed; OSU Center for Automotive Research; submitted 2026-10-22). Code: github.com/OSU-CAR-MSL/model_free_stealthy_attack

## Problem
Classical stealthy False-Data-Injection theory (Liu et al. χ²-masking, residual reflection) presumes white/grey-box access: plant model, Jacobians, estimator gains, noise covariances, detector thresholds. Real CAN/J1939 attackers hold only: (i) read/overwrite of unauthenticated frames, decodable via public specs (SAE J1939) or reverse-engineered DBCs (opendbc); (ii) long passive eavesdropping of nominal operation; (iii) deployment operating distribution matching the nominal recording. The framework learns an attack policy purely from nominal data — no plant f(·), sensing map h(·), estimator internals, or detector parameters.

## Core methodology — four structural requirements (R1–R4)

### R1: Stealth-consistent anchor + certified isotropic budget
Residual-based detectors test consistency with the observer-induced measurement manifold M (= col(H) linear; curved immersion for nonlinear h). Anchor Π is a map whose fixed set is M; the attack is a displacement d_k about the anchor.
- **Certified budget (Rayleigh quotient):** with detector statistic g_k = r_k^⊤ S^{-1} r_k, ANY displacement with ∥d_k∥ ≤ ρ := √(η·λ_min(S)) guarantees g_k ≤ η in ALL directions — the largest isotropically stealthy ball. Holds for any anchor and any (linear/nonlinear) h, using only Euclidean geometry.
- **Observable (model-free) surrogate:** S is attacker-unknown; instead enforce |y^a_k − Π(y_k)| ≤ τ with τ = the (1−ε) percentile of nominal anchor residuals — same false-alarm operating point ε, empirical quantile replacing the model-dependent covariance.
- **AE as manifold anchor:** a regularized autoencoder minimizing E∥z(y)−y∥² + σ²∥∂z/∂y∥²_F has, as σ²→0, reconstruction residual z(y)−y ≈ σ²∇_y log p(y) (score matching): the residual estimates the score, vanishes to first order on M, giving manifold-distance proxy ∥y−AE(y)∥² ≈ dist(y,M)². In the linear case AE == PCA == orthogonal projection onto col(H) exactly.
- **Bottleneck dimension = observability rank:** nz = rank dG(x) via the Hermann–Krener co-distribution (differentials of iterated Lie derivatives of the joint output map along admissible vector fields), NOT the state dimension. nz > n_M recovers nothing; nz < n_M discards observable structure; the gap nx − n_M measures structurally invisible state. Estimate model-free with a maximum-likelihood intrinsic-dimension estimator on nominal windows, confirmed by a reconstruction-error plateau over nz.

### R2: Certified residual→impact proxy (make the unobservable objective observable)
Under L-Lipschitz h and noise covariance R ⪯ σI, for any α > 0, concentration κ: with probability ≥ 1 − p/κ² (multivariate Chebyshev), residual ∥r_k∥ ≥ α ⟹ true prior estimation error ∥∆x_k∥ ≥ (α − σ√κ)/L. Non-vacuous above the noise floor. Hence maximizing the observable surrogate L_impact = E∥ỹ^a_k − y^a_k∥² provably maximizes a certified lower bound on true impact E∥∆x_k∥².

### R3: Recurrence is a structural necessity (temporal coupling)
- **Integrated-bias recursion:** the attack-induced estimation bias obeys ε_{k+1} = A·ε_k − A·K·∆r_k, independent of the injection itself; solution ε_k = −Σ A^{k−j} K ∆r_j.
- **Modal amplification:** projected on a plant mode (right/left eigenvectors ϕ,ψ, ψ^⊤ϕ=1): ψ^⊤E[ε_k] = −(ψ^⊤Kδ̄)·Σ_{m=1}^{k−k0} λ^m — converges to −cλ/(1−λ) for |λ|<1; grows linearly (semisimple λ=1) or polynomially by Jordan index (defective); geometrically for |λ|>1.
- **Impact per detectability:** for past-measurable (deterministic, history-dependent) injections, Cov is preserved to first order and E[g_k] = p + ∥∆r_k∥²_{S⁻¹} — the detector mean shift is the CONSTANT ∥δ̄∥²_{S⁻¹}, horizon-independent, while accumulated impact on a unit-circle mode (ψ^⊤Kδ̄ ≠ 0) grows WITHOUT BOUND at the fixed nominal false-alarm rate. A per-sample residual statistically indistinguishable from nominal is compatible with arbitrarily large accumulated state deviation — the amplification is a property of the plant's marginal modes, not the injection.
- **Consequence (Proposition — insufficiency of memoryless laws):** holding the residual deviation at ∆r_k = δ̄ requires injection a_k = δ̄ − C·ε_k, a FUNCTIONAL of the accumulated deviation; in the exact-stealth limit the admissible offset must itself evolve as a free plant trajectory c_{k+1} = A·c_k (dynamically stealthy constant offset only in ker(A−I), the integrator subspace). A memoryless law a_k = φ(y_k) cannot represent this history dependence — the attack law must be CAUSAL RECURSIVE: s_k = G_θ(s_{k−1}, y_k), a_k = W_θ(s_k).
- **Stability dichotomy:** accumulated bias unbounded iff a unit-circle mode is excited; unstable modes (|λ|>1) forfeit stealth because holding the bias needs an injection that leaves the nominal manifold geometrically.

### R4: Context conditioning is a structural necessity (spatial coupling)
Partial compromise: target block y^a attacked, context block ξ uncompromised, joint innovation covariance S = [[S^a, M],[M^⊤, S^ξ]] with cross-covariance M ≠ 0 whenever channels are jointly informative about the shared state (independent noises, dependent residuals). Stealth over the FULL sensor set requires preserving the nominal cross-statistics E{ã(r^ξ)^⊤} = 0-equivalent (E{a_k (r^ξ_k)^⊤} = 0), impossible for a map of y^a alone since Cov(y^a, r^ξ) ≠ 0 — the injection must be conditioned on ξ_k. Additionally the accumulated deviation ε leaks into the CONTEXT residual one step later (∆r^ξ_{k+1} = (C A ∆e_k)^ξ), so the budget must be met on the joint residual.

## Realization: recurrent context-conditioned cWGAN-GP
1. **Anchor training (frozen thereafter):** recurrent (LSTM) autoencoder Π predicting the target channel from strictly-past target history (y^a_{k−1..k−L}) and current/past context (ξ_{k..k−L}); δ_k = y^a_k − ŷ^a_k.
2. **Generator:** also recurrent; internal state s_k = G_θ(s_{k−1}, [target history, context history]); emits displacement d_k = W_θ(s_k, z_k) with z_k ~ N(0,I) (stochastic policy — attack is a distribution, not one trajectory); recentered output: ỹ^a_k = ŷ^a_k + d_k, injected attack a_k = d_k − δ_k. The recentering means the network learns ONLY the stealth-consistent correction about the anchor, not the full measurement.
3. **Loss:** min_θ L_adv + λ_s·L_stealth − L_impact, where
   - L_adv: Wasserstein critic (cWGAN-GP) on the JOINT (target, context) distribution — distributional stealth (Prop. R4);
   - L_stealth = E (h_k)²₊, hinge on budget violation h_k = |r^att| − τ (pointwise certified budget surrogate);
   - L_impact = E∥ỹ^a_k − y^a_k∥² (certified-lower-bound surrogate of true impact).

## Validation ladder (transferable evaluation pattern)
1. **MiL benchmark with known dynamics** (IoT electric-vehicle CPS, Ts=1 ms; states β, ψ̇, ψ, y_lat; LQR + feedforward; EKF + χ² detector): verify every theorem against ground truth, ablate each objective term and architecture choice.
2. **Real heavy-vehicle CAN data, offline:** transfer beyond simulation to heterogeneous real signals.
3. **Real-time Hardware-in-the-Loop** (dSPACE / J1939 truck-in-the-loop): feasibility on real-time hardware.

**Results:** 2.51 m peak lane departure (0.77 m sustained) with detector statistic 2.94 < nominal threshold 3.01, evading five SOTA IDSs (CANet, INDRA, NeuroCAN, DL LSTM-GNB, CNN-LSTM-GNB) at 1% FPR; ≈8 km/h speed deviation on the HiL truck while staying below the detection threshold. Removing recurrence or context conditioning breaks stealth (ablation).

## Defense implications (offense-informed hardening)
- Residual-based detectors are structurally blind to past-measurable bias riding marginal plant modes: monitor ACCUMULATED state deviation and mode-aligned bias, not per-sample innovation magnitude.
- Cross-channel coupling means single-channel integrity is insufficient; add message authentication (MAC) especially where channels share state.
- The amplification channel is the plant's unit-circle modes — design observers/controllers so integrated bias on marginal modes becomes detectable (shift the eigenstructure of A(I−KC) detectability for bias, not just noise).
- The anchor is trained on nominal data only — defenders can run the SAME AE residual monitor as a cheap manifold-distance anomaly signal.

## Activation
model-free attack, stealthy false data injection, CPS security, CAN J1939, intrusion detection evasion, Wasserstein GAN attack, residual-based detector, chi-square detector, autoencoder manifold anchor, stealth budget, innovation statistic, hardware-in-the-loop security test, recurrence context conditioning.