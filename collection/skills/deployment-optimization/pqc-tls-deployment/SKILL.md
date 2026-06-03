---
name: pqc-tls-deployment
description: "Post-quantum cryptography TLS deployment methodology. Automated configuration parsing and hybrid PQC (ML-KEM/ML-DSA) deployment patterns for enterprise infrastructure. Use when: deploying post-quantum cryptography, migrating TLS to PQC standards, auditing cryptographic configurations, implementing hybrid key exchanges (MLKEM + X25519), managing crypto-agility in enterprise web server stacks (Nginx, Apache, API gateways), performing cryptographic inventory and exposure assessment, or planning quantum-safe migration roadmaps."
---

# PQC TLS Deployment Methodology

Automated Post-Quantum Cryptography (PQC) deployment methodology from arXiv:2605.17955. Addresses the operational gap between PQC algorithm standardization (FIPS 203/204/205) and production deployment in enterprise environments.

## Core Problem

The **production gap** in PQC: algorithms are standardized, but hybrid combiners, versioned key formats, protocol helpers, and migration tooling remain fragmented. Security teams lack visibility into TLS configurations and repeatable methods for enabling PQC-compatible settings.

## Configuration Parsing Methodology

### Step 1: Automated TLS Configuration Extraction

Parse and normalize TLS cryptographic posture across enterprise web server stacks:
- **Nginx**: Extract `ssl_ciphers`, `ssl_protocols`, `ssl_prefer_server_ciphers` directives
- **Apache**: Extract `SSLCipherSuite`, `SSLProtocol`, `SSLOpenSSLConfCmd` directives
- **API Gateways**: Parse Kong, Envoy, HAProxy TLS termination configurations
- **Load Balancers**: Extract cryptographic posture from F5, AWS ALB/NLB configs

### Step 2: Cryptographic Inventory Generation

Produce a unified, provenance-traced cryptographic inventory:
```
{
  "endpoint": "api.example.com",
  "server_type": "nginx",
  "tls_version": "1.3",
  "kex_algorithms": ["x25519", "mlkem768_x25519"],
  "signature_algorithms": ["ML-DSA-65", "Ed25519"],
  "cipher_suites": ["TLS_AES_256_GCM_SHA384"],
  "pqc_ready": true,
  "provenance": "/etc/nginx/sites-enabled/api.conf:42"
}
```

### Step 3: Hybrid Key Exchange Deployment

Deploy hybrid key exchanges at TLS termination points:
- **ML-KEM (FIPS 203)**: Hybrid with X25519 for backward compatibility
- **ML-DSA (FIPS 204)**: Hybrid with Ed25519 for signatures
- **SLH-DSA (FIPS 205)**: Stateless hash-based signatures for long-term security

### Performance Considerations

- ML-KEM hybrid adds ~5-15ms latency per handshake
- Key sizes: ML-KEM-768 ciphertext ~1088 bytes (vs X25519 ~32 bytes)
- Zero application-layer changes required when deployed at termination points

## Migration Strategy

### Phase 1: Discovery (weeks 1-4)
- Run configuration parsing across all TLS endpoints
- Generate cryptographic inventory and exposure register
- Prioritize based on asset criticality and confidentiality longevity

### Phase 2: Pilot (weeks 5-8)
- Deploy hybrid ML-KEM on non-critical endpoints
- Monitor handshake latency, error rates, compatibility
- Validate with quantum-safe test clients

### Phase 3: Production (weeks 9-16)
- Roll out to critical infrastructure
- Implement monitoring and alerting for PQC-specific metrics
- Establish crypto-agility procedures for algorithm updates

## Security Analysis Patterns

### Side-Channel Resistance
Post-quantum cryptosystems (McEliece, BIKE) are vulnerable to Simple Power Analysis (SPA) during decapsulation. Key findings:
- EM emissions correlate with secret values during key generation
- 200 power traces sufficient for ML-based key bit prediction
- **Mitigation**: Constant-time implementations, EM shielding, randomized decapsulation

### Harvest-Now-Decrypt-Later
Data with confidentiality requirements >10 years must be prioritized for PQC migration. Exposure register should track:
- Asset criticality
- Data confidentiality longevity
- Third-party dependency timelines

## Activation Keywords
- post-quantum cryptography deployment
- PQC TLS migration
- ML-KEM hybrid deployment
- cryptographic inventory
- quantum-safe infrastructure
- FIPS 203 204 205
- crypto-agility
- harvest-now-decrypt-later
