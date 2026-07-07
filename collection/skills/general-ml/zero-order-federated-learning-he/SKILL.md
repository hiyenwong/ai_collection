---
name: zero-order-federated-learning-he
description: "Privacy-enhanced zero-order federated learning using multi-key homomorphic encryption (xMK-CKKS) over wireless channels. Methodology for secure FL aggregation without channel estimation, supporting N-1 client compromise tolerance. Use when designing privacy-preserving federated learning, multi-key HE protocols, or wireless FL systems."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.30123"
  published: "2026-05-28"
  authors: "Anthony Ayli, Khalil Harris, Jihad Fahs, Mohamad Assaad"
  tags: [federated-learning, homomorphic-encryption, xmk-ckks, privacy, wireless-ml, zero-order]
---

# Zero-Order Federated Learning with Multi-Key HE

## Overview

Privacy-preserving federated learning protocol combining zero-order FL (one encrypted scalar per device per round) with multi-key homomorphic encryption (xMK-CKKS) over wireless channels — **without channel estimation or pre-equalization**.

## Core Architecture

### Protocol Design (Four-Phase)

1. **Partial Public Key Retransmission**: Devices transmit partial public keys through the same channel realization
2. **Ciphertext Retransmission**: Partial ciphertexts retransmitted through same channel
3. **Algebraic Cancellation**: Dominant large-modulus encryption terms cancel during decryption (same channel → same fading)
4. **Aggregation**: Server aggregates encrypted scalars, decryption noise preserves O(1/√K) convergence rate

### Key Innovation

- **No channel estimation required**: Same-channel retransmission enables algebraic cancellation of fading terms
- **Client-level security**: Each device has its own secret key (multi-key HE vs single-key)
- **Compromise tolerance**: Secure against honest-but-curious server colluding with up to N-1 clients
- **Communication efficiency**: Overhead independent of model dimension (one scalar per round)

### Convergence Analysis

Decoded encryption noise preserves O(1/√K) convergence rate up to negligible noise floor, validated on MNIST with slowly varying LoS-dominant channels.

## When to Use

- Privacy-preserving FL with untrusted clients
- Wireless FL with channel fading (LoS-dominant, slowly varying)
- Scenarios where single-key HE is insufficient (multi-party trust)
- Bandwidth-constrained FL (zero-order scalar transmission)

## Pitfalls

- Requires slowly varying channel (retransmission assumes same channel realization)
- LoS-dominant channels work best; rich scattering may break cancellation
- Multi-key HE has higher computation overhead than single-key

---

*Reference: Ayli et al. (2026) "Privacy-Enhanced Zero-Order Federated Learning via xMK-CKKS over Wireless Channels" arXiv:2605.30123*
