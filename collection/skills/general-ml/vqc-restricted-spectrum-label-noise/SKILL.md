---
name: vqc-restricted-spectrum-label-noise
description: Use VQC restricted-spectrum heads to resist label noise.
category: ai_collection
version: 1.0
author: hermes-cron
license: MIT
metadata:
  hermes:
    tags: [label-noise, variational-quantum-circuit, spectral-smoothness, medical-imaging, memorization]
    related_skills: [supermartingale-label-transition-qnn, hqnn-medical-image-classification, vqc-architecture-comparison]
---

# Restricted-Spectrum VQC Heads: Architectural Label-Noise Robustness

## When to Use

- Training image classifiers (esp. medical) on datasets with corrupted/ambiguous annotations, when noise rate is unknown or unestimable
- You want robustness WITHOUT explicit noise-handling components (no loss correction, no sample selection, no transition matrices)
- Designing hybrid quantum-classical pipelines where qubit count must be decoupled from input resolution
- Diagnosing WHY a classifier head resists (or fails to resist) memorization of mislabeled examples

## Source

arXiv:2610.16153 (Oct 2026) — "Architectural Robustness to Label Noise Using Variational Quantum Circuits for Medical Image Classification" (Epa, Epa, Liyanaarachchi, et al., Univ. of Moratuwa / Toronto / UBC / UIUC)

**Trigger keywords**: label noise, VQC robustness, spectral smoothness, trigonometric polynomial head, memorization dynamics, MedMNIST, frozen backbone bottleneck, angle encoding frequency support, parameter-shift Lipschitz, hybrid quantum-classical medical imaging

## Core Insight

Label-noise robustness can be an **architectural property**, not a training-procedure property. Label flips force the decision function to change sharply between neighboring feature points; a head whose function class is *intrinsically smooth* cannot represent that sharpness, so it degrades only as fast as the true signal dilutes — no noise rate estimation needed.

A single-angle-encoding VQC is exactly such a class.

## Theory (the reusable core)

### 1. Frequency-support confinement
With product angle encoding |ψ(z)⟩ = ⊗ⱼ R_Y(zⱼ)|0⟩ and z-independent ansatz U(θ), every Pauli expectation f_σ(z) = ⟨ψ|U†σU|ψ⟩ decomposes through cos²(z/2)=(1+cos z)/2, sin²(z/2)=(1−cos z)/2, sin(z/2)cos(z/2)=sin(z)/2. Each coordinate zⱼ contributes frequencies only in Ωⱼ = {−1, 0, +1}:

f_σ(z) = Σ_{S⊆{1..N}} Σ_τ a_{S,τ}(θ) · Π_{j∈S} τⱼ(zⱼ)

a multilinear trigonometric polynomial, degree ≤1 per variable. **Training reweights a fixed low-frequency basis; it cannot introduce higher harmonics.** Depth adds nothing to expressivity (single-encoding case of Schuld–Sweke–Meyer 2021: spectrum grows only with data re-uploading).

### 2. Parameter-independent Jacobian bound
Parameter-shift identity gives |∂f_σ/∂zⱼ| = ½|f_σ(z+π/2eⱼ) − f_σ(z−π/2eⱼ)| ≤ 1 (since |f_σ|≤1). For the full 2N-output head: ‖J‖_F ≤ √2·N — a Lipschitz constant **independent of trained parameters**. A matched ReLU head's Lipschitz constant ‖A₂‖‖A₁‖ is unbounded and grows during training.

**Key contrast**: the two heads differ in the *shape* of capacity (how sharply they respond to small code displacements), not its quantity (parameter count).

## Architecture Pattern

```
224×224×3 RGB image
  → frozen ViT-B/16 backbone ϕ(·)      (768-d features, no fine-tuning)
  → trainable linear bottleneck W_c: 768→8, + arctan → z ∈ (−π/2, π/2)⁸
  → 8-qubit VQC: R_Y angle encode → L=4 layers of R_Z/R_Y + CNOT ring
  → dual Pauli ⟨σ_Z⟩,⟨σ_X⟩ readout → y_q ∈ ℝ¹⁶
  → linear classifier + softmax
```
- ~6,400 trainable params total (VQC only 64) — vs ~86M for fine-tuned ViT
- arctan bounds z to (−π/2,π/2): unique quantum-state mapping, no R_Y periodicity ambiguity
- Frozen backbone + 64 quantum params keeps optimization out of barren-plateau regime
- Dual X+Z readout adds independent low-frequency projections (improves clean accuracy WITHOUT extending frequency support)

## Empirical Results

