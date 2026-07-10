---
name: uncloneable-encryption-microcrypt
description: "Uncloneable encryption methodology in microcrypt — boosting one-time secure uncloneable bits to many-time secure multi-bit uncloneable encryption. Reduces assumptions for existence of uncloneable indistinguishability in symmetric key encryption. Use when analyzing quantum encryption schemes, designing ciphertext cloning prevention protocols, or formalizing uncloneable indistinguishability in quantum cryptography. arXiv: 2605.27647"
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.27647"
  published: "2026-05-26"
  authors: "James Bartusek, Eli Goldin"
  tags: [quantum, cryptography, uncloneable, encryption, microcrypt, security]
---

# Uncloneable Encryption in Microcrypt

## Core Concept

**Key insight**: A one-time secure "uncloneable bit" (information-theoretic uncloneable encryption for single-bit messages) can be boosted to many-time secure uncloneable encryption for arbitrary-length messages. This minimizes the cryptographic assumptions needed for uncloneable encryption existence.

## Definitions

### Uncloneable Indistinguishability

A symmetric key encryption scheme satisfies **uncloneable indistinguishability** if it prevents cloning of ciphertexts in a strong sense: an adversary receiving a ciphertext cannot produce two shares such that both can independently decrypt the message.

### Uncloneable Bit

An information-theoretic **uncloneable bit**: a one-time secure uncloneable encryption scheme for one-bit messages.

## Boosting Framework

### t → t′ Reduction

If a t → t′ uncloneable bit exists (adversary can clone at most t out of t′ copies), then:
1. Construct m-bit encryption from m independent uncloneable bits
2. Security degrades gracefully with message length
3. Many-time security achieved via careful key management

### Construction Steps

1. Start with uncloneable bit primitive
2. Apply parallel composition for multi-bit messages
3. Use key refresh for many-time security
4. Prove uncloneable indistinguishability via hybrid argument

## Security Parameters

| Parameter | Meaning |
|-----------|---------|
| t → t′ | Adversary cloning bound |
| m | Message length in bits |
| ε | Security parameter (advantage bound) |

## Error Handling

### Assumption Minimization
The framework's strength lies in minimal assumptions. When evaluating a scheme, check if the uncloneable bit assumption is truly necessary or can be further weakened.

### Cloning Attacks
Analyze adversary's quantum memory capacity — uncloneability degrades if adversary has unlimited quantum storage.

## Related Methodologies

- Post-quantum cryptography deployment (see `operationalising-post-quantum-tls`)
- Quantum key distribution networks
- Microcrypt primitives analysis
