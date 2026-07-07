---
name: quantum-conditional-mutual-information-channel-capacity
category: quantum
description: Quantum conditional mutual information (QCMI) and channel capacity methodology — establishes operational meaning of QCMI through conditional quantum communication task, proving optimal rate for establishing quantum correlation equals half the QCMI.
version: 1.0
created: 2026-06-28
tags:
  - quantum-information-theory
  - channel-capacity
  - conditional-mutual-information
  - quantum-communication
  - coding-theorems
  - entanglement
activation:
  keywords: ["QCMI", "quantum conditional mutual information", "channel capacity", "quantum communication", "strong subadditivity", "coding theorem", "quantum correlation", "entanglement rate", "quantum Shannon theory"]
  papers: ["2606.25264"]
---

# Quantum Conditional Mutual Information and Channel Capacity

## Overview

This methodology establishes the operational meaning of **Quantum Conditional Mutual Information (QCMI)** through a novel quantum communication task, filling a fundamental gap in quantum information theory.

## Core Problem

QCMI I(A;B|C) is nonnegative due to strong subadditivity, yet a direct connection with channel coding had remained elusive. Unlike classical conditional mutual information (which equals the capacity of the relay channel), QCMI lacked an operational interpretation in terms of communication rates.

## Key Innovation: Conditional Quantum Communication Task

The paper proposes a new quantum communication task — **conditional quantum communication** — where:
- Two parties (A and B) aim to establish quantum correlations
- Assisted by a third system C
- The optimal rate for this task is proven to be **exactly half the QCMI**: R* = (1/2)I(A;B|C)

## Mathematical Framework

### QCMI Definition
I(A;B|C) = S(AC) + S(BC) - S(C) - S(ABC)
where S(.) is the von Neumann entropy.

### Main Result
The optimal rate for establishing quantum correlation between two parties, assisted by a third system, equals:
R* = (1/2)I(A;B|C)

This provides the first direct operational interpretation of QCMI in terms of a communication task.

### Implications

1. **Quantum Markov Chain Recovery**: The result naturally connects to quantum Markov chain recovery maps, providing a communication-theoretic understanding of approximate Markov conditions.

2. **Entanglement of Formation**: Yields an alternate proof of a known bound on the entangment of formation.

3. **Quantum Shannon Theory**: Completes the picture of how information measures acquire operational meaning through coding theorems in the quantum setting.

## Applications

### 1. Quantum Network Communication
- Understanding multi-party quantum communication protocols
- Characterizing the role of side information in quantum networks
- Designing efficient quantum relay protocols

### 2. Quantum Error Correction
- QCMI bounds relate to quantum error correction conditions
- Provides framework for analyzing correlated noise in quantum channels
- Connects to quantum Markov recovery for error correction

### 3. Quantum Cryptography
- Understanding information flow in quantum key distribution with side information
- Characterizing security against adversaries with quantum side information

### 4. Many-Body Physics
- QCMI characterizes topological order in quantum states
- Connection to area laws and entanglement structure
- Analyzing quantum phase transitions

## Implementation Patterns

### Pattern 1: QCMI as Communication Rate
When analyzing multi-party quantum protocols, use QCMI to determine achievable rates for correlation establishment with side information assistance.

### Pattern 2: Recovery Map Construction
Use the connection between QCMI and recovery maps to construct approximate quantum Markov recoveries:
I(A;B|C) >= -2 log F(rho_ABC, R_{C->BC}(rho_AC))

### Pattern 3: Entanglement Bounds
Apply QCMI bounds to derive limits on entanglement of formation and other entanglement measures in multi-party settings.

## Key Relationships

| Information Measure | Classical Operational Meaning | Quantum Operational Meaning |
|---|---|---|
| Mutual Information I(A;B) | Channel capacity | Entanglement-assisted capacity |
| Conditional MI I(A;B|C) | Relay channel capacity | **Conditional quantum communication rate** (this work) |
| QCMI I(A;B|C) | N/A | Half the optimal correlation rate |

## Research Directions

1. **Generalized Tasks**: Extend to other quantum information measures lacking operational interpretations
2. **Finite-Blocklength**: Analyze finite-blocklength behavior of the conditional communication task
3. **Network Extensions**: Apply to more complex quantum network topologies
4. **Experimental Verification**: Design experiments to measure QCMI through communication rates

## References

- arXiv:2606.25264 — "Quantum conditional mutual information and channel capacity" by D.-S. Wang (2026)
- Strong subadditivity of quantum entropy (Lieb & Ruskai, 1973)
- Quantum Markov chain recovery (Fawzi & Renner, 2015)
