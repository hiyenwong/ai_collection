---
name: covert-quantum-computing
description: "Covert quantum computing methodology for privacy-preserving multi-tenant quantum computation. Addresses adversarial detection, crosstalk analysis, and spatial isolation on quantum processors. Use when designing privacy-preserving quantum cloud systems, analyzing quantum side channels, or studying quantum multi-tenant security."
---

# Covert Quantum Computing

## Core Concept

Covert quantum computing ensures adversaries sharing a multi-tenant quantum processing unit (QPU) cannot detect computation on inaccessible qubit subsets. Extends covert communication theory to quantum computation where the adversary controls detection systems.

## Key Framework

### Threat Model

- Adversary has access to all QCUs except the target subset
- Adversary can use quantum memories and adaptive operations
- Uses quantum-strategy framework from quantum game theory
- Adversary controls systems used for detection

### Spatial Covertness Analysis

#### Planar Graph Circuit Layouts

For n-qubit circuits under nearest-neighbor crosstalk model:
- Only O(\sqrt{n}) border qubits provide detection information to adversary
- Apply discrete isoperimetric inequalities to bound leakage
- Covertness scales with spatial layout of computation

#### Side Channel Vulnerabilities

Long-range coupling beyond border qubits exposes side channels:
- Crosstalk induced by leakage from drive/control lines
- Adversary can exploit non-nearest-neighbor coupling
- Degrades circuits spanning spatially distributed qubits

## Empirical Validation

### Ramsey Experiment Protocol

1. Implement Ramsey experiments on idle (non-computation) qubits
2. Detect nearest-neighbor crosstalk as expected
3. Measure long-range coupling effects beyond border qubits
4. Characterize spatial isolation quality

### Platform Analysis

Analyze covertness on specific hardware:
- IQM 54-qubit Emerald processor (planar layout)
- IBM 156-qubit ibm_fez with Heron 2 architecture
- Compare border qubit count vs total qubits

## Design Patterns

### Spatial Isolation

```python
# Analyze spatial covertness for a given layout
def analyze_covertness(layout_graph, computation_nodes):
    """
    Compute border qubits (adjacent to computation) vs total.
    Border qubits = detection surface for adversary.
    Covertness ratio = 1 - |border|/|total|
    """
    border = set()
    for node in computation_nodes:
        for neighbor in layout_graph.neighbors(node):
            if neighbor not in computation_nodes:
                border.add(neighbor)
    return len(border), len(layout_graph.nodes)
```

### Crosstalk Characterization

1. Map crosstalk matrix for target QPU
2. Identify long-range coupling channels
3. Quantify leakage from drive/control lines
4. Design pulse schedules to minimize side-channel leakage

## Activation Keywords
- covert quantum computing
- quantum privacy
- multi-tenant quantum security
- quantum side channels
- quantum crosstalk
- quantum spatial isolation
- quantum-strategy framework
- 量子隐蔽计算
- 量子多租户安全

## References
- arXiv:2605.14325 - Toward Covert Quantum Computing (Anderson, Datta, Bash)
- Quantum game theory and memory channel discrimination
- Discrete isoperimetric inequalities for planar graphs
