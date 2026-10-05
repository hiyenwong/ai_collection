---
name: distribution-aware-channel-capacity-ec
description: Non-Gaussian channel-capacity EC via dual-flow estimation. Use for directed brain connectivity beyond Gaussian residuals.
category: neuroscience
tags: [neuroscience, effective-connectivity, channel-capacity, normalizing-flows, information-theory, brain-network, non-gaussian, causality]
version: 1.0
arxiv: 2609.32774
date: 2026-09-26
trigger: effective connectivity, directed brain interactions, non-Gaussian residuals, channel capacity, normalizing flows, transfer entropy, Granger causality, brain signal distributions, information-theoretic connectivity, dual-flow estimator
---

# Distribution-Aware Channel Capacity for Effective Connectivity

## Overview

Information-theoretic framework replacing Gaussian residual assumptions in effective-connectivity (EC) estimation with **distribution-aware channel capacity** estimated by a **dual-flow min–max game** between a generator normalizing flow (searches admissible input distributions under power constraint) and an observer normalizing flow (estimates output entropy). Validated across 10 brain-like simulation conditions, outperforming Granger causality, VAR-LiNGAM, Gaussian capacity, and GIMME.

**arXiv**: [2609.32774](https://arxiv.org/abs/2609.32774) (cs.LG, 26 Sep 2026)
**Authors**: Jianan Jian, Jacob Kang, Nurahamed Multezem, Benjamin Li, Nan Xu (University of Maryland)
**Code**: https://github.com/inspirelab-site/EC-dual-flow

## Core Problem

- EC estimation (Granger, transfer entropy, DCM) almost universally assumes **Gaussian residuals** — enabling closed-form estimation but discarding informative distributional structure.
- Empirical diagnosis across modalities (BOLD fMRI, EEG, LFP, calcium imaging), species (human, rat, macaque), and conditions shows brain signals and fitted channel residuals **frequently deviate from Gaussianity** (heavy tails, skew, burst-like, state-dependent structure).
- Gaussian-capacity estimators characterize residual uncertainty by covariance alone → **cannot distinguish residuals with matched variance but different entropy power**, which support different achievable information rates.

## Methodology

### Step 1: Empirical FIR Channel with Residual Resampling

For source ROI x and target ROI y within a temporal window:

```
y_t = Σ_{ℓ=0}^{k-1} b_ℓ x_{t-ℓ} + w_t
```

- Estimate filter **b** by least squares; residuals ŵ_t form an **empirical residual pool**
- Do NOT impose parametric form on W — treat residual pool as samples from unknown continuous P_W with finite differential entropy
- FIR order k: BIC for long windows, corrected AIC (AICc) for short windows
- Vector form: `Y = BX + W` where B is the convolution operator

### Step 2: Capacity Formulation

```
C = sup_{P_X ∈ P_P} I(X;Y) = sup_{P_X} h(BX + W) − h(W)
P_P = {P_X : E‖X‖² ≤ dP}   (average power budget P per sample, dimension d)
```

Key identity: capacity estimation = **maximize output entropy − residual entropy**.

### Step 3: Dual-Flow Min–Max Estimator

**Generator** g_θ: maps Gaussian latent Z₁ ~ N(0,I) → candidate inputs, with power constraint via RMS normalization:
```
X_θ = Norm_P(g_θ(Z₁)),  Y_θ = B·X_θ + W,  W resampled uniformly from residual pool
```

**Observer** q_φ: invertible flow inducing density p_φ(y) = p_U(q_φ(y))·|det J_{q_φ}(y)|, negative log-likelihood:
```
L_φ(y) = −log p_φ(y) = −log det J + ½‖q_φ(y)‖² + (d/2)log(2π)
```

**Min–max objective**:
```
Ĉ = max_θ min_{φ_Y} L_Y(θ, φ_Y) − min_{φ_W} L_W(φ_W)
```
where L_Y = E[−log p_φY(B·Norm_P(g_θ(Z₁)) + W)] (signal+noise entropy) and L_W = E[−log p_φW(W)] (noise-only entropy). Train both objectives **in parallel with matched residual samples** → paired entropy difference reduces Monte Carlo variance.

### Lemma 1 (Observer-Flow Entropy Identity)

```
E_{Y~P_Y}[−log p_φ(Y)] = h(Y) + KL(P_Y ‖ P_φ)
```
Minimized observer NLL recovers differential entropy up to KL approximation term. Equality when P_φ = P_Y.

### Gaussian Recovery (Sanity Check)

When W ~ N(0, Σ_W), formulation reduces to classical Gaussian channel capacity:
```
C_G = ½ log det(I + Σ_W^{-1/2} B Σ_X B^⊤ Σ_W^{-1/2}),  max over Σ_X ⪰ 0, tr(Σ_X) ≤ dP
```

### Residual Entropy Beyond Variance

Entropy power inequality for scalar channel Y = X + W:
```
C(W) ≥ ½ log(1 + P/N(W)) ≥ ½ log(1 + P/σ_W²),  N(W) = (2πe)^{-1} exp(2h(W))
```
Equality in second bound only when W Gaussian. **Matched variance ≠ matched capacity** when residual shape differs.

### Error Decomposition (Practical Guide)

```
|Ĉ − C| ≲ ε_resid + ε_gen + ε_obs + ε_opt + ε_MC
```
(residual/channel estimation, generator restriction, observer density approximation, nonconvex optimization, Monte Carlo sampling)

## Implementation Details

- **Flow architecture**: 1D Real NVP, 3 coupling-layer pairs, alternating masks [0 1 0 1...] / [1 0 1 0...]
- Each coupling layer: conv(size 3, depth 32) → ReLU → conv(size 3, depth 32) → ReLU → conv(size 3, depth 1) for scaling s and translation t
- Soft clipping at flow output
- **Training**: alternate observer updates (min NLL) with generator updates (max signal+noise entropy estimate); Adam; declare convergence when EMA of paired entropy difference reaches stationarity
- Training-sequence length L: limited sensitivity across tested range (e.g., L=1024 stable, mean shifts ≤ 4.3% across initializations)
- Sliding windows (continuous data → dynamic directed connectivity) or condition segments (block task designs)

## Experimental Results

**Simulations (50 realizations × 10 conditions, ground-truth EC)**:
- Dual-flow achieved highest AUROC and AUPRC in **every** condition (AUROC .858–.949; AUPRC .521–.891)
- vs baselines: Gaussian capacity (GCap), Granger causality, VAR-LiNGAM, GIMME
- Robust to: diverse topologies, hidden/common drivers, feedback, heterogeneous hemodynamics
- Sparse 28-ROI recurrent Macq28 network: 52 true edges among 756 candidates (random AUPRC .069) → Dual-flow AUPRC .521 (7.5× chance)
- Compound challenge (Comp12): AUROC/AUPRC .879/.724

**Real data**: HCP tongue-motion fMRI — detects task-related directed interactions consistent with somatotopic orofacial motor circuitry (pFDR < 0.1, CV < 30th percentile); resting-state rat LFP–BOLD cross-modal correspondence.

## Use When

- Estimating directed interactions between brain ROIs from BOLD/EEG/LFP/calcium signals
- Residuals are non-Gaussian (burst-like, heavy-tailed, state-dependent) — first diagnose with normality tests on fitted residuals
- Time-resolved (sliding window) or condition-resolved dynamic effective connectivity
- Hypothesis-driven analysis of prespecified circuits / moderate-sized subnetworks
- Comparing or benchmarking EC methods beyond second-order statistics

## Limitations

- Linear FIR + additive noise within segment: inadequate for strongly nonlinear dynamics or temporally correlated residuals
- Not yet scaled to unrestricted whole-brain exploratory analysis (per-pair game cost)
- No strong duality claim for non-convex neural parameterization — use game-gap diagnostic
- Local stationarity assumption within each window

## Related Skills

- `gp-cake-brain-connectivity` — causal kernel modeling of effective connectivity (GP regression route)
- `topological-effective-connectivity-hodge` — Hodge decomposition + lead-lag MI for directed flow (topology route)
- `time-varying-brain-connectivity` — SWpC time-varying directed connectivity
- `hermes-brain-connectivity` — HERMES connectivity toolbox

## References

- Jian et al. (2026). "Beyond Gaussian Assumptions: Distribution-Aware Channel Capacity for Effective Connectivity." arXiv:2609.32774
- Cover & Thomas (2006). Elements of Information Theory (channel capacity, entropy power)
- Dinh et al. (2016). Real NVP density estimation
- Belghazi et al. (2018). MINE (contrast: fixed joint vs capacity-achieving input)
