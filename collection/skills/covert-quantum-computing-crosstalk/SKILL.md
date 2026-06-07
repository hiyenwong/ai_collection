---
name: covert-quantum-computing-crosstalk
description: "Framework for analyzing and ensuring computational covertness in multi-tenant quantum computers, accounting for crosstalk-based side channels and adversarial detection via quantum-strategy framework."
---

# Covert Quantum Computing & Crosstalk Analysis Framework

## Description

Framework for analyzing and ensuring computational covertness in multi-tenant quantum computing environments. Introduces covert quantum computing — ensuring adversaries sharing the same quantum processing unit cannot detect computation on inaccessible qubits. Derives discrete isoperimetric inequalities for border qubit scaling, identifies long-range crosstalk side channels, and employs quantum-strategy framework for covertness analysis accounting for quantum memories and adaptive operations.

## Activation Keywords
- covert quantum computing
- quantum crosstalk analysis
- multi-tenant quantum security
- quantum side channel
- quantum computing privacy
- border qubit scaling
- 量子隐蔽计算
- 量子串扰分析
- 多租户量子安全

## Core Concepts

### 1. Covert Quantum Computing Definition

An adversary with access to all other quantum computational units (QCUs) of a quantum computer **cannot detect** computation on the subset they cannot access. This extends classical covert communication to the quantum computing domain where the adversary **controls the detection systems**.

### 2. Quantum-Strategy Framework for Covertness

Unlike classical covert communication, the adversary controls the systems used for detection. Requires:
- **Quantum memories**: Adversary can store quantum states for later analysis
- **Adaptive operations**: Adversary can adjust measurements based on previous outcomes
- **Quantum game theory**: Strategic interaction between hidden computation and detection

### 3. Border Qubit Scaling Law (Discrete Isoperimetric Inequalities)

For an n-qubit circuit under planar graph layout with nearest-neighbor crosstalk:

```
Detection information scales as O(√n) border qubits
```

Only border qubits provide detection information to the adversary under nearest-neighbor crosstalk assumption.

### 4. Long-Range Crosstalk Side Channel

**Critical finding**: Beyond border qubits, long-range coupling effects exist that:
- Are induced by leakage from drive and control lines
- Allow adversaries to exploit spatially distributed information
- Weaken covertness guarantees
- Expose co-tenants to both adversarial and unintended crosstalk
- Degrade circuits spanning spatially distributed qubits

### 5. Hardware Validation

Verified on real quantum processors:
- **IQM Emerald** (54-qubit): Ramsey experiments confirm nearest-neighbor crosstalk
- **IBM ibm_fez** (156-qubit, Heron 2): Long-range coupling beyond border qubits observed

## Usage Patterns

### Pattern 1: Assessing Covertness of Quantum Computations

When evaluating whether a quantum computation is covert in a multi-tenant environment:

1. Map the qubit layout to a planar graph
2. Identify computation qubits vs. adversary-accessible qubits
3. Apply discrete isoperimetric inequality to find border qubits
4. Count border qubits: O(√n) under nearest-neighbor model
5. **Critical**: Check for long-range crosstalk effects (drive/control line leakage)
6. If long-range effects exist → covertness is weakened

### Pattern 2: Designing Spatially Isolated Quantum Computations

When designing quantum circuits that should remain undetected:

1. Place computation qubits in interior positions (not border)
2. Minimize spatial spread of the circuit
3. Account for drive/control line assignments
4. Implement spatial isolation strategies
5. Characterize crosstalk profile of the specific hardware
6. Use Ramsey experiments to empirically verify isolation

### Pattern 3: Adversarial Detection Analysis

When analyzing what an adversary can detect:

1. Apply quantum-strategy framework (not classical information theory)
2. Model adversary's quantum memory capabilities
3. Consider adaptive measurement strategies
4. Account for both nearest-neighbor and long-range crosstalk
5. Compute detection advantage from border + long-range channels

## Mathematical Framework

### Border Qubit Scaling

```
|Border| ≤ c · √n  (for planar graph with nearest-neighbor crosstalk)
```

where c is a constant depending on the graph geometry.

### Detection Information Bound

```
I_detection ≤ f(|Border| + |LongRange|)
```

where |LongRange| accounts for drive/control line induced coupling.

### Quantum-Strategy Detection Model

```
Advantage = max_{quantum strategy S} P_detect(S) - P_detect(random)
```

over all quantum strategies including memory and adaptive operations.

## Instructions for Agents

### Step 1: Characterize the Quantum Hardware

- Obtain qubit connectivity graph
- Identify physical layout (planar, 2D grid, heavy-hex, etc.)
- Map drive and control line assignments
- Characterize crosstalk profile (nearest-neighbor + long-range)

### Step 2: Apply Isoperimetric Analysis

- Map computation to subgraph of the connectivity graph
- Compute boundary size using discrete isoperimetric inequalities
- Determine information leakage through border qubits

### Step 3: Check Long-Range Effects

- Identify qubits sharing drive/control lines
- Measure or model long-range coupling strength
- Account for additional information leakage

### Step 4: Evaluate Covertness

- Combine border + long-range leakage
- Apply quantum-strategy framework for adversarial detection
- Determine if computation is covert under the adversary model

### Step 5: Mitigation Strategies

If covertness is insufficient:
- Increase spatial isolation
- Use qubits with minimal shared control infrastructure
- Implement active crosstalk cancellation
- Temporal multiplexing of computations

## Error Handling

### Hardware-Specific Variations
- **Issue**: Crosstalk profiles vary significantly between processors
- **Solution**: Always empirically characterize the specific hardware using Ramsey experiments
- **Fallback**: Use conservative bounds assuming worst-case crosstalk

### Long-Range Crosstalk Modeling
- **Issue**: Long-range effects are hardware-dependent and hard to predict
- **Solution**: Use experimental characterization + physics-based modeling
- **Caution**: Drive/control line sharing is often undocumented

### Quantum-Strategy Framework Complexity
- **Issue**: Full quantum-strategy analysis is computationally intensive
- **Solution**: Use simplified bounds for quick estimates, full analysis for critical applications
- **Fallback**: Classical information theory bounds as conservative estimates

## Examples

### Example 1: 54-Qubit IQM Emerald Analysis

1. Map the 54-qubit layout to planar graph
2. Place computation on interior qubits
3. Border qubits ≈ O(√54) ≈ 7-8 qubits
4. Ramsey experiments confirm: only nearest-neighbor crosstalk detected
5. Covertness holds under this model

### Example 2: 156-Qubit IBM Heron 2 Analysis

1. 156-qubit heavy-hex layout
2. Border qubits ≈ O(√156) ≈ 12-13 qubits (nearest-neighbor)
3. **Critical**: Long-range coupling observed beyond border
4. Drive/control line leakage creates additional detection channel
5. Covertness weakened — requires additional mitigation

## Resources

- arXiv: 2605.14325 - "Toward Covert Quantum Computing"
- Authors: Evan J. D. Anderson, Kaushik Datta, Boulat A. Bash
- Categories: quant-ph, cs.CR
- Discrete isoperimetric inequalities on planar graphs

## Related Skills

- quantum-information-security - Quantum information security patterns
- post-quantum-cryptographic-protocol-analysis - Post-quantum crypto analysis
- quantum-network-control - Quantum network resource allocation
