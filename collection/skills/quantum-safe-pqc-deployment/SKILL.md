---
name: quantum-safe-pqc-deployment
description: "Post-quantum cryptography (PQC) production deployment methodology. Hybrid-by-default architecture bridging classical and post-quantum security for production systems. Covers ML-KEM/ML-DSA migration, TLS integration, and incremental deployment strategies."
metadata:
  arxiv_id: "2605.17061"
  published: "2026-05-15"
---

# Quantum-Safe PQC Deployment

## Core Concepts

Bridging the gap between PQC standardization and production deployment requires hybrid-by-default architectures that support both classical and post-quantum cryptography simultaneously. This enables incremental migration without breaking existing systems.

## Methodology

### Hybrid-by-Default Architecture

1. Dual-stack TLS: Support both classical (ECDHE) and PQC (ML-KEM) key exchange simultaneously
2. Signature chaining: Use both classical (ECDSA) and PQC (ML-DSA) signatures
3. Fallback mechanisms: Graceful degradation when PQC is not supported by peers

### Deployment Strategy

1. **Inventory**: Catalog all cryptographic dependencies in production systems
2. **Prioritize**: Focus on long-lived secrets and high-value assets first
3. **Test**: Validate PQC compatibility in staging environments
4. **Deploy**: Roll out hybrid mode with monitoring
5. **Transition**: Phase out classical algorithms as PQC adoption matures

## Activation Keywords
- post-quantum cryptography deployment
- PQC production
- quantum-safe architecture
- ML-KEM ML-DSA migration
- hybrid TLS
- 后量子密码部署

## Pitfalls

- PQC key sizes are significantly larger (ML-KEM-768: ~1KB vs ECDHE ~32 bytes)
- ML-DSA signatures are ~2.5KB vs ECDSA ~64 bytes - impacts bandwidth
- Not all libraries support hybrid mode natively
- Performance overhead from dual computation
