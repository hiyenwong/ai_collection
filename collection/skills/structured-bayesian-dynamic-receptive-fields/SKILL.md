---
name: structured-bayesian-dynamic-receptive-fields
description: GMRF-space + AR(1)-time Bayesian receptive fields via INLA. Use for spike-count RF estimation.
category: ai_collection
trigger_words: receptive field estimation, Gaussian Markov random field, SPDE, INLA, Poisson spike model, dynamic receptive field, functional data clustering, salamander retina, ganglion cells, LASSO fragmentation, B-spline FPCA, temporal-response phenotypes, high-dimensional Bayesian
---

# Structured Bayesian Modeling of Dynamic Receptive Fields

Methodology from "Structured Bayesian Modeling of Dynamic Receptive Fields in Salamander Retinal Ganglion Cells" (arXiv:2609.30731, cs.NE/q-bio, Sep 2026, Alokesh Manna, Texas A&M Stats).

## When to Use
- Estimating spatio-temporal receptive fields from few-trial spike counts where pixels-per-time-bin predictors vastly outnumber trials (e.g., 13×13×30 = 5,070 coefficients from 3,939 trials)
- Replacing pixel-independent L1 penalties (LASSO/elastic-net) that fragment receptive fields into spatially disconnected pixel selections
- Population-level typing of neurons from fitted surfaces when biological labels are unavailable
- Any high-dimensional latent-Gaussian problem where MCMC mixing is too slow and INLA's hyperparameter integration suffices

## Observation Model (Poisson GLM on spike counts)
```
Y_nkt | λ_nkt ~ Poisson(λ_nkt)
log λ_nkt = α_k + b_r(n) + X_n^T β_kt
```
- `α_k`: neuron-specific intercept absorbing baseline excitability (electrode quality, metabolic state) — WITHOUT it, baseline differences contaminate β
- `b_r(n) ~ N(0, 1/τ_b)`: i.i.d. random effect for repeated presentations (13 repeats shared across 303 images)
- `X_ns`: pixel intensity; `β_kst`: effect of pixel s on neuron k firing at time t — sign gives excitation (+) / inhibition (−)
- Poisson restriction (variance = mean) NOT formally tested — negative-binomial extension flagged as follow-up; log link lets unconstrained Gaussian priors live on β without positivity constraints

## Core Innovation: Structured Latent Field (replaces free 5,070-dim β)
**Spatial**: continuous-domain Gaussian field via SPDE (Lindgren 2011) discretized on a triangulated mesh shared across neurons
```
w_k(u) = Σ_m ψ_m(u) w_km,   β_kt^sp = A w_kt
```
- `A ∈ R^(P×M)`: projector evaluating mesh field at P=169 pixel centers
- Precision `Q_w(κ, σ_w)` from finite-element discretization of a differential operator — **sparse by construction** (zero for non-neighbor node pairs)
- GMRF conditional-mean identity: each mesh node pulled only toward precision-weighted average of immediate neighbors — the mechanism that kills isolated-pixel selections

**Temporal**: AR(1) across T=30 time groups
```
w_kt = ρ_k w_k,t-1 + ε_kt,   ε ~ N(0, Q_w^-1),  |ρ_k| < 1
w_k1 ~ N(0, Q_w^-1/(1-ρ_k²))  (stationary marginal)
```
- Penalized-complexity prior on ρ_k

**Why INLA not MCMC**: at ~786K parameters (155 neurons × 5,070), coordinate-wise MCMC mixing is hopeless. The latent field θ = (α, b, w_1..w_T) is jointly Gaussian conditional on only 4 hyperparameters ψ = (κ, σ_w, ρ, τ_b) — INLA does numerical integration over ψ instead of sampling θ. d = 1 + 13 + M·T latent dims.

## Why LASSO Fails Here (the paper's motivating diagnosis)
1. **Coherent-vs-fragmented indistinguishable under L1**: two configs with 4 nonzero coefficients — one spatially contiguous, one scattered — pay identical penalty
2. **Correlated-pixel selection instability** (Zou & Hastie 2005): picks one pixel from a correlated group arbitrarily
3. **Shrinkage bias**: L1 shrinks nonzero β toward zero, distorting scientifically meaningful effect magnitudes
4. **Empirical**: Poisson-LASSO (λ=0.02) on real data selects 27/169 pixels including isolated border pixels with no biological interpretation

