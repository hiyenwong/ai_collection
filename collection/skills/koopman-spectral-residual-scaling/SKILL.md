---
name: koopman-spectral-residual-scaling
description: "Koopman autoencoder spectral-residual loss for reliable latent-dimension scaling. Use when training KAE/dynamics models and scaling latent dimension."
category: ai_collection
tags: [koopman-operator, spectral-residual, latent-dimension-scaling, resdmd, dynamical-systems, neural-latent-dynamics]
---

# Koopman Spectral-Residual Loss for Latent-Dimension Scaling

**Paper**: Understanding Latent-Dimension Scaling in Dynamical-System Learning through Spectral Reliability (arXiv: 2610.11866, Sakata/Miyauchi/Kawahara, RIKEN AIP + U. Osaka, 2026-10-08)

## Trigger / Activation

Use when: training Koopman autoencoders (KAE) or latent-dynamics models; scaling latent dimension of RNN/world-model latent state; diagnosing why added latent dimensions fail to reduce rollout error; detecting spurious Koopman eigenpairs (spectral pollution); evaluating learned dynamics via pseudospectra rather than one-step error; neural population latent-dynamics models where dimension choice is ad hoc.

**Keywords**: koopman autoencoder, spectral reliability, relative residual, ResDMD, spectral pollution, latent dimension, rollout error, valid prediction time, pseudospectrum, spurious eigenpair, chaotic systems, dictionary learning

## Core Problem

Deep-learning approximation theory says: bigger representation → lower error. For **autoregressive dynamics learning** this is NOT guaranteed: one-step error falls while rollout error can stagnate or grow, because finite Koopman approximations suffer **spectral pollution** — eigenvalues accumulating outside the true operator spectrum even as approximation size increases. Increasing latent dimension N expands representable dynamics but also multiplies opportunities for spurious eigenpairs whose repeated application (Â^t) compounds rollout error.

## Core Method

### 1. Spectral-residual loss replaces latent-prediction loss

Both losses operate on a shared two-stage Koopman autoencoder: encoder φ (R^dx→R^N), decoder ψ, linear latent evolution ẑ_{t+1} = Â ẑ_t.

**Latent-prediction loss** (standard): ‖Z′_Y − Â Z′_X‖²_F / (N·m) over held-out snapshot pairs — one-step error in latent coordinates.

**Spectral-residual loss**: average squared **relative residual** of candidate eigenpairs, evaluated on a HELD-OUT minibatch (disjoint from the estimation minibatch used for Â):

res_c(λ, g)² = Σ_i |g(y⁽ⁱ⁾) − λ·g(x⁽ⁱ⁾)|² / Σ_i |g(x⁽ⁱ⁾)|²

For each eigenpair (λ_k, a_k) of the reduced operator (Âᵀ v_k = λ_k v_k, a_k = U v_k over the ε-retained SVD subspace U), the candidate eigenfunction is g = φᵀ_N a_k and the loss is L_res(θ_e) = (1/r) Σ_k ρ_k², where ρ_k is the empirical residual evaluated on held-out matrices Z′_X, Z′_Y.

**Why held-out**: estimating and scoring on the same batch rewards overfitting the operator to the dictionary; residual evaluation must be out-of-sample.

### 2. Operator estimation (per Stage-2 update)

Snapshot matrices Z_X, Z_Y ∈ R^{N×m} of encoder outputs on (x⁽ⁱ⁾, y⁽ⁱ⁾=F(x⁽ⁱ⁾)) pairs. Regularized least squares:

Â = Z_Y Zᵀ_X (Z_X Zᵀ_X + ε I_N)⁻¹ = Gᵀ_XY (G_XX + ε I_N/m)⁻¹

with Gram/cross-correlation matrices G_XX = Z_X Zᵀ_X/m etc. Retain subspace U from eigenpairs of Z_X Zᵀ_X with eigenvalues κ_j ≥ ε (this ε doubles as the ridge parameter and truncation threshold). Candidate eigenfunction coefficients a_k = U v_k from eigenvectors of the compressed UᵀÂU.

### 3. Two-stage training protocol

