---
name: hybrid-pqc-pseudonym-vehicular-security
description: "Hybrid certificate methodology combining ECC with Post-Quantum Cryptography (PQC) for vehicular communication security. Covers SCMS pseudonym schemes, BKE compatibility, NIST-standardized PQC algorithms, and performance evaluation of RSA/ECC/PQC for vehicular credential management. Activation: vehicular security PQC, SCMS hybrid certificate, pseudonym scheme quantum-safe, BKE post-quantum, vehicular communication security, NIST PQC vehicular, 车载通信后量子密码, 混合证书车联安全"
metadata:
  arxiv_id: "2606.14008"
  published: "2026-06-12"
  authors: "Abel C. H. Chen, F. J. Hwang, Yu-Chih Wei, Chin-Chen Chang, Bon-Yeh Lin"
  tags: [quantum, PQC, vehicular-security, SCMS, pseudonym, hybrid-certificate, NIST]
---

# Hybrid PQC Pseudonym for Vehicular Security

## Description

Hybrid certificate methodology combining ECC with NIST-standardized Post-Quantum Cryptography (PQC) algorithms for vehicular communication security credential management systems (SCMS). Addresses quantum vulnerability of existing IEEE/ETSI standards while maintaining performance compatibility.

## Activation Keywords
- vehicular security PQC
- SCMS hybrid certificate
- pseudonym scheme quantum-safe
- BKE post-quantum
- vehicular communication security
- NIST PQC vehicular
- 车载通信后量子密码
- 混合证书车联安全
- Butterfly Key Expansion PQC
- ETSI quantum-safe

## Core Methodology

### Problem
IEEE and ETSI vehicular security standards (SCMS, BKE) rely on ECC (secp256k1, etc.), which is vulnerable to Shor's algorithm on quantum computers.

### Solution: Hybrid Certificate Architecture

1. **Dual-layer certificates**: Combine ECC + PQC in a single certificate
2. **Generalized pseudonym scheme**: Compatible with various cryptographic algorithms
3. **Privacy preservation**: Prevents correlation between pseudonym and enrollment certificate public keys

### NIST PQC Algorithms Evaluated
- ML-KEM (CRYSTALS-Kyber) - Key encapsulation
- ML-DSA (CRYSTALS-Dilithium) - Digital signatures
- SLH-DSA (SPHINCS+) - Stateless hash-based signatures
- FN-DSA (FALCON) - Lattice-based signatures

### Performance Evaluation Metrics
| Factor | RSA | ECC | PQC (ML-DSA) |
|--------|-----|-----|-------------|
| Message length | Moderate | Small | Large |
| Computation time | Slow | Fast | Moderate |
| Quantum resistance | No | No | Yes |

## Usage Patterns

### Pattern 1: Design Hybrid Certificate
For vehicular SCMS migration to PQC:
1. Select NIST-standardized PQC algorithm (ML-DSA recommended for signatures)
2. Combine with existing ECC for backward compatibility
3. Implement dual-signature verification
4. Evaluate message size and computation overhead

### Pattern 2: Pseudonym Certificate Generation
For privacy-preserving vehicular authentication:
1. Generate pseudonym using generalized scheme
2. Ensure no correlation with enrollment certificate
3. Use hybrid signature (ECC + PQC) for each pseudonym
4. Validate against IEEE/ETSI compatibility requirements

### Pattern 3: Performance Benchmarking
When evaluating PQC for vehicular deployment:
1. Measure message length impact on V2X bandwidth
2. Benchmark computation time on vehicular hardware
3. Compare RSA/ECC/PQC for signing and verification
4. Assess migration path and backward compatibility

## Instructions for Agents

### Step 1: Identify Vehicular Security Requirements
- Current cryptographic standard (IEEE 1609.2, ETSI TS 103 097)
- Performance constraints (bandwidth, computation, storage)
- Migration timeline and backward compatibility needs

### Step 2: Select PQC Algorithm
- ML-DSA (Dilithium): Recommended for vehicular signatures
- SLH-DSA (SPHINCS+): Stateless alternative
- Evaluate message size vs computation tradeoff

### Step 3: Design Hybrid Certificate
- Combine ECC + PQC signatures
- Implement dual verification path
- Maintain BKE compatibility where possible

### Step 4: Implement Pseudonym Scheme
- Generalized scheme compatible with multiple algorithms
- Prevent enrollment-pseudonym key correlation
- Validate against privacy requirements

### Step 5: Performance Evaluation
- Benchmark on target vehicular hardware
- Measure impact on V2X message latency
- Evaluate storage requirements for certificate chains

## Error Handling
### Message Size Overflow
If PQC signatures exceed V2X message size limits:
- Use ML-DSA with smaller parameter sets
- Implement signature compression
- Evaluate tradeoff between security level and size

### Backward Compatibility Failure
If hybrid certificates break existing SCMS:
- Implement gradual migration path
- Support ECC-only fallback during transition
- Use certificate versioning for algorithm negotiation

## References
- arXiv: 2606.14008v1
- IEEE 1609.2 - Wireless Access in Vehicular Environments
- ETSI TS 103 097 - Intelligent Transport Systems Security
- NIST PQC Standards: ML-KEM, ML-DSA, SLH-DSA
