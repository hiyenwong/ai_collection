---
name: quantum-stabilizer-testing-limited-memory
description: "Optimal stabilizer testing and learning methodology under limited quantum memory constraints. Provides sample complexity bounds and efficient algorithms for testing whether quantum states are stabilizer states when quantum memory is bounded."
trigger_words: ["stabilizer testing", "quantum memory constraints", "sample complexity", "quantum state testing", "limited quantum memory", "stabilizer learning"]
category: "quantum"
---

## Overview

This paper (arXiv:2607.02444) establishes optimal methods for testing and learning stabilizer states under limited quantum memory. Proves tight sample complexity bounds for stabilizer testing when the tester can only store a bounded number of qubits.

## Core Results

### Sample Complexity Bounds
- **Testing**: Θ(d²) measurement settings are necessary and sufficient for stabilizer testing
- **Learning**: Optimal algorithms exist even with severely bounded quantum memory
- **Memory constraint**: Results hold when quantum memory is limited to O(1) qubits

### Key Techniques
1. **Bell sampling**: Uses Bell difference sampling to extract stabilizer information
2. **Classical post-processing**: Efficient classical algorithms for processing measurement outcomes
3. **Memory-bounded protocols**: Protocols that work with minimal quantum memory storage

## Methodology

### Stabilizer Testing Protocol
```
1. Prepare multiple copies of the unknown state |ψ⟩
2. Perform Bell difference sampling on pairs of copies
3. Collect measurement outcomes (classical data)
4. Run classical statistical test on outcomes
5. Accept/reject stabilizer hypothesis based on test statistic
```

### Sample Complexity Analysis
- Lower bound: Ω(d²) samples needed for d-dimensional systems
- Upper bound: O(d²) samples sufficient with optimal protocol
- Gap between quantum-memory and classical-memory protocols characterized

## Implementation Patterns

### Bell Difference Sampling
```
Input: Two copies of state |ψ⟩
1. Apply Bell measurement to corresponding qubit pairs
2. Record measurement outcome x ∈ {0,1}^n
3. Repeat to collect distribution over outcomes
4. Analyze distribution for stabilizer structure
```

### Classical Testing Algorithm
```
Input: Collection of Bell measurement outcomes
1. Compute empirical distribution
2. Check if distribution concentrates on stabilizer subgroup
3. Statistical test: chi-squared or likelihood ratio
4. Threshold based on desired confidence level
```

## Pitfalls

- **Memory bottleneck**: When quantum memory is limited, cannot store full state — must use streaming protocols
- **Sample efficiency**: O(d²) scaling can be prohibitive for large systems; use dimensionality reduction
- **Noise sensitivity**: Real hardware noise can mimic non-stabilizer behavior; calibrate noise model first

## Applications

- Quantum error correction: Verify stabilizer structure of encoded states
- Quantum state verification: Certify preparation of target stabilizer states
- Quantum benchmarking: Test if device produces stabilizer states correctly

## Verification

1. Test on known stabilizer states (GHZ, graph states) — should accept
2. Test on known non-stabilizer states (T-gate outputs) — should reject
3. Vary quantum memory size and verify sample complexity scaling
4. Compare with full-memory baseline to validate bounded-memory protocols

## Activation

stabilizer testing, limited quantum memory, sample complexity, Bell sampling, quantum state testing, stabilizer learning, quantum verification, memory-bounded protocols, quantum benchmarking
