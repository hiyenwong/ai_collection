---
name: hessian-null-space-continuation
description: Use when traversing mode-connected solution regions via Hessian null space.
category: ai_collection
---

# Hessian Null Space Continuation (HNC): Traversing Function-Preserving Solution Regions of Neural Networks

**Source**: Ann Huang (Harvard/Kempner), Mitchell Ostrow, Zhouyang Lu, William T. Redman, Leo Kozachkov, Kanaka Rajan — "Traversing the solution space of neural networks with Hessian Null Space Continuation" (arXiv:2609.38081, Sep 2026)

**Trigger words**: mode connectivity, solution space, null space, Hessian, loss landscape, representational degeneracy, function-preserving, model editing, reward hacking, flat directions, implicit bias, CKA steering, alternative solutions, Platonic representation hypothesis

## The One-Line Insight

Around any trained network there exists a high-dimensional set of **approximate null-space directions** of the function-matching loss Hessian — directions along which the input-output mapping barely changes but internal representations can change drastically. Alternating "flat step within the null space" + "restore function by gradient descent" (HNC) traverses this connected low-loss region and finds alternative solutions whose representations differ MORE from the anchor than independently trained models of different architectures — including **reward-hacking policies** in RL — revealing representational diversity that gradient training never explores.

## Core Method

### 1. Function-matching loss (the anchor contract)

```
L(θ) = ½ E_{x~D} [ ‖ f_θ(x) − f_θ₀(x) ‖² ]
```

- θ₀ = the anchor (trained network). L(θ₀)=0, ∇L(θ₀)=0.
- Estimated on a fixed **probe set** X sampled from D.
- Small perturbation δ: L(θ₀+δ) = ½ δᵀ H δ + O(‖δ‖³), H = ∇²_θ L(θ₀).

### 2. Approximate null space

```
V₀ = span{ v_i : λ_i ≤ μ_rel · λ₁ }   (relative threshold, μ_rel ∈ [10⁻⁷, 10⁻³])
```

- Hessian-vector products via Pearlmutter trick (autodiff) — O(kP), never form H (P³/P²).
- Recompute the null space at EVERY linearization point (it drifts along the walk).
- Trained networks: a few sharp directions + a huge near-zero bulk → null space spans a substantial fraction of parameter space.

### 3. The HNC iteration

```
θ̃_t = θ_t + η · d_t              # flat step: d_t ∈ V₀ (random, or steered)
θ_{t+1} = θ̃_t − α ∇L(θ̃_t)       # restore: a few GD steps on function-matching loss
```

Alternation handles both the higher-order terms a zero-eigenvalue step can still incur and the drift of the local null space away from θ₀.

### 4. Steering (optional but the most useful mode)

Optimize any differentiable objective φ while preserving function, via **soft projection** of ∇φ onto the null space:

```
d = (I + H/μ)⁻¹ ∇φ = Σᵢ (v_iᵀ ∇φ / (1 + λᵢ/μ)) v_i
```

- Components along flat directions (λ≪μ) pass; sharp directions (λ≫μ) suppressed.
- μ = μ_rel·λ₁ ties both the flatness threshold and damping to ONE hyperparameter.
- Solved implicitly (matrix form (I+H/μ)⁻¹∇φ — e.g. damped Hessian-vector solves), no explicit eigenbasis.

## The Three Results That Matter

### A. RNNs (3-bit flip-flop): distinct dynamics, same behavior
HNC transforms the canonical Sussillo-Barak fixed-point solution into alternatives with qualitatively different geometry/dynamics; CKA/DSA-steered walks extend far beyond the spread of 10 independently trained seeds in representation space while staying CLOSER in weight space — representational and weight-space distance decouple.

### B. ViT-S/16 ImageNet: representational freedom exceeds cross-model spread
Steering to minimize max-over-layers CKA to the anchor: weights change only 1.3% in norm, ImageNet top-1 drops <1%, yet the endpoint's representations are **less similar to the anchor than any trained vision model** (different sizes/architectures/objectives/data) and even less similar than a randomly-initialized ViT. The endpoint's most-similar image pairs keep semantic (DINOv2) and color similarity but lose spatial-layout similarity. **Implication for the Platonic Representation Hypothesis**: cross-model representational convergence may reflect optimizer bias sampling a narrow solution subset, not a unique task-determined representation.

