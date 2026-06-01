---
name: zeroth-order-federated-learning-he
description: "Privacy-enhanced zero-order federated learning using xMK-CKKS homomorphic encryption. Combines zeroth-order optimization (gradient-free) with modified CKKS encryption for privacy-preserving distributed training. Use when: (1) Federated learning with strict privacy requirements, (2) Gradient-free distributed optimization needed (non-differentiable models), (3) Homomorphic encryption for secure aggregation, (4) Wireless communication channels with privacy constraints."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "crossref:10.1017/9781009504942.004,2605.30123"
  published: "2026-05-30"
  tags: [federated-learning, zeroth-order, homomorphic-encryption, ckks, privacy, distributed-optimization]
---

# Zeroth-Order Federated Learning with Homomorphic Encryption

## Overview

Combines two privacy-preserving techniques:
1. **Zeroth-order optimization**: Uses only function evaluations (loss values) rather than gradients, avoiding gradient leakage
2. **xMK-CKKS encryption**: Modified Multi-Key CKKS scheme for secure aggregation over wireless channels

## Core Concepts

### Zeroth-Order Optimization in FL

Instead of transmitting gradients (which can leak training data), clients:
- Sample random perturbation directions z ~ N(0, I)
- Evaluate loss at θ + δz and θ - δz
- Estimate gradient as: g ≈ (f(θ+δz) - f(θ-δz)) / (2δ) · z
- Only transmit encrypted function evaluations or perturbation results

### xMK-CKKS Encryption

Modified CKKS scheme supporting:
- **Multi-key operations**: Each client uses different encryption keys
- **Secure aggregation**: Server computes encrypted average without decryption
- **Approximate arithmetic**: CKKS supports floating-point operations on ciphertexts
- **Wireless compatibility**: Designed for noisy wireless channel transmission

### Privacy Advantages

| Aspect | Standard FL | Z0-FL + HE |
|--------|------------|------------|
| Gradient leakage | Yes | No (no gradients computed) |
| Server sees updates | Plaintext | Encrypted |
| Cross-client inference | Possible | Prevented |
| Channel security | Requires TLS | Inherent (encrypted) |

## Methodology

### Step 1: Setup
- Distribute xMK-CKKS key material to all clients
- Define perturbation dimension d and step size δ
- Set number of random directions per client (tradeoff: accuracy vs. communication)

### Step 2: Client Computation (per round)
1. Receive encrypted global model parameters θ
2. For each random direction z_i:
   - Compute local loss f(θ + δz_i) and f(θ - δz_i)
   - Compute directional estimate g_i = (f⁺ - f⁻)/(2δ) · z_i
3. Average estimates: g = (1/k) Σ g_i
4. Encrypt update: enc(θ - α·g) using xMK-CKKS
5. Transmit encrypted update to server

### Step 3: Server Aggregation
1. Receive encrypted updates from all clients
2. Compute encrypted average using CKKS homomorphic addition + scalar multiplication
3. Decrypt aggregated model (requires threshold decryption from clients)
4. Broadcast updated model

### Step 4: Convergence
- Zeroth-order methods converge slower than gradient-based (O(d/ε²) vs O(1/ε²))
- Compensate with more iterations or larger perturbation sets
- Monitor loss curve for convergence

## Pitfalls

- **Dimension curse**: ZO gradient estimation error scales with model dimension d. For large models, use structured random directions (Hadamard, Johnson-Lindenstrauss) to reduce variance.
- **CKKS precision loss**: CKKS is approximate — accumulated rounding errors can corrupt training after many rounds. Periodically refresh ciphertexts or use bootstrapping.
- **Multi-key overhead**: xMK-CKKS key management is complex. Each client pair needs shared key material for secure aggregation. For N clients, this is O(N²) key pairs.
- **Wireless channel noise**: CKKS ciphertexts are sensitive to noise. Add error correction or retransmission protocols for unreliable wireless links.
- **Communication cost**: ZO methods require more iterations. Balance privacy benefits against total training time.

## Activation Keywords
- zeroth-order federated learning
- federated learning homomorphic encryption
- ckks federated learning
- gradient-free federated learning
- privacy-preserving distributed training
- wireless federated learning encryption
- 零阶联邦学习
- 同态加密联邦学习
