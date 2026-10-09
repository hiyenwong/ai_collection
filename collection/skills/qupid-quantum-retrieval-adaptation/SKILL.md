---
name: qupid-quantum-retrieval-adaptation
description: "Use when adapting medical RAG retrieval to small archives."
version: 1.0
author: hermes-cron
license: MIT
metadata:
  hermes:
    tags: [quantum-retrieval, medical-rag, data-reuploading, contrastive-adaptation]
    related_skills: [cqc-rag-cross-query-consistency, adaptive-quantum-classical-fusion]
---

# QuPID: Quantum Parameter-Efficient Input-Dependent Retrieval Adaptation

## When to Use

- Adapting a frozen-encoder retrieval system (RAG) to a small local archive (hundreds of examples), especially medical imaging under data-locality constraints
- Designing any quantum similarity/retrieval circuit — the shared-unitary fidelity degeneracy check must run FIRST
- Replacing LoRA/adapters for retrieval adaptation with an ultra-compact (p≈60) readout

## Source

arXiv:2609.33351 (Sep 2026) — "QuPID: Quantum Parameter-Efficient Input-Dependent Retrieval Adaptation for Medical RAG"

**Trigger keywords**: quantum retrieval adaptation, medical RAG, fidelity degeneracy, data re-uploading, measurement readout retrieval, label-free contrastive adaptation, ChestX-ray14, MURA, LoRA alternative, low-data retrieval, amplitude encoding

## Core Problem

Medical case retrieval on frozen encoders (ViT-L/16) fails because pathology occupies a small image region while shared anatomy dominates pooled features — a 'Normal' study and an 'Early Pneumonia' study become nearly collinear in frozen feature space, feeding diagnostically inconsistent evidence to RAG generators. Data protection rules keep images inside the hospital; local archives offer few adaptation examples.

## The Degeneracy Pitfall (Proposition 1)

**Critical design constraint for ALL quantum retrieval systems:**

The natural variational retrieval design — apply one shared trainable circuit U(θ) to both query and database states, rank by fidelity — CANNOT be trained:

```
Sim_fid(x_q, x_p; θ) = |⟨ψ_in(x_q)| U(θ)† U(θ) |ψ_in(x_p)⟩|² = |⟨ψ_in(x_q)|ψ_in(x_p)⟩|²
```

The shared input-independent unitary cancels: `U(θ)†U(θ) = I`. Fidelity ranking is INVARIANT to training. Any quantum retrieval design applying the same unitary to both sides of the overlap is untrainable, regardless of ansatz power.

## Methodology

### Architecture (60 trainable parameters total)

1. **Frozen ViT-L/16** encodes all images → d=1024 features
2. **Amplitude encoding**: normalized feature ĥ → n_q = log₂(d) = 10 qubits (exponentially compact)
3. **L=3 blocks**, each: trainable RY rotation layer → CNOT ring entangling layer → **data re-uploading layer** E(x; α) = ⨂ RY(α_j·s_j(x)) re-injecting block-pooled projections of the input (fixed projections s_j(x) = 2^(j-1)·pooled block mean, scaled by trainable α_j)
4. **Measurement readout** (NOT state overlap): z(x) ∈ ℝ^40 = local Pauli expectations ⟨Z_j⟩, ⟨X_j⟩, ⟨Z_jZ_{j+1}⟩, ⟨X_jX_{j+1}⟩ (cyclic indices), M = 4·n_q
5. **Retrieval similarity = cosine between readout vectors**, not state fidelity

Parameter budget: 2·n_q·L = 60. All gates real → state stays real-valued.

### Why measurement readout escapes the pitfall

Without re-uploading, each readout component is exactly a quadratic form ĥ^T A_m(θ) ĥ. With re-uploading, A_m(θ, α, x) is modulated by trig functions of linear input projections — **input-modulated quadratic feature maps**. The 60 parameters jointly specify M=40 structured full-rank forms (each A_m orthogonally similar to a Pauli observable, spectrum ±1). Comparing measurement STATISTICS (not states) is what makes the similarity trainable.

### Spectral control (Proposition 2)

Re-uploading angles α_j^(l)·2^(j-1) define the Fourier frequency support of the readout channel. At α=1 frequencies are integers with bandwidth |ω| ≤ L·(2^n_q − 1). Re-uploading rate α is a tunable expressivity dial — the Schuld et al. (2021) Fourier analysis specialized to re-uploaded retrieval channels.

### Label-free contrastive adaptation

Hospitals cannot label — adapt with SimCLR-style contrastive on the quantum similarity:

```
L(θ,α) = −(1/2B) Σ_i log[ exp(Sim_qt(x_i, x_i+)/τ) / Σ_{j≠i} exp(Sim_qt(x_i, x_j)/τ) ]
```

- Two pathology-preserving augmentations → positive pair; in-batch negatives; τ = 0.07
- Every gate generator has two eigenvalues → **exact parameter-shift gradients** (no finite-diff approximation)
- Train via classical circuit simulation; deploy as fixed GPU function on 1024 amplitudes — **no quantum hardware required at inference**

### Generalization bound (Proposition 3)

Covering-number argument: gap = O(√(p·log(1+nR·L_lip) + log(1/δ))/n) — leading rate √(p/n). With p=60 vs adapter p=525K, small-data overfitting is structurally suppressed. Interpret as capacity motivation, not guarantee.

## Results

- ChestX-ray14 P@5: **+0.116** over frozen encoder; beats 5.25M-param adapters/LoRA with 60 params (4-5 orders of magnitude fewer)
- MURA P@5: +0.120; margin widest at 512 adaptation examples (+0.040 over retuned adapters)
- Train-test gap: 0.002-0.031 (QuPID) vs 0.041-0.229 (adapters/LoRA) — small budget controls overfitting
- Honest framing: margin over an equally compact classical rotation-plane head is only +0.023 full-budget / +0.007 tuned at 512 (CI includes zero at 512) — the paper explicitly disclaims quantum advantage; the advantage claim is capacity-efficiency, not computational

## Reusable Patterns

### Pattern 1: Degeneracy audit before quantum retrieval design
Before building any fidelity-based quantum retrieval: check whether the same input-independent unitary acts on both sides of the inner product. If yes, the design is untrainable by construction. Fix: make the circuit input-dependent (re-uploading) or compare measurement readouts instead of state overlaps.

### Pattern 2: Measurement-readout similarity
Replace state-fidelity similarity with cosine similarity between vectors of local observable expectations (single-qubit + nearest-neighbor Pauli). This converts an untrainable overlap into trainable structured quadratic feature maps sharing a small parameter vector.

### Pattern 3: Re-uploading as expressivity dial
The re-uploading scale α controls the Fourier bandwidth of the readout. Sweep α to control functional richness without adding parameters.

### Pattern 4: Ultra-compact retrieval adaptation under data-locality constraints
When images can't leave the hospital and adaptation samples are scarce (n≈512): frozen backbone + 60-param input-modulated readout + label-free contrastive objective. Cache archive readouts; query-side only at inference.

## Related Skills

- cqc-rag-cross-query-consistency (RAG reliability)
- superintelligent-retrieval-agent (retrieval reasoning)
- adaptive-quantum-classical-fusion (feature fusion)
