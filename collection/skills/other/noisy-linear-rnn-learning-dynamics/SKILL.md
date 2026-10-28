---
name: noisy-linear-rnn-learning-dynamics
description: Use when intrinsic noise shapes RNN learning dynamics.
category: ai_collection
---

# Noisy Linear RNN Learning Dynamics

**Source**: Vastola & Rajan (Harvard Medical School / Kempner Institute), "A theory of noisy linear recurrent neural network learning dynamics", arXiv:2610.35785 (Oct 2026).

Analytically tractable theory of how **intrinsic noise** (diffusion tensor S = GGᵀ in ṙ = −γr + Wr + x(t)u + Gη) shapes representation learning in linear RNNs trained on a leaky-integration task. Extends Bordelon et al. (2025) noise-free theory; all formulas below numerically verified (2026-10-27, 1e-12–1e-4 agreement).

## Core framework

- Dynamics: ṙ = Ar + x(t)u + Gη(t), A := −γI + W; white-noise scalar input x(t); readout y = vᵀr.
- Induced filter: f(t) = e^(−γt) vᵀ e^(Wt) u; target f*(t) = e^(−c*t) (single timescale leaky integrator).
- Objective (exact under white-noise input): J = ∫½[f−f*]² dt + ∫½ e^(−2γt) vᵀe^(Wt)S e^(Wᵀt)v dt + κ/2(‖u‖²+‖v‖²) = J_filter + J_noise + J_reg.
- Key structural fact: J_filter is invariant to the gauge v→Tᵀv, u→T⁻¹u, W→T⁻¹WT (massive solution degeneracy), but **J_noise is not** (S→T S Tᵀ). Noise is a gauge fixer = "representational pressure".

## Result 1 — noise picks preferred directions and scales

- With W = (γ−c*)I and constraint vᵀu = 1, J_noise is minimized by the **noise-inverse readout**: v* = S⁻¹u / (uᵀS⁻¹u) (reservoir-computing limit; verified by projected gradient descent to |cos|=1.0).
- Without regularization, optimal readout scale → 0 and read-in scale → ∞ (rescaling u,v keeps filter but scales noise by α²).

## Result 2 — alignment phase: weights rotate away from noisy directions

Small-init (rich regime, order ε) gradient flow reduces to:
- du/dτ ≈ v/(c*+γ) − κu;  dv/dτ ≈ u/(c*+γ) − Sv/2γ − κv;  dW/dτ ≈ vuᵀ/(c*+γ)² − vvᵀS/4γ².

In the S-eigenbasis each component evolves as an independent 2×2 linear system with eigenvalues

λ±ᵢ = −(κ + sᵢ/4γ) ± √(sᵢ²/16γ² + 1/(c*+γ)²)   (sᵢ = noise level of direction i)

λ+ᵢ **decreases** with sᵢ, so u, v, W exponentially align to the least-noisy eigenvector(s) of S — the solution becomes far less initialization-dependent than in the noise-free theory. Noise also breaks the u=v "balancing" symmetry.

## Result 3 — post-alignment 3D dynamics (κ=0)

Rank-one ansatz u≈u(τ)u₀, v≈v(τ)u₀, W≈[γ−c(τ)]u₀u₀ᵀ reduces N(N+2)-dim dynamics to 3 scalars (Eq 18-19 of paper). Verified numerically:
- d/dτ[u²−v²] = σ²v²/c > 0  →  u→∞, v→0 while filter amplitude N := uv → 1.
- c converges to c*; J_noise and J_filter both → 0 (noise on slower timescale).

## Result 4 — phase transition 1 (trainable u,v + regularization)

Minimizing J over u,v gives J(c) = 1/4c* − c·[1/(c*+c) − κ√(1+σ²/2κc)]²₊. Nontrivial solution exists iff the bracket > 0 somewhere. Critical noise level:

