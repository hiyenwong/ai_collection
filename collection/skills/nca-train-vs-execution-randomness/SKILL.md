---
name: nca-train-vs-execution-randomness
description: "Controlled split of training vs runtime randomness in neural CA."
category: ai_collection
---

# Where Does Randomness Matter in Neural Cellular Automata?

**Source**: Zuo, Shi, Liu (Fudan), arXiv:2609.36797 (29 Sep 2026), cs.LG.

**Trigger**: neural cellular automata (NCA) update schedules, asynchronous vs synchronous training, growing NCA stability, persist/grow/regenerate recipes, random update masks, second-moment stability criteria, long-horizon retention vs damage recovery.

## Core Finding

Stochastic cell updates are routinely used BOTH during training AND at rollout — this paper **disentangles the two roles** in controlled Growing NCA experiments (canonical Mordvintsev architecture: 72×72 grid, 4 RGBA + 12 hidden channels, Sobel perception, shared 1×1 conv rule `y_t = x_t + M_t ⊙ f_θ(K * x_t)`, living-mask g, update mask (M_t)_u ~ Bern(α)):

1. **Randomness matters for LEARNING, not for RUNNING**: with the fixed-rate persist recipe + Adam lr=2e-3, asynchronous training (α_train=0.5) passes the T=96 quality test in **10/10 runs vs 3/10 synchronous** (Fisher p=0.003). But ALL 10 asynchronous models then **retain the target for 4,096 fully deterministic steps** (α_eval=1) without retraining. The randomness is an optimization aid, NOT a runtime requirement.
2. **Optimizer-dependent, not fundamental**: 4 exploratory retrainings of failed synchronous configs at lr=1e-3 and 5e-4 all pass — the sync failure is specific to the tested constant learning rate.
3. **Low training loss ≠ usable rule**: all 9 recorded synchronous traces crossed minibatch loss 1e-3, yet 7/10 final checkpoints fail (6 collapse to empty absorbing states, 1 deformed).

## Exact Second-Moment Criterion (the analytical contribution)

For the linear residual rule x_{t+1} = x_t + M_t A x_t with translation-invariant A (Fourier symbol â(ω)) on N^d periodic lattice, independent Bernoulli(α) cell masks:

- **Mean dynamics** (Prop. 1): E[x_{t+1}] = (I + αA)E[x_t]; synchronous eigenvalues µ map into disk D_α = {µ: |µ − (1−1/α)| < 1/α}. Partial updates damp non-neutral oscillatory mean modes: |(1−α)+αe^{iθ}|² = 1 − 2α(1−α)(1−cos θ).
- **Second moments** (Thm. 1): expected modal power P_t(ω) follows EXACT recursion
  `P_{t+1}(ω) = d_α(ω)·P_t(ω) + [α(1−α)/N^d]·Σ_{ω'} |â(ω')|²·P_t(ω')`, with d_α(ω)=|1+αâ(ω)|².
  Diagonal modal propagation + **rank-one variance injection coupling all modes**. All non-neutral modes decay in mean square ⟺ d_α(ω)<1 on those modes AND `S = Σ_{ω:â≠0} α(1−α)|â(ω)|² / (N^d[1−d_α(ω)]) < 1`.
- **Replacing the mask by its mean overstates stability**: the mean-only test misclassifies 4 of 25 non-marginal settings on a 32×32 diffusion lattice (x ← x + M(c·Lap x)); the exact criterion matches all 25. Random masking damps mean modes but *injects variance* — two-sided effect.

## Training-State Exposure Determines Later-Use Behavior

Matched-quality comparison (30 models, all pass the same T=96 reconstruction test, medians 35–1078× below threshold):

| Recipe | Long-horizon retention @T=4096 | Damage recovery |
|---|---|---|
| Grow (seed-only rollouts) | **8/10 off-target** | worsens error (−46% both targets) |
| Persist (pool of 1024 generated states, worst→seed) | **10/10 retained** | ≈neutral (−7%, +4%) |
| Regenerate (persist + circular damage on half the batch) | **10/10 retained** | **+85% / +99% error reduction** |

- Persist models: negative mean perturbation growth λ_pert; grow: positive (bootstrap intervals exclude 0). But positive λ_pert ≠ failure — 5 models with positive λ_pert still retain.
- **Frozen-state Jacobian spectrum does NOT predict fate**: all 30 models have max |eigenvalue|>1 at the frozen state, yet persist/regenerate retain. Local expansion ≠ numerical blowup ≠ retention ≠ repair — four different properties.
- Removing living masks leaves all rollouts bounded — masks are not what prevents divergence here.

## Design Sequence (the practical takeaway)

1. Pick the update schedule that makes optimization reliable under your budget (async helps at fixed lr).
2. Test whether the learned rule actually needs stochastic updates at execution — here it did not; deploy deterministically.
3. Train on the states the deployed rule must handle: generated states → retention; explicit damage exposure → repair. Reconstruction loss, local spectrum, and finite-time perturbation growth each answer only part of the question.

**Scope caveats (authors are explicit)**: 2 synthetic targets, one NCA family, 5 seeds/config, one primary lr, finite horizons; the linear theorem does not explain the nonlinear training failures.

## Evaluation Protocol (reusable)

- Quality pass: RGBA MSE < 0.02 at T=96 in training mode.
- Long-rollout labels: dead (empty state, absorbing) / divergent (non-finite or |max|>10³) / off-target (surviving finite, MSE>0.15) / retained.
- λ_pert: perturb living cells by δ₀=10⁻³·N(0,I), evolve perturbed+clean 64 steps with SAME masks, λ = (1/64)log(‖δ₆₄‖²/‖δ₀‖²) — finite-amplitude trajectory measurement, not a Lyapunov exponent.
- Damage recovery: fixed 80-step window after circular damage; report % error change.
