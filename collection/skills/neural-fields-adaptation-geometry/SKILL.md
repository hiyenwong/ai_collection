---
name: neural-fields-adaptation-geometry

description: Tangent-kernel geometry + memory in neural fields.
category: ai_collection
trigger_words: neural fields, INR, adaptation geometry, tangent kernel, NTK, sequential fitting, warm start, memory retention, Mori-Zwanzig, regime classification, forgetting timescales, meta-learning initialization, SIREN, functa
version: 1.0
author: 工程狮5号 (research cron)
license: MIT
metadata:
  tags: [neural-fields, tangent-kernel, implicit-neural-representation, memory, sequential-fitting]
  related_skills: [neural-fields-world-models, hessian-null-space-continuation]
---

# Neural Fields Encode Adaptation Geometry

**Source**: Prateik Sinha (CMU) & Stefania Druga (Sakana AI), "Neural Fields Encode Adaptation Geometry", arXiv:2610.07253 (Oct 2026, cs.LG, under review).

## Core Insight

A fitted neural field (INR) is usually evaluated only by reconstruction quality. This misses two measurable properties: (1) **adaptation geometry** — how cheaply the fitted weights can move to represent a *new* observation, captured by the tangent kernel K_c = J_c J_c^T of the actual finite network; and (2) **fit-path memory** — sequentially continuing each frame's fit from the previous weights leaves usable information about observation history in θ, even when the current reconstruction is held fixed. One object — the tangent spectrum κ_i — controls both: high-κ modes are easy to write but quickly overwritten; low-κ modes are hard to change but persist. **Adaptability and memory are the same spectrum read in opposite directions.**

## When to Use
- Selecting among meta-learned INR/coordinate-network initializations for a new signal (which prior adapts cheapest).
- Encoding video / PDE-trajectory / time-series sequences as neural fields where downstream tasks need regime or history information (functa-style weight datasets).
- Partially observed physical systems where explicit memory terms would be used (Mori–Zwanzig regime) — sequential fitting is a cheap implicit alternative.
- Auditing fitted INR weights as data: report (µ, K) pairs, not just reconstruction error.

## Part 1 — Local Geometry Predicts Nonlinear Adaptation

### Setup
- Reptile-learn a class-specific prior θ_c per image class (MNIST-30/100, Fashion-100, KMNIST-100 × {SIREN, M-layer}).
- Adaptation energy of query x under prior c (idealized objective):
  `E_c(x) = min_δ ½‖x − F(θ_c+δ)‖²/σ² + ½λ‖δ‖²`
- Linearized exact solution is a **Mahalanobis distance**:
  `E_c^lin(x) = ½ r_c^T C_c^{-1} r_c`, `C_c = σ²I + λ^{-1}K_c`, `r_c = x − µ_c`, `µ_c = F(θ_c)`
- The local description of a fitted network is the pair **(µ_c, K_c)** — reconstruction + accessible-change directions — not µ_c alone.

### Results
| Control | Spearman ρ (MNIST-100 M-layer) | Decision agreement |
|---|---|---|
| Matched own kernel | 0.955 | 88.3% |
| Shared mean kernel | 0.886 | 75.7% |
| **Shuffled/reassigned kernel** | **0.770** | — |
- Kernel reassignment (keep µ_c, swap K_c) degrades prediction in **all 8 settings**; SIREN collapses hardest (0.853→0.466). Trace normalization (equalizing kernel total scale) does NOT close the gap — the pairing (µ_c, K_c) itself matters.
- Same-class donor kernels (from independent fits) beat different-class donors — geometry is class-transferable but class-specific.
- Own-kernel advantage stable: +0.069 Spearman (95% CI [0.061, 0.078]), +12.7pp agreement (CI [8.7, 16.7]).

**Takeaway**: when choosing among learned initializations, score candidates by E^lin with each prior's OWN tangent kernel — a cheap linearized Mahalanobis score predicts which nonlinear finite-budget adaptation will succeed.

## Part 2 — Sequential Fitting Leaves Memory in Weights

### The construction
```
Independent: θ_t^ind = Adapt(θ̄, u_t)          # restart each frame from shared prior
Sequential:  θ_t^seq = Adapt(θ_{t-1}^seq, u_t)  # continue from previous frame's weights
```
Optimizer state (Adam moments) reset every frame — information passes ONLY through weights.

### Why history can help at all (Mori–Zwanzig)
Projecting a Markovian system onto incomplete observables yields exact reduced dynamics containing a **memory integral over the past** of the observables. Past observations carry information about unresolved state that the current frame alone lacks.

### Wave endpoint-collision experiment (direct memory test)
- Pairs of wave histories with DIFFERENT pasts but **exactly identical final displacement** and opposite hidden velocities. Any function of the final observation alone = 50% by construction (verified bit-identical independent encodings).
- Linear probe on **sequential endpoint weights θ_T**: **68.6%** velocity-sign accuracy (min 64.8%, 9 seed cells; paired bootstrap 95% CI [16.5, 20.6]pp over independent). Velocity regression R² = 0.22 vs 0.
- Decoded field from θ_T: 55.6%; endpoint reconstruction residual: 56.4% — sequential weights make history MORE ACCESSIBLE than the reconstruction but do not prove output-independence completely.