- **Stage 1**: update (θ_e, θ_d) with reconstruction loss L_rec — prevents the trivial collapse where all states map to the same latent point (latent-prediction/residual losses alone admit zero or constant observables as degenerate solutions).
- **Stage 2**: freeze decoder θ_d; update ONLY encoder θ_e with either L_pred or L_res. Alternating per epoch (up to J1=J2=250 updates), plateau stopping, 200 epochs.
- Joint training (L = 2·L_evo + L_rec, both nets) also works but two-stage spectral-residual dominates: at 16N₀, two-stage residual VPT longer than joint in all 6 systems.

**Key asymmetry**: Stage 2 updates the ENCODER (dictionary), not the operator — the operator is re-estimated each update from the current dictionary. The loss shapes WHERE the dictionary spends its capacity: prediction loss shapes it for one-step fit; residual loss shapes it so candidate eigenpairs have small out-of-sample residual (spectral reliability).

### 4. Theory (bounded Koopman operators)

Proposition 2.1 (latent-dimension limit): for bounded K on H = L²(Ω, μ; C), if the learned dictionary spaces V_N approximate every observable (E_N(g) → 0 ∀g, non-nested sequences allowed), then τ_N(λ) → τ(λ) pointwise for every λ, where τ_N(λ) = min_{g∈V_N\{0}} res(λ, g) and τ(λ) = inf_{g∈H\{0}} res(λ, g). Uniform on compact sets (Lipschitz bound |τ_N(λ) − τ_N(ζ)| ≤ |λ − ζ|).

Corollary 2.2 (ordered limits): with empirical consistency (A4), the successive limits ϵ↓0, N→∞, M→∞ of the empirical minimal residual τ̂_{M,N}(λ) characterize the approximate point spectrum σ_ap(K).

Interpretation: as the dictionary grows rich enough, the minimal residual over the learned space converges to the true infimum — checking residual contours is a legitimate a-posteriori certificate of where the true spectrum can/cannot be. Eigenvalues placed in high-residual regions are spurious, and their powers poison rollout.

### 5. Spectral reliability check (diagnostic, usable standalone)

Plot residual contours τ̂^num_{M,N}(λ) over a complex-λ grid (minimize empirical ResDMD residual over the retained dictionary subspace; pool train+val+test consecutive pairs). Overlay learned eigenvalues of Â. **Certificate**: eigenvalues in low-residual regions ⇒ spectral reliability; eigenvalues in high-residual regions ⇒ spectral pollution (rollout will compound error at rate ~|λ|^t with wrong λ). In the paper, spectral-residual eigenvalues concentrated in low-residual regions for all 6 systems; latent-prediction eigenvalues scattered into high-residual regions inside AND outside the unit circle.

## Headline Results (6 chaotic systems: Rössler, Lorenz-63, Duffing, Mackey-Glass, Lorenz-96, Kuramoto-Sivashinsky)

Sweep N ∈ {N₀, 2N₀, 4N₀, 8N₀, 16N₀}, 5 seeds, windowed rollout VRMSE over (0.5, 0.7] Lyapunov time, VPT at threshold 0.5:

