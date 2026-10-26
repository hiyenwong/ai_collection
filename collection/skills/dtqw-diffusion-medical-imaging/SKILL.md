---
name: dtqw-diffusion-medical-imaging
description: Quantum-walk forward diffusion + classical U-Net denoising for medical images.
---

# DTQW Hybrid Quantum Diffusion for Medical Image Analysis

**Source**: arXiv:2609.31070 (Venturelli, Martina, Parigi, Caruso, Cervera-Lierta, González Ballester — BCN Medtech/UPF, Univ. Florence, BSC; 2026-09-25)
Categories: eess.IV, cs.AI, cs.CV, cs.ET, cs.LG, quant-ph. Code: github.com/trianam/quantumDiffusionModelsMedicalImageAnalysis
Validated on real IBM NISQ hardware (ibm_torino, 133 qubits).

## Core Idea

A **hybrid quantum-classical diffusion model (QDM)** that splits the two halves of a
diffusion model across the quantum/classical boundary in the *opposite* way of most
QDM work:

- **Forward (noising) process = QUANTUM**: a Discrete-Time Quantum Walk (DTQW) on a
  ring-chain of intensity levels, executed on real NISQ hardware.
- **Backward (denoising) process = CLASSICAL**: a U-Net trained to reverse the
  quantum-generated noise.

The counter-intuitive trick: **hardware noise is the feature, not the bug**. A pure
unitary quantum walk never converges to the uniform prior (it's invertible) — the
device's intrinsic decoherence supplies the missing dissipation that makes the
forward process converge. No error correction or mitigation needed for the forward run.

## Architecture

### 1. Per-pixel DTQW forward process

- Each pixel/voxel quantized to `2^Nq` intensity levels (Nq = 5 → 32 levels, Nq = 6 → 64 levels).
- Ring-chain Markov topology: each ring node = one intensity value → only Nq+1 qubits
  (Nq positional + 1 coin).
- State: `|ψ0⟩ = |i0⟩ ⊗ |0⟩` (position ⊗ coin); coin = Hadamard.
- Dynamics: `ρt = E(Ut ρ0 Ut†)` — unitary DTQW step **plus noise channel E** from the hardware.
- Step circuit (from Arrazola et al. QW): H gates + controlled phase rotations
  `Rk = diag(1, e^{2πi/2^k})` + inverse QFT `F†` + coin C.
- Measurement → categorical sampling: `p(it) = Tr(Pi ρt)`; estimate with 8192 shots.

**Scaling trick**: run ONE DTQW always from `|0⟩`, then *add* the sampled result to the
pixel's initial value `i0` (mod 2^Nq). One quantum run serves every pixel — this is why
real-world image sizes are feasible where other QML medical work is stuck at toy data.

RGB: independent DTQW per channel. 3D volumes: same walk per voxel.

### 2. Classical backward U-Net

- **2D version**: 5 downsampling encoders (h=1 conv layers, ReLU, maxpool) + 4
  upsampling decoders (transpose conv, skip connections: `d(l) = cat(up(l)(d(l-1)), e(L-l+1))`).
  Time embedding summed into encoder activations only. Shallow bottleneck.
- **3D version** (volumes): 4 enc/dec blocks + 3-block bottleneck, time embedding in
  *both* encoder and decoder, **GroupBatchNorm** for gradient stability, **SiLU**
  (`x·σ(x)`) instead of ReLU, early stopping at ~4000 epochs (2D: 20k epochs).
- Training pairs `(it, it+1)` built by re-preparing `|it⟩` and doing one more DTQW step.
- Optimizer ADAM lr=1e-3, cross-entropy loss (categorical intensity values).

**Time-dependent hybrid loss** (used for BraTS2020):
`L = Σt −αt Σ y log p − (1−αt) KL(P‖Q)` — high t → learn pixel-value distribution
(KL term dominates), low t → reconstruct structure (CE dominates).

### 3. Evaluation

KL divergence (pixel-intensity histograms), FID (Inception-v3 features; for 3D
average FID over slices z=5,10,15,20,25), SSIM, plus PCA(2D)+KDE overlap plots of
original vs generated distributions.

## Key Results (Table I, 100 samples)

| Dataset | KL (Q vs C) | FID (Q vs C) | SSIM (Q vs C) |
|---|---|---|---|
| BloodMNIST 64×64 RGB, 32 lvl | 0.046 / 0.098 (β=βt) | 243.3 / 166.6 | 0.336–0.377 / 0.220–0.243 |
| BraTS2020 190×190 gray, 64 lvl | 0.192 / 0.396 | 297.7 / 280.3 | 0.569–0.676 / 0.646 |
| FractureMNIST3D 28³, 32 lvl | 0.011 / 0.047 | 89.7 / 100.1 | 0.550–0.564 / 0.564 |

Honest read: quantum model **wins KL everywhere** and **wins FID+SSIM on 3D**, loses
FID on 2D (FID's Inception-v3 prior is a poor fit for specialized medical data).
Generated brain slices reproduce ventricles, folds, and occasional tumoral masses;
no mode collapse despite BraTS2020's single-mode PCA.

## When to Use / Reusable Patterns

1. **Noise-as-resource design**: when a target process needs *irreversible* mixing
   but your quantum primitive is unitary — let device decoherence supply the
   dissipation instead of fighting it with error mitigation.
2. **Additive-walk scaling**: amortize one quantum primitive over an arbitrary-size
   dataset by translating outputs (run from |0⟩, add offset) instead of re-encoding
   each datum as a quantum state.
3. **Ring-chain topology matching**: choose the algorithm's graph to match hardware
   connectivity (IBM heavy-hex → ring), so transpilation cost stays low
   (optimization level 3, 6–7 connected qubits).
4. **Time-dependent loss blending**: αt-scheduled CE+KL — distribution matching early
   (high t), structure reconstruction late (low t).
5. **Forward/backward split-point menu** for hybrid generative models: which half is
   quantum matters more than "more quantum". This paper: quantum forward + classical
   backward is scalable; the reverse (quantum backward, cf. prior work [48,49]) hits
   NISQ size limits.

## Pitfalls

- FID on medical images is misleading when the Inception features were pretrained on
  natural photos — report KL + SSIM alongside, say so explicitly.
- Low resolution + coarse quantization (64×64, 32 levels) depresses SSIM independent
  of model quality; don't compare across datasets with different quantization.
- DTQW needs a coin qubit with ≥3-degree connectivity to drive bidirectional
  diffusion; qubit selection on device matters.
- 3D U-Net overfits quickly — early stopping required.

## Reproduction Pointers

- Qiskit, ibm_torino, 6 qubits (5 intensity + 1 coin) for 32 levels; 7 for 64 levels.
- Shots: 8192. Transpile optimization_level=3.
- Datasets: BloodMNIST class 6 (3329 imgs), BraTS2020 (484 slices, 190×190),
  FractureMNIST3D (1370 vols, 28³).

## Activation Triggers

quantum diffusion model, QDM, DTQW, discrete-time quantum walk, hybrid quantum-classical
generative model, medical image generation, NISQ noise as resource, quantum forward
process, synthetic medical data, BloodMNIST, BraTS2020, FractureMNIST3D, quantum walk
denoising, noise-as-feature.