σ²_crit(κ) = (1−q(κ)²)²/q(κ),  q(κ) = (2/√3)·sinh(⅓·arsinh(3√3·κ·c*))

- Valid for κ < 1/c*; σ²_crit = 0 for κ ≥ 1/c* (regularization alone kills the nontrivial solution).
- Small κ: q ≈ 2c*κ, σ²_crit ≈ 1/(2c*κ); σ²_crit → ∞ as κ → 0 (no transition without regularization).
- Above σ²_crit the optimal filter amplitude N_opt = 0: **trivial amplitude collapse** (system trades task performance for noise minimization).
- Verified: max_c of the bracket = 0 (1e-12) exactly at σ²_crit, >0 below, <0 above, for κ ∈ {0.02..0.7}.

⚠️ PDF extraction pitfall: pdftotext/fitz corrupt Eq 22-23 and Eq 26-27 (fraction displacement). The correct q(κ) has sinh in the NUMERATOR: q = (2/√3)·sinh(⅓ arsinh(3√3κc*)) — NOT 2/(√3·sinh(...)). The paper's own small-κ limits (q≈2c*κ) + numerical boundary check disambiguate.

## Result 5 — phase transition 2 (frozen u=v=1, only W trainable)

J(c) = (1+σ²)/4c − 1/(c*+c) + 1/4c* has a stable finite optimum only below σ²_crit = 3:

c_opt = √(1+σ²)·c* / (2 − √(1+σ²))

- c_opt = c* at σ²=0; diverges like 1/(3−σ²) as σ²→3⁻ (infinitely fast filter = the escape route to f=0); above σ²=3 J is monotone decreasing in c so learning drives c→∞.
- (Also corrupted in PDF extraction; re-derived from dJ/dc=0 and verified against numeric argmin to <0.1% at σ² ∈ {0,0.5,1,2,2.9}.)

## How to use / apply

1. **Modeling noise in biological or artificial RNNs**: parametrize intrinsic noise by its diffusion tensor S; the S-eigenspectrum (not just overall gain) determines which state-space modes learning selects.
2. **Diagnosing trivial-solution collapse** in noise-trained RNNs: check filter/response amplitude N against σ²/κ ratio; near σ²_crit the learned timescale blows up before amplitude collapses.
3. **Regularization interplay**: weight decay converts noise from a nuisance into a phase boundary; small κ makes the network noise-robust (σ²_crit ≈ 1/2c*κ).
4. **Reservoir readout design**: the noise-optimal readout reweights by S⁻¹ — preferentially read out low-noise directions when calibrating BCI/decoder weights.
5. **Initialization-independence**: with anisotropic noise, converged solutions cluster on the low-noise subspace, so init-sensitivity diagnostics from noise-free theory overestimate variability.

## Numerical verification anchors (2026-10-27)

- Eq 13/14 eigenvalues: exact match to 2×2 system eigvals (err ≤ 2e-16); λ+ᵢ monotone decreasing in sᵢ.
- Alignment sim (S eigenvalues {0.05, 1, 6}): u,v converge to least-noisy eigenvector, |cos| ≥ 0.9998.
- Eq 20 identity along simulated gradient flow: rel err ≤ 7.3e-6; uv→0.98+, u/v asymmetry reproduced.
- c_opt numeric vs analytic: 1.000/1.000, 1.580/1.580, 2.414/2.414, 6.464/6.464, 78.5/78.5 (σ² = 0..2.9).
- Phase boundary: bracket max = 0 at σ²_crit to ≤1e-11 for five κ values.
- v* optimality: projected-GD matches closed form at |cos| = 1.000000.

## Related skills
- `efficiency-robustness-rnn-solution-space` — RNN solution-space geometry without noise
- `lyapunov-spectrum-random-neural-networks` — chaos (deterministic "noise") in random RNNs
- `dynamical-isometry-plasticity` — complementary rich-regime learning theory
- `low-rank-rnn-learning-dynamics` — low-rank learning structure that noise breaks degeneracy of
