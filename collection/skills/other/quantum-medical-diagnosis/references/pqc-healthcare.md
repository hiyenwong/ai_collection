# Post-Quantum Cryptography for Healthcare Systems

## ML-KEM (CRYSTALS-Kyber)
- **Key Encapsulation Mechanism**: NIST FIPS 203 standard
- **Security Levels**: ML-KEM-512 (Level 1), ML-KEM-768 (Level 3), ML-KEM-1024 (Level 5)
- **Key Sizes**: 
  - ML-KEM-768: public key 1184 bytes, ciphertext 1088 bytes, shared secret 32 bytes
  - Latency: ~2-3ms key exchange overhead vs X25519

## ML-DSA (CRYSTALS-Dilithium)
- **Digital Signature**: NIST FIPS 204 standard
- **Security Levels**: ML-DSA-44 (Level 2), ML-DSA-65 (Level 3), ML-DSA-87 (Level 5)
- **Signature Sizes**: ML-DSA-65: ~3300 bytes
- **Verification**: ~1ms per signature

## Migration Strategy
1. **Hybrid Phase**: Run classical (ECDHE/RSA) + PQC (ML-KEM/ML-DSA) simultaneously
2. **Monitor**: Track PQC performance and compatibility with legacy systems
3. **Gradual Cutover**: Deprecate classical algorithms after PQC stability confirmed
4. **Rollback Plan**: Maintain classical fallback during transition

## Regulatory Considerations
- FDA/EMA pharmacovigilance systems require validated cryptographic pipelines
- PQC migration must not alter existing data integrity guarantees
- 21 CFR Part 11 compliance for electronic records and signatures

## Related Papers
- arXiv: 2606.09412 - "Towards Post-Quantum Secure Pharmacovigilance with ML-KEM and ML-DSA"
- arXiv: 2604.15584 - "Framework for Post Quantum Migration in IoT-Based Healthcare Systems"
