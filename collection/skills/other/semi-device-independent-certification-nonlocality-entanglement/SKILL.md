---
name: semi-device-independent-certification-nonlocality-entanglement
description: "Semi-device-independent certification methodology for nonlocality without entanglement (NLWE) using maximum-confidence discrimination. Proves global measurements outperform separable ones for ensembles of separable states, establishing NLWE through confidence-based state identification. Use when analyzing quantum state discrimination protocols, semi-device-independent quantum certification, maximum-confidence measurements, nonlocality without entanglement, or quantum communication security protocols. arXiv: 2606.13667."
---

# Semi-Device-Independent Certification for Nonlocality without Entanglement

## Context

Nonlocality without entanglement (NLWE) demonstrates that separable (non-entangled) quantum states can exhibit nonlocal behavior when distinguishing them requires global measurements that outperform separable (local) measurements. This paper establishes NLWE through **maximum-confidence discrimination** — a fine-grained state-identification strategy encompassing both minimum-error and unambiguous discrimination.

## Core Methodology

### 1. Maximum-Confidence Discrimination Framework

For an ensemble of separable states {ρ_i, p_i}:
- **Maximum-confidence measurement** maximizes P(ρ_k correct | outcome k) — the probability of a correct guess given a measurement outcome
- This framework generalizes both minimum-error discrimination (maximizes overall success rate) and unambiguous discrimination (zero error, allows inconclusive outcomes)
- Key insight: maximum-confidence measurements depend only on detected outcomes, not detection efficiency

### 2. NLWE via Confidence Gap

**Procedure:**
1. Consider an ensemble of separable states
2. Compute optimal confidence achievable with global measurements: C_global
3. Compute optimal confidence achievable with separable (LOCC) measurements: C_separable
4. If C_global > C_separable → NLWE is established

**Mathematical formulation:**
- For each state ρ_k in the ensemble, the maximum confidence is:
  C_k = max_M Tr(M_k ρ_k) / Tr(M_k ρ_avg)
  where ρ_avg = Σ p_i ρ_i is the average state
- Global measurements optimize over all POVMs
- Separable measurements optimize only over separable POVMs

### 3. Semi-Device-Independent Certification

**Key result:** Verifying achievable confidence in measurement outcomes certifies that global measurements were used — i.e., semi-device-independent certification of NLWE.

**Why semi-device-independent:**
- No assumptions about the internal workings of measurement devices needed
- Only assumes the dimension of the quantum system
- Certification based solely on observed confidence statistics
- Works even with non-unit detection efficiencies (relies only on detected outcomes)

### 4. Experimental Feasibility

**Advantages over existing NLWE demonstrations:**
- Maximum-confidence measurements rely only on detected outcomes
- Robust to non-unit detection efficiency
- Compatible with present-day quantum measurement devices
- No need for perfect state preparation or detection

## Implementation Steps

1. **Define separable state ensemble**: Specify the set of product states and their prior probabilities
2. **Compute average state**: ρ_avg = Σ p_i ρ_i
3. **Find optimal global confidence**: Solve SDP for maximum confidence over all POVMs
4. **Find optimal separable confidence**: Constrain to separable POVMs (computationally harder)
5. **Compare confidences**: C_global > C_separable proves NLWE
6. **Design certification protocol**: Use observed confidence to certify global measurements were performed

## Pitfalls

- **Confidence vs success rate**: Maximum confidence is NOT the same as minimum error. Confidence conditions on the outcome being declared; success rate averages over all outcomes
- **Separable measurement optimization**: Finding optimal separable measurements is generally NP-hard — may require numerical relaxation or heuristic approaches
- **Detection efficiency assumption**: While robust to non-unit efficiency, the protocol assumes detected outcomes are representative (no systematic bias in which outcomes are detected)
- **Ensemble selection**: Not all ensembles of separable states exhibit NLWE — the ensemble must be carefully chosen

## Verification

- For known NLWE ensembles (e.g., domino states, rotated Bell basis product states), verify C_global > C_separable
- Cross-check with minimum-error discrimination results as a sanity check
- Ensure confidence values are bounded: 1/d ≤ C_k ≤ 1 where d is the Hilbert space dimension

## Activation Keywords

- NLWE nonlocality without entanglement
- maximum-confidence discrimination quantum
- semi-device-independent certification quantum
- separable state discrimination
- global vs separable measurement
- confidence-based quantum state identification
- quantum measurement certification
- product state ensemble nonlocality