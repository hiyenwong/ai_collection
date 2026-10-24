---
name: dynamic-gain-neuromodulation-stability-gap
description: "Noradrenergic gain dynamics attenuate CL stability gaps"
category: neuroscience
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [continual-learning, stability-plasticity, neuromodulation, noradrenaline, gain-modulation, optimizer-design, fast-slow-weights, loss-landscape, reparameterization, uncertainty]
    related_skills: [importance-shrinkage-continual-learning, neuroevolution-continual-rl-stability-plasticity, mpcs-neuroplasticity-continual-learning, conditional-information-bottleneck-snn]
trigger: stability gap, stability-plasticity dilemma, continual learning, catastrophic forgetting, task transition, joint training, online continual learning, noradrenaline, norepinephrine, locus coeruleus, phasic bursts, gain modulation, gain scaling, neuromodulation, unexpected uncertainty, readout entropy, fast-slow weights, Hinton Plaut, reparameterization, effective weights, curvature amplification, loss landscape flattening, sharpness, optimizer design, NGM-SGD, momentum overshoot, class-incremental, domain-incremental
---

# Dynamic Gain Neuromodulation (NGM-SGD): Attenuating Stability Gaps in Continual Learning

**Source**: "Dynamic gain neuromodulation attenuates stability gaps during continual joint training" — Alejandro Rodriguez-Garcia, Anindya Ghosh, Srikanth Ramaswamy (Neural Circuits Lab, Newcastle University), arXiv:2507.14056v4 (cs.LG/q-bio.NC, updated 19 Oct 2026). Code: github.com/alejandrorg00/ngm-sgd_project.

## When to Use

Use when continual learning shows a **stability gap** — the transient drop in old-task accuracy at every task boundary (distinct from catastrophic forgetting: it persists even under ideal joint training L_joint = L_new + L_old, so it is an *optimization-dynamics* artifact, not a memory/regularization one); when deploying models that must be **queried during training** (online CL) where transient dips are directly harmful; when designing optimizer-level, task-agnostic, lightweight interventions; when translating **noradrenergic gain modulation** (phasic LC bursts under unexpected uncertainty) into learning rules.

## Biological Foundation

Phasic locus coeruleus noradrenaline (LC-NA) bursts signal **unexpected uncertainty** (sudden contextual change; Yu & Dayan) and transiently increase neuronal gain — globally amplifying responsiveness without altering selectivity — which flattens the neural-state energy landscape and enables rapid perceptual switches (Wainstein et al. 2025: pupil-linked gain fluctuations act as a transient "network reset").

## Method: NGM-SGD (Algorithm)

Effective weight: **W_eff,ij = g_i·w_ij** (per-neuron gain scales incoming weights; ReLU nets, biases removed).

Per iteration:
1. Forward pass with gains g (softmax π = softmax(F_W(X; g))), cross-entropy loss.
2. SGD update on **base** weights: W ← W − α∇_W L (note ∂L/∂w = g·∂L/∂W_eff — gain acts as plasticity modulator).
3. Uncertainty: H(y) = mean batch **Shannon entropy of the softmax readout**.
4. Gain update: **g ← γ·g + (1−γ)·g₀ + η·H(y)** (exponential decay toward tonic baseline g₀, phasic bump η·H).

Hyperparameters (paper): γ=0.9; η dataset-scaled {0.5, 0.4, 0.2, 0.1, 0.1} for Rotated-MNIST/Split-MNIST/Split-CIFAR-10/Domain-CIFAR-100/mini-ImageNet; α=0.01; keep g low and bounded (biological analog: spiking saturation bounds cortical gain); MLPs gain-modulate all layers; **ResNet-18: gain-modulate only the classification head** (CNN feature maps share filters — per-neuron scaling disrupts features; also consistent with the finding that much of the stability gap lives in the final linear layer).

## Theory: Why Gain ≠ Learning-Rate Scaling (the paper's key lemma)

