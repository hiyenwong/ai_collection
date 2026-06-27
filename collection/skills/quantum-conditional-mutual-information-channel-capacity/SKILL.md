---
name: quantum-conditional-mutual-information-channel-capacity
description: "Quantum conditional mutual information (QCMI) as operational channel capacity — connects strong subadditivity to quantum communication tasks, extending Csiszár-Ahlswede classical key generation to quantum domain."
version: "1.0"
created: "2026-06-28"
source: "arxiv"
---

# Quantum Conditional Mutual Information and Channel Capacity

## Description

Methodology connecting quantum conditional mutual information (QCMI) to operational channel coding tasks. QCMI is nonnegative due to strong subadditivity, but a direct connection with channel coding was previously elusive. This work proposes conditional quantum communication as a task where the optimal rate for establishing quantum correlation between two parties, assisted by a third system, equals half the QCMI. Extends the classical key generation capacity of Csiszár and Ahlswede to the quantum domain.

## Activation Keywords
- quantum conditional mutual information
- QCMI channel capacity
- strong subadditivity operational meaning
- conditional quantum communication
- quantum key generation capacity
- 量子条件互信息
- quantum channel coding theorem

## Core Concepts

### Quantum Conditional Mutual Information (QCMI)
- I(A;B|C) = S(AC) + S(BC) - S(C) - S(ABC)
- Nonnegative due to strong subadditivity of von Neumann entropy
- Previously lacked direct operational interpretation in channel coding

### Conditional Quantum Communication Task
- Two parties establish quantum correlation
- Assisted by a third system (conditional party)
- Optimal rate = I(A;B|C) / 2

### Classical-to-Quantum Extension
- Extends Csiszár-Ahlswede classical key generation capacity
- Classical: key rate from correlated observations with public discussion
- Quantum: quantum correlation establishment with conditional assistance

## Applications

### 1. Quantum Code Design
- Use QCMI bounds for reliable quantum information processing
- Design codes that exploit conditional correlations
- Optimize assisted communication protocols

### 2. Quantum Network Analysis
- Compute conditional capacity for example channels
- Analyze multi-party quantum communication scenarios
- Understand role of third-party assistance in quantum protocols

### 3. Quantum Information Theory
- Bridge between abstract information measures and operational tasks
- Unify family tree of quantum protocols
- Derive new capacity formulas from QCMI

## Key Mathematical Results

1. **Main Theorem**: Optimal rate for conditional quantum correlation = QCMI / 2
2. **Channel Examples**: Conditional capacity computed for several example channels
3. **Protocol Placement**: Results placed within quantum protocol family tree

## Implementation Patterns

### Computing QCMI for a Channel
1. Identify the tripartite system (A, B, C)
2. Compute marginal entropies S(AC), S(BC), S(C), S(ABC)
3. Apply I(A;B|C) = S(AC) + S(BC) - S(C) - S(ABC)
4. Divide by 2 for communication rate

### Protocol Design
1. Set up conditional communication scenario
2. Identify assisting system and its role
3. Design encoding/decoding to achieve QCMI/2 rate
4. Verify against channel examples

## Related Concepts
- Strong subadditivity of quantum entropy
- Csiszár-Ahlswede key generation capacity
- Quantum channel coding theorems
- Quantum state redistribution
- Quantum state merging
- Entanglement-assisted communication

## arXiv Reference
- Paper: "Quantum conditional mutual information and channel capacity"
- ID: 2606.25264
- URL: https://arxiv.org/abs/2606.25264
- Authors: D.-S. Wang
- Published: 2026-06-24
- Categories: quant-ph, cs.IT

## Notes
- This work fills a gap between abstract information theory and operational quantum communication
- The factor of 1/2 is consistent with quantum-vs-classical rate relationships
- Provides design principles for codes in reliable quantum information processing
