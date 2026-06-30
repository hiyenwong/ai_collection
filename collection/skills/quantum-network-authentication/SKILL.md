---
name: quantum-network-authentication
description: "Quantum network authentication patterns - survey of classical message authentication, quantum message authentication, and entity authentication protocols for quantum networks. Covers security assumptions, setup requirements, composability, and scalability. Use when: designing quantum network security, QKD authentication, quantum communication protocols, quantum cryptography infrastructure. Activation: quantum authentication, quantum network security, QKD authentication, quantum message authentication, entity authentication quantum, quantum cryptographic protocols."
---

## Overview

This survey (arXiv:2606.30636) provides a comprehensive analysis of authentication in quantum communication networks, covering three main flavours that are often conflated in the literature.

## Three Authentication Flavours

### 1. Classical Message Authentication
- Standard MAC (Message Authentication Code) protocols
- Pre-shared symmetric keys required
- Security: computational or information-theoretic

### 2. Quantum Message Authentication
- Protects quantum states from tampering
- Requires shared entanglement or secret keys
- Security: quantum information-theoretic

### 3. Entity Authentication
- Verifies identity of communicating parties
- Can be classical or quantum protocols
- Often hardware-assisted (PUF, quantum signatures)

## Key Criteria for Protocol Selection

- **Security assumptions**: computational vs information-theoretic
- **Setup requirements**: pre-shared keys, entanglement, hardware
- **Composability**: how protocols combine securely
- **Scalability**: performance in large/dynamic networks

## Practical Steps

1. Identify required authentication flavour for your use case
2. Evaluate security assumptions against threat model
3. Check setup requirements against available infrastructure
4. Verify composable security for multi-protocol scenarios
5. Assess scalability for network size and dynamics

## QKD Integration Case Study

- Authentication is prerequisite for QKD security
- Initial authentication must use pre-shared key
- QKD can then generate fresh authentication keys
- Bootstrapping: small initial key → large authenticated key pool

## Pitfalls

- Don't conflate the three authentication flavours
- Authentication requirement is NOT intrinsic limitation
- Each protocol relies on particular authentication resource
- Security claims only meaningful when authentication resource made explicit
- Hardware-assisted approaches may have different trust assumptions