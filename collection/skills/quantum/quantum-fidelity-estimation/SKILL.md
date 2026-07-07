---
name: quantum-fidelity-estimation
description: "Quantum state fidelity estimation methodology with optimal sample complexity bounds. Covers O(r²/ε²) upper and Ω(r/ε²) lower bounds for rank-r reference states, tolerant certification, and quantum query complexity implications. Use when estimating quantum state fidelity, designing certification protocols, or analyzing quantum sample complexity."
metadata:
  arxiv_id: "2606.26034"
  published: "2026-06-24"
  authors: "Qisheng Wang"
  tags: ["quantum", "statistics", "fidelity", "sample-complexity", "certification", "quantum-query-complexity"]
---

# Quantum Fidelity Estimation

## Description
Methodology for estimating the fidelity of an unknown quantum state to a known reference state with optimal sample complexity bounds. Provides tight upper bound O(r²/ε²) and lower bound Ω(r/ε²) for rank-r reference states.

## Activation Keywords
- quantum state fidelity estimation
- fidelity to reference state
- quantum sample complexity
- quantum state certification
- tolerant certification
- 量子态保真度估计
- 量子样本复杂度
- quantum query complexity fidelity
- fidelity estimation bounds

## Core Theory

### Problem Statement
Given an unknown quantum state ρ and a known reference state σ of rank r, estimate F(ρ, σ) to within additive error ε.

### Sample Complexity Bounds
- **Upper bound**: O(r²/ε²) when reference state has rank r (improves prior O(r²log²(1/ε)/ε⁴))
- **Lower bound**: Ω(r/ε²) (improves prior Ω(r/ε + 1/ε²))
- **Generalized case**: Unknown state rank ≤ r, arbitrary reference → O(r²/ε⁴)

### Key Improvement
The ε-dependence is now optimal (1/ε² in upper bound, matching lower bound), removing the logarithmic factors from previous work (Utsumi et al., QIP 2026).

## Usage Patterns

### Pattern 1: Fidelity Estimation Protocol Design
1. Identify reference state rank r
2. Choose error tolerance ε
3. Compute sample budget: O(r²/ε²) copies
4. Implement parity-based observable measurements
5. Apply tolerant certification framework if needed

### Pattern 2: Quantum Query Complexity Analysis
1. Use Ω(r/ε²) lower bound to establish query complexity limits
2. Compare algorithm performance against optimal bounds
3. Identify gap between upper and lower bounds (factor of r)

### Pattern 3: Tolerant Quantum State Certification
1. Generalize exact certification (Badescu-O'Donnell-Wright, STOC 2019)
2. Define acceptance/rejection thresholds based on fidelity
3. Use O(r²/ε⁴) sample complexity for unknown low-rank states

## Error Handling
- If ε is too small relative to available copies, increase ε or use amplitude estimation techniques
- If reference state is full-rank (r = d), sample complexity becomes O(d²/ε²) — may be infeasible for large d
- Lower bound gap of factor r indicates room for algorithm improvement

## References
- arXiv:2606.26034 - Estimating Fidelity to a Reference Quantum State (Qisheng Wang, 2026)
- Utsumi, Nakata, Wang, Takagi (QIP 2026) - previous best O(r²log²(1/ε)/ε⁴)
- Badescu, O'Donnell, Wright (STOC 2019) - exact quantum state certification
