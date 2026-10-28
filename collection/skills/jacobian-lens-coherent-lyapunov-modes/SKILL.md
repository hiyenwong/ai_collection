---
name: jacobian-lens-coherent-lyapunov-modes
description: "Use when auditing averaged-Jacobian LLM interpretability."
category: ai_collection
version: 1.0
author: cs-cron-2026-10-27
license: MIT
metadata:
  hermes:
    tags: [jacobian-lens, j-lens, averaged-jacobian, interpretability, coherent-features, lyapunov-modes, lyapunov-exponent, transformer-dynamics, working-memory-representation, global-workspace, omega-lens, coherence-parameters, hmm-bayes-filter, belief-state-probing, unembedding]
    source: arXiv:2610.31955
    related_skills: [attention-sink-structural, mechanistic-interpretability-neural-quantum-states, correspondence-score-audit-alignment, llm-icl-representational-geometry-reorganization]
---

# Jacobian Lens: Coherent-Lyapunov-Mode Theory (arXiv 2610.31955)

## When to Use

- Diagnosing WHAT an averaged-Jacobian probe (J-lens and cousins) actually
  selects in a transformer — before attributing findings to "workspaces".
- Designing or auditing interpretability tools that average Jacobians over
  prompts/tokens/lags, or predicting their feature orderings.
- Hunting features at a chosen temporal scale via frequency-selective lenses.
- Benchmarking such probes on a closed-form HMM/Bayes-filter testbed.
- Reviewing papers that analyze perturbation growth across depth and token
  position (Lyapunov-style transformer analysis).

## Overview

Theory + validation methodology for interpreting what averaged-Jacobian
("J-lens", Gurnee et al. 2026) interpretability tools select in transformers:
**the lens preferentially identifies coherent features — directions that act
like leading, spatially coherent Lyapunov modes** (perturbations that amplify
across layers, stay roughly constant across token positions, and are
consistent across contexts). Use this skill to (a) predict/diagnose what any
context-and-lag-averaged Jacobian probe will surface, (b) build
frequency-selective ω-J-lenses for different temporal scales, (c) benchmark
such probes on the closed-form ring-HMM Bayes-filter testbed.

## Core equations

J-lens (input layer ℓ, final layer L, lag window H, context c=(x,t)):
- K(c,ℓ,τ) = ∂h_{L,t+τ} / ∂h_{ℓ,t}   (per-context lag-τ Jacobian)
- G_c(ℓ,H) = (1/H) Σ_τ K(c,ℓ,τ);  J_H(ℓ) = E_c G_c(ℓ,H)
- lens(h) = softmax(W_U · norm(J_H h))  (unembedding transfer)

Coherence parameters for any unit input direction v (operational, 2-norms):
- **magnitude**  a(v)   = E_{c,τ} ||K(c,ℓ,τ) v||        (growth across depth; canonical Lyapunov analog)
- **lag coherence** ρ_τ(v) = E_c ||G_c v|| / E_{c,τ} ||K v||  (stationarity across token positions; ρ_τ=1 ⇒ topic-like static, low ⇒ word-type-like fast)
- **context coherence** ρ_c(v) = ||E_{c,τ} K v|| / E_c ||G_c v||  (same read-in/write-out across contexts)

**Telescoping identity (exact, verified to ~1e-15):** σ_i(J_H) = a(v_i)·ρ_τ(v_i)·ρ_c(v_i)
for each right singular vector v_i. Leading lens directions maximize the PRODUCT;
subsequent ones maximize subject to orthogonality. Interpretability consequence:
J-space is a coherence selector, NOT an importance/variance selector — a lens
direction may explain arbitrarily little activation variance (Corollary 1.1:
singular values do not determine variance explained).

Token-indexed J-space directions: j_q = J_H* w_q = Σ_i σ_i ⟨u_i, w_q⟩ v_i —
each is a singular-value-weighted mixture of coherent response channels aligned
with the token unembedding. The sparse non-negative decomposition over {j_q}
translates dynamical geometry into token-level "concepts".

ω-J-lens family: replace the lag average (a zero-frequency Fourier projection)
with projection at frequency ω ∈ [−π, π]: J_ω = E_c[(1/H) Σ_τ e^{-iωτ} K(c,ℓ,τ)].
Sweeping ω re-selects modes by their per-token rotation θ — low ω targets
slowly varying content (topic/working-memory-like), ω near π targets
alternating/fast information (syntax-like). Validated: peaks at ω=θ.

## Analytic testbed (ring HMM Bayes filter)

Latent on n-ring: X_{t+1} = X_t+v+D_t w.p. λ else uniform; evidence revealed w.p.
ε; optional key W=±1 (bias ψ) flips observed state. Fourier modes ϕ_j, belief
update m_t = α_j((1−B_t) m_{t−1} + B_t ϕ_j(X_t)) with α_j = λ c_j e^{iθ_j},
c_j = 1−2q+2q cos(2πj/n), r_j = |α_j|(1−ε). Then (large H):

