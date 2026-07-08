---
name: routing-anonymity-quantum-cloud
category: quantum-security
description: Formal framework for backend identifiability and routing anonymity in quantum cloud services with utility-anonymity trade-offs.
trigger_words: ["routing anonymity", "quantum cloud", "backend identifiability", "quantum fingerprint", "utility-anonymity", "Pauli-transfer-matrix", "Chernoff rate"]
---

# Routing Anonymity for Quantum Cloud Services

Methodology from arXiv:2607.05281 (Priestley & Doosti, Jul 2026).

## Problem

Cloud-based quantum computing lets users submit circuits to proprietary backends. Noisy finite-shot outputs carry backend-specific fingerprints that can reveal which physical device was used. Providers may want to hide implementation details, but this creates privacy risks.

## Solution: Formal Routing Anonymity Framework

### Core Concepts

1. **Backend-Identifiability Game**: Formalizes routing anonymity as a security notion for quantum cloud services
2. **Hypothesis Testing Formulation**: Backend identifiability is cast as a statistical hypothesis testing problem
3. **Chernoff Rate Decay**: Under passive i.i.d. access, routing anonymity decays exponentially at the Chernoff rate
4. **Utility-Anonymity Trade-off**: Fundamental limits on removing backend-specific info without degrading usefulness
5. **Depth Principle**: Identifying fingerprints are inherently intermediate-depth phenomena (Pauli-transfer-matrix analysis)

### Experimental Findings

- 87-90% classification accuracy between superconducting backends on AWS Braket
- 96-100% classification accuracy across physical platforms (ion-trap vs superconducting)
- Identifiability survives natural forms of post-processing
- Fingerprints are intermediate-depth phenomena (not shallow or deep circuit regimes)

### Application

Use when:
- Designing quantum cloud service architectures
- Evaluating backend privacy guarantees
- Analyzing utility-anonymity trade-offs in quantum computing
- Auditing quantum hardware fingerprinting risks
- Implementing quantum circuit routing with privacy guarantees

### Security Framework

```
User Circuit → Backend Execution → Noisy Output →
  [Fingerprint Analysis] → Backend Identity (if identifiable)
  
Anonymity = P(adversary fails to identify backend)
Decays as: exp(-n * Chernoff_rate) where n = number of shots
```

### Depth Principle

Shallow circuits: noise dominates, no fingerprint
Intermediate circuits: fingerprint emerges (optimal for identification)
Deep circuits: noise washes out, fingerprint fades
