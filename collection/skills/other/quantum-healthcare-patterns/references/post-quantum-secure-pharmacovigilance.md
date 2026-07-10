# Post-Quantum Secure Pharmacovigilance Pipeline

**Paper**: Towards Post-Quantum Secure Pharmacovigilance with ML-KEM and ML-DSA
**arXiv**: 2606.09412
**Authors**: Saee Desai, Tom Shimoni, Eddie Cameron, David Akamine, Aniketh Chunduri
**Date**: 2026-06-08
**Category**: cs.CR (Cryptography and Security)

## Summary

Educational prototype demonstrating integration of NIST-standardized post-quantum cryptographic (PQC) primitives into healthcare data pipelines for pharmacovigilance systems.

## Architecture

```
Hospital (Encrypt + Sign) → Gateway (Route) → Pharma Receiver (Decrypt + Verify)
```

### Cryptographic Stack

| Layer | Primitive | Purpose |
|-------|-----------|---------|
| Key Establishment | ML-KEM-768 (CRYSTALS-Kyber) | Post-quantum key exchange |
| Key Derivation | HKDF-SHA-256 | Derive AES key from shared secret |
| Encryption | AES-256-GCM | Efficient authenticated encryption |
| Signing | ML-DSA-65 (CRYSTALS-Dilithium) | Digital signatures, tamper detection |

### Performance

- ML-KEM key exchange: small constant overhead (~independent of file size)
- AES-256-GCM encryption: linear scaling, dominates for large files
- ML-DSA-65 signing: linear scaling, dominates for large files
- Supported formats: TXT, CSV, JSON, PDF (raw bytes, metadata preserved)

## Healthcare Relevance

- Pharmacovigilance: adverse event reporting, drug safety monitoring
- Long-term confidentiality: healthcare data must remain secret for decades
- "Harvest now, decrypt later": quantum computers may retroactively break current encryption
- Regulatory: HIPAA, GDPR require strong encryption

## Key Insight

PQC migration for healthcare is **feasible today** — the quantum key exchange overhead is negligible, and the symmetric components (AES, signing) are already efficient. The main bottleneck is integration complexity, not performance.

## Activation

post-quantum cryptography, pharmacovigilance, ML-KEM, ML-DSA, healthcare security, AES-256-GCM, HKDF, key encapsulation, digital signatures, adverse event reporting, clinical data, tamper detection, NIST PQC, CRYSTALS-Kyber, CRYSTALS-Dilithium
