---
name: reasoning-decision-timing
description: Understanding when LLM reasoning models make decisions - before or during chain-of-thought. Use when discussing reasoning model interpretability, AI safety, chain-of-thought reliability, or the philosophical implications of LLM decision-making processes. Triggers on questions about "reasoning models decide first", "chain-of-thought rationalization", "LLM interpretability", or "reasoning timing".
---

# Reasoning Decision Timing

Key findings from "Therefore I am. I Think" (arXiv:2604.01202) by Esakkivel et al.

## Core Discovery

Reasoning models encode detectable decisions **before** chain-of-thought generation, challenging the assumption that thinking precedes deciding.

## Key Evidence

1. **Linear probes** decode tool-calling decisions from pre-generation activations with very high confidence, even before any reasoning tokens are produced.

2. **Activation steering** perturbing the decision direction:
   - Leads to inflated deliberation
   - Flips behavior in 7-79% of examples (depending on model/benchmark)

3. **Behavioral analysis**: When steering changes the decision, chain-of-thought often **rationalizes** the flip rather than resisting it.

## Implications

### For Interpretability
- Chain-of-thought may be post-hoc rationalization, not faithful explanation
- Early decisions shape downstream reasoning
- Current oversight mechanisms may be misaligned with actual behavior

### For AI Safety
- If decisions are encoded before deliberation, transparency mechanisms based on reading reasoning traces may be fundamentally flawed
- Safety interventions should target early activation patterns, not just output text

### For Model Design
- Reasoning models may not actually "think then decide"
- Architecture may need redesign for truly deliberative decision-making

## Practical Applications

When evaluating reasoning model outputs:
- Don't assume chain-of-thought reflects actual decision process
- Consider probing early activations for decision detection
- Be cautious about relying on reasoning transparency for safety

## Reference

arXiv:2604.01202 - "Therefore I am. I Think" by Esakkivel Esakkiraja et al.
Submitted: April 1, 2026