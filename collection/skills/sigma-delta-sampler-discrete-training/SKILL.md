---
name: sigma-delta-sampler-discrete-training
description: Sigma-delta noise-shaped annealing for discrete NN training.
trigger: binary neural network training, ternary weights, quantization-aware training, QUBO Ising solver, noise shaping, sigma-delta, on-device training, edge AI, straight-through estimator replacement, discrete weight optimization, BitNet
author: engineering-lion5
category: ai_collection
version: 1.0
license: MIT
related_skills: shiftlif-power-of-two-quantization, quantization-snn-beyond-accuracy, training-free-looped-transformers, fpqc-hot-framework, hotstart-quantum-portfolio-optimization
---

# Sigma-Delta Sampler: Noise-Shaped Annealing for Discrete-Weight Training

**Source**: arXiv 2610.22621 (Chen, Xiao, Zhu, Wang, Eshraghian, Chakrabarty — WashU / UCSC, Oct 2026). Train binary {−1,+1} and ternary {−1,0,+1} networks directly in discrete space by embedding a stochastic sampling-and-annealing step as a noisy quantizer inside a first-order Sigma-Delta (ΣΔ) noise-shaping loop.

## Core Insight

The training loss of a discrete-weight network, expanded over the Walsh–Fourier (parity-monomial) basis of {−1,+1}^D, is EXACTLY a hierarchical high-order Ising Hamiltonian: L(W) = Σ_m Σ_{|S|=m} J_S^(m) Π_{i∈S} W_i. Low-order terms give a smooth envelope (descent directions, low-frequency); high-order terms add frustration and local minima (white/high-frequency noise). Weight quantization error, mini-batch coupling fluctuation, and sampler randomness share the same white spectral signature. Signal and noise are separated IN FREQUENCY, not amplitude — so reshape the noise spectrum instead of suppressing it: a ΣΔ loop pushes quantization noise out of the low-frequency adaptation band (NTF(z) = 1 − z⁻¹, first-order high-pass), letting discrete updates track the smooth descent contour.

This closes both gaps vs. classical Ising solvers: single-flip SA is stable but O(D) too slow at network scale; parallel SA scales but diverges on rugged landscapes (per-coordinate flips from noisy local fields, uncontrolled joint energy). The ΣΔ accumulator provides the temporal memory that makes parallel flips coherent.

## Algorithm (verified sign conventions — see Pitfalls)

Per coordinate i, maintain integrator state ω_i (init 0). Each iteration:

1. **Integrate**: ω_i ← ω_i + g_i − β·d_i^{n−1}, where g = minibatch gradient, d^{n−1} = realized discrete update of the previous step, β = per-row/kernel learnable gain (feedback closes on the realized update). For ternary via W = W_on − W_off the feedback closes on the EFFECTIVE weight: ω ← ω + g − ½Δβ(W − W_prev).
2. **Adaptive threshold (AGC)**: track geometric-mean scale Ḡ = EMA(log|ω| + ε). Target above-threshold fraction ramps harmonically ρ_t = ρ_init + (ρ_final − ρ_init)·n/(n + τ_thld) with defaults ρ_init = 0.2 (80% stochastic early), ρ_final = 0.7 (30% stochastic late). Realized fraction ρ_ema tracked by EMA; threshold µ = µ_min + γ·Ḡ·(ρ_ema/ρ_t)^α_agc.
3. **Sample** (temperature T_n = T0/(T0 + n/τ), hyperbolic schedule):
   - Deterministic flip W_i ← −W_i if |ω_i| > µ AND sign(ω_i) == sign(W_i)
   - Stochastic flip W_i ← −W_i with probability exp(−|ω_i| / (Ḡ·T_n)) if |ω_i| ≤ µ
   - Otherwise keep. Update d = W_new − W.
4. **Ternary decomposition**: W = W_on − W_off with W_on, W_off ∈ {0,1}; single SHARED integrator per weight; antipodal decision signals d_on ~ P(+ω, T), d_off ~ P(−ω, T); INDEPENDENT random draws per component (uncorrelated stochastic branches). No second gradient buffer (W_off carries no own gradient; ∂W/∂W_on = +1, ∂W/∂W_off = −1).
5. **Continuous parameters stay under AdamW**: per-output-row scales, biases, norms, embeddings, LM head (negligible memory vs discrete bulk). This is the STE-inverted design: STE keeps a full-precision latent copy of every weight; ΣΔ needs only ω (reuses the gradient buffer) — 6 bytes/param vs 16 bytes/param for FP/STE (which need weight+gradient+two AdamW moments at 4 bytes each).

**Large-scale stabilization**: for billion-parameter models, cap deterministic flips per layer per step (update-rate cap ~1e-3) inside the feedback loop.

## Theory