- Spectral-residual median windowed VRMSE lower than latent-prediction in **30/30** cases (below the prediction model's first quartile in 29/30).
- Median reduction from N₀→16N₀: 10% (Lorenz-96) to 76% (Mackey-Glass) for residual loss vs 2–52% for prediction loss; larger factor in every system.
- Residual median monotone decreasing with dimension in 4/6 systems vs 1/6 for prediction loss.
- Mean VPT longer at all dimensions in all systems (factors 1.06–5.21); VPT nondecreasing in dimension in all 6 systems under two-stage AND joint, with/without operator-norm penalty (w_op‖Â‖²).
- Against 4 baselines (Neural ODE, Consistent KAE, kernel DMD+RFF, ESN): longest or near-longest mean VPT nearly always (exceptions at small N or kernel DMD on Rössler).
- One-step prediction error of latent-prediction model DID decrease with N in all systems — one-step metrics are blind to the rollout gap; spectral placement is the missing variable.

## Reusable Recipes

### Recipe A — drop-in spectral-residual loss for any KAE

```python
# Per Stage-2 update (encoder-only), estimation + held-out minibatches
Zx, Zy = phi(x_batch), phi(y_batch)          # estimation
Zxh, Zyh = phi(x_hold), phi(y_hold)          # held-out (disjoint)
Gxx = Zx @ Zx.T / m + eps * np.eye(N) / m   # regularized
A = (Zx @ Zy.T) @ np.linalg.inv(Gxx)        # == Zy Zx^T (Zx Zx^T + eps I)^-1
# Retained subspace
kappa, U = np.linalg.eigh(Zx @ Zx.T)
U = U[:, kappa >= eps]
Atr = U.T @ A @ U
lams, V = np.linalg.eig(Atr.T)              # eigenpairs on observable coefficients
# Spectral-residual loss over eigenpairs, on HELD-OUT data
loss = 0
for lam, v in zip(lams, V.T):
    a = U @ v
    g_x, g_y = a @ Zxh, a @ Zyh            # candidate eigenfunction values
    loss = loss + (np.sum(np.abs(g_y - lam * g_x)**2)
                    / np.sum(np.abs(g_x)**2))
loss = loss / len(lams)                     # L_res
```

### Recipe B — spectral-reliability diagnostic for any trained latent-dynamics model

1. Pool M consecutive state pairs; compute dictionary snapshots.
2. Truncated SVD → retained subspace U_r.
3. On a complex grid λ ∈ grid: minimize empirical relative residual over nonzero observables in span(U_r) (ResDMD quadratic eigenproblem: solve (G_YY − λG*_XY − λ̄G_XY + |λ|²G_XX) a = τ² G_XX a for smallest τ²).
4. Contour-plot τ̂(λ); overlay eigenvalues of Â.
5. Report: fraction of eigenvalues with τ̂ < ϵ; flag eigenpairs in high-τ̂ regions as rollout hazards.

### Recipe C — dimension-scaling study design

- Sweep N multiplicatively (×2 per step) relative to input dim N₀.
- Report median + IQR of windowed rollout VRMSE (Lyapunov-time windowed) and mean VPT, per seed, 5 seeds minimum.
- Always include a held-out-batch residual evaluation; model-select on validation one-step VRMSE, then CHECK residual contours before trusting large-N models.

## Connections

- **Neural dynamics**: latent-dimension choice in low-rank RNN population models and neural field autoencoders is the same problem — this is the a-posteriori certificate that added dimensions encode real modes rather than pollution. One-step-accurate fits with scattered high-residual eigenvalues (latent-prediction pattern) are exactly the failure mode to screen for.
- **ResDMD lineage** (Colbrook–Townsend): residual/pseudospectrum as ground truth for computed spectra; this paper makes the residual the TRAINING objective and shows the scaling benefit.
- **ResKoopNet / operator-residual dictionary learning** (Xu et al.; Coote–Colbrook): same residual-first dictionary philosophy; this paper adds the latent-dimension scaling study + held-out evaluation + two-stage protocol.
- **World models / MBRL**: VPT-style long-horizon metrics, not one-step likelihood, are the target; spectral-residual transfer should be tested on Dreamer-style latent models.

## Pitfalls

- **Never score residuals on the estimation batch** — in-sample residuals vanish for overfit dictionaries; the paper's gains depend on the disjoint held-out pool.
- Reconstruction loss in Stage 1 is not optional: residual/prediction losses alone admit trivial constant-observable solutions (Lemma A.1 degeneracy).
- The convergence result needs bounded K (μ F-invariant ⇒ isometry); for unbounded operators (e.g.,某些 hyperbolic maps) the guarantee does not apply.
- Latent-prediction rollouts can diverge with the raw least-squares Â at large N — the paper used a rank-constrained rollout operator for the prediction baseline (Appendix B); without it the comparison is unfair to the baseline.
- VRMSE denominator: variance-scaled with ε_vrmse=1e-7 floor; VPT threshold ϵ=0.5, horizon 5 Lyapunov times, per-component std from the reference time series.
- One-step validation error is a poor model-selection signal for large N (both models select fine but differ hugely in rollout); residual contours are the discriminating diagnostic.
