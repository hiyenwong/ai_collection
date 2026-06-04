---
name: squeezed-state-quantum-randomness-generation
description: "Closed-form Shannon-rate methodology for semi-device-independent quantum randomness generation using squeezed-coherent BPSK sources. Derives analytical bounds on certified randomness rates accounting for detector side information. Applicable to quantum key distribution, medical data security, and cryptographic systems. Activation: quantum randomness generation, squeezed state QRNG, semi-device-independent, BPSK quantum, certified randomness, Shannon rate quantum"
category: "medicine"
arxiv_id: "2606.03898"
---

## Squeezed-State Semi-Device-Independent Quantum Randomness Generation

### Core Problem

Quantum randomness generation (QRG) requires certifying that outputs are truly random even when devices are partially untrusted. Existing projective-only treatments overestimate certified rates by ignoring deterministic extreme points in binary-qubit POVM optimization.

### Key Innovation

**Closed-form Shannon-rate expression** for semi-device-independent QRG that:
- Depends only on trusted Gram overlap of two source states + observed symmetric error probability
- Includes the two deterministic extreme points omitted by projective-only treatments
- Gives substantially lower but **correct** certified rates

### Technical Framework

#### 1. Semi-Device-Independent Model
- **Trusted**: Binary pure-state source (two prepared quantum states)
- **Untrusted**: Binary detector (can have arbitrary classical side information)
- **Adversary**: May hold detector-purification register that tags outcomes

#### 2. Closed-Form Rate Expression
```
R ≤ f(γ, ε)
where:
  γ = Gram overlap = |⟨ψ₀|ψ₁⟩|²  (trusted parameter)
  ε = symmetric error probability  (observed)
```
- Unconditional upper bound on certified asymptotic i.i.d. Shannon rate
- Tight on numerically verified dual-feasibility region
- Remains upper bound outside this region

#### 3. Full Binary-Qubit POVM Optimization
- Projective-only treatment misses two deterministic extreme points
- Including them: **corrects overestimation** of certified randomness
- Critical for practical security guarantees

#### 4. Squeezed-Coherent BPSK Application
- Squeezing changes trade-off between state distinguishability and certified randomness
- Lossless regime: squeezing enhances distinguishability but may reduce certified rate
- Lossy regime: optimal squeezing level depends on channel transmissivity

### Reusable Patterns

#### Pattern 1: Security Rate Computation
```
Input: source states |ψ₀⟩, |ψ₁⟩, observed error rate ε
1. Compute Gram overlap: γ = |⟨ψ₀|ψ₁⟩|²
2. Check dual-feasibility region
3. Apply closed-form rate: R = f(γ, ε)
4. If outside region → rate is upper bound (conservative)
```

#### Pattern 2: Squeezing Optimization
- Trade-off: squeezing ↑ → distinguishability ↑ but certified rate may ↓
- Optimal squeezing depends on: channel loss, detector noise, security requirements
- Numerical verification needed for tight rate outside dual-feasibility region

### Pitfalls

- **Projective-only treatment overestimates rates**: Always include deterministic extreme points in POVM optimization
- **Dual-feasibility region**: Closed form is only tight within verified region; outside it's a conservative upper bound
- **Adversary model clarity**: Specify whether adversary holds detector-purification register — this changes security analysis

### Applications to Medical/Healthcare Security

1. **Medical Device Security**: Certified random number generation for implantable devices
2. **Healthcare Data Encryption**: QRNG for securing patient records and genomic data
3. **Clinical Trial Randomization**: Provably random assignment using quantum sources
4. **Biomedical Sensor Security**: Squeezed-state sources compatible with optical fiber infrastructure

### References

- arXiv: 2606.03898
- Author: Hamid Tebyanian
- Category: quant-ph
- 11 pages, 6 figures