Linearizing the closed loop around a local minimum with Hessian H gives z-domain error E(z) = −[I + z⁻¹ηH − I]⁻¹·η(1 − z⁻¹)·Q(z): the noise transfer function NTF(z) = 1 − z⁻¹ is a first-order high-pass on quantization noise. In-band (bandwidth γa ≪ iteration rate γs) mean-square error scales as (γa/γs)² (quadratic suppression; paper Eq 21 quotes ≈ γa²/3γs², constant set by frequency-unit convention). The accumulator residual (ω − d) shows the V-shaped spectrum: low-frequency branch = preserved learning signal, high-frequency branch rising to Nyquist = shaped quantization noise (paper Fig 2g). Update budget self-regulates: coordinates with large |g| flip often and keep |ω| small (low-SNR, rapid discharge); coordinates with small |g| flip rarely and accumulate |ω| (high-SNR) — emergent per-parameter adaptive learning rate in discrete space.

## Verified Reproduction (2026-10-20, planted QUBO D=100)

Planted QUBO with known minimizer: L(W) = ½WᵀQW − bᵀW, random ±1 symmetric Q with diagonal shift λI (λ > spectral bound → PD), b = QW*, W* uniform binary. 1000 steps, hyperbolic T0=5/τ=100:
- ΣΔ-Sampler: EXACT recovery of W* (loss == L(W*) to machine precision) on 3/8 seeds; ≥0.96 match on all seeds; convergence within ~5 steps (paper: within ~100 with warmup).
- Single-flip SA: 0.49 match, oscillates, never reaches optimum. Parallel-flip SA: 0.31, diverges. PF-20: 0.33. All baselines fail as paper reports.
- STE is the T→0 deterministic limit of the same sampler family (decision signal = latent fp weight).

## Performance (paper)
- CIFAR-10: ternary VGG-8 (13M) 92.20% vs FP 92.88% (>99% retention); binary 91.89%; 13.4 s/epoch ternary vs 9.2 s FP; TWN pipeline 18.5× slower.
- ImageNet-1k: ternary ResNet-18 61.65% Top-1 / 83.81% Top-5 — within 0.15%/0.39% of TWN (which keeps an FP classifier head; this model is fully discrete).
- Continual learning: prior-task accuracy preserved across class-incremental phases.
- MatMul-free LLMs (BitNet-style) 370M/1.3B/2.7B: stable from-scratch pretraining (FineWeb-Edu, ~1.07B tokens); beats STE under matched continued pretraining from the same quantized checkpoint (STE must build latent pressure before any flip; ΣΔ flips viable directions directly).
- Hardware: >50% training-memory reduction vs QAT; order-of-magnitude speedup; weight-update DRAM traffic down 4 orders of magnitude (writes only on committed flips).

## When to Use
- On-device / edge training or fine-tuning of binary/ternary models (training footprint → inference footprint).
- Extreme-low-bit (1-bit / 1.58-bit) training from scratch where post-training quantization and STE underperform.
- Any discrete optimization where an Ising-solver viewpoint applies but the objective is generalization, not ground state: replace per-iteration Metropolis on raw gradients with the ΣΔ loop.
- Mapping onto Ising hardware (quantum annealers, CIMs, probabilistic bits): the loop's primitives (binary states, thermal flips, local-field arithmetic) are natively supported.

## Pitfalls (verified 2026-10-20)
- **Sign-convention trap**: the working update is ω ← ω + g − β·d with flip when sign(ω) == sign(W). A 'more stable-looking' variant (input −g, flip when sign(ω) ≠ sign(W)) FAILS the planted-QUBO test (0.14 match). Trust the literal paper convention; verify any re-derivation against the planted-QUBO positive control before use.
- **Never measure noise-shaping spectra after convergence**: post-freeze streams are DC-dominated. Measure PSD of (ω − d) only during the active-flip phase.
- **AGC is load-bearing**: without the log-domain EMA scale + fraction-locking ramp, the threshold µ cannot track ω magnitudes that span orders of magnitude across layers/stages; early-stochastic → late-deterministic crystallization emerges from the ρ ramp (0.2→0.7), not from temperature alone.
- **Feedback must close on the realized update** (or effective ternary weight): an open-loop accumulator with no −β·d term is not noise shaping.
- **Shared integrator for ternary on/off halves** — two integrators per weight double memory and break the antipodal symmetry that keeps W_off gradient-free.

## References
- arXiv 2610.22621 — Noise-shaped Sampling and Annealing for Scalable On-the-edge Training of Binary and Ternary AI Models
- Related local skills: shiftlif-power-of-two-quantization (SNN quantized neurons), quantization-snn-beyond-accuracy (EMD evaluation of quantized SNNs), scale-control rules in qaoa-feasibility-penalty-scheduling (temperature-scheduled discrete optimization).
