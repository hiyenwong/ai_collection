---
name: quantum-crypto-agility
description: Intent-based cryptographic API design for post-quantum cryptography (PQC) migration — cryptographic agility patterns for large software portfolios.
trigger_words:
  - cryptographic agility
  - post-quantum cryptography migration
  - intent-based crypto API
  - PQC API design
  - crypto migration
---

# Intent-Based Cryptographic API Design for PQC Migration

Methodology from arXiv:2606.13445 for designing cryptographic APIs that support cryptographic agility during post-quantum cryptography (PQC) migration.

## Problem

Most cryptographic APIs are designed around specific algorithms (RSA, ECC, AES). Migrating to PQC (ML-KEM, ML-DSA, SLH-DSA) requires:
- Rewiring explicit algorithm references across large codebases
- Testing each integration point
- Managing hybrid (classical + PQC) transition periods

## Intent-Based API Pattern

### Core Design Principle

Instead of: `crypto.encrypt("RSA-OAEP", plaintext, key)`
Use: `crypto.encrypt({intent: "confidentiality", security_level: 5}, plaintext)`

### API Structure

```
CryptoService
├── encrypt(intent: CryptoIntent, data: bytes) → bytes
├── decrypt(intent: CryptoIntent, ciphertext: bytes) → bytes
├── sign(intent: CryptoIntent, data: bytes) → bytes
├── verify(intent: CryptoIntent, data: bytes, signature: bytes) → bool
└── derive(intent: CryptoIntent, input: bytes) → bytes

CryptoIntent {
    purpose: "confidentiality" | "integrity" | "authentication" | "non-repudiation"
    security_level: 1 | 2 | 3 | 4 | 5  // NIST PQC levels
    performance_tier: "low_latency" | "balanced" | "high_throughput"
    compliance: ["fips140-3", "pqc-ready"]
}
```

### Implementation Steps

1. **Define Intent Taxonomy**: Map security requirements to intent objects
2. **Build Algorithm Registry**: Map intents to concrete algorithms with fallbacks
3. **Implement Policy Engine**: Select algorithms based on intent + policy
4. **Add Migration Layer**: Gradually swap classical → PQC in registry
5. **Audit Trail**: Log which algorithm was used for each operation

### Algorithm Registry Pattern

```yaml
registry:
  confidentiality:
    level_1: [ML-KEM-512, X25519]      # hybrid
    level_3: [ML-KEM-768, X448]        # hybrid
    level_5: [ML-KEM-1024]             # pure PQC
  integrity:
    level_1: [ML-DSA-44, Ed25519]
    level_3: [ML-DSA-65, Ed448]
    level_5: [ML-DSA-87]
```

### Migration Strategy

1. **Phase 1**: Intent layer + classical algorithms (no code changes in consumers)
2. **Phase 2**: Add PQC algorithms to registry as options
3. **Phase 3**: Enable hybrid mode (classical + PQC)
4. **Phase 4**: Switch default to PQC-only
5. **Phase 5**: Remove classical algorithms from registry

## Pitfalls

- **Intent ambiguity**: Vague intents lead to wrong algorithm selection
- **Performance regression**: PQC can be slower; need performance_tier
- **Key size growth**: PQC keys are larger; consider storage/network limits
- **Compliance gaps**: Not all PQC algorithms are FIPS-approved yet
- **Side channels**: PQC implementations may have different side-channel profiles

## References

- arXiv:2606.13445 - "Intent-Based Cryptographic API Design for Cryptographic Agility"
- NIST PQC Standardization: ML-KEM (FIPS 203), ML-DSA (FIPS 204), SLH-DSA (FIPS 205)
