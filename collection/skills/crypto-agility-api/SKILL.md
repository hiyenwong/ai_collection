---
name: crypto-agility-api
description: "Intent-Based Cryptographic API Design for Cryptographic Agility — designing APIs that support transparent post-quantum algorithm migration without code rewrites. Use when building cryptographic systems, migrating to post-quantum cryptography, designing intent-based crypto APIs, or implementing policy-driven algorithm selection. Activation: cryptographic agility, post-quantum migration, intent-based API, policy-driven selection, key rotation, cryptographic governance"
metadata:
  arxiv_id: "2606.13445"
  published: "2026-06-11"
  authors: "Navaneeth Rameshan, Gregoire Messmer"
  tags: ["cryptography", "post-quantum", "api-design", "software-engineering", "information-science", "security"]
---

# Intent-Based Cryptographic API Design for Cryptographic Agility

Design cryptographic APIs that enable transparent migration to post-quantum algorithms without rewriting application code.

## Problem

Current crypto APIs (PKCS#11, OpenSSL 3.0, JCA, Google Tink, AWS KMS, HashiVault) tie applications to specific algorithms. Post-quantum transition requires rewriting code because APIs lack:
- Intent-based key creation (decoupled from algorithm identity)
- Policy-driven algorithm selection (distinct from access control)
- First-class key evolution operations (rotation, transformation, migration)

## Five Design Principles

1. **Abstraction**: Decouple key creation from algorithm identities via intent vocabulary
2. **Stability**: Stable key identifiers that persist across algorithm changes
3. **Temporal Flexibility**: Support transparent algorithm substitution within scoped contexts
4. **Separation**: Separate governance policy from implementation
5. **Extensibility**: Enable future algorithm additions without API changes

## Implementation Patterns

### Intent-Based Key Creation
- Keys created with intent (scope, purpose) not algorithm name
- Policy layer maps intent to current algorithm
- Enable transparent substitution by updating policy, not code

### Key Evolution Operations
- **Rotation**: Generate new key material under same identifier
- **Transformation**: Convert existing key to different algorithm
- **Migration**: Move keys between providers while tracking evolution history

### Governance via Abstract Policy API
- Policy format not prescribed by the API
- Scope-based intent vocabulary enables decoupled algorithm selection
- Track original key identity + full evolution history

## Seven Assessment Dimensions

When evaluating cryptographic agility, measure along these dimensions:

1. **Creation Decoupling**: What application code knows about algorithm at key creation
2. **Operation Decoupling**: What code knows during cryptographic operations
3. **Storage Decoupling**: What code knows about stored key format
4. **Cross-Cutting Decoupling**: Central mechanism enabling decoupling across system
5. **Governance Authority**: Who/what controls algorithm selection policy
6. **Algorithm Substitution Enabler**: Actual capability to swap algorithms
7. **Key Migration Enabler**: Actual capability to migrate existing keys

## Pitfalls

- No existing major crypto API supports all three gaps identified in assessment
- Algorithm selection ≠ access control — they address different concerns
- Key transformation is distinct from key rotation (transformation changes algorithm)

## Verification

- After API design, evaluate against all 7 dimensions independently
- Ensure policy updates do not require application code changes
- Verify key evolution history tracks both original identity and transformations
