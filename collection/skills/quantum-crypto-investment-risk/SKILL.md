---
name: quantum-crypto-investment-risk
category: finance
description: Quantum computing risk assessment framework for cryptocurrency investments - Monte-Carlo forecasting of quantum threat timelines, exposure analysis, and post-quantum migration pathways
version: "1.0.0"
created: "2026-06-27"
source_paper: "arXiv:2606.14484"
---

# Quantum Crypto Investment Risk Assessment

## Overview

Framework for assessing quantum computing threats to cryptocurrency investments using the "Quantum Horizon" methodology from arXiv:2606.14484 (Gershteyn & Alber, 2026). Separates Shor's algorithm threats (signature breaking) from Grover's algorithm threats (mining), provides probabilistic timelines, and maps exposure/migration pathways.

## Core Methodology

### 1. Threat Separation

- **Shor's Algorithm**: Breaks elliptic-curve signatures (ECDSA over secp256k1, BLS over BLS12-381) that authorize spending
- **Grover's Algorithm**: Does NOT meaningfully threaten proof-of-work mining due to:
  - Quadratic speedup only (not exponential)
  - Fault-tolerant per-operation costs
  - Square-root parallelization wall
  - Difficulty adjustment mechanisms

### 2. Monte-Carlo Timeline Forecasting

Combine four factors into bimodal arrival distribution for cryptographically relevant quantum computer (CRQC):
- Hardware scaling trajectories
- Falling resource requirements
- Fault-tolerance readiness lag
- Expert survey aggregation

**Probabilities:**
- ~1/6 (17%) by 2035
- ~30% by 2040
- ~60% by 2050

### 3. Exposure Analysis Framework

**Bitcoin exposure:**
- Total quantum-exposed coins: ~6 million
- Irreducibly at risk: ~2.3 million (lost keys, early mining)
- Migratable: ~3.7 million (reusable addresses)

**Ethereum exposure:**
- 50-65% at key-revealed accounts
- Can adopt post-quantum signatures proactively

### 4. Risk Assessment Matrix

| Threat Type | Probability | Impact | Mitigation |
|---|---|---|---|
| Signature breakage (Shor) | High (60% by 2050) | Catastrophic | Post-quantum signature migration |
| Mining disruption (Grover) | Low (quadratic only) | Moderate | Already accounted for |
| Governance failure | Medium | Catastrophic | Protocol upgrade coordination |

## Investment Decision Framework

### Step 1: Quantum Exposure Audit
```
For each crypto asset:
1. Identify signature algorithm (ECDSA, EdDSA, BLS, etc.)
2. Calculate % of coins at reusable/derived addresses
3. Estimate migration friction (protocol complexity, governance readiness)
4. Score: 0 (fully quantum-safe) to 100 (fully exposed, no migration path)
```

### Step 2: Timeline Risk Pricing
```
Risk discount factor = Σ P(CRQC at year t) × Impact(t)
Where:
- P(CRQC) = probability from Monte-Carlo forecast
- Impact(t) = function of migration readiness at time t
- Discount to present value
```

### Step 3: Migration Readiness Assessment
- Is there a defined post-quantum signature standard?
- Can the protocol upgrade without hard fork?
- What % of holders can be reached for key migration?
- Is there an economic incentive alignment for migration?

## Key Insight

**The binding constraint is governance, not technology.** A timely post-quantum migration beats even an optimistic 2035 CRQC timeline. Assets with strong governance mechanisms for protocol upgrades are significantly more quantum-resilient.

## Activation Triggers

**Trigger words**: quantum threat bitcoin, quantum ethereum, crypto quantum risk, post-quantum crypto, Shor algorithm crypto, quantum timeline, quantum-resistant blockchain, cryptocurrency quantum vulnerability

**Use cases**:
- Cryptocurrency portfolio risk assessment under quantum threat scenarios
- Investment thesis evaluation for quantum-resilient blockchain protocols
- Timeline-based risk pricing for long-term crypto holdings
- Due diligence on post-quantum migration readiness
- Comparative analysis of different blockchain quantum exposure

## Related Papers

- arXiv:2606.24942 - Quantum-Resilient Decentralized AI Economies (post-quantum security for decentralized systems)
- arXiv:2606.16201 - Q-READY: Predictive Feasibility Assessment for Hybrid Quantum-Classical Applications
- arXiv:2508.21031 - Quantum Economic Advantage Online Calculator
- arXiv:2505.08917 - Quantum Discord and Bounded Rationality in Game Theory
