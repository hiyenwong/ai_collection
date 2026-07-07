---
name: non-isometric-qec-theory
description: "General theory of non-isometric quantum error-correcting codes using approximate QEC framework. Quantifies fundamental limitations imposed by non-isometric encodings on QEC accuracy and logical operation implementation. Applied to GKP and tiger codes under energy constraints, with implications for holography. (arXiv: 2606.13559)"
category: quantum-error-correction
metadata:
  arxiv_id: "2606.13559"
  authors: "Yixu Wang, Yijia Xu, Zi-Wen Liu"
  submitted_date: "2026-06-11"
  subjects: "quant-ph"
---

## Context

Non-isometric encoding arises in critical contexts: (1) finite-energy, non-ideal codewords in experimental continuous-variable codes (GKP, tiger codes), (2) holographic quantum gravity (AdS/CFT bulk-boundary maps). Existing QEC theory assumes isometric encodings — this paper develops a general theory for the non-isometric case.

## Core Methodology

### Non-Isometric Encoding Model

An encoding map E: H_L → H_P is non-isometric when E†E ≠ I_L. This means:
- Logical states are not perfectly normalized after encoding
- Different logical states may have different norms
- The encoding is not invertible on the full logical space

### Approximate QEC Framework

1. **Recovery Condition**: A channel R recovers the logical state with fidelity ≥ 1-ε iff the Knill-Laflamme condition is approximately satisfied:
   PE†E_j E_k EP ≈ c_jk P where P = EE† (projector onto code space)

2. **Error Measure**: Use diamond norm ||R∘N∘E - id||_⋄ to quantify QEC accuracy

3. **Non-Isometric Correction**: The deviation from isometry δ = ||E†E - I|| introduces a fundamental lower bound on achievable QEC accuracy:
   ε ≥ f(δ, noise strength) — even with optimal recovery

### Application to GKP Codes

- GKP codewords have finite energy → E†E ≈ I - ε_E where ε_E ~ exp(-Δ²)
- Logical operation implementation accuracy degrades as O(ε_E + noise)
- Trade-off: higher energy → better isometry → better QEC but more susceptible to certain noise

### Application to Tiger Codes

- Tiger codes use non-orthogonal codewords → inherently non-isometric
- Error correction accuracy depends on overlap between codewords
- Optimal recovery requires knowledge of the non-isometry structure

## Implementation Steps

1. **Characterize Non-Isometry**: Compute E†E, find its eigenvalue spectrum λ_i
2. **Bound QEC Accuracy**: Use ε ≥ max_i |1 - λ_i| as fundamental limit
3. **Design Recovery**: Optimize R to minimize ||R∘N∘E - id||_⋄ given the non-isometry
4. **Logical Operations**: Implement logical gates U_L via U_P on physical space; accuracy bound: ||U_P E - E U_L|| ≤ O(δ)
5. **Energy-Error Trade-off**: For CV codes, optimize energy budget vs. QEC accuracy

## Pitfalls

- **Assuming isometry**: Standard QEC theorems (Knill-Laflamme, Eastin-Knill) assume exact isometry — applying them to non-isometric codes gives incorrect bounds
- **Ignoring energy constraints**: GKP codes with finite energy are ALWAYS non-isometric; ignoring this overestimates QEC performance
- **Holographic implications**: In AdS/CFT, non-isometric bulk-boundary maps mean boundary recovery is inherently approximate — this affects quantum gravity interpretations
- **Tiger code normalization**: Non-orthogonal tiger codewords require careful normalization to avoid biasing the logical basis

## Verification

1. Verify E†E eigenvalue spectrum for GKP codewords with finite squeezing Δ
2. Confirm QEC accuracy bound ε ≥ ||E†E - I|| matches numerical simulation
3. Verify logical gate implementation accuracy degrades as O(δ)
4. Cross-check with holographic code models (HaPPY, random tensor networks)

## Activation

non-isometric quantum error correction, approximate QEC, GKP codes, tiger codes, continuous-variable QEC, holographic codes, quantum error correction theory, energy-constrained QEC, logical operation accuracy