---
name: quantum-isogeny-sampling
description: "Quantum polynomial-time sampling of secure supersingular elliptic curves with unknown endomorphism rings — foundational methodology for isogeny-based cryptography instantiation without trusted setup."
---

# Quantum Isogeny Sampling

## Description
Quantum algorithm methodology for sampling random supersingular elliptic curves with unknown endomorphism rings. First provable quantum polynomial-time solution to a problem critical for isogeny-based cryptographic protocols. Two variants: (1) O~(log^4 p) quantum gate complexity under GRH, outputting provably secure curves based on endomorphism ring problem hardness; (2) uniform O-oriented curve sampling based on Vectorization Problem hardness. Enables secure instantiation of CGL hash function and related isogeny-based primitives when combined with interactive quantum verification.

## Activation Keywords
- isogeny graph
- supersingular elliptic curve sampling
- quantum isogeny sampling
- CGL hash function
- vectorization problem
- endomorphism ring problem
- 同源图采样
- 超奇异椭圆曲线
- isogeny-based cryptography
- quantum number theory

## Tools Used
- terminal: Run mathematical computations and quantum simulations
- web_search: Search for related cryptographic protocols
- browser: Access mathematical libraries

## Usage Patterns

### Pattern 1: Secure Curve Generation for Isogeny Cryptography
1. Determine field characteristic p
2. Choose imaginary quadratic order O (for oriented variant)
3. Run quantum sampling algorithm:
   - Variant 1: O~(log^4 p) gate complexity (GRH)
   - Variant 2: O~(log^13 p) (unconditional)
4. Verify curve security via endomorphism ring problem hardness

### Pattern 2: CGL Hash Function Instantiation
1. Sample secure supersingular curve using quantum algorithm
2. Combine with interactive quantum computation verification
3. Use as input to CGL hash function
4. Achieve provably secure instantiation without trusted setup

### Pattern 3: Spectral Analysis of Isogeny Graphs
1. Model isogeny graph as expander
2. Compute spectral gap via quantum walk
3. Relate spectral properties to mixing time
4. Use for security parameter selection

## Instructions for Agents

### Step 1: Understand the Problem
Supersingular elliptic curve sampling requires:
- Random curve from S_p (supersingular curves over F_{p^2})
- Unknown endomorphism ring (critical for security)
- Previous methods: trusted setup only

### Step 2: Choose Algorithm Variant
| Variant | Complexity | Security Assumption | Output |
|---------|-----------|-------------------|--------|
| Booher-based | O~(log^4 p) under GRH | Average-case ERP | Secure curve |
| Oriented | O~(log^13 p) | Vectorization Problem | Uniform O-oriented |

### Step 3: Verify Security
- Endomorphism Ring Problem (ERP): Given curve E, find End(E)
- Average-case hardness ensures sampled curve is secure
- Interactive verification adds quantum proof of correctness

### Step 4: Application to Cryptography
- CGL hash: Map curve to hash output via isogeny walks
- SIDH/SIKE: Use sampled curves as starting points
- SQIsign: Use for signature scheme instantiation

## Error Handling

### GRH Dependency
If Generalized Riemann Hypothesis cannot be assumed:
- Fall back to unconditional O~(log^13 p) variant
- Or use classical methods with trusted setup

### Small Prime p
For small p, spectral methods may not provide sufficient security:
- Choose p >= 2^256 for cryptographic security
- Verify isogeny graph expansion properties

## Resources
- arXiv: 2602.02263 — "On the Spectral theory of Isogeny Graphs and Quantum Sampling of Secure Supersingular Elliptic curves"
- Booher et al. algorithm for isogeny-based sampling
- CGL hash function (Charles-Goren-Lauter)
