---
name: brain-prompt-injection-bci-llm-security
description: Brain-Prompt Injection security audit framework for BCI-LLM agents with route-safety audit contract, C3 decomposition, and split-conformal calibration
version: 1.0.0
author: Hermes Agent (Cron Job)
date: 2026-06-10
paper_id: arXiv:2606.09315v1
paper_title: "Brain-Prompt Injection - A Route-Safety Audit for BCI-LLM Agents"
paper_authors: Jianwei Tai
tags:
  - neuroscience
  - bci-security
  - llm-agents
  - brain-computer-interface
  - security-audit
  - route-safety
  - eeg
  - adversarial-attacks
---

# Brain-Prompt Injection: BCI-LLM Security Audit Framework

## Overview

Brain-Prompt Injection exposes a novel attack surface in BCI-to-agent pipelines where decoded neural activity becomes an authorization channel for tool-use agents. This framework defines a Route-Safety Audit Contract with mathematical guarantees for detecting three attack types: signal-side perturbations, context-only injections, and adaptive dual-decoder attacks.

## Core Innovation

**Route-Safety Audit Contract**: A minimal log schema, denominator hierarchy, and endpoint specification that enables detection of attacks that bypass EEG-side or text-side monitors.

## Attack Surface Analysis

### Three Attack Types

```
Attack Taxonomy:
├── Signal-Side Perturbations
│   └── Modify neural signals before decoding
├── Context-Only Injections
│   └── Inject malicious context without signal changes
└── Adaptive Dual-Decoder Attacks
    └── Exploit decoder differences to route malicious actions
```

### Blind Monitor Problem

**Key Finding**: Clean agreement and marginal robustness do not identify the joint term that controls C3 routing. Traditional monitors (EEG-side, text-side) remain blind to these attacks.

## Route-Safety Audit Contract

### Contract Components

**1. Minimal Log Schema**:
- Signal Provenance (signal-side audit)
- Context Provenance (text-side audit)
- Route Decision (endpoint specification)
- Confirmation Channel (split-conformal calibration)

**2. Denominator Hierarchy**:
- Seed: Initial signal/context denominator
- Case: Per-event denominator tracking
- Endpoint: Final route decision denominator

**3. Endpoint Specification**:
- C2 routes: Provenance-blocked (FAR: 0.000)
- C3 routes: Agreement-plus-provenance required (FAR: 1.000)
- Confirmation-plus-provenance: C3 flips blocked (FAR: 0.000)

### Audit-Schema Separation Theorem

**Mathematical Guarantee**: Clean agreement + marginal robustness ≠ C3 routing control. C3 attacked-dependence decomposition shows joint term separation.

## Split-Conformal Calibration

### False-Accept Frontier Results

**EEGMMI Native Left/Right Command-Control (5,400 events)**:

- Alpha 0.005: FAR 0.000, Clean utility 0.150 (acquisition isolation)
- Alpha 0.10: FAR 0.119, Clean utility 0.452 (acquisition isolation)
- Attacker-controlled confirmation: FAR ≈ 1.0 (bound broken)

**Key Insight**: Attacker-controlled confirmation channel breaks conformal bound.

## Experimental Validation

### Dataset: EEGMMI (60 Subjects)
- Native left/right command-control
- 5,400 events total
- Harmless tool stubs for route endpoints
- Cross-architecture: TinyEEGNet, EEGNetV4

### Route Blocking Results
- Provenance-only → C2 routes blocked (FAR: 0.000)
- Agreement + Provenance → C3 flips routed (FAR: 1.000)
- Confirmation + Provenance → C3 flips blocked (FAR: 0.000)

## Implementation Guide

### Step 1: Deploy Audit Contract Log Schema

```python
class RouteSafetyLog:
    def __init__(self):
        self.signal_provenance = []  # Signal-side audit
        self.context_provenance = []  # Text-side audit
        self.route_decisions = []     # Endpoint decisions
        self.confirmation_scores = []  # Split-conformal scores
```

### Step 2: Split-Conformal Calibration

```python
def split_conformal_calibration(EEG_signals, threat_matrix, alpha):
    cal_signals, test_signals = split_data(EEG_signals)
    cal_scores = compute_confirmation_scores(cal_signals)
    threshold = np.quantile(cal_scores, 1 - alpha)
    FAR = compute_false_accept_rate(test_signals, threshold, threat_matrix)
    return FAR, threshold
```

### Step 3: Route Decision Validation

Check provenance + agreement + confirmation triple.

## Pitfalls and Security Considerations

### 1. Attacker-Controlled Confirmation Channel
- Risk: Conformal bound breaks to ≈1.0
- Mitigation: Use non-oracle, hardened confirmation source

### 2. Context-Only Injection Blindness
- Traditional monitors blind to context attacks
- Solution: Add context provenance logging

### 3. Dual-Decoder Exploit
- Agreement check alone insufficient
- Mitigation: Provenance + agreement + confirmation triple check

### 4. C3 Routing Control Blindness
- Joint term not detected by clean metrics
- Solution: C3 attacked-dependence decomposition

## Applications

- BCI security audit and attack detection
- LLM agent safety for brain-to-agent pipelines
- Medical device compliance (FDA/IEC 62304)
- Neurotechnology security standards

## Key Findings Summary

1. **Agreement Insufficiency**: Clean agreement ≠ route safety
2. **Conformal Effectiveness**: FAR 0.000 at α=.005, 0.119 at α=.10
3. **Attacker-Control Failure**: Confirmation control breaks bounds
4. **Mediation vs Intent**: Mediation reduces risk but not intent certificate

## References

- Paper: arXiv:2606.09315v1
- Author: Jianwei Tai
- Categories: cs.CR, cs.AI
- Keywords: BCI security, brain-prompt injection, route safety, EEG command-control

## Activation Keywords

brain-prompt injection, BCI security, route safety audit, LLM agent BCI, EEG command control, adversarial brain attacks, neural authorization security

---

**Summary**: Brain-Prompt Injection framework provides mathematical guarantees for detecting BCI-LLM attacks through Route-Safety Audit Contract. Split-conformal calibration achieves FAR 0.000 at α=.005 under acquisition isolation. Provenance + agreement + confirmation triple check required for route safety; mediation alone insufficient for intent certification.