- a(j) = |α_j| r_j/(1−r_j);  E_c S = r_j e^{iθ_j}/(1−r_j e^{iθ_j})
- σ(j) = |α_j| r_j/|1−r_j e^{iθ_j}| (Eq. 44; the E|S| series cancels from the product)
- ρ_τ(j) = (1−r_j) E|S|/r_j;  ρ_c(j) = |E S|/E|S|; keyed modes: ρ_c = ψ
- θ=0 ⇒ ρ_τ=ρ_c=1 (pure magnitude); θ=π ⇒ ρ_c=1, ρ_τ=(1−r)/(1+r)
- Task knobs modulate factors independently: persistence λ→magnitude only;
  velocity v (θ=2πv/n)→lag coherence only; key bias ψ→context coherence only.
- Crossing point where a static latent overtakes a rotating one (θ₀=0, mode j):
  κ = |α₁|²/|1−r₁e^{iθ₁}|; λ*₀ = [√((1−ε)²κ²+4κ) − (1−ε)κ]/(2c_j)  (Eq. 46)

Paper sweep numbers reproduced by the script (ε=0.2, n=8, q=1/4, j=1):
λ=0.8/0.9/0.95 ⇒ a=0.82/1.23/1.50; θ=0/π/2/π... ⇒ ρ_τ=1.0/0.35/0.24; ρ_c=ψ.

Empirical transfer notes: trained 2-layer transformer (d=128) shows the same
factor ordering at both read-in (v_i) and write-out (u_i) directions; layers
compress the ρ_c range (incoherent latents read higher-than-Bayes ρ_c) — a
transformer bias toward context-independent features; lens also surfaces
non-belief features (reveal bit B_t, key W) unsupervised.

## Pipeline for auditing a real model

1. Collect Jacobians K(c,ℓ,τ) at read-in layer ℓ for ~1k+ contexts (prompts),
   H~128 lags, forward-mode autodiff; validate with split-halves reliability.
2. Average → J_H; SVD. Expect the mean Jacobian to lie OFF the manifold of
   individual Jacobians (spectra do not average) — that is fine and expected.
3. For each candidate feature direction v (e.g. SAE feature, probe direction,
   latent encoding subspace), compute a(v), ρ_τ(v), ρ_c(v) directly from the
   K ensemble — do NOT infer "importance" from σ or variance explained.
4. Attribute a lens finding to its dominant factor: growth (a) vs spatial
   stationarity (ρ_τ) vs cross-context consistency (ρ_c). Design controls that
   modulate exactly one factor (as the HMM knobs do).
5. To hunt features at a chosen temporal scale, sweep ω-J-lenses and read the
   peak ω per direction; compare against the direction's measured rotation θ.
6. Order predictions are the strong claim: theory ranks which latents the lens
   surfaces first, incl. exact crossings (Eq. 46) — test orderings, not just
   presence/absence.

## Validation

`scripts/validate_jlens.py` (numpy only; `--quick` for fast pass) verifies:
- T1 telescoping identity exact on random Jacobian ensembles; no probe
  direction exceeds σ₁.
- T2 Bayes-filter closed forms via MC over reveal schedules (Geometric(ε)),
  incl. paper sweep numbers and the θ=π edge case.
- T3 Eq. 46 crossing vs grid crossing of σ₀(λ₀)−σ₁.
- T4 ω-lens peaks at ω=θ per rotating latent; DC lens favors static.
- T5 perturb-and-propagate on the simulated filter recovers a(j) and E|S|.
All 5/5 must pass; regression-test after any edit.

## Pitfalls / honest limits

- **Mean-Jacobian fallacy**: an average Jacobian has no reason to behave like
  any element; singular vectors/values are nonlinear in the matrix and can
  deviate grossly under averaging. Interpret J_H only through the coherence
  decomposition, never as "the" Jacobian.
- **Variance-explained fallacy**: lens selection strength (σ) is unrelated to
  variance explained (2-D counterexample, Cor. 1.1). Small J-space variance ≠
  irrelevant; large variance ≠ lens-detectable.
- **1/H normalization**: Eq. 35's a(j) is the LAG-SUMMED magnitude (drops 1/H,
  which rescales all σ equally, preserving order). If you estimate a(v) as a
  mean over (c,τ) pairs you get a(j)/H — multiply by H before comparing.
- **Perturbation tests**: reveals WIPE the belief perturbation (m=αφ replaces
  old state); count zero responses in expectations; use common random numbers
  for perturbed/unperturbed trajectories; perturb the evidence additively.
- **Stein's-lemma analyses assume Gaussian inputs** — transformer hidden states
  are heavy-tailed/non-Gaussian; the Lyapunov framing does not need that assumption.
- **MC tolerance**: E|S| series has no closed form for general θ; allow ~1-2%
  MC error when validating against closed forms; the product ρ_τρ_c = (1−r)/|1−re^{iθ}|
  IS closed and cancels the series.
- Theory selects only the LEADING modes; transformer evidence transfers with
  small bias (O(0.01) in crossings) and per-layer direction differences; the
  Global-Workspace reading is agnostic — coherence explains the findings
  without committing to the cognitive interpretation.

## Activation

jacobian lens, J-lens, averaged Jacobian, interpretability probe design,
coherent features, Lyapunov modes, lyapunov exponent transformer, working
memory representation LLM, global workspace, lens unembedding, tuned lens,
binary opposition fast/slow feature, omega lens frequency-selective
interpretability, coherence parameters, HMM Bayes filter testbed, belief-state
probing, feature growth across layers, token-position stationarity,
context-invariant features
