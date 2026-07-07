---
name: ai-math-discovery
description: >
  AI-assisted mathematical discovery methodology. Use when: (1) collaborating with LLMs to generate
  mathematical conjectures, inequalities, bounds, or proofs; (2) verifying AI-generated mathematical results;
  (3) structuring human-AI mathematical research workflows; (4) exploring AI's role in mathematical research;
  (5) analyzing mathematical inequality patterns (Gaussian perimeter, moment comparison, autoconvolution,
  Sidon sets, Szarek's inequality). Trigger words: AI math discovery, Grokability, mathematical conjecture,
  inequality bound, AI-assisted proof, 数学发现, AI数学, 不等式.
---

# AI-Assisted Mathematical Discovery

## Overview

Methodology for collaborative mathematical discovery between humans and LLMs, based on the "Grokability in
five inequalities" framework (arXiv:2605.05193). AI generates mathematical conjectures and bounds; humans
verify and formalize proofs.

## Core Workflow

### Phase 1: Conjecture Generation
- Frame the mathematical problem with precise definitions
- Ask LLM to propose conjectures with supporting intuition
- Request numerical/experimental evidence for conjectures
- Iterate: refine conjecture based on LLM reasoning

### Phase 2: Verification
- Independently verify all AI-generated claims
- Check edge cases and boundary conditions
- Formalize proofs using standard mathematical rigor
- Identify gaps where AI reasoning was incomplete

### Phase 3: Publication
- Structure results in standard mathematical paper format
- Credit AI collaboration transparently
- Include both conjecture and proof

## Key Mathematical Patterns

### Inequality Discovery Patterns
- **Gaussian perimeter bounds**: Maximize perimeter of convex sets in R^n
- **Moment comparison**: L2-L1 inequalities on discrete domains (Hamming cube)
- **Autoconvolution**: Strengthened bounds for f*f type operations
- **Sidon sets**: Asymptotic bounds on g-Sidon set sizes in {1,...,n}
- **Szarek-type**: Optimal balanced inequalities for norm comparisons

### Prompt Templates for LLM Collaboration

```
Given [mathematical object], find the tightest known/provable bound for [quantity].
Provide: (1) conjectured bound, (2) heuristic justification, (3) known related results.
```

```
Improve the following inequality: [current inequality].
Suggest: (1) tighter constant, (2) additional conditions, (3) equality cases.
```

### Verification Checklist
- [ ] Conjecture stated precisely with all assumptions
- [ ] Numerical evidence for small cases (n=1,2,3,...)
- [ ] Asymptotic behavior matches intuition
- [ ] Known special cases are recovered
- [ ] Proof technique identified and validated
- [ ] Equality/ extremal cases characterized
- [ ] Comparison with existing literature

## Error Modes

### AI Hallucination in Math
- LLM may generate plausible-looking but false statements
- Always verify claims independently
- Check references the LLM cites actually exist

### Overfitting to Examples
- LLM may generalize from limited numerical examples
- Test conjectures across different parameter regimes
- Look for counterexamples systematically

### Suboptimal Bounds
- AI often finds loose bounds first
- Iterate: "Can this bound be improved? What prevents it?"
- Compare with known results in literature

## Resources

- **Paper**: "Grokability in five inequalities" (arXiv:2605.05193)
- **Authors**: Paata Ivanisvili, Xinyuan Xie
- **Categories**: math.PR, cs.AI, math.AP, math.CA, math.FA
