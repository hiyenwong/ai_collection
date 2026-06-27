---
name: quantum-conditional-mutual-information-channel-capacity
description: >
  Quantum conditional mutual information (QCMI) and channel capacity methodology. Proposes conditional
  quantum communication task showing optimal rate for establishing quantum correlation between two parties
  assisted by a third system equals half the QCMI. Extends classical key generation capacity (Csiszar-Ahlswede)
  to the quantum domain. Use when: analyzing quantum channel capacity, designing quantum communication protocols,
  studying quantum conditional mutual information, or computing conditional capacity for quantum channels.
  Trigger words: quantum conditional mutual information, QCMI, channel capacity, quantum communication,
  Csiszar Ahlswede, strong subadditivity, quantum correlation, quantum key generation.
---

# Quantum Conditional Mutual Information and Channel Capacity

arXiv: 2606.25264 | Wang (2026)

## Core Result

The **optimal rate** for establishing quantum correlation between two parties, assisted by a third system,
is given by **half the QCMI**:

```
R* = I(A;B|C) / 2
```

This fills the gap between QCMI's nonnegativity (from strong subadditivity) and an operational channel coding interpretation.

## Key Contributions

1. **Conditional quantum communication task**: New protocol family connecting QCMI to coding theorems
2. **Quantum extension of Csiszar-Ahlswede**: Generalizes classical key generation capacity to quantum domain
3. **Protocol family tree**: Places conditional communication within the landscape of quantum protocols
4. **Conditional capacity computations**: Provides explicit calculations for example channels

## Methodology

### For Quantum Channel Analysis
1. Identify the three-party structure (A, B, C) in your system
2. Compute QCMI: I(A;B|C) = S(AC) + S(BC) - S(C) - S(ABC)
3. The conditional capacity equals I(A;B|C)/2
4. Design coding schemes achieving this rate

### Design Principles
- QCMI quantifies the "quantum correlation assistable by a third party"
- Rate is achievable with appropriate coding strategies
- Extensions to multiple parties follow similar patterns

## Applications
- Quantum network capacity analysis
- Distributed quantum computing protocols
- Quantum key distribution with trusted relays
- Multi-party quantum communication complexity

## Activation Keywords
quantum conditional mutual information, QCMI, channel capacity, quantum communication, Csiszar Ahlswede, strong subadditivity, quantum correlation
