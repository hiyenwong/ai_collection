---
name: fidlif-parallel-exact-bptt-lif
description: Use for long-sequence SNN training. Newton scan exact BPTT.
category: ai_collection
---

# FidLIF: Parallel Training of High-Fidelity Hard-Reset LIF Neurons with Exact BPTT

**Source**: Kaixiang He & Yujie Wu (Hong Kong PolyU), arXiv:2610.16924 (12 Oct 2026), cs.NE. Triton implementation.

## Problem

Hard-reset LIF dynamics couple time steps through resets: a spike at step i produces v′_i = v_rest, altering all subsequent evolution. Spikes cannot be known in advance, so standard forward propagation is inherently sequential, and BPTT cost grows with T. Existing parallelization strategies trade away something:

- **Reset removal** (PSN, MF-PSN, sliding PSN): decouples time but sacrifices hard-reset fidelity and temporal expressivity; temporal-matrix variants break the recurrent structure so the model can no longer run step-by-step at deployment.
- **Iterative fixed-point solvers** (FPT): treat the whole trajectory as a fixed point and iterate, but backpropagate through every solver iteration — memory grows ~linearly with iteration count K, and repeated-substitution converges slowly.

FidLIF keeps hard-reset LIF fidelity AND parallel training AND step-by-step deployment inference in one neuron.

## Core Method

### 1. Trajectory as root-finding

Stack all T membrane potentials. With P the strictly-subdiagonal shift matrix (one-step local recurrence) and z_i = (1−ρ)(v_rest + Rc_i):

```
v = P((1−s)⊙v + v_rest·s) + q      ⇒      G(v) = v − P((1−s)⊙v + v_rest·s) − q = 0
```

The membrane-potential trajectory v is the ROOT of G(v) = 0.

### 2. Sigmoid relaxation — during the solve only

The Heaviside gate H(v_i − v_th) is non-differentiable. Replace with σ(α(v_i − v_th)) DURING Newton iterations (differentiable + stabilizes convergence). After convergence, spikes are emitted with the ORIGINAL Heaviside gate on the recovered trajectory: **final outputs remain binary spikes** — no fidelity loss in representation.

### 3. Newton iteration → affine recurrence → associative scan (the key step)

Because LIF recurrence is local (G_i depends only on v_i, v_{i−1}), the Jacobian is **lower bidiagonal**: JG = I − A with A strictly subdiagonal (A_ij = a_{j}^{(m)} for i = j+1). The Newton update becomes an AFFINE RECURRENCE:

```
v_1^{(m+1)} = b_1^{(m)}
 v_i^{(m+1)} = a_{i−1}^{(m)} · v_{i−1}^{(m+1)} + b_i^{(m)}
```

Affine maps compose associatively: `(x2,y2) ∘ (x1,y1) = (x2x1, x2y1 + y2)`. A **parallel associative scan** evaluates all T prefix updates in O(log T) temporal depth. Total forward depth: O(K log T).

Newton beats FPT's repeated substitution because each iteration propagates first-order corrections across many time steps at once (quasi-Newton wavefront), not just one.

### 4. Finite-step convergence (Theorem 1)

Induction: iteration m recovers the exact prefix v_i^{(m)} = v_i* for all i ≤ m. Exact recovery within ≤ T iterations for any initialization; empirically **K = 3 suffices** (MAE < 10⁻⁷ vs matched serial sigmoid-relaxed dynamics at K = 5).

### 5. Backward: ONE reverse scan, exactly BPTT-equivalent

Do NOT backprop through the K forward iterations. Implicit differentiation at the converged trajectory v*:

```
∂v*/∂x = −JG(v*)⁻¹ ∂G/∂x,    adjoint: JG(v*)ᵀ y = g
```

JG(v*)ᵀ is UPPER bidiagonal, so the adjoint is a REVERSE affine recurrence y_i = a_i* y_{i+1} + g_i → one reverse associative scan, O(log T) depth. Crucially, the adjoint needs ONLY (v*, {a_i*}) — not the forward iterates — so the forward solve runs with gradient tracking disabled and **memory is independent of K** (near-constant vs FPT's linear growth at T=256).

Equivalence: y_i ≡ δ_i, the total BPTT state gradient (chain rule on v_{i+1} = φ(v_i) gives the identical recurrence). Gradient error < 10⁻⁶ at K = 3 relative to serial BPTT.

### 6. Input-dependent parameters, causally generated

Enhance capacity with τ_i, R_i produced by a small causal generator g_ψ on the recent n-step input window C_i, bounded via sigmoid so ρ_i = exp(−Δt/τ_i) ∈ (0,1) always (leaky dynamics preserved). Parameters are generated BEFORE the iterative solve and held FIXED through the K iterations — no new temporal dependency enters the solver, and **step-by-step inference is preserved** (no future inputs needed). Ablation: removing this drops Seq-CIFAR10 91.25% → 80.66%.

## Results

| Benchmark | FidLIF | Notes |
|---|---|---|
| Seq CIFAR10 (ConvNet) | 91.25% best (90.99±0.25) | beats PSN 88.45, FPT 89.53 |
| Seq CIFAR100 | 66.42±0.17 | beats MF-PSN 66.21 |
| CIFAR10-DVS (VGG) | 84.13±0.65 | |
| SHD 80–140 steps (FCNet+delays) | 94.38±0.31 | K=3 enough at this length |

Parallel→serial consistency: same trained neuron evaluated step-by-step matches parallel accuracy (90.99 → 90.69, 94.38 → 94.30). Latency advantage grows with T (RTX 4090, FP32, Triton).

## Reusable Patterns (beyond SNNs)

1. **Banded-Jacobian → scan parallelization test**: any one-step-recurrent system (LIF, gated cells, discretized SSMs) whose residual G has support only on (i, i−1) admits Newton + associative-scan parallel recovery. FIRST check whether the Jacobian is bidiagonal/banded — that decides if this pattern applies.
2. **Relax-then-restore**: use a smooth surrogate only inside the iterative solve; re-quantize with the original hard gate after convergence so downstream sees exact binary/hard dynamics.
3. **Implicit differentiation for iterative forwards**: never backprop through solver iterations; differentiate the converged fixed point once. Decouples memory from iteration count (DEQ-style, applied to full TRAJECTORIES rather than equilibria).
4. **Causal parameter generation** reconciles train-time full-sequence parallelism with deploy-time incremental execution — the deployment constraint must be designed INTO the parameterization, not patched after training.

## When to Use

- Training SNNs on long sequences (T ≫ 100) where BPTT memory/time dominates
- Applications needing BOTH parallel training and streaming/edge step-by-step inference
- Any recurrent dynamical system with local (banded) temporal coupling to parallelize

## Key References

- FPT (Feng et al. 2025): predecessor fixed-point approach, soft-reset only, memory grows with K
- PSN (Fang et al. 2023) / MF-PSN (Xue et al. 2026): reset-removal line, breaks recurrence
- Blelloch (1990): associative scans; Wang et al. (2020): scans for RNN BPTT
