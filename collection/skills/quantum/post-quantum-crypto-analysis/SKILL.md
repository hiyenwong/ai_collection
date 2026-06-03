---
name: post-quantum-crypto-analysis
description: >
  Analyze and evaluate post-quantum cryptography (PQC) implementations, security trade-offs,
  and deployment strategies for IoT, blockchain, and network systems. Covers lattice-based
  cryptography (FALCON, Kyber, Dilithium), hash-based signatures, NIST PQC standards,
  quantum-resistant protocol design, and performance benchmarking on resource-constrained devices.
  Use when: evaluating PQC algorithms, deploying quantum-resistant security, analyzing
  PQC overhead on IoT/edge devices, comparing signature schemes, designing quantum-safe
  network protocols, or assessing blockchain PQC migration costs.
  Trigger keywords: post-quantum cryptography, PQC, quantum-resistant, quantum-safe,
  FALCON signature, lattice-based crypto, NIST PQC, Kyber, Dilithium, quantum attack,
  Shor's algorithm vulnerability, IoT security quantum, blockchain quantum migration,
  后量子密码, 抗量子密码.
---

# Post-Quantum Cryptography Analysis

## Overview

Analyze PQC algorithm selection, security guarantees, and deployment trade-offs
for quantum-resistant systems. Covers lattice-based, hash-based, code-based, and
isogeny-based cryptographic schemes.

## PQC Algorithm Families

### Lattice-Based (NIST Selected)

| Algorithm | Type | Key Strength | Notes |
|-----------|------|-------------|-------|
| **ML-KEM (Kyber)** | KEM | IND-CCA2 | Primary NIST KEM selection |
| **ML-DSA (Dilithium)** | Signature | EUF-CMA | Primary NIST signature |
| **SLH-DSA (SPHINCS+)** | Signature | EUF-CMA | Stateless hash-based backup |
| **FALCON** | Signature | EUF-CMA | Compact signatures, FFT-based |

### Hash-Based

- **XMSS**: Stateful, proven security, RFC 8391
- **SPHINCS+**: Stateless, larger signatures, NIST selected
- **LMS**: Stateless, NIST standard (RFC 8554)

### Key Trade-offs

- **Signature size**: FALCON (~1KB) << Dilithium (~2.5KB) << SPHINCS+ (~8-50KB)
- **Verification speed**: Dilithium > FALCON >> SPHINCS+
- **Security basis**: Lattice worst-case hardness vs. hash collision resistance

## IoT/Edge Deployment Analysis

### Resource Constraints

When deploying PQC on constrained devices (Raspberry Pi, microcontrollers):

1. **Memory**: FALCON signing requires ~64KB RAM; SPHINCS+ needs ~100KB
2. **Computation**: Lattice ops (NTT/FFT) dominate; hash-based is CPU-heavy
3. **Bandwidth**: Signature size impacts MQTT packet overhead significantly
4. **Power**: PQC signing can consume 5-50x more energy than ECDSA

### Performance Benchmarking Pattern

```python
import time
import statistics

def benchmark_pqc(algorithm, n_iterations=100):
    """Benchmark PQC algorithm performance metrics."""
    times = {'keygen': [], 'sign': [], 'verify': []}
    
    for _ in range(n_iterations):
        t0 = time.perf_counter()
        pk, sk = algorithm.keygen()
        times['keygen'].append(time.perf_counter() - t0)
        
        t0 = time.perf_counter()
        sig = algorithm.sign(sk, message)
        times['sign'].append(time.perf_counter() - t0)
        
        t0 = time.perf_counter()
        algorithm.verify(pk, message, sig)
        times['verify'].append(time.perf_counter() - t0)
    
    return {k: {'mean': statistics.mean(v), 'p95': sorted(v)[95]} 
            for k, v in times.items()}
```

## Security Analysis Framework

### Threat Model Assessment

1. **Harvest-now-decrypt-later**: Data captured today, decrypted when quantum computers arrive
2. **Protocol downgrade attacks**: Mixed classical/PQC deployments vulnerable to stripping
3. **Side-channel resistance**: Many PQC implementations leak through timing/power
4. **Implementation complexity**: PQC algorithms are harder to implement correctly than ECC

### Security Guarantees

| Level | Classical | Quantum (Grover) | Quantum (Shor) |
|-------|-----------|------------------|----------------|
| AES-128 | 2^128 | 2^64 | N/A |
| AES-256 | 2^256 | 2^128 | N/A |
| SHA-256 | 2^128 | 2^128 | N/A |
| RSA-2048 | 2^112 | 2^56 | **~2^30** |
| ML-KEM-768 | 2^236 | 2^118 | **Secure** |

## Deployment Patterns

### MQTT + PQC (IoT)

For IoT message brokers using MQTT:

- Integrate FALCON or Dilithium signatures for message authenticity
- Measure MQTT packet overhead: signature size + protocol headers
- Consider batch verification for high-throughput brokers
- Use hybrid signatures (ECDSA + PQC) during transition

### Blockchain PQC Migration

Key considerations:

- **Transaction size blowup**: 10-100x signature increase affects block capacity
- **Verification cost**: Full nodes must verify all PQC signatures
- **Migration strategy**: Hybrid signatures, then PQC-only after quantum readiness
- **Commit-reveal**: Hash-based alternatives minimize infrastructure overhead

### Protocol Layer Integration

```
Application Layer:  PQC signatures (FALCON/Dilithium)
Transport Layer:    Hybrid TLS 1.3 (X25519 + ML-KEM)
Network Layer:      IPSec with PQC transforms
Link Layer:         No changes needed
```

## Error Handling

### Common Issues

- **FALCON signing failure**: Rare (~10^-5 rate), retry with fresh randomness
- **Memory exhaustion**: On constrained devices, prefer hash-based (lower RAM)
- **Large packet sizes**: With SPHINCS+, fragment MQTT messages or use compression
- **Timing attacks**: Use constant-time implementations; verify with timing analysis

## Best Practices

1. **Start with hybrid**: Deploy classical + PQC simultaneously during transition
2. **Benchmark on target hardware**: Performance varies dramatically by platform
3. **Monitor quantum progress**: Adjust PQC parameters as quantum capabilities grow
4. **Use NIST-standardized algorithms**: Avoid proprietary or unvetted schemes
5. **Plan key rotation**: PQC key sizes require updates to key management infrastructure

## Related Skills

- quantum-systems-engineering: Quantum system design patterns
- quantum-computing-patterns: Reusable quantum computing research patterns
- cross-layer-crypto-analysis: Cross-layer security analysis
