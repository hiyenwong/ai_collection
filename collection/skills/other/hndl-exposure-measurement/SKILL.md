---
name: hndl-exposure-measurement
description: >
  Formal framework for measuring quantum cryptographic exposure under Harvest-Now-Decrypt-Later (HNDL) threats.
  Models adversary copying encrypted traffic today to decrypt with future quantum computers.
  Uses multiplicative factorization of temporal hazard, cryptographic vulnerability, operational exposure,
  and defense-attack saturation — proving additive scoring frameworks are structurally inadequate.
  Use when: assessing post-quantum cryptographic risk, designing quantum-safe security architectures,
  evaluating HNDL threat exposure, comparing cryptographic scoring frameworks, or performing
  quantum-era threat modeling for enterprise systems.
  Activation: HNDL, harvest now decrypt later, quantum cryptographic exposure, post-quantum risk,
  cryptographic vulnerability scoring, quantum threat assessment, defense-attack intensity ratio,
  quantum security prioritization.
---

# HNDL Exposure Measurement Framework

Methodology from arXiv:2605.22569 — "A Formal Basis for Quantum Cryptographic Exposure Measurement under HNDL Threat" (Rufino, Marcelino, Garcia, 2026).

## Core Insight

The HNDL compromise probability has a **specific multiplicative structure** justified by three
assumptions about adversarial production and value-decay dynamics:

```
P_compromise = Temporal_Hazard × (Crypto_Vulnerability × Operational_Exposure) / (1 + Defense/Attack_Ratio)
```

This is **not** a calibration choice — it is the unique functional form satisfying the assumptions.

## Why Additive Scoring Fails

Additive frameworks (e.g., CVSS-style scoring) **cannot** reproduce this structure because the
interaction between cryptographic vulnerability and operational exposure is absent by construction,
regardless of calibration. The multiplicative coupling is essential.

## Three Structural Assumptions

1. **Adversarial Production**: Attacker's ability to decrypt scales with accumulated encrypted data
2. **Value Decay**: Information value decays over time (compromised data becomes less valuable)
3. **Defense-Attack Dynamics**: Defense intensity vs. attack intensity determines saturation

## Key Properties

### Marginal Sensitivity is Endogenous
- Sensitivity to each dimension depends on the organization's position in the vulnerability-exposure plane
- NOT a fixed global constant (contrary to most scoring frameworks)

### Saturation Behavior
- Defense-attack intensity ratio governs a saturation denominator
- Beyond a certain defense level, additional investment has diminishing returns
- The ratio determines the operating regime, not absolute values

## When to Apply

- Prioritizing which systems to migrate to post-quantum cryptography first
- Quantifying organizational exposure to quantum computing threats
- Designing cryptographic risk assessment frameworks
- Justifying security investment allocation under partial observability
- Evaluating whether current additive scoring frameworks adequately capture HNDL risk

## Limitations

- Framework assumes partial observability — exact adversary capabilities unknown
- Requires estimation of temporal hazard rates and value-decay functions
- Defense-attack intensity ratio may be difficult to quantify in practice