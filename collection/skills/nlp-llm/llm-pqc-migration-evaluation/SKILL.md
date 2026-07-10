---
name: llm-pqc-migration-evaluation
description: "Framework for evaluating and training LLMs to assist in migrating pre-quantum cryptographic code to post-quantum counterparts. Systematic assessment methodology measuring code correctness, security preservation, and functional equivalence during PQC migration. Use when evaluating LLMs for cryptographic code migration, designing PQC training datasets, or building automated crypto migration tools."
metadata:
  arxiv_id: "2606.07341"
  published: "2026-06-05"
  authors: "Javier Pallarés de Bonrostro, Ana I. González-Tablas, María Isabel González Vasco"
---

# LLM PQC Migration Evaluation

Framework for systematically evaluating whether LLMs can assist in migrating pre-quantum cryptographic code to post-quantum cryptographic implementations. Measures code correctness, security preservation, and functional equivalence.

## Core Problem

PQC transition requires:
1. Replacing vulnerable cryptographic primitives (RSA, ECC → ML-KEM, ML-DSA, etc.)
2. Refactoring surrounding software logic (key sizes, error handling, API changes)
3. Preserving functional equivalence and security properties

Existing PQC migration frameworks provide organizational guidance, but code-level remediation remains manual and error-prone.

## Evaluation Framework

### Dimension 1: Code Correctness
- Does the migrated code compile?
- Are type signatures consistent with the new PQC API?
- Are memory management patterns correct (key allocation, buffer sizes)?

### Dimension 2: Security Preservation
- Are key generation parameters correct (security levels, parameter sets)?
- Are side-channel mitigations preserved or improved?
- Does the migrated code maintain equivalent security guarantees?

### Dimension 3: Functional Equivalence
- Does the migrated code produce correct outputs for known inputs?
- Are edge cases handled equivalently?
- Is the API contract preserved for callers?

## Assessment Methodology

### Step 1: Dataset Construction
- Collect pre-quantum cryptographic code fragments (RSA, ECDSA, DH, etc.)
- Annotate with correct PQC migrations (reference implementations)
- Categorize by complexity: primitive replacement, protocol-level, system-level

### Step 2: LLM Evaluation Protocol
- Prompt LLM with pre-quantum code + migration instructions
- Collect migrated code output
- Evaluate against three dimensions above
- Measure success rate per complexity category

### Step 3: Error Analysis
- Classify failures: syntax errors, semantic errors, security vulnerabilities
- Identify patterns: which PQC primitives are hardest to migrate?
- Determine if fine-tuning improves specific failure modes

## PQC Migration Patterns

| Pre-Quantum | Post-Quantum | Key Changes |
|-------------|-------------|-------------|
| RSA-2048 | ML-KEM-768 | Key size: 256B → 1184B (encapsulated) |
| ECDSA-P256 | ML-DSA-44 | Signature size: 64B → 2420B |
| ECDH-P256 | ML-KEM-768 | Key exchange → KEM encapsulation |
| AES-256-GCM | AES-256-GCM | No change (symmetric, quantum-safe with 256-bit) |
| SHA-256 | SHA-384/SHA-512 | Hash output size increase |

## Activation Keywords
- LLM PQC migration
- post-quantum code migration
- cryptographic code migration
- LLM cryptography evaluation
- PQC refactoring
- quantum-safe code migration
- post-quantum LLM
- 大语言模型后量子密码迁移
- PQC 代码迁移

## Related Skills
- `post-quantum-cryptographic-protocol-analysis` — PQC protocol analysis
- `pqc-tls-deployment` — PQC TLS deployment methodology
- `magiq-post-quantum-agent-governance` — Multi-agent AI governance with post-quantum security

## References
- arXiv:2606.07341 — "Empirical Evaluation of Large Language Models for Migration of Code Fragments to Post-Quantum Cryptography" (Pallarés de Bonrostro et al., 2026)
