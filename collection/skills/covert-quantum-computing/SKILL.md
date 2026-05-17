---
name: covert-quantum-computing
description: "Covert quantum computing methodology — ensuring privacy against co-tenant adversaries in multi-tenant quantum cloud platforms. Covers information-theoretic covertness analysis, discrete isoperimetric inequalities, crosstalk-based side channels, and quantum-strategy framework for adversarial detection."
tags: ["quantum-computing", "information-theory", "security", "privacy", "quantum-cloud"]
related_skills: ["quantum-information-protocol-analyzer", "cross-layer-crypto-analysis"]
---

# Covert Quantum Computing

## Description

Methodology for designing and analyzing covert quantum computing systems that hide computation from adversarial co-tenants on shared quantum processing units. Based on arXiv:2505.11747 "Toward Covert Quantum Computing" (Anderson, Datta, Bash, 2026). Applies information theory to quantum multi-tenant privacy, using quantum-strategy frameworks and discrete isoperimetric analysis.

## Activation Keywords

- covert quantum computing
- quantum privacy
- quantum cloud security
- 量子隐蔽计算
- multi-tenant quantum
- quantum crosstalk
- quantum side channel
- QCU privacy
- quantum covertness
- 量子云平台安全

## Core Concepts

### 1. Covert Quantum Computing Definition

An adversary with access to all other Quantum Computational Units (QCUs) of a shared quantum computer **cannot detect** computation happening on the subset they cannot access. Analogous to covert communication, but the adversary controls the detection systems.

### 2. Quantum-Strategy Framework

Since the adversary controls the systems used for detection, standard information theory is insufficient. The analysis requires:
- **Quantum memories**: Adversary can store quantum states for later measurement
- **Adaptive operations**: Adversary can adjust detection strategy based on prior results
- **Memory channel discrimination**: The adversary's detection is modeled as distinguishing between quantum channels

### 3. Discrete Isoperimetric Inequality

For an n-qubit circuit under planar graph nearest-neighbor crosstalk model:
- Only **O(√n) border qubits** provide detection information to the adversary
- Interior qubits are "shielded" by the graph topology
- This scaling law determines the fundamental covertness limit

### 4. Crosstalk Side Channels

Real quantum hardware reveals additional attack surfaces:
- **Nearest-neighbor crosstalk**: Expected and modeled by the isoperimetric analysis
- **Long-range coupling**: Observed on both IQM Emerald (54-qubit) and IBM Heron 2 (156-qubit)
- **Leakage-induced coupling**: Drive and control lines induce side channels beyond border qubits
- These weaken covertness and degrade spatially distributed circuits

## Implementation Methodology

### Phase 1: Covertness Analysis

```python
def analyze_covertness(n_qubits, topology="planar"):
    """Analyze covertness properties for a given circuit."""
    
    # Step 1: Compute border qubits via isoperimetric inequality
    if topology == "planar":
        border_qubits = O(sqrt(n_qubits))
    else:
        # For other topologies, compute vertex boundary
        border_qubits = vertex_boundary(circuit_graph)
    
    # Step 2: Model adversary's detection capability
    # Adversary measures border qubits using quantum-strategy framework
    detection_capacity = compute_detection_capacity(
        border_qubits=border_qubits,
        adversary_memory=True,
        adaptive_operations=True
    )
    
    # Step 3: Compute covertness bound
    # Probability adversary detects computation
    detection_probability = bound_detection_probability(detection_capacity)
    
    return {
        "border_qubits": border_qubits,
        "detection_probability": detection_probability,
        "covertness_achievable": detection_probability < threshold
    }
```

### Phase 2: Crosstalk Characterization

```python
def characterize_crosstalk(backend_name, num_qubits):
    """Characterize crosstalk channels on real quantum hardware."""
    
    # Ramsey experiment on idle qubits while neighbors execute gates
    for idle_qubit in qubits:
        # Apply Ramsey sequence
        ramsey_signal = run_ramsey(idle_qubit)
        
        # While neighbors execute random gates
        for neighbor in get_neighbors(idle_qubit):
            execute_random_gates(neighbor)
        
        # Measure phase shift → crosstalk strength
        crosstalk_strength = measure_phase_shift(ramsey_signal)
    
    # Map both nearest-neighbor and long-range crosstalk
    return crosstalk_map
```

### Phase 3: Security Assessment

| Threat Model | Detection Method | Mitigation |
|-------------|-----------------|------------|
| Nearest-neighbor crosstalk | Isoperimetric bound O(√n) | Already limited by topology |
| Long-range crosstalk | Drive line leakage | Shielding, scheduling |
| Control line leakage | Spectral analysis | Frequency planning |
| Adversary with quantum memory | Quantum-strategy framework | Temporal isolation |

## Practical Implications

### For Quantum Cloud Providers

1. **Spatial isolation**: Assign qubits with maximum graph distance between tenants
2. **Crosstalk characterization**: Regular Ramsey-based crosstalk mapping
3. **Temporal scheduling**: Serialize operations when covertness is critical
4. **Hardware hardening**: Reduce long-range coupling through better drive line design

### For Quantum Algorithm Designers

1. **Qubit selection**: Prefer interior qubits for sensitive computations
2. **Circuit layout**: Minimize border exposure of critical subcircuits
3. **Timing**: Execute sensitive operations when neighboring QCUs are idle

### For Security Researchers

1. **Attack surface**: Long-range crosstalk is a previously uncharacterized side channel
2. **Detection limits**: O(√n) border provides theoretical upper bound on adversary info
3. **Quantum-strategy framework**: Generalizes beyond simple measurement to adaptive quantum detection

## Related Research Patterns

- **Covert classical communication**: Information-theoretic square-root law for classical channels
- **Quantum key distribution**: Related but different — QKD secures content, covert computing hides existence
- **Side-channel attacks**: Crosstalk is analogous to electromagnetic/timing side channels in classical systems
- **Multi-tenant cloud security**: Quantum extension of classical cloud isolation problems

## Error Handling

### Hardware-Specific Variations
Different quantum processors have different crosstalk profiles:
- IQM Emerald: Nearest-neighbor dominated
- IBM Heron 2: Significant long-range coupling observed
- Always characterize your specific hardware

### Framework Limitations
- The O(√n) bound assumes planar nearest-neighbor topology
- Real hardware may violate this assumption via long-range coupling
- Quantum-strategy framework analysis is computationally intensive

## Examples

### Example 1: Covertness Assessment for 54-Qubit Processor

```
Given: IQM Emerald, 54 qubits, planar topology
Border qubits: O(√54) ≈ 7 qubits
Detection information available: Limited to 7/54 ≈ 13% of qubits
Covertness: Achievable for interior computations
Risk: Long-range crosstalk may increase detection surface
```

### Example 2: Security Design for Multi-Tenant Quantum Cloud

```
Problem: Two tenants share a 156-qubit IBM Heron 2 processor
Solution:
1. Map crosstalk topology via Ramsey experiments
2. Assign qubit subsets maximizing graph distance
3. Schedule sensitive operations during idle neighbor periods
4. Monitor for long-range coupling anomalies
```

## References

- arXiv: "Toward Covert Quantum Computing" — Anderson, Datta, Bash (2026)
- Quantum game theory and memory channel discrimination literature
- Discrete isoperimetric inequalities in graph theory
- Classical covert communication (Bash et al., square-root law)

## Limitations

- Current analysis limited to nearest-neighbor crosstalk models
- Long-range coupling mechanisms not fully characterized
- Quantum-strategy framework computations scale exponentially with adversary resources
- Hardware-specific results may not generalize across quantum architectures
