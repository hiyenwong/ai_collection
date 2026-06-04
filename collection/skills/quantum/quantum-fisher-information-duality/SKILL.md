---
name: quantum-fisher-information-duality
description: "Quantum Fisher Information (QFI) duality methodology for distributed quantum sensing — establishing fundamental trade-offs between sensing precision and parameter privacy."
---

# Quantum Fisher Information Duality

## Description
Quantum Fisher Information (QFI) duality methodology for analyzing precision-privacy trade-offs in distributed quantum sensor networks. Establishes the fundamental bound F_Q(w^T θ) + F_Q(v^T θ) ≤ N for any N-qubit probe state with orthogonal sensing directions, proving that Heisenberg-limited precision for a target parameter forces zero QFI for all other independent directions — making precision the condition for parameter privacy. Based on arXiv:2605.20765 (Farhad Farokhi, May 2026).

## Activation Keywords
- quantum fisher information duality
- QFI duality
- precision privacy quantum sensing
- 量子费舍尔信息对偶性
- distributed quantum sensing
- parameter privacy quantum
- quantum sensor network privacy
- Heisenberg precision privacy

## Core Concepts

### QFI Duality Theorem
For any N-qubit probe state with local phase encoding:

**F_Q(w^T θ) + F_Q(v^T θ) ≤ N**

for all unit orthogonal sensing directions w and v, with equality for:
- All equatorial states when N=2
- Greenberger-Horne-Zeilinger (GHZ) states when N≥2

### Precision-Privacy Duality
- **Heisenberg-limited precision** for direction w: F_Q(w^T θ) = N
- **Privacy guarantee**: Zero QFI for all other independent directions
- **Interpretation**: Achieving maximum sensing precision for a target parameter renders all alternative privacy-intrusive estimations impossible
- This is the **quantum information security** equivalent of "knowing one thing perfectly means knowing nothing else"

### Key States
| State Type | Equality Condition | N Range |
|-----------|-------------------|---------|
| Equatorial states | F_Q(w^T θ) + F_Q(v^T θ) = N | N = 2 |
| GHZ states | F_Q(w^T θ) + F_Q(v^T θ) = N | N ≥ 2 |

## Mathematical Framework

### QFI for Linear Combinations
For sensing direction w and parameter vector θ:
- **QFI(w^T θ)** = variance of generator H_w in probe state ρ
- Bound: QFI(w^T θ) ≤ N·||w||² for N sensors

### Privacy Condition
- **Privacy breach risk**: Adversary estimating θ along direction v ≠ w
- **Privacy guarantee**: F_Q(v^T θ) = 0 when F_Q(w^T θ) = N
- **Trade-off curve**: F_Q(v^T θ) ≤ N - F_Q(w^T θ)

### GHZ State Optimality
GHZ states achieve the tight bound for all N ≥ 2, making them optimal for precision-privacy applications in distributed quantum sensing.

## Usage Patterns

### Pattern 1: Precision-Privacy Analysis
Analyze quantum sensor networks to determine:
1. What precision level is achievable for the target parameter
2. What privacy guarantees exist for other parameters
3. Which probe states (GHZ, equatorial, etc.) optimize the trade-off

### Pattern 2: Sensor Network Design
Design distributed quantum sensors that:
1. Use GHZ states for N ≥ 2 sensors
2. Encode parameters locally (phase encoding)
3. Verify QFI duality bound holds
4. Quantify the privacy margin for non-target parameters

### Pattern 3: Quantum Information Security
Apply QFI duality to:
1. Prove privacy guarantees in quantum metrology
2. Design secure quantum sensor protocols
3. Analyze information leakage in multi-parameter estimation

## Instructions for Agents

### Step 1: Identify the Quantum Sensing Problem
- Determine number of sensors N
- Identify target parameter θ_target (direction w)
- Identify privacy-sensitive parameters θ_privacy (direction v)
- Verify w · v = 0 (orthogonal directions)

### Step 2: Apply QFI Duality Bound
- Calculate F_Q(w^T θ) for the target parameter
- Use bound: F_Q(v^T θ) ≤ N - F_Q(w^T θ)
- Determine if Heisenberg limit F_Q(w^T θ) = N is achievable

### Step 3: Select Optimal Probe State
- For N = 2: Equatorial states achieve equality
- For N ≥ 2: GHZ states achieve equality
- For non-optimal states: privacy margin is reduced

### Step 4: Analyze Privacy Guarantees
- If F_Q(w^T θ) = N (Heisenberg limit): complete privacy for orthogonal directions
- If F_Q(w^T θ) < N: partial information leakage possible
- Quantify the maximum extractable information by adversary

### Step 5: Design and Validate
- Propose sensor configuration
- Verify QFI bound analytically
- Simulate or reference theoretical results
- Document precision-privacy trade-off curve

## Error Handling

### Non-Orthogonal Directions
- If w and v are not orthogonal, the bound F_Q(w^T θ) + F_Q(v^T θ) ≤ N does not apply directly
- Use generalized bound: F_Q(w^T θ) + F_Q(v^T θ) ≤ N(1 + |w·v|)

### Noisy Channels
- The duality theorem assumes local phase encoding without noise
- For noisy channels: QFI is reduced, trade-off curve shifts
- Consider noise-aware extensions of the duality

### Multi-Parameter Estimation
- For k > 2 orthogonal directions: sum of QFIs ≤ N
- Each additional direction reduces available precision for others
- Design sensor allocation strategy based on priority

## Examples

### Example: 4-Sensor Network with Privacy
```
Setup: N=4 sensors, target direction w, privacy direction v
Probe state: GHZ state (optimal for N≥2)
Result: F_Q(w^T θ) = 4 (Heisenberg limit)
Privacy: F_Q(v^T θ) = 0 (complete privacy guarantee)
Conclusion: Maximum precision for target, zero information leakage for adversary
```

### Example: Precision-Privacy Trade-off Curve
```
For N sensors, vary target precision F_Q(w^T θ) from 0 to N:
Privacy margin = N - F_Q(w^T θ)
At F_Q = 0: Full information available for all directions (no privacy)
At F_Q = N: Zero information for orthogonal directions (maximum privacy)
Linear trade-off: Precision + Privacy = N
```

## Resources
- arXiv:2605.20765 - "Precision and Privacy in Distributed Quantum Sensing: A Quantum Fisher Information Duality"
- Categories: quant-ph, cs.CR (Cryptography and Security), cs.IT (Information Theory)
- Related: quantum metrology, quantum parameter estimation, distributed sensing

## Related Skills
- quantum-computational-sensing
- quantum-fisher-information-duality
- quantum-privacy-amplification
