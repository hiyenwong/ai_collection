---
name: post-quantum-network-security
description: "Analysis and design of post-quantum cryptographic network architectures for protecting against harvest-now-decrypt-later threats. Covers transparent proxy architectures, KEM-based encryption, and quantum-resilient key establishment patterns."
---

# Post-Quantum Network Security

## Description
Methodology for designing and analyzing post-quantum cryptographic (PQC) network architectures that protect against the harvest-now-decrypt-later (HNDL) threat. Covers transparent proxy patterns for quantum-resilient key establishment, KEM-based integrated encryption schemes, and migration strategies from classical to post-quantum cryptography.

## Activation Keywords
- post-quantum cryptography
- PQC
- HNDL
- harvest now decrypt later
- quantum resilient
- quantum-resistant network
- KEM
- key encapsulation mechanism
- ECIES replacement
- 后量子密码
- 抗量子网络
- 量子安全

## Key Concepts

### 1. Harvest-Now-Decrypt-Later (HNDL) Threat
- Adversaries intercept and archive ciphertext today for retrospective decryption once quantum computers mature
- Affects all public-key primitives (RSA, Diffie-Hellman, ECC)
- Turns future quantum threat into present liability
- **Action**: Audit all long-lived encrypted communications; prioritize migration of long-validity secrets

### 2. Transparent Proxy Architecture (Aquaman Pattern)
- Intercept session-key requests at network edge
- Replace vulnerable key exchanges with PQC alternatives
- Deploy incrementally without endpoint changes
- Benefits:
  - No client/server modifications required
  - Can deploy at load balancers, API gateways, or edge routers
  - Supports hybrid (classical + PQC) mode during transition

### 3. KEM-Based Integrated Encryption (KEM-IES)
- Replaces ECIES with post-quantum Key Encapsulation Mechanism
- Structure: PQC-KEM key agreement + symmetric encryption
- Standards: NIST PQC candidates (Kyber/ML-KEM, Dilithium/ML-DSA, SPHINCS+)
- Integration path:
  1. Identify ECIES usage in protocol stack
  2. Select appropriate PQC-KEM (security level, key size)
  3. Wrap symmetric layer with KEM-IES
  4. Test hybrid mode before full migration

### 4. Post-Quantum Signature Tradeoffs
| Scheme | Type | Signature Size | Key Size | Best For |
|--------|------|---------------|----------|----------|
| ML-DSA (Dilithium) | Lattice | ~2-3 KB | ~1-2 KB | General purpose |
| SPHINCS+ | Hash-based | ~8-50 KB | ~32-64 KB | Conservative security |
| Falcon | Lattice | ~0.7-1 KB | ~1 KB | Bandwidth-constrained |

## Implementation Patterns

### Pattern 1: Quantum-Resilient Session Key Establishment
```
Client → [Classical Key Exchange] → Proxy → [PQC Key Exchange] → Server
                ↓                            ↑
        Intercept at edge           Upgrade with PQC-KEM
        No client changes           Server gets quantum-resilient session key
```

### Pattern 2: Hybrid Cryptographic Migration
```
Phase 1: Deploy PQC alongside classical (dual encapsulation)
Phase 2: Monitor PQC interoperability and performance
Phase 3: Phase out classical algorithms
Phase 4: Full PQC deployment
```

### Pattern 3: KEM-IES Protocol Integration
```python
# Conceptual structure
def kem_ies_encrypt(public_key, message):
    # 1. KEM encapsulation (post-quantum)
    ciphertext, shared_secret = kem_encapsulate(public_key)
    
    # 2. KDF on shared secret
    aes_key = kdf(shared_secret, info=b"KEM-IES")
    
    # 3. Symmetric encryption (e.g., AES-GCM)
    encrypted_msg = aes_gcm_encrypt(aes_key, message)
    
    return ciphertext, encrypted_msg
```

## Security Assessment Checklist
- [ ] Identify all long-lived encrypted data (certificates, stored messages, backups)
- [ ] Audit cryptographic algorithms in use (RSA, ECDSA, ECDH, etc.)
- [ ] Assess HNDL exposure for each data class
- [ ] Select appropriate PQC algorithms (NIST standards or candidates)
- [ ] Plan hybrid deployment (classical + PQC)
- [ ] Consider bandwidth/storage impact of larger PQC keys and signatures
- [ ] Test interoperability with existing infrastructure
- [ ] Document migration timeline and rollback procedures

## Common Pitfalls
- **Underestimating PQC key sizes**: Lattice-based signatures are 2-100x larger than ECDSA
- **Ignoring state management**: Hash-based schemes (SPHINCS+) are stateless but large
- **Forgetting about blockchain**: Post-quantum signatures in blockchain multiply overhead across all nodes
- **Transition timing**: Don't wait for quantum computers to start HNDL protection
- **Performance testing**: PQC operations may have different latency profiles than classical

## Related Topics
- NIST PQC standardization (ML-KEM/Kyber, ML-DSA/Dilithium, SLH-DSA/SPHINCS+)
- Quantum key distribution (QKD)
- Cryptographic agility
- TLS 1.3 post-quantum extensions
- Blockchain post-quantum migration

## Resources
- NIST Post-Quantum Cryptography Standardization: https://csrc.nist.gov/projects/post-quantum-cryptography
- arXiv: 2605.06932 (Aquaman transparent proxy architecture)
- arXiv: 2605.10175 (KEM-IES integrated encryption scheme)

## Notes
- The HNDL threat means quantum resistance should be implemented NOW, not when quantum computers arrive
- Transparent proxy architectures provide the lowest-friction migration path
- Hybrid mode (classical + PQC) provides defense-in-depth during transition
