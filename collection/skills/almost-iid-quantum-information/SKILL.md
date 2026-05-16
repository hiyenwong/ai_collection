---
name: almost-iid-quantum-information
description: >
  Methodology for analyzing almost i.i.d. (independent and identically distributed) quantum states
  using quantum Wasserstein distance, k-body marginals, and normalized information theory.
  Based on arXiv 2605.15114. Use when: analyzing quantum information sources, evaluating
  quantum state similarity beyond i.i.d. assumptions, designing quantum communication protocols,
  or working with non-i.i.d. quantum data. Covers three hierarchical definitions of almost i.i.d.
  states and their strict separation properties.
---

# Almost-IID Quantum Information Theory

## Description
Analysis of quantum information sources that relax the strict i.i.d. assumption.
Three alternative definitions form a strict hierarchy: k-body marginals (loosest),
quantum Wasserstein distance (intermediate), and Mazzola et al. notion (strictest).

## Activation Keywords
- almost iid quantum
- quantum wasserstein distance
- quantum information theory non-iid
- quantum state similarity
- quantum source analysis
- 量子信息论
- 量子态相似性
- quantum marginal analysis
- quantum resource distillation

## Tools Used
- `exec`: Run quantum information analysis scripts
- `read`: Read paper content and mathematical proofs
- `web_search`: Find related quantum information papers

## Instructions for Agents

### Step 1: Understand the Problem
Traditional quantum information theory assumes i.i.d. sources, which is too stringent
for real quantum systems. This methodology provides three relaxed alternatives.

### Step 2: Three Hierarchical Definitions
1. **k-body marginals** - Compare reduced density matrices of k-body subsystems
   - Loosest definition, allows more variation in global state
2. **Quantum Wasserstein distance** - Distance based on quantum transport cost
   - Intermediate strictness, physically motivated
3. **Mazzola et al. notion** - Based on typical subspace analysis
   - Strictest definition, closest to i.i.d.

### Step 3: Strict Separation
The paper proves these three notions are strictly separated:
- Mazzola et al. → Quantum Wasserstein → k-body marginals
- Each implication is one-way; explicit counterexamples exist

### Step 4: Application to Quantum Resource Distillation
Universal distillation rates are achievable without knowledge of input state,
certifying robustness of quantum resource distillation. This applies to:
- Entanglement purification under non-entangling maps
- Rates governed by regularized relative entropy of entanglement

## Error Handling
### Quantum Wasserstein Calculation Issues
If Wasserstein distance calculation fails:
- Fall back to k-body marginal comparison
- Use trace distance as upper bound

### Non-IID Source Analysis
For sources that don't fit any definition:
- Check if system size allows polynomial vs exponential subspace growth
- Verify translation symmetry constraints

## Best Practices
1. Use the loosest definition that suffices for the application
2. When designing protocols, account for non-i.i.d. behavior explicitly
3. Consider symmetry constraints when analyzing state properties

## Examples
### Example 1: Source Analysis
```
User: "分析这个量子信源是否接近i.i.d."

Agent: 
1. Check k-body marginals match for small k
2. Compute quantum Wasserstein distance
3. Determine which definition the source satisfies
```

## Resources
- arXiv: 2605.15114 - "New approaches to almost i.i.d. information theory"
- arXiv: 2605.15174 - "Universal quantum resource distillation"

## Related Skills
- quantum-information-protocol-analyzer: Analyze quantum protocols
- quantum-error-correction-methods: QEC patterns
- quantum-ml-patterns: QML research patterns

## Notes
- Paper proves strict hierarchy with explicit counterexamples
- Translation-invariant subspace dimension grows polynomially,
  while full subspace grows exponentially - key to LRE in mixed states
