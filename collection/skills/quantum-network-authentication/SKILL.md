---
name: quantum-network-authentication
description: "Authentication in Quantum Networks — comprehensive survey of classical, quantum, and entity authentication for quantum communication. Covers security guarantees, composability, QKD integration, and hardware-assisted approaches. Use when: quantum network security, QKD authentication, quantum cryptography protocols, quantum network infrastructure, quantum message authentication, entity authentication, quantum-secure authentication schemes, 量子网络认证, 量子密钥分发认证."
metadata:
  arxiv_id: "2606.30636"
  published: "2026-06-29"
  authors: "Christopher Battarbee, Suchetana Goswami, Elham Kashefi, Mina Doosti"
---

# Quantum Network Authentication

## Description

Comprehensive framework for understanding and implementing authentication in quantum networks. Classifies authentication into three distinct flavours (classical message, quantum message, entity), provides security/composability analysis, and guides protocol selection for quantum network infrastructure.

## Activation Keywords
- quantum network authentication
- quantum message authentication
- entity authentication quantum
- QKD authentication
- quantum-secure authentication
- quantum cryptography protocols
- quantum network security
- 量子网络认证
- 量子密钥分发认证
- 量子消息认证

## Core Concepts

### Three Flavours of Authentication

1. **Classical Message Authentication**: Authenticating classical control/data messages in quantum networks. Uses MACs, digital signatures. Prerequisite for most quantum protocols.

2. **Quantum Message Authentication**: Authenticating quantum states themselves. Ensures quantum data integrity against adversarial modification. Schemes include Barnum-Crepeau-Gottesman (BCG), Barnum et al. authentication codes.

3. **Entity Authentication**: Verifying the identity of communicating parties in quantum networks. Hardware-assisted approaches leverage quantum properties for identity verification.

### Key Evaluation Criteria

| Criterion | Description |
|-----------|-------------|
| **Security assumptions** | Computational vs information-theoretic, trust in setup |
| **Set-up requirements** | Pre-shared keys, trusted third parties, quantum memory |
| **Composability** | Security preserved under composition with other protocols |
| **Scalability** | Performance in large/dynamic quantum networks |

### Core Insight

> An authentication requirement is not an intrinsic limitation of quantum networks. Each protocol relies on a particular authentication resource, and the security claim is meaningful only once the authentication resource and its deployment assumptions are made explicit.

## Usage Patterns

### Pattern 1: QKD Protocol Selection
When deploying QKD, select authentication based on:
- Network topology (point-to-point vs multi-party)
- Available infrastructure (pre-shared keys, PKI)
- Security requirements (information-theoretic vs computational)
- Scalability needs

### Pattern 2: Quantum Network Design
For quantum network architecture:
1. Identify authentication flavour needed per protocol layer
2. Match authentication scheme to security/composability requirements
3. Explicitly document authentication resource assumptions
4. Verify composability when chaining protocols

### Pattern 3: Hardware-Assisted Authentication
When quantum hardware is available:
- Leverage quantum properties for entity authentication
- Consider device-independent approaches
- Account for hardware imperfections in security proofs

## Methodology

### Step 1: Identify Authentication Requirements
- What type of data needs authentication? (classical, quantum, or both)
- What security level is required? (computational, information-theoretic)
- What are the deployment constraints? (pre-shared keys, PKI, quantum memory)

### Step 2: Select Authentication Protocol
- For classical messages: MACs with information-theoretic security, or post-quantum digital signatures
- For quantum messages: Quantum authentication codes (QACs) with error detection
- For entity: Quantum identification protocols, hardware-assisted approaches

### Step 3: Verify Composability
- Check protocol security under composition
- Ensure authentication resource assumptions are consistent across protocol stack
- Document all implicit authentication dependencies

### Step 4: Deploy and Monitor
- Implement with explicit authentication resource tracking
- Monitor for authentication failures
- Plan for key refresh and authentication resource management

## Pitfalls

- **Conflating authentication flavours**: Classical, quantum, and entity authentication are fundamentally different and require different analysis. Do not assume a solution for one applies to another.
- **Implicit authentication assumptions**: Many quantum protocol security claims implicitly assume authenticated classical channels. Make these assumptions explicit.
- **Scalability overlooked**: Point-to-point authentication schemes may not scale to large quantum networks. Consider composability and key management overhead.
- **Hardware assumptions**: Hardware-assisted approaches require specific quantum capabilities. Verify that assumptions match available infrastructure.

## Resources
- arXiv: 2606.30636 — "Authentication in Quantum Networks" (Battarbee et al., 2026)
