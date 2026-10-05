---
name: encryptability-coordinate-choice-he-fedavg
description: Quaternion chart makes SU(2) updates degree-2 → depth-1 homomorphic FL.
category: ai_collection
trigger_words: homomorphic encryption, federated learning of quantum models, SU(2) weights, quaternion parameterization, encrypted aggregation, bootstrapping elimination, Spin group
---

# Encryptability As a Coordinate Choice: Depth-One Homomorphic FL of QNNs

Methodology from "Encryptability As a Coordinate Choice: Depth-One Homomorphic Federated Learning of Quantum Neural Networks" (arXiv:2609.30581, Sep 2026).

## When to Use
- Encrypted/privacy-preserving federated training where model weights live in a compact Lie group (variational quantum circuits with SU(2) rotations; also any Spin(n)-parameterized layer)
- When homomorphic encryption of "transcendental" updates (Euler angles) costs 25,000+ ops per weight or one client-server round per gate
- Designing HE-friendly model parameterizations generally: the lesson is *encryptability is a property of coordinates, not the model*

## Core Idea
The HE penalty for quantum weights is **strictly an artefact of coordinates**. In the unit-quaternion (spin) chart ℍ₁ ≅ Spin(3), group composition is exactly **bilinear**:

(q ⊗ q′)_i = Σ_{j,k} M^(i)_{jk} q_j q'_k, where M^(i)_{jk} ∈ {−1, 0, +1}

So a rotation U(θ,û) = cos(θ/2)I − i·sin(θ/2)(u_x X + u_y Y + u_z Z) is encoded by q(θ,û) = (cos θ/2, −u_x sin θ/2, −u_y sin θ/2, −u_z sin θ/2), ‖q‖=1.

**Depth ledger** (Proposition 1, any levelled HE scheme):
| Operation | Multiplicative depth |
|---|---|
| Encrypted rotation update Enc(q⊗r) (plaintext r) | 1 (plaintext–ciphertext mult only) |
| Weighted FedAvg q̄ = Σ (n_k/n) q^(k) | 0 (ℝ-linear combination) |
| Renormalisation q̄/‖q̄‖ | 0 (client-side after decryption) |
| Clifford key update (Pauli-OTP) | 0 (XOR) |

A full federated round = **one multiplicative level**; bootstrapping eliminated entirely.

## Protocol Skeleton
1. Clients train locally **in plaintext**, encrypt only resulting angles as unit quaternions
2. Server composes encrypted q with plaintext rotation key via bilinear Hamilton product (depth 1)
3. Server aggregates: weighted mean of K ciphertexts (depth 0)
4. Clients decrypt, renormalise q̄/‖q̄‖ (branch/sign handling in plaintext — costs nothing)
5. Hybrid scheme: Pauli-OTP handles Clifford gates (CNOT, H, S) via XOR; Quaternion-OTP handles continuous rotations R_n(θ) via degree-2 arithmetic; both woven to complete universal circuits

## Generalisation (Corollary 1 — Spin(n))
Spin(n) rotors in the even Clifford subalgebra Cl^[0](n): geometric product is bilinear on 2^(n−1) even-graded coordinates → every statement holds verbatim for Spin(n)-parameterized layers. ℍ₁ ≅ Spin(3) is the case n=3.

## Verified Properties
- Zero utility tax: Δ = +9×10⁻⁶ MSE (p=0.92, paired 5-seed study); encryption noise does NOT regularise (noise-budget ablation falsified the hypothesis)
- Aggregation error: 0.0 and −2.0×10⁻¹² rad across two cryptographic backends
- Scales to 20 clients; independent of dataset and client count
- 156-qubit hardware validation: 0.9918 fidelity vs 0.99957 unencrypted control
- Parameterised entanglers add only constant-factor overhead without altering the depth class (compilation lemma)

## Design Pattern to Reuse
> When a model's parameter space is a compact Lie group G and a downstream constraint demands low-degree arithmetic (HE, secure aggregation, quantized integer pipelines), search for a chart φ: chart-space → G in which the group law is polynomial (bilinear if possible). The double-cover trick (quaternions for SU(2), rotors for SO(n)) is the canonical example. Do heavier corrections (renormalisation, branch/sign resolution) in plaintext outside the encrypted region.
