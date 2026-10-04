---
name: fast-brain-flow-aligned-fmri-surrogate
description: Flow-aligned direct clean-signal fMRI surrogate modeling.
category: ai_collection
---

# FAST-Brain: Flow-Aligned Spatio-Temporal Surrogate Brain Model

**arXiv:2609.34354** — "FAST-Brain: A Flow-Aligned Spatio-Temporal Surrogate Brain Model" (Liu, Shi, Zhang, Zhu; submitted 28 Sep 2026, q-bio.NC)

Use when: generating surrogate rs-fMRI/BOLD time series (digital-twin brains), recovering functional/effective connectivity from generative rollouts, or applying flow matching to any *low-dimensional-in-ambient-space* spatio-temporal signal (traffic, climate, power grids). Trigger words: flow matching, clean-signal prediction, fMRI surrogate, BOLD generation, spatio-temporal GCN, low-dimensional subspace, digital twin brain.

## 1. Core Idea: Predict the Clean Signal, Not Noise or Velocity

Standard flow matching parameterizes a velocity field V_θ(Z_τ, τ) in the FULL ambient N×P space (N ROIs × P future steps). rs-fMRI signals concentrate near a low-dimensional subspace, so off-subspace velocity components carry no information about brain dynamics — wasting capacity and hurting sample efficiency.

**FAST-Brain's reparameterization:** keep the linear interpolation path Z_τ = τ·Y_t + (1−τ)·ε, but make the network predict the **clean signal** Ŷ_t = F_θ(Z_τ, τ, H_t, G). Recover the velocity analytically:

```
V̂_θ = (Ŷ_t − Z_τ) / max(1 − τ, τ0),   τ0 = 0.05
```

The training loss then reduces to a **weighted clean-prediction loss**:

```
L_FAST = E[ (1−τ)^(−2) · ||F_θ(Z_τ, τ, H_t, G) − Y_t||² ]
```

so the Bayes-optimal predictor is the conditional mean E[Y_t | Z_τ, H_t, G] — and the training time τ follows a logit-normal schedule.

## 2. Theory (Theorem 1): Why Clean-Signal Prediction Wins

**Assumption 1 (low-dim subspace):** Y_t = A·S_t a.s. with orthonormal A ∈ R^{N×d}, d ≪ N.

**Factorization:** the Bayes-optimal denoiser satisfies F*(Z, τ, h, g) = A·f(A⊤Z, τ, h, g) — it depends on the noisy observation ONLY through its d-dimensional projection A⊤Z. A ReLU network approximating it has error bound scaling as **√(dP) + ε, independent of ambient N**.

**Contrast:** velocity target v* = (F* − Z_τ)/(1−τ) contains the term −Z_τ/(1−τ) which lives in the FULL ambient space — noise/velocity parameterizations cannot factorize and retain N-dependence. This is the theoretical justification for direct data prediction (echoes EDM / JiT / SiD2 findings from image generation, first brought to structured time series here).

## 3. Architecture: Additive Dual Decoder

```
F_θ(Z_τ, τ, H_t, G) = D_temp(Z_τ, τ, H_t) + D_spat(Z_τ, G)
```

**Temporal decoder D_temp** (history-conditioned Transformer):
- Noisy future tokens Z_τ (+ τ time embedding) = queries; history window H_t = keys/values
- Cross-attention with **RoPE** (relative temporal position) → residual + LayerNorm → 2 self-attention layers over the P future points

**Spatial decoder D_spat** (multi-graph GCN residual):
- Three anatomical priors as adjacency matrices:
  - G^(1)_ij = SC_ij (structural connectivity strength)
  - G^(2)_ij = 1 − L_ij (shorter fiber ⇒ larger weight; L normalized to [0,1])
  - G^(3)_ij = 1(c_i = c_j) (shared functional-network membership)
- Symmetrically normalized Laplacians L^(m) = I − (D^(m))^(−1/2) G^(m) (D^(m))^(−1/2)
- **Learnable polynomial graph filter:** L̃^(m) = Σ_k α_{m,k} (L^(m))^k (higher-order structural interactions)
- L_g = 2 GCN layers, feature transform shared across nodes

**Curriculum via zero-init:** the final projection of D_spat is zero-initialized, so the spatial branch contributes nothing at first — the model learns the global temporal trend, then progressively folds in structural corrections. The additive form guarantees D_temp is never destabilized early.

**Sampling:** K=20 Euler steps of Z_{i+1} = Z_i + Δτ·V̂_i; autoregressive rollout with P=24-step future windows (multi-step generation reduces exposure bias vs one-step autoregression).

## 4. Results

| Dataset (ROIs) | Metric | Best baseline | FAST-Brain |
|---|---|---|---|
| RNN synthetic (20) | FC corr / MAE | 0.846 / 0.059 | **0.938 / 0.028** |
| SDDEs (66) | FC corr / MAE | 0.890 / 0.170 | **0.975 / 0.115** |
| HCP real (360) | FC corr / MAE | 0.726 / 0.199 (DSFM) | **0.938 / 0.073** |

- **Effective connectivity (RNN, ground truth):** correlation 0.956, AUROC 0.999, AUPRC 0.995 vs FlowTS 0.851/0.916/0.810
- Conditional generation: best CRPS (0.154), QICE (0.005), ProbCorr, Conditional-FID on all metrics
- **Ablations confirm both parts matter:** w/o GCN, ε-prediction, and v-prediction all degrade — worst on high-dimensional SDDEs/HCP (HCP FC corr: 0.867 / 0.799 / 0.856 vs 0.938 full), matching the d-vs-N theory
- Latent geometry: ε-prediction yields a shrunken misaligned PCA ring; v-prediction over-smooths the marginal; clean-signal prediction matches the ground-truth circular manifold and bimodal KDE

## 5. Evaluation Protocol (reusable)

- FC via Pearson correlation over generated vs reference FC matrices; EC via perturbation response EC_{i→j} = E_t[(Ŷ_{t+T,j}^{(i,+δ)} − Ŷ_{t+T,j})/δ]
- Conditional quality: CRPS, QICE (calibration), ProbCorr, Conditional-FID (TS2Vec feature space)
- Baselines: NPI, DSFM (fMRI-domain); TimeDiff, SSSD, DiffusionTS, FlowTS (general TS)
- 10 repetitions, mean ± SE; 80/20 train/test split on the sequence

## 6. Implementation Checklist

1. In flow matching over structured low-rank signals, parameterize the **clean signal** and recover velocity analytically with the max(1−τ, τ0) clip
2. Use the weighted-loss equivalence (1−τ)^(−2)·||F−Y||² for analysis; logit-normal τ schedule
3. Add spatial/anatomical priors as a residual branch with zero-initialized final layer (curriculum)
4. Encode multiple complementary graphs (strength, distance, membership) through one learnable polynomial filter
5. Generate multi-step windows (P≈24) autoregressively to limit exposure bias
6. Evaluate on FC/EC recovery and latent-geometry preservation (PCA/t-SNE + KDE), not just rollout MSE

**Limits:** finite-sample statistical learning bounds remain open (theory is approximation-side only); evaluated on rs-fMRI + synthetic dynamics; the paper itself flags traffic/climate/power-grid as candidate transfer domains.