## Population Typing Pipeline (two-stage, per 155 neurons)
1. **Independent per-neuron INLA fits** → 155 surfaces β̂_k1..β̂_kT
2. **Space-averaged temporal profile**: β̄_k(t) = (1/169) Σ_s β_kst — one 30-point curve per neuron
3. **B-spline expansion**: least-squares projection onto cubic B-spline, 8 basis functions → 155×8 matrix
4. **Functional PCA**: retain PCs (≥2) reaching 99% cumulative variance
5. **Gaussian mixture (mclust)** on PCA scores; BIC over k ∈ {2..10} × covariance families
6. **Result**: k=3 temporal-response phenotypes (85/32/38 neurons) — vs degenerate grouping when clustering raw 5,070-dim surfaces directly

**Phenotype characterization** (deliberately conservative):
- All three share broad shape: positive early → negative middle → partial late recovery; differ in decline timing/depth
- Magnitude-weighted centroids fall near grid center for all (NOT spatially separated); single peak pixels at periphery differ (read as suggestive only)
- Explicitly NOT claimed as validated biological cell types (no test vs ON/OFF or fast/slow RGC classes — future work)

## Simulation Results (the honest evidence)
Design: 2×2×2 factorial — spatial config {compact, disconnected} × true types G ∈ {1,3} × deviation τ_δ ∈ {0.4, 1.6}; K=12 synthetic neurons, T=6 bins. Five methods compared.

Key numbers (spatio-temporal SPDE/AR(1) vs LASSO, representative cells):
- **Log-score (held-out spikes)**: SPDE/AR(1) −1.80 to −2.04 vs LASSO −2.41 to −2.93 (SPDE clearly better)
- **TPR**: SPDE/AR(1) 0.82–0.93 vs LASSO 0.56–0.73
- **FPR**: LASSO best (0.04–0.25) vs SPDE/AR(1) (0.04–0.49) — **LASSO controls false positives better, honestly reported**
- **Coefficient error ||β̂−β||₂**: SPDE/AR(1) 0.39–0.65 vs LASSO 0.95–1.79

Full design (5 spatial configs × G∈{1,2,3} × τ_δ continuum × GMRF deviations) stated but NOT executed — SPDE fits too slow per neuron; the paper says so explicitly rather than hiding it.

## Bonus: Free Posterior Quantities
INLA marginals give P(β_kst > 0 | Y) at every pixel-time cell at no extra cost — direct posterior evidence for excitation/inhibition, available from per-neuron fits alone.

## Implementation Notes
- R-INLA stack: `inla()` with SPDE mesh (`inla.mesh.2d`), `group` + `control.group = list(model='ar1')` for the AR(1); A-matrix via `inla.spde.make.A`
- Clustering: `mclust` GMM + BIC; B-spline via `splines::bs(x, df=8)`
- Scaling caution: SPDE/AR(1) fit time grows with T; paper reduced T=30→6 for simulations
- The fully hierarchical extension (shared type-level μ_g,t + structured-sparsity prior across neurons, Section 9 Part B) is specified but NOT fit — G=3 from the two-stage typing is the data-driven input for that future joint fit

## Pitfalls
- Do NOT interpret the 85/32/38 clusters as biological RGC classes without validation against physiological labels
- Do NOT use held-out log-score alone as evidence of correct pixel identification — a method can log-score well while misattributing pixels; only simulation with known ground truth can test support recovery
- Held-out splits must be audited for symmetry disguises (rotations/reflections/recolourings can make "held-out" pairs duplicate trained transformations)
- Poisson dispersion unchecked in the real-data fits — run Pearson χ² or negative-binomial refit before trusting interval estimates

## Cross-Links
- [[gp-cake-brain-connectivity]] — alternative Bayesian kernel approach for effective connectivity
- [[neural-population-decoding]] — population-level analysis complementary frame
- Pillow et al. 2008 / Park & Pillow 2011 (localized priors) — direct lineage of this approach
