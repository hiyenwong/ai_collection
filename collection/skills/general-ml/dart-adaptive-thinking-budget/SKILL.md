---
name: dart-adaptive-thinking-budget
description: Training-free routing framework for hybrid reasoning models. Uses draft agreement signals to adaptively allocate thinking budgets without labeled data or gradient updates.
trigger_words:
  - thinking budget
  - adaptive reasoning
  - draft agreement
  - hybrid reasoning
  - reasoning allocation
version: 1.0
arxiv: 2606.23181v1
authors: Jungseob Lee, Seongtae Hong, Seungjun Lee, et al.
date: 2026-06-22
categories: cs.AI, cs.CL
---

# DART: Draft-Agreement Routing for Training-Free Adaptive Thinking Budgets

**Core Insight:** Training-free routing that samples two cheap no-think drafts, accepts direct answering when drafts agree, and predicts thinking budget from draft entropy when they disagree.

## Key Methodology

### Three-Stage Framework

1. **Draft Sampling**: Generate two cheap "no-think" responses
2. **Agreement Detection**: 
   - If drafts agree → accept direct answer (no extended thinking needed)
   - If drafts disagree → predict thinking budget from draft entropy
3. **Budget Prediction**: Use entropy signal to allocate thinking tokens

### Benefits
- **No training data required** - fully training-free
- **No gradient updates** - no fine-tuning needed
- **Exponential inference reduction** - easy problems skip reasoning entirely
- **Cross-scale applicability** - works on 0.6B to 32B models

## Implementation Pattern

```python
def dart_routing(query, model):
    # Stage 1: Sample two cheap drafts (no thinking)
    draft_1 = model.generate(query, thinking_budget=0)
    draft_2 = model.generate(query, thinking_budget=0)
    
    # Stage 2: Check agreement
    agreement_score = compute_agreement(draft_1, draft_2)
    
    if agreement_score > threshold:
        # Drafts agree → accept direct answer
        return draft_1
    else:
        # Stage 3: Predict thinking budget from entropy
        entropy = compute_draft_entropy(draft_1, draft_2)
        thinking_budget = predict_budget_from_entropy(entropy)
        
        # Generate with predicted budget
        return model.generate(query, thinking_budget=thinking_budget)
```

## Performance Gains
- Math reasoning: **+9.0 points** on Olympiad problems, **15-69%** token reduction
- Code reasoning: **+22.5 points** accuracy, **51-63%** token reduction

## When to Use
- Hybrid reasoning models with thinking/non-thinking modes
- Adaptive inference budget allocation
- Training-free routing decisions
- API-only hosted models (no gradient access)

## Key Insight
The **draft agreement signal** is a free complexity indicator - disagreement reveals uncertainty that warrants extended reasoning.

---

## References
- arXiv: [2606.23181v1](https://arxiv.org/abs/2606.23181v1)
- Authors: Jungseob Lee et al. (10 authors)
- Categories: cs.AI, cs.CL