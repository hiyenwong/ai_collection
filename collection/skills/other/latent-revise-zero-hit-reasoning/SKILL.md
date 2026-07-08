---
name: latent-revise-zero-hit-reasoning
description: "LatentRevise — First-order latent revision method that recovers training signal from zero-hit prompts in RLVR. Optimizes input embeddings of failed reasoning prefixes under dual gradients (away from failed continuation, toward gold answer), constrained to vocabulary embedding convex hull."
tags: [RLVR, reinforcement-learning, reasoning, latent-optimization, zero-hit, training-data-augmentation, SFT]
source: "arXiv:2606.29938"
trigger: "RLVR, zero-hit prompts, reasoning failure, latent revision, failed rollouts, training signal recovery, hard prompts"
---

# LatentRevise: Learning from Zero-Hit Reasoning

## Problem
RLVR (Reinforcement Learning with Verifiable Rewards) is bottlenecked by hard prompts where correct trajectories have low probability. Within practical sampling budgets, these prompts yield zero correct rollouts, leaving the policy update with little useful signal.

**Key insight**: Failed rollouts are informative — they expose where the model's reasoning went wrong.

## Core Methodology

### Latent Revision Framework
Given a failed rollout and the gold answer as anchor:

1. **Identify revision point**: Take the reasoning prefix (tokens before the failure point)
2. **Optimize input embeddings** under two complementary gradients:
   - **Away gradient**: Push prefix embedding away from the failed continuation direction
   - **Toward gradient**: Pull prefix embedding toward the gold answer direction
3. **Constraint**: Optimization stays within the **convex hull of vocabulary embeddings**
   - Ensures each update moves toward a real token embedding, not arbitrary feature direction
   - Prevents drift into meaningless latent space

### First-Order Approximation
- Optimizes input embeddings (not model weights) — fast, no backprop through transformer
- Uses gradient of loss w.r.t. embedding layer
- Revised prefix serves as new starting point for sampling

## Implementation Pattern
```python
def latent_revise(model, failed_prefix_ids, gold_answer_ids, lr=0.01, steps=10):
    # Get embedding of failed prefix
    prefix_emb = model.embed(failed_prefix_ids).detach().requires_grad_(True)
    optimizer = torch.optim.Adam([prefix_emb], lr=lr)
    
    for _ in range(steps):
        optimizer.zero_grad()
        
        # Forward from revised prefix
        logits = model.forward_from_embedding(prefix_emb)
        
        # Dual gradient objective
        loss_away = -log_prob(logits, failed_continuation)  # move away from failure
        loss_toward = -log_prob(logits, gold_answer)         # move toward gold
        
        # Combined: minimize away, minimize toward (both negative log-prob)
        # But we want to move AWAY from failed, so:
        loss = loss_away - loss_toward  # or weighted combination
        
        loss.backward()
        
        # Project onto convex hull of vocabulary embeddings
        with torch.no_grad():
            prefix_emb.data = project_to_vocab_hull(prefix_emb.data, model.embed.weight)
        
        optimizer.step()
    
    # Sample new continuation from revised prefix
    revised_continuation = model.sample(prefix_emb, max_tokens=...)
    return revised_continuation
```

## Results
- Revised prefixes produce continuations that **lengthen** and exhibit **self-reflection**
- Reach correct answers missed by original rollouts
- When used as training data, improve SFT and RLVR on math benchmarks over standard baselines
- No additional human annotation or reward model needed

## Key Insights
1. **Convex hull constraint is critical**: Without it, optimization drifts into meaningless regions
2. **Failed rollouts contain signal**: The model knows what went wrong; latent revision extracts it
3. **First-order is sufficient**: No need for expensive second-order or full backprop
4. **Sampling frontier**: Zero-hit prompts are where new reasoning behavior is most valuable

## When to Use
- RLVR training on hard math/code problems with sparse correct samples
- Data augmentation for reasoning tasks where correct examples are scarce
- Bootstrapping from failed attempts in self-play or iterative training

## Pitfalls
- Convex hull projection is expensive for large vocabularies; approximate with nearest neighbors
- Too many revision steps → prefix drifts too far from original semantics
- Works best when failure is "local" (one wrong step), not global misunderstanding
- Requires access to gold answer; not applicable to open-ended generation without verifiers

## Activation
LatentRevise, RLVR, zero-hit reasoning, latent revision, failed rollouts, training signal recovery, hard prompts, reasoning augmentation