### Physical-regime classification (3 systems, class-conditioned linear next-step readout)
| System | Raw fields | Indep. weights | **Seq. weights** | Raw+delays | Seq−best |
|---|---|---|---|---|---|
| Allen–Cahn (param-ID, full obs) | 42.1 | 31.9 | **64.4** | 64.4/66.2 | −1.0 (tie) |
| Gray–Scott (reduced obs) | 57.0 | 59.0 | **64.9** | 59.3 | +5.7 |
| Shear flow (reduced obs) | 27.7 | 28.6 | **34.8** | 27.7 (H=1) | +6.2 |
- Sequential advantage is LARGEST on reduced/partial observations (Mori–Zwanzig regime); raw delays close the gap only when the full state is observed (Allen–Cahn) — the advantage boundary case.
- Controls: decoded fields from sequential weights give only 26.8% on shear flow (weights themselves 44.6%); removing movement penalty (β=0) keeps the gain (45.5%); intermediate checkpoints don't help.

## Part 3 — One Spectrum Controls Both (the bridge)

Gradient descent on a frozen linearization: a perturbation along tangent mode i with curvature κ_i retains fraction
```
ρ_i(s) = (1 − ηκ_i)^s      after s steps
```
- Large-κ: cheap to reach, fast to overwrite. Small-κ: expensive to reach, slow to overwrite. **The tangent spectrum IS a set of memory timescales.**
- Measured: predicted vs measured mode-wise retention rank-correlate at 0.986 (Allen–Cahn) / 0.945 (Gray–Scott); after 16 steps slowest quartile retains 0.998/0.999 vs fastest quartile 0.259/0.579.
- Budget trade-off (validated): more fitting steps monotonically improve reconstruction but classification PEAKS at intermediate budget then declines — finite-budget fitting is a mode-dependent temporal filter (Allen–Cahn: 200 steps 69.4% vs 1000 steps 60.1%).
- Closed-loop existence proof: network follows a closed loop of target outputs (min-norm parameter velocity θ̇ = J_θ^+ ẏ), returns to bit-identical reconstruction (rel. err 3e−14) but with CHANGED parameters and tangent kernel — reconstruction does not uniquely determine adaptation geometry. Ordinary SGD/Adam do NOT reproduce this transport signature.

## Method Recipe (when to reuse)

1. **Choosing among learned INR initializations** → score with per-prior tangent-kernel Mahalanobis E^lin, never with reconstruction loss alone; keep each prior's own K_c.
2. **Encoding observation sequences** (video, PDE trajectories, time series as fields) → prefer SEQUENTIAL warm-start fitting over independent per-frame fits; the fitting path becomes a state variable carrying Mori–Zwanzig memory.
3. **Partial/reduced observations** (spatial down-sampling, missing variables) → sequential-weight advantage is largest; if full state is observable, explicit raw frame delays may tie.
4. **Fitting budget** → tune for downstream task, not reconstruction; intermediate budgets can beat large ones because fast modes wash out history.
5. **Readout** → PCA on weights + class-conditioned ridge linear next-step model; score = one-step prediction residual S_c.

## Pitfalls

- The retention law ρ_i(s) = (1−ηκ_i)^s is exact only for frozen-linearization GD; practical Adam fits deviate (differentiating through Adam fits unstable beyond 8 frames).
- Selective erasure of slow modes did NOT identify them as the causal memory carrier — the tangent picture explains retention timescales but not yet WHICH modes carry useful memory.
- Tangent geometry is parameterization-dependent (network+loss+movement metric jointly define it).
- Sequential decoded fields ≠ exactly identical at endpoint; result is "history more accessible", not perfectly output-independent hidden state.
- Endpoint memory non-monotonic in history length (strongest at 16 frames tested) and flat across 25–500 per-frame budgets on the wave task.

## Connection Map
- Mori–Zwanzig memory → motivation for history in weights (Buitrago Ruiz et al. 2025 show explicit memory helps PDE surrogates under partial observation).
- NIRVANA (warm-start video INRs), continual neural fields (Woo 2025) — sequential warm-start known; novelty here is ANALYSIS of what it leaves behind.
- Task2Vec (Fisher/Jacobian task embeddings), NTK literature — related but this uses actual finite-network Jacobians at the fitted point, not infinite-width kernels.
- Functa/INR-as-data pipelines (Dupont 2022) — downstream consumers of fitted weights should audit (µ, K) not just reconstruction.

## References
- arXiv:2610.07253 — Sinha & Druga 2026 (CMU + Sakana AI)
- Jacot et al. 2018 (NTK); Maddox et al. 2021 (trained-network Jacobians); Mallak 2026 (Kernel Reboot)
- Mori 1965 / Zwanzig 1961 (formalism); Chorin et al. 2000 (optimal prediction)
- Buitrago Ruiz et al. ICLR 2025 (memory for time-dependent PDEs)
- Sitzmann et al. 2020 (SIREN); Nichol et al. 2018 (Reptile); Ohana et al. 2024 (The Well benchmark)