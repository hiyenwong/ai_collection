---
name: equation-asymmetry-information-security
description: "Equation Asymmetry Degree (EAD) framework for unifying secrecy and covertness in information-theoretic security. EAD = 1 - r/n governs both equivocation and detection error probability. Applies to MIMO wiretap, secure network coding, FRFT multi-angle transmission, traffic steganography, post-quantum security. Use when analyzing information-theoretic security, secrecy capacity, covertness, or designing secure communication protocols."
metadata:
  arxiv_id: "2606.10374"
  published: "2026-06-09"
  authors: "Wang Hao, Zhang Kuang"
  tags: [information-theory, security, secrecy, covertness, equation-asymmetry, post-quantum]
---

## Equation Asymmetry Degree (EAD) Framework

### Core Concept

The Equation Asymmetry Degree **EAD = Φ = 1 - r/n** where:
- **n** = signal embedding dimension
- **r** = effective rank of adversary's observation matrix

This single parameter simultaneously governs:
1. **Secrecy** — measured by equivocation H(X|Y)
2. **Covertness** — measured by detection error probability P_e

### Key Theorems

**Theorem 1 (Finite Fields)**: Equivocation lower bound H(X|Y) ≥ Φ·log|F| with exact probabilistic conditions on F_q.

**Theorem 2 (Secrecy Capacity)**: Complete achievability and converse proofs for secrecy capacity C_s in terms of Φ.

**Theorem 5' (Continuous Gaussian)**: High-SNR secrecy capacity asymptotics + 2-Wasserstein distance covertness condition W_2 ≤ ε·Φ.

**Theorem 6 (Monotonicity)**: Both secrecy capacity and detection error probability are monotone functions of Φ (Pearson correlation 0.997 in experiments).

**Theorem 7 (EAD-SDoF Equivalence)**: Φ = SDoF/n where SDoF is the secure degrees of freedom.

**Theorem 8 (Strong Converse)**: Strong converse theorem for secrecy capacity on finite fields.

**Theorem 9 (Post-Quantum Security)**: Post-quantum security follows from information-theoretic hardness of underdetermined linear systems (Ax = b where A is m×n with m < n).

### Unified Form

Seven existing security schemes unified under common form y = Ax + e:
1. Matrix embedding
2. MIMO wiretap channels
3. Secure network coding
4. FRFT multi-angle transmission
5. Traffic steganography
6. Group-key secure summation
7. MDS secure summation

### Usage Patterns

**Pattern 1: Security Scheme Analysis**
Given a security protocol → compute EAD = 1 - r/n → bound equivocation and covertness → compare with other schemes on same Φ scale.

**Pattern 2: Post-Quantum Assessment**
Evaluate whether a scheme's security reduces to underdetermined linear system solving → if yes, Theorem 9 applies → information-theoretic post-quantum security guaranteed.

**Pattern 3: Design Optimization**
Maximize Φ = 1 - r/n by increasing embedding dimension n or reducing adversary's effective rank r through signal design.

### Activation Keywords
- equation asymmetry
- EAD framework
- information-theoretic security
- secrecy capacity
- covertness
- secure network coding
- MIMO wiretap
- post-quantum security linear system
- 方程不对称度
- 信息论安全
- 保密容量