Gain is a **forward-pass reparameterization** Φ: W_eff = G·w (isotropic G = gI), not a step-size change:
- **Gradient**: ∇_w L̃ = G^T ∇_Weff L → ΔW_eff = −α·g²·∇_Weff L (effective step α_eff = αg²: transient boost amplifies adaptation)
- **Hessian**: H_w = G^T H_eff G → **λ_eff,i = λ_w,i / g²** ("effective-coordinate flattening": curvature in forward-pass coordinates shrinks by g⁻²)
- Gradient **direction** is unchanged — unlike momentum/Adam whose inertia terms deviate from the true gradient and overshoot at abrupt distribution shifts.
- Emergent fast-slow weights: W_eff = g₀·w + (g−g₀)·w — tonic **slow** component consolidates, phasic **fast** component adapts (Hinton & Plaut's fast-slow scheme without separate weight stores).

## Results (5 seeds, joint training, continual evaluation every iteration)

avg stability gap (max transient old-task accuracy drop):
| Benchmark | NGM-SGD | MSGD | Adam | SGD |
|---|---|---|---|---|
| Split MNIST | **0.017** | 0.267 | 0.283 | 0.034 |
| Split CIFAR-10 | **0.134** | 0.425 | 0.310 | 0.241 |
| Split mini-ImageNet | **0.300** | 0.409 | 0.384 | 0.332 |
| Rotated MNIST | **0.054** | 0.117 | 0.092 | 0.053 |
| Domain CIFAR-100 | **0.224** | 0.232 | 0.256 | 0.243 |

Final avg-ACC stays competitive (99.0 / 90.6 / 48.3 / 94.9 / 68.7). Gap is largest at T1→2 (biggest relative distribution shift) and shrinks for later tasks — averaging across transitions can hide the effect.

## Ablations (mechanism isolation)
- **Tonic gain (η=0)**: small gaps but poor new-task acquisition — apparent stability = reduced plasticity.
- **Instantaneous gain (γ=0)**: no temporal integration → limited rapid acquisition.
- **Entropy-LR (α(t)=α₀·q(t)²)**: matches NGM's effective displacement but gives the **LARGEST stability gap** — applying uncertainty directly to the learning rate reproduces momentum-like instability. **The transition-stabilizing effect comes from the forward-pass reparameterization, not from a bigger step.**
- Full NGM-SGD: low gap AND highest final cumulative accuracy.
- Resetting Adam/MSGD inertia at transitions helps but still underperforms NGM-SGD.

## Diagnostics Worth Reusing
- **Curvature ratio** R_λ(t) = |λ_eff(t)|/|λ_eff(0)| via 25-step power iteration on old-task loss: NGM shows markedly smaller post-transition curvature amplification.
- **Gain asymptote as complexity proxy**: sustained (tonic) gain level rises across class-incremental tasks (positive slope), stays flat for domain-incremental — gain tracks accumulated uncertainty/task complexity.

## Pitfalls & Scope
- Joint-training setting isolates the gap from other forgetting sources; combine NGM-SGD with replay/regularization for realistic CL (works with replay, Appendix E).
- No final-accuracy gain (does not realize Hess et al.'s H3) — the value is **trajectory robustness**, crucial when inference happens mid-training.
- Small task counts are intentional (large measurable shifts); scale η with dataset complexity.
- Momentum optimizers' overshoot can also be reduced by state resets at known boundaries — but NGM-SGD needs no task boundary detection (uncertainty-driven, task-agnostic).

## References
- Rodriguez-Garcia, Ghosh, Ramaswamy (2025/2026). arXiv:2507.14056.
- Hess et al. (2024), Kamath et al. (2024): stability gap persists under joint training; non-increasing-loss paths exist but MSGD deviates.
- Wainstein et al. (2025): pupil-linked gain → perceptual switches (biological model; gains fixed during training there — NGM-SGD closes that gap).
- Hinton & Plaut (1987): fast-slow weights. Dinh et al. (2017): sharpness is parameterization-dependent.
- Yu & Dayan (2005): NA = unexpected uncertainty. Łapacz et al. (2025): stability gap concentrated in classifier head.