### C. RL: behaviorally distinct, reward-matched policies
- **Plume tracking**: alternative policy slides to the plume edge and tracks it instead of surging/casting; fewer casts, farther from centerline, same-or-better return, and it BEATS the anchor under OOD conditions (sparse odor, wind switches).
- **AI Safety Gridworld boat race**: steering = maximize KL(π_θ₀‖π_θ) on buffer states while preserving the importance-sampled surrogate return φ_R = (1/N)Σ π_θ(a_i|s_i)/π_θ₀(a_i|s_i) · A_i⁰; 3 of 10 walks land on the known **reward-hacking** exploit (step on/off a single arrow tile, zero net progress). HNC exposes reward-design underspecification lurking NEAR a well-behaved policy.
- Buffer periodically recollected from the current policy (state distribution shifts).

## Geometry Measurements (bonus output)

- **Effective null fraction** (function-drift tolerance: 1% weight-norm step raising L by ≤ ε=0.05): grows with width, shrinks with number of classes; even smallest network on hardest task retains a large null fraction.
- **Normalized curvature dᵀHd/(nC)** along the walk: increases with task complexity, decreases with width — harder tasks stiffen the landscape around the minimum.
- Reconciles Huang et al. 2025 (harder tasks → less inter-seed dynamics variability) with Huh et al. 2024 (larger models → narrower sampled solutions): **larger models admit MORE local alternative solutions even as training converges to less of them**.

## When to Use

1. **Testing whether a property is task-demanded or training-run-specific**: compare the trained solution against HNC-discovered alternatives (dissociates optimizer implicit bias from task constraints).
2. **Finding reward hacking / misalignment proxies**: walk from a well-behaved policy while preserving reward surrogate and maximizing behavioral divergence.
3. **Model merging/editing/fine-tuning research**: map the exploitable function-preserving degrees of freedom (LoRA-style low-norm updates live exactly here).
4. **Representational degeneracy studies**: constructively enumerate diverse solutions instead of only comparing independently trained seeds.
5. **Multi-task / neural-data-aligned steering**: φ can encode a second task's performance or neural-data alignment (the preserved quantity and steering objective are both arbitrary differentiable functions).

## Implementation Sketch

```python
# Pseudocode — one HNC step (PyTorch)
def hnc_step(theta, model, X, phi=None, mu_rel=1e-5, eta=1e-2, restore_steps=5, alpha=1e-3):
    # 1. Hessian-vector products of the function-matching loss via double-backward
    def f_loss():
        return 0.5 * ((model(X) - anchor_out)**2).mean()
    Hv = make_hvp(f_loss, theta)                      # Pearlmutter closure
    # 2. Estimate top eigenvalue + null-space directions (e.g. power/Lanczos on Hv)
    lam1, null_dirs = low_spectrum(Hv, k=64, rel_thresh=mu_rel)   # λ_i <= mu_rel*lam1
    # 3. Flat step: random combination of null dirs, or soft-projected steering gradient
    if phi is None:
        d = rand_combination(null_dirs)
    else:
        g = torch.autograd.grad(phi(), theta, retain_graph=True)
        d = soft_project(Hv, g, mu=mu_rel * lam1)      # solve (I + H/mu) d = g approximately
    theta.data += eta * d
    # 4. Restore function matching
    for _ in range(restore_steps):
        L = f_loss(); gL = torch.autograd.grad(L, theta)[0]
        theta.data -= alpha * gL
```

## Pitfalls / Limitations

- **Function preservation is approximate and probe-set-bound**: small L does NOT guarantee agreement on unseen inputs or under distribution shift — always run held-out functional evaluation.
- Diversity depends on probe coverage and allowed output drift.
- Local search: agnostic to other basins — combine with global methods (e.g. dissimilarity-regularized training) for broader search.
- Preserved quantity is a choice: function-matching loss explores function-preserving alternatives; swapping in the task loss explores the broader task-compatible set.
- Dual prescription: to CHANGE the function fast, move along SHARP directions (largest eigenvalues), not flat ones.

## Related

- Mode connectivity (Garipov, Draxler, Frankle): HNC characterizes what's INSIDE the connected region, not just that it exists.
- `platonic-representations-brain-universal-geometry` — HNC is the constructive counter-argument tool to PRH convergence claims.
- `representational-degeneracy` / solution-degeneracy literature (Huang et al. 2025, D'Amour et al. 2022).
- Code: ann-huang-0.github.io/Hessian-null-space-continuation
