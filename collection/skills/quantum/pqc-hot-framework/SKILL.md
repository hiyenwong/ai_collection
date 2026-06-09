---
name: "pqc-hot-framework"
description: "PQC-HOT framework for post-quantum cryptography implementation in software systems. Analyzes PQC migration through Human, Organisation, and Technology dimensions. Use when implementing post-quantum cryptography, PQC migration, quantum-safe security transitions, or evaluating PQC implementation readiness. Activation: PQC implementation, post-quantum cryptography, quantum-safe migration, PQC-HOT model, quantum security transition"
---

# PQC-HOT Framework

Post-Quantum Cryptography implementation analysis through the Human-Organisation-Technology (HOT) lens. Based on arXiv:2606.04669 (Shakya et al., 2026).

## Core Insight

PQC implementation is not just a cryptographic replacement — it is a socio-technological transformation requiring coordinated approaches across three interconnected dimensions.

## HOT Dimensions

### Human Dimension
- Developer awareness and training on PQC algorithms
- Security team capability for quantum threat assessment
- Knowledge gaps between cryptographic theory and practical implementation
- Human factors: usability, cognitive load, developer resistance to change

### Organisation Dimension
- Governance and policy for PQC adoption timelines
- Budget allocation and resource planning for migration
- Compliance requirements and regulatory alignment
- Risk management: prioritizing systems by quantum vulnerability
- Vendor management: third-party PQC readiness assessment

### Technology Dimension
- Algorithm selection: NIST-standardized (ML-KEM, ML-DSA, SLH-DSA) + HQC
- Performance benchmarking: latency, throughput, key/ciphertext size
- Compatibility: hybrid mode (classical + PQC) during transition
- Infrastructure: NPU/GPU acceleration (see paper: 18x efficiency on Hexagon NPU)
- Crypto agility: ability to swap algorithms without system redesign

## PQC-HOT Model

```
    ┌──────────┐     ┌──────────┐     ┌──────────┐
    │  Human   │────▶│Organisation│────▶│Technology│
    │          │◀────│          │◀────│          │
    └──────────┘     └──────────┘     └──────────┘
       ▲                                    │
       └────────────────────────────────────┘
```

All three dimensions are interconnected — weakness in any one constrains the others.

## Implementation Workflow

1. **Assess** — Inventory cryptographic assets, map dependencies, identify quantum-vulnerable systems
2. **Prioritize** — Rank by sensitivity, exposure, and migration complexity
3. **Train** — Build PQC competency in development and security teams
4. **Prototype** — Implement hybrid mode in non-critical systems first
5. **Deploy** — Phased rollout with rollback capability
6. **Monitor** — Track algorithm performance, security incidents, and emerging quantum threats

## Key PQC Algorithms (NIST + Additional)

| Algorithm | Type | Standard | Use Case |
|-----------|------|----------|----------|
| ML-KEM (CRYSTALS-Kyber) | KEM | FIPS 203 | Key exchange |
| ML-DSA (CRYSTALS-Dilithium) | Signature | FIPS 204 | Digital signatures |
| SLH-DSA (SPHINCS+) | Signature | FIPS 205 | Stateless signatures |
| HQC | KEM | NIST additional | Code-based KEM diversity |
| FALCON | Signature | Round 4 alt | Compact signatures |

## Activation Keywords

- PQC implementation, post-quantum cryptography, quantum-safe migration
- PQC-HOT model, NIST PQC algorithms, crypto agility
- quantum security transition, cryptographic migration

## References

- arXiv:2606.04669 — "SoK: Post-Quantum Cryptography (PQC) Implementation in Software Systems"
- arXiv:2606.01968 — "HQC Decoding Optimization on NPU-Integrated Devices"