- **Clean**: leads 5/6 MedMNISTv2 vs published hybrids (+17.4 BloodMNIST, +15.7 PathMNIST); 11-class OrganA/C where fully-parameterized hybrids (QTNet, HQNet) collapse to ~12% (chance)
- **50% symmetric noise**: PathMNIST 89.8% vs best baseline 58.0% — model loses only 1.2% relative to its own clean accuracy while half the labels are wrong
- **Control experiment (the causal isolation)**: same backbone/bottleneck/param-count/optimizer, only 8→16 ReLU map swapped in. Indistinguishable on clean labels (90.94 vs 90.92 PathMNIST); gap grows monotonically with noise → 10.8 pts at 50% (PathMNIST 89.75 vs 78.96)
- **Memorization dynamics (60 epochs, early stop OFF)**: both heads fit corrupted labels equally (7.0% vs 7.4% agreement — NOT incapacity); quantum head loses 2.5 pts peak→end vs classical 6.5. Random-label capacity test: quantum reaches 89% of classical excess memorization → the 8-d bottleneck is the binding capacity constraint; the circuit contributes *stability under prolonged training*
- **Sensitivity ratio** (random code perturbation): quantum 0.71–0.88 vs classical 1.71–2.89 (2–4× lower, within √2·N≈11.3 bound)
- **IDN (instance-dependent noise)**: competitive but NOT leading at 20%; partially reverses at 50% — expected: IDN flips concentrate on genuinely ambiguous cases, so corruption is partly aligned with smooth class structure and inside the expressible band
- DermaMNIST: AUROC 0.906 but macro-F1 0.438 — robustness to label noise ≠ class-imbalance handling

## Honest Limitations (authors' own)
- Noiseless state-vector simulation (PennyLane lightning.qubit); coherent gate errors on hardware may distort the learned function unpredictably
- MedMNISTv2 source is 28×28 upsampled to 224 — not native high-res
- Advantage is encoding-specific: data re-uploading widens the spectrum and should erode it (falsifiable prediction)
- Robustness is bought by restricted expressivity: trails NQNN by 7.5 pts clean on DermaMNIST
- Authors explicitly do NOT claim the effect is intrinsically quantum — a smoothness-matched classical head is the stated future test

## Reusable Patterns

### Pattern 1: Robustness-by-function-class, not by-procedure
When corruption (label noise, adversarial shifts) requires sharp decision boundaries, choose a head with confined frequency support / bounded Lipschitz constant rather than adding correction machinery. The head then *cannot* express the corruption regardless of training length — robustness needs no noise-rate estimate.

### Pattern 2: The matched-everything control
To attribute an effect to one component, build a control sharing EVERYTHING (backbone, bottleneck dims, arctan activation, param count, optimizer, LR) and swap ONLY the component under test. Clean-label parity + noise-dependent gap = causal isolation of inductive bias.

### Pattern 3: Measure memorization directly, not via test accuracy
Track per-epoch agreement with corrupted labels (memorization proper), with true labels (resistance), and on the clean subset (signal fit), with early stopping disabled. Distinguish "fits corruption slowly" (slow optimization) from "fits it but stays stable" (the useful property — a model that only resists if stopped at the right epoch needs trusted validation labels, precisely what's missing when annotations are unreliable).

### Pattern 4: Bounded bottleneck as resolution–qubit decoupler
Input resolution is decoupled from qubit count by making the circuit see only an N-dim code from a trainable linear bottleneck + arctan. 224×224×3 images on 8 qubits. The bottleneck (not the head) is the binding capacity constraint — confirmed by random-label capacity test.

### Pattern 5: Encoding choice = inductive bias dial
Single angle encoding → spectrum {−1,0,+1}/coordinate (max smoothness). Data re-uploading → wider spectrum (more expressivity, less robustness). Choose encoding by the noise structure: symmetric noise lives in high frequencies (suppressed); instance-dependent noise lives partly in the smooth band (not suppressed — matches the IDN results).

## Implementation Notes

- Simulator: PennyLane lightning.qubit, adjoint differentiation for memory efficiency
- LR split: η_q=0.01 (VQC), η_c=0.003 (classical parts); Adam, batch 32, ≤30 epochs, 5-epoch patience early stop, 0.2 dropout in early classical layers
- Depth L=4 peaks on 4/6 datasets then saturates (predicted by theory: depth reweights the fixed basis without extending support)
- 3 independent circuit init seeds; report mean±std

## Related Skills

- supermartingale-label-transition-qnn — the *explicit-correction* counterpart (stability-gated transition-matrix refinement); use together: architecture restricts what can be fit, correction handles the rest
- hqnn-medical-image-classification — broader hybrid pipeline design
- fourier-vqc-nonlinear-embedding-barren-plateau — Fourier analysis of VQC expressivity
- training/globally-optimal-snn-training — parameter-reconstruction for smooth heads
