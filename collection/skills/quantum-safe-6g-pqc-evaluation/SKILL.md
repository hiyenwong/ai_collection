---
name: quantum-safe-6g-pqc-evaluation
description: "Practical evaluation methodology for deploying NIST-standardized Post-Quantum Cryptography (PQC) in bandwidth and latency-constrained wireless systems (6G, IoT, edge). Covers ML-KEM/Kyber, ML-DSA/Dilithium, and Falcon benchmarking, size expansion impact analysis, and deployment-aware design patterns. Activation: quantum-safe 6G, post-quantum cryptography evaluation, PQC deployment, NIST PQC benchmarking, quantum-secure networks."
category: information-science
tags: ["quantum", "security", "networks", "6G", "PQC", "cryptography", "NIST"]
related_skills: ["post-quantum-cryptographic-protocol-analysis", "quantum-resistant-networks", "pqc-tls-deployment"]
source_paper: "arXiv:2605.06881"
---

# Quantum-Safe 6G PQC Evaluation

Practical evaluation methodology for deploying NIST-standardized Post-Quantum Cryptography (PQC) algorithms in bandwidth and latency-constrained wireless systems, particularly 6G networks, edge nodes, and resource-constrained IoT devices.

## Source

**Paper**: "Toward Quantum-Safe 6G: Experimental Evaluation of Post-Quantum Cryptography Techniques"
**Authors**: Ananya Kudaloor, Adnan Aijaz
**arXiv**: [2605.06881](https://arxiv.org/abs/2605.06881) (May 2026)
**Journal**: Accepted for publication in IEEE Communications Standards Magazine
**Category**: cs.NI (Networking and Internet Architecture)

## Core Findings

6G networks require quantum-secure cryptography deployed across three tiers:
1. **Core infrastructure** - high-capacity backbone
2. **Edge nodes** - moderate capacity, higher latency sensitivity
3. **Resource-constrained IoT devices** - severely limited compute/bandwidth

### PQC Algorithms Evaluated

Three NIST-standardized schemes benchmarked with OpenSSL + OQS provider:

| Algorithm | Type | Key Insight |
|-----------|------|-------------|
| **ML-KEM (Kyber)** | KEM (Key Encapsulation) | Computational overhead acceptable; ciphertext size expansion significant |
| **ML-DSA (Dilithium)** | Digital Signature | Signature size impacts handshake efficiency at network edge |
| **Falcon** | Digital Signature | Smaller signatures than Dilithium but different performance trade-offs |

### Critical Trade-off: Size vs. Computation

**Key finding**: Computational performance is acceptable across all platforms, but **ciphertext and signature size expansion** significantly impacts:
- **Handshake reliability** — larger TLS handshakes fail more often on lossy/low-bandwidth links
- **Bandwidth efficiency** — PQC key/sig sizes are 3-10x larger than classical equivalents
- **Edge deployment** — particularly problematic for IoT devices with MTU constraints

### Benchmark Methodology

```bash
# Benchmark setup (OpenSSL + liboqs provider)
# Run on heterogeneous platforms:
# 1. x86 server (core infrastructure simulation)
# 2. ARM edge device (edge node simulation)
# 3. Cortex-M microcontroller (IoT device simulation)

# ML-KEM key generation + encapsulation/decapsulation timing
openssl speed -evp ML-KEM-768

# ML-DSA signing + verification timing
openssl speed -evp ML-DSA-65

# Falcon signing + verification timing
openssl speed -evp Falcon-512
```

**Measure these metrics**:
- Key generation latency (ms)
- Encapsulation/decapsulation latency (ms)
- Signing/verification latency (ms)
- Ciphertext size (bytes) vs. classical ECDH
- Signature size (bytes) vs. classical ECDSA
- Handshake completion rate on lossy channels

## Deployment Patterns

### Pattern 1: Hybrid Handshake (Recommended for 6G Core)

Use classical + PQC in parallel during migration:
```
TLS 1.3 + X25519 + ML-KEM-768 hybrid key exchange
```
- Maintains classical security as fallback
- PQC provides quantum-safe layer
- Size overhead is acceptable at core tier

### Pattern 2: Size-Optimized Selection (Edge/IoT)

For bandwidth-constrained edge nodes:
- Prefer **Falcon** over ML-DSA (smaller signatures: ~897 bytes vs. ~2,420 bytes)
- Use **ML-KEM-512** (smallest KEM) over ML-KEM-768/1024 when security margins allow
- Implement **connection pooling** to amortize handshake costs

### Pattern 3: Asynchronous PQC Handshake

For IoT with intermittent connectivity:
- Pre-provision PQC keys during manufacturing/registration
- Use **key caching** to reduce handshake frequency
- Implement **resumption sessions** to avoid full PQC handshake on each reconnect

## System-Level Trade-offs

| Factor | Impact | Mitigation |
|--------|--------|------------|
| Ciphertext expansion (ML-KEM-768: ~1184 bytes) | Increased bandwidth consumption, MTU fragmentation | Compression, packet aggregation |
| Signature expansion (ML-DSA-65: ~2420 bytes) | Handshake timeout on lossy links | Prefer Falcon, reduce MTU |
| Key generation time (~0.1-1ms) | Negligible for most applications | None needed |
| Encapsulation time (~0.05-0.5ms) | Negligible for most applications | None needed |

## Pitfalls

- **MTU fragmentation**: PQC key exchange packets may exceed standard 1500-byte MTU, causing IP fragmentation which increases loss probability
- **Handshake timeout**: Larger TLS handshakes take longer on lossy wireless links, increasing timeout rate
- **Memory constraints**: IoT devices with <64KB RAM may struggle with PQC key storage
- **NIST standard updates**: ML-KEM/ML-DSA parameters may be updated — verify against latest FIPS publications
- **Side-channel vulnerability**: Software implementations may leak timing information — use constant-time implementations

## Activation

Use this skill when:
- Designing quantum-secure network protocols or 6G security architecture
- Evaluating PQC algorithms for deployment in bandwidth-constrained environments
- Benchmarking post-quantum cryptography performance on heterogeneous platforms
- Planning migration from classical to quantum-safe cryptographic infrastructure
- Assessing the trade-offs between PQC algorithm size and network performance
