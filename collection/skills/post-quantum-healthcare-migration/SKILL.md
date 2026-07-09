---
name: "post-quantum-healthcare-migration"
description: "Post-Quantum Cryptography (PQC) migration framework for IoT-based healthcare systems. Provides systematic approach for transitioning healthcare infrastructure from classical to post-quantum cryptographic standards (NIST ML-KEM, ML-DSA) while maintaining HIPAA/GDPR compliance. Activation: post-quantum healthcare, PQC migration IoT healthcare, healthcare cryptography upgrade, medical device PQC, HIPAA quantum security"
metadata:
  arxiv_id: "2604.15584"
  published: "2026-04"
  tags: ["post-quantum", "healthcare", "IoT", "PQC-migration", "HIPAA"]
---

## Context

Healthcare IoT devices (implantable monitors, wearable sensors, hospital networks) face a critical threat from quantum computing's ability to break RSA/ECC. Healthcare systems have unique constraints: long device lifecycles (10-20 years), regulatory compliance (HIPAA, GDPR), and real-time data requirements. PQC migration must be planned now to avoid future breaches.

## Core Methodology

### Step 1: Risk Assessment
1. Inventory all cryptographic dependencies in healthcare infrastructure
2. Classify devices by quantum vulnerability level (critical, high, medium, low)
3. Assess data sensitivity: PHI (Protected Health Information) requires highest protection
4. Map device lifecycle: devices with >5 year remaining life need immediate PQC planning

### Step 2: PQC Algorithm Selection
| Use Case | Recommended Algorithm | NIST Standard |
|----------|----------------------|---------------|
| Key exchange (device-server) | ML-KEM (Kyber) | FIPS 203 |
| Digital signatures (data integrity) | ML-DSA (Dilithium) | FIPS 204 |
| Stateless signatures (firmware) | SLH-DSA (SPHINCS+) | FIPS 205 |

### Step 3: Migration Phases
1. **Phase 1 — Crypto-agility**: Implement hybrid classical+PQC support
2. **Phase 2 — PQC-primary**: Switch to PQC as primary, classical as fallback
3. **Phase 3 — PQC-only**: Remove classical algorithms entirely

### Step 4: Device Constraints Handling
1. Resource-constrained devices: Use optimized PQC implementations (e.g., liboqs)
2. Firmware updates: Sign with SLH-DSA for stateless verification
3. Network protocols: TLS 1.3 with ML-KEM key exchange

## Pitfalls

- **Device firmware size limits**: PQC keys/signatures are larger than RSA/ECC. ML-KEM-768 public key = 1184 bytes vs RSA-2048 = 256 bytes. Verify device storage capacity.
- **Regulatory lag**: HIPAA/GDPR haven't yet mandated PQC. Plan migration ahead of regulatory deadlines.
- **Hybrid mode overhead**: Running both classical and PQC doubles computational cost. Use hardware acceleration where available.
- **Long-lived devices**: Implantable devices cannot be updated easily. Select devices with PQC-ready hardware during procurement.

## Verification

1. All PHI transmission uses ML-KEM key exchange
2. Device firmware integrity verified via ML-DSA signatures
3. No classical-only cryptographic paths remain in production
4. Migration timeline: complete within 3 years (before cryptographically relevant quantum computers)
